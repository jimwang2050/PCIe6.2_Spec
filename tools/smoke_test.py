#!/usr/bin/env python3
import json
import fitz
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')

with open(OUT_ROOT / 'chapter_index.json') as f:
    idx = json.load(f)
ch1 = idx['chapters'][0]
doc = fitz.open(idx['pdf'])
p = doc[ch1['start'] - 1]  # page 127
print(f'Sample page {ch1["start"]} text first 500 chars:')
print(p.get_text('text')[:500])
print()
print('--- draw check ---')
print(f'  drawings: {len(p.get_drawings())}')
print(f'  images: {len(p.get_images())}')
print()
# Also check page size for crop params
rect = p.rect
print(f'Page rect: {rect} (w x h in PDF points)')
print(f'At 150 dpi, page = {int(rect.width*150/72)} x {int(rect.height*150/72)} px')
