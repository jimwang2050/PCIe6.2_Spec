#!/usr/bin/env python3
"""PCIe 6.2 中文版 Markdown 质量检查（lint）。

检查项分三级：
  error    结构正确性问题（标题编号/锚点不一致、链接失效、占位符缺失原文）
  warning  排版一致性问题（标题尾 §、图注格式混用、重复分隔线、td 内代码块、图片宽度等）
  info     翻译风格问题（中文半角标点、双语行不完整等）

用法：
  python3 tools/lint_md.py                     # 控制台摘要
  python3 tools/lint_md.py --json report.json  # 另存完整报告
  python3 tools/lint_md.py --strict            # warning 也视为失败
  python3 tools/lint_md.py --baseline tools/lint_baseline.json   # 与基线对比
  python3 tools/lint_md.py --write-baseline tools/lint_baseline.json  # 写入基线
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT_DEFAULT = Path(__file__).resolve().parent.parent
GLOB = 'PCIe6.2_Spec_ch*.md'
IMAGE_WIDTH = '700'

SEVERITY_ORDER = {'error': 0, 'warning': 1, 'info': 2}

PLACEHOLDER_PATTERNS = [
    (r'Reserved for future definition\.', '英文占位符 Reserved for future definition'),
    (r'保留供未来定义使用', '中文占位符 保留供未来定义使用'),
    (r'参见上一节内容', '中文占位符 参见上一节内容'),
    (r'说明保留位', '中文占位符 说明保留位'),
    (r'Reserved for [A-Z][A-Za-z ]{3,60} description\.', '英文占位符 Reserved for ... description'),
]

_TRAIL = r'(?: *<!--[^>]*-->)?$'
CAPTION_FIG_SINGLE = re.compile(r'^\*\*Figure [\d-]+\. .*\| 图 [\d-]+\. .*\*\*' + _TRAIL, re.M)
CAPTION_FIG_EN = re.compile(r'^\*\*Figure [\d-]+\. .*\*\*' + _TRAIL, re.M)
CAPTION_TBL_SINGLE = re.compile(r'^\*\*Table [\d-]+\. .*\| 表 [\d-]+\. .*\*\*' + _TRAIL, re.M)
CAPTION_TBL_EN = re.compile(r'^\*\*Table [\d-]+\. .*\*\*' + _TRAIL, re.M)

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
HEADING_AFTER_ANCHOR = re.compile(r'<a id="sec-([0-9-]+)"></a>\s*\n#{2,3} ([0-9.]+)?')
TOC_LINK = re.compile(r'\[[^\]]*\]\(#([^)]+)\)')
BILINGUAL_ROW = re.compile(
    r'<tr>(?:\s*<!--[^>]*-->)*\s*<td>(.*?)</td>(?:\s*<!--[^>]*-->)*\s*<td[^>]*background-color:#e8e8e8[^>]*>(.*?)</td>(?:\s*<!--[^>]*-->)*\s*</tr>',
    re.S,
)


@dataclass
class Issue:
    file: str
    severity: str
    code: str
    detail: str
    line: int = 0


@dataclass
class FileStat:
    issues: list[Issue] = field(default_factory=list)
    metrics: Counter = field(default_factory=Counter)

    def add(self, severity: str, code: str, detail: str, line: int = 0, count: int = 1):
        self.issues.append(Issue('', severity, code, detail, line))
        self.metrics[code] += count


def strip_code(text: str) -> str:
    """去掉围栏代码与行内代码，避免误报。"""
    text = re.sub(r'```.*?```', lambda m: '\n' * m.group(0).count('\n'), text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def normalize_sec(value: str) -> str:
    return value.strip().rstrip('.')


def collect_headings(lines: list[str], levels: str = '2,3') -> list[tuple[int, str]]:
    """收集真正的文档标题：跳过表格单元格内的标题与图表标题。"""
    out = []
    depth = 0
    pattern = re.compile('^#{' + levels + '} ')
    caption = re.compile(r'^#{2,4}\s+(Figure|Table|图|表)[\s-]')
    for i, line in enumerate(lines):
        if depth == 0 and pattern.match(line) and not caption.match(line):
            out.append((i + 1, line))
        depth += len(re.findall(r'<td[ >]', line)) - line.count('</td>')
        depth = max(depth, 0)
    return out


def lint_file(path: Path, siblings: dict[str, set[str]]) -> FileStat:
    stat = FileStat()
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    name = path.name

    anchors = set(ANCHOR_RE.findall(text))

    # 1) 标题编号 ↔ 锚点
    for m in HEADING_AFTER_ANCHOR.finditer(text):
        sec_raw, heading_num = m.group(1), m.group(2)
        if heading_num is None:
            continue
        sec = normalize_sec(sec_raw.replace('-', '.'))
        num = normalize_sec(heading_num)
        if sec == num:
            continue
        # 章根锚点 sec-7-0 对应标题 "7."，属于正常
        if re.fullmatch(r'\d+-0', sec_raw) and num == sec_raw.split('-')[0]:
            continue
        line = text[:m.start()].count('\n') + 1
        # 续页别名：sec-7-5-1-1-4-2 挂在 7.5.1.1.4 标题前，且同名基锚点存在
        base = sec_raw.rsplit('-', 1)[0]
        if num == base.replace('-', '.') and f'<a id="sec-{base}"></a>' in text:
            stat.add('info', 'anchor_continuation_alias',
                     f'subsection anchor sec-{sec_raw} 指向父级标题 {num}', line)
            continue
        # 别名式锚点（sec-7-9-0 → 7.9）只提示，不作为错误
        severity = 'warning' if sec_raw.endswith('-0') else 'error'
        stat.add(severity, 'heading_anchor_mismatch',
                 f'锚点 sec-{sec_raw} 对应标题编号 {heading_num.strip()}', line)

    # 2) 内部链接可达性（区分同文件 / 跨拆分文件）
    for m in TOC_LINK.finditer(text):
        target = m.group(1)
        if target.startswith(('http', 'mailto')):
            continue
        if target in anchors or target == '':
            continue
        others = siblings.get(target)
        line = text[:m.start()].count('\n') + 1
        if others:
            stat.add('info', 'cross_file_link',
                     f'#{target} 不在本文件，出现在 {", ".join(sorted(others))}', line)
        else:
            stat.add('error', 'broken_link', f'#{target} 无对应锚点', line)

    # 3) 标题尾部 §
    for lineno, line in collect_headings(lines, '2,4'):
        if line.rstrip().endswith('§'):
            stat.add('warning', 'heading_trailing_sect', line.strip()[:90], lineno)

    # 4) 图/表标题格式混用
    fig_single = CAPTION_FIG_SINGLE.findall(text)
    fig_en = [x for x in CAPTION_FIG_EN.findall(text) if '| 图 ' not in x]
    tbl_single = CAPTION_TBL_SINGLE.findall(text)
    tbl_en = [x for x in CAPTION_TBL_EN.findall(text) if '| 表 ' not in x]
    # 纯英文表注为既定写法（ch07 寄存器表），不计入双行格式混用，单列信息项
    tbl_en_only = [x for x in tbl_en if not re.search(r'[一-鿿]', x)]
    tbl_en = [x for x in tbl_en if re.search(r'[一-鿿]', x)]
    stat.metrics['caption_fig_single'] = len(fig_single)
    stat.metrics['caption_fig_two_line'] = len(fig_en)
    stat.metrics['caption_tbl_single'] = len(tbl_single)
    stat.metrics['caption_tbl_two_line'] = len(tbl_en)
    stat.metrics['caption_tbl_en_only'] = len(tbl_en_only)
    if tbl_en_only:
        stat.add('info', 'caption_tbl_en_only',
                 f'{len(tbl_en_only)} 条纯英文表注（既定写法）', count=0)
    if fig_single and fig_en:
        stat.add('warning', 'caption_format_mixed',
                 f'图注单行 {len(fig_single)} 条、双行 {len(fig_en)} 条并存')
    if tbl_single and tbl_en:
        stat.add('warning', 'caption_format_mixed',
                 f'表注单行 {len(tbl_single)} 条、双行 {len(tbl_en)} 条并存')

    # 5) 连续分隔线
    for m in re.finditer(r'\n---\n(?:[ \t]*\n)+---\n', text):
        stat.add('warning', 'duplicate_hr', '相邻两条 --- 分隔线', text[:m.start()].count('\n') + 2)

    # 6) 表格单元格内的围栏代码块
    for m in re.finditer(r'<td[^>]*>\s*\n\s*```', text):
        stat.add('warning', 'code_block_in_table_cell', 'td 内使用 fenced code block',
                 text[:m.start()].count('\n') + 1)

    # 7) 图片：缺失、宽度、引用块（按文件汇总，避免刷屏）
    missing_imgs, width_imgs, unquoted_imgs = [], [], []
    td_depth, td_lines = 0, set()
    for i, ln in enumerate(lines):
        if td_depth > 0:
            td_lines.add(i + 1)
        td_depth += len(re.findall(r'<td[ >]', ln)) - ln.count('</td>')
        td_depth = max(td_depth, 0)
    for m in re.finditer(r'<img[^>]*>', text):
        tag = m.group(0)
        line = text[:m.start()].count('\n') + 1
        src_m = re.search(r'src="([^"]+)"', tag)
        if src_m:
            src = src_m.group(1)
            if src.startswith(('http://', 'https://')):
                pass
            elif not (path.parent / src).exists():
                missing_imgs.append((line, src))
        if f'width="{IMAGE_WIDTH}"' not in tag:
            width_imgs.append((line, tag[:60]))
        if not lines[line - 1].lstrip().startswith('>') and line not in td_lines:
            unquoted_imgs.append(line)

    for line, src in missing_imgs[:20]:
        stat.add('error', 'missing_image', src, line)
    if len(missing_imgs) > 20:
        stat.add('error', 'missing_image', f'另有 {len(missing_imgs) - 20} 张缺失')
    if width_imgs:
        line, tag = width_imgs[0]
        stat.add('warning', 'image_width',
                 f'{len(width_imgs)} 张宽度不是 {IMAGE_WIDTH}，例：{tag}', line, len(width_imgs))
    if unquoted_imgs:
        stat.add('info', 'image_not_quoted',
                 f'{len(unquoted_imgs)} 张图片不在引用块内', unquoted_imgs[0], len(unquoted_imgs))

    # 8) 占位符
    for pattern, label in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pattern, text):
            stat.add('error', 'placeholder_text', label,
                     text[:m.start()].count('\n') + 1)

    # 8.1) 重复标题（排除 (continued) 续页标记；排除表格单元格内的标题）
    headings = collect_headings(lines)
    seen: dict[str, list[int]] = defaultdict(list)
    for lineno, h in headings:
        seen[h.strip()].append(lineno)
    for h, linenos in seen.items():
        if len(linenos) > 1 and not re.search(r'\(continued\)|（续）|\(续', h):
            stat.add('warning', 'duplicate_heading',
                     f'{len(linenos)} 次重复：{h[:60]}', linenos[0])

    # 8.2) 空章节（标题后无正文、无图、无表）
    def has_content(body: list[str]) -> bool:
        joined = '\n'.join(body)
        if '<img' in joined or '<table' in joined:
            return True
        if re.search(r'^\|.*\|', joined, re.M):
            return True
        if '```' in joined and len(joined.strip()) > 12:
            return True
        cleaned = re.sub(r'<!--.*?-->', '', joined, flags=re.S)
        cleaned = re.sub(r'</?a[^>]*>|<[^>]+>', '', cleaned)
        cleaned = re.sub(r'^---$', '', cleaned, flags=re.M)
        return len(cleaned.strip()) > 20

    for k, (lineno, _) in enumerate(headings):
        end = headings[k + 1][0] - 1 if k + 1 < len(headings) else len(lines)
        body = lines[lineno:end]
        if has_content(body):
            continue
        cur = lines[lineno - 1]
        cur_num = (re.match(r'^#{2,3}\s+([\d.]+)', cur) or [None, ''])[1]
        nxt = lines[end] if end < len(lines) else ''
        nxt_num = (re.match(r'^#{2,3}\s+([\d.]+)', nxt) or [None, ''])[1]
        # 只有子节、没有正文的容器章节属于正常结构
        if cur_num and nxt_num.startswith(cur_num + '.'):
            continue
        # 中英文各占一行、内容在同一双语表格里的标题对
        if cur_num and nxt_num == cur_num:
            cur_cjk = len(re.findall(r'[\u4e00-\u9fff]', cur))
            nxt_cjk = len(re.findall(r'[\u4e00-\u9fff]', nxt))
            if (cur_cjk == 0) != (nxt_cjk == 0):
                stat.add('info', 'heading_bilingual_split',
                         f'中英标题分成两行：{cur.strip()[:50]}', lineno)
                continue
        stat.add('warning', 'empty_section', cur.strip()[:80], lineno)

    # 9) 双语行完整性
    rows = BILINGUAL_ROW.findall(text)
    en_only = zh_only = both_empty = imbalanced = 0
    for en, zh in rows:
        et = re.sub(r'<[^>]+>', '', en).strip()
        zt = re.sub(r'<[^>]+>', '', zh).strip()
        if et and not zt:
            en_only += 1
        elif zt and not et:
            zh_only += 1
        elif not et and not zt:
            both_empty += 1
        elif len(et) > 100 and len(zt) < 20:
            imbalanced += 1
    stat.metrics.update(rows=len(rows), en_only=en_only, zh_only=zh_only,
                        both_empty=both_empty, imbalanced=imbalanced)
    if en_only:
        stat.add('info', 'bilingual_en_only', f'{en_only} 行缺少中文')
    if zh_only:
        stat.add('info', 'bilingual_zh_only', f'{zh_only} 行缺少英文')
    if both_empty:
        stat.add('info', 'bilingual_empty', f'{both_empty} 行中英皆空（多为分页注释）')
    if imbalanced:
        stat.add('info', 'bilingual_imbalanced', f'{imbalanced} 行中文明显少于英文')

    # 10) 中文语境半角标点
    no_code = strip_code(text)
    for code, pattern, label in [
        ('punct_halfwidth_comma', r'[\u4e00-\u9fff],[\u4e00-\u9fff]', '中文间使用半角逗号'),
        ('punct_halfwidth_colon', r'[\u4e00-\u9fff]:[\u4e00-\u9fff]', '中文间使用半角冒号'),
        ('punct_halfwidth_paren', r'[\u4e00-\u9fff]\([A-Za-z]', '中文后紧跟半角左括号'),
    ]:
        hits = list(re.finditer(pattern, no_code))
        if hits:
            sample = hits[0]
            line = no_code[:sample.start()].count('\n') + 1
            stat.add('info', code, f'{len(hits)} 处，例：{sample.group(0)}', line, len(hits))

    for issue in stat.issues:
        issue.file = name
    return stat


def collect_sibling_anchors(files: list[Path]) -> dict[str, set[str]]:
    """锚点 -> 出现的文件集合，用于识别拆分文件之间的跳转。"""
    mapping: dict[str, set[str]] = defaultdict(set)
    for f in files:
        for a in ANCHOR_RE.findall(f.read_text(encoding='utf-8')):
            mapping[a].add(f.name)
    return mapping


def summarize(results: dict[str, FileStat]) -> dict:
    totals = Counter()
    by_severity = Counter()
    by_code = Counter()
    for stat in results.values():
        totals.update(stat.metrics)
        for issue in stat.issues:
            by_severity[issue.severity] += 1
            by_code[issue.code] += 1
    # 聚合型检查项（按发生次数统计）优先使用 metrics 中的真实次数
    for code in list(by_code):
        if totals.get(code):
            by_code[code] = totals[code]
    return {
        'files': {name: {'metrics': dict(sorted(s.metrics.items())),
                         'issues': len(s.issues)} for name, s in sorted(results.items())},
        'totals': dict(sorted(totals.items())),
        'by_severity': dict(by_severity),
        'by_code': dict(sorted(by_code.items())),
    }


def print_summary(results: dict[str, FileStat], summary: dict) -> None:
    print('=' * 78)
    print('PCIe 6.2 Markdown Lint')
    print('=' * 78)
    for name, stat in sorted(results.items()):
        counts = Counter(i.severity for i in stat.issues)
        flag = 'FAIL' if counts['error'] else ('WARN' if counts['warning'] else ' OK ')
        print(f'[{flag}] {name[:52]:<52} error={counts["error"]:<3} '
              f'warning={counts["warning"]:<3} info={counts["info"]:<3}')

    print('-' * 78)
    sev = summary['by_severity']
    print(f"合计: error={sev.get('error', 0)}  warning={sev.get('warning', 0)}  "
          f"info={sev.get('info', 0)}")
    print('按检查项:')
    for code, n in sorted(summary['by_code'].items(), key=lambda kv: -kv[1]):
        print(f'  {code:<34} {n}')

    print('关键指标:')
    t = summary['totals']
    for key in ['rows', 'en_only', 'zh_only', 'both_empty', 'imbalanced',
                'caption_fig_single', 'caption_fig_two_line',
                'caption_tbl_single', 'caption_tbl_two_line']:
        if key in t:
            print(f'  {key:<28} {t[key]}')


def main() -> int:
    parser = argparse.ArgumentParser(description='PCIe 6.2 Markdown lint')
    parser.add_argument('--root', default=str(ROOT_DEFAULT))
    parser.add_argument('--json', dest='json_path')
    parser.add_argument('--strict', action='store_true', help='warning 也视为失败')
    parser.add_argument('--baseline', help='与基线 JSON 对比，指标恶化则失败')
    parser.add_argument('--write-baseline', help='写入基线 JSON')
    parser.add_argument('--max-issues', type=int, default=3000,
                        help='JSON 中单个检查项最多输出的明细条数')
    args = parser.parse_args()

    root = Path(args.root)
    files = sorted(root.glob(GLOB))
    if not files:
        print(f'未找到 {GLOB}：{root}', file=sys.stderr)
        return 2

    siblings = collect_sibling_anchors(files)
    results = {f.name: lint_file(f, siblings) for f in files}
    summary = summarize(results)

    issues = []
    per_code = Counter()
    for name, stat in results.items():
        for issue in stat.issues:
            per_code[issue.code] += 1
            if per_code[issue.code] <= args.max_issues:
                issues.append({
                    'file': issue.file, 'line': issue.line,
                    'severity': issue.severity, 'code': issue.code,
                    'detail': issue.detail,
                })

    report = {**summary,
              'issues': sorted(issues, key=lambda x: (SEVERITY_ORDER[x['severity']], x['file'], x['line']))}

    print_summary(results, summary)

    if args.json_path:
        Path(args.json_path).write_text(json.dumps(report, ensure_ascii=False, indent=1),
                                        encoding='utf-8')
        print(f'\nJSON 报告: {args.json_path}')

    if args.write_baseline:
        baseline = {'totals': report['totals'], 'by_code': report['by_code'],
                    'by_severity': report['by_severity']}
        Path(args.write_baseline).write_text(json.dumps(baseline, ensure_ascii=False, indent=1),
                                             encoding='utf-8')
        print(f'基线已写入: {args.write_baseline}')

    failed = report['by_severity'].get('error', 0) > 0
    if args.strict and report['by_severity'].get('warning', 0) > 0:
        failed = True

    if args.baseline:
        base = json.loads(Path(args.baseline).read_text(encoding='utf-8'))
        regress = []
        for key, old in base.get('totals', {}).items():
            new = report['totals'].get(key, 0)
            if isinstance(old, int) and new > old:
                regress.append((key, old, new))
        for code, old in base.get('by_code', {}).items():
            new = report['by_code'].get(code, 0)
            if new > old:
                regress.append((code, old, new))
        if regress:
            failed = True
            print('\n相对基线恶化:')
            for key, old, new in regress:
                print(f'  {key}: {old} -> {new}')
        else:
            print('\n相对基线无恶化')

    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
