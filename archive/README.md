# Archived project artifacts

本目录用于归档 PCIe 6.2 翻译项目的过程文档、质量报告、修复记录和一次性维护脚本，避免与主要阅读内容混在仓库根目录。

## 归档范围

### 过程与质量文档

- `CH4_FIGURE_STRATEGY.md`
- `CHECKLIST.md`
- `FIX_LOG.md`
- `FIX_emoji_report.md`
- `QUALITY_IMPROVEMENT_PLAN.md`
- `REVIEW_20260715.md`
- `REVIEW_ch04_audit_report.md`
- `REVIEW_full_audit_report.md`
- `SELF_CHECK_REPORT.md`
- `qa_report.json`
- `qa_deep_report.json`

### 一次性维护脚本

- `add_missing_anchors.py`
- `fix_anchors.py`
- `fix_ch07_all_orphans.py`
- `fix_ch07_table.py`
- `fix_ch07_tables.py`
- `fix_toc_links.py`

这些文件保留在 Git 历史中，并在后续整理中移入本目录；主要内容仍位于仓库根目录：README、12 个章节 Markdown、`figures/`、`preview/`、`book.md`、`chapter_index.json`、`glossary.json`、`tools/` 和 `tight_crops/`。

> 说明：GitHub 文件 API 不支持单次目录移动；本次先建立归档入口和清单，后续可在本地使用 `git mv` 完成上述文件的实际迁移，并提交为一次原子变更。
