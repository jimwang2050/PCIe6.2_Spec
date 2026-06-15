#!/usr/bin/env python3
"""Remove ZH figure blocks (with optional blank line between caption and img)."""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()

        # Find all fig blocks (both EN and ZH patterns) with optional blank line
        # Pattern A: > **Figure X-X.** caption\n\n> <img ...>
        # Pattern B: > **图 X-X.** caption\n\n> <img ...>
        zh_fig_pattern = re.compile(
            r'>\s*\*\*图\s+[\w\.\-]+\.?\s*\*\*[^\n]*\n'
            r'(?:>\s*\n)?'  # optional empty line
            r'>\s*<img\s+src="[^"]+"\s+width="\d+">\s*\n?',
            re.MULTILINE
        )
        # Also catch EN style in case any remain
        en_fig_pattern = re.compile(
            r'>\s*\*\*Figure\s+[\w\.\-]+(?:\([^)]*\))?\.?\s*\*\*[^\n]*\n'
            r'(?:>\s*\n)?'
            r'>\s*<img\s+src="[^"]+"\s+width="\d+">\s*\n?',
            re.MULTILINE
        )

        # Only modify table contents, not standalone lines
        def process_table(m):
            table = m.group(0)
            # Remove ZH fig blocks
            table = zh_fig_pattern.sub('', table)
            # Remove EN fig blocks (in case still in tables)
            table = en_fig_pattern.sub('', table)
            return table

        new_content = re.sub(
            r'<table>.*?</table>',
            process_table,
            content,
            flags=re.DOTALL,
        )

        # Count removed
        n_zh = len(zh_fig_pattern.findall(content)) - len(zh_fig_pattern.findall(new_content))
        n_en = len(en_fig_pattern.findall(content)) - len(en_fig_pattern.findall(new_content))

        if n_zh + n_en > 0:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: removed {n_zh} ZH + {n_en} EN fig blocks from tables")
        else:
            print(f"✓ {name[:50]}: clean")


if __name__ == '__main__':
    main()
