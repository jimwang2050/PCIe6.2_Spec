#!/usr/bin/env python3
"""Remove duplicate figure blocks (per user request: keep one figure per location)."""
import re
from collections import Counter
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def find_figure_blocks(content):
    blocks = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        m = re.match(r'^>\s*\*\*Figure\s+[\w\.\-]+.*\*\*', lines[i])
        if m:
            j = i + 1
            img_src = None
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines):
                m2 = re.search(r'<img\s+src="([^"]+)"', lines[j])
                if m2:
                    img_src = m2.group(1)
                    block_end = j + 1
                else:
                    block_end = i + 1
            else:
                block_end = i + 1
            blocks.append((i, block_end, img_src))
            i = block_end
        else:
            i += 1
    return blocks


def dedup_figures(content):
    blocks = find_figure_blocks(content)
    seen = set()
    lines_to_remove = set()
    n_removed = 0

    for start, end, src in blocks:
        if src is None:
            continue
        if src in seen:
            for i in range(start, end):
                lines_to_remove.add(i)
            for i in range(end, min(end + 3, len(content.split('\n')))):
                if content.split('\n')[i].strip() == '':
                    lines_to_remove.add(i)
                else:
                    break
            n_removed += 1
        else:
            seen.add(src)

    lines = content.split('\n')
    new_lines = [l for i, l in enumerate(lines) if i not in lines_to_remove]
    result = '\n'.join(new_lines)
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    return result, n_removed


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        n_before = len(find_figure_blocks(content))

        new_content, n_removed = dedup_figures(content)
        n_after = len(find_figure_blocks(new_content))

        if n_before != n_after:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: {n_before} → {n_after} (removed {n_removed} dups)")
        else:
            print(f"✓ {name[:50]}: {n_before} figures (no dups)")


if __name__ == '__main__':
    main()
