#!/usr/bin/env python3
"""
修复 ch04 MD 中跨中英文两列重复的 <img> 引用。

策略:
- 对每对重复 (English 侧 + Chinese 侧),保留 English 侧,删除 Chinese 侧
- 也清除孤立的"图 X-X"重复 caption (在没有 <img> 的情况下)
- 保持 figure block 完整性 (不破坏 caption 引用关系)
"""
import re
from pathlib import Path

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
MD = ROOT / 'PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md'


def main():
    with open(MD) as f:
        text = f.read()

    # Find all <img> with their line numbers and src
    lines = text.split('\n')
    img_re = re.compile(r'<img\s+src="figures/chapter_04/fig_(\d{4})_(\d+)(_tight)?\.png"\s+(\w+)="([^"]+)"\s*>')

    # Pass 1: collect all <img> positions
    positions = []  # (line_idx, src)
    for i, line in enumerate(lines):
        m = img_re.search(line)
        if m:
            positions.append((i, m.group(1) + '_' + m.group(2)))

    # Group by src
    from collections import defaultdict
    by_src = defaultdict(list)
    for line_idx, src_key in positions:
        by_src[src_key].append(line_idx)

    # Find duplicates (same src within 30 lines = same figure group)
    dup_groups = []
    for src_key, locs in by_src.items():
        if len(locs) < 2:
            continue
        # Find all close pairs
        for i in range(len(locs)):
            for j in range(i+1, len(locs)):
                if abs(locs[i] - locs[j]) < 50:
                    dup_groups.append((src_key, locs[i], locs[j]))

    # Deduplicate dup_groups
    seen_pairs = set()
    unique_dupes = []
    for src, l1, l2 in dup_groups:
        key = (src, min(l1, l2), max(l1, l2))
        if key in seen_pairs: continue
        seen_pairs.add(key)
        unique_dupes.append((src, l1, l2))

    print(f"Found {len(unique_dupes)} duplicate pairs to fix")
    print()

    # For each duplicate pair, identify the LATER occurrence (Chinese side) and remove
    # Strategy: keep the first occurrence, remove the second
    # But we need to also remove the surrounding "图 X-X" caption if it becomes orphan
    lines_to_remove = set()

    for src, l1, l2 in unique_dupes:
        # Keep l1 (earlier), remove l2
        # Also check if l1 is on English side (left td) and l2 on Chinese side
        # If they're in the same <tr> (table row), l2 is in Chinese <td>
        # If they're outside table (Category 2), check blockquote "> " pattern
        first_line = lines[l1]
        second_line = lines[l2]
        print(f"  src={src}: L{l1+1} ↔ L{l2+1}")
        print(f"    keep: {first_line[:80]}")
        print(f"    drop: {second_line[:80]}")

        # Determine if in same table row
        same_table = False
        for i in range(max(0, l1-5), l1):
            if '<table>' in lines[i]:
                # Found table start
                table_start = i
                break
        else:
            table_start = -1

        # Add the img line and the "图 X-X" caption before it (if any) to removal set
        lines_to_remove.add(l2)
        # Also remove the line above if it's a "图 X-X" caption (Chinese)
        if l2 > 0 and re.match(r'>\s+\*\*图\s*\d+-\d+', lines[l2-1]):
            lines_to_remove.add(l2-1)

    # Apply removals (in reverse order to keep indices stable)
    new_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
    removed = len(lines) - len(new_lines)
    print(f"\nRemoved {removed} lines (img + orphan Chinese captions)")

    # Write back
    with open(MD, 'w') as f:
        f.write('\n'.join(new_lines))
    print(f"✓ Updated: {MD.name}")


if __name__ == '__main__':
    main()
