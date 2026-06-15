#!/usr/bin/env python3
"""
For Ch 4 (Physical Layer Logical Block), re-render ALL figures as
150 DPI full-page renders (de-watermarked). The tight crops via
MinerU bbox detection often miss multi-page figures (state diagrams,
timing diagrams that span columns). Full-page is the safe choice.

Other chapters can stay with their mixed rendering (full-page for
MinerU-unrecognized pages, tight crop for recognized figures).
"""
import re
from pathlib import Path

import fitz

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
FIG_DIR = OUT_ROOT / 'figures' / 'chapter_04'
PDF_PATH = '/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_all/NCB-PCI_Express_Base_6.2-2024-01-25.pdf'

ZOOM = 150 / 72
CLIP = fitz.Rect(0, 110, 1275, 1530)


def main():
    figs = sorted(FIG_DIR.glob('fig_*_1.png'))
    print(f"Re-rendering {len(figs)} Ch 4 figures as full-page (150 DPI de-watermarked)...")

    doc = fitz.open(PDF_PATH)
    n = 0
    for f in figs:
        m = re.search(r'fig_(\d{4})_1\.png', f.name)
        if not m:
            continue
        page_num = int(m.group(1))
        page = doc[page_num - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=CLIP)
        pix.save(str(f))
        n += 1
    doc.close()
    print(f"Done: {n} figures re-rendered as full-page")


if __name__ == '__main__':
    main()
