# 📚 PCIe 6.2 Spec 中英对照翻译

> **PCI Express® Base Specification — Revision 6.2, Version 1.0 — January 25, 2024**

📄 **Source PDF**: [`NCB-PCI_Express_Base_6.2-2024-01-25.pdf`](https://pcisig.com/specifications) (2111 pages, 27.8 MB)
🎨 **Format**: 中英对照双语 Markdown · 原始图表保留为 PNG · 中文背景色灰色 · GitHub Flavored Markdown
📐 **Template**: 基于 [CXL 3.2 Spec 中英对照翻译](https://github.com/jimwang2050/CXL_3.2_Spec) 模板
🐙 **GitHub**: https://github.com/jimwang2050/PCIe6.2_Spec

---

## 🧭 内容导航与归档

仓库根目录优先保留最终阅读内容：12 个章节 Markdown、`book.md`、`preview/`、`figures/`、`chapter_index.json`、`glossary.json`、`tight_crops/` 和 `tools/`。

项目过程文档、质量报告和一次性修复脚本的归档范围见 [`archive/README.md`](archive/README.md)。

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

---

## 📖 阅读目录指引 (Reading Guide)

> 12 章按主题归为 5 个板块，可按需跳读；标 ★ 为核心协议栈，建议重点精读。

### ① 入门 · 建立全局视角

- **第 1 章 [引言](PCIe6.2_Spec_ch01_Introduction_引言.md)** — PCIe 6.2 概览、术语定义、与 6.0/6.1 的差异、文档约定
- **第 6 章 [系统架构](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md)** — Root Complex / Switch / Endpoint 拓扑、组件模型、中断与错误上报

### ② 核心协议栈 ★ · 事务 → 链路 → 物理

| 协议层 | 章节 | 核心内容 |
|--------|------|----------|
| 事务层 | 第 2 章 [事务层规范](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) | TLP 结构、事务类型、排序、流控、地址空间 |
| 数据链路层 | 第 3 章 [数据链路层规范](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) | DLLP、ACK/NAK、重试、LCRC、链路初始化 |
| 物理层逻辑块 | 第 4 章 [物理层逻辑块](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) | Flit 模式、128b/130b 编码、LTSSM、链路训练 |

### ③ 电气与电源 · 信号完整性与功耗

- **第 8 章 [电气子块](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md)** — 电气参数、发送/接收均衡、抖动、互操作性
- **第 5 章 [电源管理](PCIe6.2_Spec_ch05_Power_Management_电源管理.md)** — ASPM、L/D 状态、PME、电源预算、热插拔

### ④ 软件视角 · 配置与枚举

- **第 7 章 [软件初始化与配置](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md)** — 配置空间、能力结构、枚举流程、寄存器定义
  - 本章已拆分便于阅读：[Part A (7.1–7.8)](PCIe6.2_Spec_ch07_软件初始化与配置_Part_A_7_1-7_8.md) · [Part B (7.9–7.30)](PCIe6.2_Spec_ch07_软件初始化与配置_Part_B_7_9-7_30.md)

### ⑤ 高级/可选特性 · 按需查阅

- **第 9 章 [SR-IOV](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md)** — 单根 I/O 虚拟化（PF/VF、ARI）
- **第 10 章 [ATS](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md)** — 地址转换服务（IOMMU / 设备 TLB）
- **第 11 章 [TDISP](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md)** — TEE 设备接口安全协议
- **第 12 章 [架构带外管理](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md)** — 带外管理、FRU、Sideband

### 🎯 快速定位

| 想了解… | 直接读… |
|---------|---------|
| TLP 报文格式 / 排序 / 流控 | 第 2 章 |
| 链路可靠性（ACK/NAK / 重试 / CRC） | 第 3 章 |
| Flit 模式 / 编码 / 链路训练 / LTSSM | 第 4 章 |
| 电气参数 / 均衡 / 抖动 | 第 8 章 |
| 电源状态 / ASPM / 热插拔 | 第 5 章 |
| 配置寄存器 / 枚举 / 能力结构 | 第 7 章 |
| 虚拟化 (PF/VF) | 第 9 章 |
| 地址转换 / IOMMU | 第 10 章 |
| 安全 / TEE | 第 11 章 |
| 带外管理 / FRU | 第 12 章 |
