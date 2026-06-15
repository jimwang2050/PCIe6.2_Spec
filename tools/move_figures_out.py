#!/usr/bin/env python3
"""Move figures out of bilingual table cells.

For each <table>...</table>, find figure blocks (caption + img) inside
<td> cells and move them to a standalone line after </table>.
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def process_table(table_text):
    """Extract figure blocks from inside table cells, return (new_table, extracted_figs)."""
    figs = []
    # Pattern: > **Figure X-X.** caption\n> <img src=...>
    fig_pattern = re.compile(
        r'>\s*\*\*Figure\s+[\w\.\-]+(?:\([^)]*\))?\.?\*\*[^\n]*\n'
        r'>\s*<img\s+src="[^"]+"\s+width="\d+">\s*\n?',
        re.MULTILINE
    )
    extracted_figs = []
    def repl(m):
        fig = m.group(0).rstrip() + '\n'
        extracted_figs.append(fig)
        return ''  # Remove from cell
    new_table = fig_pattern.sub(repl, table_text)
    return new_table, extracted_figs


def move_figs_out(content):
    """Find all tables, extract figs, place them after </table>."""
    n_figs_moved = 0
    # Find each <table>...</table>
    def repl(m):
        nonlocal n_figs_moved
        table = m.group(0)
        new_table, figs = process_table(table)
        if figs:
            n_figs_moved += len(figs)
            figs_text = '\n'.join(figs).rstrip() + '\n'
            # Insert after </table>
            return new_table + '\n\n' + figs_text
        return table
    new_content = re.sub(
        r'<table>.*?</table>',
        repl,
        content,
        flags=re.DOTALL,
    )
    # Clean up empty cells (where fig was removed, leave <td> with just whitespace)
    new_content = re.sub(
        r'<td>\s*\n\s*\n\s*</td>',
        '<td></td>',
        new_content,
    )
    return new_content, n_figs_moved


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        new_content, n = move_figs_out(content)
        if n > 0:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: moved {n} figures out of tables")
        else:
            print(f"✓ {name[:50]}: no figures in tables")


if __name__ == '__main__':
    main()
