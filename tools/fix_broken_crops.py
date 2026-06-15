#!/usr/bin/env python3
"""
Fix broken tight crops by re-rendering them as de-watermarked full-page crops
(150 DPI, header/footer stripped) — same as extract_pcie6_2.py.

Broken = size 0 (empty) OR very small (< 5KB) AND extreme aspect ratio
(width/height > 6 or < 0.17) OR very narrow strip (width < 200 or height < 100).
"""
import os
from pathlib import Path

import fitz
from PIL import Image

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
FIG_DIR = OUT_ROOT / 'figures'
PDF_PATH = '/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_all/NCB-PCI_Express_Base_6.2-2024-01-25.pdf'

ZOOM = 150 / 72
CLIP = fitz.Rect(0, 110, 1275, 1530)


def is_broken(f):
    size = os.path.getsize(f)
    if size == 0:
        return True
    try:
        im = Image.open(f)
        w, h = im.size
    except Exception:
        return True
    size_kb = size / 1024
    aspect = w / h if h else 0
    if size_kb < 5 and (w < 200 or h < 100 or aspect > 6 or aspect < 0.17):
        return True
    if aspect > 10 or aspect < 0.1:
        return True
    return False


def page_from_filename(name):
    """Extract page number from 'fig_PPPP_1.png'."""
    import re
    m = re.search(r'fig_(\d{4})_1\.png', name)
    if m:
        return int(m.group(1))
    return None


def re_render(doc, page_num, out_path):
    page = doc[page_num - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=CLIP)
    pix.save(str(out_path))


def main():
    broken = [f for f in FIG_DIR.glob('chapter_*/fig_*_1.png') if is_broken(f)]
    print(f"Found {len(broken)} broken figures")
    for f in broken:
        size = os.path.getsize(f) / 1024
        try:
            im = Image.open(f)
            dims = f"{im.size[0]}x{im.size[1]}"
        except Exception:
            dims = "?"
        print(f"  {f.relative_to(OUT_ROOT)}: {size:.1f}KB, {dims}")

    if not broken:
        print("\nNothing to fix")
        return

    doc = fitz.open(PDF_PATH)
    print(f"\nRe-rendering {len(broken)} figures from PDF...")

    n_fixed = 0
    for f in broken:
        page_num = page_from_filename(f.name)
        if page_num is None:
            print(f"  ! cannot parse page from {f.name}")
            continue
        try:
            re_render(doc, page_num, f)
            n_fixed += 1
            new_size = os.path.getsize(f) / 1024
            im = Image.open(f)
            print(f"  ✓ {f.relative_to(OUT_ROOT)}: {new_size:.1f}KB, {im.size}")
        except Exception as e:
            print(f"  ✗ {f.name}: {e}")

    doc.close()
    print(f"\nFixed {n_fixed} figures")


if __name__ == '__main__':
    main()
