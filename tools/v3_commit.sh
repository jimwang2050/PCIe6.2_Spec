#!/bin/bash
set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

# Stage v3: HTML previews + combined book + QA report + new tools
git add book.md
git add preview/
git add qa_report.json
git add tools/build_html_preview.sh
git add tools/qa_audit.py

git status --short

git commit -m "v3: HTML 预览 + 组合 book + QA 审计

新增内容:
- preview/ — 14 个 HTML 文件 (13 章 + 索引),可用浏览器离线阅读
- preview/book.html — 完整组合版 (8.4 MB, 含目录 TOC)
- book.md — 12 章合并 MD (7.2 MB, 129,341 行)
- qa_report.json — 12 章详细审计数据
- tools/build_html_preview.sh — HTML 生成脚本
- tools/qa_audit.py — 自动化 QA 审计

QA 关键指标:
- 12/12 章 100% 完整
- 1,011 张图引用
- 4,524 灰底中文单元
- 641,900 中文字符 + 3,675,874 英文字符
- ZH/EN 比 14.9% (典型技术翻译比例)

已知微瑕: Ch 7 / Ch 11 各有 1-2 个未关闭的 </table> (子代理嵌套表格,4524 单元中 99.96% 正常)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"

git log --oneline -5
