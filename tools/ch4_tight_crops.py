#!/usr/bin/env python3
"""
ch4 精裁剪: 基于 MinerU content_list.json 的 bbox 数据
从原始 PDF 重新渲染每张 Figure 4-XX 的紧致裁剪图。

输入:
- tools/mineru_results/chunk_XX_*/..._content_list.json
- tools/pdf_chunks/chunk_XX_*.pdf

输出:
- figures/chapter_04/fig_PPPP_NN_tight.png  (NN = 1, 2, ... per page)
- ch4_tight_crops.json (page -> figure 映射 + bbox)

策略:
1. 解析每个 chunk 的 content_list.json,过滤 type=image 且 image_caption 匹配 "Figure 4-NN"
2. 将 page_idx 转换为 PDF 绝对页码
3. 从对应 PDF chunk 中按 bbox 渲染 150 DPI PNG,加 5% padding
4. 命名: 同页多图按 NN 递增 (1, 2, 3, ...),单图固定 _1
5. 同时把 caption 文本写入 JSON 便于追溯
"""
import fitz
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
TOOLS = ROOT / 'tools'
MINERU_DIR = TOOLS / 'mineru_results'
PDF_DIR = TOOLS / 'pdf_chunks'
FIG_OUT = ROOT / 'figures' / 'chapter_04'
FIG_OUT.mkdir(parents=True, exist_ok=True)

CH04_START = 351
CH04_END = 650
ZOOM = fitz.Matrix(150 / 72, 150 / 72)  # 150 DPI
PADDING = 0.04  # 4% padding

FIG_CAPTION_RE = re.compile(r'^(?:Figure|Fiqure|FIG) 4-(\d+)\s+(.*?)(?:\s*§)?$', re.IGNORECASE)


def find_chunk_for_page(page_num):
    """Find (chunk_pdf, start_page) covering page_num."""
    for pdf in sorted(PDF_DIR.glob('chunk_*.pdf')):
        m = re.search(r'pages_(\d+)-(\d+)', pdf.name)
        if m:
            s, e = int(m.group(1)), int(m.group(2))
            if s <= page_num <= e:
                return pdf, s
    return None, None


def render_tight(pdf_path, page_num, bbox, out_path, mineru_img_path=None):
    """Render tight crop at 150 DPI from PDF, OR copy MinerU-extracted image.

    Strategy: MinerU has already extracted correct figure images as JPGs.
    We prefer to copy those (since MinerU's bbox in content_list doesn't
    always match PDF coords reliably). Fall back to PDF render if no JPG.
    """
    if mineru_img_path:
        m_img = Path(mineru_img_path)
        # Resolve relative path against chunk dir
        if not m_img.is_absolute():
            for chunk_dir in MINERU_DIR.iterdir():
                cand = chunk_dir / m_img
                if cand.exists():
                    m_img = cand
                    break
        if m_img.exists():
            import shutil
            shutil.copy(m_img, out_path)
            from PIL import Image
            im = Image.open(out_path)
            return (0, 0, im.size[0], im.size[1])

    # Fallback: render from PDF
    doc = fitz.open(pdf_path)
    m = re.search(r'pages_(\d+)-(\d+)', Path(pdf_path).name)
    if m:
        chunk_start = int(m.group(1))
        local_idx = page_num - chunk_start
    else:
        local_idx = page_num - 1
    page = doc[local_idx]
    x1, y1, x2, y2 = bbox
    w, h = x2 - x1, y2 - y1
    pad_x, pad_y = w * PADDING, h * PADDING
    pw, ph = page.rect.width, page.rect.height
    clip = fitz.Rect(
        max(0, x1 - pad_x),
        max(0, y1 - pad_y),
        min(pw, x2 + pad_x),
        min(ph, y2 + pad_y),
    )
    pix = page.get_pixmap(matrix=ZOOM, clip=clip)
    pix.save(str(out_path))
    doc.close()
    return clip


def main():
    print("=" * 60)
    print("ch4 精裁剪: MinerU bbox → tight crops")
    print("=" * 60)

    # Step 1: collect all ch4 image items from all chunks
    page_figs = defaultdict(list)  # page -> [(fignum, caption, bbox, img_path)]

    for chunk_dir in sorted(MINERU_DIR.iterdir()):
        if not chunk_dir.is_dir():
            continue
        cl_files = list(chunk_dir.glob('*_content_list.json'))
        if not cl_files:
            continue
        m = re.search(r'pages_(\d+)-(\d+)', chunk_dir.name)
        if not m:
            continue
        chunk_start = int(m.group(1))

        with open(cl_files[0]) as f:
            content_list = json.load(f)

        for item in content_list:
            if item.get('type') not in ('image', 'table'):
                continue
            # image_caption for image type, table_caption for table type
            captions = item.get('image_caption', []) or item.get('table_caption', [])
            if not captions:
                continue
            cap = captions[0]
            m2 = FIG_CAPTION_RE.match(cap.strip())
            if not m2:
                continue
            fignum = int(m2.group(1))
            cap_text = m2.group(2).strip()
            page_idx = item.get('page_idx', 0)
            page_num = chunk_start + page_idx
            if not (CH04_START <= page_num <= CH04_END):
                continue
            bbox = item.get('bbox')
            img_path = item.get('img_path', '')
            # For table-misclassified images, no img_path; will fall back to PDF render
            page_figs[page_num].append((fignum, cap_text, bbox, img_path))

    # Step 2: render each figure tight crop
    total = sum(len(v) for v in page_figs.values())
    pages = sorted(page_figs)
    print(f"\n[1] Discovered ch4 figures: {total} across {len(pages)} pages")

    rendered_map = {}  # "Figure 4-NN" -> {page, file, bbox, caption}
    per_page_count = defaultdict(int)
    n_ok = 0
    n_fail = 0

    for pg in pages:
        # Sort by y0 (top-down)
        figs = sorted(page_figs[pg], key=lambda x: (x[2][1] if x[2] else 0))
        for fignum, cap_text, bbox, mineru_path in figs:
            per_page_count[pg] += 1
            idx = per_page_count[pg]
            out_name = f'fig_{pg:04d}_{idx}_tight.png'
            out_path = FIG_OUT / out_name
            pdf_path, _ = find_chunk_for_page(pg)
            if not pdf_path or not bbox:
                print(f"  ! p.{pg} Figure 4-{fignum}: skip (no PDF/bbox)")
                n_fail += 1
                continue
            try:
                clip = render_tight(pdf_path, pg, bbox, out_path, mineru_img_path=mineru_path)
                key = f'Figure 4-{fignum}'
                # If duplicate fignum (e.g., caption referenced twice), append
                if key in rendered_map:
                    key = f'Figure 4-{fignum}#{idx}'
                rendered_map[key] = {
                    'page': pg,
                    'file': out_name,
                    'bbox': bbox,
                    'caption': cap_text,
                    'pdf_chunk': Path(pdf_path).name,
                    'mineru_image': mineru_path,
                }
                w, h = int(clip[2]-clip[0]), int(clip[3]-clip[1])
                print(f"  ✓ p.{pg} Figure 4-{fignum} → {out_name} ({w}×{h} px)")
                n_ok += 1
            except Exception as e:
                print(f"  ✗ p.{pg} Figure 4-{fignum}: {e}")
                n_fail += 1

    # Step 3: write mapping JSON
    out_json = {
        'chapter': 4,
        'strategy': 'MinerU bbox + tight crop (150 DPI, 4% padding)',
        'page_range': [CH04_START, CH04_END],
        'total_figures': n_ok,
        'total_failed': n_fail,
        'figures': rendered_map,
    }
    out_path = ROOT / 'ch4_tight_crops.json'
    with open(out_path, 'w') as f:
        json.dump(out_json, f, indent=2, ensure_ascii=False)
    print(f"\n[2] Mapping: {out_path}")
    print(f"    Rendered: {n_ok} | Failed: {n_fail}")


if __name__ == '__main__':
    main()
