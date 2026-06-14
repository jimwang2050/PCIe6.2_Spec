#!/usr/bin/env python3
"""
Auto-fix common layout issues in the 12 PCIe 6.2 chapter MDs.

Fixes:
1. Unbalanced <table> tags (add/remove closing tags)
2. Duplicate <a id="..."> anchors (rename duplicates with -1, -2 suffix)
3. EN-only "section header" leaks in cells (e.g. "4.2.7.2.3 Polling.Configuration §")
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def fix_table_balance(content):
    """Add or remove </table> tags to balance."""
    n_open = len(re.findall(r'<table\b[^>]*>', content))
    n_close = len(re.findall(r'</table>', content))

    if n_open == n_close:
        return content, 0

    diff = n_open - n_close
    # Split content into table blocks
    if diff > 0:
        # Need to add close tags
        # Find last unclosed <table>: the one that has <table> but no following </table>
        # Simpler: just append diff </table> before end
        # But we should be smarter: find the last <table> without a following </table>
        # For now, just append the missing closes
        content = content.rstrip() + ('\n</table>' * diff) + '\n'
    else:
        # diff < 0, need to remove extra closes
        # Find and remove diff extra </table> tags
        # Use last <table>...</table> blocks and remove the last one's close
        # Simpler: remove the last diff </table> tags
        excess = -diff
        for _ in range(excess):
            # Remove the last </table> tag
            content = content.rsplit('</table>', 1)
            content = '</table>'.join(content[:-1]) + ''.join(['</table>'] * (len(content) - 1)) if False else content[0] + content[1]
            # Actually simpler: regex find last
        # Use a different approach: just keep first n opens and n closes
        # find positions of all </table> and remove the last diff
        close_positions = [m.start() for m in re.finditer(r'</table>', content)]
        if len(close_positions) >= excess:
            for pos in reversed(close_positions[:excess]):
                # Remove this </table> occurrence
                content = content[:pos] + content[pos+len('</table>'):]
    return content, diff


def fix_duplicate_anchors(content):
    """Rename duplicate <a id="..."> to -1, -2 suffix."""
    anchors = list(re.finditer(r'<a\s+id="([^"]+)">', content))
    seen = {}
    new_content = content
    for m in reversed(anchors):  # Reverse to preserve positions
        anchor_id = m.group(1)
        if anchor_id in seen:
            seen[anchor_id] += 1
            new_id = f"{anchor_id}-{seen[anchor_id]}"
            new_content = new_content[:m.start()] + f'<a id="{new_id}">' + new_content[m.end():]
        else:
            seen[anchor_id] = 1
    return new_content, sum(1 for c in seen.values() if c > 1)


def fix_en_only_section_headers(content):
    """Remove section header leaks like '4.2.7.2.3 Polling.Configuration §' from table cells."""
    # Pattern: <td> section_header §</td> where section_header is "N.M.K.L Title §"
    # This is content that shouldn't be in a table cell
    new_content = re.sub(
        r'<td>(\d+(\.\d+)+\.?\s+\S+\s+§)</td>',
        r'<!-- removed leaked section header: \1 -->',
        content
    )
    diff_count = content.count('<td>') - new_content.count('<td>')
    return new_content, diff_count


def main():
    print("=" * 70)
    print("PCIe 6.2 中英对照翻译 — 修复布局问题")
    print("=" * 70)
    print()

    total_table_fixes = 0
    total_anchor_fixes = 0
    total_header_leaks = 0

    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        original = content

        # 1. Fix table balance
        content, table_diff = fix_table_balance(content)
        if table_diff != 0:
            print(f"📄 {name}: 表格标签 {abs(table_diff)} 修复")
            total_table_fixes += abs(table_diff)

        # 2. Fix duplicate anchors
        content, n_dup = fix_duplicate_anchors(content)
        if n_dup > 0:
            print(f"📄 {name}: 去重 {n_dup} 个 anchor")
            total_anchor_fixes += n_dup

        # 3. Fix EN-only section header leaks
        content, n_leaks = fix_en_only_section_headers(content)
        if n_leaks > 0:
            print(f"📄 {name}: 移除 {n_leaks} 个 section header 泄漏")
            total_header_leaks += n_leaks

        if content != original:
            ch.write_text(content)
            print(f"   ✓ 已更新 {ch.name}")
            print()

    print("=" * 70)
    print("修复汇总")
    print("=" * 70)
    print(f"  表格标签平衡修复: {total_table_fixes}")
    print(f"  Anchor 去重: {total_anchor_fixes}")
    print(f"  Section header 泄漏移除: {total_header_leaks}")
    print()

    if total_table_fixes + total_anchor_fixes + total_header_leaks == 0:
        print("✓ 无需修复")


if __name__ == '__main__':
    main()
