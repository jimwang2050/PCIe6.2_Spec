#!/usr/bin/env python3
"""
Process MinerU results and re-render tight crop figures.

For each chunk in tools/mineru_results/:
1. Parse content_list.json to get image items with (page_idx, bbox, img_path)
2. Map back to original PDF page (chunk_start + page_idx)
3. Render tight crop at high DPI from the original PDF

Original figure naming preserved: fig_PPPP_1.png
"""
import json
import re
from pathlib import Path

import fitz  # PyMuPDF

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
RESULTS_DIR = OUT_ROOT / 'tools' / 'mineru_results'
FIGURES_DIR = OUT_ROOT / 'figures'

PDF_PATH = '/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_all/NCB-PCI_Express_Base_6.2-2024-01-25.pdf'
ZOOM = 2.0  # 144 dpi (72 * 2.0)
PADDING_PCT = 0.05  # 5% padding around bbox


def parse_chunk_name(name):
    """Extract start page from 'chunk_NN_pages_X-Y' name."""
    m = re.search(r'pages_(\d+)-(\d+)', name)
    if m:
        return int(m.group(1))
    return None


def render_tight_crop(doc, page_num_1indexed, bbox, out_path):
    """Render the bbox region from page_num (1-indexed) of doc to out_path."""
    page = doc[page_num_1indexed - 1]
    page_w, page_h = page.rect.width, page.rect.height

    x1, y1, x2, y2 = bbox
    # Add 5% padding
    w = x2 - x1
    h = y2 - y1
    pad_x = w * PADDING_PCT
    pad_y = h * PADDING_PCT
    x1 = max(0, x1 - pad_x)
    y1 = max(0, y1 - pad_y)
    x2 = min(page_w, x2 + pad_x)
    y2 = min(page_h, y2 + pad_y)

    clip = fitz.Rect(x1, y1, x2, y2)
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), clip=clip)
    pix.save(str(out_path))
    return out_path


def process_chunk(chunk_dir):
    name = chunk_dir.name
    start_page = parse_chunk_name(name)
    if start_page is None:
        print(f"  [SKIP] cannot parse {name}")
        return 0, 0

    # Find content_list.json
    cl_files = list(chunk_dir.glob('*_content_list.json')) + list(chunk_dir.glob('*_content_list_v2.json'))
    if not cl_files:
        print(f"  [SKIP] no content_list.json in {name}")
        return 0, 0
    cl_path = cl_files[0]

    with open(cl_path) as f:
        content_list = json.load(f)

    # Filter image items
    images = [item for item in content_list if item.get('type') == 'image']
    if not images:
        print(f"  [SKIP] no images in {name}")
        return 0, 0

    # Determine chapter from page number
    # Ch 1: 127-140, Ch 2: 141-308, Ch 3: 309-350, Ch 4: 351-650, ...
    chapters = {
        1: (127, 140), 2: (141, 308), 3: (309, 350), 4: (351, 650),
        5: (651, 706), 6: (707, 980), 7: (981, 1408), 8: (1409, 1522),
        9: (1523, 1558), 10: (1559, 1608), 11: (1609, 1658), 12: (1659, 1702),
    }

    doc = fitz.open(PDF_PATH)
    n_rendered = 0
    n_skipped = 0

    # Use image_path as dedup key
    seen_img_paths = set()

    for item in images:
        img_path_rel = item.get('img_path', '')
        # Use the basename without ext as dedup key
        img_id = Path(img_path_rel).stem
        if img_id in seen_img_paths:
            n_skipped += 1
            continue
        seen_img_paths.add(img_id)

        # Map to original page
        page_idx = item.get('page_idx', 0)
        actual_page = start_page + page_idx
        bbox = item.get('bbox', [])

        if not bbox or len(bbox) != 4:
            n_skipped += 1
            continue

        # Find which chapter
        ch_num = None
        for cn, (s, e) in chapters.items():
            if s <= actual_page <= e:
                ch_num = cn
                break
        if ch_num is None:
            n_skipped += 1
            continue

        ch_fig_dir = FIGURES_DIR / f'chapter_{ch_num:02d}'
        ch_fig_dir.mkdir(parents=True, exist_ok=True)

        out_path = ch_fig_dir / f'fig_{actual_page:04d}_1.png'
        try:
            render_tight_crop(doc, actual_page, bbox, out_path)
            n_rendered += 1
        except Exception as e:
            print(f"    error rendering {img_id}: {e}")
            n_skipped += 1

    doc.close()
    return n_rendered, n_skipped


def main():
    chunks = sorted(RESULTS_DIR.glob('chunk_*'))
    chunks = [c for c in chunks if (c / 'full.md').exists()]
    print(f"Processing {len(chunks)} chunks with results...")
    print()

    total_rendered = 0
    total_skipped = 0
    for chunk_dir in chunks:
        print(f"  {chunk_dir.name}...", end=' ', flush=True)
        rendered, skipped = process_chunk(chunk_dir)
        print(f"rendered {rendered}, skipped {skipped}")
        total_rendered += rendered
        total_skipped += skipped

    print()
    print(f"=== Summary ===")
    print(f"  Rendered: {total_rendered}")
    print(f"  Skipped:  {total_skipped}")
    print(f"  Total figures in figures/: ", end='')
    n = sum(1 for _ in FIGURES_DIR.glob('chapter_*/fig_*_1.png'))
    print(n)


if __name__ == '__main__':
    main()
