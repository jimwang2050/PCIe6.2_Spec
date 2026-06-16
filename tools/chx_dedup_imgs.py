#!/usr/bin/env python3
"""
通用化: 修复章节 MD 中跨中英文两列重复的 <img> 引用。

对每对重复 (English 侧 + Chinese 侧),保留 English 侧,删除 Chinese 侧
及其前一行"图 X-X" caption(若存在)。
"""
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')


def dedup(ch_num):
    md_files = list(ROOT.glob(f'PCIe6.2_Spec_ch{ch_num:02d}_*.md'))
    if not md_files:
        print(f"Ch{ch_num}: MD not found")
        return
    md = md_files[0]
    with open(md) as f:
        text = f.read()
    lines = text.split('\n')

    # Match <img> for any chapter_NN
    img_re = re.compile(r'<img\s+src="figures/chapter_\d{2,3}/fig_(\d{4})_(\d+)(_tight)?\.png"\s+(\w+)="([^"]+)"\s*>')

    positions = []
    for i, line in enumerate(lines):
        m = img_re.search(line)
        if m:
            positions.append((i, m.group(1) + '_' + m.group(2)))

    by_src = defaultdict(list)
    for line_idx, src_key in positions:
        by_src[src_key].append(line_idx)

    # Find close pairs (within 50 lines)
    dup_pairs = []
    for src_key, locs in by_src.items():
        if len(locs) < 2: continue
        for i in range(len(locs)):
            for j in range(i+1, len(locs)):
                if abs(locs[i] - locs[j]) < 50:
                    dup_pairs.append((src_key, locs[i], locs[j]))

    if not dup_pairs:
        print(f"Ch{ch_num}: no duplicates")
        return

    # Deduplicate pairs
    seen = set()
    unique = []
    for src, l1, l2 in dup_pairs:
        k = (src, min(l1, l2), max(l1, l2))
        if k in seen: continue
        seen.add(k)
        unique.append((src, l1, l2))

    print(f"Ch{ch_num}: {len(unique)} duplicate pairs")

    # Remove the LATER occurrence (Chinese side) and the caption above it
    to_remove = set()
    for src, l1, l2 in unique:
        later = max(l1, l2)
        to_remove.add(later)
        if later > 0 and re.match(r'>\s+\*\*图\s*\d+-\d+', lines[later-1]):
            to_remove.add(later-1)

    new_lines = [line for i, line in enumerate(lines) if i not in to_remove]
    removed = len(lines) - len(new_lines)
    print(f"  Removed {removed} lines")
    with open(md, 'w') as f:
        f.write('\n'.join(new_lines))


def main():
    args = sys.argv[1:] or ['1-12']
    chs = []
    for arg in args:
        if '-' in arg:
            s, e = arg.split('-')
            chs.extend(range(int(s), int(e)+1))
        elif ',' in arg:
            chs.extend(int(x) for x in arg.split(',') if x.strip().isdigit())
        else:
            chs.append(int(arg))
    for c in chs:
        dedup(c)


if __name__ == '__main__':
    main()
