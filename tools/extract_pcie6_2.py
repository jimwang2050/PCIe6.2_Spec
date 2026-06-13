#!/usr/bin/env python3
"""
PCIe 6.2 PDF → per-chapter raw text + figures
- Reads chapter_index.json
- For each chapter: extract raw text (preserving section headings) and figures
- Output: raw/chXX_raw.md, figures/chapter_XX/fig_PPPP_1.png (de-watermarked)
- Reuses CXL_zh style: 150 dpi, crop top/bottom headers/footers
"""
import fitz  # PyMuPDF
import json
import os
import re
import sys
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
RAW_DIR = OUT_ROOT / 'raw'
FIG_DIR = OUT_ROOT / 'figures'
INDEX_PATH = OUT_ROOT / 'chapter_index.json'

# CXL_zh style crop params: top 110, bottom 1200 → 1580, x: 0 → 1200 (full width)
# Page is 1240×1580 at 150 dpi; CXL spec is "Evaluation Copy" watermarked
# For PCIe 6.2 we have "6.2-1.0-PUB — PCI Express® Base Specification Revision 6.2"
# We do simpler crop: full page (no watermark on PCIe 6.2, just header/footer)
# Adjust: top=100, bottom=1530, x=0→1240


def extract_text(doc, start_page, end_page, ch_num):
    """Extract text from a chapter's pages, preserving section structure."""
    lines = []
    lines.append(f"=== Chapter {ch_num} raw text ===")
    lines.append(f"PDF pages: {start_page}-{end_page} (1-indexed)")
    lines.append(f"PyMuPDF 0-indexed: {start_page-1}-{end_page-1}")
    lines.append("")

    # Per-page extract with section header detection
    section_re = re.compile(r'^(Chapter \d+\.\s+|Section \d+\.\d+(\.\d+)*\s+)', re.IGNORECASE)
    page_break = "<<<PAGE_BREAK>>>"

    for page_num in range(start_page - 1, end_page):  # PyMuPDF is 0-indexed
        if page_num >= len(doc):
            break
        page = doc[page_num]
        text = page.get_text("text")
        # Mark page boundary
        lines.append(f"\n{page_break} page_{page_num + 1}\n")
        # Filter out the page footer (6.2-1.0-PUB ... Page NNN)
        text_lines = text.split('\n')
        for tl in text_lines:
            tl_stripped = tl.strip()
            # Skip footer
            if re.match(r'^\d+\.\d+-\d+\.\d+-[A-Z]+', tl_stripped):
                continue
            if re.match(r'^Page \d+$', tl_stripped):
                continue
            if tl_stripped:
                lines.append(tl)

    return '\n'.join(lines)


def extract_figures(doc, start_page, end_page, ch_num):
    """Extract figures from a chapter: full-page PNG render with header/footer cropped.

    PCIe 6.2 page = 612x792 PDF points = 1275x1650 px at 150 dpi.
    Crop: top 110 (header), bottom 1530 (footer).
    """
    ch_fig_dir = FIG_DIR / f'chapter_{ch_num:02d}'
    ch_fig_dir.mkdir(parents=True, exist_ok=True)

    extracted = []
    CLIP = fitz.Rect(0, 110, 1275, 1530)  # in 150-dpi pixel coords
    ZOOM = fitz.Matrix(150 / 72, 150 / 72)

    for page_num in range(start_page - 1, end_page):
        if page_num >= len(doc):
            break
        page = doc[page_num]
        page_num_1 = page_num + 1

        drawings = page.get_drawings()
        images = page.get_images(full=True)

        if drawings or images:
            try:
                pix_cropped = page.get_pixmap(matrix=ZOOM, clip=CLIP)
                fname = f'fig_{page_num_1:04d}_1.png'
                pix_cropped.save(str(ch_fig_dir / fname))
                extracted.append((page_num_1, fname, len(drawings), len(images)))
            except Exception as e:
                print(f"  ! page {page_num_1} crop failed: {e}")

    return extracted


def main():
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    doc = fitz.open(idx['pdf'])
    print(f"PDF opened: {len(doc)} pages")
    print(f"Spec: {idx['spec_title']}")
    print()

    summary = []

    for ch in idx['chapters']:
        ch_num = ch['ch']
        start = ch['start']
        end = ch['end']
        print(f"=== Ch{ch_num:02d} {ch['en']} (p.{start}-{end}) ===")

        # 1. Extract text
        text = extract_text(doc, start, end, ch_num)
        raw_path = RAW_DIR / f'chapter_{ch_num:02d}_raw.md'
        with open(raw_path, 'w') as f:
            f.write(text)
        print(f"  text: {len(text):,} chars → {raw_path.name}")

        # 2. Extract figures
        figs = extract_figures(doc, start, end, ch_num)
        print(f"  figures: {len(figs)} pages with figures")
        summary.append({
            'ch': ch_num,
            'en': ch['en'],
            'zh': ch['zh'],
            'pages': end - start + 1,
            'text_chars': len(text),
            'fig_pages': len(figs),
        })

    # Write summary
    with open(OUT_ROOT / 'extraction_summary.json', 'w') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print()
    print("=== Summary ===")
    for s in summary:
        print(f"  Ch{s['ch']:02d}: {s['pages']:4d} pages, {s['text_chars']:7,d} chars, {s['fig_pages']:3d} fig pages")
    total_text = sum(s['text_chars'] for s in summary)
    total_figs = sum(s['fig_pages'] for s in summary)
    print(f"  TOTAL: {total_text:,} chars, {total_figs} fig pages")


if __name__ == '__main__':
    main()
