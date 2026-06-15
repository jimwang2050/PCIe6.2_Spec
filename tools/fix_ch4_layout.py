#!/usr/bin/env python3
"""
Fix long tables in Ch 4 (and all chapters) by wrapping each <table> in a
scrollable <div>. This prevents tables from overflowing the viewport on
narrow screens (GitHub, mobile, etc.).

Also updates the CSS file to include table overflow handling.
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))
CSS_FILE = OUT_ROOT / 'preview' / 'pcie62_style.css'


def fix_chapter(path):
    """Wrap each <table>...</table> in a scrollable div."""
    content = path.read_text()
    n_wrapped = 0
    # Skip if already wrapped (idempotent)
    # Pattern: find <table>...</table> not preceded by a scrollable div
    new_content = []
    i = 0
    while i < len(content):
        # Look for a <table> tag
        m = re.search(r'<table\b', content[i:])
        if not m:
            new_content.append(content[i:])
            break
        # Append everything up to <table>
        new_content.append(content[i:i + m.start()])
        # Check if preceded by our wrapper
        tail = ''.join(new_content[-3:])
        if 'overflow-x: auto' in tail or 'overflow-x:auto' in tail:
            # Already wrapped
            new_content.append(content[i + m.start():i + m.start()])
            i = i + m.start() + 1
            continue
        # Find end of table
        end_m = re.search(r'</table>', content[i + m.start():])
        if not end_m:
            new_content.append(content[i + m.start():])
            break
        table_block = content[i + m.start():i + m.start() + end_m.end()]
        # Check table length — only wrap long tables (>1000 chars)
        if len(table_block) > 1000:
            wrapped = f'\n<div style="overflow-x: auto; max-width: 100%;">\n{table_block}\n</div>\n'
            new_content.append(wrapped)
            n_wrapped += 1
        else:
            new_content.append(table_block)
        i = i + m.start() + end_m.end()

    if n_wrapped > 0:
        path.write_text(''.join(new_content))
    return n_wrapped


def update_css():
    """Add table overflow CSS."""
    if not CSS_FILE.exists():
        return
    content = CSS_FILE.read_text()
    if 'table { overflow-x' in content:
        return  # already updated
    new_css = '''/* Table layout - prevent wide tables from overflowing */
table { border-collapse: collapse; margin: 12px 0; max-width: 100%; table-layout: auto; word-wrap: break-word; }
th, td { border: 1px solid #ddd; padding: 8px 12px; vertical-align: top; max-width: 600px; word-wrap: break-word; overflow-wrap: break-word; }
th { background-color: #f0f0f0; }
/* Long tables can be wrapped in a scrollable div */
div:has(> table) { overflow-x: auto; max-width: 100%; }
/* Code inside tables should not break layout */
td code { word-break: break-all; }
td pre { max-width: 100%; overflow-x: auto; }
'''
    # Replace the table style block
    new_content = re.sub(
        r'table \{[^}]*\}',
        '/* See new table styles below */',
        content
    )
    new_content = new_content + '\n\n' + new_css
    CSS_FILE.write_text(new_content)
    return True


def main():
    print("=" * 70)
    print("PCIe 6.2 — 长表格布局修复")
    print("=" * 70)
    print()

    total = 0
    for ch in CHAPTERS:
        n = fix_chapter(ch)
        if n > 0:
            print(f"  {ch.name[:60]}: 包裹 {n} 个长表格")
            total += n

    print(f"\n共包裹 {total} 个长表格 (> 1000 chars)")

    # Update CSS
    if update_css():
        print(f"✓ 更新 CSS: {CSS_FILE}")

    print("\n完成。表格将使用 div 包裹,支持水平滚动。")


if __name__ == '__main__':
    main()
