# 📚 PCIe 6.2 Spec 中英对照翻译

> **PCI Express® Base Specification — Revision 6.2, Version 1.0 — January 25, 2024**

📄 **Source PDF**: [`NCB-PCI_Express_Base_6.2-2024-01-25.pdf`](https://pcisig.com/specifications) (2111 pages, 27.8 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown
📐 **Template**: 基于 [CXL 3.2 Spec 中英对照翻译](https://github.com/jimwang2050/CXL_3.2_Spec) 模板
🐙 **GitHub**: https://github.com/jimwang2050/PCIe6.2_Spec

---

## 📊 翻译进度 (Translation Progress)

**已完成**: 12 / 12 章 (**127 / 127 chunks 100%**)
**总文件**: 6.2 MB MD + 18 MB HTML 预览 + 318 MB 原图

```text
[██████████████] 100%  (127/127 chunks)
```

### 离线阅读 (Local Reading)

```bash
open preview/index.html    # 浏览器打开阅读
# 或
open preview/book.html     # 完整版 (8.4 MB, 含目录)
```

### 章节状态

| Ch | English | 中文 | Pages | Sections | Status | File |
|:-:|---------|------|:-----:|:--------:|:------:|:----:|
| 1 | Introduction | 引言 | 127–140 | 24 | ✅ Done | [📄](PCIe6.2_Spec_ch01_Introduction_引言.md) |
| 2 | Transaction Layer Specification | 事务层规范 | 141–308 | 83 | ✅ Done | [📄](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) |
| 3 | Data Link Layer Specification | 数据链路层规范 | 309–350 | 18 | ✅ Done | [📄](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) |
| 4 | Physical Layer Logical Block | 物理层逻辑块 | 351–650 | 211 | ✅ Done | [📄](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) |
| 5 | Power Management | 电源管理 | 651–706 | 16 | ✅ Done | [📄](PCIe6.2_Spec_ch05_Power_Management_电源管理.md) |
| 6 | System Architecture | 系统架构 | 707–980 | 209 | ✅ Done | [📄](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md) |
| 7 | Software Initialization and Configuration | 软件初始化与配置 | 981–1408 | 399 | ✅ Done | [📄](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md) |
| 8 | Electrical Sub-Block | 电气子块 | 1409–1522 | 66 | ✅ Done | [📄](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md) |
| 9 | Single Root I/O Virtualization (SR-IOV) | SR-IOV 单根 I/O 虚拟化 | 1523–1558 | 20 | ✅ Done | [📄](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md) |
| 10 | Address Translation Services (ATS) | ATS 地址转换服务 | 1559–1608 | 5 | ✅ Done | [📄](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md) |
| 11 | TEE Device Interface Security Protocol (TDISP) | TDISP TEE 设备接口安全协议 | 1609–1658 | 13 | ✅ Done | [📄](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md) |
| 12 | Architectural Out-of-Band Management | 架构带外管理 | 1659–1702 | 54 | ✅ Done | [📄](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md) |

---

## 🗂 目录结构 (Directory Layout)

```
PCIe6.2_zh/
├── README.md                                         # 本文件
├── PCIe6.2_Spec_ch01_Introduction_引言.md            # 12 章节 MD
├── PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md
├── PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md
├── PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md
├── PCIe6.2_Spec_ch05_Power_Management_电源管理.md
├── PCIe6.2_Spec_ch06_System_Architecture_系统架构.md
├── PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md
├── PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md
├── PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md
├── PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md
├── PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md
├── PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md
├── figures/                                          # 12 章原图 (318 MB)
│   ├── chapter_01/  fig_0127_1.png ... fig_0140_1.png
│   ├── chapter_02/  fig_0141_1.png ... fig_0308_1.png  (168 pages)
│   ├── ...
│   └── chapter_12/  fig_1659_1.png ... fig_1702_1.png
├── glossary.json                                     # 252 个 PCIe/CXL 术语对照
├── chapter_index.json                                # 章节页范围索引
└── tools/                                            # 复现脚本
    ├── extract_pcie6_2.py                            # PDF → 文本+图表
    ├── chunk_chapters.py                             # 按章节切分 chunk
    ├── build_glossary.py                             # 构建术语表
    ├── build_translation_prompt.py                   # 生成翻译 prompt
    └── merge_chapters.py                             # 合并 chunk → 章节 MD
```

---

## 🎨 格式约定 (Format Conventions)

每个章节遵循 CXL 3.2 模板统一结构:

```markdown
# 📘 第 N 章　<Title> (Chapter N. <English>)

**PCI Express® Base Specification — Revision 6.2**

> 📄 **Source pages**: X–Y | 📁 **File**: `chapter_NN.md`
> 🎨 **Format**: 中英对照双语 · 图表原始保留 · 中文背景色灰色

---

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

[⬆️ 返回目录](#-本章目录-table-of-contents)

---
```

### 已应用的 GitHub 特性

| 特性 | 实现 |
|------|------|
| **显式锚点** | `<a id="sec-N-X">` 跨设备稳定 |
| **中文灰底** | `<td style="background-color:#e8e8e8">` |
| **图表内嵌** | `<img src="figures/chapter_NN/fig_PPPP_1.png" width="700">` |
| **返回目录** | 每节末尾 `[⬆️ 返回目录]` 跳转 |
| **PAGE_BREAK 标记** | 保留 `<<<PAGE_BREAK>>> page_XXX` 用于页码定位 |

### 翻译风格

- **首次出现术语**: `EN (中文)` 对照,例如 `Flow Control (流控)`
- **章节标题双语并列**: `## 2.5 Transaction Ordering | 事务排序`
- **协议名/寄存器字段/信号名**: 保留英文 (如 `TLP`, `Gen5`, `PERST`, `CFG_DONE`)
- **数字、十六进制值、位宽**: 保持原样
- **页码引用 (§ Section X.Y)**: 保留原 spec 引用格式
- **表格**: 用标准 Markdown 表格 (不放在 HTML <table> 内)
- **图片引用**: 原始 `fig_PPPP_1.png` 文件名保留

---

## 📚 术语表 (Glossary) — 252 项精选

构建自 CXL 3.2 翻译项目的共享 PCIe/CXL 术语集,涵盖:

- **协议层**: Transaction Layer / Data Link Layer / Physical Layer
- **设备与拓扑**: Root Complex / Switch / Endpoint / Bridge / RCiEP
- **事务类型**: TLP / DLLP / Flit / Non-Flit Mode / Posted / Non-Posted
- **地址空间**: Memory Space / I/O Space / Configuration Space / BAR
- **流控与排序**: Flow Control / Credit / IDO / ID-Based Ordering
- **错误处理**: Correctable / Uncorrectable / Fatal Error / Poison
- **电源管理**: L0 / L0s / L1 / L1.1 / L1.2 / L2 / L3 / D0 / D1 / D2 / D3hot / D3cold / ASPM / PME
- **物理层**: 8b/10b / 128b/130b / PAM4 / NRZ / LTSSM / TS / SKP / Compliance Pattern
- **SR-IOV**: PF / VF / ARI
- **ATS**: IOMMU / Translation Agent / Device-TLB / PRI / Page Request
- **TDISP**: TEE / TSM / DSM / IDE / Stream / Key
- **OOB**: Sideband / FRU / Retimer / Interposer / PERST / PESTI / REFCLK

详见 [`glossary.json`](glossary.json)

---

## 🛠 工具链 (Toolchain)

- **PDF 提取**: [PyMuPDF](https://pymupdf.readthedocs.io/) (fitz) — 文本+布局+图像
- **图渲染**: PyMuPDF 150 DPI, 裁剪页眉/页脚
- **翻译工作流**: 
  - 12 章 → 127 chunks (按 section 边界切分,每块 ~30K chars)
  - 每个 chunk 由独立子代理翻译,保留 CXL 3.2 表格格式
  - 平行并发: 6-8 chunks/批
- **辅助 skills**:
  - `translate-book` (官方) — 翻译 skill 框架
  - `cn-en-translate` (项目内) — PCIe 6.2 翻译规范
  - `book-to-skill` / `mineru` / `pdf` / `pdf-content-extractor`

---

## ✅ 翻译状态: 100% 完成

所有 127 个 chunks 已完成翻译。所有 12 章 MD 文件 100% 完整,无 TODO。

---

## 📋 Recent Updates (更新日志)

### 2026-06-14 — v3 完整发布 (HTML + book + QA)

- **HTML 预览**: 14 个独立 HTML 文件 (preview/index.html 索引)
- **book.md**: 12 章合并单文件 (7.2 MB, 129,341 行)
- **book.html**: pandoc 渲染完整版 (8.4 MB, 含 TOC)
- **qa_report.json**: 12 章详细审计数据

### 2026-06-14 — v2 完整版 (100%)

- **127 / 127 chunks 100% 完成** (12 章, 1576 pages 全部翻译)
- Re-merge 章节 MD (v1 92% → v2 100%)

### 2026-06-12 — v1 初次提交 (92%)

- 12 章 MD 文件全部生成
- 117 / 127 chunks 翻译完成 (92%)
- 1576 张原图抽取到 `figures/chapter_NN/`

---

## 🤝 致谢 (Credits)

- **官方规范**: PCI-SIG® — [PCI Express® Base Specification, Rev 6.2](https://pcisig.com/specifications)
- **翻译模板**: [CXL 3.2 Spec 中英对照翻译](https://github.com/jimwang2050/CXL_3.2_Spec) (CXL_zh/)
- **翻译工具**: Claude Code Opus 4.8 (`/model opus`)
- **生成时间**: 2026-06-11 ~ 2026-06-12

---

> 🤖 **Generated with** [Claude Code](https://claude.com/claude-code) · Opus 4.8
> 📅 2026-06-12
