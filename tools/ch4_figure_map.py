#!/usr/bin/env python3
"""
ch4 章节 figure 映射 + 精裁剪策略

步骤:
1. 解析 raw/chapter_04_raw.md 中的 PAGE_BREAK + Figure 标题
2. 构建 page -> [figure numbers] 映射
3. 与 figures/chapter_04/ 中已有图交叉对比,识别:
   - 缺失: 源 spec 有图但未抽取
   - 多图: 同一页多张 figure 共享一张全页图
4. 对每张图,在 PDF 中用 PyMuPDF 找到 caption bbox,反向向上推断
   figure 实际 bbox,导出 fig_PPPP_NN_tight.png
5. 输出 ch4_figure_map.json
"""
import fitz
import json
import re
import os
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
RAW_MD = ROOT / 'raw' / 'chapter_04_raw.md'
FIG_DIR = ROOT / 'figures' / 'chapter_04'
PDF_DIR = ROOT / 'tools' / 'pdf_chunks'

# ch04 spans pages 351-650
CH04_START = 351
CH04_END = 650

# Figure caption regex (in raw text)
FIG_RE = re.compile(r'^Figure 4-(\d+)\s+(.+?)$', re.MULTILINE)
TABLE_RE = re.compile(r'^Table 4-(\d+)\s+(.+?)$', re.MULTILINE)
PAGE_BREAK_RE = re.compile(r'<<<PAGE_BREAK>>> page_(\d+)')


def find_pdf_for_page(page_num):
    """Find which PDF chunk contains this page (0-indexed in PyMuPDF)."""
    for pdf_path in sorted(PDF_DIR.glob('chunk_*.pdf')):
        m = re.search(r'pages_(\d+)-(\d+)', pdf_path.name)
        if m:
            start, end = int(m.group(1)), int(m.group(2))
            if start <= page_num <= end:
                return pdf_path
    return None


def parse_raw_md():
    """Parse raw markdown to map page -> figures/tables."""
    with open(RAW_MD) as f:
        text = f.read()

    # Split by page breaks
    page_map = {}
    parts = re.split(r'<<<PAGE_BREAK>>> page_(\d+)', text)
    for i in range(1, len(parts), 2):
        pg = int(parts[i])
        content = parts[i+1] if i+1 < len(parts) else ''
        page_map[pg] = content

    figure_pages = defaultdict(list)  # fig_num -> [page, ...]
    table_pages = defaultdict(list)
    page_figs = defaultdict(list)  # page -> [fig_num, ...]
    page_tables = defaultdict(list)

    for pg, content in page_map.items():
        for m in FIG_RE.finditer(content):
            fnum = int(m.group(1))
            figure_pages[fnum].append(pg)
            page_figs[pg].append(fnum)
        for m in TABLE_RE.finditer(content):
            tnum = int(m.group(1))
            table_pages[tnum].append(pg)
            page_tables[pg].append(tnum)

    return figure_pages, table_pages, page_figs, page_tables


def analyze():
    print("=" * 60)
    print("ch04 Figure Mapping Analysis")
    print("=" * 60)

    figure_pages, table_pages, page_figs, page_tables = parse_raw_md()

    # 1) List all figure captions found in spec
    print(f"\n[1] Total unique figures in spec: {len(figure_pages)}")
    print(f"    Figure numbers: {sorted(figure_pages.keys())}")

    # 2) Per-page figure distribution
    print(f"\n[2] Pages with figure captions: {len(page_figs)}")
    multi_fig_pages = {p: f for p, f in page_figs.items() if len(f) > 1}
    print(f"    Pages with multiple figures: {len(multi_fig_pages)}")
    for p in sorted(multi_fig_pages):
        print(f"      p.{p}: figs={multi_fig_pages[p]}")

    # 3) Cross-check with existing image extraction
    print(f"\n[3] Existing image files in figures/chapter_04/:")
    existing = {}
    for f in FIG_DIR.glob('fig_*.png'):
        m = re.match(r'fig_(\d+)_(\d+)\.png', f.name)
        if m:
            pg, n = int(m.group(1)), int(m.group(2))
            existing.setdefault(pg, []).append((n, f.name))

    pages_with_figs = sorted(p for p in page_figs if p in existing)
    pages_with_figs_no_image = sorted(set(page_figs) - set(existing))
    pages_with_image_no_fig = sorted(set(existing) - set(page_figs))

    print(f"    Pages with figure + image: {len(pages_with_figs)}")
    print(f"    Pages with figure but NO image: {len(pages_with_figs_no_image)}")
    if pages_with_figs_no_image:
        print(f"      Missing: {pages_with_figs_no_image[:20]}")
    print(f"    Pages with image but no figure caption: {len(pages_with_image_no_fig)}")
    if pages_with_image_no_fig:
        print(f"      Stray: {pages_with_image_no_fig[:20]}")

    # 4) Build final mapping
    out_map = {
        'chapter': 4,
        'page_range': [CH04_START, CH04_END],
        'figures': {},
        'tables': {},
        'missing_extractions': [],
        'multi_figure_pages': [],
    }
    for fnum in sorted(figure_pages):
        pages = sorted(set(figure_pages[fnum]))
        out_map['figures'][f'Figure 4-{fnum}'] = {
            'pages': pages,
            'image_file': f'fig_{pages[0]:04d}_1.png' if pages and pages[0] in existing else None,
            'available': pages[0] in existing if pages else False,
        }
    for tnum in sorted(table_pages):
        pages = sorted(set(table_pages[tnum]))
        out_map['tables'][f'Table 4-{tnum}'] = {
            'pages': pages,
        }
    out_map['missing_extractions'] = pages_with_figs_no_image
    out_map['multi_figure_pages'] = [
        {'page': p, 'figures': f} for p, f in sorted(multi_fig_pages.items())
    ]

    out_path = ROOT / 'ch4_figure_map.json'
    with open(out_path, 'w') as f:
        json.dump(out_map, f, indent=2, ensure_ascii=False)
    print(f"\n[4] Mapping written: {out_path}")
    print(f"    Total figures: {len(out_map['figures'])}")
    print(f"    Total tables: {len(out_map['tables'])}")
    print(f"    Missing extractions: {len(out_map['missing_extractions'])}")
    print(f"    Pages needing multi-figure split: {len(out_map['multi_figure_pages'])}")


if __name__ == '__main__':
    analyze()
