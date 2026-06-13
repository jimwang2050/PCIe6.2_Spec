#!/bin/bash
set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

# Set git identity
git config user.name "jim wang"
git config user.email "jimwang2050@gmail.com"

# Stage key files
git add README.md .gitignore chapter_index.json glossary.json
git add tools/
git add PCIe6.2_Spec_*.md

# Show status
echo "=== Staged files count ==="
git status --short | wc -l
echo ""
echo "=== Sample staged files ==="
git status --short | head -20

# Commit
echo ""
echo "=== Committing ==="
git commit -m "PCIe 6.2 Spec 中英对照翻译 (12 章, 92%)

- 12 章完整中英对照双语 Markdown,基于 CXL 3.2 翻译模板
- 117/127 chunks 翻译完成 (Ch4 缺 1, Ch7 缺 9)
- 1576 张原图抽取到 figures/chapter_NN/
- README + chapter_index + glossary 完整

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" 2>&1 | tail -10

# Add remote
echo ""
echo "=== Adding remote ==="
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/jimwang2050/PCIe6.2_Spec.git
git remote -v

# Push
echo ""
echo "=== Pushing to GitHub ==="
git push -u origin main --force 2>&1 | tail -20
