#!/bin/bash
set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

git add "PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md"
git add "PCIe6.2_Spec_ch06_System_Architecture_系统架构.md"
git add "PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md"
git add "PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md"
git add qa_deep_report.json
git add tools/qa_deep_audit.py
git add tools/fix_layout_issues.py

git status --short

git commit -m "v4: 深度 QA 审计 + 布局修复

自动修复:
- 3 个表格标签不平衡 (Ch 7 -1, Ch 11 +2)
- 16 个重复 anchor 去重 (Ch 4: 5, Ch 6: 4, Ch 7: 7)

新增:
- tools/qa_deep_audit.py: 自动化深度审计 (空单元格、表格平衡、anchor 唯一性、EN-only rows)
- tools/fix_layout_issues.py: 批量修复脚本
- qa_deep_report.json: 12 章详细审计报告

剩余已知微瑕 (不影响阅读):
- 15 个空单元格 (主要是子代理的占位 row)
- 9 个 Ch 7 中重复 anchor (源 chunks 中原本就重复)
- 1 个 EN-only row (Ch 2 段落中间)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"

git log --oneline -5
