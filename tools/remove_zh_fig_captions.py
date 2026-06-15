#!/usr/bin/env python3
"""
Remove ZH figure captions from chunks_translated/.

Heuristic: any > **Figure X-X.** ... line that has Chinese characters in
its caption is the translator-added Chinese caption. Remove the entire
block (caption + image + blank lines).

This cleans up the source so re-merge produces clean single-figure
references (EN only).
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHUNKS_DIR = OUT_ROOT / 'chunks_translated'


def has_zh(s):
    return any('一' <= c <= '鿿' for c in s)


def remove_zh_fig_captions(content):
    n_removed = 0
    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Look for a > **Figure X-X.** ... line
        m = re.match(r'^>\s*\*\*Figure\s+[\w\.\-]+\.\*\*\s*(.*)', line)
        if m and has_zh(m.group(1)):
            # This is a ZH caption. Remove the block.
            # Skip the caption line
            i += 1
            # Skip the next image line (if any)
            if i < len(lines) and '<img' in lines[i]:
                i += 1
            # Skip trailing blank lines
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            n_removed += 1
            continue
        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines), n_removed


def main():
    chunk_files = sorted(CHUNKS_DIR.glob('chapter_*_CN_EN.md'))
    total_removed = 0
    for f in chunk_files:
        content = f.read_text()
        new_content, n = remove_zh_fig_captions(content)
        if n > 0:
            f.write_text(new_content)
            total_removed += n
    print(f"Removed {total_removed} ZH figure caption blocks from {len(chunk_files)} chunks")


if __name__ == '__main__':
    main()
