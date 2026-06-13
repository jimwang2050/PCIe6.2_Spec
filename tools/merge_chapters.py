#!/usr/bin/env python3
"""
Merge translated chunks into per-chapter MD files in CXL 3.2 format.

For chunks not yet translated, insert a TBD placeholder.
"""
import json
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHUNKS_DIR = OUT_ROOT / 'chunks'
TRANSLATED_DIR = OUT_ROOT / 'chunks_translated'
INDEX_PATH = OUT_ROOT / 'chapter_index.json'
PLAN_PATH = OUT_ROOT / 'chunk_plan.json'

# CXL 3.2 standard chapter H1 header
H1_TEMPLATE = """# 📘 第 {ch} 章　{en} (Chapter {ch}. {en})

**PCI Express® Base Specification — Revision 6.2, Version 1.0 — January 25, 2024**

> 📄 **Source pages**: {pages} (PDF 1-indexed) | 📁 **File**: `chapter_{ch:02d}_raw.md`
> 🎨 **Format**: 中英对照双语 · 图表原始保留 · 中文背景色灰色 · GitHub Flavored Markdown
> 📚 **Template**: CXL 3.2 Spec translation (CXL_zh/)

---

## 📑 本章目录 (Table of Contents)

> 由合并阶段自动生成。请使用浏览器/GitHub 渲染时,各小节标题链接跳转。

## 🖼 本章图表 (Figures)

> 所有图已抽取为 PNG 存放在 `figures/chapter_{ch:02d}/`。

## 📊 本章表格 (Tables)

> 各章表格以标准 Markdown 表格形式嵌入正文。

---

"""


def main():
    with open(INDEX_PATH) as f:
        idx = json.load(f)
    with open(PLAN_PATH) as f:
        plan = json.load(f)

    ch_titles = {c['ch']: c for c in idx['chapters']}

    for ch_str, info in sorted(plan.items(), key=lambda x: int(x[0])):
        ch_num = int(ch_str)
        ch_meta = ch_titles[ch_num]
        en = ch_meta['en']
        zh = ch_meta['zh']
        pages = ch_meta['end'] - ch_meta['start'] + 1
        page_range = f"{ch_meta['start']}–{ch_meta['end']}"

        # Build the chapter file
        out = H1_TEMPLATE.format(
            ch=ch_num,
            en=en,
            zh=zh,
            pages=page_range,
        )

        # Build TOC (synthesized from section headers we find in chunks)
        toc_entries = []
        all_section_ids = []

        for i, chunk_file in enumerate(info['chunks']):
            stem = chunk_file.replace('_raw.md', '')
            translated_file = TRANSLATED_DIR / f'{stem}_CN_EN.md'
            raw_file = CHUNKS_DIR / chunk_file

            if translated_file.exists():
                content = translated_file.read_text()
                # Find all section anchors
                for m in re.finditer(r'<a id="(sec-[\d\-]+)"></a>\s*\n## ([^\n]+)', content):
                    sec_id = m.group(1)
                    sec_title = m.group(2).strip()
                    all_section_ids.append((sec_id, sec_title))

                # Strip the placeholder TOC/Figure/Table blocks if present in chunk
                content = re.sub(
                    r'## 📑 本章目录 \(Table of Contents\)\n.*?(?=\n## |\Z)',
                    '',
                    content,
                    flags=re.DOTALL,
                )
                content = re.sub(
                    r'## 🖼 本章图表 \(Figures\)\n.*?(?=\n## |\Z)',
                    '',
                    content,
                    flags=re.DOTALL,
                )
                content = re.sub(
                    r'## 📊 本章表格 \(Tables\)\n.*?(?=\n## |\Z)',
                    '',
                    content,
                    flags=re.DOTALL,
                )

                out += f"\n---\n\n{content}\n"
            else:
                # Placeholder for untranslated chunk
                out += f"\n---\n\n## ⚠️ TODO: {stem} 未翻译\n\n"
                out += f"本 chunk (`{chunk_file}`) 尚未完成翻译。在最终版本中将包含原文 + 中英对照翻译。\n\n"
                if raw_file.exists():
                    raw_size = raw_file.stat().st_size
                    out += f"- 源文件: `chunks/{chunk_file}` ({raw_size:,} bytes)\n"
                    out += f"- 提示: 重跑此 prompt: `prompts/prompt_{stem}.md`\n\n"
                out += "---\n"

        # Generate TOC from collected section IDs
        if all_section_ids:
            out += "\n---\n\n## 📑 本章目录 (Table of Contents) — Auto-Generated\n\n"
            for sec_id, sec_title in all_section_ids:
                # Strip "## " prefix from sec_title for cleaner display
                clean_title = re.sub(r'^##\s+', '', sec_title).strip()
                out += f"- [{clean_title}](#{sec_id})\n"

        # Write chapter file (sanitize filename aggressively for filesystem safety)
        safe_en = re.sub(r'[^A-Za-z0-9]+', '_', en).strip('_')
        safe_zh = re.sub(r'[^一-鿿A-Za-z0-9]+', '', zh)
        out_name = f"PCIe6.2_Spec_ch{ch_num:02d}_{safe_en}_{safe_zh}.md"
        out_path = OUT_ROOT / out_name
        out_path.write_text(out)
        print(f"  Ch{ch_num:02d} → {out_name} ({len(out):,} chars, {len(all_section_ids)} sections)")


if __name__ == '__main__':
    main()
