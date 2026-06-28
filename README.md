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
| 1 | [Introduction](PCIe6.2_Spec_ch01_Introduction_引言.md) | [引言](PCIe6.2_Spec_ch01_Introduction_引言.md) | 127–140 | 24 | ✅ Done | [📄](PCIe6.2_Spec_ch01_Introduction_引言.md) |
| 2 | [Transaction Layer Specification](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) | [事务层规范](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) | 141–308 | 83 | ✅ Done | [📄](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) |
| 3 | [Data Link Layer Specification](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) | [数据链路层规范](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) | 309–350 | 18 | ✅ Done | [📄](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) |
| 4 | [Physical Layer Logical Block](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) | [物理层逻辑块](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) | 351–650 | 211 | ✅ Done | [📄](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) |
| 5 | [Power Management](PCIe6.2_Spec_ch05_Power_Management_电源管理.md) | [电源管理](PCIe6.2_Spec_ch05_Power_Management_电源管理.md) | 651–706 | 16 | ✅ Done | [📄](PCIe6.2_Spec_ch05_Power_Management_电源管理.md) |
| 6 | [System Architecture](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md) | [系统架构](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md) | 707–980 | 209 | ✅ Done | [📄](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md) |
| 7 | [Software Initialization and Configuration](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md) | [软件初始化与配置](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md) | 981–1408 | 399 | ✅ Done | [📄](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md) |
| 8 | [Electrical Sub-Block](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md) | [电气子块](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md) | 1409–1522 | 66 | ✅ Done | [📄](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md) |
| 9 | [Single Root I/O Virtualization (SR-IOV)](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md) | [SR-IOV 单根 I/O 虚拟化](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md) | 1523–1558 | 20 | ✅ Done | [📄](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md) |
| 10 | [Address Translation Services (ATS)](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md) | [ATS 地址转换服务](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md) | 1559–1608 | 5 | ✅ Done | [📄](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md) |
| 11 | [TEE Device Interface Security Protocol (TDISP)](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md) | [TDISP TEE 设备接口安全协议](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md) | 1609–1658 | 13 | ✅ Done | [📄](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md) |
| 12 | [Architectural Out-of-Band Management](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md) | [架构带外管理](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md) | 1659–1702 | 54 | ✅ Done | [📄](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md) |

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

### 2026-06-28 — README 跳转链接修复 + 各章 TOC 小节跳转

- **README 章节状态表**: EN/ZH 标题链接改为直接指向对应 `.md` 文件（点击直接打开章节）
- **各章 📑 章节索引**: 12 章共添加 **+1526 个** Markdown 小节跳转链接（中英双语列均可用）
- **主锚点补全**: ch04/ch05/ch07/ch08 各章主入口锚点 `sec-N-0` 就绪
- **验证结果**: 全部 5574 个锚点引用，0 处断裂；43 行正文不存在的节保留原文无链接
- **工具脚本**: `fix_toc_links.py`（TOC 链接批量修复）

### 2026-06-16 — 全章节 Figure 精裁剪 + 去重 (Round 3: 模板推广)

- **ch4 模板推广到 ch1-12**: 三套通用化脚本(精裁剪/升级/去重)对 12 章批量运行
- **精裁图统计**:
  - 12 章共 **611 个 `<img>` 标签**,其中 **491 (80%)** 升级到 `*_tight.png`,120 个保留全页兜底
- **跨列重复 img 清理**: ch2 18 对 / ch5 4 对 / ch6 11 对 / ch7 40 对 / ch8 10 对 / ch11 2 对,合计 **85 对** 重复清理
- **新增通用化脚本**:
  - `tools/chx_tight_crops.py` (支持任意章节 N→M 范围)
  - `tools/chx_apply_tight.py` (批量升级 MD 引用)
  - `tools/chx_dedup_imgs.py` (批量去重)
- **每章输出**: `ch{N}_tight_crops.json` 映射数据

### 2026-06-16 — ch04 Figure 精裁剪与排版修复 (Round 2)

- **ch4 精裁图抽取**：基于 MinerU `content_list.json` bbox + 抽取图,渲染 **46 张** `*_tight.png` 精裁 PNG,覆盖 40 页 / 46 个 Figure 4-XX
- **双轨制策略**：`fig_PPPP_NN_tight.png` (精裁) 优先 + `fig_PPPP_NN.png` (全页) 兜底,详见 [`CH4_FIGURE_STRATEGY.md`](CH4_FIGURE_STRATEGY.md)
- **ch04 MD img 引用升级**：64 个 `<img>` 标签中 **47 个**自动升级为精裁图,17 个保留全页兜底(MinerU 未捕获的图)
- **Figure 4-24 误分类修复**：MinerU 将 PAM4 信令表误判为 `type=table`,通过同时检查 `image_caption` + `table_caption` 解决
- **多图页面拆分**：9 个含多张 Figure 的页面(page 354/359/360/368/384/404/433/448/586)按 caption y 坐标顺序生成 _1/_2/_3 后缀
- **新增文件**:
  - `tools/ch4_figure_map.py` (扫描脚本)
  - `tools/ch4_tight_crops.py` (精裁渲染脚本)
  - `tools/ch4_apply_tight_crops.py` (MD 引用升级脚本)
  - `ch4_figure_map.json` / `ch4_tight_crops.json` (映射数据)
  - `CH4_FIGURE_STRATEGY.md` (策略文档)

### 2026-06-16 — ch04 排版与图引用修复

针对 `PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md` 的扫描修复：

- **HTML 截断修复**：批量补齐 152 处 `table>` 缺失的 `<` 起始符（`→ <table>`），恢复中英对照双列渲染。
- **4.2.3.1.1 PAM4 Signaling**：
  - 补齐缺失的 intro 段（PAM4 定义、4 电平映射、DC 平衡说明）+ 对应中文翻译
  - 嵌入 **Figure 4-24** (`fig_0385_1.png`)，并配中英双语 caption
- **4.2.3.1.2 末尾**：嵌入 **Figure 4-25** (`fig_0386_1.png`)，加注原图主体未被单独抽取的回退说明
- **4.2.4 Link Equalization 标题层级**：13 个 `## 4.2.4` 子节降级为 `### 4.2.4`（保留主节 h2），原 `## 4.2.4.1` / `## 4.2.4.2` 同步降为 h3
- **3 处 Figure 标题**（Figure 4-40 / 4-41 / 4-44）误用 h2，降为 h4
- **Figure 4-43 缺失图**：原 `fig_0448_2.png` 不存在，替换为 `fig_0448_1.png` 并加占位说明

净变更：24078 → 24002 行（-76 行）。

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
