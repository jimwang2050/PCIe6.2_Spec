# PCIe 6.2 Spec 中英对照翻译 — Code Wiki

> **项目**: PCI Express® Base Specification Revision 6.2 中英对照双语翻译工程
> **源 PDF**: `NCB-PCI_Express_Base_6.2-2024-01-25.pdf` (2111 页，27.8 MB)
> **范围**: 第 1–12 章（PDF 页码 127–1702），附录 A–L 不在范围内
> **模板**: 基于 [CXL 3.2 Spec 中英对照翻译](https://github.com/jimwang2050/CXL_3.2_Spec)
> **GitHub**: https://github.com/jimwang2050/PCIe6.2_Spec
> **进度**: 12/12 章 100% 完成（127 chunks）

---

## 目录

1. [项目概述](#1-项目概述)
2. [目录结构](#2-目录结构)
3. [整体架构与流水线](#3-整体架构与流水线)
4. [核心模块职责](#4-核心模块职责)
5. [关键脚本与函数说明](#5-关键脚本与函数说明)
6. [依赖关系](#6-依赖关系)
7. [运行方式](#7-运行方式)
8. [配置与关键文件](#8-配置与关键文件)
9. [术语表与质量保证](#9-术语表与质量保证)
10. [FAQ 与常见问题](#10-faq-与常见问题)

---

## 1. 项目概述

本项目是一个将 PCIe 6.2 Base Specification（PCI-SIG 官方规范）从英文翻译为中英对照双语 Markdown 的工程。核心目标是：

- **保留原始图表**：将 PDF 中的所有图表抽取为 PNG，嵌入翻译文档
- **中英对照双语格式**：使用 CXL 3.2 模板的两列 HTML 表格（英文 + 灰底中文）
- **GitHub Flavored Markdown**：兼容 GitHub 在线阅读与本地 HTML 预览
- **127 个 chunk 并行翻译**：通过子代理（sub-agent）分批完成，最后合并为单章 MD

项目并非传统意义上的"应用程序"，而是一套**文档翻译工具链**，由若干 Python 脚本和 Shell 脚本组成，覆盖从 PDF 解析、图片抽取、术语表构建、分块、翻译 prompt 生成、合并、图片精裁剪、布局修复、QA 审计到 HTML 预览生成的完整流水线。

---

## 2. 目录结构

```
/workspace/
├── README.md                          # 项目入口与阅读导航
├── book.md                            # 12 章合并的完整版 Markdown
├── chapter_index.json                 # 章节元数据（页码、标题、文件名模式）
├── glossary.json                      # PCIe/CXL 共享术语翻译表（v2）
├── .gitignore                         # 排除中间产物（raw/chunks/prompts 等）
│
├── PCIe6.2_Spec_chNN_*.md             # 12 个章节 Markdown（最终交付物）
│   ├── ch01 Introduction 引言
│   ├── ch02 Transaction Layer 事务层规范
│   ├── ch03 Data Link Layer 数据链路层规范
│   ├── ch04 Physical Layer Logical Block 物理层逻辑块
│   ├── ch05 Power Management 电源管理
│   ├── ch06 System Architecture 系统架构
│   ├── ch07 Software Init & Config 软件初始化与配置（含 Part_A/Part_B 拆分版）
│   ├── ch08 Electrical Sub-Block 电气子块
│   ├── ch09 SR-IOV 单根 I/O 虚拟化
│   ├── ch10 ATS 地址转换服务
│   ├── ch11 TDISP TEE 设备接口安全协议
│   └── ch12 Architectural OOB 架构带外管理
│
├── figures/                           # 抽取的图片（318 MB，150 DPI PNG）
│   └── chapter_NN/                    # 每章子目录
│       ├── fig_PPPP_1.png             # 全页渲染（去页眉页脚）
│       └── fig_PPPP_NN_tight.png      # 精裁剪版（MinerU bbox）
│
├── tight_crops/                       # 每章精裁剪映射 JSON
│   └── ch{N}_tight_crops.json         # figure → page/file/bbox/caption
│
├── preview/                           # HTML 预览（pandoc 生成）
│   ├── index.html                     # 章节导航主页
│   ├── book.html                      # 完整版单文件 HTML
│   ├── PCIe6.2_Spec_chNN_*.html       # 分章 HTML
│   └── pcie62_style.css               # 样式表（灰底中文、表格等）
│
├── tools/                             # 全部工具脚本
│   ├── extract_pcie6_2.py             # [阶段1] PDF → raw 文本 + 图片
│   ├── chunk_chapters.py              # [阶段2] 按 section 切分 chunk
│   ├── build_glossary.py              # [术语] 从 CXL_zh 构建 glossary.json
│   ├── build_translation_prompt.py    # [阶段3] 生成每个 chunk 的翻译 prompt
│   ├── merge_chapters.py              # [阶段4] 合并 chunks_translated → 章节 MD
│   ├── generate_indexes.py            # [索引] 生成章节 Section/Figure/Table 索引表
│   ├── build_html_preview.sh          # [预览] pandoc 生成 HTML + book.html
│   │
│   ├── split_pdf_for_mineru.py        # [图片] PDF 切 200 页 chunk 给 MinerU
│   ├── mineru_submit.py               # [图片] 调 MinerU API 批量解析
│   ├── render_tight_crops.py          # [图片] 从 MinerU bbox 渲染精裁剪
│   ├── ch4_figure_map.py              # [图片] ch4 figure 映射分析
│   ├── ch4_tight_crops.py             # [图片] ch4 精裁剪（ch4 专用）
│   ├── chx_tight_crops.py             # [图片] 通用化精裁剪（1-12 章）
│   ├── ch4_apply_tight_crops.py       # [图片] ch4 MD 中 img 引用替换为 _tight
│   ├── chx_apply_tight.py             # [图片] 通用化 img 引用替换为 _tight
│   ├── ch4_dedup_imgs.py              # [图片] ch4 跨中英文列去重 img
│   ├── chx_dedup_imgs.py              # [图片] 通用化跨列去重 img
│   ├── dedup_figures.py               # [图片] 全局去重重复 figure block
│   ├── fix_broken_crops.py            # [图片] 修复损坏/空的精裁剪图
│   ├── fix_ch4_full_page.py           # [图片] ch4 全图重渲染为全页版
│   ├── move_figures_out.py            # [布局] 将 figure 从 <td> 移到表外
│   ├── remove_zh_fig_captions.py      # [布局] 移除翻译 chunk 中的 ZH 图题
│   ├── remove_zh_figs_from_cells.py   # [布局] 从 <td> 移除 ZH 风格 figure block
│   ├── remove_zh_figs_v2.py           # [布局] v2: 表格内 EN/ZH figure block 移除
│   ├── fix_zh_missing_imgs.py         # [布局] ZH 列缺 img 时从 EN 列复制
│   ├── scan_zh_missing_imgs.py        # [布局] 扫描 ZH 列缺 img 情况
│   ├── fill_orphan_figures.py         # [布局] 为缺 img 的 figure 引用补图
│   ├── fig_caption_translator.py      # [翻译] 自动补全 figure 中文图题
│   │
│   ├── fix_layout_issues.py           # [修复] 表格平衡/anchor 去重/section 泄漏
│   ├── fix_ch4_layout.py              # [修复] 长表格包裹可滚动 div
│   ├── transform_to_single_column.py  # [修复] 两列表 → 单列堆叠格式
│   ├── cleanup_v2_format.py           # [修复] 单列格式清理（去重图、孤儿 </div>）
│   ├── fix_terminology_drift.py       # [修复] 术语漂移归一化（重置→复位等）
│   │
│   ├── qa_audit.py                    # [QA] 基础审计（表格/灰底/字符比/TODO）
│   ├── qa_deep_audit.py               # [QA] 深度审计（空单元/anchor/失衡行/EN-only）
│   ├── qa_bilingual_audit.py          # [QA] 双语行完整性审计
│   ├── qa_translation_audit.py        # [QA] 翻译质量审计（数字丢失/英文泄漏/术语漂移）
│   │
│   ├── smoke_test.py                  # [调试] PDF 单页文本/图片/尺寸冒烟测试
│   ├── push_to_github.sh              # [发布] git commit + push 到 GitHub
│   ├── figures_commit.sh              # [发布] figures 单独 commit/amend
│   ├── v2_commit.sh / v3_commit.sh / v4_commit.sh  # [发布] 各版本提交脚本
│
└── archive/                           # 归档：过程文档、QA 报告、一次性脚本
    ├── README.md                      # 归档清单
    ├── CHECKLIST.md / FIX_LOG.md / SELF_CHECK_REPORT.md
    ├── REVIEW_*.md / CH4_FIGURE_STRATEGY.md / QUALITY_IMPROVEMENT_PLAN.md
    ├── qa_report.json / qa_deep_report.json / qa_translation_audit*.json
    └── fix_*.py / add_missing_anchors.py / fix_toc_links.py ...
```

> **说明**：`raw/`、`chunks/`、`chunks_translated/`、`prompts/`、`tools/pdf_chunks/`、`tools/mineru_results/` 等中间产物目录通过 `.gitignore` 排除，不在仓库中保留。

---

## 3. 整体架构与流水线

项目采用**分阶段流水线**设计，从原始 PDF 到最终双语 Markdown + HTML 预览，共经历 6 个主要阶段：

```
┌─────────────────────────────────────────────────────────────────────┐
│                        阶段 0: 准备                                  │
│   chapter_index.json (章节元数据)  +  glossary.json (术语表)         │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   阶段 1: PDF 解析与抽取                              │
│   extract_pcie6_2.py                                                 │
│   输入: PDF + chapter_index.json                                     │
│   输出: raw/chapter_NN_raw.md (文本) + figures/chapter_NN/fig_*.png  │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   阶段 2: 分块 (Chunking)                            │
│   chunk_chapters.py                                                  │
│   输入: raw/*.md                                                     │
│   输出: chunks/chapter_NN[_aa].md (每块 ~120K 字符) + chunk_plan.json│
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│              阶段 3: 翻译 Prompt 生成 + 子代理翻译                    │
│   build_translation_prompt.py                                        │
│   输入: chunks/* + glossary.json + figures/ 列表                     │
│   输出: prompts/prompt_*.md → 子代理翻译 → chunks_translated/*.md    │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   阶段 4: 合并章节                                    │
│   merge_chapters.py                                                  │
│   输入: chunks_translated/* + chunk_plan.json + chapter_index.json   │
│   输出: PCIe6.2_Spec_chNN_*.md (12 章)                               │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│         阶段 5: 图片精裁剪 + 布局修复 + 索引生成                       │
│   ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│   │ chx_tight_crops │  │ move_figures_out │  │ generate_indexes │  │
│   │ chx_apply_tight │  │ fix_layout_issues│  │ fig_caption_trans│  │
│   │ dedup_figures   │  │ fix_ch4_layout   │  │ fill_orphan_figs │  │
│   └─────────────────┘  └──────────────────┘  └──────────────────┘  │
└──────────────────────────────┬──────────────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   阶段 6: QA 审计 + HTML 预览 + 发布                  │
│   qa_audit.py / qa_deep_audit.py / qa_bilingual_audit.py            │
│   qa_translation_audit.py                                            │
│   build_html_preview.sh → preview/                                   │
│   push_to_github.sh → GitHub                                         │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.1 图片处理子流水线

图片抽取有两条路径，互为补充：

```
路径 A（全页渲染）:                    路径 B（MinerU 精裁剪）:
extract_pcie6_2.py                     split_pdf_for_mineru.py
  └─ 150 DPI, 裁页眉页脚                  └─ 200 页/块 PDF
       → fig_PPPP_1.png                    mineru_submit.py
                                            └─ MinerU API OCR + bbox
                                               render_tight_crops.py / chx_tight_crops.py
                                                  └─ 按 bbox 渲染精裁剪
                                                     → fig_PPPP_NN_tight.png

chx_apply_tight.py 将 MD 中 fig_PPPP_NN.png 替换为 fig_PPPP_NN_tight.png（若存在）
```

---

## 4. 核心模块职责

### 4.1 数据模型

| 概念 | 说明 |
|------|------|
| **Chapter** | 一个 PCIe 6.2 章节，对应 `chapter_index.json` 中一条记录（ch/en/zh/start/end） |
| **Chunk** | 章节按 section 边界切分的翻译单元，目标 ~120K 字符，文件命名 `chapter_NN[_aa]_raw.md` |
| **Translated Chunk** | 子代理翻译后的产物 `chapter_NN[_aa]_CN_EN.md`，含 CXL 3.2 双语表格 |
| **Figure** | PDF 中的图表，全页版 `fig_PPPP_1.png`，精裁剪版 `fig_PPPP_NN_tight.png` |
| **Glossary Term** | `glossary.json` 中的术语条目：`{source, target, category, confidence, ...}` |
| **Section Anchor** | `<a id="sec-N-X-Y"></a>` 形式的章节锚点，用于目录跳转 |

### 4.2 模块职责总览

| 模块类别 | 关键脚本 | 职责 |
|----------|----------|------|
| **PDF 解析** | `extract_pcie6_2.py` | 按章节抽取文本（去页眉页脚）+ 全页图片渲染 |
| **分块** | `chunk_chapters.py` | 按 section 边界切分为可翻译 chunk，生成 `chunk_plan.json` |
| **术语** | `build_glossary.py` | 从 CXL_zh 精选 PCIe 共享术语，输出 `glossary.json` |
| **翻译编排** | `build_translation_prompt.py` | 为每个 chunk 生成含格式规范+术语表+图清单的 prompt |
| **合并** | `merge_chapters.py` | 合并 translated chunks → 单章 MD，自动生成 TOC |
| **索引** | `generate_indexes.py` | 提取 Section/Figure/Table 索引表插入各章 |
| **图片精裁** | `chx_tight_crops.py`, `ch4_*_tight_crops.py` | 基于 MinerU bbox 渲染精裁剪图 |
| **图片修复** | `fix_broken_crops.py`, `dedup_figures.py`, `chx_dedup_imgs.py` | 修复空图、去重 |
| **布局修复** | `fix_layout_issues.py`, `fix_ch4_layout.py`, `move_figures_out.py` | 表格平衡、anchor 去重、figure 移出表格 |
| **翻译辅助** | `fig_caption_translator.py`, `fix_terminology_drift.py` | 图题翻译、术语漂移归一化 |
| **QA 审计** | `qa_audit.py`, `qa_deep_audit.py`, `qa_bilingual_audit.py`, `qa_translation_audit.py` | 结构/内容/翻译质量四层审计 |
| **预览发布** | `build_html_preview.sh`, `push_to_github.sh` | pandoc HTML、git 提交推送 |

---

## 5. 关键脚本与函数说明

### 5.1 `extract_pcie6_2.py` — PDF 文本与图片抽取

**职责**：读取 `chapter_index.json`，对每章从 PDF 抽取原始文本与图片。

| 函数 | 签名 | 说明 |
|------|------|------|
| `extract_text(doc, start_page, end_page, ch_num)` | `(fitz.Document, int, int, int) -> str` | 抽取指定页范围文本，过滤页脚（`6.2-1.0-PUB...`、`Page N`），插入 `<<<PAGE_BREAK>>> page_NNN` 标记 |
| `extract_figures(doc, start_page, end_page, ch_num)` | `(fitz.Document, int, int, int) -> list` | 对含 drawings/images 的页，用 150 DPI + `CLIP=Rect(0,110,1275,1530)` 渲染去页眉页脚的 PNG，命名 `fig_PPPP_1.png` |
| `main()` | `() -> None` | 遍历 12 章，写出 `raw/chapter_NN_raw.md` + `figures/chapter_NN/`，生成 `extraction_summary.json` |

**关键常量**：
- `CLIP = fitz.Rect(0, 110, 1275, 1530)` — 150 DPI 下的裁剪框，去除页眉页脚
- `ZOOM = fitz.Matrix(150/72, 150/72)` — 150 DPI 缩放

### 5.2 `chunk_chapters.py` — 章节分块

**职责**：将每章 raw 文本按 section 边界切分为 ~120K 字符的 chunk。

| 函数 | 签名 | 说明 |
|------|------|------|
| `find_section_offsets(text)` | `(str) -> list[(offset, label)]` | 用 `SECTION_RE` 正则（`^N.M Title §`）定位所有 section 标题 |
| `split_chapter(ch_num, raw_text, target_size)` | `(int, str, int) -> list[str]` | 贪心分组：累计 section 直到接近 `target_size`（120K），切分；若无 section 则退化为按 `<<<PAGE_BREAK>>>` 切分 |
| `main()` | `() -> None` | 写出 `chunks/chapter_NN[_aa].md`，生成 `chunk_plan.json`（含每章 chunk 列表与大小） |

**命名规则**：多 chunk 时用双字母后缀 `_aa, _ab, ..., _az, _ba, ...`。

### 5.3 `build_glossary.py` — 术语表构建

**职责**：从硬编码的 `TERMS` 列表（~140 条 PCIe/CXL 共享术语）生成 `glossary.json`。

| 函数 | 签名 | 说明 |
|------|------|------|
| `main()` | `() -> None` | 将 `TERMS` 转为 `{id, source, target, category, aliases, confidence, ...}` 条目，写出 `glossary.json`（version=2） |

**术语分类**：`layer, block, interface, device, port, link, packet, mode, transaction, address, register, feature, field, error, state, signal, bus, modulation, encoding, concept, speed, organization`。

### 5.4 `build_translation_prompt.py` — 翻译 Prompt 生成

**职责**：为每个 chunk 生成完整翻译 prompt，包含格式规范、术语表、图清单、源文本。

| 函数 | 签名 | 说明 |
|------|------|------|
| `build_glossary_excerpt()` | `() -> str` | 读取 `glossary.json`，格式化为 3 列 Markdown 表格 |
| `get_figures_for_chapter(ch_num)` | `(int) -> list[(stem, fname)]` | 列出某章 figures 目录下所有 PNG |
| `main()` | `() -> None` | 遍历 chunk_plan，为每个 chunk 写 `prompts/prompt_<stem>.md` |

**核心模板 `FORMAT_TEMPLATE`**：定义 CXL 3.2 双语格式规范——H1 章节头、`<a id="sec-N-X"></a>` 锚点、`<table>` 双列（EN + 灰底 ZH）、图引用、翻译风格规则。

### 5.5 `merge_chapters.py` — 章节合并

**职责**：将 `chunks_translated/` 中的翻译产物合并为单章 MD。

| 函数 | 签名 | 说明 |
|------|------|------|
| `main()` | `() -> None` | 1) 拼接 `H1_TEMPLATE` 头部；2) 遍历 chunk，若 translated 文件存在则拼接并提取 section anchor，否则插入 TODO 占位；3) 自动生成 TOC；4) 写出 `PCIe6.2_Spec_chNN_*.md` |

**文件名安全化**：`safe_en` 只保留字母数字，`safe_zh` 只保留中日韩字符与字母数字。

### 5.6 `generate_indexes.py` — 索引表生成

**职责**：从各章 MD 提取 Section/Figure/Table 索引表，替换原占位 TOC 区。

| 函数 | 签名 | 说明 |
|------|------|------|
| `extract_page_markers(text)` | `(str) -> list[(line_idx, page_num)]` | 提取 `<!-- 📄 Page NNN -->` 标记 |
| `page_of_line(line_idx, page_markers)` | `(int, list) -> int` | 根据标记定位某行所在页 |
| `extract_indexes(ch)` | `(int) -> (sections, figures, tables)` | 提取章节标题、Figure 标题、Table 标题（支持多种格式变体） |
| `insert_indexes(ch, sections, figures, tables)` | `(int, ...) -> bool` | 将索引表插入 MD 的 TOC 区（替换原占位） |

### 5.7 `chx_tight_crops.py` — 通用精裁剪

**职责**：从 MinerU 的 `content_list.json` 中提取 figure bbox，渲染精裁剪 PNG。

| 函数 | 签名 | 说明 |
|------|------|------|
| `find_pdf_for_page(page_num)` | `(int) -> Path\|None` | 查找包含指定页的 PDF chunk |
| `render_or_copy(pdf_path, page_num, bbox, out_path, mineru_img_path)` | `(...) -> clip` | 优先复制 MinerU 提取的 JPG，否则用 PyMuPDF 按 bbox + 4% padding 渲染 150 DPI |
| `process_chapter(ch_num, start_page, end_page)` | `(int, int, int) -> (ok, fail)` | 遍历 MinerU 结果，匹配 `Figure N-NN` caption，渲染并写出 `ch{N}_tight_crops.json` |

**caption 正则**：`FIG_CAPTION_RE = r'^(?:Figure|Fiqure|FIG) (\d+)-(\d+)\s+(.*?)(?:\s*§)?$'`（兼容 OCR 拼写错误 "Fiqure"）。

### 5.8 `chx_apply_tight.py` — 应用精裁剪引用

**职责**：将 MD 中 `fig_PPPP_NN.png` 替换为 `fig_PPPP_NN_tight.png`（若精裁剪文件存在）。

| 函数 | 签名 | 说明 |
|------|------|------|
| `get_chapter_files(ch_num)` | `(int) -> (md_path, fig_dir)` | 定位章节 MD 与 figures 目录 |
| `apply(ch_num)` | `(int) -> None` | 正则匹配所有 `<img>`，逐个检查 `_tight.png` 是否存在并替换 |

### 5.9 `fix_layout_issues.py` — 布局自动修复

**职责**：批量修复合并后 MD 的常见布局问题。

| 函数 | 签名 | 说明 |
|------|------|------|
| `fix_table_balance(content)` | `(str) -> (str, diff)` | 平衡 `<table>`/`</table>` 标签数 |
| `fix_duplicate_anchors(content)` | `(str) -> (str, n_dup)` | 重复 anchor 加 `-1, -2` 后缀（倒序处理保位置） |
| `fix_en_only_section_headers(content)` | `(str) -> (str, n_leaks)` | 移除泄漏到 `<td>` 中的 section 标题（`N.M Title §`） |

### 5.10 QA 审计脚本族

#### `qa_audit.py` — 基础审计
检查：`<table>` 平衡、灰底中文单元数、图片引用数、Section 锚点数、ZH/EN 字符比、TODO 标记、关键术语频次。输出 `qa_report.json`。

#### `qa_deep_audit.py` — 深度审计
检查：空 `<td>`、EN/ZH 列长度失衡、anchor 平衡与重复、代码块配对、TODO 泄漏、纯英文行（无中文翻译）。输出 `qa_deep_report.json`。

#### `qa_bilingual_audit.py` — 双语行审计
针对双语行（`<tr><td>EN</td><td style=gray>ZH</td></tr>`）统计：完整翻译、EN-only、ZH-only、失衡行占比。输出 `qa_bilingual_report.json`。

#### `qa_translation_audit.py` — 翻译质量审计
核心检查项：
| 检查类型 | 说明 |
|----------|------|
| `untranslated` | EN > 200 字符但 ZH CJK < 10 |
| `short_ratio` | ZH/EN 长度比 < 0.18 |
| `numbers_missing` | ZH 中丢失的数字 token（排除 1-2 位纯数字） |
| `english_leak` | ZH 列中出现完整英文句子（含 stopwords） |
| `ascii_comma` | 中文段落中半角逗号多于全角 |
| `blacklist` | 出现黑名单译法（如"有序集合"、"热插入"） |
| `table_structure` / `columns_swapped` / `heading_in_cell` | 表格结构异常 |

术语漂移检测：`VARIANTS` 列表（如 `根复合体` vs `根联合体`、`流控` vs `流量控制`）。

### 5.11 `fig_caption_translator.py` — 图题自动翻译

**职责**：为缺中文图题的 Figure 自动生成中文标题。

| 函数 | 签名 | 说明 |
|------|------|------|
| `translate_caption(en_title)` | `(str) -> str` | 1) 多词术语替换；2) 单词术语替换；3) caption 专用规则（Diagram→图、Flowchart→流程图等）；4) 清理标点 |
| `process_file(fpath, dry_run)` | `(Path, bool) -> list` | 查找缺 ZH 图题的 Figure，在 img 后插入 `> **图 X-NN.** 中文标题` |

### 5.12 `build_html_preview.sh` — HTML 预览生成

**职责**：用 pandoc 将各章 MD 转为 HTML，并合并为 `book.html`。

主要步骤：
1. 对每个 `PCIe6.2_Spec_ch*.md` 执行 `pandoc -f gfm -t html5 --standalone --css=pcie62_style.css`
2. 拼接 `book.md`（含目录 TOC + 12 章内容）
3. `pandoc book.md ... --toc --toc-depth=2` 生成 `preview/book.html`
4. 复制 CSS 到 `preview/`

### 5.13 `mineru_submit.py` — MinerU API 调用

**职责**：将 PDF chunk 提交到 MinerU OCR 服务，轮询结果并下载。

| 函数 | 签名 | 说明 |
|------|------|------|
| `submit_local_file(pdf_path)` | `(Path) -> dict\|None` | POST `/api/v4/file-urls/batch` 提交文件元数据，获取 `batch_id` + 上传 URL |
| `upload_file(pdf_path, upload_url)` | `(Path, str) -> bool` | PUT 上传文件到预签名 URL |
| `poll_batch(batch_id, max_wait, poll_interval)` | `(str, int, int) -> list\|None` | 轮询 `/api/v4/extract-results/batch/{batch_id}` 直到 `done`/`failed` |
| `download_and_unzip(zip_url, out_dir)` | `(str, Path) -> bool` | 下载结果 ZIP 并解压到 `tools/mineru_results/chunk_NN/` |

---

## 6. 依赖关系

### 6.1 Python 依赖

| 包 | 用途 | 使用脚本 |
|----|------|----------|
| `PyMuPDF` (`fitz`) | PDF 解析、文本提取、图片渲染 | `extract_pcie6_2.py`, `split_pdf_for_mineru.py`, `render_tight_crops.py`, `chx_tight_crops.py`, `fix_broken_crops.py`, `fix_ch4_full_page.py`, `smoke_test.py` |
| `Pillow` (`PIL`) | 图片尺寸读取、格式检查 | `chx_tight_crops.py`, `fix_broken_crops.py` |
| `requests` | MinerU REST API 调用 | `mineru_submit.py` |
| `json`, `re`, `os`, `sys`, `pathlib`, `collections`, `argparse`, `html`, `zipfile`, `time`, `shutil` | 标准库 | 所有脚本 |

### 6.2 系统依赖

| 工具 | 用途 |
|------|------|
| `pandoc` | Markdown → HTML 转换（`build_html_preview.sh`） |
| `bash` | Shell 脚本执行 |
| `git` | 版本管理与发布 |
| MinerU API（远程） | PDF 版面分析、图片 bbox 检测 |

### 6.3 模块间数据流依赖

```
chapter_index.json ──┬──> extract_pcie6_2.py ──> raw/ + figures/
                     │
glossary.json <──────┴── build_glossary.py (硬编码 TERMS)
                     │
raw/ ──> chunk_chapters.py ──> chunks/ + chunk_plan.json
                     │
chunks/ + glossary.json + figures/ ──> build_translation_prompt.py ──> prompts/
                     │
prompts/ ──> [子代理翻译] ──> chunks_translated/
                     │
chunks_translated/ + chunk_plan.json ──> merge_chapters.py ──> PCIe6.2_Spec_chNN_*.md
                     │
PCIe6.2_Spec_chNN_*.md ──┬──> generate_indexes.py (索引表)
                         ├──> chx_apply_tight.py (图片引用替换)
                         ├──> fix_layout_issues.py (布局修复)
                         ├──> qa_audit.py / qa_deep_audit.py / ... (QA)
                         └──> build_html_preview.sh (HTML)

PDF ──> split_pdf_for_mineru.py ──> tools/pdf_chunks/
                                         │
                                         └──> mineru_submit.py ──> tools/mineru_results/
                                                                    │
                                                                    └──> chx_tight_crops.py ──> figures/*_tight.png + ch{N}_tight_crops.json
```

### 6.4 配置路径硬编码

多数脚本顶部有硬编码的绝对路径（作者本地环境），复用时需修改：

```python
OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
PDF_PATH = '/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_all/NCB-PCI_Express_Base_6.2-2024-01-25.pdf'
CXL_ZH = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh')
```

`qa_translation_audit.py` 与 `fix_terminology_drift.py` 已改用 `ROOT = Path(__file__).resolve().parent.parent`，可移植性更好。

---

## 7. 运行方式

### 7.1 环境准备

```bash
# Python 依赖
pip install PyMuPDF Pillow requests

# 系统依赖（macOS/Homebrew 示例）
brew install pandoc git

# 环境变量（仅 MinerU 流程需要）
export MINERU_TOKEN=<your_mineru_token>
```

### 7.2 完整流水线（从零重跑）

```bash
cd /workspace

# 阶段 1: 构建术语表
python3 tools/build_glossary.py

# 阶段 2: PDF 文本 + 图片抽取
python3 tools/extract_pcie6_2.py

# 阶段 3: 分块
python3 tools/chunk_chapters.py

# 阶段 4: 生成翻译 prompt
python3 tools/build_translation_prompt.py
# → 人工/子代理执行 prompts/*.md，输出到 chunks_translated/

# 阶段 5: 合并章节
python3 tools/merge_chapters.py

# 阶段 6a: 图片精裁剪（需要 MinerU 结果）
python3 tools/split_pdf_for_mineru.py
python3 tools/mineru_submit.py
python3 tools/chx_tight_crops.py 1-12
python3 tools/chx_apply_tight.py 1-12

# 阶段 6b: 布局修复与索引
python3 tools/generate_indexes.py
python3 tools/fix_layout_issues.py
python3 tools/dedup_figures.py

# 阶段 7: QA 审计
python3 tools/qa_audit.py
python3 tools/qa_deep_audit.py
python3 tools/qa_bilingual_audit.py
python3 tools/qa_translation_audit.py

# 阶段 8: HTML 预览
bash tools/build_html_preview.sh
open preview/index.html
```

### 7.3 仅阅读（无需重跑）

```bash
# 直接打开已有产物
open preview/index.html    # 分章导航
open preview/book.html     # 完整版
# 或直接在 GitHub 上阅读 PCIe6.2_Spec_chNN_*.md
```

### 7.4 常用维护命令

```bash
# 重新生成某章精裁剪
python3 tools/chx_tight_crops.py 7

# 应用精裁剪引用到某章
python3 tools/chx_apply_tight.py 7

# 修复布局问题
python3 tools/fix_layout_issues.py

# 术语漂移修复（预览）
python3 tools/fix_terminology_drift.py --dry-run

# 翻译质量审计指定章节
python3 tools/qa_translation_audit.py ch04 ch07
```

---

## 8. 配置与关键文件

### 8.1 `chapter_index.json`

项目元数据中枢，定义了 12 章的页码范围与标题。

```json
{
  "pdf": ".../NCB-PCI_Express_Base_6.2-2024-01-25.pdf",
  "total_pages": 2111,
  "spec_title": "PCI Express® Base Specification Revision 6.2",
  "filename_pattern": "PCIe6.2_Spec_chNN_<EnglishTitle>_<中文Title>.md",
  "chapters": [
    {"ch": 1, "en": "Introduction", "zh": "引言", "start": 127, "end": 140},
    ...
  ],
  "out_of_scope": "Appendices A through L (pages 1703-2092) + Acknowledgements"
}
```

### 8.2 `glossary.json`

术语翻译表，`version: 2`，含 `terms` 数组，每条：

```json
{
  "id": "transaction_layer",
  "source": "Transaction Layer",
  "target": "事务层",
  "category": "layer",
  "confidence": "high",
  "notes": "Curated from CXL 3.2 (CXL_zh/) translation; shared PCIe terminology"
}
```

### 8.3 `tight_crops/ch{N}_tight_crops.json`

每章 figure 映射，`chx_tight_crops.py` 产出：

```json
{
  "chapter": 7,
  "page_range": [981, 1408],
  "total_figures": 325,
  "figures": {
    "Figure 7-1": {
      "page": 981,
      "file": "fig_0981_1_tight.png",
      "bbox": [336, 714, 632, 840],
      "caption": "PCI Express Root Complex Device Mapping",
      "mineru_image": "images/xxx.jpg"
    }
  }
}
```

### 8.4 `.gitignore`

排除中间产物：`raw/`, `chunks/`, `chunks_translated/`, `prompts/`, `tools/pdf_chunks/`, `tools/mineru_results/`, `extraction_summary.json`, `chunk_plan.json`, `qa_bilingual_report.json` 等。

---

## 9. 术语表与质量保证

### 9.1 翻译格式规范（CXL 3.2 模板）

每个 Section 的双语格式：

```html
<a id="sec-N-X-Y"></a>
## N.X.Y Section | 中文小节标题

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🇨🇳 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>
[英文原文]
</td>
<td style="background-color:#e8e8e8">
[中文翻译]
</td>
</tr>
</tbody>
</table>
```

**关键规则**：
- 中文单元格必须带 `style="background-color:#e8e8e8"`（灰底）
- Section 锚点格式 `sec-N-X-Y`
- 术语首次出现 `EN (中文)`，后续保留英文缩写
- 协议名/寄存器/信号名保留英文（`TLP`, `Gen5`, `PERST`）
- 数字、十六进制、位宽保持原样

### 9.2 质量保证层级

| 层级 | 工具 | 检查内容 |
|------|------|----------|
| L1 结构 | `qa_audit.py` | 表格平衡、灰底单元、图片引用、字符比 |
| L2 深度 | `qa_deep_audit.py` | 空单元、anchor 重复/平衡、代码块、EN-only 行 |
| L3 双语 | `qa_bilingual_audit.py` | 双语行完整度、EN-only/ZH-only/失衡占比 |
| L4 翻译 | `qa_translation_audit.py` | 数字丢失、英文泄漏、术语漂移、黑名单译法 |

### 9.3 术语漂移纠正（`fix_terminology_drift.py`）

| 错误译法 | 正确译法 | 说明 |
|----------|----------|------|
| 重置 | 复位 | reset |
| 吞吐率 | 吞吐量 | throughput |
| 接收者 | 接收方 | Receiver |
| 发送者 | 发送方 | Sender |
| 完成方 | 完成者 | Completer |
| 请求方 (ch02/ch06) | 请求者 | Requester |

---

## 10. FAQ 与常见问题

### Q1: 为什么图片有全页版和精裁剪版两种？
全页版（`fig_PPPP_1.png`）由 `extract_pcie6_2.py` 直接渲染，包含页眉页脚裁剪后的整页内容，作为兜底。精裁剪版（`fig_PPPP_NN_tight.png`）由 MinerU 检测 figure bbox 后渲染，更紧凑。`chx_apply_tight.py` 会优先用精裁剪版，不存在时保留全页版。

### Q2: Ch4 为什么用全页渲染而非精裁剪？
Ch4（物理层逻辑块）含大量跨列、跨页的状态图与时序图，MinerU bbox 检测常漏检。`fix_ch4_full_page.py` 将 Ch4 所有图重渲染为全页版（150 DPI），是更安全的选择。

### Q3: `<<<PAGE_BREAK>>> page_NNN` 标记的作用？
在 `extract_pcie6_2.py` 抽取时插入，保留页边界信息，供合并阶段定位页码、索引生成时计算 page 归属。

### Q4: 如何新增一个术语？
编辑 `tools/build_glossary.py` 的 `TERMS` 列表，添加 `{source, target, category}`，重新运行 `python3 tools/build_glossary.py` 生成 `glossary.json`。翻译 prompt 会自动包含新术语。

### Q5: MinerU 结果如何本地使用？
`tools/mineru_results/chunk_NN/` 下包含 `full.md`（OCR 全文）和 `*_content_list.json`（元素列表，含 image/table/chart 的 bbox、caption、img_path）。`chx_tight_crops.py` 解析 `content_list.json` 提取 figure bbox。

### Q6: 翻译是如何完成的？
`build_translation_prompt.py` 为每个 chunk 生成 prompt（含格式规范+术语表+图清单+源文本），由子代理（sub-agent）读取 prompt 并输出 `chunks_translated/<stem>_CN_EN.md`，最后 `merge_chapters.py` 合并。项目使用了 Claude Opus 作为翻译子代理（见 commit 的 Co-Authored-By）。

### Q7: 如何在本地预览 HTML？
运行 `bash tools/build_html_preview.sh` 后打开 `preview/index.html`。CSS 优先使用 CXL_zh 的 `pdf-style.css`，不存在时用内置 fallback CSS。

---

## 附录：脚本分类速查表

| 类别 | 脚本 |
|------|------|
| **PDF 解析** | `extract_pcie6_2.py`, `smoke_test.py` |
| **分块与 prompt** | `chunk_chapters.py`, `build_translation_prompt.py` |
| **合并与索引** | `merge_chapters.py`, `generate_indexes.py` |
| **术语** | `build_glossary.py`, `fix_terminology_drift.py`, `fig_caption_translator.py` |
| **图片-全页** | `extract_pcie6_2.py`(内), `fix_ch4_full_page.py`, `fix_broken_crops.py` |
| **图片-精裁** | `split_pdf_for_mineru.py`, `mineru_submit.py`, `render_tight_crops.py`, `ch4_tight_crops.py`, `chx_tight_crops.py`, `ch4_apply_tight_crops.py`, `chx_apply_tight.py` |
| **图片-去重** | `dedup_figures.py`, `ch4_dedup_imgs.py`, `chx_dedup_imgs.py` |
| **布局修复** | `fix_layout_issues.py`, `fix_ch4_layout.py`, `move_figures_out.py`, `fill_orphan_figures.py`, `fix_zh_missing_imgs.py`, `scan_zh_missing_imgs.py` |
| **格式转换** | `transform_to_single_column.py`, `cleanup_v2_format.py`, `remove_zh_fig_captions.py`, `remove_zh_figs_from_cells.py`, `remove_zh_figs_v2.py` |
| **QA** | `qa_audit.py`, `qa_deep_audit.py`, `qa_bilingual_audit.py`, `qa_translation_audit.py` |
| **预览发布** | `build_html_preview.sh`, `push_to_github.sh`, `figures_commit.sh`, `v2_commit.sh`, `v3_commit.sh`, `v4_commit.sh` |
| **ch4 专用** | `ch4_figure_map.py`, `ch4_tight_crops.py`, `ch4_apply_tight_crops.py`, `ch4_dedup_imgs.py`, `fix_ch4_full_page.py`, `fix_ch4_layout.py` |
