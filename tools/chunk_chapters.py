#!/usr/bin/env python3
"""
Split each chapter's raw text into sub-chunks at section boundaries.

Heuristic: split on lines starting with "Section N.M" (e.g., "Section 2.5.3.4")
or "Chapter N." — these are clean cut points. Aim for ~100-150K char chunks.
"""
import json
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
RAW_DIR = OUT_ROOT / 'raw'
CHUNKS_DIR = OUT_ROOT / 'chunks'
INDEX_PATH = OUT_ROOT / 'chapter_index.json'

# Target chunk size in chars
TARGET_CHUNK_SIZE = 120_000
# Section header pattern: e.g. "7. Software Init §" or "7.2.1 PCI-compatible §"
# Sections appear as a numbered line ending with "§"
SECTION_RE = re.compile(r'^(\d+(\.\d+)+\.?)\s+\S.*§\s*$', re.MULTILINE)


def find_section_offsets(text):
    """Return list of (offset, section_label) for section headers in text."""
    matches = []
    for m in SECTION_RE.finditer(text):
        # Get the section title until end of line
        end = text.find('\n', m.start())
        if end == -1:
            end = m.end()
        label = text[m.start():end].strip()
        matches.append((m.start(), label))
    return matches


def split_chapter(ch_num, raw_text, target_size):
    """Split a chapter's raw text into chunks of ~target_size chars at section boundaries."""
    if len(raw_text) <= target_size * 1.3:
        # Single chunk is fine if not much over target
        return [raw_text]

    # Find section offsets
    sections = find_section_offsets(raw_text)

    if not sections:
        # Fallback: split on PAGE_BREAK markers
        markers = [m.start() for m in re.finditer(r'<<<PAGE_BREAK>>>', raw_text)]
        if not markers:
            return [raw_text]
        chunks = []
        start = 0
        for i, m in enumerate(markers):
            if m - start >= target_size and start > 0:
                chunks.append(raw_text[start:m])
                start = m
        if start < len(raw_text):
            chunks.append(raw_text[start:])
        return chunks

    # Group sections into chunks of ~target_size
    chunks = []
    current_start = 0
    current_size = 0

    for sec_offset, sec_label in sections:
        sec_size = sec_offset - current_start
        if current_size + sec_size > target_size and current_size > 0:
            # Cut before this section
            chunks.append(raw_text[current_start:sec_offset])
            current_start = sec_offset
            current_size = sec_size
        else:
            current_size += sec_size

    if current_start < len(raw_text):
        chunks.append(raw_text[current_start:])

    return chunks


def main():
    CHUNKS_DIR.mkdir(exist_ok=True)
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    plan = {}
    for ch in idx['chapters']:
        ch_num = ch['ch']
        raw_path = RAW_DIR / f'chapter_{ch_num:02d}_raw.md'
        with open(raw_path) as f:
            text = f.read()
        chunks = split_chapter(ch_num, text, TARGET_CHUNK_SIZE)
        # Write each chunk
        chunk_files = []
        for i, c in enumerate(chunks, 1):
            if len(chunks) == 1:
                suffix = ''
            else:
                # Use 2-char letter suffix (aa, ab, ..., az, ba, ...) for many chunks
                idx = i - 1
                first = chr(ord('a') + idx // 26)
                second = chr(ord('a') + idx % 26)
                suffix = f'_{first}{second}'
            fname = f'chapter_{ch_num:02d}{suffix}_raw.md'
            (CHUNKS_DIR / fname).write_text(c)
            chunk_files.append(fname)
        plan[str(ch_num)] = {
            'en': ch['en'],
            'zh': ch['zh'],
            'pages': f"{ch['start']}-{ch['end']}",
            'chunks': chunk_files,
            'chunk_sizes': [len(c) for c in chunks],
        }
        print(f"Ch{ch_num:02d} {ch['en']:50s} -> {len(chunks)} chunks ({sum(len(c) for c in chunks):,} chars)")

    with open(OUT_ROOT / 'chunk_plan.json', 'w') as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_ROOT/'chunk_plan.json'}")


if __name__ == '__main__':
    main()
