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

> ★ = 核心必读章节（基础 + 协议栈 + 软件配置）；未标 ★ 为专题/可选特性，按方向或需求查阅。

| Ch | 章节 | 页码 | 核心内容 |
|:--:|------|:----:|----------|
| 1 | [Introduction · 引言](PCIe6.2_Spec_ch01_Introduction_引言.md) ★ | 127–140 | 规范组织、术语定义、与 6.0/6.1 的差异 |
| 2 | [Transaction Layer · 事务层规范](PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md) ★ | 141–308 | TLP 格式、事务类型、排序、流控、地址空间 |
| 3 | [Data Link Layer · 数据链路层规范](PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md) ★ | 309–350 | DLLP、ACK/NAK、重试、LCRC、链路初始化 |
| 4 | [Physical Layer Logical Block · 物理层逻辑块](PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md) ★ | 351–650 | Flit 模式、128b/130b 编码、LTSSM、链路训练 |
| 5 | [Power Management · 电源管理](PCIe6.2_Spec_ch05_Power_Management_电源管理.md) | 651–706 | D/L 电源状态、ASPM、PME、热插拔 |
| 6 | [System Architecture · 系统架构](PCIe6.2_Spec_ch06_System_Architecture_系统架构.md) ★ | 707–980 | RC/Switch/Endpoint 拓扑、组件模型、中断与错误上报 |
| 7 | [Software Init & Config · 软件初始化与配置](PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md) ★ | 981–1408 | 配置空间、能力结构、枚举、寄存器定义 |
| 8 | [Electrical Sub-Block · 电气子块](PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md) | 1409–1522 | 电气参数、发送/接收均衡、抖动、互操作性 |
| 9 | [SR-IOV · 单根 I/O 虚拟化](PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md) | 1523–1558 | PF/VF、ARI、资源虚拟化与共享 |
| 10 | [ATS · 地址转换服务](PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md) | 1559–1608 | 地址转换、设备 TLB、IOMMU 交互 |
| 11 | [TDISP · TEE 设备接口安全协议](PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md) | 1609–1658 | TEE、TSM、安全上下文、设备认证 |
| 12 | [Architectural OOB · 架构带外管理](PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md) | 1659–1702 | 带外管理、FRU、Sideband、Retimer |

> **建议阅读顺序**：第 1、6 章建立全局视角 → 第 2、3、4 章精读协议栈 → 按方向深入（软件走第 7 章，硬件走第 5、8 章）→ 第 9–12 章按需查阅专题。

> **第 7 章已拆分**：[Part A (7.1–7.8)](PCIe6.2_Spec_ch07_软件初始化与配置_Part_A_7_1-7_8.md) · [Part B (7.9–7.30)](PCIe6.2_Spec_ch07_软件初始化与配置_Part_B_7_9-7_30.md) 便于分篇阅读。
