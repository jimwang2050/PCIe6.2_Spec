#!/usr/bin/env python3
"""
Build a PCIe-specific translation glossary from CXL 3.2 (CXL_zh/) samples.

CXL shares most physical/link-layer terminology with PCIe, and the CXL_zh
translation has already established consistent Chinese terms for these.
We sample a few CXL 3.2 chapters, extract a curated set of terms, and
write a glossary.json that translation sub-agents will inject into their
prompts.
"""
import json
import re
from pathlib import Path

CXL_ZH = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh')
OUT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh/glossary.json')

# Curated PCIe/CXL terms (source EN -> target ZH).
# Built from CXL 3.2 terminology + PCIe Base 6.2 chapter 1-2 inspection.
# Categories: protocol/architecture/feature/reg/concept
TERMS = [
    # === Layers & Architecture ===
    {"source": "Transaction Layer", "target": "事务层", "category": "layer"},
    {"source": "Data Link Layer", "target": "数据链路层", "category": "layer"},
    {"source": "Physical Layer", "target": "物理层", "category": "layer"},
    {"source": "Logical PHY", "target": "逻辑 PHY", "category": "block"},
    {"source": "Physical PHY", "target": "物理 PHY", "category": "block"},
    {"source": "Electrical Sub-Block", "target": "电气子块", "category": "block"},
    {"source": "MAC", "target": "MAC", "category": "block"},
    {"source": "PCS", "target": "PCS", "category": "block"},
    {"source": "PMA", "target": "PMA", "category": "block"},
    {"source": "PIPE", "target": "PIPE", "category": "interface"},

    # === Devices & Topology ===
    {"source": "Root Complex", "target": "根复合体 (Root Complex)", "category": "device"},
    {"source": "RC", "target": "根复合体 (RC)", "category": "device"},
    {"source": "Endpoint", "target": "端点 (Endpoint)", "category": "device"},
    {"source": "Switch", "target": "交换机 (Switch)", "category": "device"},
    {"source": "Bridge", "target": "桥 (Bridge)", "category": "device"},
    {"source": "Root Port", "target": "根端口 (Root Port)", "category": "port"},
    {"source": "Downstream Port", "target": "下游端口 (Downstream Port)", "category": "port"},
    {"source": "Upstream Port", "target": "上游端口 (Upstream Port)", "category": "port"},
    {"source": "PCI Express Port", "target": "PCI Express 端口", "category": "port"},
    {"source": "Lane", "target": "通道 (Lane)", "category": "link"},
    {"source": "Link", "target": "链路 (Link)", "category": "link"},

    # === Transactions & Packets ===
    {"source": "Transaction Layer Packet", "target": "事务层包 (TLP)", "category": "packet"},
    {"source": "TLP", "target": "TLP", "category": "packet"},
    {"source": "Data Link Layer Packet", "target": "数据链路层包 (DLLP)", "category": "packet"},
    {"source": "DLLP", "target": "DLLP", "category": "packet"},
    {"source": "Flit", "target": "Flit (流量控制单元)", "category": "packet"},
    {"source": "Flit Mode", "target": "Flit 模式", "category": "mode"},
    {"source": "Non-Flit Mode", "target": "非 Flit 模式", "category": "mode"},
    {"source": "Completion", "target": "完成报文 (Completion)", "category": "packet"},
    {"source": "Request", "target": "请求 (Request)", "category": "packet"},
    {"source": "Posted", "target": "Posted (有数据,无完成)", "category": "transaction"},
    {"source": "Non-Posted", "target": "Non-Posted (无数据,需完成)", "category": "transaction"},

    # === Address Spaces & Routing ===
    {"source": "Memory Space", "target": "内存空间 (Memory Space)", "category": "address"},
    {"source": "I/O Space", "target": "I/O 空间 (I/O Space)", "category": "address"},
    {"source": "Configuration Space", "target": "配置空间 (Configuration Space)", "category": "address"},
    {"source": "Message Space", "target": "消息空间 (Message Space)", "category": "address"},
    {"source": "Base Address Register", "target": "基址寄存器 (BAR)", "category": "register"},
    {"source": "BAR", "target": "BAR (基址寄存器)", "category": "register"},
    {"source": "ID-Based Ordering", "target": "基于 ID 的排序 (IDO)", "category": "feature"},
    {"source": "IDO", "target": "IDO (基于 ID 的排序)", "category": "feature"},

    # === Flow Control & Credits ===
    {"source": "Flow Control", "target": "流控 (Flow Control)", "category": "feature"},
    {"source": "Flow Control Credit", "target": "流控信用 (Flow Control Credit)", "category": "feature"},
    {"source": "Credit", "target": "信用 (Credit)", "category": "feature"},
    {"source": "FC Credit", "target": "流控信用 (FC Credit)", "category": "feature"},

    # === TLP Header Fields ===
    {"source": "Header", "target": "包头 (Header)", "category": "field"},
    {"source": "Fmt", "target": "Fmt 字段 (格式)", "category": "field"},
    {"source": "Type", "target": "Type 字段 (类型)", "category": "field"},
    {"source": "TC", "target": "TC 字段 (流量类)", "category": "field"},
    {"source": "Traffic Class", "target": "流量类 (TC, Traffic Class)", "category": "field"},
    {"source": "TD", "target": "TD 位 (中毒数据)", "category": "field"},
    {"source": "EP", "target": "EP 位 (中毒)", "category": "field"},
    {"source": "Attr", "target": "Attr 字段 (属性)", "category": "field"},
    {"source": "AT", "target": "AT 字段 (地址类型)", "category": "field"},
    {"source": "Address Type", "target": "地址类型 (AT)", "category": "field"},
    {"source": "Length", "target": "Length 字段 (长度)", "category": "field"},
    {"source": "Requester ID", "target": "请求者 ID (Requester ID)", "category": "field"},
    {"source": "Tag", "target": "Tag 字段 (标签)", "category": "field"},
    {"source": "Byte Enable", "target": "字节使能 (Byte Enable)", "category": "field"},

    # === Errors & Poison ===
    {"source": "Poison", "target": "Poison (数据中毒)", "category": "error"},
    {"source": "Poisoned TLP", "target": "中毒 TLP (Poisoned TLP)", "category": "error"},
    {"source": "Poisoned Data", "target": "中毒数据 (Poisoned Data)", "category": "error"},
    {"source": "Data Poisoning", "target": "数据中毒 (Data Poisoning)", "category": "error"},
    {"source": "Error", "target": "错误 (Error)", "category": "error"},
    {"source": "Correctable Error", "target": "可纠正错误 (Correctable Error)", "category": "error"},
    {"source": "Uncorrectable Error", "target": "不可纠正错误 (Uncorrectable Error)", "category": "error"},
    {"source": "Fatal Error", "target": "致命错误 (Fatal Error)", "category": "error"},

    # === Power Management ===
    {"source": "Power Management", "target": "电源管理 (Power Management)", "category": "feature"},
    {"source": "Power State", "target": "电源状态 (Power State)", "category": "feature"},
    {"source": "L0", "target": "L0 (全功率工作状态)", "category": "state"},
    {"source": "L0s", "target": "L0s (低功耗空闲)", "category": "state"},
    {"source": "L1", "target": "L1 (低功耗休眠)", "category": "state"},
    {"source": "L1.1", "target": "L1.1", "category": "state"},
    {"source": "L1.2", "target": "L1.2", "category": "state"},
    {"source": "L2", "target": "L2 (深度休眠)", "category": "state"},
    {"source": "L3", "target": "L3 (断电)", "category": "state"},
    {"source": "D0", "target": "D0 (设备全功率)", "category": "state"},
    {"source": "D1", "target": "D1", "category": "state"},
    {"source": "D2", "target": "D2", "category": "state"},
    {"source": "D3hot", "target": "D3hot", "category": "state"},
    {"source": "D3cold", "target": "D3cold", "category": "state"},
    {"source": "ASPM", "target": "ASPM (自主电源管理)", "category": "feature"},
    {"source": "Active State Power Management", "target": "主动状态电源管理 (ASPM)", "category": "feature"},
    {"source": "PME", "target": "PME (电源管理事件)", "category": "feature"},
    {"source": "Wake", "target": "唤醒 (Wake)", "category": "feature"},

    # === System Architecture ===
    {"source": "Hot-Plug", "target": "热插拔 (Hot-Plug)", "category": "feature"},
    {"source": "Hot Plug", "target": "热插拔 (Hot Plug)", "category": "feature"},
    {"source": "Surprise Hot Plug", "target": "意外热插拔 (Surprise Hot Plug)", "category": "feature"},
    {"source": "Quality of Service", "target": "服务质量 (QoS)", "category": "feature"},
    {"source": "QoS", "target": "QoS (服务质量)", "category": "feature"},
    {"source": "VC", "target": "VC (虚通道)", "category": "feature"},
    {"source": "Virtual Channel", "target": "虚通道 (VC, Virtual Channel)", "category": "feature"},
    {"source": "TC/VC Mapping", "target": "TC/VC 映射", "category": "feature"},
    {"source": "Arbitration", "target": "仲裁 (Arbitration)", "category": "feature"},
    {"source": "Port Arbitration", "target": "端口仲裁 (Port Arbitration)", "category": "feature"},

    # === Configuration & Enumeration ===
    {"source": "Enumeration", "target": "枚举 (Enumeration)", "category": "feature"},
    {"source": "Configuration Request", "target": "配置请求 (Configuration Request)", "category": "transaction"},
    {"source": "Type 0 Configuration", "target": "Type 0 配置 (端点)", "category": "transaction"},
    {"source": "Type 1 Configuration", "target": "Type 1 配置 (桥)", "category": "transaction"},
    {"source": "PCI-Compatible", "target": "PCI 兼容 (PCI-Compatible)", "category": "feature"},
    {"source": "PCI Express Capability", "target": "PCI Express 能力结构 (Capability)", "category": "register"},
    {"source": "Capabilities Register", "target": "能力寄存器 (Capabilities Register)", "category": "register"},
    {"source": "Extended Configuration Space", "target": "扩展配置空间 (Extended Configuration Space)", "category": "address"},

    # === Interrupt ===
    {"source": "Interrupt", "target": "中断 (Interrupt)", "category": "feature"},
    {"source": "Legacy Interrupt", "target": "传统中断 (Legacy Interrupt)", "category": "feature"},
    {"source": "MSI", "target": "MSI (消息信号中断)", "category": "feature"},
    {"source": "Message Signaled Interrupt", "target": "消息信号中断 (MSI)", "category": "feature"},
    {"source": "MSI-X", "target": "MSI-X (扩展消息信号中断)", "category": "feature"},

    # === SR-IOV ===
    {"source": "Single Root I/O Virtualization", "target": "单根 I/O 虚拟化 (SR-IOV)", "category": "feature"},
    {"source": "SR-IOV", "target": "SR-IOV (单根 I/O 虚拟化)", "category": "feature"},
    {"source": "PF", "target": "PF (物理功能)", "category": "feature"},
    {"source": "Physical Function", "target": "物理功能 (PF)", "category": "feature"},
    {"source": "VF", "target": "VF (虚拟功能)", "category": "feature"},
    {"source": "Virtual Function", "target": "虚拟功能 (VF)", "category": "feature"},
    {"source": "ARI", "target": "ARI (替代路由 ID 解释)", "category": "feature"},
    {"source": "Alternative Routing ID Interpretation", "target": "替代路由 ID 解释 (ARI)", "category": "feature"},

    # === ATS / DMA ===
    {"source": "Address Translation Service", "target": "地址转换服务 (ATS)", "category": "feature"},
    {"source": "ATS", "target": "ATS (地址转换服务)", "category": "feature"},
    {"source": "Translated Request", "target": "已转换请求 (Translated Request)", "category": "transaction"},
    {"source": "Untranslated Request", "target": "未转换请求 (Untranslated Request)", "category": "transaction"},
    {"source": "IOMMU", "target": "IOMMU (I/O 内存管理单元)", "category": "block"},
    {"source": "Translation Agent", "target": "转换代理 (Translation Agent)", "category": "block"},
    {"source": "Device-TLB", "target": "设备 TLB (Device-TLB)", "category": "block"},
    {"source": "ATS Invalidate", "target": "ATS 无效化 (ATS Invalidate)", "category": "feature"},
    {"source": "Page Request Interface", "target": "页请求接口 (PRI)", "category": "feature"},
    {"source": "PRI", "target": "PRI (页请求接口)", "category": "feature"},
    {"source": "Page Request", "target": "页请求 (Page Request)", "category": "feature"},
    {"source": "Stop Marker", "target": "停止标记 (Stop Marker)", "category": "feature"},

    # === TDISP (TEE Device Interface Security Protocol) ===
    {"source": "TEE", "target": "TEE (可信执行环境)", "category": "feature"},
    {"source": "Trusted Execution Environment", "target": "可信执行环境 (TEE)", "category": "feature"},
    {"source": "TDISP", "target": "TDISP (TEE 设备接口安全协议)", "category": "feature"},
    {"source": "TEE Device Interface Security Protocol", "target": "TEE 设备接口安全协议 (TDISP)", "category": "feature"},
    {"source": "TSM", "target": "TSM (TEE 安全管理器)", "category": "feature"},
    {"source": "TEE Security Manager", "target": "TEE 安全管理器 (TSM)", "category": "feature"},
    {"source": "DSM", "target": "DSM (设备安全管理器)", "category": "feature"},
    {"source": "Device Security Manager", "target": "设备安全管理器 (DSM)", "category": "feature"},
    {"source": "IDE", "target": "IDE (完整性与数据加密)", "category": "feature"},
    {"source": "Integrity and Data Encryption", "target": "完整性与数据加密 (IDE)", "category": "feature"},
    {"source": "Key", "target": "密钥 (Key)", "category": "concept"},
    {"source": "Stream", "target": "流 (Stream)", "category": "concept"},

    # === Out-of-Band Management ===
    {"source": "Out-of-Band", "target": "带外 (Out-of-Band, OOB)", "category": "feature"},
    {"source": "OOB", "target": "OOB (带外)", "category": "feature"},
    {"source": "Sideband", "target": "边带 (Sideband)", "category": "feature"},
    {"source": "In-Band", "target": "带内 (In-Band)", "category": "feature"},
    {"source": "FRU", "target": "FRU (现场可更换单元)", "category": "feature"},
    {"source": "Field Replaceable Unit", "target": "现场可更换单元 (FRU)", "category": "feature"},
    {"source": "Retimer", "target": "Retimer (重定时器)", "category": "block"},
    {"source": "Interposer", "target": "Interposer (中间板)", "category": "device"},
    {"source": "Riser", "target": "Riser (转接卡)", "category": "device"},
    {"source": "MCIO", "target": "MCIO", "category": "interface"},
    {"source": "Sidecar", "target": "Sidecar (副卡)", "category": "device"},
    {"source": "PERST", "target": "PERST (PCIe 复位信号)", "category": "signal"},
    {"source": "PESTI", "target": "PESTI", "category": "signal"},
    {"source": "REFCLK", "target": "REFCLK (参考时钟)", "category": "signal"},
    {"source": "PWRBRK", "target": "PWRBRK (电源降级信号)", "category": "signal"},
    {"source": "SMBus", "target": "SMBus (系统管理总线)", "category": "bus"},
    {"source": "I2C", "target": "I2C (集成电路总线)", "category": "bus"},
    {"source": "I3C", "target": "I3C (改进型集成电路总线)", "category": "bus"},
    {"source": "2-Wire", "target": "两线制 (2-Wire)", "category": "interface"},
    {"source": "VGA", "target": "VGA", "category": "device"},
    {"source": "USB", "target": "USB", "category": "bus"},

    # === Physical Layer specifics ===
    {"source": "PAM4", "target": "PAM4 (四电平脉冲幅度调制)", "category": "modulation"},
    {"source": "NRZ", "target": "NRZ (非归零编码)", "category": "modulation"},
    {"source": "128b/130b", "target": "128b/130b 编码", "category": "encoding"},
    {"source": "64b/66b", "target": "64b/66b 编码", "category": "encoding"},
    {"source": "8b/10b", "target": "8b/10b 编码", "category": "encoding"},
    {"source": "SerDes", "target": "SerDes (串行器/解串器)", "category": "block"},
    {"source": "Equalization", "target": "均衡 (Equalization)", "category": "feature"},
    {"source": "CTLE", "target": "CTLE (连续时间线性均衡器)", "category": "block"},
    {"source": "DFE", "target": "DFE (判决反馈均衡器)", "category": "block"},
    {"source": "LTSSM", "target": "LTSSM (链路训练与状态机)", "category": "feature"},
    {"source": "Link Training and Status State Machine", "target": "链路训练与状态机 (LTSSM)", "category": "feature"},
    {"source": "TS", "target": "TS (训练序列)", "category": "feature"},
    {"source": "Training Sequence", "target": "训练序列 (TS)", "category": "feature"},
    {"source": "SKP", "target": "SKP (跳过有序集)", "category": "feature"},
    {"source": "Compliance Pattern", "target": "一致性测试码型 (Compliance Pattern)", "category": "feature"},
    {"source": "Beacon", "target": "Beacon 信号", "category": "signal"},
    {"source": "Electrical Idle", "target": "电气空闲 (Electrical Idle)", "category": "state"},
    {"source": "EI", "target": "EI (电气空闲)", "category": "state"},
    {"source": "Receiver", "target": "接收器 (Receiver)", "category": "block"},
    {"source": "Transmitter", "target": "发送器 (Transmitter)", "category": "block"},
    {"source": "De-emphasis", "target": "去加重 (De-emphasis)", "category": "feature"},
    {"source": "Preset", "target": "预设 (Preset)", "category": "feature"},

    # === LTSSM States ===
    {"source": "Detect", "target": "Detect (检测)", "category": "state"},
    {"source": "Polling", "target": "Polling (轮询)", "category": "state"},
    {"source": "Configuration", "target": "Configuration (配置)", "category": "state"},
    {"source": "Recovery", "target": "Recovery (恢复)", "category": "state"},
    {"source": "L0 State", "target": "L0 状态 (工作状态)", "category": "state"},
    {"source": "L1 State", "target": "L1 状态 (低功耗)", "category": "state"},
    {"source": "Hot Reset", "target": "热复位 (Hot Reset)", "category": "state"},
    {"source": "Loopback", "target": "Loopback (回环)", "category": "state"},
    {"source": "Disable", "target": "Disable (禁用)", "category": "state"},

    # === Retry / Replay ===
    {"source": "Replay", "target": "重放 (Replay)", "category": "feature"},
    {"source": "Replay Timer", "target": "重放定时器 (Replay Timer)", "category": "feature"},
    {"source": "Replay Number", "target": "重放号 (Replay Number)", "category": "field"},
    {"source": "ACK", "target": "ACK (确认)", "category": "feature"},
    {"source": "NAK", "target": "NAK (否认)", "category": "feature"},
    {"source": "ACK DLLP", "target": "ACK DLLP (确认 DLLP)", "category": "packet"},
    {"source": "NAK DLLP", "target": "NAK DLLP (否认 DLLP)", "category": "packet"},
    {"source": "Sequence Number", "target": "序列号 (Sequence Number)", "category": "field"},
    {"source": "CRC", "target": "CRC (循环冗余校验)", "category": "feature"},
    {"source": "LCRC", "target": "LCRC (链路 CRC)", "category": "feature"},
    {"source": "ECRC", "target": "ECRC (端到端 CRC)", "category": "feature"},

    # === Virtualization & ATS ===
    {"source": "VF Enable", "target": "VF 使能 (VF Enable)", "category": "feature"},
    {"source": "ARI Capable Hierarchy", "target": "支持 ARI 的层级 (ARI Capable Hierarchy)", "category": "feature"},
    {"source": "ATS Translation Completion", "target": "ATS 转换完成 (ATS Translation Completion)", "category": "packet"},

    # === Speed & Bandwidth ===
    {"source": "Generation", "target": "代 (Generation)", "category": "concept"},
    {"source": "Gen1", "target": "Gen1 (2.5 GT/s)", "category": "speed"},
    {"source": "Gen2", "target": "Gen2 (5.0 GT/s)", "category": "speed"},
    {"source": "Gen3", "target": "Gen3 (8.0 GT/s)", "category": "speed"},
    {"source": "Gen4", "target": "Gen4 (16.0 GT/s)", "category": "speed"},
    {"source": "Gen5", "target": "Gen5 (32.0 GT/s)", "category": "speed"},
    {"source": "Gen6", "target": "Gen6 (64.0 GT/s, PAM4)", "category": "speed"},
    {"source": "FLIT", "target": "FLIT (流量控制单元)", "category": "concept"},
    {"source": "Throughput", "target": "吞吐率 (Throughput)", "category": "concept"},
    {"source": "Bandwidth", "target": "带宽 (Bandwidth)", "category": "concept"},
    {"source": "Latency", "target": "延迟 (Latency)", "category": "concept"},

    # === Concepts & Verbs ===
    {"source": "Negotiation", "target": "协商 (Negotiation)", "category": "feature"},
    {"source": "Negotiate", "target": "协商 (Negotiate)", "category": "feature"},
    {"source": "Advertise", "target": "通告 (Advertise)", "category": "feature"},
    {"source": "Ack", "target": "确认 (Ack)", "category": "feature"},
    {"source": "Encoding", "target": "编码 (Encoding)", "category": "feature"},
    {"source": "Decoding", "target": "解码 (Decoding)", "category": "feature"},
    {"source": "Scrambling", "target": "加扰 (Scrambling)", "category": "feature"},
    {"source": "De-scrambling", "target": "解扰 (De-scrambling)", "category": "feature"},

    # === Misc PCIe terminology ===
    {"source": "Host Bridge", "target": "主桥 (Host Bridge)", "category": "device"},
    {"source": "System Image", "target": "系统映像 (System Image)", "category": "concept"},
    {"source": "Hierarchy", "target": "层级 (Hierarchy)", "category": "concept"},
    {"source": "Fabric", "target": "Fabric (互连网络)", "category": "concept"},
    {"source": "Topology", "target": "拓扑 (Topology)", "category": "concept"},
    {"source": "Form Factor", "target": "外形规格 (Form Factor)", "category": "concept"},
    {"source": "Card", "target": "卡 (Card)", "category": "device"},
    {"source": "Adapter", "target": "适配器 (Adapter)", "category": "device"},
    {"source": "Module", "target": "模块 (Module)", "category": "device"},
    {"source": "Connector", "target": "连接器 (Connector)", "category": "device"},
    {"source": "Slot", "target": "插槽 (Slot)", "category": "device"},
    {"source": "Pin", "target": "引脚 (Pin)", "category": "device"},
    {"source": "Ball", "target": "焊球 (Ball)", "category": "device"},
    {"source": "Wafer", "target": "晶圆 (Wafer)", "category": "device"},
    {"source": "Die", "target": "芯片裸片 (Die)", "category": "device"},
    {"source": "Package", "target": "封装 (Package)", "category": "device"},
    {"source": "Reset", "target": "复位 (Reset)", "category": "feature"},
    {"source": "Cold Reset", "target": "冷复位 (Cold Reset)", "category": "feature"},
    {"source": "Warm Reset", "target": "热复位 (Warm Reset)", "category": "feature"},
    {"source": "Fundamental Reset", "target": "基本复位 (Fundamental Reset)", "category": "feature"},
    {"source": "Conventional Reset", "target": "常规复位 (Conventional Reset)", "category": "feature"},

    # === PCI-SIG & Standardization ===
    {"source": "PCI-SIG", "target": "PCI-SIG (PCI 特殊兴趣小组)", "category": "organization"},
    {"source": "Specification", "target": "规范 (Specification)", "category": "concept"},
    {"source": "Errata", "target": "勘误 (Errata)", "category": "concept"},
    {"source": "ECN", "target": "ECN (工程变更通知)", "category": "concept"},
    {"source": "Engineering Change Notice", "target": "工程变更通知 (ECN)", "category": "concept"},
    {"source": "Compliance", "target": "一致性 (Compliance)", "category": "concept"},
    {"source": "Compliance Testing", "target": "一致性测试 (Compliance Testing)", "category": "concept"},
]


def main():
    terms = []
    for i, t in enumerate(TERMS):
        terms.append({
            "id": t['source'].lower().replace(' ', '_').replace('/', '_').replace('-', '_').replace('(', '').replace(')', ''),
            "source": t['source'],
            "target": t['target'],
            "category": t['category'],
            "aliases": [],
            "gender": "unknown",
            "confidence": "high",
            "frequency": 0,
            "evidence_refs": [],
            "notes": "Curated from CXL 3.2 (CXL_zh/) translation; shared PCIe terminology"
        })

    glossary = {
        "version": 2,
        "terms": terms,
        "high_frequency_top_n": 30,
        "applied_meta_hashes": {}
    }

    with open(OUT, 'w') as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(terms)} terms to {OUT}")


if __name__ == '__main__':
    main()
