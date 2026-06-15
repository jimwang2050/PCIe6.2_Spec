#!/usr/bin/env python3
"""
Transform chapter MDs to new single-column format (per user request).

Changes:
1. Convert 2-col bilingual tables → 1-col tables with EN row + ZH row stacked
2. Remove duplicate (CN) figure blocks (keep only EN captions)
3. Remove all <div style="overflow-x: auto"> wrappers (no longer needed)
4. Keep section headers bilingual (## X | Y) as-is
5. Keep prose paragraphs as-is
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def convert_bilingual_table(table_match):
    """Convert a 2-col bilingual HTML table to single-col stacked format."""
    table = table_match.group(0)
    # Find thead (header row)
    thead_match = re.search(r'<thead>(.*?)</thead>', table, re.DOTALL)
    tbody_match = re.search(r'<tbody>(.*?)</tbody>', table, re.DOTALL)

    if not tbody_match:
        return table

    # Extract header content (combine EN+ZH into one cell)
    if thead_match:
        # Get first th text
        th_texts = re.findall(r'<th[^>]*>(.*?)</th>', thead_match.group(1), re.DOTALL)
        header_text = ' / '.join(re.sub(r'<[^>]+>', '', t).strip() for t in th_texts)
    else:
        header_text = ''

    # Get body rows
    rows = re.findall(r'<tr>(.*?)</tr>', tbody_match.group(1), re.DOTALL)
    new_rows = []
    for row in rows:
        # Get td cells (without inner tr/td)
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        if len(cells) == 0:
            continue
        if len(cells) == 1:
            # Already single-col row
            new_rows.append(f'<tr><td>{cells[0]}</td></tr>')
        else:
            # Multi-col: stack EN then ZH
            # First cell is EN, second is ZH, etc.
            for i, cell in enumerate(cells):
                if i == 0:
                    new_rows.append(f'<tr><td>{cell}</td></tr>')
                else:
                    # Add a divider or just stack
                    new_rows.append(f'<tr><td>{cell}</td></tr>')

    # Rebuild the table as single column
    new_table = '<table>\n<thead>\n<tr>\n'
    if header_text:
        new_table += f'<th>{header_text}</th>\n'
    else:
        new_table += '<th></th>\n'
    new_table += '</tr>\n</thead>\n<tbody>\n'
    new_table += '\n'.join(new_rows)
    new_table += '\n</tbody>\n</table>'
    return new_table


def transform(content):
    """Apply all transformations."""
    n_tables = 0
    n_figs_removed = 0

    # 1. Convert each bilingual table
    def repl_table(m):
        nonlocal n_tables
        # Detect bilingual: must have at least one <td> with background-color:#e8e8e8
        if '#e8e8e8' in m.group(0):
            n_tables += 1
            return convert_bilingual_table(m)
        return m.group(0)

    # Use non-greedy with DOTALL for nested tags
    # First, find each <table>...</table> block
    content = re.sub(
        r'<table>.*?</table>',
        repl_table,
        content,
        flags=re.DOTALL,
    )

    # 2. Remove <div style="overflow-x: auto; max-width: 100%;">...</div> wrappers
    content = re.sub(
        r'<div\s+style="overflow-x: auto;?\s*max-width:\s*100%;?">\s*\n',
        '',
        content,
    )
    content = re.sub(
        r'</div>\s*\n---\n',
        '\n---\n',
        content,
    )

    # 3. Remove duplicate (CN) figure blocks
    # Pattern: > **Figure X-X (CN).** ... followed by image
    cn_fig_pattern = r'> \*\*Figure [\d\.\-]+ \(CN\)\.\*\*[^\n]*\n(?:> [^\n]*\n)*'
    matches = re.findall(cn_fig_pattern, content)
    n_figs_removed = len(matches)
    content = re.sub(cn_fig_pattern, '', content)

    # 4. Remove <th> gray bg style (no longer needed)
    content = re.sub(
        r'<th[^>]*style="background-color:#e8e8e8"[^>]*>',
        '<th>',
        content,
    )
    # Remove the gray bg from td cells (keep the cells)
    content = re.sub(
        r'<td style="background-color:#e8e8e8">',
        '<td>',
        content,
    )
    # Remove the bg flag column header text (🇨🇳 中文) — keep just English
    content = re.sub(
        r'<th>🇬🇧 English</th>\s*<th[^>]*>🇨🇳 中文</th>',
        '<th>English / 中文</th>',
        content,
    )

    # Clean up multiple blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    return content, n_tables, n_figs_removed


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        new_content, n_tables, n_figs = transform(content)
        if new_content != content:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: {n_tables} tables, {n_figs} (CN) figs removed")
        else:
            print(f"✓ {name[:50]}: no change")


if __name__ == '__main__':
    main()
