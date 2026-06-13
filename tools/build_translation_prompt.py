#!/usr/bin/env python3
"""
Build translation prompt files for each chunk.

Each prompt file contains:
1. CXL 3.2 format spec (H1, section header, table layout, gray bg, anchor, fig refs)
2. Glossary terms (curated from CXL_zh)
3. Figure list for the chapter
4. The raw text to translate
5. Output path instruction

The sub-agent reads the prompt, translates, and writes the output_chunk_NNN.md file.
"""
import json
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHUNKS_DIR = OUT_ROOT / 'chunks'
PROMPTS_DIR = OUT_ROOT / 'prompts'
GLOSSARY_PATH = OUT_ROOT / 'glossary.json'
INDEX_PATH = OUT_ROOT / 'chapter_index.json'
PLAN_PATH = OUT_ROOT / 'chunk_plan.json'

PROMPTS_DIR.mkdir(exist_ok=True)

# === CXL 3.2 FORMAT TEMPLATE ===
# This is the canonical format every translated chunk must use.
FORMAT_TEMPLATE = r"""# CXL 3.2 中英对照翻译格式规范（必须严格遵守）

## 文档结构

每个翻译 chunk 是一组连续的 Section 段落。完整的章节文件由 1 个或多个 chunk 拼接而成。

### 1. 文件级 H1（只在第一个 chunk 写出，后续 chunk 跳过）

```markdown
# 📘 第 N 章　<Title> (Chapter N. <English>)

> 📄 **Source pages**: X–Y | 📁 **File**: `chapter_NN.md`
> 🎨 **Format**: 中英对照双语 · 图表原始保留 · 中文背景色灰色 · GitHub Flavored Markdown

---

## 📑 本章目录 (Table of Contents)
[TOC 由合并阶段自动生成,不要在 chunk 中重复]

## 🖼 本章图表 (Figures)
[Figure 列表由合并阶段自动生成,不要在 chunk 中重复]

## 📊 本章表格 (Tables)
[Table 列表由合并阶段自动生成,不要在 chunk 中重复]
```

### 2. 每个 Section 的双语格式

每个 Section 必须按下列 CXL 3.2 格式翻译:

```markdown
<a id="sec-N-X-Y"></a>
## N.X.Y Section | 中文小节标题

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

[英文原文]

</td>
<td style="background-color:#e8e8e8">

[中文翻译]

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---
```

**重要规则**:
- Section 编号 ID 格式: `sec-N-X-Y-Z`（根据实际层级），例如 `sec-1-0`, `sec-2-5-3`
- H2 标题格式: `## N.X Title | 中文标题`（层级对应原 spec）
- 英文单元格 + 中文单元格必须都是有效的 HTML，且中文单元格必须 `style="background-color:#e8e8e8"`
- 段落必须保留换行：每个 <td> 内的多段用空行分隔
- 列表、引用块、强调等 markdown 元素都保留

### 3. 表格翻译

```markdown
**Table N-X. Title | 表 N-X. 中文标题**

| Header 1 | Header 2 |
|----------|----------|
| ...      | ...      |
```

不要把表格放在 HTML <table> 内,使用标准 markdown 表格。

### 4. 图片引用

如果原文中出现 Figure 引用，例如:
```
[figures/chapter_07/fig_0400_1.png]
```

在 markdown 中嵌入:
```markdown
> **Figure N-X.** English caption
> <img src="figures/chapter_NN/fig_PPPP_1.png" width="700">
```

每个 chapter 的 figure 文件名列表在每个 chunk 提示中给出。
- 如果 chunk 内有 figure 引用,保留原文件名(包括 fig_PPPP_1.png 形式)
- 图片 alt/caption 必须双语

### 5. 翻译风格

- **首次出现的术语**: `EN (中文)` 对照,例如 `Flow Control (流控)`
- **后续出现**: 保留英文术语 (在中文中给出 EN 缩写)
- **协议名/寄存器字段/信号名**: 保留英文 (如 `TLP`, `Gen5`, `PERST`, `CFG_DONE`)
- **章节标题双语并列**: `## 2.5 Transaction Ordering | 事务排序`
- **数字、十六进制值、位宽**: 保持原样
- **页码引用 (§ Section X.Y)**: 保留原 spec 引用格式

### 6. 章节内容识别规则

源文本结构 (raw text):
```
=== Chapter N raw text ===
<<<PAGE_BREAK>>> page_XXX

<普通段落>

1.1 Section Title §

<Section 1.1 段落>

1.1.1 Sub-section Title §
```

识别方法:
- `<<<PAGE_BREAK>>> page_XXX` 是页边界,**保留**到输出(便于合并阶段定位)
- `1.1 Section Title §` 是 Section 标题,`§` 表示这是 spec 内部 section
- 编号格式 `N.M.K` 是子小节
- 段落文字正常翻译,列表保留
"""


def build_glossary_excerpt():
    """Read the glossary and format as a 3-col markdown table."""
    with open(GLOSSARY_PATH) as f:
        gl = json.load(f)
    lines = ["| Source | Target | Category |", "|--------|--------|----------|"]
    for t in gl['terms']:
        # Escape pipe in target
        target = t['target'].replace('|', '\\|')
        lines.append(f"| {t['source']} | {target} | {t['category']} |")
    return '\n'.join(lines)


def get_figures_for_chapter(ch_num):
    """List figure files for a chapter."""
    fig_dir = OUT_ROOT / 'figures' / f'chapter_{ch_num:02d}'
    if not fig_dir.exists():
        return []
    figs = sorted(fig_dir.glob('*.png'))
    return [(f.stem, f.name) for f in figs]


def main():
    with open(INDEX_PATH) as f:
        idx = json.load(f)
    with open(PLAN_PATH) as f:
        plan = json.load(f)

    glossary_table = build_glossary_excerpt()
    fmt = FORMAT_TEMPLATE

    prompt_count = 0
    for ch_str, info in plan.items():
        ch_num = int(ch_str)
        ch_meta = next(c for c in idx['chapters'] if c['ch'] == ch_num)
        ch_en = ch_meta['en']
        ch_zh = ch_meta['zh']
        ch_pages = info['pages']
        chunks = info['chunks']
        figs = get_figures_for_chapter(ch_num)

        for i, chunk_file in enumerate(chunks):
            chunk_path = CHUNKS_DIR / chunk_file
            if not chunk_path.exists():
                print(f"  ! missing chunk: {chunk_path}")
                continue

            with open(chunk_path) as f:
                raw_text = f.read()

            # Output filename
            stem = chunk_file.replace('_raw.md', '')
            output_file = f'{stem}_CN_EN.md'

            # Figures section
            if figs:
                figs_md = "本 chapter 的 figure 文件 (figures/chapter_NN/...):\n\n"
                for stem_name, fname in figs[:30]:  # show first 30 as sample
                    figs_md += f"- `figures/chapter_{ch_num:02d}/{fname}` (page {stem_name.split('_')[1]})\n"
                if len(figs) > 30:
                    figs_md += f"- ... 共 {len(figs)} 张 figure\n"
            else:
                figs_md = "本 chapter 无 figure"

            # Tail figure list
            fig_patterns = '\n'.join([f"- `figures/chapter_{ch_num:02d}/{fname}`" for _, fname in figs])

            prompt = f"""# 任务：翻译 PCIe 6.2 规范 chunk 为中英对照双语 Markdown

## 输入
- **源文件**: `chunks/{chunk_file}` (PCIe 6.2 spec raw text)
- **输出文件**: `chunks_translated/{output_file}`
- **章节**: Chapter {ch_num}. {ch_en} ({ch_zh}) — PDF pages {ch_pages}
- **本 chunk 编号**: {i+1}/{len(chunks)}

## 重要：使用 skill

**本项目使用的翻译 skill 路径**: `/Users/jianmingwang/Downloads/00_study/02_work/06_claude/ws/.claude/skills/cn-en-translate.md`

该 skill 定义了项目的整体翻译规则（图表提取、commit 等）。本任务的 chunk 翻译严格遵循其语言风格 + CXL 3.2 模板格式。

## 翻译规则 (必须严格遵守)

{fmt}

## 术语表 (Glossary) — 严格使用以下译法

> 本术语表是从 CXL 3.2 (CXL_zh/) 翻译中精选的 PCIe 共享术语。所有术语**必须**使用表中的"Target"列译法。

{glossary_table}

## 本章 Figure 文件清单

{figs_md}

完整列表（按页码排序）:
{fig_patterns}

## 待翻译的源文本

以下是 `chunks/{chunk_file}` 的内容，**严格按顺序翻译，不要跳过任何段落**：

---

{raw_text}

---

## 输出要求

1. 将翻译结果写入 `chunks_translated/{output_file}`
2. 输出**完整的中英对照双语文档**，**只输出 markdown 内容，不要有任何说明/对话/注释**
3. 严格按 CXL 3.2 格式输出：每个 Section 一个 HTML <table>，中文列灰底
4. **必须保留**所有 `<<<PAGE_BREAK>>> page_XXX` 标记（合并阶段需要定位页码）
5. **必须保留**所有 `figures/chapter_{ch_num:02d}/fig_PPPP_1.png` 形式的图片引用
6. 翻译要技术准确、自然流畅，符合中文技术文档表达习惯

开始翻译。
"""
            # Write prompt file
            prompt_file = PROMPTS_DIR / f'prompt_{stem}.md'
            prompt_file.write_text(prompt)
            prompt_count += 1

    print(f"Wrote {prompt_count} prompt files to {PROMPTS_DIR}")


if __name__ == '__main__':
    main()
