#!/usr/bin/env python3
"""
对 12 章中所有 ZH td 缺 img 的情况,自动从 EN td 复制 img 引用到 ZH td。

策略:
1. 扫描所有 <tr><td>EN</td><td style="...">ZH</td></tr> 对
2. 当 EN 包含 img 但 ZH 不包含时,在 ZH 中插入 img 引用
3. img 引用前加上中文图标题 (从 EN 标题提取或保持 EN 标题)
"""
import re
from pathlib import Path

ROOT = Path('.')
md_files = sorted(ROOT.glob('PCIe6.2_Spec_ch*_*.md'))

# 找配对: <tr><td>EN</td><td style="background-color:#e8e8e8">ZH</td></tr>
# 不在 <table> 内
pair_re = re.compile(r'<tr>(?:(?!<table>).)*?</tr>', re.DOTALL)

# 抓 EN 和 ZH 内容的正则
td_pair_re = re.compile(
    r'<td>(.*?)</td>\s*<td style="background-color:#e8e8e8">(.*?)</td>',
    re.DOTALL
)

# img 标签
img_re = re.compile(r'(<img\s+src="[^"]+"[^>]*>)')

# EN 中的 Figure 标题 (从 img 前一行)
fig_cap_re = re.compile(
    r'(?:>\s*\*\*Figure\s+(\d+)-(\d+)\.?\s*\*?\*?\s*([^*\n]*?)\*?\*?\s*\n)?',
    re.MULTILINE
)


def fix_pair(tr_match):
    """If EN has img but ZH doesn't, copy img to ZH. Return (new_tr, was_fixed)."""
    tr = tr_match.group(0)
    m = td_pair_re.search(tr)
    if not m:
        return tr, False
    en, zh = m.group(1), m.group(2)

    en_imgs = img_re.findall(en)
    zh_imgs = img_re.findall(zh)

    if not en_imgs or zh_imgs:
        return tr, False  # no fix needed

    # Find ZH closing position
    zh_text = re.sub(r'<[^>]+>', '', zh).strip()
    if len(zh_text) < 5:
        return tr, False  # ZH empty, can't reliably add

    # Find the img to insert (use first EN img, replace src path)
    first_img = en_imgs[0]
    # Insert the same img at the end of ZH (before </td>)
    new_zh = zh.rstrip()
    # Add blank line + img
    if not new_zh.endswith('\n'):
        new_zh += '\n'
    new_zh += '\n' + first_img + '\n'

    new_tr = tr.replace(zh, new_zh, 1)
    return new_tr, True


def main():
    total_fixed = 0
    for md in md_files:
        m = re.search(r'ch(\d{2})_', md.name)
        if not m: continue
        ch = int(m.group(1))
        with open(md) as f: s = f.read()

        new_s = s
        n_ch_fixed = 0
        # 逐个替换
        for tr_match in list(pair_re.finditer(s))[::-1]:  # reverse for stable indices
            new_tr, was_fixed = fix_pair(tr_match)
            if was_fixed:
                new_s = new_s.replace(tr_match.group(0), new_tr, 1)
                n_ch_fixed += 1

        if n_ch_fixed > 0:
            with open(md, 'w') as f: f.write(new_s)
            print(f'  Ch{ch:02d}: {n_ch_fixed} ZH imgs added')
            total_fixed += n_ch_fixed
    print(f'\nTotal ZH imgs added: {total_fixed}')


if __name__ == '__main__':
    main()
