#!/usr/bin/env python3
"""
通用化章节精裁剪工具 (ch04 模板推广版)

支持任意章节 1-12,自动从 chapter_index.json 读取页范围,
从 MinerU content_list.json 抽取 Figure caption 匹配的 bbox,
并按 150 DPI 渲染或直接复制 MinerU JPG。

输出:
- figures/chapter_NN/fig_PPPP_NN_tight.png
- ch{N}_tight_crops.json
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
INDEX_PATH = ROOT / 'chapter_index.json'

ZOOM = fitz.Matrix(150 / 72, 150 / 72)
PADDING = 0.04

# Match "Figure N-NN ..." or "Table N-NN ..." (in captions of any chapter)
FIG_CAPTION_RE = re.compile(r'^(?:Figure|Fiqure|FIG) (\d+)-(\d+)\s+(.*?)(?:\s*§)?$', re.IGNORECASE)


def find_pdf_for_page(page_num):
    for pdf in sorted(PDF_DIR.glob('chunk_*.pdf')):
        m = re.search(r'pages_(\d+)-(\d+)', pdf.name)
        if m:
            s, e = int(m.group(1)), int(m.group(2))
            if s <= page_num <= e:
                return pdf
    return None


def render_or_copy(pdf_path, page_num, bbox, out_path, mineru_img_path=None):
    """Render tight crop at 150 DPI from PDF, or copy MinerU JPG."""
    if mineru_img_path:
        m_img = Path(mineru_img_path)
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

    doc = fitz.open(pdf_path)
    m = re.search(r'pages_(\d+)-(\d+)', Path(pdf_path).name)
    chunk_start = int(m.group(1)) if m else 0
    local_idx = page_num - chunk_start
    page = doc[local_idx]
    x1, y1, x2, y2 = bbox
    w, h = x2 - x1, y2 - y1
    pad_x, pad_y = w * PADDING, h * PADDING
    pw, ph = page.rect.width, page.rect.height
    clip = fitz.Rect(max(0, x1-pad_x), max(0, y1-pad_y),
                     min(pw, x2+pad_x), min(ph, y2+pad_y))
    pix = page.get_pixmap(matrix=ZOOM, clip=clip)
    pix.save(str(out_path))
    doc.close()
    return clip


def process_chapter(ch_num, start_page, end_page):
    print(f"\n{'='*60}\nCh{ch_num:02d}: pages {start_page}-{end_page}\n{'='*60}")
    fig_dir = ROOT / 'figures' / f'chapter_{ch_num:02d}'
    fig_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: collect figures from MinerU
    page_figs = defaultdict(list)
    for chunk_dir in sorted(MINERU_DIR.iterdir()):
        if not chunk_dir.is_dir(): continue
        cl_files = list(chunk_dir.glob('*_content_list.json'))
        if not cl_files: continue
        m = re.search(r'pages_(\d+)-(\d+)', chunk_dir.name)
        if not m: continue
        chunk_start, chunk_end = int(m.group(1)), int(m.group(2))
        if chunk_end < start_page or chunk_start > end_page: continue

        with open(cl_files[0]) as f:
            content_list = json.load(f)

        for item in content_list:
            if item.get('type') not in ('image', 'table', 'chart'): continue
            captions = (item.get('image_caption', []) or
                        item.get('table_caption', []) or
                        item.get('chart_caption', []))
            if not captions: continue
            cap = captions[0]
            m2 = FIG_CAPTION_RE.match(cap.strip())
            if not m2: continue
            ch_n, fnum = int(m2.group(1)), int(m2.group(2))
            if ch_n != ch_num: continue  # 只处理当前章节
            cap_text = m2.group(3).strip()
            page_idx = item.get('page_idx', 0)
            page_num = chunk_start + page_idx
            if not (start_page <= page_num <= end_page): continue
            bbox = item.get('bbox')
            img_path = item.get('img_path', '')
            page_figs[page_num].append((ch_num, fnum, cap_text, bbox, img_path))

    total = sum(len(v) for v in page_figs.values())
    print(f"Discovered ch{ch_num} figures: {total} across {len(page_figs)} pages")

    # Step 2: render each figure
    rendered_map = {}
    per_page_count = defaultdict(int)
    n_ok = n_manual = n_fail = 0

    for pg in sorted(page_figs):
        figs = sorted(page_figs[pg], key=lambda x: (x[3][1] if x[3] else 0))
        for ch_n, fnum, cap_text, bbox, mineru_path in figs:
            per_page_count[pg] += 1
            idx = per_page_count[pg]
            out_name = f'fig_{pg:04d}_{idx}_tight.png'
            out_path = fig_dir / out_name
            pdf_path = find_pdf_for_page(pg)
            if not pdf_path:
                print(f"  ! p.{pg} Figure {ch_n}-{fnum}: no PDF")
                n_fail += 1
                continue
            try:
                if bbox is None and mineru_path is None:
                    full_img = fig_dir / f'fig_{pg:04d}_1.png'
                    if full_img.exists():
                        import shutil
                        shutil.copy(full_img, out_path)
                        from PIL import Image
                        im = Image.open(out_path)
                        clip = (0, 0, im.size[0], im.size[1])
                        n_manual += 1
                    else:
                        raise FileNotFoundError(f'No full-page image for p.{pg}')
                else:
                    clip = render_or_copy(pdf_path, pg, bbox, out_path, mineru_img_path=mineru_path)
                key = f'Figure {ch_n}-{fnum}'
                if key in rendered_map:
                    key = f'Figure {ch_n}-{fnum}#{idx}'
                rendered_map[key] = {
                    'page': pg, 'file': out_name, 'bbox': bbox,
                    'caption': cap_text, 'pdf_chunk': Path(pdf_path).name,
                    'mineru_image': mineru_path,
                }
                w, h = int(clip[2]-clip[0]), int(clip[3]-clip[1])
                marker = '~' if bbox is None and mineru_path is None else '✓'
                print(f"  {marker} p.{pg} Figure {ch_n}-{fnum} → {out_name} ({w}×{h} px)")
                n_ok += 1
            except Exception as e:
                print(f"  ✗ p.{pg} Figure {ch_n}-{fnum}: {e}")
                n_fail += 1

    out_json = {
        'chapter': ch_num,
        'page_range': [start_page, end_page],
        'total_figures': n_ok,
        'total_manual': n_manual,
        'total_failed': n_fail,
        'figures': rendered_map,
    }
    out_path = ROOT / f'ch{ch_num}_tight_crops.json'
    with open(out_path, 'w') as f:
        json.dump(out_json, f, indent=2, ensure_ascii=False)
    print(f"\nMapping: {out_path}")
    print(f"Rendered: {n_ok} ({n_manual} manual) | Failed: {n_fail}")
    return n_ok, n_fail


def main():
    chapters = sys.argv[1:]  # e.g. '5' '5-8' '5,7,9'
    if not chapters:
        # Default: all chapters
        with open(INDEX_PATH) as f:
            idx = json.load(f)
        chs = idx.get('chapters', [])
    else:
        # Parse chapter list
        with open(INDEX_PATH) as f:
            idx = json.load(f)
        all_chs = {c['ch']: c for c in idx.get('chapters', [])}
        chs = []
        for arg in chapters:
            if '-' in arg:
                s, e = arg.split('-')
                chs.extend(c for c in all_chs.values() if s.isdigit() and e.isdigit() and int(s) <= c['ch'] <= int(e))
            elif ',' in arg:
                chs.extend(all_chs[int(x)] for x in arg.split(',') if x.strip().isdigit())
            else:
                chs.append(all_chs[int(arg)])

    print(f"Processing {len(chs)} chapters: {[c['ch'] for c in chs]}")
    total_ok = total_fail = 0
    for ch in chs:
        ok, fail = process_chapter(ch['ch'], ch['start'], ch['end'])
        total_ok += ok
        total_fail += fail
    print(f"\n=== Total: Rendered {total_ok} | Failed {total_fail} ===")


if __name__ == '__main__':
    main()
