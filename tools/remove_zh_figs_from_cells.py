#!/usr/bin/env python3
"""Remove ZH-style figure blocks from <td> cells.

The previous dedup + move_figures_out left ZH-cell figures because:
- move_figures_out only matched > **Figure X-X.** (EN pattern)
- ZH cells have > **图 X-X.** (Chinese "图")
- So ZH figures were never moved out

This script also matches Chinese-style figure captions and moves them.
Also dedups: if the same img_src was already moved out by previous script,
the ZH copy here is a duplicate and should be removed entirely (not re-added).
"""
import re
from collections import OrderedDict
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def find_existing_standalone_figs(content):
    """Find all img_src that are already standalone (outside tables)."""
    # Remove all <table>...</table> blocks, then find img refs
    no_tables = re.sub(r'<table>.*?</table>', '', content, flags=re.DOTALL)
    srcs = re.findall(r'<img\s+src="([^"]+)"', no_tables)
    return set(srcs)


def process_table(table_text, existing_standalone):
    """Find ZH-style figure blocks inside this table.

    Returns (new_table, figs_to_add_outside, n_removed)
    figs_to_add_outside: list of fig blocks to add AFTER the table
    n_removed: count of removed fig blocks
    """
    n_removed = 0
    figs_to_add = []

    # Pattern matches both EN and ZH figure blocks:
    # > **Figure X-X.** caption EN/ZH\n> <img src=...>
    # > **图 X-X.** 中文\n> <img src=...>
    # Use a non-greedy approach: find each > **...** block followed by > <img>

    # Try multiple patterns
    patterns = [
        # ZH: > **图 X-X.** 中文 caption
        re.compile(
            r'>\s*\*\*图\s+[\w\.\-]+\.?\s*\*\*[^\n]*\n'
            r'>\s*<img\s+src="([^"]+)"\s+width="\d+">\s*\n?',
            re.MULTILINE
        ),
        # EN: > **Figure X-X.** caption
        re.compile(
            r'>\s*\*\*Figure\s+[\w\.\-]+(?:\([^)]*\))?\.?\s*\*\*[^\n]*\n'
            r'>\s*<img\s+src="([^"]+)"\s+width="\d+">\s*\n?',
            re.MULTILINE
        ),
    ]

    for pat in patterns:
        def repl(m):
            nonlocal n_removed
            src = m.group(1)
            n_removed += 1
            # If this src is NOT already in standalone, add it
            if src not in existing_standalone:
                figs_to_add.append(m.group(0).rstrip() + '\n')
                existing_standalone.add(src)
            return ''
        table_text = pat.sub(repl, table_text)

    return table_text, figs_to_add, n_removed


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        existing = find_existing_standalone_figs(content)

        total_removed = 0
        total_added = 0

        def repl(m):
            nonlocal total_removed, total_added
            new_table, figs, n_removed = process_table(m.group(0), existing)
            total_removed += n_removed
            total_added += len(figs)
            if figs:
                return new_table + '\n\n' + '\n'.join(figs).rstrip() + '\n'
            return new_table

        new_content = re.sub(
            r'<table>.*?</table>',
            repl,
            content,
            flags=re.DOTALL,
        )

        if total_removed > 0:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: removed {total_removed} fig blocks, added {total_added} standalone")
        else:
            print(f"✓ {name[:50]}: no ZH fig blocks found")


if __name__ == '__main__':
    main()
