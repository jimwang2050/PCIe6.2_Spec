#!/bin/bash
set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

echo "=== Current state ==="
git log --oneline -3
echo "---"
git rev-parse HEAD
echo "---"

# Re-amend the test commit with proper message and figures
git commit --amend -m "Add 1576 figures (318 MB) extracted from PCIe 6.2 PDF

- 12 chapter subdirs: figures/chapter_01/ ... figures/chapter_12/
- 150 DPI PNG renders, de-watermarked (page header/footer cropped)
- Original filenames: fig_PPPP_1.png (4-digit page, 1-indexed)
- Total disk size: 318 MB

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"

echo ""
echo "=== After amend ==="
git log --oneline -3
echo "---"
git show --stat HEAD 2>&1 | head -10
echo "---"
git status --short
