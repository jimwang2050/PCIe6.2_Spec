#!/bin/bash
set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

git add README.md \
  "PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md" \
  "PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md"

git status --short

git commit -m "v2 完整版 (100% 完成)

- 翻译完成剩余 10 chunks: Ch 4 chapter_04_ai + Ch 7 chapter_07_bi..bq
- 重新 merge 章节 MD (v1 92% → v2 100%)
- 更新 README: 12/12 章 + 127/127 chunks, 移除 TODO 段
- Ch 4 物理层逻辑块: 27 → 27 chunks 完整
- Ch 7 软件初始化: 34 → 43 chunks 完整 (399 sections, 1.7M chars)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"

git log --oneline -5
