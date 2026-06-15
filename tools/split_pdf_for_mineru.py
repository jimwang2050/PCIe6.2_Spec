#!/usr/bin/env python3
"""
Split PCIe 6.2 PDF (2111 pages) into 200-page chunks for MinerU batch processing.

Each chunk + its page range is submitted to MinerU. The content_list.json
returned tells us image positions; we re-render tight crops locally with
PyMuPDF.

Usage:
    python3 tools/split_pdf_for_mineru.py

Output: tools/pdf_chunks/chunk_NN_pages_X-Y.pdf
"""
import os
import sys
from pathlib import Path

import fitz  # PyMuPDF

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHUNKS_DIR = OUT_ROOT / 'tools' / 'pdf_chunks'
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

PDF_PATH = '/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_all/NCB-PCI_Express_Base_6.2-2024-01-25.pdf'
PAGE_PER_CHUNK = 200


def main():
    doc = fitz.open(PDF_PATH)
    total = len(doc)
    print(f"Total pages: {total}")

    # Skip first 1-126 (front matter: TOC, lists, etc.). Start from page 127 (Ch 1).
    # User's chapter range is 127-1702 (1-indexed). Pages 1-126 are front matter.
    # Pages 1703+ are appendices (out of scope).
    START_PAGE = 127  # 1-indexed
    END_PAGE = 1702

    chunk_num = 1
    page = START_PAGE
    while page <= END_PAGE:
        chunk_end = min(page + PAGE_PER_CHUNK - 1, END_PAGE)
        # PyMuPDF is 0-indexed; we use 1-indexed for MinerU
        doc_chunk = fitz.open()
        doc_chunk.insert_pdf(doc, from_page=page - 1, to_page=chunk_end - 1)
        out_path = CHUNKS_DIR / f"chunk_{chunk_num:02d}_pages_{page}-{chunk_end}.pdf"
        doc_chunk.save(str(out_path))
        doc_chunk.close()
        size_mb = out_path.stat().st_size / 1024 / 1024
        print(f"  chunk_{chunk_num:02d}_pages_{page}-{chunk_end}.pdf: {size_mb:.1f} MB ({chunk_end - page + 1} pages)")
        page = chunk_end + 1
        chunk_num += 1

    print(f"\nTotal chunks: {chunk_num - 1}")
    print(f"Output dir: {CHUNKS_DIR}")


if __name__ == '__main__':
    main()
