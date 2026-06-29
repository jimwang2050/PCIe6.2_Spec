## 7.9 Additional PCI and PCIe Capabilities | 7.9 其他 PCI 和 PCIe 能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This section, contains a description of additional PCI and PCIe capabilities that are individually optional in this but may be required by other PCISIG specifications.

</td>
<td style="background-color:#e8e8e8">

本节描述本规范中各自独立的可选 PCI 和 PCIe 能力,虽然这些能力在本规范中是可选的,但其他 PCI-SIG 规范可能要求实现。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-1"></a>
## 7.9.1 Virtual Channel Extended Capability | 7.9.1 虚通道扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Virtual Channel Extended Capability (VC Extended Capability) is an optional Extended Capability required for devices that have Ports (or for individual Functions) that support functionality beyond the default Traffic Class (TC0) over the default Virtual Channel (VC0). This may apply to devices with only one VC that support TC filtering or to devices that support multiple VCs. Note that a PCI Express device that supports only TC0 over VC0 does not require VC Extended Capability and associated registers. § Figure 7-221 provides a high level view of the Virtual Channel Extended Capability structure. This structure controls Virtual Channel assignment for PCI Express Links and may be present in any device (or RCRB) that contains (controls) a Port, or any device that has a Multi-Function Virtual Channel (MFVC) Capability structure. Some registers/fields in the Virtual Channel Extended Capability structure may have different interpretation

</td>
<td style="background-color:#e8e8e8">

虚通道扩展能力(VC Extended Capability)是一项可选的扩展能力,适用于在默认虚通道(VC0)上支持超出默认流量类(TC0)功能的设备 Port(或单个 Function)。这可以适用于仅支持一个 VC 但具有 TC 过滤功能的设备,或支持多个 VC 的设备。请注意,仅在 VC0 上支持 TC0 的 PCI Express 设备不需要 VC 扩展能力及其相关寄存器。§ 图 7-221 提供了虚通道扩展能力结构的高层视图。该结构控制 PCI Express 链路的虚通道分配,可出现在包含(控制)一个 Port 的任何设备(或 RCRB)中,或任何具有多函数虚通道(MFVC)能力结构的设备中。虚通道扩展能力结构中的某些寄存器/字段可能对 Endpoint、Switch 端口、Root Port 和 RCRB 具有不同的解释。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1264 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

for Endpoints, Switch Ports, Root Ports and RCRB. Software must interpret the Device/Port Type field in the PCI Express Capabilities register to determine the availability and meaning of these registers/fields.

The number of (extended) Virtual Channels is indicated by the Extended VC Count field in the Port VC Capability Register 1. Software must interpret this field to determine the availability of extended VC Resource registers.

The VC Extended Capability structure is permitted in the Extended Configuration Space of all single-Function devices or in RCRBs.

Each VF uses the Virtual Channel of its associated PF. VFs themselves must not contain any Virtual Channel Capabilities.

A Multi-Function Device at an Upstream Port is permitted to contain a Multi-Function Virtual Channel (MFVC) Capability structure (see § Section 7.9.2 ). If a Multi-Function Device contains an MFVC Capability structure, any or all of its Functions with the exception of VFs are permitted to contain a VC Extended Capability structure. Per-Function VC Extended Capability structures are also permitted for devices inside a Switch that contain only Switch Downstream Port Functions, or for RCiEPs. Otherwise, only Function 0 is permitted to contain a VC Extended Capability structure.

To preserve software backward compatibility, two Extended Capability IDs are permitted for VC Extended Capability structures: 0002h and 0009h. Any VC Extended Capability structure in a device that also contains an MFVC Capability structure must use the Extended Capability ID 0009h. A VC Extended Capability structure in a device that does not contain an MFVC Capability structure must use the Extended Capability ID 0002h.

</td>
<td style="background-color:#e8e8e8">

软件必须解读 PCI Express 能力寄存器中的 Device/Port Type 字段,以确定这些寄存器/字段的可用性与含义。

(扩展)虚通道的数量由 Port VC Capability Register 1 中的 Extended VC Count 字段表示。软件必须解读该字段以确定扩展 VC 资源寄存器的可用性。

VC 扩展能力结构允许出现在所有单 Function 设备的扩展配置空间(Extended Configuration Space)中,或出现在 RCRB 中。

每个 VF 使用其关联 PF 的虚通道。VF 自身不得包含任何虚通道能力。

位于 Upstream Port 的多函数设备允许包含多函数虚通道(MFVC)能力结构(参见 § 7.9.2)。如果多函数设备包含 MFVC 能力结构,则其任何或所有 Function(VF 除外)允许包含 VC 扩展能力结构。仅包含 Switch 下游端口 Function 的 Switch 内部设备或 RCiEP 也允许包含按 Function 的 VC 扩展能力结构。除此之外,仅 Function 0 允许包含 VC 扩展能力结构。

为保持软件向后兼容性,VC 扩展能力结构允许使用两个扩展能力 ID:0002h 和 0009h。同时包含 MFVC 能力结构的设备中的任何 VC 扩展能力结构必须使用扩展能力 ID 0009h。不包含 MFVC 能力结构的设备中的 VC 扩展能力结构必须使用扩展能力 ID 0002h。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Figure 7-221. Virtual Channel Extended Capability Structure | 图 7-221 虚通道扩展能力结构**


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

*n = Extended VC Count
OM14320B
Port VC Capability Register 2
Port VC Capability Register 1
*n (2:0)
PCI Express Extended Capability Header
Port VC Control Register
Port VC Status Register
VC Arb Table
Offset (31:24)
Port Arb Table
Offset (31:24)
Port Arb Table
Offset (31:24)
0
Byte
Offset
31
16 15
04h
08h
00h
0Ch
10h
14h
18h
10h + *n 0Ch
14h + *n 0Ch
18h + *n 0Ch
VAT_Offset
*10h
PAT_Offset(0)
*10h
PAT_Offset(n)
*10h
 VC Resource Status Register (n)
RsvdP
 VC Resource Status Register (0)
RsvdP
VC Arbitration Table
VC Resource Capability Register (0)
VC Resource Control Register (0)
VC Resource Control Register (n)
VC Resource Capability Register (n)
All Devices
Switch ports, Root Ports and RCRB
Port Arbitration Table (0)
Port Arbitration Table (n)
Figure 7-221 Virtual Channel Extended Capability Structure

</td>
<td style="background-color:#e8e8e8">

*n = Extended VC Count(扩展 VC 数量)
OM14320B
Port VC Capability Register 2(Port VC 能力寄存器 2)
Port VC Capability Register 1(Port VC 能力寄存器 1)
*n (2:0)
PCI Express Extended Capability Header(PCI Express 扩展能力头)
Port VC Control Register(Port VC 控制寄存器)
Port VC Status Register(Port VC 状态寄存器)
VC Arb Table(VC 仲裁表)
Offset (31:24)(偏移量 (31:24))
Port Arb Table(端口仲裁表)
Offset (31:24)(偏移量 (31:24))
Port Arb Table(端口仲裁表)
Offset (31:24)(偏移量 (31:24))
0
Byte(字节)
Offset(偏移量)
31
16 15
04h
08h
00h
0Ch
10h
14h
18h
10h + *n 0Ch
14h + *n 0Ch
18h + *n 0Ch
VAT_Offset(VC 仲裁表偏移)
*10h
PAT_Offset(0)(端口仲裁表偏移(0))
*10h
PAT_Offset(n)(端口仲裁表偏移(n))
*10h
VC Resource Status Register (n)(VC 资源状态寄存器 (n))
RsvdP(保留,保留置位)
VC Resource Status Register (0)(VC 资源状态寄存器 (0))
RsvdP(保留,保留置位)
VC Arbitration Table(VC 仲裁表)
VC Resource Capability Register (0)(VC 资源能力寄存器 (0))
VC Resource Control Register (0)(VC 资源控制寄存器 (0))
VC Resource Control Register (n)(VC 资源控制寄存器 (n))
VC Resource Capability Register (n)(VC 资源能力寄存器 (n))
All Devices(所有设备)
Switch ports, Root Ports and RCRB(Switch 端口、Root Port 和 RCRB)
Port Arbitration Table (0)(端口仲裁表 (0))
Port Arbitration Table (n)(端口仲裁表 (n))
图 7-221 虚通道扩展能力结构

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The following sections describe the registers/fields of the Virtual Channel Extended Capability structure.

Refer to § Section 7.6.3 for a description of the PCI Express Extended Capability header. A Virtual Channel Extended Capability must use one of two Extended Capability IDs: 0002h or 0009h. Refer to § Section 7.9.1 for rules governing when each should be used. § Figure 7-222 details allocation of register fields in the Virtual Channel Extended Capability Header; § Table 7-201 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

以下各节描述虚通道扩展能力结构的寄存器/字段。

有关 PCI Express 扩展能力头的描述,请参见 § 7.6.3。虚通道扩展能力必须使用两个扩展能力 ID 之一:0002h 或 0009h。有关何时应使用何种 ID 的规则,请参见 § 7.9.1。§ 图 7-222 详述了虚通道扩展能力头中寄存器字段的分配;§ 表 7-201 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Figure 7-222. Virtual Channel Extended Capability Header | 图 7-222 虚通道扩展能力头**

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
15
PCI Express Extended Capability ID
0002h or 0009h
16
19
Capability Version
20
31
Next Capability Offset
Figure 7-222 Virtual Channel Extended Capability Header

</td>
<td style="background-color:#e8e8e8">

0
15
PCI Express Extended Capability ID(PCI Express 扩展能力 ID)
0002h 或 0009h
16
19
Capability Version(能力版本)
20
31
Next Capability Offset(下一能力偏移量)
图 7-222 虚通道扩展能力头

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

7.9.1.1 Virtual Channel Extended Capability Header (Offset 00h) §
§
§

<!-- 📄 Page 1265 -->
---

**Table 7-201. Virtual Channel Extended Capability Header | 表 7-201 虚通道扩展能力头**


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
15:0
PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability.
Extended Capability ID for the Virtual Channel Extended Capability is either 0002h or 0009h.
RO
19:16
Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present.
Must be 1h for this version of the specification.
RO
31:20
Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities.
For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh.
RO

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
15:0
PCI Express Extended Capability ID(PCI Express 扩展能力 ID) – 该字段是 PCI-SIG 定义的 ID 编号,用于指示扩展能力的性质和格式。
虚通道扩展能力的扩展能力 ID 为 0002h 或 0009h。
RO
19:16
Capability Version(能力版本) – 该字段是 PCI-SIG 定义的版本号,用于指示所呈现能力结构的版本。
对于本版本的规范,必须为 1h。
RO
31:20
Next Capability Offset(下一能力偏移量) – 该字段包含指向下一 PCI Express 能力结构的偏移量;若链接的能力列表中不存在其他项,则为 000h。
对于在配置空间中实现的扩展能力,该偏移量相对于 PCI 兼容配置空间的起始位置,因此必须始终为 000h(表示能力列表的终止)或大于 0FFh。
RO

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

7.9.1.2 Port VC Capability Register 1 (Offset 04h) §
§
§
§

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Port VC Capability Register 1 describes the configuration of the Virtual Channels associated with a PCI Express Port. § Figure 7-223 details allocation of register fields in the Port VC Capability Register 1; § Table 7-202 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

Port VC Capability Register 1 描述与 PCI Express Port 关联的虚通道的配置。§ 图 7-223 详述了 Port VC Capability Register 1 中寄存器字段的分配;§ 表 7-202 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1266 -->
---

**Figure 7-223. Port VC Capability Register 1 | 图 7-223 Port VC 能力寄存器 1**

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
2
Extended VC Count
3
RsvdP
4
6
Low Priority Extended VC Count
7
RsvdP
8
9
Reference Clock
10
11
Port Arbitration Table Entry Size
12
31
RsvdP
Figure 7-223 Port VC Capability Register 1

</td>
<td style="background-color:#e8e8e8">

0
2
Extended VC Count(扩展 VC 数量)
3
RsvdP(保留,保留置位)
4
6
Low Priority Extended VC Count(低优先级扩展 VC 数量)
7
RsvdP(保留,保留置位)
8
9
Reference Clock(参考时钟)
10
11
Port Arbitration Table Entry Size(端口仲裁表条目大小)
12
31
RsvdP(保留,保留置位)
图 7-223 Port VC 能力寄存器 1

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-202. Port VC Capability Register 1 | 表 7-202 Port VC 能力寄存器 1**


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
2:0
Extended VC Count - Indicates the number of (extended) Virtual Channels in addition to the default VC supported by the device. This field is valid for all Functions.
This value indicates the number of (extended) VC Resource Capability, Control, and Status registers that are present in Configuration Space in addition to the required VC Resource registers for the default VC.
The minimum value of this field is 0 (for devices that only support the default VC and only have 1 set of VC Resource Registers for that VC). The maximum value is 7.
RO
6:4
Low Priority Extended VC Count - Indicates the number of (extended) Virtual Channels in addition to the default VC belonging to the low-priority VC (LPVC) group that has the lowest priority with respect to other VC resources in a strict-priority VC Arbitration. This field is valid for all Functions.
The minimum value of this field is 000b and the maximum value is Extended VC Count.
RO

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
2:0
Extended VC Count(扩展 VC 数量) – 指示除设备支持的默认 VC 之外的(扩展)虚通道数量。该字段对所有 Function 有效。
该值指示在配置空间中,除默认 VC 所需的 VC 资源寄存器外,还存在多少(扩展)VC 资源能力、控制和状态寄存器。
该字段的最小值为 0(适用于仅支持默认 VC 且只有该 VC 一套 VC 资源寄存器的设备)。最大值为 7。
RO
6:4
Low Priority Extended VC Count(低优先级扩展 VC 数量) – 指示除默认 VC 外,属于低优先级 VC(LPVC)组的(扩展)虚通道数量,该组在严格优先级 VC 仲裁中相对于其他 VC 资源具有最低优先级。该字段对所有 Function 有效。
该字段的最小值为 000b,最大值为 Extended VC Count。
RO

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

00b
01b - 11b
00b
01b
10b
11b
Bit 0
Bit Location
Register Description
Attributes
9:8
Reference Clock - Indicates the reference clock for Virtual Channels that support time-based WRR Port Arbitration. This field is valid for RCRBs, Switch Ports, and Root Ports that support peer-to-peer traffic. It is not valid for Root Ports that do not support peer-to-peer traffic, Endpoints, and Switches or Root Complexes not implementing WRR, and must be hardwired to 00b.
Defined encodings are:
100 ns reference clock
Reserved
RO
11:10
Port Arbitration Table Entry Size - Indicates the size (in bits) of Port Arbitration table entry in the Function. This field is valid only for RCRBs, Switch Ports, and Root Ports that support peer-to-peer traffic. It is not valid and must be hardwired to 00b for Root Ports that do not support peer-to-peer traffic and Endpoints.
Defined encodings are:
The size of Port Arbitration table entry is 1 bit.
The size of Port Arbitration table entry is 2 bits.
The size of Port Arbitration table entry is 4 bits.
The size of Port Arbitration table entry is 8 bits.
RO

</td>
<td style="background-color:#e8e8e8">

00b
01b - 11b
00b
01b
10b
11b
Bit 0
位位置
寄存器描述
属性
9:8
Reference Clock(参考时钟) – 指示支持基于时间的 WRR 端口仲裁的虚通道所使用的参考时钟。该字段对支持点对点(peer-to-peer)流量的 RCRB、Switch 端口和 Root Port 有效。对于不支持点对点流量的 Root Port、Endpoint,以及未实现 WRR 的 Switch 或根复合体(RC),该字段无效,且必须硬连线为 00b。
已定义的编码为:
100 ns 参考时钟
保留
RO
11:10
Port Arbitration Table Entry Size(端口仲裁表条目大小) – 指示 Function 中端口仲裁表条目的大小(以位为单位)。该字段仅对支持点对点流量的 RCRB、Switch 端口和 Root Port 有效。对于不支持点对点流量的 Root Port 和 Endpoint,该字段无效且必须硬连线为 00b。
已定义的编码为:
端口仲裁表条目大小为 1 位。
端口仲裁表条目大小为 2 位。
端口仲裁表条目大小为 4 位。
端口仲裁表条目大小为 8 位。
RO

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Port VC Capability Register 2 provides further information about the configuration of the Virtual Channels associated with a PCI Express Port. § Figure 7-224 details allocation of register fields in the Port VC Capability Register 2; § Table 7-203 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

Port VC Capability Register 2 提供有关与 PCI Express Port 关联的虚通道配置的更多信息。§ 图 7-224 详述了 Port VC Capability Register 2 中寄存器字段的分配;§ 表 7-203 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Figure 7-224. Port VC Capability Register 2 | 图 7-224 Port VC 能力寄存器 2**

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
7
VC Arbitration Capability
8
23
RsvdP
24
31
VC Arbitration Table Offset
Figure 7-224 Port VC Capability Register 2

</td>
<td style="background-color:#e8e8e8">

0
7
VC Arbitration Capability(VC 仲裁能力)
8
23
RsvdP(保留,保留置位)
24
31
VC Arbitration Table Offset(VC 仲裁表偏移量)
图 7-224 Port VC 能力寄存器 2

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-203. Port VC Capability Register 2 | 表 7-203 Port VC 能力寄存器 2**


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
7:0
VC Arbitration Capability - Indicates the types of VC Arbitration supported by the Function for the LPVC group. This field is valid for all Functions that report a Low Priority Extended VC Count field greater than 0. For all other Functions, this field must be hardwired to 00h.
Each Bit Location within this field corresponds to a VC Arbitration Capability defined below. When more than 1 bit in this field is Set, it indicates that the Port can be configured to provide different VC arbitration services.
Defined bit positions are:
Hardware fixed arbitration scheme, e.g., Round Robin
RO

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
7:0
VC Arbitration Capability(VC 仲裁能力) – 指示 Function 为 LPVC 组所支持的 VC 仲裁类型。该字段对所有上报 Low Priority Extended VC Count 字段大于 0 的 Function 有效。对于所有其他 Function,该字段必须硬连线为 00h。
该字段中的每个位位置对应于下述一种 VC 仲裁能力。当该字段中有多于 1 个位被置位时,表示该 Port 可被配置为提供不同的 VC 仲裁服务。
已定义的位位置为:
硬件固定仲裁方案,例如轮询(Round Robin)
RO

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---


---

---
<!-- 📄 Page 1267 -->
---

<a id="sec-7-9-1-3"></a>
## 7.9.1.3 Port VC Capability Register 2 (Offset 08h) | 端口 VC 能力寄存器 2 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit 1
Bit 2
Bit 3
Bits 4-7
Bit Location
Register Description
Attributes
Weighted Round Robin (WRR) arbitration with 32 phases
WRR arbitration with 64 phases
WRR arbitration with 128 phases
Reserved
31:24
VC Arbitration Table Offset - Indicates the location of the VC Arbitration Table. This field is valid for all Functions.
This field contains the zero-based offset of the table in DQWORDS (16 bytes) from the base address of the Virtual Channel Extended Capability structure. A value of 0 indicates that the table is not present.
RO

§ Figure 7-225 details allocation of register fields in the Port VC Control Register; § Table 7-204 provides the respective bit definitions.

0
Load VC Arbitration Table
1
3
VC Arbitration Select
4
All VCs Enabled
5
15
RsvdP

Figure 7-225 Port VC Control Register

</td>
<td style="background-color:#e8e8e8">

位 1
位 2
位 3
位 4-7
位位置
寄存器描述
属性
加权轮询 (WRR) 仲裁,32 个相位
加权轮询 (WRR) 仲裁,64 个相位
加权轮询 (WRR) 仲裁,128 个相位
保留
31:24
VC 仲裁表偏移量 (VC Arbitration Table Offset) — 指示 VC 仲裁表的位置。该字段对所有 Function (功能) 有效。
该字段包含以 DQWORD (16 字节) 为单位的表相对于虚通道扩展能力结构 (Virtual Channel Extended Capability structure) 基址的零基偏移量。值为 0 表示该表不存在。
RO

§ 图 7-225 详细说明了 Port VC Control Register (端口 VC 控制寄存器) 中各寄存器字段的分配;§ 表 7-204 给出了相应的位定义。

0
Load VC Arbitration Table (加载 VC 仲裁表)
1
3
VC Arbitration Select (VC 仲裁选择)
4
All VCs Enabled (使能所有 VC)
5
15
RsvdP

图 7-225 Port VC Control Register (端口 VC 控制寄存器)

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-1-3-table"></a>

**Table 7-204 Port VC Control Register | 表 7-204 端口 VC 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Load VC Arbitration Table - Used by software to update the VC Arbitration Table. This bit is valid for all Functions when the selected VC Arbitration uses the VC Arbitration Table.<br>Software sets this bit to request hardware to apply new values programmed into VC Arbitration Table; clearing this bit has no effect. Software checks the VC Arbitration Table Status bit to confirm that new values stored in the VC Arbitration Table are latched by the VC arbitration logic.<br>This bit always returns 0b when read. | RW |
| 3:1 | VC Arbitration Select - Used by software to configure the VC arbitration by selecting one of the supported VC Arbitration schemes indicated by the VC Arbitration Capability field in the Port VC Capability Register 2. This field is valid for all Functions.<br>The permissible values of this field are numbers corresponding to one of the asserted bits in the VC Arbitration Capability field.<br>This field cannot be modified when more than one VC in the LPVC group is enabled. | RW |
| 4 | All VCs Enabled - Setting this bit indicates that all VCs that will be used by the Port have been enabled. Setting this bit allows hardware to allocate assigned buffer resources across the enabled VCs. | RW |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Load VC Arbitration Table (加载 VC 仲裁表) — 软件使用该位来更新 VC 仲裁表。当所选 VC 仲裁使用 VC Arbitration Table (VC 仲裁表) 时,该位对所有 Function 有效。<br>软件置位该位以请求硬件应用 VC 仲裁表中编程的新值;清除该位无效。软件通过检查 VC Arbitration Table Status 位来确认 VC 仲裁表中存储的新值是否已被 VC 仲裁逻辑锁存。<br>读该位时始终返回 0b。 | RW |
| 3:1 | VC Arbitration Select (VC 仲裁选择) — 软件通过选择 Port VC Capability Register 2 中 VC Arbitration Capability 字段所指示的支持的 VC 仲裁方案之一来配置 VC 仲裁。该字段对所有 Function 有效。<br>该字段的允许值是与 VC Arbitration Capability 字段中置位位之一相对应的数字。<br>当 LPVC 组中启用的 VC 多于一个时,该字段不可修改。 | RW |
| 4 | All VCs Enabled (使能所有 VC) — 置位该位表示将被端口使用的所有 VC 均已启用。置位该位允许硬件在已启用的 VC 之间分配已分配的缓冲区资源。 | RW |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-1-4"></a>
## 7.9.1.4 Port VC Control Register (Offset 0Ch) | 端口 VC 控制寄存器 (偏移量 0Ch)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
Setting this bit is optional. If this bit remains Clear and some VC Resources are never enabled, performance may be affected but the Link and all enabled VCs must operate correctly.
Behavior is undefined if this bit is Set and any VC Enable bit in this capability changes value.
Default value of this bit is 0b.
The Port VC Status Register provides status of the configuration of Virtual Channels associated with a Port. § Figure 7-226 details allocation of register fields in the Port VC Status Register; § Table 7-205 provides the respective bit definitions.

0
VC Arbitration Table Status
1
15
RsvdZ

Figure 7-226 Port VC Status Register

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
置位该位是可选的。如果该位保持清除状态且某些 VC 资源永远不被启用,则性能可能受到影响,但链路 (Link) 和所有已启用的 VC 必须正确运行。
如果该位置位且此能力中的任何 VC Enable 位改变了值,则行为未定义。
该位的默认值为 0b。
Port VC Status Register (端口 VC 状态寄存器) 提供与端口关联的虚通道 (Virtual Channels) 配置的状态。§ 图 7-226 详细说明了 Port VC Status Register 中各寄存器字段的分配;§ 表 7-205 给出了相应的位定义。

0
VC Arbitration Table Status (VC 仲裁表状态)
1
15
RsvdZ

图 7-226 Port VC Status Register (端口 VC 状态寄存器)

</td>
</tr>
</tbody>
</table>
</div>


<a id="sec-7-9-1-4-table"></a>

**Table 7-205 Port VC Status Register | 表 7-205 端口 VC 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | VC Arbitration Table Status - Indicates the coherency status of the VC Arbitration Table. This bit is valid for all Functions when the selected VC uses the VC Arbitration Table.<br>This bit is Set by hardware when any entry of the VC Arbitration Table is written by software. This bit is Cleared by hardware when hardware finishes loading values stored in the VC Arbitration Table after software sets the Load VC Arbitration Table bit in the Port VC Control Register.<br>Default value of this bit is 0b. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | VC Arbitration Table Status (VC 仲裁表状态) — 指示 VC Arbitration Table 的一致性状态。当所选 VC 使用 VC Arbitration Table 时,该位对所有 Function 有效。<br>当 VC 仲裁表的任何条目被软件写入时,该位由硬件置位。在软件置位 Port VC Control Register 中的 Load VC Arbitration Table 位之后,当硬件完成加载 VC 仲裁表中存储的值时,该位由硬件清除。<br>该位的默认值为 0b。 | RO |

The VC Resource Capability Register describes the capabilities and configuration of a particular Virtual Channel resource. § Figure 7-227 details allocation of register fields in the VC Resource Capability Register; § Table 7-206 provides the respective bit definitions.

VC Resource Capability Register (VC 资源能力寄存器) 描述特定虚通道资源的能力和配置。§ 图 7-227 详细说明了 VC Resource Capability Register 中各寄存器字段的分配;§ 表 7-206 给出了相应的位定义。

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1268 -->
---

---
<!-- 📄 Page 1269 -->
---

<a id="sec-7-9-1-5"></a>
## 7.9.1.5 Port VC Status Register (Offset 0Eh) | 端口 VC 状态寄存器 (偏移量 0Eh)

<a id="sec-7-9-1-6"></a>
## 7.9.1.6 VC Resource Capability Register | VC 资源能力寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit 0
Bit 1
Bit 2
Bit 3
Bit 4
Bit 5
Bits 6-7
0
7
Port Arbitration Capability
8
13
RsvdP
14
Undefined
15
Reject Snoop Transactions
16
22
Maximum Time Slots
23
RsvdP
24
31
Port Arbitration Table Offset

Figure 7-227 VC Resource Capability Register

</td>
<td style="background-color:#e8e8e8">

位 0
位 1
位 2
位 3
位 4
位 5
位 6-7
0
7
Port Arbitration Capability (端口仲裁能力)
8
13
RsvdP
14
Undefined (未定义)
15
Reject Snoop Transactions (拒绝探测事务)
16
22
Maximum Time Slots (最大时间槽数)
23
RsvdP
24
31
Port Arbitration Table Offset (端口仲裁表偏移量)

图 7-227 VC Resource Capability Register (VC 资源能力寄存器)

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-1-6-table"></a>

**Table 7-206 VC Resource Capability Register | 表 7-206 VC 资源能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Port Arbitration Capability - Indicates types of Port Arbitration supported by the VC resource. This field is valid for all Switch Ports, Root Ports that support peer-to-peer traffic, and RCRBs, but not for Endpoints or Root Ports that do not support peer-to-peer traffic.<br>Each Bit Location within this field corresponds to a Port Arbitration Capability defined below. When more than 1 bit in this field is Set, it indicates that the VC resource can be configured to provide different arbitration services.<br>Software selects among these capabilities by writing to the Port Arbitration Select field (see § Section 7.9.1.7 ).<br>Defined bit positions are:<br>Non-configurable hardware-fixed arbitration scheme, e.g., Round Robin (RR)<br>Weighted Round Robin (WRR) arbitration with 32 phases<br>WRR arbitration with 64 phases<br>WRR arbitration with 128 phases<br>Time-based WRR with 128 phases<br>WRR arbitration with 256 phases<br>Reserved | RO |
| 14 | Undefined Undefined - The value read from this bit is undefined. In previous versions of this specification, this bit was used to indicate Advanced Packet Switching. System software must ignore the value read from this bit. | RO |
| 15 | Reject Snoop Transactions - When Clear, transactions with or without the No Snoop bit Set within the TLP header are allowed on this VC. When Set, any transaction for which the No Snoop attribute is applicable but is not Set within the TLP header is permitted to be rejected as an Unsupported Request.<br>Refer to § Section 2.2.6.5 for information on where the No Snoop attribute is applicable. This bit is valid for Root Ports and RCRB; it is not valid for Endpoints or Switch Ports. | HwInit |
| 22:16 | Maximum Time Slots - Indicates the maximum number of time slots (minus one) that the VC resource is capable of supporting when it is configured for time-based WRR Port Arbitration. For example, a value 000 0000b in this field indicates the supported maximum number of time slots is 1 and a value of 111 1111b indicates the supported maximum number of time slots is 128. This field is valid for all Switch Ports, Root Ports that support peer-to-peer traffic, and RCRBs, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic. In addition, this field is valid only when the Port Arbitration Capability field indicates that the VC resource supports time-based WRR Port Arbitration. | HwInit |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | Port Arbitration Capability (端口仲裁能力) — 指示 VC 资源支持的端口仲裁类型。该字段对所有 Switch Port (交换机端口)、支持点对点 (peer-to-peer) 流量的 Root Port (根端口) 和 RCRB 有效,但对不支持点对点流量的 Endpoint (端点) 或 Root Port 无效。<br>该字段中的每个位位置对应下述定义的端口仲裁能力。当该字段中有多于 1 个位置位时,表示 VC 资源可被配置以提供不同的仲裁服务。<br>软件通过对 Port Arbitration Select 字段写入来选择这些能力 (参见 § Section 7.9.1.7)。<br>已定义的位位置如下:<br>不可配置的硬件固定仲裁方案,例如轮询 (Round Robin, RR)<br>加权轮询 (WRR) 仲裁,32 个相位<br>加权轮询 (WRR) 仲裁,64 个相位<br>加权轮询 (WRR) 仲裁,128 个相位<br>基于时间的 WRR,128 个相位<br>加权轮询 (WRR) 仲裁,256 个相位<br>保留 | RO |
| 14 | Undefined (未定义) — 从该位读取的值未定义。在本规范的早期版本中,该位用于指示 Advanced Packet Switching (高级分组交换)。系统软件必须忽略从该位读取的值。 | RO |
| 15 | Reject Snoop Transactions (拒绝探测事务) — 当清除时,在 TLP (事务层包) Header 中设置了或未设置 No Snoop 位的事务都允许在该 VC 上传输。当置位时,对于任何 No Snoop 属性适用但 TLP Header 中未设置该属性的事务,允许作为 Unsupported Request (不支持的请求) 拒绝。<br>有关 No Snoop 属性适用位置的信息,请参阅 § Section 2.2.6.5。该位对 Root Port 和 RCRB 有效;对 Endpoint 或 Switch Port 无效。 | HwInit |
| 22:16 | Maximum Time Slots (最大时间槽数) — 指示当 VC 资源被配置用于基于时间的 WRR 端口仲裁时,所支持的最大时间槽数 (减一)。例如,该字段中值为 000 0000b 表示支持的最大时间槽数为 1,值为 111 1111b 表示支持的最大时间槽数为 128。该字段对所有 Switch Port、支持点对点流量的 Root Port 和 RCRB 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。此外,仅当 Port Arbitration Capability 字段指示 VC 资源支持基于时间的 WRR 端口仲裁时,该字段才有效。 | HwInit |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1270 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
31:24
Port Arbitration Table Offset - Indicates the location of the Port Arbitration Table associated with the VC resource. This field is valid for all Switch Ports, Root Ports that support peer-to-peer traffic, and RCRBs, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic.
This field contains the zero-based offset of the table in DQWORDS (16 bytes) from the base address of the Virtual Channel Extended Capability structure. A value of 00h indicates that the table is not present.
RO

§ Figure 7-228 details allocation of register fields in the VC Resource Control Register; § Table 7-207 provides the respective bit definitions.

0
7
TC/VC Map
8
15
RsvdP
16
Load Port Arbitration Table
17
19
Port Arbitration Select
20
23
RsvdP
24
26
VC ID
27
29
Shared Flow Control Usage Limit
30
Shared Flow Control Usage Limit Enable
31
VC Enable

Figure 7-228 VC Resource Control Register

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
31:24
Port Arbitration Table Offset (端口仲裁表偏移量) — 指示与 VC 资源关联的 Port Arbitration Table (端口仲裁表) 的位置。该字段对所有 Switch Port、支持点对点流量的 Root Port 和 RCRB 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。
该字段包含以 DQWORD (16 字节) 为单位的表相对于 Virtual Channel Extended Capability structure 基址的零基偏移量。值为 00h 表示该表不存在。
RO

§ 图 7-228 详细说明了 VC Resource Control Register 中各寄存器字段的分配;§ 表 7-207 给出了相应的位定义。

0
7
TC/VC Map (TC/VC 映射)
8
15
RsvdP
16
Load Port Arbitration Table (加载端口仲裁表)
17
19
Port Arbitration Select (端口仲裁选择)
20
23
RsvdP
24
26
VC ID (VC 标识)
27
29
Shared Flow Control Usage Limit (共享流控使用限制)
30
Shared Flow Control Usage Limit Enable (共享流控使用限制使能)
31
VC Enable (VC 使能)

图 7-228 VC Resource Control Register (VC 资源控制寄存器)

</td>
</tr>
</tbody>
</table>
</div>


<a id="sec-7-9-1-7"></a>
## 7.9.1.7 VC Resource Control Register | VC 资源控制寄存器

<a id="sec-7-9-1-7-table"></a>

**Table 7-207 VC Resource Control Register | 表 7-207 VC 资源控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | TC/VC Map - This field indicates the TCs that are mapped to the VC resource. This field is valid for all Functions.<br>Bit locations within this field correspond to TC values. For example, when bit 7 is Set in this field, TC7 is mapped to this VC resource. When more than 1 bit in this field is Set, it indicates that multiple TCs are mapped to the VC resource.<br>In order to remove one or more TCs from the TC/VC Map of an enabled VC, software must ensure that no new or outstanding transactions with the TC labels are targeted at the given Link.<br>Default value of this field is FFh for the first VC resource and is 00h for other VC resources.<br>Note:<br>Bit 0 of this field is read-only. It must be Set for the default VC0 and Clear for all other enabled VCs. | RW (see the note for exceptions) |
| 16 | Load Port Arbitration Table - When Set, this bit updates the Port Arbitration logic from the Port Arbitration Table for the VC resource. This bit is valid for all Switch Ports, Root Ports that support peer-to-peer traffic, and RCRBs, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic. In addition, this bit is only valid when the Port Arbitration Table is used by the selected Port Arbitration scheme (that is indicated by a Set bit in the Port Arbitration Capability field selected by Port Arbitration Select).<br>Software sets this bit to signal hardware to update Port Arbitration logic with new values stored in Port Arbitration Table; clearing this bit has no effect. Software uses the Port Arbitration Table Status bit to confirm whether the new values of Port Arbitration Table are completely latched by the arbitration logic.<br>This bit always returns 0b when read.<br>Default value of this bit is 0b. | RW |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | TC/VC Map (TC/VC 映射) — 该字段指示映射到该 VC 资源的 TC (流量类, Traffic Class)。该字段对所有 Function 有效。<br>该字段内的位位置对应 TC 值。例如,当该字段中位 7 置位时,TC7 被映射到该 VC 资源。当该字段中有多个位置位时,表示有多个 TC 被映射到该 VC 资源。<br>为了从已启用 VC 的 TC/VC 映射中移除一个或多个 TC,软件必须确保没有新的或未完成的使用这些 TC 标签的事务被定向到给定的 Link。<br>该字段的默认值为第一个 VC 资源的 FFh,以及其他 VC 资源的 00h。<br>注意:<br>该字段的位 0 是只读的。对于默认 VC0 必须置位,对于所有其他已启用 VC 必须清除。 | RW (参见注释中的例外) |
| 16 | Load Port Arbitration Table (加载端口仲裁表) — 当置位时,该位从 VC 资源的 Port Arbitration Table 更新端口仲裁逻辑。该位对所有 Switch Port、支持点对点流量的 Root Port 和 RCRB 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。此外,该位仅当所选端口仲裁方案使用端口仲裁表时 (即 Port Arbitration Select 所选 Port Arbitration Capability 字段中的位置位) 才有效。<br>软件置位该位以通知硬件使用 Port Arbitration Table 中存储的新值更新端口仲裁逻辑;清除该位无效。软件通过 Port Arbitration Table Status 位来确认 Port Arbitration Table 的新值是否已被仲裁逻辑完全锁存。<br>读该位时始终返回 0b。<br>该位的默认值为 0b。 | RW |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1271 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

000b
001b
010b
011b
100b
101b
110b
111b
Bit Location
Register Description
Attributes
19:17
Port Arbitration Select - This field configures the VC resource to provide a particular Port Arbitration service. This field is valid for RCRBs, Root Ports that support peer-to-peer traffic, and Switch Ports, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic.
The permissible value of this field is a number corresponding to one of the asserted bits in the Port Arbitration Capability field of the VC resource.
RW
26:24
VC ID - This field assigns a VC ID to the VC resource (see note for exceptions). This field is valid for all Functions.
This field cannot be modified when the VC is already enabled.
Note:
For the first VC resource (default VC), this field is read-only and must be hardwired to 000b.
RW
29:27
Shared Flow Control Usage Limit - this field controls what percentage of the available Shared Flow Control a given FC/VC is permitted to consume.
This limit is applied independently for each Flow Control credit type. For example, if this field contains 101b and Shared Flow Control Usage Limit Enable is Set, a Posted TLP may not pass the Tx Gate if doing so would cause that VC to consume more than 62.5% of the available Shared Posted Header credits or if doing so would cause that VC to consume more than 62.5% of the available Shared Data credits.
If Shared Flow Control Usage Limit Enable is Clear, this field is ignored and this VC is permitted to consume all of the shared credits.
When Shared Flow Control Usage Limit Enable is Set, and this field contains 000b, this VC is not permitted to consume any shared credits.
Behavior is undefined when all VCs have Shared Flow Control Usage Limit Enable Set and the sum of the Shared Flow Control Limit values for all VCs is less than 100%.
Encodings are:
0%
12.5%
25%
37.5%
50%
62.5%
75%
87.5%
Behavior is undefined if this field changes value while VC Enable and Shared Flow Control Usage Limit Enable are both Set.
This field is RsvdP when Flit Mode Supported is Clear.
When Extended VC Count is 0, this field is permitted to be hardwired to any value.
When this field is RW, the default value is implementation specific.
RW / RO / RsvdP
30
Shared Flow Control Usage Limit Enable - When Set, this bit enables use of the Shared Flow Control Usage Limit value above at the transmitter for this Virtual Channel.
Behavior is undefined of the value of this bit changes while VC Enable is Set.
This bit is RsvdP when Flit Mode Supported is Clear.
RW / RO / RsvdP

</td>
<td style="background-color:#e8e8e8">

000b
001b
010b
011b
100b
101b
110b
111b
位位置
寄存器描述
属性
19:17
Port Arbitration Select (端口仲裁选择) — 该字段配置 VC 资源以提供特定的端口仲裁服务。该字段对 RCRB、支持点对点流量的 Root Port 和 Switch Port 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。
该字段的允许值是与 VC 资源的 Port Arbitration Capability 字段中置位位之一相对应的数字。
RW
26:24
VC ID (VC 标识) — 该字段为 VC 资源分配一个 VC ID (参见例外情况的注释)。该字段对所有 Function 有效。
当 VC 已启用时,不能修改该字段。
注意:
对于第一个 VC 资源 (默认 VC),该字段是只读的,且必须硬连线为 000b。
RW
29:27
Shared Flow Control Usage Limit (共享流控使用限制) — 该字段控制给定的 FC/VC 可使用可用共享流控 (Shared Flow Control) 的百分比。
该限制针对每种流控信用 (Flow Control credit) 类型独立应用。例如,如果该字段值为 101b 且 Shared Flow Control Usage Limit Enable 置位,则当 Posted TLP 通过 Tx Gate 将导致该 VC 消耗超过 62.5% 的可用 Shared Posted Header 信用,或导致该 VC 消耗超过 62.5% 的可用 Shared Data 信用时,该 Posted TLP 可能无法通过 Tx Gate。
如果 Shared Flow Control Usage Limit Enable 被清除,则忽略该字段,且允许该 VC 消耗所有共享信用。
当 Shared Flow Control Usage Limit Enable 置位且该字段值为 000b 时,不允许该 VC 消耗任何共享信用。
当所有 VC 的 Shared Flow Control Usage Limit Enable 都已置位,且所有 VC 的 Shared Flow Control Limit 值之和小于 100% 时,行为未定义。
编码如下:
0%
12.5%
25%
37.5%
50%
62.5%
75%
87.5%
当 VC Enable 和 Shared Flow Control Usage Limit Enable 都已置位时,如果该字段改变值,则行为未定义。
当 Flit Mode Supported 清除时,该字段为 RsvdP。
当 Extended VC Count 为 0 时,该字段允许被硬连线为任意值。
当该字段为 RW 时,默认值由实现决定。
RW / RO / RsvdP
30
Shared Flow Control Usage Limit Enable (共享流控使用限制使能) — 当置位时,该位使能在该虚通道的发送端使用上述 Shared Flow Control Usage Limit 值。
当 VC Enable 已置位时,如果该位的值发生变化,则行为未定义。
当 Flit Mode Supported 清除时,该位为 RsvdP。
RW / RO / RsvdP

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1272 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
When Extended VC Count is 0, this bit is permitted to be hardwired to 0b.
When this bit is RW, the default value is implementation specific.
31
VC Enable - This bit, when Set, enables a Virtual Channel. The Virtual Channel is disabled when this bit is cleared. This bit is valid for all Functions.
Software must use the VC Negotiation Pending bit to check whether the VC negotiation is complete.
For VC0, the attribute is RO. If no SVC capability is implemented in this Port, this bit's value must be 1b; otherwise, this bit's value must always be the same value as the Use VC/MFVC bit in the SVC Port Status Register. See § Section 6.3.5 .
For other VCs, if no SVC capability is implemented in this Port or if the Use VC/MFVC bit is Set, the default value of this bit is 0b and the attribute is RW; otherwise, this bit must be RO with a value of 0b.
To enable a Virtual Channel in a Port using VC mechanisms, the VC Enable bit for that Virtual Channel must be Set. The corresponding Virtual Channel in the Link partner Port must be enabled as well, and that Virtual Channel may be in SVC, VC, or MFVC capabilities. To disable a Virtual Channel, Virtual Channel must be disabled in both components on the Link. Software must ensure that no traffic is using a Virtual Channel at the time it is disabled. Software must fully disable a Virtual Channel in both components on a Link before re-enabling the Virtual Channel.
When this bit is forced to be RO with a value of 0b due to the Use VC/MFVC bit being Clear, its associated VC is disabled, rendering most of its control registers to be ineffective.
RW/HwInit

§ Figure 7-229 details allocation of register fields in the VC Resource Status Register; § Table 7-208 provides the respective bit definitions.

0
Port Arbitration Table Status
1
VC Negotiation Pending
2
15
RsvdZ

Figure 7-229 VC Resource Status Register

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
当 Extended VC Count 为 0 时,该位允许被硬连线为 0b。
当该位为 RW 时,默认值由实现决定。
31
VC Enable (VC 使能) — 当置位时,该位启用一个虚通道。当该位清除时,该虚通道被禁用。该位对所有 Function 有效。
软件必须使用 VC Negotiation Pending 位检查 VC 协商是否完成。
对于 VC0,属性为 RO。如果该端口未实现 SVC 能力,则该位的值必须为 1b;否则,该位的值必须始终与 SVC Port Status Register 中 Use VC/MFVC 位的值相同。参见 § Section 6.3.5。
对于其他 VC,如果该端口未实现 SVC 能力,或者 Use VC/MFVC 位置位,则该位的默认值为 0b,属性为 RW;否则,该位必须为 RO,且值为 0b。
要使用 VC 机制在端口中启用虚通道,必须置位该虚通道的 VC Enable 位。链路对端端口中的对应虚通道也必须被启用,且该虚通道可以位于 SVC、VC 或 MFVC 能力中。要禁用虚通道,必须在链路上两个组件中同时禁用该虚通道。软件必须确保在禁用虚通道时,没有流量正在使用该虚通道。软件必须在链路上两个组件中完全禁用虚通道后,才能重新启用该虚通道。
当该位因 Use VC/MFVC 位清除而被强制为 RO 且值为 0b 时,其关联的 VC 被禁用,导致其大部分控制寄存器失效。
RW/HwInit

§ 图 7-229 详细说明了 VC Resource Status Register 中各寄存器字段的分配;§ 表 7-208 给出了相应的位定义。

0
Port Arbitration Table Status (端口仲裁表状态)
1
VC Negotiation Pending (VC 协商挂起)
2
15
RsvdZ

图 7-229 VC Resource Status Register (VC 资源状态寄存器)

</td>
</tr>
</tbody>
</table>
</div>


<a id="sec-7-9-1-8"></a>
## 7.9.1.8 VC Resource Status Register | VC 资源状态寄存器

<a id="sec-7-9-1-8-table"></a>

**Table 7-208 VC Resource Status Register | 表 7-208 VC 资源状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Port Arbitration Table Status - This bit indicates the coherency status of the Port Arbitration Table associated with the VC resource. This bit is valid for RCRBs, Root Ports that support peer-to-peer traffic, and Switch Ports, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic. In addition, this bit is valid only when the Port Arbitration Table is used by the selected Port Arbitration for the VC resource.<br>This bit is Set by hardware when any entry of the Port Arbitration Table is written to by software. This bit is Cleared by hardware when hardware finishes loading values stored in the Port Arbitration Table after software sets the Load Port Arbitration Table bit.<br>Default value of this bit is 0b. | RO |
| 1 | VC Negotiation Pending - This bit indicates whether the Virtual Channel negotiation (initialization or disabling) is in pending state. This bit is valid for all Functions.<br>The value of this bit is defined only when the Link is in the DL_Active state and the Virtual Channel is enabled (its VC Enable bit is Set).<br>When this bit is Set by hardware, it indicates that the VC resource has not completed the process of negotiation. This bit is Cleared by hardware after the VC negotiation is complete (on exit from the FC_INIT2 state). For VC0, this bit is permitted to be hardwired to 0b.<br>Before using a Virtual Channel, software must check whether the VC Negotiation Pending bits for that Virtual Channel are Clear in both components on the Link. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Port Arbitration Table Status (端口仲裁表状态) — 该位指示与 VC 资源关联的端口仲裁表的一致性状态。该位对 RCRB、支持点对点流量的 Root Port 和 Switch Port 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。此外,该位仅当所选端口仲裁为该 VC 资源使用端口仲裁表时才有效。<br>当端口仲裁表的任何条目被软件写入时,该位由硬件置位。在软件置位 Load Port Arbitration Table 位之后,当硬件完成加载端口仲裁表中存储的值时,该位由硬件清除。<br>该位的默认值为 0b。 | RO |
| 1 | VC Negotiation Pending (VC 协商挂起) — 该位指示虚通道协商 (初始化或禁用) 是否处于挂起状态。该位对所有 Function 有效。<br>该位的值仅在 Link 处于 DL_Active 状态且虚通道已启用 (其 VC Enable 位置位) 时才有定义。<br>当该位由硬件置位时,表示 VC 资源尚未完成协商过程。该位在 VC 协商完成后 (从 FC_INIT2 状态退出时) 由硬件清除。对于 VC0,允许将该位硬连线为 0b。<br>在使用虚通道之前,软件必须检查链路上两个组件中该虚通道的 VC Negotiation Pending 位是否都已清除。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1273 -->
---

The VC Arbitration Table is a read-write register array that is used to store the arbitration table for VC Arbitration. This register array is valid for all Functions when the selected VC Arbitration uses a WRR table. Functions that do not support WRR VC arbitration are not required to implement a VC Arbitration Table. If it exists, the VC Arbitration Table is located by the VC Arbitration Table Offset field.

The VC Arbitration Table is a register array with fixed-size entries of 4 bits. § Figure 7-230 depicts the table structure of an example VC Arbitration Table with 32 phases. Each 4-bit table entry corresponds to a phase within a WRR arbitration period. The definition of table entry is depicted in § Table 7-209. The lower 3 bits (bits 0-2) contain the VC ID value, indicating that the corresponding phase within the WRR arbitration period is assigned to the Virtual Channel indicated by the VC ID (must be a valid VC ID that corresponds to an enabled VC).

The highest bit (bit 3) of the table entry is Reserved. The length of the table depends on the selected VC Arbitration as shown in § Table 7-210.

When the VC Arbitration Table is used by the default VC Arbitration method, the default values of the table entries must be all zero to ensure forward progress for the default VC (with VC ID of 0).

VC Arbitration Table (VC 仲裁表) 是一个读/写寄存器数组,用于存储 VC 仲裁的仲裁表。当所选 VC 仲裁使用 WRR 表时,该寄存器数组对所有 Function 有效。不支持 WRR VC 仲裁的 Function 不需要实现 VC Arbitration Table。如果存在,VC Arbitration Table 由 VC Arbitration Table Offset 字段定位。

VC Arbitration Table 是一个固定大小为 4 位条目的寄存器数组。§ 图 7-230 展示了包含 32 个相位的 VC Arbitration Table 的示例表结构。每个 4 位表条目对应 WRR 仲裁周期内的一个相位。表条目的定义如图 § 表 7-209 所示。低 3 位 (位 0-2) 包含 VC ID 值,指示 WRR 仲裁周期内的对应相位被分配给 VC ID 所指示的虚通道 (必须是与已启用 VC 对应的有效 VC ID)。

表条目的最高位 (位 3) 为保留位。表的长度取决于所选的 VC 仲裁,如 § 表 7-210 所示。

当默认 VC 仲裁方法使用 VC Arbitration Table 时,表条目的默认值必须全为 0,以确保默认 VC (VC ID 为 0) 的前向推进。

> **Figure 7-230.** Example VC Arbitration Table with 32 Phases
> <img src="figures/chapter_07/fig_1273_1_tight.png" width="700">

<a id="sec-7-9-1-9-table"></a>

**Table 7-209 Definition of the 4-bit Entries in the VC Arbitration Table | 表 7-209 VC 仲裁表中 4 位条目的定义**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 2:0 | VC ID | RW |
| 3 | RsvdP | RW |

| 位位置 | 描述 | 属性 |
|--------|------|------|
| 2:0 | VC ID (VC 标识) | RW |
| 3 | RsvdP | RW |

<a id="sec-7-9-1-9"></a>
## 7.9.1.9 VC Arbitration Table | VC 仲裁表

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1274 -->
---

**Table 7-210 Length of the VC Arbitration Table | 表 7-210 VC 仲裁表的长度**

| VC Arbitration Select | VC Arbitration Table Length |
|-----------------------|-----------------------------|
| 001b | 32 entries |
| 010b | 64 entries |
| 011b | 128 entries |

| VC Arbitration Select | VC Arbitration Table Length |
|-----------------------|-----------------------------|
| 001b | 32 个条目 |
| 010b | 64 个条目 |
| 011b | 128 个条目 |

The Port Arbitration Table register is a read-write register array that is used to store the WRR or time-based WRR arbitration table for Port Arbitration for the VC resource. This register array is valid for all Switch Ports, Root Ports that support peer-to-peer traffic, and RCRBs, but is not valid for Endpoints or Root Ports that do not support peer-to-peer traffic. It is only present when one or more asserted bits in the Port Arbitration Capability field indicate that the component supports a Port Arbitration scheme that uses a programmable arbitration table. Furthermore, it is only valid when one of the above-mentioned bits in the Port Arbitration Capability field is selected by the Port Arbitration Select field.

The Port Arbitration Table represents one Port arbitration period. § Figure 7-231 shows the structure of an example Port Arbitration Table with 128 phases and 2-bit table entries. Each table entry containing a Port Number corresponds to a phase within a Port arbitration period. For example, a table with 2-bit entries can be used by a Switch component with up to four Ports. A Port Number written to a table entry indicates that the phase within the Port Arbitration period is assigned to the selected PCI Express Port (the Port Number must be a valid one).

Port Arbitration Table (端口仲裁表) 寄存器是一个读/写寄存器数组,用于为 VC 资源存储 WRR 或基于时间的 WRR 端口仲裁表。该寄存器数组对所有 Switch Port、支持点对点流量的 Root Port 和 RCRB 有效,但对不支持点对点流量的 Endpoint 或 Root Port 无效。它仅在 Port Arbitration Capability 字段中有一个或多个置位位指示组件支持使用可编程仲裁表的端口仲裁方案时才存在。此外,它仅在上述 Port Arbitration Capability 字段中的某一位由 Port Arbitration Select 字段选中时才有效。

Port Arbitration Table 表示一个端口仲裁周期。§ 图 7-231 展示了包含 128 个相位和 2 位表条目的 Port Arbitration Table 示例结构。包含端口号的每个表条目对应端口仲裁周期内的一个相位。例如,具有 2 位条目的表可用于具有多达四个端口的 Switch 组件。写入表条目的端口号表示端口仲裁周期内的该相位被分配给所选 PCI Express 端口 (端口号必须是有效的)。

- When the WRR Port Arbitration is used for a VC of any Egress Port, at each arbitration phase, the Port Arbiter serves one transaction from the Ingress Port indicated by the Port Number of the current phase. When finished, it immediately advances to the next phase. A phase is skipped, i.e., the Port Arbiter simply moves to the next phase immediately if the Ingress Port indicated by the phase does not contain any transaction for the VC (note that a phase cannot contain the Egress Port's Port Number).

- When the Time-based WRR Port Arbitration is used for a VC of any given Port, at each arbitration phase aligning to a virtual timeslot, the Port Arbiter serves one transaction from the Ingress Port indicated by the Port Number of the current phase. It advances to the next phase at the next virtual timeslot. A phase indicates an "idle" timeslot, i.e., the Port Arbiter does not serve any transaction during the phase, if:
  - the phase contains the Egress Port's Port Number, or
  - the Ingress Port indicated by the phase does not contain any transaction for the VC.

- The Port Arbitration Table Entry Size field in the Port VC Capability Register 1 determines the table entry size. The length of the table is determined by the Port Arbitration Select field as shown in § Table 7-211.

- When the Port Arbitration Table is used by the default Port Arbitration for the default VC, the default values for the table entries must contain at least one entry for each of the other PCI Express Ports of the component to ensure forward progress for the default VC for each Port. The table may contain RR or RR-like fair Port Arbitration for the default VC.

- 当对任何 Egress Port (出口端口) 的 VC 使用 WRR 端口仲裁时,在每个仲裁相位,端口仲裁器从当前相位端口号指示的 Ingress Port (入口端口) 提供一个事务。完成后,它立即推进到下一个相位。如果相位指示的 Ingress Port 不包含该 VC 的任何事务,则该相位被跳过 (即端口仲裁器立即移动到下一相位) (注意,相位不能包含 Egress Port 的端口号)。

- 当对任何给定端口的 VC 使用基于时间的 WRR 端口仲裁时,在每个与虚拟时隙对齐的仲裁相位,端口仲裁器从当前相位端口号指示的 Ingress Port 提供一个事务。它在下一个虚拟时隙推进到下一相位。在以下情况下,相位指示一个 "idle" (空闲) 时隙,即端口仲裁器在该相位期间不提供任何事务:
  - 该相位包含 Egress Port 的端口号,或
  - 该相位指示的 Ingress Port 不包含该 VC 的任何事务。

- Port VC Capability Register 1 中的 Port Arbitration Table Entry Size 字段决定表条目大小。表的长度由 Port Arbitration Select 字段决定,如 § 表 7-211 所示。

- 当默认 VC 的默认端口仲裁使用 Port Arbitration Table 时,表条目的默认值必须为组件中每个其他 PCI Express Port 至少包含一个条目,以确保每个端口默认 VC 的前向推进。该表可以包含默认 VC 的 RR 或类 RR 公平端口仲裁。

<a id="sec-7-9-1-10"></a>
## 7.9.1.10 Port Arbitration Table | 端口仲裁表

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1275 -->
---

> **Figure 7-231.** Example Port Arbitration Table with 128 Phases and 2-bit Table Entries
> <img src="figures/chapter_07/fig_1275_1_tight.png" width="700">

<a id="sec-7-9-1-10-table"></a>

**Table 7-211 Length of Port Arbitration Table | 表 7-211 端口仲裁表的长度**

| Port Arbitration Select | Port Arbitration Table Length |
|-------------------------|-------------------------------|
| 001b | 32 entries |
| 010b | 64 entries |
| 011b | 128 entries |
| 100b | 128 entries |
| 101b | 256 entries |

| Port Arbitration Select | Port Arbitration Table Length |
|-------------------------|-------------------------------|
| 001b | 32 个条目 |
| 010b | 64 个条目 |
| 011b | 128 个条目 |
| 100b | 128 个条目 |
| 101b | 256 个条目 |

The Multi-Function Virtual Channel Extended Capability (MFVC Capability) is an optional Extended Capability that permits enhanced QoS management in a Multi-Function Device, including TC/VC mapping, optional VC arbitration, and optional Function arbitration for Upstream Requests. When implemented, the MFVC Extended Capability structure must be present in the Extended Configuration Space of Function 0 of the Multi-Function Device's Upstream Port. § Figure 7-232 provides a high level view of the MFVC Extended Capability structure. This MFVC Extended Capability structure controls Virtual Channel assignment at the PCI Express Upstream Port of the Multi-Function Device, while a VC Extended Capability structure, if present in a Function, controls the Virtual Channel assignment for that individual Function.

The number of (extended) Virtual Channels is indicated by the MFVC Extended VC Count field in the Port VC Capability Register 1. Software must interpret this field to determine the availability of extended MFVC VC Resource registers.

A Multi-Function Device is permitted to have an MFVC Extended Capability structure even if none of its Functions have a VC Extended Capability structure. However, an MFVC Extended Capability structure is permitted only in Function 0 in the Upstream Port of a Multi-Function Device.

Multi-Function Virtual Channel Extended Capability (多功能虚通道扩展能力, MFVC Capability) 是一种可选的扩展能力,允许在多功能设备 (Multi-Function Device) 中进行增强的 QoS 管理,包括 TC/VC 映射、可选的 VC 仲裁以及用于上游请求的可选功能仲裁。实现时,MFVC Extended Capability structure 必须出现在多功能设备上游端口 (Upstream Port) Function 0 的扩展配置空间中。§ 图 7-232 提供了 MFVC Extended Capability structure 的高级视图。该 MFVC Extended Capability structure 控制多功能设备 PCI Express 上游端口的虚通道分配,而 VC Extended Capability structure (如果存在于 Function 中) 控制该单独 Function 的虚通道分配。

(扩展) 虚通道的数量由 Port VC Capability Register 1 中的 MFVC Extended VC Count 字段指示。软件必须解释该字段以确定扩展 MFVC VC Resource 寄存器的可用性。

多功能设备允许具有 MFVC Extended Capability structure,即使其任何 Function 都没有 VC Extended Capability structure。但是,MFVC Extended Capability structure 仅允许存在于上游端口的 Function 0 中。

<a id="sec-7-9-2"></a>
## 7.9.2 Multi-Function Virtual Channel Extended Capability | 多功能虚通道扩展能力

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1276 -->
---

> **Figure 7-232.** MFVC Capability Structure
> <img src="figures/chapter_07/fig_1276_1_tight.png" width="700">

The following sections describe the registers/fields of the MFVC Extended Capability structure.

Refer to § Section 7.6.3 for a description of the PCI Express Extended Capability header. The Extended Capability ID for the MFVC Extended Capability is 0008h. § Figure 7-233 details allocation of register fields in the MFVC Extended Capability header; § Table 7-212 provides the respective bit definitions.

以下各节描述了 MFVC Extended Capability structure 的寄存器/字段。

有关 PCI Express Extended Capability Header 的说明,请参阅 § Section 7.6.3。MFVC Extended Capability 的 Extended Capability ID 为 0008h。§ 图 7-233 详细说明了 MFVC Extended Capability Header 中各寄存器字段的分配;§ 表 7-212 给出了相应的位定义。

> **Figure 7-233.** MFVC Extended Capability Header
> <img src="figures/chapter_07/fig_1276_2_tight.png" width="700">

<a id="sec-7-9-2-table"></a>

**Table 7-212 MFVC Extended Capability Header | 表 7-212 MFVC 扩展能力头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability.<br>The Extended Capability ID for the MFVC Extended Capability is 0008h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present.<br>Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities.<br>For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 15:0 | PCI Express Extended Capability ID (PCI Express 扩展能力 ID) — 该字段是 PCI-SIG 定义的 ID 号,用于指示扩展能力的性质和格式。<br>MFVC Extended Capability 的 Extended Capability ID 为 0008h。 | RO |
| 19:16 | Capability Version (能力版本) — 该字段是 PCI-SIG 定义的版本号,用于指示所表示能力结构的版本。<br>对于本版本的规范,必须为 1h。 | RO |
| 31:20 | Next Capability Offset (下一能力偏移量) — 该字段包含到下一个 PCI Express Capability structure 的偏移量;如果链表中不存在其他项,则为 000h。<br>对于在配置空间中实现的扩展能力,该偏移量相对于 PCI 兼容配置空间 (PCI-compatible Configuration Space) 的起始处,因此必须始终为 000h (用于终止能力列表) 或大于 0FFh。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

---

<a id="sec-7-9-2-1"></a>
## 7.9.2.1 MFVC Extended Capability Header (Offset 00h) | MFVC 扩展能力头 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MFVC Port VC Capability Register 1 describes the configuration of the Virtual Channels associated with a PCI Express Port of the Multi-Function Device. Figure 7-234 details allocation of register fields in the MFVC Port VC Capability Register 1; Table 7-213 provides the respective bit definitions.

```
 0
 2
 Extended VC Count
 3
 RsvdP
 4
 6
 Low Priority Extended VC Count
 7
 RsvdP
 8
 9
 Reference Clock
 10
 11
 Function Arbitration Table Entry Size
 12
 31
 RsvdP
```

Figure 7-234 MFVC Port VC Capability Register 1

</td>
<td style="background-color:#e8e8e8">

MFVC Port VC Capability Register 1 (MFVC 端口 VC 能力寄存器 1) 描述与多功能设备 (Multi-Function Device) 的 PCI Express 端口相关联的虚通道 (Virtual Channels) 的配置。图 7-234 详细说明了 MFVC Port VC Capability Register 1 中各寄存器字段的分配;表 7-213 给出了相应的位定义。

```
 0
 2
 Extended VC Count (扩展 VC 计数)
 3
 RsvdP
 4
 6
 Low Priority Extended VC Count (低优先级扩展 VC 计数)
 7
 RsvdP
 8
 9
 Reference Clock (参考时钟)
 10
 11
 Function Arbitration Table Entry Size (Function 仲裁表条目大小)
 12
 31
 RsvdP
```

图 7-234 MFVC Port VC Capability Register 1 (MFVC 端口 VC 能力寄存器 1)

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-2-1-table"></a>

**Table 7-213 MFVC Port VC Capability Register 1 | 表 7-213 MFVC 端口 VC 能力寄存器 1**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2:0 | Extended VC Count - Indicates the number of (extended) Virtual Channels in addition to the default VC supported by the device.<br>This value indicates the number of (extended) MFVC VC Resource Capability, Control, and Status registers that are present in Configuration Space in addition to the required MFVC VC Resource registers for the default VC.<br>The minimum value of this field is 0 (for devices that only support the default VC and only have 1 set of MFVC VC Resource registers for that VC). The maximum value is 7. | RO |
| 6:4 | Low Priority Extended VC Count - Indicates the number of (extended) Virtual Channels in addition to the default VC belonging to the low-priority VC (LPVC) group that has the lowest priority with respect to other VC resources in a strict-priority VC Arbitration.<br>The minimum value of this field is 000b and the maximum value is Extended VC Count. | RO |
| 9:8 | Reference Clock - Indicates the reference clock for Virtual Channels that support time-based WRR Function Arbitration.<br>Defined encodings are:<br>00b = 100 ns reference clock<br>01b - 11b = Reserved | RO |
| 11:10 | Function Arbitration Table Entry Size - Indicates the size (in bits) of Function Arbitration table entry in the device.<br>Defined encodings are:<br>00b = Size of Function Arbitration table entry is 1 bit<br>01b = Size of Function Arbitration table entry is 2 bits<br>10b = Size of Function Arbitration table entry is 4 bits<br>11b = Size of Function Arbitration table entry is 8 bits | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 2:0 | Extended VC Count (扩展 VC 计数) — 指示除默认 VC 之外,设备支持的(扩展)虚通道 (Virtual Channels) 的数量。<br>该值指示除默认 VC 所需 MFVC VC Resource 寄存器之外,配置空间 (Configuration Space) 中存在的(扩展)MFVC VC Resource Capability、Control 和 Status 寄存器的数量。<br>该字段的最小值为 0(针对仅支持默认 VC 且仅具有 1 套该 VC 的 MFVC VC Resource 寄存器的设备)。最大值为 7。 | RO |
| 6:4 | Low Priority Extended VC Count (低优先级扩展 VC 计数) — 指示除默认 VC 之外,属于低优先级 VC (LPVC) 组(在严格优先级 VC 仲裁中具有最低优先级)的(扩展)虚通道的数量。<br>该字段的最小值为 000b,最大值为 Extended VC Count。 | RO |
| 9:8 | Reference Clock (参考时钟) — 指示支持基于时间的 WRR Function 仲裁的虚通道的参考时钟。<br>已定义的编码为:<br>00b = 100 ns 参考时钟<br>01b - 11b = 保留 | RO |
| 11:10 | Function Arbitration Table Entry Size (Function 仲裁表条目大小) — 指示设备中 Function 仲裁表条目的大小(以位为单位)。<br>已定义的编码为:<br>00b = Function 仲裁表条目大小为 1 位<br>01b = Function 仲裁表条目大小为 2 位<br>10b = Function 仲裁表条目大小为 4 位<br>11b = Function 仲裁表条目大小为 8 位 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1277 -->
---

<a id="sec-7-9-2-2"></a>
## 7.9.2.2 MFVC Port VC Capability Register 1 (Offset 04h) | MFVC 端口 VC 能力寄存器 1 (偏移量 04h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MFVC Port VC Capability Register 2 provides further information about the configuration of the Virtual Channels associated with a PCI Express Port of the Multi-Function Device. Figure 7-235 details allocation of register fields in the MFVC Port VC Capability Register 2; Table 7-214 provides the respective bit definitions.

```
 0
 7
 VC Arbitration Capability
 8
 23
 RsvdP
 24
 31
 VC Arbitration Table Offset
```

Figure 7-235 MFVC Port VC Capability Register 2

</td>
<td style="background-color:#e8e8e8">

MFVC Port VC Capability Register 2 (MFVC 端口 VC 能力寄存器 2) 提供关于与多功能设备的 PCI Express 端口相关联的虚通道配置的更多信息。图 7-235 详细说明了 MFVC Port VC Capability Register 2 中各寄存器字段的分配;表 7-214 给出了相应的位定义。

```
 0
 7
 VC Arbitration Capability (VC 仲裁能力)
 8
 23
 RsvdP
 24
 31
 VC Arbitration Table Offset (VC 仲裁表偏移量)
```

图 7-235 MFVC Port VC Capability Register 2 (MFVC 端口 VC 能力寄存器 2)

</td>
</tr>
</tbody>
</table>
</div>


<a id="sec-7-9-2-2-table"></a>

**Table 7-214 MFVC Port VC Capability Register 2 | 表 7-214 MFVC 端口 VC 能力寄存器 2**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | VC Arbitration Capability - Indicates the types of VC Arbitration supported by the device for the LPVC group. This field is valid for all devices that report a Low Priority Extended VC Count greater than 0.<br>Each Bit Location within this field corresponds to a VC Arbitration Capability defined below. When more than 1 bit in this field is Set, it indicates that the device can be configured to provide different VC arbitration services.<br>Defined bit positions are:<br>Bit 0 = Hardware fixed arbitration scheme, e.g., Round Robin<br>Bit 1 = Weighted Round Robin (WRR) arbitration with 32 phases<br>Bit 2 = WRR arbitration with 64 phases<br>Bit 3 = WRR arbitration with 128 phases<br>Bits 4-7 = Reserved | RO |
| 31:24 | VC Arbitration Table Offset - Indicates the location of the MFVC VC Arbitration Table.<br>This field contains the zero-based offset of the table in DQWORDS (16 bytes) from the base address of the MFVC Extended Capability structure. A value of 00h indicates that the table is not present. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | VC Arbitration Capability (VC 仲裁能力) — 指示设备针对 LPVC 组所支持的 VC 仲裁类型。该字段对所有报告 Low Priority Extended VC Count 大于 0 的设备有效。<br>该字段中的每个位位置对应于下文定义的一种 VC 仲裁能力。当该字段中有多于 1 位置位时,指示该设备可被配置为提供不同的 VC 仲裁服务。<br>已定义的位位置为:<br>位 0 = 硬件固定仲裁方案,例如轮询 (Round Robin)<br>位 1 = 加权轮询 (WRR) 仲裁,32 个相位<br>位 2 = WRR 仲裁,64 个相位<br>位 3 = WRR 仲裁,128 个相位<br>位 4-7 = 保留 | RO |
| 31:24 | VC Arbitration Table Offset (VC 仲裁表偏移量) — 指示 MFVC VC Arbitration Table (MFVC VC 仲裁表) 的位置。<br>该字段包含以 DQWORD (16 字节) 为单位的表相对于 MFVC 扩展能力结构 (MFVC Extended Capability structure) 基址的零基偏移量。值为 00h 表示该表不存在。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1278 -->
---

<a id="sec-7-9-2-3"></a>
## 7.9.2.3 MFVC Port VC Capability Register 2 (Offset 08h) | MFVC 端口 VC 能力寄存器 2 (偏移量 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-236 details allocation of register fields in the Port VC Control register; Table 7-215 provides the respective bit definitions.

```
 0
 Load VC Arbitration Table
 1
 3
 VC Arbitration Select
 4
 All VCs Enabled
 5
 15
 RsvdP
```

Figure 7-236 MFVC Port VC Control Register

</td>
<td style="background-color:#e8e8e8">

图 7-236 详细说明了 Port VC Control Register (端口 VC 控制寄存器) 中各寄存器字段的分配;表 7-215 给出了相应的位定义。

```
 0
 Load VC Arbitration Table (加载 VC 仲裁表)
 1
 3
 VC Arbitration Select (VC 仲裁选择)
 4
 All VCs Enabled (使能所有 VC)
 5
 15
 RsvdP
```

图 7-236 MFVC Port VC Control Register (MFVC 端口 VC 控制寄存器)

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-2-4"></a>
## 7.9.2.4 MFVC Port VC Control Register (Offset 0Ch) | MFVC 端口 VC 控制寄存器 (偏移量 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MFVC Port VC Status Register provides status of the configuration of Virtual Channels associated with a Port of the Multi-Function Device. Figure 7-237 details allocation of register fields in the MFVC Port VC Status Register; Table 7-216 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

MFVC Port VC Status Register (MFVC 端口 VC 状态寄存器) 提供与多功能设备的端口相关联的虚通道配置的状态。图 7-237 详细说明了 MFVC Port VC Status Register 中各寄存器字段的分配;表 7-216 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-2-4-table"></a>

**Table 7-215 MFVC Port VC Control Register | 表 7-215 MFVC 端口 VC 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Load VC Arbitration Table - Used by software to update the MFVC VC Arbitration Table. This bit is valid when the selected VC Arbitration uses the MFVC VC Arbitration Table.<br>Software Sets this bit to request hardware to apply new values programmed into MFVC VC Arbitration Table; Clearing this bit has no effect. Software checks the VC Arbitration Table Status bit in the MFVC Port VC Status register to confirm that new values stored in the MFVC VC Arbitration Table are latched by the VC arbitration logic.<br>This bit always returns 0b when read. | RW |
| 3:1 | VC Arbitration Select - Used by software to configure the VC arbitration by selecting one of the supported VC Arbitration schemes indicated by the VC Arbitration Capability field in the MFVC Port VC Capability Register 2.<br>The permissible values of this field are numbers corresponding to one of the asserted bits in the VC Arbitration Capability field.<br>This field cannot be modified when more than one VC in the LPVC group is enabled. | RW |
| 4 | All VCs Enabled - Setting this bit indicates that all VCs that will be used by the Port have been enabled. Setting this bit allows hardware to allocate assigned buffer resources across the enabled VCs.<br>Setting this bit is optional. If this bit remains Clear and some VC Resources are never enabled, performance may be affected but the Link and all enabled VCs must operate correctly.<br>Behavior is undefined if this bit is Set and any VC Enable bit in this capability changes value.<br>Default value of this bit is 0b. | RW |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Load VC Arbitration Table (加载 VC 仲裁表) — 软件使用该位来更新 MFVC VC Arbitration Table (MFVC VC 仲裁表)。当所选 VC 仲裁使用 MFVC VC Arbitration Table 时,该位有效。<br>软件置位该位以请求硬件应用 MFVC VC 仲裁表中编程的新值;清除该位无效。软件通过检查 MFVC Port VC Status Register 中的 VC Arbitration Table Status 位来确认 MFVC VC 仲裁表中存储的新值是否已被 VC 仲裁逻辑锁存。<br>读该位时始终返回 0b。 | RW |
| 3:1 | VC Arbitration Select (VC 仲裁选择) — 软件通过选择 MFVC Port VC Capability Register 2 中 VC Arbitration Capability 字段所指示的支持的 VC 仲裁方案之一来配置 VC 仲裁。<br>该字段的允许值是与 VC Arbitration Capability 字段中置位位之一相对应的数字。<br>当 LPVC 组中启用的 VC 多于一个时,该字段不可修改。 | RW |
| 4 | All VCs Enabled (使能所有 VC) — 置位该位表示将被端口使用的所有 VC 均已启用。置位该位允许硬件在已启用的 VC 之间分配已分配的缓冲区资源。<br>置位该位是可选的。如果该位保持清除状态且某些 VC 资源永远不被启用,则性能可能受到影响,但链路 (Link) 和所有已启用的 VC 必须正确运行。<br>如果该位置位且此能力中的任何 VC Enable 位改变了值,则行为未定义。<br>该位的默认值为 0b。 | RW |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1279 -->
---

<a id="sec-7-9-2-5"></a>
## 7.9.2.5 MFVC Port VC Status Register (Offset 0Eh) | MFVC 端口 VC 状态寄存器 (偏移量 0Eh)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```
 0
 VC Arbitration Table Status
 1
 15
 RsvdZ
```

Figure 7-237 MFVC Port VC Status Register

</td>
<td style="background-color:#e8e8e8">

```
 0
 VC Arbitration Table Status (VC 仲裁表状态)
 1
 15
 RsvdZ
```

图 7-237 MFVC Port VC Status Register (MFVC 端口 VC 状态寄存器)

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-2-5-table"></a>

**Table 7-216 MFVC Port VC Status Register | 表 7-216 MFVC 端口 VC 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | VC Arbitration Table Status - Indicates the coherency status of the MFVC VC Arbitration Table. This bit is valid when the selected VC uses the MFVC VC Arbitration Table.<br>This bit is Set by hardware when any entry of the MFVC VC Arbitration Table is written by software. This bit is Cleared by hardware when hardware finishes loading values stored in the MFVC VC Arbitration Table after software sets the Load VC Arbitration Table bit in the MFVC Port VC Control Register.<br>Default value of this bit is 0b. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | VC Arbitration Table Status (VC 仲裁表状态) — 指示 MFVC VC Arbitration Table 的一致性状态。当所选 VC 使用 MFVC VC Arbitration Table 时,该位有效。<br>当 MFVC VC 仲裁表的任何条目被软件写入时,该位由硬件置位。在软件置位 MFVC Port VC Control Register 中的 Load VC Arbitration Table 位之后,当硬件完成加载 MFVC VC 仲裁表中存储的值时,该位由硬件清除。<br>该位的默认值为 0b。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1280 -->
---

<a id="sec-7-9-2-6"></a>
## 7.9.2.6 MFVC VC Resource Capability Register | MFVC VC 资源能力寄存器


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MFVC VC Resource Capability Register describes the capabilities and configuration of a particular Virtual Channel resource. Figure 7-238 details allocation of register fields in the MFVC VC Resource Capability Register; Table 7-217 provides the respective bit definitions.

```
 0
 7
 Function Arbitration Capability
 8
 15
 RsvdP
 16
 22
 Maximum Time Slots
 23
 RsvdP
 24
 31
 Function Arbitration Table Offset
```

Figure 7-238 MFVC VC Resource Capability Register

</td>
<td style="background-color:#e8e8e8">

MFVC VC Resource Capability Register (MFVC VC 资源能力寄存器) 描述特定虚通道资源的能力和配置。图 7-238 详细说明了 MFVC VC Resource Capability Register 中各寄存器字段的分配;表 7-217 给出了相应的位定义。

```
 0
 7
 Function Arbitration Capability (Function 仲裁能力)
 8
 15
 RsvdP
 16
 22
 Maximum Time Slots (最大时隙数)
 23
 RsvdP
 24
 31
 Function Arbitration Table Offset (Function 仲裁表偏移量)
```

图 7-238 MFVC VC Resource Capability Register (MFVC VC 资源能力寄存器)

</td>
</tr>
</tbody>
</table>
</div>


<a id="sec-7-9-2-6-table"></a>

**Table 7-217 MFVC VC Resource Capability Register | 表 7-217 MFVC VC 资源能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Function Arbitration Capability - Indicates types of Function Arbitration supported by the VC resource.<br>Each Bit Location within this field corresponds to a Function Arbitration Capability defined below. When more than 1 bit in this field is Set, it indicates that the VC resource can be configured to provide different arbitration services.<br>Software selects among these capabilities by writing to the Function Arbitration Select field (see Section 7.9.2.7).<br>Defined bit positions are:<br>Bit 0 = Non-configurable hardware-fixed arbitration scheme, e.g., Round Robin (RR)<br>Bit 1 = Weighted Round Robin (WRR) arbitration with 32 phases<br>Bit 2 = WRR arbitration with 64 phases<br>Bit 3 = WRR arbitration with 128 phases<br>Bit 4 = Time-based WRR with 128 phases<br>Bit 5 = WRR arbitration with 256 phases<br>Bits 6-7 = Reserved | RO |
| 22:16 | Maximum Time Slots - Indicates the maximum number of time slots (minus 1) that the VC resource is capable of supporting when it is configured for time-based WRR Function Arbitration. For example, a value of 000 0000b in this field indicates the supported maximum number of time slots is 1 and a value of 111 1111b indicates the supported maximum number of time slots is 128.<br>This field is valid only when the Function Arbitration Capability indicates that the VC resource supports time-based WRR Function Arbitration. | HwInit |
| 31:24 | Function Arbitration Table Offset - Indicates the location of the Function Arbitration Table associated with the VC resource.<br>This field contains the zero-based offset of the table in DQWORDS (16 bytes) from the base address of the MFVC Extended Capability structure. A value of 00h indicates that the table is not present. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | Function Arbitration Capability (Function 仲裁能力) — 指示 VC 资源所支持的 Function 仲裁类型。<br>该字段中的每个位位置对应于下文定义的一种 Function 仲裁能力。当该字段中有多于 1 位置位时,指示该 VC 资源可被配置为提供不同的仲裁服务。<br>软件通过写入 Function Arbitration Select 字段来选择这些能力之一(参见第 7.9.2.7 节)。<br>已定义的位位置为:<br>位 0 = 不可配置的硬件固定仲裁方案,例如轮询 (RR)<br>位 1 = 加权轮询 (WRR) 仲裁,32 个相位<br>位 2 = WRR 仲裁,64 个相位<br>位 3 = WRR 仲裁,128 个相位<br>位 4 = 基于时间的 WRR,128 个相位<br>位 5 = WRR 仲裁,256 个相位<br>位 6-7 = 保留 | RO |
| 22:16 | Maximum Time Slots (最大时隙数) — 指示 VC 资源配置为基于时间的 WRR Function 仲裁时能够支持的最大时隙数(减 1)。例如,该字段值为 000 0000b 表示所支持的最大时隙数为 1,值为 111 1111b 表示所支持的最大时隙数为 128。<br>仅当 Function Arbitration Capability 指示 VC 资源支持基于时间的 WRR Function 仲裁时,该字段才有效。 | HwInit |
| 31:24 | Function Arbitration Table Offset (Function 仲裁表偏移量) — 指示与 VC 资源相关联的 Function Arbitration Table (Function 仲裁表) 的位置。<br>该字段包含以 DQWORD (16 字节) 为单位的表相对于 MFVC 扩展能力结构 (MFVC Extended Capability structure) 基址的零基偏移量。值为 00h 表示该表不存在。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1281 -->
---

<a id="sec-7-9-2-7"></a>
## 7.9.2.7 MFVC VC Resource Control Register | MFVC VC 资源控制寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-239 details allocation of register fields in the MFVC VC Resource Control Register; Table 7-218 provides the respective bit definitions.

```
 0
 7
 TC/VC Map
 8
 15
 RsvdP
 16
 Load Function Arbitration Table
 17
 19
 Function Arbitration Select
 20
 23
 RsvdP
 24
 26
 VC ID
 27
 29
 Shared Flow Control Usage Limit
 30
 Shared Flow Control Usage Limit Enable
 31
 VC Enable
```

Figure 7-239 MFVC VC Resource Control Register

</td>
<td style="background-color:#e8e8e8">

图 7-239 详细说明了 MFVC VC Resource Control Register (MFVC VC 资源控制寄存器) 中各寄存器字段的分配;表 7-218 给出了相应的位定义。

```
 0
 7
 TC/VC Map (TC/VC 映射)
 8
 15
 RsvdP
 16
 Load Function Arbitration Table (加载 Function 仲裁表)
 17
 19
 Function Arbitration Select (Function 仲裁选择)
 20
 23
 RsvdP
 24
 26
 VC ID
 27
 29
 Shared Flow Control Usage Limit (共享流控使用限制)
 30
 Shared Flow Control Usage Limit Enable (共享流控使用限制使能)
 31
 VC Enable (VC 使能)
```

图 7-239 MFVC VC Resource Control Register (MFVC VC 资源控制寄存器)

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-2-7-table"></a>

**Table 7-218 MFVC VC Resource Control Register | 表 7-218 MFVC VC 资源控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | TC/VC Map - This field indicates the TCs that are mapped to the VC resource.<br>Bit Locations within this field correspond to TC values. For example, when bit 7 is Set in this field, TC7 is mapped to this VC resource. When more than 1 bit in this field is Set, it indicates that multiple TCs are mapped to the VC resource.<br>In order to remove one or more TCs from the TC/VC Map of an enabled VC, software must ensure that no new or outstanding transactions with the TC labels are targeted at the given Link.<br>Default value of this field is FFh for the first VC resource and is 00h for other VC resources.<br>Note: Bit 0 of this field is read-only. It must be hardwired to 1b for the default VC0 and hardwired to 0b for all other enabled VCs. | RW (see the note for exceptions) |
| 16 | Load Function Arbitration Table - When Set, this bit updates the Function Arbitration logic from the Function Arbitration Table for the VC resource. This bit is only valid when the Function Arbitration Table is used by the selected Function Arbitration scheme (that is indicated by a Set bit in the Function Arbitration Capability field selected by Function Arbitration Select).<br>Software sets this bit to signal hardware to update Function Arbitration logic with new values stored in the Function Arbitration Table; clearing this bit has no effect. Software uses the Function Arbitration Table Status bit to confirm whether the new values of Function Arbitration Table are completely latched by the arbitration logic.<br>This bit always returns 0b when read.<br>Default value of this bit is 0b. | RW |
| 19:17 | Function Arbitration Select - This field configures the VC resource to provide a particular Function Arbitration service.<br>The permissible value of this field is a number corresponding to one of the asserted bits in the Function Arbitration Capability field of the VC resource. | RW |
| 26:24 | VC ID - This field assigns a VC ID to the VC resource (see note for exceptions).<br>This field cannot be modified when the VC is already enabled.<br>Note: For the first VC resource (default VC), this field is a read-only field that must be hardwired to 000b. | RW |
| 29:27 | Shared Flow Control Usage Limit - this field controls what percentage of the available Shared Flow Control a given FC/VC is permitted to consume.<br>This limit is applied independently for each Flow Control credit type. For example, if this field contains 101b and Shared Flow Control Usage Limit Enable is Set, a Posted TLP may not pass the Tx Gate if doing so would cause that VC to consume more than 62.5% of the available Shared Posted Header credits or if doing so would cause that VC to consume more than 62.5% of the available Shared Data credits.<br>If Shared Flow Control Usage Limit Enable is Clear, this field is ignored and this VC is permitted to consume all of the shared credits.<br>When Shared Flow Control Usage Limit Enable is Set, and this field contains 000b, this VC is not permitted to consume any shared credits.<br>Behavior is undefined when all VCs have Shared Flow Control Usage Limit Enable Set and the sum of the Shared Flow Control Limit values for all VCs is less than 100%.<br>Encodings are:<br>000b = 0%<br>001b = 12.5%<br>010b = 25%<br>011b = 37.5%<br>100b = 50%<br>101b = 62.5%<br>110b = 75%<br>111b = 87.5% | RW / RO / RsvdP |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | TC/VC Map (TC/VC 映射) — 该字段指示映射到该 VC 资源的 TC。<br>该字段中的位位置对应于 TC 值。例如,当该字段中位 7 置位时,TC7 被映射到该 VC 资源。当该字段中有多于 1 位置位时,指示有多个 TC 被映射到该 VC 资源。<br>为了从已启用 VC 的 TC/VC Map 中移除一个或多个 TC,软件必须确保没有带有这些 TC 标签的新事务或未完成的事务被定向到给定的链路 (Link)。<br>该字段的默认值为第一个 VC 资源为 FFh,其他 VC 资源为 00h。<br>注:该字段的位 0 为只读。对于默认 VC0 必须硬连线为 1b,对于所有其他已启用的 VC 必须硬连线为 0b。 | RW(参见注释中的例外) |
| 16 | Load Function Arbitration Table (加载 Function 仲裁表) — 置位时,该位从 VC 资源的 Function Arbitration Table 更新 Function 仲裁逻辑。仅当所选 Function 仲裁方案使用 Function Arbitration Table 时(由 Function Arbitration Select 所选 Function Arbitration Capability 字段中的置位指示),该位才有效。<br>软件置位该位以通知硬件使用 Function 仲裁表中存储的新值更新 Function 仲裁逻辑;清除该位无效。软件使用 Function Arbitration Table Status 位来确认 Function Arbitration Table 的新值是否已被仲裁逻辑完全锁存。<br>读该位时始终返回 0b。<br>该位的默认值为 0b。 | RW |
| 19:17 | Function Arbitration Select (Function 仲裁选择) — 该字段将 VC 资源配置为提供特定的 Function 仲裁服务。<br>该字段的允许值是与 VC 资源的 Function Arbitration Capability 字段中置位位之一相对应的数字。 | RW |
| 26:24 | VC ID — 该字段为 VC 资源分配一个 VC ID(例外情况参见注释)。<br>当 VC 已启用时,该字段不可修改。<br>注:对于第一个 VC 资源(默认 VC),该字段为只读字段,必须硬连线为 000b。 | RW |
| 29:27 | Shared Flow Control Usage Limit (共享流控使用限制) — 该字段控制允许给定 FC/VC 消耗的可用共享流控 (Shared Flow Control) 百分比。<br>该限制针对每种流控 (Flow Control) 信用 (Credit) 类型独立应用。例如,如果该字段包含 101b 且 Shared Flow Control Usage Limit Enable 置位,则 Posted TLP (有数据,无完成) 在通过 Tx Gate 时可能不被允许,如果这样做将导致该 VC 消耗超过 62.5% 的可用共享 Posted Header 信用,或导致该 VC 消耗超过 62.5% 的可用共享 Data 信用。<br>如果 Shared Flow Control Usage Limit Enable 清除,则该字段被忽略,且该 VC 被允许消耗所有共享信用。<br>当 Shared Flow Control Usage Limit Enable 置位且该字段包含 000b 时,该 VC 不被允许消耗任何共享信用。<br>当所有 VC 都将 Shared Flow Control Usage Limit Enable 置位且所有 VC 的 Shared Flow Control Limit 值之和小于 100% 时,行为未定义。<br>编码为:<br>000b = 0%<br>001b = 12.5%<br>010b = 25%<br>011b = 37.5%<br>100b = 50%<br>101b = 62.5%<br>110b = 75%<br>111b = 87.5% | RW / RO / RsvdP |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1282 -->
---

<a id="sec-7-9-2-7-continued"></a>
## 7.9.2.7 MFVC VC Resource Control Register (continued) | MFVC VC 资源控制寄存器(续)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Behavior is undefined if this field changes value while VC Enable and Shared Flow Control Usage Limit Enable are both Set.

This field is RsvdP when Flit Mode Supported is Clear.

When Extended VC Count is 0, this field is permitted to be hardwired to 000b.

When this field is RW, the default value is implementation specific.

**Bit 30 - Shared Flow Control Usage Limit Enable**

When Set, this bit enables use of the Shared Flow Control Usage Limit value above at the transmitter for this Virtual Channel.

Behavior is undefined of the value of this bit changes while VC Enable is Set.

This bit is RsvdP when Flit Mode Supported is Clear.

When Extended VC Count is 0, this bit is permitted to be hardwired to 0b.

When this bit is RW, the default value is implementation specific.

**Bit 31 - VC Enable**

When Set, this bit enables a Virtual Channel. The Virtual Channel is disabled when this bit is cleared.

Software must use the VC Negotiation Pending bit to check whether the VC negotiation is complete.

For VC0, the attribute is RO. If no SVC capability is implemented in this Port, this bit's value must be 1b; otherwise, this bit's value must always be the same value as the Use VC/MFVC bit in the SVC Port Status Register. See Section 6.3.5.

For other VCs, if no SVC capability is implemented in this Port or if the Use VC/MFVC bit is Set, the default value of this bit is 0b and the attribute is RW; otherwise, this bit must be RO with a value of 0b.

To enable a Virtual Channel, in a Port using MFVC mechanisms, the VC Enable bit for that Virtual Channel must be Set. The corresponding Virtual Channel in the Link partner Port must be enabled as well, and that Virtual Channel may be in SVC, VC, or MFVC capabilities. To disable a Virtual Channel, the Virtual Channel must be disabled in both components on the Link. Software must ensure that no traffic is using a Virtual Channel at the time it is disabled. Software must fully disable a Virtual Channel in both components on a Link before re-enabling the Virtual Channel.

When this bit is forced to be RO with a value of 0b due to the Use VC/MFVC bit being Clear, its associated VC is disabled, rendering most of its control registers to be ineffective.

| Attribute | Value |
|-----------|-------|
| 30 | RW / RO / RsvdP |
| 31 | RW/HwInit |

</td>
<td style="background-color:#e8e8e8">

如果该字段在 VC Enable 和 Shared Flow Control Usage Limit Enable 均置位时改变值,则行为未定义。

当 Flit Mode Supported 清除时,该字段为 RsvdP。

当 Extended VC Count 为 0 时,该字段允许硬连线为 000b。

当该字段为 RW 时,默认值为实现特定的。

**位 30 - Shared Flow Control Usage Limit Enable (共享流控使用限制使能)**

置位时,该位使能上述共享流控使用限制值在该虚通道发送器上的使用。

如果该位的值在 VC Enable 置位时改变,则行为未定义。

当 Flit Mode Supported 清除时,该位为 RsvdP。

当 Extended VC Count 为 0 时,该位允许硬连线为 0b。

当该位为 RW 时,默认值为实现特定的。

**位 31 - VC Enable (VC 使能)**

置位时,该位使能一个虚通道。当该位清除时,虚通道被禁用。

软件必须使用 VC Negotiation Pending 位检查 VC 协商是否完成。

对于 VC0,属性为 RO。如果该端口中未实现 SVC 能力,则该位的值必须为 1b;否则,该位的值必须始终与 SVC Port Status Register 中 Use VC/MFVC 位的值相同。参见第 6.3.5 节。

对于其他 VC,如果该端口中未实现 SVC 能力,或者 Use VC/MFVC 位置位,则该位的默认值为 0b,属性为 RW;否则,该位必须为 RO,值为 0b。

要在使用 MFVC 机制的端口中使能一个虚通道,必须置位该虚通道的 VC Enable 位。链路 (Link) 伙伴端口中的相应虚通道也必须被使能,且该虚通道可以位于 SVC、VC 或 MFVC 能力中。要禁用一个虚通道,该虚通道必须在链路两端组件中均被禁用。软件必须确保在禁用虚通道时没有任何流量正在使用该虚通道。软件必须在重新使能虚通道之前,在链路两端组件中完全禁用该虚通道。

当由于 Use VC/MFVC 位被清除而迫使该位为值 0b 的 RO 时,其关联的 VC 被禁用,导致其大部分控制寄存器失效。

| 属性 | 值 |
|------|----|
| 30 | RW / RO / RsvdP |
| 31 | RW/HwInit |

</td>
</tr>
</tbody>
</table>
</div>


Figure 7-240 details allocation of register fields in the MFVC VC Resource Status Register; Table 7-219 provides the respective bit definitions.

```
 0
 Function Arbitration Table Status
 1
 VC Negotiation Pending
 2
 15
 RsvdZ
```

Figure 7-240 MFVC VC Resource Status Register

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1283 -->
---

<a id="sec-7-9-2-8"></a>
## 7.9.2.8 MFVC VC Resource Status Register | MFVC VC 资源状态寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

<a id="sec-7-9-2-8-table"></a>

**Table 7-219 MFVC VC Resource Status Register | 表 7-219 MFVC VC 资源状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Function Arbitration Table Status - This bit indicates the coherency status of the Function Arbitration Table associated with the VC resource. This bit is valid only when the Function Arbitration Table is used by the selected Function Arbitration for the VC resource.<br>This bit is Set by hardware when any entry of the Function Arbitration Table is written to by software. This bit is Cleared by hardware when hardware finishes loading values stored in the Function Arbitration Table after software sets the Load Function Arbitration Table bit.<br>Default value of this bit is 0b. | RO |
| 1 | VC Negotiation Pending - This bit indicates whether the Virtual Channel negotiation (initialization or disabling) is in pending state.<br>When this bit is Set by hardware, it indicates that the VC resource is still in the process of negotiation. This bit is Cleared by hardware after the VC negotiation is complete. For a non-default Virtual Channel, software may use this bit when enabling or disabling the VC. For the default VC, this bit indicates the status of the process of Flow Control initialization.<br>Before using a Virtual Channel, software must check whether the VC Negotiation Pending bits for that Virtual Channel are Clear in both components on a Link. | RO |

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Function Arbitration Table Status (Function 仲裁表状态) — 该位指示与 VC 资源相关联的 Function Arbitration Table 的一致性状态。仅当所选 Function 仲裁使用该 VC 资源的 Function Arbitration Table 时,该位才有效。<br>当 Function Arbitration Table 的任何条目被软件写入时,该位由硬件置位。在软件置位 Load Function Arbitration Table 位之后,当硬件完成加载 Function Arbitration Table 中存储的值时,该位由硬件清除。<br>该位的默认值为 0b。 | RO |
| 1 | VC Negotiation Pending (VC 协商挂起) — 该位指示虚通道协商(初始化或禁用)是否处于挂起状态。<br>当该位由硬件置位时,指示该 VC 资源仍处于协商过程中。该位在 VC 协商完成后由硬件清除。对于非默认虚通道,软件可在启用或禁用 VC 时使用该位。对于默认 VC,该位指示流控 (Flow Control) 初始化过程的状态。<br>在使用虚通道之前,软件必须检查该虚通道在链路两端组件中的 VC Negotiation Pending 位是否均已清除。 | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1284 -->
---

<a id="sec-7-9-2-9"></a>
## 7.9.2.9 MFVC VC Arbitration Table | MFVC VC 仲裁表

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The definition of the MFVC VC Arbitration Table in the MFVC Extended Capability structure is identical to that in the VC Extended Capability structure (see Section 7.9.1.9).

</td>
<td style="background-color:#e8e8e8">

MFVC 扩展能力结构中 MFVC VC Arbitration Table (MFVC VC 仲裁表) 的定义与 VC 扩展能力结构中的定义相同(参见第 7.9.1.9 节)。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-2-10"></a>
## 7.9.2.10 Function Arbitration Table | Function 仲裁表


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Function Arbitration Table register in the MFVC Extended Capability structure takes the same form as the Port Arbitration Table register in the VC Extended Capability structure (see Section 7.9.1.10).

The Function Arbitration Table register is a read-write register array that is used to store the WRR or time-based WRR arbitration table for Function Arbitration for the VC resource. It is only present when one or more asserted bits in the Function Arbitration Capability field indicate that the Multi-Function Device supports a Function Arbitration scheme that uses a programmable arbitration table. Furthermore, it is only valid when one of the above-mentioned bits in the Function Arbitration Capability field is selected by the Function Arbitration Select field.

The Function Arbitration Table represents one Function arbitration period. Each table entry containing a Function Number or Function Group Number corresponds to a phase within a Function Arbitration period. The table entry size requirements are as follows:

- The table entry size for non-ARI devices must support enough values to specify all implemented Functions plus at least one value that does not correspond to an implemented Function. For example, a table with 2-bit entries can be used by a Multi-Function Device with up to three Functions.
- The table entry size for ARI Devices must be either 4 bits or 8 bits.
  - If MFVC Function Groups are enabled, each entry maps to a single Function Group. Arbitration between multiple Functions within a Function Group is implementation specific, but must guarantee forward progress. ¹⁸²

¹⁸² If an ARI Device supports MFVC Function Groups capability and ARI-aware software enables it, arbitration is based on Function Groups instead of Functions. See Section 7.8.8.

</td>
<td style="background-color:#e8e8e8">

MFVC 扩展能力结构中 Function Arbitration Table (Function 仲裁表) 寄存器的形式与 VC 扩展能力结构中 Port Arbitration Table (端口仲裁表) 寄存器的形式相同(参见第 7.9.1.10 节)。

Function Arbitration Table 寄存器是一个读-写寄存器数组,用于存储 VC 资源 Function 仲裁的 WRR 或基于时间的 WRR 仲裁表。仅当 Function Arbitration Capability 字段中有一个或多个置位位指示多功能设备 (Multi-Function Device) 支持使用可编程仲裁表的 Function 仲裁方案时,它才会出现。此外,仅当 Function Arbitration Capability 字段中上述位之一被 Function Arbitration Select 字段选中时,它才有效。

Function Arbitration Table 表示一个 Function 仲裁周期。包含 Function Number (Function 编号) 或 Function Group Number (Function 组编号) 的每个表条目对应于 Function 仲裁周期内的一个相位。表条目大小要求如下:

- 对于非 ARI 设备,表条目大小必须支持足够的值以指定所有已实现的 Function 加上至少一个不对应于已实现 Function 的值。例如,具有 2 位条目的表可用于最多具有三个 Function 的多功能设备。
- 对于 ARI 设备 (ARI Devices),表条目大小必须为 4 位或 8 位。
  - 如果启用了 MFVC Function Groups,则每个条目映射到单个 Function 组。Function 组内多个 Function 之间的仲裁是实现特定的,但必须保证前向进度。¹⁸²

¹⁸² 如果 ARI 设备支持 MFVC Function Groups 能力且 ARI 感知的软件启用了该能力,则仲裁将基于 Function 组而不是 Function 进行。参见第 7.8.8 节。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1285 -->
---

<a id="sec-7-9-2-10-continued"></a>
## 7.9.2.10 Function Arbitration Table (continued) | Function 仲裁表(续)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

- If MFVC Function Groups are not enabled and 4-bit entries are implemented, a given entry maps to all Functions whose Function Number modulo 8 matches its value. Similarly, if 8-bit entries are implemented, a given entry maps to all Functions whose Function Number modulo 128 matches its value. If a given entry maps to multiple Functions, arbitration between those Functions is implementation specific, but must guarantee forward progress.

A Function Number or Function Group Number written to a table entry indicates that the phase within the Function Arbitration period is assigned to the selected Function or Function Group (the Function Number or Function Group Number must be a valid one).

- When the WRR Function Arbitration is used for a VC of the Egress Port of the Multi-Function Device, at each arbitration phase the Function Arbiter serves one transaction from the Function or Function Group indicated by the Function Number or Function Group Number of the current phase. When finished, it immediately advances to the next phase. A phase is skipped, i.e., the Function Arbiter simply moves to the next phase immediately if the Function or Function Group indicated by the phase does not contain any transaction for the VC.
- When the Time-based WRR Function Arbitration is used for a VC of the Egress Port of the Multi-Function Device, at each arbitration phase aligning to a virtual timeslot, the Function Arbiter serves one transaction from the Function or Function Group indicated by the Function Number or Function Group Number of the current phase. It advances to the next phase at the next virtual timeslot. A phase indicates an "idle" timeslot, i.e., the Function Arbiter does not serve any transaction during the phase, if:
  - the phase contains the Number of a Function or a Function Group that does not exist, or
  - the Function or Function Group indicated by the phase does not contain any transaction for the VC.

The Function Arbitration Table Entry Size field in the MFVC Port VC Capability Register 1 determines the table entry size. The length of the table is determined by the Function Arbitration Select field as shown in Table 7-220.

When the Function Arbitration Table is used by the default Function Arbitration for the default VC, the default values for the table entries must contain at least one entry for each of the active Functions or Function Groups in the Multi-Function Device to ensure forward progress for the default VC for the Multi-Function Device's Upstream Port. The table may contain RR or RR-like fair Function Arbitration for the default VC.

**Table 7-220 Length of Function Arbitration Table | 表 7-220 Function 仲裁表长度**

| Function Arbitration Select | Function Arbitration Table Length |
|------------------------------|-----------------------------------|
| 001b | 32 entries |
| 010b | 64 entries |
| 011b | 128 entries |
| 100b | 128 entries |
| 101b | 256 entries |

| Function Arbitration Select | Function Arbitration Table Length |
|------------------------------|-----------------------------------|
| 001b | 32 entries (32 个条目) |
| 010b | 64 entries (64 个条目) |
| 011b | 128 entries (128 个条目) |
| 100b | 128 entries (128 个条目) |
| 101b | 256 entries (256 个条目) |

</td>
<td style="background-color:#e8e8e8">

- 如果未启用 MFVC Function Groups 且实现了 4 位条目,则给定条目映射到其 Function Number 模 8 与该值匹配的所有 Function。类似地,如果实现了 8 位条目,则给定条目映射到其 Function Number 模 128 与该值匹配的所有 Function。如果给定条目映射到多个 Function,则这些 Function 之间的仲裁是实现特定的,但必须保证前向进度。

写入表条目的 Function Number 或 Function Group Number 指示 Function 仲裁周期内的该相位被分配给所选 Function 或 Function 组(Function Number 或 Function Group Number 必须为有效值)。

- 当多功能设备出口端口 (Egress Port) 的 VC 使用 WRR Function 仲裁时,在每个仲裁相位,Function Arbiter (Function 仲裁器) 从当前相位的 Function Number 或 Function Group Number 所指示的 Function 或 Function 组中服务一个事务。完成后,它立即前进到下一个相位。如果该相位指示的 Function 或 Function 组没有该 VC 的任何事务,则跳过该相位,即 Function Arbiter 立即移至下一个相位。
- 当多功能设备出口端口的 VC 使用基于时间的 WRR Function 仲裁时,在每个与虚拟时隙对齐的仲裁相位,Function Arbiter 从当前相位的 Function Number 或 Function Group Number 所指示的 Function 或 Function 组中服务一个事务。它在下一个虚拟时隙前进到下一个相位。如果出现以下情况,则相位表示"空闲"时隙,即 Function Arbiter 在该相位期间不服务任何事务:
  - 该相位包含不存在的 Function 或 Function 组的编号,或
  - 该相位所指示的 Function 或 Function 组没有该 VC 的任何事务。

MFVC Port VC Capability Register 1 中的 Function Arbitration Table Entry Size 字段决定表条目大小。表的长度由 Function Arbitration Select 字段决定,如表 7-220 所示。

当默认 Function 仲裁将 Function Arbitration Table 用于默认 VC 时,表条目的默认值必须至少包含多功能设备中每个活动的 Function 或 Function 组的一个条目,以确保多功能设备上游端口 (Upstream Port) 的默认 VC 的前向进度。该表可以包含用于默认 VC 的 RR 或类似 RR 的公平 Function 仲裁。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1290 -->
---

<a id="sec-7-9-3-2"></a>
## 7.9.3 Device Serial Number Extended Capability | 设备序列号扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Device Serial Number Extended Capability is an optional Extended Capability that may be implemented by any PCI Express device Function. The Device Serial Number is a read-only 64-bit value that is unique for a given PCI Express device. Figure 7-241 details allocation of register fields in the Device Serial Number Extended Capability structure.

It is permitted but not recommended for RCiEPs to implement this Capability.

</td>
<td style="background-color:#e8e8e8">

Device Serial Number Extended Capability (设备序列号扩展能力) 是一种可选的扩展能力,可由任何 PCI Express 设备 Function 实现。Device Serial Number (设备序列号) 是一个只读 64 位值,对于给定的 PCI Express 设备是唯一的。图 7-241 详细说明了 Device Serial Number Extended Capability 结构中各寄存器字段的分配。

允许但不推荐 RCiEP 实现此能力。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


---

<a id="sec-7-9-3"></a>
## 7.9.3 Device Serial Number Extended Capability | 设备序列号扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.3 Device Serial Number Extended Capability §

§

RCiEPs that implement this Capability are permitted but not required to return the same Device Serial Number value as that reported by other RCiEPs of the same Root Complex (根复合体).

All Multi-Function Devices other than RCiEPs that implement this Capability must implement it for Function 0; other Functions that implement this Capability must return the same Device Serial Number value as that reported by Function 0.

RCiEPs are permitted to implement or not implement this Capability on an individual basis, independent of whether they are part of a Multi-Function Device.

A PCI Express component other than a Root Complex containing multiple Devices such as a PCI Express Switch (交换机) that implements this Capability must return the same Device Serial Number for each device.

The Device Serial Number Extended Capability is permitted to be present in PFs (物理功能). If a PF contains the capability, its value applies to all associated VFs (虚拟功能). VFs are permitted but not recommended to implement this capability. VFs that implement this capability must return the same Device Serial Number value as that reported by their associated PF.

</td>
<td style="background-color:#e8e8e8">

7.9.3 设备序列号扩展能力 §

§

实现此能力的 RCiEP 允许(但非必须)返回与同一根复合体 (Root Complex) 中其他 RCiEP 所报告的设备序列号相同的值。

除 RCiEP 之外,实现此能力的所有多功能设备必须为 Function 0 实现该能力;实现此能力的其他 Function 必须返回与 Function 0 所报告的设备序列号相同的值。

RCiEP 可以根据自身情况决定是否实现此能力,而无需考虑其是否属于多功能设备的一部分。

除根复合体外,包含多个设备的 PCI Express 组件(例如实现此能力的 PCI Express 交换机 (Switch))必须为每个设备返回相同的设备序列号。

设备序列号扩展能力允许出现在 PF 中。若 PF 包含该能力,则其值适用于所有关联的 VF。VF 允许(但不推荐)实现此能力。实现此能力的 VF 必须返回与其关联 PF 所报告的设备序列号相同的值。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1286 -->
---

<a id="sec-7-9-3-fig"></a>

> **Figure 7-241.** Device Serial Number Extended Capability Structure
> <img src="figures/chapter_07/fig_1286_1_tight.png" width="700">

> **图 7-241.** 设备序列号扩展能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-241 Device Serial Number Extended Capability Structure

§ Figure 7-242 details allocation of register fields in the Device Serial Number Extended Capability Header; § Table 7-221 provides the respective bit definitions. Refer to § Section 7.6.3 for a description of the PCI Express Extended Capability header. The Extended Capability ID for the Device Serial Number Extended Capability is 0003h.

</td>
<td style="background-color:#e8e8e8">

图 7-241 设备序列号扩展能力结构

§ 图 7-242 详细说明了设备序列号扩展能力包头 (Header) 中各寄存器字段的分配;§ 表 7-221 给出了相应的位定义。有关 PCI Express 扩展能力包头的描述,请参见 § 第 7.6.3 节。设备序列号扩展能力的扩展能力 ID 为 0003h。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-242.** Device Serial Number Extended Capability Header
> <img src="figures/chapter_07/fig_1286_2_tight.png" width="700">

> **图 7-242.** 设备序列号扩展能力包头

**Table 7-221. Device Serial Number Extended Capability Header | 表 7-221. 设备序列号扩展能力包头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the Device Serial Number Extended Capability is 0003h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space (配置空间), this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

---

<a id="sec-7-9-3-1"></a>
## 7.9.3.1 Device Serial Number Extended Capability Header (Offset 00h) | 设备序列号扩展能力包头(偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.3.1 Device Serial Number Extended Capability Header (Offset 00h) §

§

§

§

</td>
<td style="background-color:#e8e8e8">

7.9.3.1 设备序列号扩展能力包头(偏移 00h) §

§

§

§

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1287 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Serial Number register is a 64-bit field that contains the IEEE defined 64-bit extended unique identifier [EUI-64].

§ Figure 7-243 details allocation of register fields in the Serial Number register; § Table 7-222 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

序列号寄存器是一个 64 位字段,包含 IEEE 定义的 64 位扩展唯一标识符 [EUI-64]。

§ 图 7-243 详细说明了序列号寄存器中各寄存器字段的分配;§ 表 7-222 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-243.** Serial Number Register
> <img src="figures/chapter_07/fig_1287_1_tight.png" width="700">

> **图 7-243.** 序列号寄存器

**Table 7-222. Serial Number Register | 表 7-222. 序列号寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 63:0 | PCI Express Device Serial Number - This field contains the IEEE defined 64-bit Extended Unique Identifier [EUI-64]. This identifier includes a 24-bit company id value assigned by IEEE registration authority and a 40-bit extension identifier assigned by the manufacturer.<br>PCI Express Device Serial Number[07:00] = EUI[63:56]<br>PCI Express Device Serial Number[15:08] = EUI[55:48]<br>PCI Express Device Serial Number[23:16] = EUI[47:40]<br>PCI Express Device Serial Number[31:24] = EUI[39:32]<br>PCI Express Device Serial Number[39:32] = EUI[31:24]<br>PCI Express Device Serial Number[47:40] = EUI[23:16]<br>PCI Express Device Serial Number[55:48] = EUI[15:08]<br>PCI Express Device Serial Number[63:56] = EUI[07:00] | RO |

---

<a id="sec-7-9-3-2"></a>
## 7.9.3.2 Serial Number Register (Offset 04h) | 序列号寄存器(偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.3.2 Serial Number Register (Offset 04h) §

</td>
<td style="background-color:#e8e8e8">

7.9.3.2 序列号寄存器(偏移 04h) §

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-4"></a>
## 7.9.4 Vendor-Specific Capability | 厂商特定能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Vendor-Specific Capability is a capability structure in PCI-compatible Configuration Space (first 256 bytes) as shown in § Figure 7-244.

The Vendor-Specific Capability allows device vendors to use the Capability mechanism for vendor-specific information.

The layout of the information is vendor-specific, except for the first three bytes, as explained below.

A single PCI Express Function is permitted to contain multiple VSEC structures.

</td>
<td style="background-color:#e8e8e8">

厂商特定能力是 PCI 兼容配置空间 (前 256 字节) 中的一种能力结构,如 § 图 7-244 所示。

厂商特定能力允许设备厂商使用能力机制来携带厂商特定信息。

除前三个字节外,信息的布局由厂商自行定义,具体如下所述。

单个 PCI Express Function 允许包含多个 VSEC 结构。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1288 -->
---

> **Figure 7-244.** Vendor-Specific Capability
> <img src="figures/chapter_07/fig_1288_1.png" width="700">

> **图 7-244.** 厂商特定能力

**Table 7-223. Vendor-Specific Capability | 表 7-223. 厂商特定能力**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Capability ID - Indicates the PCI Express Capability structure. This field must return a Capability ID of 09h indicating that this is a Vendor-Specific Capability structure. | RO |
| 15:8 | Next Capability Pointer - This field contains the offset to the next PCI Capability structure or 00h if no other items exist in the linked list of Capabilities. | RO |
| 23:16 | Capability Length - This field provides the number of bytes in the Capability structure (including the three bytes consumed by the Capability ID, Next Capability Pointer, and Capability Length field). | RO |
| 31:24 | Vendor Specific Information | Vendor Specific |

---

<a id="sec-7-9-5"></a>
## 7.9.5 Vendor-Specific Extended Capability | 厂商特定扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Vendor-Specific Extended Capability (VSEC Capability) is an optional Extended Capability that is permitted to be implemented by any PCI Express Function or RCRB. This allows PCI Express component vendors to use the Extended Capability mechanism to expose vendor-specific registers.

A single PCI Express Function or RCRB is permitted to contain multiple VSEC structures.

An example usage is a set of vendor-specific features that are intended to go into an on-going series of components from that vendor. A VSEC structure can tell vendor-specific software which features a particular component supports, including components developed after the software was released.

§ Figure 7-245 details allocation of register fields in the VSEC structure. The structure of the Vendor-Specific Extended Capability Header and the Vendor-Specific Header is architected by this specification.

With a PCI Express Function, the structure and definition of the vendor-specific Registers area is determined by the vendor indicated by the Vendor ID field located at byte offset 00h in PCI-compatible Configuration Space. With an RCRB, a VSEC is permitted only if the RCRB also contains an RCRB Header Extended Capability structure, which contains a Vendor ID field indicating the vendor.

</td>
<td style="background-color:#e8e8e8">

厂商特定扩展能力 (VSEC Capability) 是一种可选的扩展能力,允许由任何 PCI Express Function 或 RCRB 实现。这允许 PCI Express 组件厂商使用扩展能力机制来公开厂商特定的寄存器。

单个 PCI Express Function 或 RCRB 允许包含多个 VSEC 结构。

一个示例用法是:厂商预期在未来一系列组件中持续加入的厂商特定功能集。VSEC 结构可告知厂商特定软件某个特定组件支持哪些功能,包括在软件发布之后开发的组件。

§ 图 7-245 详细说明了 VSEC 结构中各寄存器字段的分配。厂商特定扩展能力包头和厂商特定包头的结构由本规范定义。

对于 PCI Express Function,厂商特定寄存器区域的结构和定义由 PCI 兼容配置空间中字节偏移 00h 处的 Vendor ID 字段所指示的厂商确定。对于 RCRB,仅当 RCRB 同时包含 RCRB Header 扩展能力结构(其中包含指示厂商的 Vendor ID 字段)时,才允许使用 VSEC。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1289 -->
---

> **Figure 7-245.** VSEC Capability Structure
> <img src="figures/chapter_07/fig_1289_1_tight.png" width="700">

> **图 7-245.** VSEC 能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-246 details allocation of register fields in the Vendor-Specific Extended Capability Header; § Table 7-224 provides the respective bit definitions. Refer to § Section 7.6.3 for a description of the PCI Express Extended Capability Header. The Extended Capability ID for the Vendor-Specific Extended Capability is 000Bh.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-246 详细说明了厂商特定扩展能力包头中各寄存器字段的分配;§ 表 7-224 给出了相应的位定义。有关 PCI Express 扩展能力包头的描述,请参见 § 第 7.6.3 节。厂商特定扩展能力的扩展能力 ID 为 000Bh。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-246.** Vendor-Specific Extended Capability Header
> <img src="figures/chapter_07/fig_1289_2_tight.png" width="700">

> **图 7-246.** 厂商特定扩展能力包头

**Table 7-224. Vendor-Specific Extended Capability Header | 表 7-224. 厂商特定扩展能力包头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the Vendor-Specific Extended Capability is 000Bh. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

---

<a id="sec-7-9-5-1"></a>
## 7.9.5.1 Vendor-Specific Extended Capability Header (Offset 00h) | 厂商特定扩展能力包头(偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.5.1 Vendor-Specific Extended Capability Header (Offset 00h) §

§

§

§

</td>
<td style="background-color:#e8e8e8">

7.9.5.1 厂商特定扩展能力包头(偏移 00h) §

§

§

§

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1290 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-247 details allocation of register fields in the Vendor-Specific Header; § Table 7-225 provides the respective bit definitions.

Vendor-specific software must qualify the associated Vendor ID of the PCI Express Function or RCRB before attempting to interpret the values in the VSEC ID or VSEC Rev fields.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-247 详细说明了厂商特定包头中各寄存器字段的分配;§ 表 7-225 给出了相应的位定义。

厂商特定软件在尝试解读 VSEC ID 或 VSEC Rev 字段中的值之前,必须先确认 PCI Express Function 或 RCRB 的相关 Vendor ID。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-247.** Vendor-Specific Header
> <img src="figures/chapter_07/fig_1290_1_tight.png" width="700">

> **图 7-247.** 厂商特定包头

**Table 7-225. Vendor-Specific Header | 表 7-225. 厂商特定包头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | VSEC ID - This field is a vendor-defined ID number that indicates the nature and format of the VSEC structure. Software must qualify the Vendor ID before interpreting this field. | RO |
| 19:16 | VSEC Rev - This field is a vendor-defined version number that indicates the version of the VSEC structure. Software must qualify the Vendor ID and VSEC ID before interpreting this field. | RO |
| 31:20 | VSEC Length - This field indicates the number of bytes in the entire VSEC structure, including the Vendor-Specific Extended Capability Header, the Vendor-Specific Header, and the vendor-specific registers. | RO |

---

<a id="sec-7-9-5-2"></a>
## 7.9.5.2 Vendor-Specific Header (Offset 04h) | 厂商特定包头(偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.5.2 Vendor-Specific Header (Offset 04h) §

</td>
<td style="background-color:#e8e8e8">

7.9.5.2 厂商特定包头(偏移 04h) §

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-6"></a>
## 7.9.6 Designated Vendor-Specific Extended Capability (DVSEC) | 指定厂商特定扩展能力 (DVSEC)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Designated Vendor-Specific Extended Capability (DVSEC Capability) is an optional Extended Capability that is permitted to be implemented by any PCI Express Function or RCRB. This allows PCI Express component vendors to use the Extended Capability mechanism to expose vendor-specific registers that can be present in components by a variety of vendors.

A single PCI Express Function or RCRB is permitted to contain multiple DVSEC Capability structures.

An example usage is a set of vendor-specific features that are intended to go into an on-going series of components from a collection of vendors. A DVSEC Capability structure can tell vendor-specific software which features a particular component supports, including components developed after the software was released.

§ Figure 7-248 details allocation of register fields in the DVSEC Capability structure. The structure of the PCI Express Extended Capability Header and the Designated Vendor-Specific header is architected by this specification.

The DVSEC Vendor-Specific Register area begins at offset 0Ah.

</td>
<td style="background-color:#e8e8e8">

指定厂商特定扩展能力 (DVSEC Capability) 是一种可选的扩展能力,允许由任何 PCI Express Function 或 RCRB 实现。这允许 PCI Express 组件厂商使用扩展能力机制来公开可能由多家厂商提供的组件中的厂商特定寄存器。

单个 PCI Express Function 或 RCRB 允许包含多个 DVSEC 能力结构。

一个示例用法是:多个厂商预期在未来一系列组件中持续加入的厂商特定功能集。DVSEC 能力结构可告知厂商特定软件某个特定组件支持哪些功能,包括在软件发布之后开发的组件。

§ 图 7-248 详细说明了 DVSEC 能力结构中各寄存器字段的分配。PCI Express 扩展能力包头和指定厂商特定包头的结构由本规范定义。

DVSEC 厂商特定寄存器区域从偏移 0Ah 处开始。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1291 -->
---

> **Figure 7-248.** Designated Vendor-Specific Extended Capability
> <img src="figures/chapter_07/fig_1291_1_tight.png" width="700">

> **图 7-248.** 指定厂商特定扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-249 details allocation of register fields in the Designated Vendor-Specific Extended Capability Header; § Table 7-226 provides the respective bit definitions. Refer to § Section 7.9.3 for a description of the PCI Express Extended Capability Header. The Extended Capability ID for the Designated Vendor-Specific Extended Capability is 0023h.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-249 详细说明了指定厂商特定扩展能力包头中各寄存器字段的分配;§ 表 7-226 给出了相应的位定义。有关 PCI Express 扩展能力包头的描述,请参见 § 第 7.9.3 节。指定厂商特定扩展能力的扩展能力 ID 为 0023h。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-249.** Designated Vendor-Specific Extended Capability Header
> <img src="figures/chapter_07/fig_1291_2_tight.png" width="700">

> **图 7-249.** 指定厂商特定扩展能力包头

**Table 7-226. Designated Vendor-Specific Extended Capability Header | 表 7-226. 指定厂商特定扩展能力包头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the Designated Vendor-Specific Extended Capability is 0023h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

---

<a id="sec-7-9-6-1"></a>
## 7.9.6.1 Designated Vendor-Specific Extended Capability Header (Offset 00h) | 指定厂商特定扩展能力包头(偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.6.1 Designated Vendor-Specific Extended Capability Header (Offset 00h) §

§

§

§

</td>
<td style="background-color:#e8e8e8">

7.9.6.1 指定厂商特定扩展能力包头(偏移 00h) §

§

§

§

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1292 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-250 details allocation of register fields in the Designated Vendor-Specific Header 1; § Table 7-227 provides the respective bit definitions.

Vendor-specific software must qualify the DVSEC Vendor ID before attempting to interpret the DVSEC Revision field.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-250 详细说明了指定厂商特定包头 1 中各寄存器字段的分配;§ 表 7-227 给出了相应的位定义。

厂商特定软件在尝试解读 DVSEC Revision 字段之前,必须先确认 DVSEC Vendor ID。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-250.** Designated Vendor-Specific Header 1
> <img src="figures/chapter_07/fig_1292_1_tight.png" width="700">

> **图 7-250.** 指定厂商特定包头 1

**Table 7-227. Designated Vendor-Specific Header 1 | 表 7-227. 指定厂商特定包头 1**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | DVSEC Vendor ID - This field is the Vendor ID associated with the vendor that defined the contents of this capability. | RO |
| 19:16 | DVSEC Revision - This field is a vendor-defined version number that indicates the version of the DVSEC structure. Software must qualify the DVSEC Vendor ID and DVSEC ID before interpreting this field. | RO |
| 31:20 | DVSEC Length - This field indicates the number of bytes in the entire DVSEC structure, including the PCI Express Extended Capability Header, the DVSEC Header 1, DVSEC Header 2, and DVSEC vendor-specific registers. | RO |

---

<a id="sec-7-9-6-2"></a>
## 7.9.6.2 Designated Vendor-Specific Header 1 (Offset 04h) | 指定厂商特定包头 1(偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.6.2 Designated Vendor-Specific Header 1 (Offset 04h) §

</td>
<td style="background-color:#e8e8e8">

7.9.6.2 指定厂商特定包头 1(偏移 04h) §

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-6-3"></a>
## 7.9.6.3 Designated Vendor-Specific Header 2 (Offset 08h) | 指定厂商特定包头 2(偏移 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-251 details allocation of register fields in the Designated Vendor-Specific Header 2; § Table 7-228 provides the respective bit definitions.

Vendor-specific software must qualify the DVSEC Vendor ID before attempting to interpret the DVSEC ID field.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-251 详细说明了指定厂商特定包头 2 中各寄存器字段的分配;§ 表 7-228 给出了相应的位定义。

厂商特定软件在尝试解读 DVSEC ID 字段之前,必须先确认 DVSEC Vendor ID。

</td>
</tr>
</tbody>
</table>

---

><!-- 📄 Page 1293 -->
---

> **Figure 7-251.** Designated Vendor-Specific Header 2
> <img src="figures/chapter_07/fig_1293_1_tight.png" width="700">

> **图 7-251.** 指定厂商特定包头 2

**Table 7-228. Designated Vendor-Specific Header 2 | 表 7-228. 指定厂商特定包头 2**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | DVSEC ID - This field is a vendor-defined ID that indicates the nature and format of the DVSEC structure. Software must qualify the DVSEC Vendor ID before interpreting this field. | RO |

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The PCI Express RCRB Header Extended Capability is an optional Extended Capability that may be implemented in an RCRB to provide a Vendor ID and Device ID for the RCRB and to permit the management of parameters that affect the behavior of Root Complex functionality associated with the RCRB.

</td>
<td style="background-color:#e8e8e8">

PCI Express RCRB Header 扩展能力是一种可选的扩展能力,可以在 RCRB 中实现,以便为该 RCRB 提供 Vendor ID 和 Device ID,并允许管理与该 RCRB 关联的根复合体 (Root Complex) 功能行为的参数。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-252.** RCRB Header Extended Capability Structure
> <img src="figures/chapter_07/fig_1293_2_tight.png" width="700">

> **图 7-252.** RCRB Header 扩展能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-253 details allocation of register fields in the RCRB Header Extended Capability Header. § Table 7-229 provides the respective bit definitions. Refer to § Section 7.6.3 for a description of the PCI Express Enhanced Capabilities header. The Extended Capability ID for the RCRB Header Extended Capability is 000Ah.

</td>
<td style="background-color:#e8e8e8">

§ 图 7-253 详细说明了 RCRB Header 扩展能力包头中各寄存器字段的分配;§ 表 7-229 给出了相应的位定义。有关 PCI Express 增强能力包头的描述,请参见 § 第 7.6.3 节。RCRB Header 扩展能力的扩展能力 ID 为 000Ah。

</td>
</tr>
</tbody>
</table>

---

> **Figure 7-253.** RCRB Header Extended Capability Header
> <img src="figures/chapter_07/fig_1293_1.png" width="700">

> **图 7-253.** RCRB Header 扩展能力包头

---

---

<a id="sec-7-9-7"></a>
## 7.9.7 RCRB Header Extended Capability | RCRB 头扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<a id="sec-7-9-7-1-2"></a>
### 7.9.7.1 RCRB Header Extended Capability Header (Offset 00h)

</td>
<td style="background-color:#e8e8e8">

<a id="sec-7-9-7-1"></a>
### 7.9.7.1 RCRB 头扩展能力头（偏移 00h）

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1294 -->
---

**Table 7-229. RCRB Header Extended Capability Header | 表 7-229. RCRB 头扩展能力头**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the RCRB Header Extended Capability is 000Ah. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID（PCI Express 扩展能力 ID）— 该字段是 PCI-SIG 定义的 ID 编号，用于指示扩展能力的性质和格式。RCRB Header Extended Capability 的扩展能力 ID 为 000Ah。 | RO |
| 19:16 | Capability Version（能力版本）— 该字段是 PCI-SIG 定义的版本号，用于指示当前 Capability 结构的版本。本规范版本必须为 1h。 | RO |
| 31:20 | Next Capability Offset（下一能力偏移）— 该字段包含指向下一个 PCI Express Capability 结构的偏移，若链接列表中不存在其他项，则为 000h。对于在配置空间中实现的扩展能力，该偏移相对于 PCI 兼容配置空间的起始位置，因此必须为 000h（表示能力列表终止）或大于 0FFh。 | RO |

Figure 7-254 details allocation of register fields in the RCRB Vendor ID and Device ID register; Table 7-230 provides the respective bit definitions.

图 7-254 详细说明了 RCRB Vendor ID and Device ID 寄存器中寄存器字段的分配；表 7-230 给出了相应的位定义。

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-254.** RCRB Vendor ID and Device ID register
> <img src="figures/chapter_07/fig_1294_1_tight.png" width="700">


**Table 7-230. RCRB Vendor ID and Device ID register | 表 7-230. RCRB Vendor ID and Device ID 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | Vendor ID - PCI-SIG assigned. Analogous to the equivalent field in PCI-compatible Configuration Space. This field provides a means to associate an RCRB with a particular vendor. | RO |
| 31:16 | Device ID - Vendor assigned. Analogous to the equivalent field in PCI-compatible Configuration Space. This field provides a means for a vendor to classify a particular RCRB. | RO |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | Vendor ID（供应商 ID）— 由 PCI-SIG 分配。类似于 PCI 兼容配置空间中的相应字段。该字段提供将 RCRB 与特定供应商相关联的方式。 | RO |
| 31:16 | Device ID（设备 ID）— 由供应商分配。类似于 PCI 兼容配置空间中的相应字段。该字段为供应商提供对特定 RCRB 进行分类的方式。 | RO |

Figure 7-255 details allocation of register fields in the RCRB Capabilities register; Table 7-231 provides the respective bit definitions.

图 7-255 详细说明了 RCRB Capabilities 寄存器中寄存器字段的分配；表 7-231 给出了相应的位定义。

<a id="sec-7-9-7-2-2"></a>
### 7.9.7.2 RCRB Vendor ID and Device ID register (Offset 04h)
### 7.9.7.3 RCRB Capabilities register (Offset 08h)

<a id="sec-7-9-7-2"></a>
### 7.9.7.2 RCRB Vendor ID and Device ID 寄存器（偏移 04h）
### 7.9.7.3 RCRB Capabilities 寄存器（偏移 08h）

<!-- 📄 Page 1295 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-255.** RCRB Capabilities register
> <img src="figures/chapter_07/fig_1295_1_tight.png" width="700">


**Table 7-231. RCRB Capabilities register | 表 7-231. RCRB Capabilities 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 0 | Configuration RRS Software Visibility - When Set, this bit indicates that the Root Complex is capable of returning Request Retry Status (RRS) Completion Status in response to a Configuration Request for all Root Ports and integrated devices associated with this RCRB (see Section 2.3.1). | RO |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 0 | Configuration RRS Software Visibility（配置 RRS 软件可见性）— 置位时，该位表示根复合体（Root Complex）能够针对与该 RCRB 关联的所有根端口（Root Port）和集成设备的配置请求（Configuration Request）返回 Request Retry Status (RRS) 完成状态（参见第 2.3.1 节）。 | RO |

Figure 7-256 details allocation of register fields in the RCRB Control register; Table 7-232 provides the respective bit definitions.

图 7-256 详细说明了 RCRB Control 寄存器中寄存器字段的分配；表 7-232 给出了相应的位定义。

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-256.** RCRB Control register


**Table 7-232. RCRB Control register | 表 7-232. RCRB Control 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 0 | Configuration RRS Software Visibility Enable - When Set, this bit enables the Root Complex to return Request Retry Status (RRS) Completion Status in response to a Configuration Request for all Root Ports and integrated devices associated with this RCRB (see Section 2.3.1). RCRBs that do not implement this capability must hardwire this bit to 0b. Default value of this bit is 0b. | RW |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 0 | Configuration RRS Software Visibility Enable（配置 RRS 软件可见性使能）— 置位时，该位使根复合体能够针对与该 RCRB 关联的所有根端口和集成设备的配置请求返回 Request Retry Status (RRS) 完成状态（参见第 2.3.1 节）。未实现此能力的 RCRB 必须将该位硬连线为 0b。该位的默认值为 0b。 | RW |

The Root Complex Link Declaration Extended Capability is an optional Capability that is permitted to be implemented by Root Ports, RCiEPs, or RCRBs to declare a Root Complex's internal topology.

Root Complex Link Declaration Extended Capability 是一种可选能力，允许由根端口、RCiEP 或 RCRB 实现，以声明根复合体的内部拓扑。

A Root Complex consists of one or more following elements:

根复合体由以下一个或多个元素组成：

- PCI Express Root Port
- A default system Egress Port or an internal sink unit such as memory (represented by an RCRB)
- Internal Data Paths/Links (represented by an RCRB on either side of an internal Link)

- PCI Express 根端口
- 默认系统出口端口或内部汇聚单元（例如内存，由 RCRB 表示）
- 内部数据路径/链路（由内部链路任一侧的 RCRB 表示）

<a id="sec-7-9-7-4-2"></a>
### 7.9.7.4 RCRB Control register (Offset 0Ch)
<a id="sec-7-9-8-2"></a>
## 7.9.8 Root Complex Link Declaration Extended Capability

<a id="sec-7-9-7-4"></a>
### 7.9.7.4 RCRB Control 寄存器（偏移 0Ch）
<a id="sec-7-9-8"></a>
## 7.9.8 Root Complex Link Declaration Extended Capability（根复合体链路声明扩展能力）

<!-- 📄 Page 1296 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

- Integrated devices
- Functions

</td>
<td style="background-color:#e8e8e8">

- 集成设备
- 功能（Function）

</td>
</tr>
</tbody>
</table>

A Root Complex Component is a logical aggregation of the above described Root Complex elements. No single element can be part of more than one Root Complex Component. Each Root Complex Component must have a unique Component ID.

根复合体组件（Root Complex Component）是上述根复合体元素的逻辑聚合。任何单个元素不能属于多个根复合体组件。每个根复合体组件必须具有唯一的 Component ID。

A Root Complex is represented either as an opaque Root Complex or as a collection of one or more Root Complex Components.

根复合体可以表示为不透明的根复合体，或者表示为一个或多个根复合体组件的集合。

The Root Complex Link Declaration Extended Capability is permitted to be present in a Root Complex element's Configuration Space or RCRB. It declares Links from the respective element to other elements of the same Root Complex Component or to an element in another Root Complex Component. The Links are required to be declared bidirectional such that each valid data path from one元素 to another has corresponding Link Entries in the Configuration Space (or RCRB) of both elements.

允许在根复合体元素的配置空间或 RCRB 中出现 Root Complex Link Declaration Extended Capability。它声明从相应元素到同一根复合体组件的其他元素，或到另一个根复合体组件中的元素的链路。链路必须以双向方式声明，使得从一个元素到另一个元素的每个有效数据路径在两个元素的配置空间（或 RCRB）中都具有对应的链路条目。

The Root Complex Link Declaration Extended Capability is permitted to also declare an association between a Configuration Space element (Root Port or RCiEP) and an RCRB Header Extended Capability (see Section 7.9.7) contained in an RCRB that affects the behavior of the Configuration Space element. Note that an RCRB Header association is not declared bidirectional; the association is only declared by the Configuration Space element and not by the target RCRB.

Root Complex Link Declaration Extended Capability 还允许声明配置空间元素（根端口或 RCiEP）与 RCRB 中包含的 RCRB Header Extended Capability（参见第 7.9.7 节）之间的关联，该关联会影响配置空间元素的行为。请注意，RCRB 头关联不声明为双向；该关联仅由配置空间元素声明，而不是由目标 RCRB 声明。

The Root Complex Link Declaration Extended Capability, as shown in Figure 7-257, consists of the PCI Express Extended Capability header and Root Complex Element Self Description followed by one or more Root Complex Link Entries.

如图 7-257 所示，Root Complex Link Declaration Extended Capability 由 PCI Express Extended Capability 头和 Root Complex Element Self Description 组成，后跟一个或多个 Root Complex Link Entry。

**IMPLEMENTATION NOTE:**
**TOPOLOGIES TO AVOID**

Topologies that create more than one data path between any two Root Complex elements (either directly or through other Root Complex elements) may not be able to support bandwidth allocation in a standard manner.

**实现说明：**
**应避免的拓扑**

在任何两个根复合体元素之间（直接或通过其他根复合体元素）创建多个数据路径的拓扑可能无法以标准方式支持带宽分配。

The description of how traffic is routed through such a topology is implementation specific, meaning that general purpose-operating systems may not have enough information about such a topology to correctly support bandwidth allocation. In order to circumvent this problem, these operating systems may require that a single RCRB element (of type Internal Link) not declare more than one Link to a Root Complex Component other than the one containing the RCRB element itself.

关于流量如何通过此类拓扑路由的描述是特定于实现的，这意味着通用操作系统可能没有足够的信息来正确支持带宽分配。为了规避此问题，这些操作系统可能要求单个 RCRB 元素（类型为 Internal Link）不向除包含该 RCRB 元素本身的根复合体组件之外的多个根复合体组件声明多于一条链路。

<!-- 📄 Page 1297 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Extended Capability ID for the Root Complex Link Declaration Extended Capability is 0005h.

</td>
<td style="background-color:#e8e8e8">

Root Complex Link Declaration Extended Capability 的扩展能力 ID 为 0005h。

</td>
</tr>
</tbody>
</table>

> **Figure 7-257.** Root Complex Link Declaration Extended Capability
> <img src="figures/chapter_07/fig_1297_1_tight.png" width="700">


<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-258.** Root Complex Link Declaration Extended Capability Header
> <img src="figures/chapter_07/fig_1297_2_tight.png" width="700">


<a id="sec-7-9-8-1-2"></a>
### 7.9.8.1 Root Complex Link Declaration Extended Capability Header (Offset 00h)

<a id="sec-7-9-8-1"></a>
### 7.9.8.1 Root Complex Link Declaration Extended Capability Header（偏移 00h）

<!-- 📄 Page 1298 -->
---

**Table 7-233. Root Complex Link Declaration Extended Capability Header | 表 7-233. Root Complex Link Declaration Extended Capability Header**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. The Extended Capability ID for the Root Complex Link Declaration Extended Capability is 0005h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. The bottom 2 bits of this offset are Reserved and must be implemented as 00b although software must mask them to allow for future uses of these bits. | RO |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID（PCI Express 扩展能力 ID）— 该字段是 PCI-SIG 定义的 ID 编号，用于指示扩展能力的性质和格式。Root Complex Link Declaration Extended Capability 的扩展能力 ID 为 0005h。 | RO |
| 19:16 | Capability Version（能力版本）— 该字段是 PCI-SIG 定义的版本号，用于指示当前 Capability 结构的版本。本规范版本必须为 1h。 | RO |
| 31:20 | Next Capability Offset（下一能力偏移）— 该字段包含指向下一个 PCI Express Capability 结构的偏移，若链接列表中不存在其他项，则为 000h。对于在配置空间中实现的扩展能力，该偏移相对于 PCI 兼容配置空间的起始位置，因此必须为 000h（表示能力列表终止）或大于 0FFh。该偏移的低 2 位为保留位，必须实现为 00b，但软件必须将其屏蔽以允许将来使用这些位。 | RO |

The Element Self Description Register provides information about the Root Complex element containing the Root Complex Link Declaration Extended Capability.

Element Self Description 寄存器提供关于包含 Root Complex Link Declaration Extended Capability 的根复合体元素的信息。

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-259.** Element Self Description Register
> <img src="figures/chapter_07/fig_1298_1_tight.png" width="700">


**Table 7-234. Element Self Description Register | 表 7-234. Element Self Description 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 3:0 | Element Type - This field indicates the type of the Root Complex Element. Defined encodings are: <br>0h = Configuration Space Element <br>1h = System Egress Port or internal sink (memory) <br>2h = Internal Root Complex Link <br>3h-Fh = Reserved | RO |
| 15:8 | Number of Link Entries - This field indicates the number of Link Entries following the Element Self Description. This field must report a value of 01h or higher. | HwInit |
| 23:16 | Component ID - This field identifies the Root Complex Component that contains this Root Complex Element. Component IDs must start at 01h, as a value of 00h is Reserved. | HwInit |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 3:0 | Element Type（元素类型）— 该字段指示根复合体元素的类型。已定义的编码为：<br>0h = Configuration Space Element（配置空间元素）<br>1h = System Egress Port or internal sink (memory)（系统出口端口或内部汇聚单元，如内存）<br>2h = Internal Root Complex Link（内部根复合体链路）<br>3h-Fh = Reserved（保留） | RO |
| 15:8 | Number of Link Entries（链路条目数）— 该字段指示紧随 Element Self Description 之后的链路条目数。该字段必须报告为 01h 或更高的值。 | HwInit |
| 23:16 | Component ID（组件 ID）— 该字段标识包含此根复合体元素的根复合体组件。Component ID 必须从 01h 开始，因为值 00h 为保留值。 | HwInit |

<a id="sec-7-9-8-2-2"></a>
### 7.9.8.2 Element Self Description Register (Offset 04h)

<a id="sec-7-9-8-2"></a>
### 7.9.8.2 Element Self Description 寄存器（偏移 04h）

<!-- 📄 Page 1299 -->
---

**Table 7-234 (cont.). Element Self Description Register | 表 7-234（续）. Element Self Description 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 31:24 | Port Number - This field specifies the Port Number associated with this element with respect to the Root Complex Component that contains this element. An element with a Port Number of 00h indicates the default Egress Port to configuration software. | HwInit |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 31:24 | Port Number（端口号）— 该字段指定与此元素关联的端口号，相对于包含此元素的根复合体组件。Port Number 为 00h 的元素表示对配置软件的默认出口端口（Egress Port）。 | HwInit |

Link Entries start at offset 10h of the Root Complex Link Declaration Extended Capability structure. Each Link Entry consists of a Link description followed by a 64-bit Link Address at offset 08h from the start of Link Entry identifying the target element for the declared Link. A Link Entry declares an internal Link to another Root Complex Element.

链路条目从 Root Complex Link Declaration Extended Capability 结构的偏移 10h 开始。每个 Link Entry 由一个 Link description 组成，后跟位于 Link Entry 起始处偏移 08h 处的 64 位 Link Address，用于标识所声明链路的目标元素。Link Entry 声明到另一个根复合体元素的内部链路。

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Link Description Register is located at offset 00h from the start of a Link Entry and is defined as follows:

</td>
<td style="background-color:#e8e8e8">

Link Description 寄存器位于 Link Entry 起始处的偏移 00h 处，定义如下：

</td>
</tr>
</tbody>
</table>

> **Figure 7-260.** Link Entry
> <img src="figures/chapter_07/fig_1299_1_tight.png" width="700">


<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-261.** Link Description Register
> <img src="figures/chapter_07/fig_1299_2_tight.png" width="700">


**Table 7-235. Link Description Register | 表 7-235. Link Description 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 0 | Link Valid - When Set, this bit indicates that the Link Entry specifies a valid Link. Link Entries that do not have either this bit Set or the Associate RCRB Header bit Set (or both) are ignored by software. | HwInit |
| 1 | Link Type - This bit indicates the target type of the Link and defines the format of the Link Address field. Defined Link Type values are: | HwInit |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 0 | Link Valid（链路有效）— 置位时，该位表示 Link Entry 指定有效链路。未设置该位或 Associate RCRB Header 位（或两者均未设置）的 Link Entries 将被软件忽略。 | HwInit |
| 1 | Link Type（链路类型）— 该位指示链路的目标类型，并定义 Link Address 字段的格式。已定义的 Link Type 值为： | HwInit |

<a id="sec-7-9-8-3-2"></a>
### 7.9.8.3 Link Entries
<a id="sec-7-9-8-3-1-2"></a>
#### 7.9.8.3.1 Link Description Register

<a id="sec-7-9-8-3"></a>
### 7.9.8.3 Link Entries（链路条目）
<a id="sec-7-9-8-3-1"></a>
#### 7.9.8.3.1 Link Description 寄存器

<!-- 📄 Page 1300 -->
---

**Table 7-235 (cont.). Link Description Register | 表 7-235（续）. Link Description 寄存器**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 1 (0b) | Link points to memory-mapped space 183 (for RCRB). The Link Address specifies the 64-bit base address of the target RCRB. | HwInit |
| 1 (1b) | Link points to Configuration Space (for a Root Port or RCiEP). The Link Address specifies the configuration address (PCI Segment Group, Bus, Device, Function) of the target element. | HwInit |
| 2 | Associate RCRB Header - When Set, this bit indicates that the Link Entry associates the declaring element with an RCRB Header Extended Capability in the target RCRB. Link Entries that do not have either this bit Set or the Link Valid bit Set (or both) are ignored by software. The Link Type bit must be Clear when this bit is Set. | HwInit |
| 23:16 | Target Component ID - This field identifies the Root Complex Component that is targeted by this Link Entry. Components IDs must start at 01h, as a value of 00h is Reserved. | HwInit |
| 31:24 | Target Port Number - This field specifies the Port Number associated with the element targeted by this Link Entry; the Target Port Number is with respect to the Root Complex Component (identified by the Target Component ID) that contains the target element. | HwInit |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 1 (0b) | 链路指向内存映射空间 183（用于 RCRB）。Link Address 指定目标 RCRB 的 64 位基址。 | HwInit |
| 1 (1b) | 链路指向配置空间（用于根端口或 RCiEP）。Link Address 指定目标元素的配置地址（PCI Segment Group、Bus、Device、Function）。 | HwInit |
| 2 | Associate RCRB Header（关联 RCRB 头）— 置位时，该位表示 Link Entry 将声明元素与目标 RCRB 中的 RCRB Header Extended Capability 相关联。未设置该位或 Link Valid 位（或两者均未设置）的 Link Entries 将被软件忽略。当该位置位时，Link Type 位必须清零。 | HwInit |
| 23:16 | Target Component ID（目标组件 ID）— 该字段标识此 Link Entry 所指向的根复合体组件。Component ID 必须从 01h 开始，因为值 00h 为保留值。 | HwInit |
| 31:24 | Target Port Number（目标端口号）— 该字段指定与此 Link Entry 所指向元素关联的端口号；Target Port Number 相对于包含目标元素的根复合体组件（由 Target Component ID 标识）。 | HwInit |

The Link Address is a HwInit field located at offset 08h from the start of a Link Entry that identifies the target element for the Link Entry. For a Link of Link Type 0 in its Link Description, the Link Address specifies the memory-mapped base address of RCRB. For a Link of Link Type 1 in its Link Description, the Link Address specifies the Configuration Space address of a PCI Express Root Port or an RCiEP.

Link Address 是一个 HwInit 字段，位于 Link Entry 起始处偏移 08h 处，用于标识 Link Entry 的目标元素。对于其 Link Description 中 Link Type 为 0 的链路，Link Address 指定 RCRB 的内存映射基址。对于其 Link Description 中 Link Type 为 1 的链路，Link Address 指定 PCI Express 根端口或 RCiEP 的配置空间地址。

For a Link pointing to a memory-mapped RCRB (Link Type bit = 0), the first DWORD specifies the lower 32 bits of the RCRB base address of the target element as shown below; bits 11:0 are hardwired to 000h and Reserved for future use. The second DWORD specifies the high order 32 bits (63:32) of the RCRB base address of the target element.

对于指向内存映射 RCRB 的链路（Link Type 位 = 0），如下图所示，第一个 DWORD 指定目标元素的 RCRB 基址的低 32 位；位 11:0 硬连线为 000h 并保留以供将来使用。第二个 DWORD 指定目标元素的 RCRB 基址的高 32 位（63:32）。

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-262.** Link Address for Link Type 0
> <img src="figures/chapter_07/fig_1300_1_tight.png" width="700">


For a Link pointing to the Configuration Space of a Root Complex element (Link Type bit = 1), bits in the first DWORD specify the Bus, Device, and Function Number of the target element. As shown in Figure 7-263, bits 2:0 (N) encode the number of bits n associated with the Bus Number, with N = 000b specifying n = 8 and all other encodings specifying

<a id="sec-7-9-8-3-2-2"></a>
#### 7.9.8.3.2 Link Address
<a id="sec-7-9-8-3-2-1-2"></a>
##### 7.9.8.3.2.1 Link Address for Link Type 0
<a id="sec-7-9-8-3-2-2-2"></a>
##### 7.9.8.3.2.2 Link Address for Link Type 1

对于指向根复合体元素配置空间的链路（Link Type 位 = 1），第一个 DWORD 中的位指定目标元素的 Bus、Device 和 Function Number。如图 7-263 所示，位 2:0（N）编码与 Bus Number 关联的位数 n，其中 N = 000b 指定 n = 8，所有其他编码指定

<a id="sec-7-9-8-3-2"></a>
#### 7.9.8.3.2 Link Address（链路地址）
<a id="sec-7-9-8-3-2-1"></a>
##### 7.9.8.3.2.1 Link Type 0 的 Link Address
<a id="sec-7-9-8-3-2-2"></a>
##### 7.9.8.3.2.2 Link Type 1 的 Link Address

> 183. The memory-mapped space for accessing an RCRB is not the same as Memory Space, and must not overlap with Memory Space.
> 183. 用于访问 RCRB 的内存映射空间与 Memory Space 不同，且不得与 Memory Space 重叠。

<!-- 📄 Page 1301 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

n = <value of N>. Bits 11:3 are Reserved and hardwired to 0. Bits 14:12 specify the Function Number, and bits 19:15 specify the Device Number. Bits (19 + n):20 specify the Bus Number, with 1 ≤ n ≤ 8.

Bits 31:(20 + n) of the first DWORD together with the second DWORD optionally identify the target element's hierarchy for systems implementing the PCI Express Enhanced Configuration Access Mechanism by specifying bits 63:(20 + n) of the memory-mapped Configuration Space base address of the PCI Express hierarchy associated with the targeted element; single hierarchy systems that do not implement more than one memory mapped Configuration Space are allowed to report a value of zero to indicate default Configuration Space.

A Configuration Space base address [63:(20 + n)] equal to zero indicates that the Configuration Space address defined by bits (19 + n):12 (Bus Number, Device Number, and Function Number) exists in the default PCI Segment Group; any non-zero value indicates a separate Configuration Space base address.

Software must not use n outside the context of evaluating the Bus Number and memory-mapped Configuration Space base address for this specific target element. In particular, n does not necessarily indicate the maximum Bus Number supported by the associated PCI Segment Group.

</td>
<td style="background-color:#e8e8e8">

n = <N 的值>。位 11:3 为保留位，硬连线为 0。位 14:12 指定 Function Number，位 19:15 指定 Device Number。位 (19 + n):20 指定 Bus Number，其中 1 ≤ n ≤ 8。

第一个 DWORD 的位 31:(20 + n) 与第二个 DWORD 一起，通过指定与目标元素关联的 PCI Express 层级（hierarchy）的内存映射配置空间基址的位 63:(20 + n)，可选地标识目标元素的层级（对于实现 PCI Express Enhanced Configuration Access Mechanism 的系统）；不实现多于一个内存映射配置空间的单层级系统允许报告零值以表示默认配置空间。

等于零的 Configuration Space 基址 [63:(20 + n)] 表示由位 (19 + n):12（Bus Number、Device Number 和 Function Number）定义的配置空间地址存在于默认 PCI Segment Group 中；任何非零值都表示单独的 Configuration Space 基址。

软件不得在评估此特定目标元素的 Bus Number 和内存映射配置空间基址的上下文之外使用 n。特别地，n 不一定表示关联 PCI Segment Group 支持的最大 Bus Number。

</td>
</tr>
</tbody>
</table>
</div>


<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-263.** Link Address for Link Type 1
> <img src="figures/chapter_07/fig_1301_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

**Table 7-236. Link Address for Link Type 1 | 表 7-236. Link Type 1 的 Link Address**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 2:0 | N - Encoded number of Bus Number bits | HwInit |
| 14:12 | Function Number | HwInit |
| 19:15 | Device Number | HwInit |
| (19 + n):20 | Bus Number | HwInit |
| 63:(20 + n) | PCI Express Configuration Space Base Address (1 ≤ n ≤ 8) <br> **Note:** A Root Complex that does not implement multiple Configuration Spaces is allowed to report this field as 0. | HwInit |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 2:0 | N — Bus Number 位数的编码值 | HwInit |
| 14:12 | Function Number（功能号） | HwInit |
| 19:15 | Device Number（设备号） | HwInit |
| (19 + n):20 | Bus Number（总线号） | HwInit |
| 63:(20 + n) | PCI Express Configuration Space Base Address（PCI Express 配置空间基址）（1 ≤ n ≤ 8）<br>**注：** 不实现多个 Configuration Space 的根复合体允许将该字段报告为 0。 | HwInit |

The Root Complex Internal Link Control Extended Capability is an optional Capability that controls an internal Root Complex Link between two distinct Root Complex Components. This Capability is valid for RCRBs that declare an Element Type field as Internal Root Complex Link in the Element Self-Description register of the Root Complex Link Declaration Capability structure.

Root Complex Internal Link Control Extended Capability 是一种可选能力，用于控制两个不同根复合体组件之间的内部根复合体链路。此能力对于在 Root Complex Link Declaration Capability 结构的 Element Self-Description 寄存器中将 Element Type 字段声明为 Internal Root Complex Link 的 RCRB 有效。

The Root Complex Internal Link Control Extended Capability structure is defined as shown in Figure 7-264.

Root Complex Internal Link Control Extended Capability 结构定义如图 7-264 所示。

<a id="sec-7-9-9-2"></a>
## 7.9.9 Root Complex Internal Link Control Extended Capability

<a id="sec-7-9-9"></a>
## 7.9.9 Root Complex Internal Link Control Extended Capability（根复合体内部链路控制扩展能力）

<!-- 📄 Page 1302 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Extended Capability ID for the Root Complex Internal Link Control Extended Capability is 0006h.

</td>
<td style="background-color:#e8e8e8">

Root Complex Internal Link Control Extended Capability 的扩展能力 ID 为 0006h。

</td>
</tr>
</tbody>
</table>

> **Figure 7-264.** Root Complex Internal Link Control Extended Capability
> <img src="figures/chapter_07/fig_1302_1_tight.png" width="700">


<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-265.** Root Complex Internal Link Control Extended Capability Header
> <img src="figures/chapter_07/fig_1302_2_tight.png" width="700">


**Table 7-237. Root Complex Internal Link Control Extended Capability Header | 表 7-237. Root Complex Internal Link Control Extended Capability Header**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. The Extended Capability ID for the Root Complex Internal Link Control Extended Capability is 0006h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. The bottom 2 bits of this offset are Reserved and must be implemented as 00b although software must mask them to allow for future uses of these bits. | RO |

| Bit Location | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID（PCI Express 扩展能力 ID）— 该字段是 PCI-SIG 定义的 ID 编号，用于指示扩展能力的性质和格式。Root Complex Internal Link Control Extended Capability 的扩展能力 ID 为 0006h。 | RO |
| 19:16 | Capability Version（能力版本）— 该字段是 PCI-SIG 定义的版本号，用于指示当前 Capability 结构的版本。本规范版本必须为 1h。 | RO |
| 31:20 | Next Capability Offset（下一能力偏移）— 该字段包含指向下一个 PCI Express Capability 结构的偏移，若链接列表中不存在其他项，则为 000h。对于在配置空间中实现的扩展能力，该偏移相对于 PCI 兼容配置空间的起始位置，因此必须为 000h（表示能力列表终止）或大于 0FFh。该偏移的低 2 位为保留位，必须实现为 00b，但软件必须将其屏蔽以允许将来使用这些位。 | RO |

The Root Complex Link Capabilities Register identifies capabilities for this Link.

Root Complex Link Capabilities 寄存器标识此链路的能力。

---

<a id="sec-7-9-9-1"></a>
## 7.9.9.1 Root Complex Internal Link Control Extended Capability Header (Offset 00h) | 根复合体内部链路控制扩展能力头(偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Root Complex Internal Link Control Extended Capability Header

</td>
<td style="background-color:#e8e8e8">

根复合体 (Root Complex) 内部链路控制扩展能力头

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-9-2"></a>
## 7.9.9.2 Root Complex Link Capabilities Register (Offset 04h) | 根复合体链路能力寄存器(偏移量 04h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0001b
0010b
0011b
0100b
0101b
0110b
0111b
Others
00 0001b
00 0010b
00 0100b
00 1000b
01 0000b
00b
01b
10b
11b
0
3
Max Link Speed
4
9
Maximum Link Width
10
11
Active State Power Management (ASPM) Support
12
14
L0s Exit Latency
15
17
L1 Exit Latency
18
24
Supported Link Speeds Vector
25
31
RsvdP
Figure 7-266 Root Complex Link Capabilities Register
Table 7-238 Root Complex Link Capabilities Register
Bit Location
Register Description
Attributes
3:0
Max Link Speed - This field indicates the maximum Link speed of the associated Link.
The encoded value specifies a bit location in the Supported Link Speeds Vector (in the Root Complex
Link Capabilities Register) that corresponds to the maximum Link speed.
Defined encodings are:
Supported Link Speeds Vector field bit 0
Supported Link Speeds Vector field bit 1
Supported Link Speeds Vector field bit 2
Supported Link Speeds Vector field bit 3
Supported Link Speeds Vector field bit 4
Supported Link Speeds Vector field bit 5
Supported Link Speeds Vector field bit 6
All other encodings are reserved.
A Root Complex that does not support this feature must report 0000b in this field.
RO
9:4
Maximum Link Width - This field indicates the maximum width of the given Link.
Defined encodings are:
x1
x2
x4
x8
x16
All other encodings are Reserved. A Root Complex that does not support this feature must report
00 0000b in this field.
RO
11:10
Active State Power Management (ASPM) Support - This field indicates the level of ASPM supported on
the given Link.
Defined encodings are:
No ASPM Support
L0s Supported
L1 Supported
L0s and L1 Supported
RO

</td>
<td style="background-color:#e8e8e8">

0001b
0010b
0011b
0100b
0101b
0110b
0111b
其他(保留)
00 0001b
00 0010b
00 0100b
00 1000b
01 0000b
00b
01b
10b
11b
0
3
Max Link Speed(最大链路速度)
4
9
Maximum Link Width(最大链路宽度)
10
11
Active State Power Management (ASPM) Support(主动状态电源管理支持)
12
14
L0s Exit Latency(L0s 退出延迟)
15
17
L1 Exit Latency(L1 退出延迟)
18
24
Supported Link Speeds Vector(支持的链路速度向量)
25
31
RsvdP
图 7-266 Root Complex Link Capabilities Register(根复合体链路能力寄存器)
表 7-238 Root Complex Link Capabilities Register(根复合体链路能力寄存器)
位位置
寄存器描述
属性
3:0
Max Link Speed(最大链路速度) — 该字段指示关联链路 (Link) 的最大链路速度。
编码值指定 Supported Link Speeds Vector(支持的链路速度向量,位于 Root Complex Link Capabilities Register 中)中与最大链路速度对应的位位置。
已定义的编码为:
Supported Link Speeds Vector 字段位 0
Supported Link Speeds Vector 字段位 1
Supported Link Speeds Vector 字段位 2
Supported Link Speeds Vector 字段位 3
Supported Link Speeds Vector 字段位 4
Supported Link Speeds Vector 字段位 5
Supported Link Speeds Vector 字段位 6
所有其他编码为保留。
不支持此特性的根复合体 (Root Complex) 必须在该字段中报告 0000b。
RO
9:4
Maximum Link Width(最大链路宽度) — 该字段指示给定链路 (Link) 的最大宽度。
已定义的编码为:
x1
x2
x4
x8
x16
所有其他编码为保留。不支持此特性的根复合体必须在该字段中报告 00 0000b。
RO
11:10
Active State Power Management (ASPM) Support(主动状态电源管理支持) — 该字段指示给定链路上所支持的 ASPM 等级。
已定义的编码为:
No ASPM Support(不支持 ASPM)
L0s Supported(支持 L0s)
L1 Supported(支持 L1)
L0s and L1 Supported(支持 L0s 和 L1)
RO

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1304 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

000b
001b
010b
011b
100b
101b
110b
111b
000b
001b
010b
011b
100b
101b
110b
111b
Bit 0
Bit 1
Bit 2
Bit 3
Bit 4
Bit 5
Bit 6
Bit Location
Register Description
Attributes
14:12
L0s Exit Latency - This field indicates the L0s exit latency for the given Link. The value reported indicates
the length of time this Port requires to complete transition from L0s to L0. If L0s is not supported, the
value is undefined.
Defined encodings are:
Less than 64 ns
64 ns to less than 128 ns
128 ns to less than 256 ns
256 ns to less than 512 ns
512 ns to less than 1 μs
1 μs to less than 2 μs
2 μs to 4 μs
More than 4 μs
RO
17:15
L1 Exit Latency - This field indicates the L1 exit latency for the given Link. The value reported indicates
the length of time this Port requires to complete transition from ASPM L1 to L0. If ASPM L1 is not
supported, the value is undefined.
Defined encodings are:
Less than 1 μs
1 μs to less than 2 μs
2 μs to less than 4 μs
4 μs to less than 8 μs
8 μs to less than 16 μs
16 μs to less than 32 μs
32 μs to 64 μs
More than 64 μs
RO
24:18
Supported Link Speeds Vector - This field indicates the supported Link speed(s) of the associated Link.
For each bit, a value of 1b indicates that the corresponding Link speed is supported; otherwise, the Link
speed is not supported. See § Section 8.2.1 for further requirements.
Bit definitions within this field are:
2.5 GT/s
5.0 GT/s
8.0 GT/s
16.0 GT/s
32.0 GT/s
64.0 GT/s
RsvdP
RO

</td>
<td style="background-color:#e8e8e8">

000b
001b
010b
011b
100b
101b
110b
111b
000b
001b
010b
011b
100b
101b
110b
111b
位 0
位 1
位 2
位 3
位 4
位 5
位 6
位位置
寄存器描述
属性
14:12
L0s Exit Latency(L0s 退出延迟) — 该字段指示给定链路的 L0s 退出延迟。所报告的值表示此端口 (Port) 完成从 L0s 到 L0 转换所需的时间长度。如果不支持 L0s,则该值未定义。
已定义的编码为:
小于 64 ns
64 ns 至小于 128 ns
128 ns 至小于 256 ns
256 ns 至小于 512 ns
512 ns 至小于 1 μs
1 μs 至小于 2 μs
2 μs 至 4 μs
大于 4 μs
RO
17:15
L1 Exit Latency(L1 退出延迟) — 该字段指示给定链路的 L1 退出延迟。所报告的值表示此端口完成从 ASPM L1 到 L0 转换所需的时间长度。如果不支持 ASPM L1,则该值未定义。
已定义的编码为:
小于 1 μs
1 μs 至小于 2 μs
2 μs 至小于 4 μs
4 μs 至小于 8 μs
8 μs 至小于 16 μs
16 μs 至小于 32 μs
32 μs 至 64 μs
大于 64 μs
RO
24:18
Supported Link Speeds Vector(支持的链路速度向量) — 该字段指示关联链路所支持的链路速度。对于每一位,值为 1b 表示支持相应的链路速度;否则表示不支持该链路速度。更多要求请参见 § 第 8.2.1 节。
该字段内的位定义如下:
2.5 GT/s
5.0 GT/s
8.0 GT/s
16.0 GT/s
32.0 GT/s
64.0 GT/s
RsvdP
RO

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1305 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Root Complex Link Control Register controls parameters for this internal Link.
0
1
Active State Power Management (ASPM) Control
2
6
RsvdP
7
Extended Synch
8
15
RsvdP
Figure 7-267 Root Complex Link Control Register
IMPLEMENTATION NOTE:
SUPPORTED LINK SPEEDS WITH EARLIER HARDWARE
Hardware components compliant to versions prior to the [PCIe-3.0] did not implement the Supported Link
Speeds Vector field and instead returned 0000 000b in bits 24:18.
For software to determine the supported Link speeds for components where this field is contains 0000 000b,
software can read bits 3:0 of the Root Complex Link Capabilities Register (now defined to be the Max Link Speed
field), and interpret the value as follows:
0001b
2.5 GT/s Link speed supported
0010b
5.0 GT/s and 2.5 GT/s Link speeds supported
For such components, the same encoding is also used for the values for the Current Link Speed field (in the Root
Complex Link Status Register).

</td>
<td style="background-color:#e8e8e8">

Root Complex Link Control Register(根复合体链路控制寄存器)控制此内部链路的参数。
0
1
Active State Power Management (ASPM) Control(主动状态电源管理控制)
2
6
RsvdP
7
Extended Synch(扩展同步)
8
15
RsvdP
图 7-267 Root Complex Link Control Register(根复合体链路控制寄存器)
实现注意事项:
早期硬件支持的链路速度
符合 [PCIe-3.0] 之前版本的硬件组件未实现 Supported Link Speeds Vector(支持的链路速度向量)字段,而是在位 24:18 返回 0000 000b。
对于该字段包含 0000 000b 的组件,软件可读取 Root Complex Link Capabilities Register(根复合体链路能力寄存器,现定义为 Max Link Speed 字段)的位 3:0,并按下表解释其值:
0001b
支持 2.5 GT/s 链路速度
0010b
支持 5.0 GT/s 和 2.5 GT/s 链路速度
对于此类组件,相同的编码也用于 Root Complex Link Status Register(根复合体链路状态寄存器)中 Current Link Speed 字段的值。

</td>
</tr>
</tbody>
</table>
</div>


---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

IMPLEMENTATION NOTE:
SOFTWARE MANAGEMENT OF LINK SPEEDS WITH FUTURE
HARDWARE
It is strongly encouraged that software primarily utilize the Supported Link Speeds Vector instead of the Max Link
Speed field, so that software can determine the exact set of supported speeds on current and future hardware.
This can avoid software being confused if a future specification defines Links that do not require support for all
slower speeds.

</td>
<td style="background-color:#e8e8e8">

实现注意事项:
未来硬件的链路速度软件管理
强烈建议软件主要使用 Supported Link Speeds Vector(支持的链路速度向量)而非 Max Link Speed(最大链路速度)字段,以便软件能够在当前和未来硬件上确定所支持速度的精确集合。这可以避免在未来规范定义了不需要支持所有较慢速度的链路时,软件产生混淆。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-9-3"></a>
## 7.9.9.3 Root Complex Link Control Register (Offset 08h) | 根复合体链路控制寄存器(偏移量 08h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

00b
01b
10b
11b
Table 7-239 Root Complex Link Control Register
Bit Location
Register Description
Attributes
1:0
Active State Power Management (ASPM) Control - This field controls the level of ASPM enabled on the
given Link.
Defined encodings are:
Disabled
L0s Entry Enabled
L1 Entry Enabled
L0s and L1 Entry Enabled
Note: "L0s Entry Enabled" enables the Transmitter to enter L0s. If L0s is supported, the Receiver must be
capable of entering L0s even when the Transmitter is disabled from entering L0s (00b or 10b).
In Flit Mode, L0s is not supported, bit 0 of this field is ignored and has no effect (i.e., encodings 01b and
00b are equivalent as are encodings 11b and 10b).
Default value of this field is implementation specific.
Software must not enable L0s in either direction on a given Link unless components on both sides of the
Link each support L0s, as indicated by their ASPM Support field values. Otherwise, the result is
undefined.
ASPM L1 must be enabled by software in the Upstream component on a Link prior to enabling ASPM L1
in the Downstream component on that Link. When disabling ASPM L1, software must disable ASPM L1 in
the Downstream component on a Link prior to disabling ASPM L1 in the Upstream component on that
Link. ASPM L1 must only be enabled on the Downstream component if both components on a Link
support ASPM L1.
A Root Complex that does not support this feature for the given internal Link must hardwire this field to
00b.
RW
7
Extended Synch - This bit when Set forces the transmission of additional Ordered Sets when exiting the
L0s state (see § Section 4.2.5.6 ) and when in the Recovery state (see § Section 4.2.7.4.1 ). This mode
provides external devices (e.g., logic analyzers) monitoring the Link time to achieve bit and Symbol lock
before the Link enters the L0 state and resumes communication.
A Root Complex that does not support this feature for the given internal Link must hardwire this bit to
0b.
In Flit Mode, this bit is ignored and has no effect since L0s is not supported.
Default value for this bit is 0b.
RW

</td>
<td style="background-color:#e8e8e8">

00b
01b
10b
11b
表 7-239 Root Complex Link Control Register(根复合体链路控制寄存器)
位位置
寄存器描述
属性
1:0
Active State Power Management (ASPM) Control(主动状态电源管理控制) — 该字段控制给定链路上启用的 ASPM 等级。
已定义的编码为:
Disabled(禁用)
L0s Entry Enabled(允许进入 L0s)
L1 Entry Enabled(允许进入 L1)
L0s and L1 Entry Enabled(允许进入 L0s 和 L1)
注:"L0s Entry Enabled"(允许进入 L0s)使发送器 (Transmitter) 能够进入 L0s。如果支持 L0s,则即使发送器被禁止进入 L0s(00b 或 10b),接收器 (Receiver) 也必须能够进入 L0s。
在 Flit 模式下,不支持 L0s,该字段的位 0 被忽略且无效(即编码 01b 与 00b 等效,编码 11b 与 10b 等效)。
该字段的默认值是实现特定的。
除非链路上两侧的组件均支持 L0s(如其 ASPM Support 字段值所示),否则软件不得在任何方向上的给定链路上启用 L0s。否则结果未定义。
软件必须先在链路的上游组件 (Upstream component) 启用 ASPM L1,然后才能在该链路的下游组件 (Downstream component) 启用 ASPM L1。禁用 ASPM L1 时,软件必须先在该链路的下游组件禁用 ASPM L1,然后才能在该链路的上游组件禁用 ASPM L1。仅当链路上的两个组件均支持 ASPM L1 时,才允许在下游组件上启用 ASPM L1。
对于给定内部链路不支持此特性的根复合体,必须将该字段硬连线 (hardwire) 为 00b。
RW
7
Extended Synch(扩展同步) — 该位置位 (Set) 时,强制在退出 L0s 状态(见 § 第 4.2.5.6 节)和处于 Recovery(恢复)状态(见 § 第 4.2.7.4.1 节)时传输额外的有序集 (Ordered Sets)。此模式为监控链路的外部设备(例如逻辑分析仪)提供在链路进入 L0 状态并恢复通信之前实现位和符号锁定的时间。
对于给定内部链路不支持此特性的根复合体,必须将该位硬连线为 0b。
在 Flit 模式下,该位被忽略且无效,因为不支持 L0s。
该位的默认值为 0b。
RW

</td>
</tr>
</tbody>
</table>
</div>


---

<a id="sec-7-9-9-4"></a>
## 7.9.9.4 Root Complex Link Status Register (Offset 0Ah) | 根复合体链路状态寄存器(偏移量 0Ah)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Root Complex Link Status Register provides information about Link specific parameters.

</td>
<td style="background-color:#e8e8e8">

Root Complex Link Status Register(根复合体链路状态寄存器)提供有关链路特定参数的信息。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1307 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0001b
0010b
0011b
0100b
0101b
0110b
0111b
00 0001b
00 0010b
00 0100b
00 1000b
01 0000b
0
3
Current Link Speed
4
9
Negotiated Link Width
10
15
RsvdZ
Figure 7-268 Root Complex Link Status Register
Table 7-240 Root Complex Link Status Register
Bit Location
Register Description
Attributes
3:0
Current Link Speed - This field indicates the negotiated Link speed of the given Link.
The encoded value specifies a bit location in the Supported Link Speeds Vector (in the Root Complex
Link Capabilities Register) that corresponds to the current Link speed.
Defined encodings are:
Supported Link Speeds Vector field bit 0
Supported Link Speeds Vector field bit 1
Supported Link Speeds Vector field bit 2
Supported Link Speeds Vector field bit 3
Supported Link Speeds Vector field bit 4
Supported Link Speeds Vector field bit 5
Supported Link Speeds Vector field bit 6
All other encodings are Reserved.
The value in this field is undefined when the Link is not up. A Root Complex that does not support this
feature must report 0000b in this field.
RO
9:4
Negotiated Link Width - This field indicates the negotiated width of the given Link. This includes the
Link Width determined during initial link training as well changes that occur after initial link training
(e.g., L0p)
Defined encodings are:
x1
x2
x4
x8
x16
All other encodings are Reserved. The value in this field is undefined when the Link is not up. A Root
Complex that does not support this feature must hardwire this field to 00 0000b.
RO

</td>
<td style="background-color:#e8e8e8">

0001b
0010b
0011b
0100b
0101b
0110b
0111b
00 0001b
00 0010b
00 0100b
00 1000b
01 0000b
0
3
Current Link Speed(当前链路速度)
4
9
Negotiated Link Width(协商链路宽度)
10
15
RsvdZ
图 7-268 Root Complex Link Status Register(根复合体链路状态寄存器)
表 7-240 Root Complex Link Status Register(根复合体链路状态寄存器)
位位置
寄存器描述
属性
3:0
Current Link Speed(当前链路速度) — 该字段指示给定链路的协商后链路速度。
编码值指定 Supported Link Speeds Vector(支持的链路速度向量,位于 Root Complex Link Capabilities Register 中)中与当前链路速度对应的位位置。
已定义的编码为:
Supported Link Speeds Vector 字段位 0
Supported Link Speeds Vector 字段位 1
Supported Link Speeds Vector 字段位 2
Supported Link Speeds Vector 字段位 3
Supported Link Speeds Vector 字段位 4
Supported Link Speeds Vector 字段位 5
Supported Link Speeds Vector 字段位 6
所有其他编码为保留。
当链路未建立时,该字段中的值未定义。不支持此特性的根复合体必须在该字段中报告 0000b。
RO
9:4
Negotiated Link Width(协商链路宽度) — 该字段指示给定链路的协商后宽度。这包括初始链路训练期间确定的链路宽度以及初始链路训练之后发生的更改(例如 L0p)。
已定义的编码为:
x1
x2
x4
x8
x16
所有其他编码为保留。当链路未建立时,该字段中的值未定义。不支持此特性的根复合体必须将该字段硬连线为 00 0000b。
RO

</td>
</tr>
</tbody>
</table>
</div>


---

<a id="sec-7-9-10"></a>
## 7.9.10 Root Complex Event Collector Endpoint Association Extended Capability | 根复合体事件收集器端点关联扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Root Complex Event Collector Endpoint Association Extended Capability is implemented by Root Complex Event
Collectors. It declares the RCiEPs supported by the Root Complex Event Collector. A Root Complex Event Collector must
implement the Root Complex Event Collector Endpoint Association Extended Capability; no other PCI Express Device
Function is permitted to implement this Capability.
The Root Complex Event Collector Endpoint Association Extended Capability, as shown in § Figure 7-269, consists of the
PCI Express Extended Capability header followed by a DWORD bitmap enumerating RCiEPs on the same Bus, and
optionally an additional range of Bus Numbers that may contain RCiEPs associated with the Root Complex Event
Collector. Functions other than RCiEPs (e.g., Root Ports) contained in the range described by this Capability are not
associated with this Root Complex Event Collector.

</td>
<td style="background-color:#e8e8e8">

Root Complex Event Collector Endpoint Association Extended Capability(根复合体事件收集器端点关联扩展能力)由 Root Complex Event Collector(根复合体事件收集器)实现。它声明该根复合体事件收集器所支持的 RCiEP(RCiEP, Root Complex integrated Endpoint)。根复合体事件收集器必须实现 Root Complex Event Collector Endpoint Association Extended Capability;不允许任何其他 PCI Express Device Function(PCI Express 设备功能)实现此 Capability(能力)。
如 § 图 7-269 所示,Root Complex Event Collector Endpoint Association Extended Capability 由 PCI Express Extended Capability header(PCI Express 扩展能力头)组成,后跟一个 DWORD 位图,用于枚举同一 Bus(总线)上的 RCiEP,并可选地附加一段 Bus Number(总线号)范围,该范围内可能包含与该根复合体事件收集器关联的 RCiEP。此 Capability 所描述范围内的非 RCiEP 功能(例如 Root Port(根端口))与该根复合体事件收集器无关。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1308 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset
PCI Express Extended Capability Header
Association Bitmap for RCiEPs
RCEC Associated Bus Numbers
+000h
+004h
+008h
Figure 7-269 Root Complex Event Collector Endpoint Association Extended Capability
The Extended Capability ID for the Root Complex Event Collector Endpoint Association Extended Capability is 0007h.
§ Figure 7-270 details allocation of fields in the Root Complex Event Collector Endpoint Association Extended Capability
Header; § Table 7-241 provides the respective bit definitions.
0
15
PCI Express Extended Capability ID
0007h
16
19
Capability Version
20
31
Next Capability Offset
Figure 7-270 Root Complex Event Collector Endpoint Association Extended Capability Header
Table 7-241 Root Complex Event Collector Endpoint Association Extended Capability Header
Bit Location
Register Description
Attributes
15:0
PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature
and format of the Extended Capability.
The Extended Capability ID for the Root Complex Event Collector Endpoint Association Extended
Capability is 0007h.
RO
19:16
Capability Version - This field is a PCI-SIG defined version number that indicates the version of the
Capability structure present.
Must be 2h if the Extended Capability contains the RCEC Associated Bus Numbers Register (see § Section
7.9.10.3 ). Must be 1h otherwise.
RO

</td>
<td style="background-color:#e8e8e8">

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset(字节偏移)
PCI Express Extended Capability Header(PCI Express 扩展能力头)
Association Bitmap for RCiEPs(RCiEP 关联位图)
RCEC Associated Bus Numbers(RCEC 关联总线号)
+000h
+004h
+008h
图 7-269 Root Complex Event Collector Endpoint Association Extended Capability(根复合体事件收集器端点关联扩展能力)
Root Complex Event Collector Endpoint Association Extended Capability 的 Extended Capability ID(扩展能力 ID)为 0007h。
§ 图 7-270 详细说明了 Root Complex Event Collector Endpoint Association Extended Capability Header 中各字段的分配;§ 表 7-241 给出了相应的位定义。
0
15
PCI Express Extended Capability ID(PCI Express 扩展能力 ID)
0007h
16
19
Capability Version(能力版本)
20
31
Next Capability Offset(下一能力偏移量)
图 7-270 Root Complex Event Collector Endpoint Association Extended Capability Header(根复合体事件收集器端点关联扩展能力头)
表 7-241 Root Complex Event Collector Endpoint Association Extended Capability Header(根复合体事件收集器端点关联扩展能力头)
位位置
寄存器描述
属性
15:0
PCI Express Extended Capability ID(PCI Express 扩展能力 ID) — 该字段是 PCI-SIG 定义的 ID 号,用于指示 Extended Capability(扩展能力)的性质和格式。
Root Complex Event Collector Endpoint Association Extended Capability 的 Extended Capability ID 为 0007h。
RO
19:16
Capability Version(能力版本) — 该字段是 PCI-SIG 定义的版本号,用于指示当前 Capability(能力)结构的版本。
如果 Extended Capability 包含 RCEC Associated Bus Numbers Register(见 § 第 7.9.10.3 节),则必须为 2h;否则必须为 1h。
RO

</td>
</tr>
</tbody>
</table>
</div>


---

<a id="sec-7-9-10-1"></a>
## 7.9.10.1 Root Complex Event Collector Endpoint Association Extended Capability Header (Offset 00h) | 根复合体事件收集器端点关联扩展能力头(偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
31:20
Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h
if no other items exist in the linked list of Capabilities.
For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of
PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of
Capabilities) or greater than 0FFh.
The bottom 2 bits of this offset are Reserved and must be implemented as 00b although software must
mask them to allow for future uses of these bits.
RO

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
31:20
Next Capability Offset(下一能力偏移量) — 该字段包含下一个 PCI Express Capability(能力)结构的偏移量,如果链接的 Capability 列表中不存在其他项,则为 000h。
对于在 Configuration Space(配置空间)中实现的 Extended Capability(扩展能力),此偏移量相对于 PCI-compatible Configuration Space(PCI 兼容配置空间)的开头,因此必须始终为 000h(用于终止 Capability 列表)或大于 0FFh。
此偏移量的低 2 位为保留位,必须实现为 00b,但软件必须屏蔽它们以便将来使用这些位。
RO

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1309 -->
---

<a id="sec-7-9-10-2"></a>
## 7.9.10.2 Association Bitmap for RCiEPs (Offset 04h) | RCiEP 关联位图(偏移量 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Association Bitmap for RCiEPs is a read-only register that sets the bits corresponding to the Device Numbers of
RCiEPs associated with the Root Complex Event Collector on the same Bus Number as the Event Collector itself. The bit
corresponding to the Device Number of the Root Complex Event Collector must always be Set.

</td>
<td style="background-color:#e8e8e8">

Association Bitmap for RCiEPs(RCiEP 关联位图)是一个只读寄存器,用于设置与事件收集器所在同一 Bus Number 上的根复合体事件收集器关联的 RCiEP 的 Device Number(设备号)所对应的位。与根复合体事件收集器 Device Number 对应的位必须始终置位。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-10-3"></a>
## 7.9.10.3 RCEC Associated Bus Numbers Register (Offset 08h) | RCEC 关联总线号寄存器(偏移量 08h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The RCEC Associated Bus Numbers Register is a read-only register that indicates an additional range of Bus Numbers
containing RCiEPs associated with this Root Complex Event Collector. It is permitted for Functions other than RCiEPs,
including Root Ports, to appear within the Association Bus Range. Only RCiEPs in the range are associated with this Root
Complex Event Collector. This register is present if the Capability Version is 2h or greater.
This register does not indicate association between an Event Collector and any Virtual Functions within the Association
Bus Range (see § Section 9.2.1.2 ). This register does not indicate association between an Event Collector and any
Function on the same Bus Number as the Event Collector itself, however it is permitted for the Association Bus Range to
include the Bus Number of the Root Complex Event Collector.
0
7
RsvdP
8
15
RCEC Next Bus
16
23
RCEC Last Bus
24
31
RsvdP
Figure 7-271 RCEC Associated Bus Numbers Register
Table 7-242 RCEC Associated Bus Numbers Register
Bit Location
Register Description
Attributes
15:8
RCEC Next Bus - This field contains the lowest additional bus number containing RCiEPs associated with
this Root Complex Event Collector. If all of the Devices associated with this Root Complex Event
Collector are on the same bus as the Event Collector, then this field must be set to FFh.
HwInit
23:16
RCEC Last Bus - This field contains the highest additional bus number containing RCiEPs associated
with this Root Complex Event Collector.
If all of the Devices associated with this Root Complex Event Collector are on the same bus as the Event
Collector, then this field must be set to 00h.
HwInit

</td>
<td style="background-color:#e8e8e8">

RCEC Associated Bus Numbers Register(RCEC 关联总线号寄存器)是一个只读寄存器,用于指示包含与此根复合体事件收集器关联的 RCiEP 的附加总线号范围。允许 Association Bus Range(关联总线范围)内出现除 RCiEP 之外的 Function(包括 Root Port)。只有该范围内的 RCiEP 才与此根复合体事件收集器关联。如果 Capability Version 为 2h 或更高,则存在此寄存器。
此寄存器不指示事件收集器与 Association Bus Range 内的任何 Virtual Function(虚拟功能,见 § 第 9.2.1.2 节)之间的关联。此寄存器不指示事件收集器与事件收集器所在同一 Bus Number 上的任何 Function 之间的关联,但允许 Association Bus Range 包含该根复合体事件收集器的 Bus Number。
0
7
RsvdP
8
15
RCEC Next Bus(RCEC 下一总线)
16
23
RCEC Last Bus(RCEC 上一总线)
24
31
RsvdP
图 7-271 RCEC Associated Bus Numbers Register(RCEC 关联总线号寄存器)
表 7-242 RCEC Associated Bus Numbers Register(RCEC 关联总线号寄存器)
位位置
寄存器描述
属性
15:8
RCEC Next Bus(RCEC 下一总线) — 该字段包含与此根复合体事件收集器关联的 RCiEP 所在的最低附加总线号。如果与此根复合体事件收集器关联的所有 Device 都位于与事件收集器相同的总线上,则该字段必须设置为 FFh。
HwInit
23:16
RCEC Last Bus(RCEC 上一总线) — 该字段包含与此根复合体事件收集器关联的 RCiEP 所在的最高附加总线号。
如果与此根复合体事件收集器关联的所有 Device 都位于与事件收集器相同的总线上,则该字段必须设置为 00h。
HwInit

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1310 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

IMPLEMENTATION NOTE:
RCEC ASSOCIATED BUS NUMBER COMPATIBILITY WITH
LEGACY SOFTWARE
Legacy software may not support the use of the RCEC Associated Bus Numbers Register as a mechanism to
associate Devices with a RCEC. Such software may see events in the RCEC from Devices on different bus numbers
that it does not consider to be associated with the Root Complex Event Collector. System Software is strongly
encouraged to report all events seen on the Root Complex Event Collector, regardless of whether or not it can
determine association.

</td>
<td style="background-color:#e8e8e8">

实现注意事项:
与传统软件的 RCEC 关联总线号兼容性
传统软件可能不支持使用 RCEC Associated Bus Numbers Register 作为将 Device 与 RCEC 关联的机制。此类软件可能会在 RCEC 中看到来自不同总线号上 Device 的事件,但这些 Device 不被视为与此根复合体事件收集器相关联。强烈建议 System Software(系统软件)报告在根复合体事件收集器上观察到的所有事件,无论它是否能够确定关联性。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11"></a>
## 7.9.11 Multicast Extended Capability | 组播扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Multicast is an optional normative functionality that is controlled by the Multicast Extended Capability structure. The
Multicast Extended Capability is applicable to Root Ports, RCRBs, Switch Ports, Endpoint Functions, and RCiEPs. It is not
applicable to PCI Express to PCI/PCI-X Bridges.
Multicast support is optional in SR-IOV devices. If a VF implements a Multicast capability, its associated PF must
implement a Multicast capability.
In the cases of a Switch or Root Complex or a component that contains multiple Functions, multiple copies of this
Capability structure are required - one for each Endpoint Function, Switch Port, or Root Port that supports Multicast. To
provide implementation efficiencies, certain fields within each of the Multicast Extended Capability structures within a
component must be programmed the same and results are indeterminate if this is not the case. The fields and registers
that must be configured with the same values include MC_Enable, MC_Num_Group, MC_Base_Address and
MC_Index_Position. These same fields in an Endpoint's Multicast Extended Capability structure must match those
configured into a Multicast Extended Capability structure of the Switch or Root Complex above the Endpoint or in which
the RCiEP is integrated.

</td>
<td style="background-color:#e8e8e8">

Multicast(组播)是一种可选的规范性功能,由 Multicast Extended Capability(组播扩展能力)结构控制。Multicast Extended Capability 适用于 Root Port、RCRB、Switch Port、Endpoint Function 和 RCiEP。它不适用于 PCI Express 到 PCI/PCI-X 的桥接设备 (Bridge)。
SR-IOV(单根 I/O 虚拟化)设备中的 Multicast 支持是可选的。如果 VF(虚拟功能)实现 Multicast capability(组播能力),则其关联的 PF(物理功能)必须实现 Multicast capability。
对于 Switch(交换机)或 Root Complex(根复合体)或包含多个 Function 的组件,需要此 Capability 结构的多个副本——每个支持 Multicast 的 Endpoint Function、Switch Port 或 Root Port 各一个。为了提供实现效率,组件内每个 Multicast Extended Capability 结构中的某些字段必须以相同方式编程,否则结果不确定。必须配置为相同值的字段和寄存器包括 MC_Enable、MC_Num_Group、MC_Base_Address 和 MC_Index_Position。Endpoint 的 Multicast Extended Capability 结构中的这些相同字段必须与 Endpoint 上方的 Switch 或 Root Complex 的 Multicast Extended Capability 结构中配置的字段匹配,或者与 RCiEP 集成所在的 Switch 或 Root Complex 中的字段匹配。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1311 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset
PCI Express Extended Capability Header
Multicast Capability Register
Multicast Control Register
MC_Base_Address Register
MC_Receive Register
MC_Block_All Register
MC_Block_Untranslated Register
MC_Overlay_BAR Register
+000h
+004h
+008h
+00Ch
+010h
+014h
+018h
+01Ch
+020h
+024h
+028h
+02Ch
Figure 7-272 Multicast Extended Capability Structure
§ Figure 7-273 details allocation of the fields in the Multicast Extended Capability Header and § Table 7-243 provides the
respective bit definitions.
0
15
PCI Express Extended Capability ID
0012h
16
19
Capability Version
20
31
Next Capability Offset
Figure 7-273 Multicast Extended Capability Header
Table 7-243 Multicast Extended Capability Header
Bit Location
Register Description
Attributes
15:0
PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature
and format of the Extended Capability.
RO

</td>
<td style="background-color:#e8e8e8">

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset(字节偏移)
PCI Express Extended Capability Header(PCI Express 扩展能力头)
Multicast Capability Register(组播能力寄存器)
Multicast Control Register(组播控制寄存器)
MC_Base_Address Register(MC 基址寄存器)
MC_Receive Register(MC 接收寄存器)
MC_Block_All Register(MC 全部阻止寄存器)
MC_Block_Untranslated Register(MC 阻止未转换寄存器)
MC_Overlay_BAR Register(MC 覆盖 BAR 寄存器)
+000h
+004h
+008h
+00Ch
+010h
+014h
+018h
+01Ch
+020h
+024h
+028h
+02Ch
图 7-272 Multicast Extended Capability Structure(组播扩展能力结构)
§ 图 7-273 详细说明了 Multicast Extended Capability Header(组播扩展能力头)中各字段的分配;§ 表 7-243 给出了相应的位定义。
0
15
PCI Express Extended Capability ID(PCI Express 扩展能力 ID)
0012h
16
19
Capability Version(能力版本)
20
31
Next Capability Offset(下一能力偏移量)
图 7-273 Multicast Extended Capability Header(组播扩展能力头)
表 7-243 Multicast Extended Capability Header(组播扩展能力头)
位位置
寄存器描述
属性
15:0
PCI Express Extended Capability ID(PCI Express 扩展能力 ID) — 该字段是 PCI-SIG 定义的 ID 号,用于指示 Extended Capability(扩展能力)的性质和格式。
RO

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-1"></a>
## 7.9.11.1 Multicast Extended Capability Header (Offset 00h) | 组播扩展能力头(偏移量 00h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Bit Location
Register Description
Attributes
PCI Express Extended Capability ID for the Multicast Extended Capability is 0012h.
19:16
Capability Version - This field is a PCI-SIG defined version number that indicates the version of the
Capability structure present.
Must be 1h for this version of the specification.
RO
31:20
Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability
structure or 000h if no other items exist in the linked list of Capabilities.
RO

</td>
<td style="background-color:#e8e8e8">

位位置
寄存器描述
属性
Multicast Extended Capability 的 PCI Express Extended Capability ID 为 0012h。
19:16
Capability Version(能力版本) — 该字段是 PCI-SIG 定义的版本号,用于指示当前 Capability(能力)结构的版本。
在本版本的规范中必须为 1h。
RO
31:20
Next Capability Offset(下一能力偏移量) — 该字段包含下一个 PCI Express Extended Capability(扩展能力)结构的偏移量,如果链接的 Capability 列表中不存在其他项,则为 000h。
RO

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1312 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-274 details allocation of the fields in the Multicast Capability Register and § Table 7-244 provides the
respective bit definitions.
0
5
MC_Max_Group
6
7
RsvdP
8
13
MC_Window_Size_Requested
14
RsvdP
15
MC_ECRC_Regeneration_Supported
Figure 7-274 Multicast Capability Register
Table 7-244 Multicast Capability Register
Bit Location
Register Description
Attributes
5:0
MC_Max_Group - Value indicates the maximum number of Multicast Groups that the component
supports, encoded as M-1. A value of 00h indicates that one Multicast Group is supported.
For VFs, this field is RsvdP. The value from the associated PF applies.
RO
VF RsvdP
13:8
MC_Window_Size_Requested - In Endpoints, the log2 of the Multicast Window size requested. RsvdP in
Switch and Root Ports.
For VFs, this field is RsvdP. The value from the associated PF applies.
RO
VF RsvdP
15
MC_ECRC_Regeneration_Supported - If Set, indicates that ECRC regeneration is supported.
This bit must not be Set unless the Function supports Advanced Error Reporting, and the ECRC Check
Capable bit in the Advanced Error Capabilities and Control Register is also Set. However, if ECRC
regeneration is supported, its operation is not contingent upon the setting of the ECRC Check Enable bit in
the Advanced Error Capabilities and Control Register. This bit is applicable to Switch and Root Ports and
is RsvdP in all other Functions.
RO/RsvdP

</td>
<td style="background-color:#e8e8e8">

§ 图 7-274 详细说明了 Multicast Capability Register(组播能力寄存器)中各字段的分配;§ 表 7-244 给出了相应的位定义。
0
5
MC_Max_Group(MC 最大组数)
6
7
RsvdP
8
13
MC_Window_Size_Requested(MC 请求的窗口大小)
14
RsvdP
15
MC_ECRC_Regeneration_Supported(MC 支持 ECRC 重新生成)
图 7-274 Multicast Capability Register(组播能力寄存器)
表 7-244 Multicast Capability Register(组播能力寄存器)
位位置
寄存器描述
属性
5:0
MC_Max_Group(MC 最大组数) — 该值指示组件所支持的 Multicast Group(组播组)最大数量,以 M-1 进行编码。值为 00h 指示支持一个 Multicast Group。
对于 VF,该字段为 RsvdP。适用关联 PF 的值。
RO
VF RsvdP
13:8
MC_Window_Size_Requested(MC 请求的窗口大小) — 在 Endpoint 中,表示请求的 Multicast Window(组播窗口)大小的 log2 值。在 Switch 和 Root Port 中为 RsvdP。
对于 VF,该字段为 RsvdP。适用关联 PF 的值。
RO
VF RsvdP
15
MC_ECRC_Regeneration_Supported(MC 支持 ECRC 重新生成) — 如果置位,指示支持 ECRC(端到端 CRC)重新生成。
除非 Function 支持 Advanced Error Reporting(高级错误报告)且 Advanced Error Capabilities and Control Register(高级错误能力与控制寄存器)中的 ECRC Check Capable 位也被置位,否则不得置位该位。但是,如果支持 ECRC 重新生成,则其操作不依赖于 Advanced Error Capabilities and Control Register 中 ECRC Check Enable 位的设置。该位适用于 Switch 和 Root Port,在所有其他 Function 中为 RsvdP。
RO/RsvdP

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1313 -->
---

<a id="sec-7-9-11-2"></a>
## 7.9.11.2 Multicast Capability Register (Offset 04h) | 组播能力寄存器(偏移量 04h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
5
MC_Num_Group
6
14
RsvdP
15
MC_Enable
Figure 7-275 Multicast Control Register
Table 7-245 Multicast Control Register
Bit Location
Register Description
Attributes
5:0
MC_Num_Group - Value indicates the number of Multicast Groups configured for use, encoded as N-1.
The default value of 00 0000b indicates that one Multicast Group is configured for use. Behavior is
undefined if value exceeds MC_Max_Group. This parameter indirectly defines the upper limit of the
Multicast address range. This field is ignored if MC_Enable is Clear. Default value is 00 0000b.
For VFs, this field is RsvdP. The value from the associated PF applies.
RW
VF RsvdP
15
MC_Enable - When Set, the Multicast mechanism is enabled for the component. Default value is 0b.
RW
The MC_Base_Address Register contains the MC_Base_Address and the MC_Index_Position. § Figure 7-276 details
allocation of the fields in the MC_Base_Address Register and § Table 7-246 provides the respective bit definitions.
A-0751
0
31
MC_Base_Address [31:12]
MC_Index_Position
RsvdP
MC_Base_Address [63:32]
12 11
6
5
Figure 7-276 MC_Base_Address Register
Table 7-246 MC_Base_Address Register
Bit Location
Register Description
Attributes
5:0
MC_Index_Position - The location of the LSB of the Multicast Group number within the address.
Behavior is undefined if this value is less than 12 and MC_Enable is Set. Default is 0.
For VFs, this field is RsvdP. The value from the associated PF applies.
RW
VF RsvdP

</td>
<td style="background-color:#e8e8e8">

0
5
MC_Num_Group(MC 组数)
6
14
RsvdP
15
MC_Enable(MC 使能)
图 7-275 Multicast Control Register(组播控制寄存器)
表 7-245 Multicast Control Register(组播控制寄存器)
位位置
寄存器描述
属性
5:0
MC_Num_Group(MC 组数) — 该值指示已配置使用的 Multicast Group 数量,以 N-1 进行编码。默认值 00 0000b 指示已配置一个 Multicast Group。如果该值超过 MC_Max_Group,则行为未定义。该参数间接定义 Multicast 地址范围的上限。如果 MC_Enable 清零,则忽略该字段。默认值为 00 0000b。
对于 VF,该字段为 RsvdP。适用关联 PF 的值。
RW
VF RsvdP
15
MC_Enable(MC 使能) — 置位时,为该组件启用 Multicast 机制。默认值为 0b。
RW
MC_Base_Address Register(MC 基址寄存器)包含 MC_Base_Address 和 MC_Index_Position。§ 图 7-276 详细说明了 MC_Base_Address Register 中各字段的分配;§ 表 7-246 给出了相应的位定义。
A-0751
0
31
MC_Base_Address [31:12]
MC_Index_Position(MC 索引位置)
RsvdP
MC_Base_Address [63:32]
12 11
6
5
图 7-276 MC_Base_Address Register(MC 基址寄存器)
表 7-246 MC_Base_Address Register(MC 基址寄存器)
位位置
寄存器描述
属性
5:0
MC_Index_Position(MC 索引位置) — 地址中 Multicast Group 编号的 LSB(最低有效位)的位置。
如果该值小于 12 且 MC_Enable 已置位,则行为未定义。默认值为 0。
对于 VF,该字段为 RsvdP。适用关联 PF 的值。
RW
VF RsvdP

</td>
</tr>
</tbody>
</table>
</div>


---


---

<a id="sec-7-9-11-3"></a>
## 7.9.11.3 Multicast Control Register (Offset 06h) | 多播控制寄存器（偏移 06h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.3 Multicast Control Register (Offset 06h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.3 多播控制寄存器（Multicast Control Register，偏移 06h）

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-4"></a>
## 7.9.11.4 MC_Base_Address Register (Offset 08h) | MC_Base_Address 寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.4 MC_Base_Address Register (Offset 08h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.4 MC_Base_Address 寄存器（偏移 08h）

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1314 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Bit Location**

**Register Description**

**Attributes**

63:12

MC_Base_Address - The base address of the Multicast address range. The behavior is undefined if MC_Enable is Set and bits in this field corresponding to address bits that contain the Multicast Group number or address bits less than MC_Index_Position are non-zero. Default is 0.

For VFs, this field is RsvdP. The value from the associated PF applies.

RW

VF RsvdP

</td>
<td style="background-color:#e8e8e8">

**位位置**

**寄存器描述**

**属性**

63:12

MC_Base_Address — 多播地址范围的基地址。如果 MC_Enable 被置位，且本字段中对应于包含 Multicast Group 编号的地址位或小于 MC_Index_Position 的地址位为非零，则行为未定义。默认值为 0。

对于 VF，本字段为 RsvdP，其值由所关联的 PF 决定。

RW

VF RsvdP

</td>
</tr>
</tbody>
</table>

---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MC_Receive Register provides a bit vector denoting which Multicast groups the Function should accept, or in the case of Switch and Root Complex Ports, forward Multicast TLPs. This register is required in all Functions that implement the MC Capability structure.

§ Figure 7-277 details allocation of the fields in the MC_Receive Register and § Table 7-247 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

MC_Receive 寄存器提供一个位向量，用于指示该 Function 应接受哪些多播组（Multicast Group）的流量；对于交换机（Switch）和根复合体（Root Complex）端口，则指示应转发哪些多播 TLP。所有实现 MC Capability 结构的 Function 中都必须实现该寄存器。

§ 图 7-277 详述了 MC_Receive 寄存器中各字段的分配，§ 表 7-247 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

> **Figure 7-277.** MC_Receive Register
> <img src="figures/chapter_07/fig_1314_1_tight.png" width="700">

</div>


---

**Table 7-247. MC_Receive Register | 表 7-247. MC_Receive 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| MC_Max_Group:0 | MC_Receive - For each bit that's Set, this Function gets a copy of any Multicast TLPs for the associated Multicast Group. Bits above MC_Num_Group are ignored by hardware. Default value of each bit is 0b. | RW |
| All other bits | Reserved | RsvdP |

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MC_Block_All Register provides a bit vector denoting which Multicast groups the Function should block. This register is required in all Functions that implement the MC Capability structure.

§ Figure 7-278 details allocation of the fields in the MC_Block_All Register and § Table 7-248 provides the respective bit definitions.

> **Figure 7-278.** MC_Block_All Register
> <img src="figures/chapter_07/fig_1314_2_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">

MC_Block_All 寄存器提供一个位向量，用于指示该 Function 应阻止哪些多播组（Multicast Group）的流量。所有实现 MC Capability 结构的 Function 中都必须实现该寄存器。

§ 图 7-278 详述了 MC_Block_All 寄存器中各字段的分配，§ 表 7-248 给出了相应的位定义。

<img src="figures/chapter_07/fig_1314_2_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-5"></a>
## 7.9.11.5 MC_Receive Register (Offset 10h) | MC_Receive 寄存器（偏移 10h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.5 MC_Receive Register (Offset 10h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.5 MC_Receive 寄存器（偏移 10h）

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-6"></a>
## 7.9.11.6 MC_Block_All Register (Offset 18h) | MC_Block_All 寄存器（偏移 18h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.6 MC_Block_All Register (Offset 18h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.6 MC_Block_All 寄存器（偏移 18h）

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1315 -->
---

**Table 7-248. MC_Block_All Register | 表 7-248. MC_Block_All 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| MC_Max_Group:0 | MC_Block_All - For each bit that is Set, this Function is blocked from sending TLPs to the associated Multicast Group. Bits above MC_Num_Group are ignored by hardware. Default value of each bit is 0b. | RW |
| All other bits | Reserved | RsvdP |

---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MC_Block_Untranslated Register is used to determine whether or not a TLP that includes an Untranslated Address should be blocked. This register is required in all Functions that implement the MC Capability structure. However, an Endpoint Function that does not implement the ATS capability may implement this register as RsvdP.

§ Figure 7-279 details allocation of the fields in the MC_Block_Untranslated Register and § Table 7-249 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

MC_Block_Untranslated 寄存器用于确定是否应阻止包含未转换地址（Untranslated Address）的 TLP。所有实现 MC Capability 结构的 Function 中都必须实现该寄存器。但是，未实现 ATS 能力的端点（Endpoint）Function 可以将该寄存器实现为 RsvdP。

§ 图 7-279 详述了 MC_Block_Untranslated 寄存器中各字段的分配，§ 表 7-249 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

> **Figure 7-279.** MC_Block_Untranslated Register
> <img src="figures/chapter_07/fig_1315_1_tight.png" width="700">

</div>


---

**Table 7-249. MC_Block_Untranslated Register | 表 7-249. MC_Block_Untranslated 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| MC_Max_Group:0 | MC_Block_Untranslated - For each bit that is Set, this Function is blocked from sending TLPs containing Untranslated Addresses to the associated MCG. Bits above MC_Num_Group are ignored by hardware. Default value of each bit is 0b. | RW |
| All other bits | Reserved | RsvdP |

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MC_Overlay_BAR Register is required in Switch and Root Complex Ports that support the Multicast Extended Capability and not implemented in Endpoints. Software must interpret the Device/Port Type field in the PCI Express Capabilities Register to determine if the MC_Overlay_BAR Register is present in a Function.

The MC_Overlay_BAR specifies the base address of a window in unicast space onto which Multicast TLPs going out an Egress Port are overlaid by a process of address replacement. This allows a single BAR in an Endpoint attached to the Switch or Root Port to be used for both unicast and Multicast traffic. At a Switch Upstream Port, it allows the Multicast address range, or a portion of it, to be overlayed onto host memory.

§ Figure 7-280 details allocation of the fields in the MC_Overlay_BAR Register and § Table 7-250 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

MC_Overlay_BAR 寄存器是支持 Multicast 扩展能力的交换机（Switch）和根复合体（Root Complex）端口所必需的，端点（Endpoint）中不实现。软件必须通过解读 PCI Express 能力寄存器（PCI Express Capabilities Register）中的 Device/Port Type 字段来确定 Function 中是否存在 MC_Overlay_BAR 寄存器。

MC_Overlay_BAR 用于指定单播（unicast）地址空间中一个窗口的基地址，从出口端口（Egress Port）出去的多播 TLP 通过地址替换（address replacement）的方式被覆盖到该窗口。这允许连接到交换机或根端口的端点中的单个 BAR 既可用于单播流量，也可用于多播流量。在交换机上游端口（Upstream Port）处，它允许将多播地址范围（或其一部分）覆盖到主机内存上。

§ 图 7-280 详述了 MC_Overlay_BAR 寄存器中各字段的分配，§ 表 7-250 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-7"></a>
## 7.9.11.7 MC_Block_Untranslated Register (Offset 20h) | MC_Block_Untranslated 寄存器（偏移 20h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.7 MC_Block_Untranslated Register (Offset 20h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.7 MC_Block_Untranslated 寄存器（偏移 20h）

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-11-8"></a>
## 7.9.11.8 MC_Overlay_BAR Register (Offset 28h) | MC_Overlay_BAR 寄存器（偏移 28h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.11.8 MC_Overlay_BAR Register (Offset 28h)

</td>
<td style="background-color:#e8e8e8">

7.9.11.8 MC_Overlay_BAR 寄存器（偏移 28h）

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1316 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-280.** MC_Overlay_BAR Register
> <img src="figures/chapter_07/fig_1316_1_tight.png" width="700">


---

**Table 7-250. MC_Overlay_BAR Register | 表 7-250. MC_Overlay_BAR 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 5:0 | MC_Overlay_Size - If 6 or greater, specifies the size in bytes of the overlay aperture as a power of 2. If less than 6, disables the overlay mechanism. Default value is 00 0000b. | RW |
| 63:6 | MC_Overlay_BAR - Specifies the base address of the window onto which MC TLPs passing through this Function will be overlaid. Default value is 0. | RW |

---

<a id="sec-7-9-12"></a>
## 7.9.12 Dynamic Power Allocation Extended Capability (DPA Capability) | 动态功率分配扩展能力（DPA 能力）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12 Dynamic Power Allocation Extended Capability (DPA Capability)

The DPA Capability structure is shown in § Figure 7-281.

</td>
<td style="background-color:#e8e8e8">

7.9.12 动态功率分配（Dynamic Power Allocation，DPA）扩展能力（DPA Capability）

DPA Capability 结构如 § 图 7-281 所示。

</td>
</tr>
</tbody>
</table>

> **Figure 7-281.** Dynamic Power Allocation Extended Capability Structure
> <img src="figures/chapter_07/fig_1316_2_tight.png" width="700">


<!-- 📄 Page 1317 -->
---

<a id="sec-7-9-12-1"></a>
## 7.9.12.1 DPA Extended Capability Header (Offset 00h) | DPA 扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.1 DPA Extended Capability Header (Offset 00h)

</td>
<td style="background-color:#e8e8e8">

7.9.12.1 DPA 扩展能力头（偏移 00h）

</td>
</tr>
</tbody>
</table>

> **Figure 7-282.** DPA Extended Capability Header
> <img src="figures/chapter_07/fig_1317_1_tight.png" width="700">


---

**Table 7-251. DPA Extended Capability Header | 表 7-251. DPA 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. PCI Express Extended Capability ID for the DPA Extended Capability is 0016h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. | RO |

---

<a id="sec-7-9-12-2"></a>
## 7.9.12.2 DPA Capability Register (Offset 04h) | DPA 能力寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.2 DPA Capability Register (Offset 04h)

</td>
<td style="background-color:#e8e8e8">

7.9.12.2 DPA 能力寄存器（偏移 04h）

</td>
</tr>
</tbody>
</table>

> **Figure 7-283.** DPA Capability Register
> <img src="figures/chapter_07/fig_1317_2_tight.png" width="700">


---

**Table 7-252. DPA Capability Register | 表 7-252. DPA 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4:0 | Substate_Max - Value indicates the maximum substate number, which is the total number of supported substates minus one. A value of 0 0000b indicates support for one substate. | RO |

<!-- 📄 Page 1318 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 9:8 | Transition Latency Unit (Tlunit) - A substate's Transition Latency Value is multiplied by the Transition Latency Unit to determine the maximum Transition Latency for the substate. Defined encodings are: 00b = 1 ms, 01b = 10 ms, 10b = 100 ms, 11b = Reserved | RO |
| 13:12 | Power Allocation Scale (PAS) - The encodings provide the scale to determine power allocation per substate in Watts. The value corresponding to the substate in the Substate Power Allocation field is multiplied by this field to determine the power allocation for the substate. Defined encodings are: 00b = 10.0x, 01b = 1.0x, 10b = 0.1x, 11b = 0.01x | RO |
| 23:16 | Transition Latency Value 0 (Xlcy0) - This value is multiplied by the Transition Latency Unit to determine the maximum Transition Latency for the substate | RO |
| 31:24 | Transition Latency Value 1 (Xlcy1) - This value is multiplied by the Transition Latency Unit to determine the maximum Transition Latency for the substate. | RO |

</td>
<td style="background-color:#e8e8e8">

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 9:8 | 转换延迟单位（Transition Latency Unit，TLunit）— 子状态（substate）的转换延迟值与该转换延迟单位相乘，以确定该子状态的最大转换延迟。已定义的编码为：00b = 1 ms，01b = 10 ms，10b = 100 ms，11b = 保留 | RO |
| 13:12 | 功率分配缩放（Power Allocation Scale，PAS）— 该编码提供用于确定每个子状态功率分配（以瓦特为单位）的缩放因子。Substate Power Allocation 字段中子状态对应的值与本字段相乘，以确定该子状态的功率分配。已定义的编码为：00b = 10.0x，01b = 1.0x，10b = 0.1x，11b = 0.01x | RO |
| 23:16 | 转换延迟值 0（Transition Latency Value 0，Xlcy0）— 该值与转换延迟单位相乘，以确定该子状态的最大转换延迟 | RO |
| 31:24 | 转换延迟值 1（Transition Latency Value 1，Xlcy1）— 该值与转换延迟单位相乘，以确定该子状态的最大转换延迟 | RO |

</td>
</tr>
</tbody>
</table>
</div>


---

<a id="sec-7-9-12-3"></a>
## 7.9.12.3 DPA Latency Indicator Register (Offset 08h) | DPA 延迟指示寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.3 DPA Latency Indicator Register (Offset 08h)

> **Figure 7-284.** DPA Latency Indicator Register
> <img src="figures/chapter_07/fig_1318_1.png" width="700">

</td>
<td style="background-color:#e8e8e8">

7.9.12.3 DPA 延迟指示寄存器（偏移 08h）

<img src="figures/chapter_07/fig_1318_1.png" width="700">
</td>
</tr>
</tbody>
</table>

---

**Table 7-253. DPA Latency Indicator Register | 表 7-253. DPA 延迟指示寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 31:0 | Transition Latency Indicator Bits - Each bit indicates which Transition Latency Value is associated with the corresponding substate. A value of 0b indicates Transition Latency Value 0; a value of 1b indicates Transition Latency Value 1. Only bits [Substate_Max:0] are defined. Bits above Substate_Max are RsvdP. | RO |

<!-- 📄 Page 1319 -->
---

<a id="sec-7-9-12-4"></a>
## 7.9.12.4 DPA Status Register (Offset 0Ch) | DPA 状态寄存器（偏移 0Ch）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.4 DPA Status Register (Offset 0Ch)

</td>
<td style="background-color:#e8e8e8">

7.9.12.4 DPA 状态寄存器（偏移 0Ch）

</td>
</tr>
</tbody>
</table>

> **Figure 7-285.** DPA Status Register
> <img src="figures/chapter_07/fig_1319_1_tight.png" width="700">


---

**Table 7-254. DPA Status Register | 表 7-254. DPA 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4:0 | Substate Status - Indicates current substate for this Function. Default is 0 0000b. | RO |
| 8 | Substate Control Enabled - Used by software to disable the Substate Control field in the DPA Control Register. Hardware sets this bit following a Conventional Reset or FLR. Software clears this bit by writing a 1b to it. Software is unable to set this bit directly. When this bit is Set, the Substate Control field determines the current substate. When this bit is Clear, the Substate Control field has no effect on the current substate. Default value is 1b. | RW1C |

---

<a id="sec-7-9-12-5"></a>
## 7.9.12.5 DPA Control Register (Offset 0Eh) | DPA 控制寄存器（偏移 0Eh）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.5 DPA Control Register (Offset 0Eh)

</td>
<td style="background-color:#e8e8e8">

7.9.12.5 DPA 控制寄存器（偏移 0Eh）

</td>
</tr>
</tbody>
</table>

> **Figure 7-286.** DPA Control Register
> <img src="figures/chapter_07/fig_1319_2_tight.png" width="700">


---

**Table 7-255. DPA Control Register | 表 7-255. DPA 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4:0 | Substate Control - Used by software to configure the Function substate. Software writes the substate value in this field to initiate a substate transition. When the Substate Control Enabled bit in the DPA Status Register is Set, this field determines the Function substate. When the Substate Control Enabled bit in the DPA Status Register is Clear, this field has no effect on the Function substate. | RW |

<!-- 📄 Page 1320 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Default value is 0 0000b.

</td>
<td style="background-color:#e8e8e8">

默认值为 0 0000b。

</td>
</tr>
</tbody>
</table>

> **Figure 7-287.** DPA Power Allocation Array
> <img src="figures/chapter_07/fig_1320_1_tight.png" width="700">


---

<a id="sec-7-9-12-6"></a>
## 7.9.12.6 DPA Power Allocation Array | DPA 功率分配数组

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.12.6 DPA Power Allocation Array

Each Substate Power Allocation register indicates the power allocation value for its associated substate. The number of Substate Power Allocation registers implemented must be equal to the number of substates supported by Function, which is Substate_Max plus one.

</td>
<td style="background-color:#e8e8e8">

7.9.12.6 DPA 功率分配数组（DPA Power Allocation Array）

每个 Substate Power Allocation 寄存器指示其关联子状态（substate）的功率分配值。所实现的 Substate Power Allocation 寄存器数量必须等于 Function 所支持的子状态数，即 Substate_Max 加 1。

</td>
</tr>
</tbody>
</table>

> **Figure 7-288.** Substate Power Allocation Register (0 to Substate_Max)
> <img src="figures/chapter_07/fig_1320_2_tight.png" width="700">


---

**Table 7-256. Substate Power Allocation Register (0 to Substate_Max) | 表 7-256. Substate Power Allocation 寄存器（0 至 Substate_Max）**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Substate Power Allocation - The value in this field is multiplied by the Power Allocation Scale to determine power allocation in Watts for the associated substate. | RO |

---

<a id="sec-7-9-13"></a>
## 7.9.13 TPH Requester Extended Capability | TPH 请求者扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.13 TPH Requester Extended Capability

The TPH Requester Extended Capability structure is required for all Functions that are capable of generating Request TLPs with TPH. For a Multi-Function Device, this capability must be present in each Function that is capable of generating Request TLPs with TPH.

The capability is optional for PFs and VFs. However, if a VF associated with a given PF contains the capability, all VFs associated with that PF must contain the capability.

For fields in the TPH Requester Capability Register (offset 04h), all VFs associated with a given PF must have the same values in all fields, but the PF's fields may have values different from those in its VFs.

</td>
<td style="background-color:#e8e8e8">

7.9.13 TPH 请求者扩展能力（TPH Requester Extended Capability）

所有能够生成带 TPH 的请求 TLP 的 Function 都必须实现 TPH Requester Extended Capability 结构。对于多功能设备（Multi-Function Device），能够生成带 TPH 的请求 TLP 的每个 Function 都必须包含此能力。

该能力对 PF 和 VF 均为可选。但是，如果某个给定 PF 关联的某个 VF 包含此能力，则与该 PF 关联的所有 VF 都必须包含此能力。

对于 TPH Requester Capability 寄存器（偏移 04h）中的字段，与给定 PF 关联的所有 VF 在所有字段中必须具有相同的值，但 PF 的字段可以具有与其 VF 不同的值。

</td>
</tr>
</tbody>
</table>
</div>


<!-- 📄 Page 1321 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-289.** TPH Extended Capability Structure
> <img src="figures/chapter_07/fig_1321_1_tight.png" width="700">

> **Figure 7-290.** TPH Requester Extended Capability Header
> <img src="figures/chapter_07/fig_1321_2_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">



</td>
</tr>
</tbody>
</table>

---

**Table 7-257. TPH Requester Extended Capability Header | 表 7-257. TPH 请求者扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. PCI Express Extended Capability ID for the TPH Requester Extended Capability is 0017h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. | RO |

---

<a id="sec-7-9-13-1"></a>
## 7.9.13.1 TPH Requester Extended Capability Header (Offset 00h) | TPH 请求者扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.13.1 TPH Requester Extended Capability Header (Offset 00h)

</td>
<td style="background-color:#e8e8e8">

7.9.13.1 TPH 请求者扩展能力头（偏移 00h）

</td>
</tr>
</tbody>
</table>

> **Figure 7-291.** TPH Requester Capability Register
> <img src="figures/chapter_07/fig_1321_3_tight.png" width="700">


---

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

---

<a id="sec-7-9-13-2"></a>
## 7.9.13.2 TPH Requester Capability Register (Offset 04h) | TPH 请求者能力寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.13.2 TPH Requester Capability Register (Offset 04h)

</td>
<td style="background-color:#e8e8e8">

7.9.13.2 TPH 请求者能力寄存器（TPH Requester Capability Register，偏移 04h）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1322 -->
---

**Table 7-258. TPH Requester Capability Register | 表 7-258. TPH 请求者能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | No ST Mode Supported - If set indicates that the Function supports the No ST Mode of operation. This mode is required to be supported by all Functions that implement this Capability structure. This bit must have a value of 1b. | RO |
| 1 | Interrupt Vector Mode Supported - If set indicates that the Function supports the Interrupt Vector Mode of operation. | RO |
| 2 | Device Specific Mode Supported - If set indicates that the Function supports the Device Specific Mode of operation. | RO |
| 8 | Extended TPH Requester Supported - If Set indicates that the Function is capable of generating Requests with additional TPH information using the TPH TLP Prefix. See § Section 2.2.7.1.1 for additional details. | RO |
| 10:9 | ST Table Location - Value indicates if and where the ST Table is located. Defined Encodings are: 00b = ST Table is not present; 01b = ST Table is located in the TPH Requester Extended Capability structure; 10b = ST Table is located in the MSI-X Table (see § Section 7.7.2); 11b = Reserved. A Function that only supports the No ST Mode of operation must have a value of 00b in this field. A Function may report a value of 10b only if it implements an MSI-X Capability. | RO |
| 26:16 | ST Table Size - Value indicates the maximum number of ST Table entries the Function may use. Software reads this field to determine the ST Table Size N, which is encoded as N-1. For example, a returned value of 000 0000 0011b indicates a table size of four entries. There is an upper limit of 64 entries when the ST Table is located in the TPH Requester Extended Capability structure. When the ST Table is located in the MSI-X Table, this value is limited by the size of the MSI-X Table. This field is only applicable for Functions that implement an ST Table as indicated by the ST Table Location field. Otherwise, the value in this field is undefined. | RO |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-292.** TPH Requester Control Register
> <img src="figures/chapter_07/fig_1322_1_tight.png" width="700">


---

<a id="sec-7-9-13-3"></a>
## 7.9.13.3 TPH Requester Control Register (Offset 08h) | TPH 请求者控制寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.13.3 TPH Requester Control Register (Offset 08h)

</td>
<td style="background-color:#e8e8e8">

7.9.13.3 TPH 请求者控制寄存器（TPH Requester Control Register，偏移 08h）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1323 -->
---

**Table 7-259. TPH Requester Control Register | 表 7-259. TPH 请求者控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2:0 | ST Mode Select - selects the ST Mode of operation. Defined encodings are: 000b = No ST Mode; 001b = Interrupt Vector Mode; 010b = Device Specific Mode; others = reserved for future use. Functions that support only the No ST Mode of operation must hardwire this field to 000b. Function operation is undefined if software enables a mode of operation that does not correspond to a mode supported by the Function. The default value of this field is 000b. See § Section 6.17.3 for details on ST modes of operation. | RW |
| 9:8 | TPH Requester Enable - Controls the ability to issue Request TLPs using either TPH or Extended TPH. Defined encodings are: 00b = Function operating as a Requester is not permitted to issue Requests with TPH or Extended TPH; 01b = Function operating as a Requester is permitted to issue Requests with TPH and is not permitted to issue Requests with Extended TPH; 10b = Reserved; 11b = Function operating as a Requester is permitted to issue Requests with TPH and Extended TPH. Functions that advertise that they do not support Extended TPH are permitted to hardwire bit 9 of this field to 0b. The default value of this field is 00b. | RW |


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The TPH ST Table must be implemented in the TPH Requester Extended Capability structure if the value of the ST Table Location field is 01b. For all other values, the ST Entry registers must not be implemented. Each implemented ST Entry is 16 bits. The number of ST Entry registers implemented must be equal to the number of ST Table entries supported by the Function, which is the value of the ST Table Size field plus one.

</td>
<td style="background-color:#e8e8e8">

若 ST Table Location 字段的值为 01b，则 TPH ST 表必须在 TPH 请求者扩展能力结构内实现。对于其他所有值，ST Entry 寄存器不得实现。每个已实现的 ST Entry 为 16 位。已实现的 ST Entry 寄存器的数量必须等于该 Function 所支持的 ST 表条目数（即 ST Table Size 字段的值加一）。

</td>
</tr>
</tbody>
</table>

> **Figure 7-293.** TPH ST Table
> <img src="figures/chapter_07/fig_1323_1.png" width="700">

</div>


---

<a id="sec-7-9-13-4"></a>
## 7.9.13.4 TPH ST Table (Starting from Offset 0Ch) | TPH ST 表（起始偏移 0Ch）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.13.4 TPH ST Table (Starting from Offset 0Ch)

</td>
<td style="background-color:#e8e8e8">

7.9.13.4 TPH ST 表（TPH ST Table，起始偏移 0Ch）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1324 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-294.** TPH ST Table Entry
> <img src="figures/chapter_07/fig_1324_1.png" width="700">


**Table 7-260. TPH ST Table Entry | 表 7-260. TPH ST 表条目**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | ST Lower - This field contains the lower 8 bits of a Steering Tag. Default value of this field is 00h. | RW |
| 15:8 | ST Upper - If the Function's Extended TPH Requester Supported bit is Set, then this field contains the upper 8 bits of a Steering Tag. Otherwise, this field is RsvdP. Default value of this field is 00h. | RW |

---

<a id="sec-7-9-14"></a>
## 7.9.14 DPC Extended Capability | DPC 扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Downstream Port Containment (DPC) Extended Capability is an optional normative capability that provides a mechanism for Downstream Ports to contain uncorrectable errors and enable software to recover from them. See § Section 6.2.11. This capability may be implemented by a Root Port or a Switch Downstream Port. It is not applicable to any other Device/Port type.

If a Downstream Port implements the DPC Extended Capability, that Port must also be capable of reporting the DL_Active state, and indicate so by Setting the Data Link Layer Link Active Reporting Capable bit in the Link Capabilities Register. See § Section 7.5.3.6.

If a Downstream Port implements the DPC Extended Capability, it is strongly recommended for that Port to support ERR_COR Subclass capability, and indicate so by Setting the ERR_COR Subclass Capable bit in the Device Capabilities Register. See § Section 7.5.3.3.

The various RP PIO registers must be implemented only by Root Ports that support RP Extensions for DPC, as indicated by the RP Extensions for DPC bit in the DPC Capability Register.

</td>
<td style="background-color:#e8e8e8">

下游端口遏制（Downstream Port Containment, DPC）扩展能力是一种可选的规范性能力，为下游端口（Downstream Port）提供遏制不可纠正错误并使软件得以恢复的机制。参见 § Section 6.2.11。此能力可由根端口（Root Port）或交换机下游端口（Switch Downstream Port）实现，不适用于任何其他 Device/Port 类型。

若一个下游端口实现了 DPC 扩展能力，则该端口必须也能报告 DL_Active 状态，并通过在链路能力寄存器（Link Capabilities Register）中设置数据链路层链路激活上报能力位（Data Link Layer Link Active Reporting Capable bit）来表明这一点。参见 § Section 7.5.3.6。

若一个下游端口实现了 DPC 扩展能力，则强烈建议该端口支持 ERR_COR 子类能力（ERR_COR Subclass capability），并通过在设备能力寄存器（Device Capabilities Register）中设置 ERR_COR 子类能力位（ERR_COR Subclass Capable bit）来表明这一点。参见 § Section 7.5.3.3。

各 RP PIO 寄存器只能由支持 DPC RP 扩展（RP Extensions for DPC）的根端口实现，该能力由 DPC 能力寄存器（DPC Capability Register）中的 DPC RP 扩展位指示。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1325 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-295.** DPC Extended Capability – Non-Flit Mode
> <img src="figures/chapter_07/fig_1325_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1326 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-296.** DPC Extended Capability – Flit Mode
> <img src="figures/chapter_07/fig_1326_1_tight.png" width="700">


---

<!-- 📄 Page 1327 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-297.** DPC Extended Capability Header
> <img src="figures/chapter_07/fig_1327_1_tight.png" width="700">


**Table 7-261. DPC Extended Capability Header | 表 7-261. DPC 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the extended capability. PCI Express Extended Capability ID for the DPC Extended Capability is 001Dh. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of capabilities. | RO |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-298.** DPC Capability Register
> <img src="figures/chapter_07/fig_1327_2_tight.png" width="700">


---

<a id="sec-7-9-14-1"></a>
## 7.9.14.1 DPC Extended Capability Header (Offset 00h) | DPC 扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.1 DPC Extended Capability Header (Offset 00h)

</td>
<td style="background-color:#e8e8e8">

7.9.14.1 DPC 扩展能力头（DPC Extended Capability Header，偏移 00h）

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-14-2"></a>
## 7.9.14.2 DPC Capability Register (Offset 04h) | DPC 能力寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.2 DPC Capability Register (Offset 04h)

</td>
<td style="background-color:#e8e8e8">

7.9.14.2 DPC 能力寄存器（DPC Capability Register，偏移 04h）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1328 -->
---

**Table 7-262. DPC Capability Register | 表 7-262. DPC 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4:0 | DPC Interrupt Message Number - This field indicates which MSI/MSI-X vector is used for the interrupt message generated in association with the DPC Capability structure. For MSI, the value in this field indicates the offset between the base Message Data and the interrupt message that is generated. Hardware is required to update this field so that it is correct if the number of MSI Messages assigned to the Function changes when software writes to the Multiple Message Enable field in the Message Control Register for MSI. For MSI-X, the value in this field indicates which MSI-X Table entry is used to generate the interrupt message. The entry must be one of the first 32 entries even if the Function implements more than 32 entries. For a given MSI-X implementation, the entry must remain constant. If both MSI and MSI-X are implemented, they are permitted to use different vectors, though software is permitted to enable only one mechanism at a time. If MSI-X is enabled, the value in this field must indicate the vector for MSI-X. If MSI is enabled or neither is enabled, the value in this field must indicate the vector for MSI. If software enables both MSI and MSI-X at the same time, the value in this field is undefined. | RO |
| 5 | RP Extensions for DPC - If Set, this bit indicates that a Root Port supports a defined set of DPC Extensions that are specific to Root Ports. Switch Downstream Ports must not Set this bit. | RO |
| 6 | Poisoned TLP Egress Blocking Supported - If Set, this bit indicates that the Root Port or Switch Downstream Port supports the ability to block the transmission of a poisoned TLP from its Egress Port. Root Ports that support RP Extensions for DPC must Set this bit. | RO |
| 7 | DPC Software Triggering Supported - If Set, this bit indicates that a Root Port or Switch Downstream Port supports the ability for software to trigger DPC. Root Ports that support RP Extensions for DPC must Set this bit. | RO |
| 11:8 | RP PIO Log Size[3:0] - This field indicates how many DWORDs are allocated for the RP PIO log registers, comprised by the RP PIO Header Log, the RP PIO ImpSpec Log, and RP PIO TLP Prefix Log. If the Root Port does not support RP Extensions for DPC, the value of this field must be Zero. If the Root Port supports RP Extensions for DPC but does not support Flit Mode, the value of this field must be 4 or greater. If the Root Port supports both RP Extensions for DPC and Flit Mode, see § Section 6.2.11.3 for requirements. See § Section 7.9.14.11, § Section 7.9.14.12, and § Section 7.9.14.13. | RO |
| 12 | DL_Active ERR_COR Signaling Supported - If Set, this bit indicates that the Root Port or Switch Downstream Port supports the ability to signal with ERR_COR when the Link transitions to the DL_Active state. Root Ports that support RP Extensions for DPC must Set this bit. | RO |
| 13 | RP PIO Log Size[4] - This bit is an extension of RP PIO Log Size[3:0] for use in Flit Mode. If Flit Mode is not supported, this bit is RsvdP. | RO/RsvdP |

---

<!-- 📄 Page 1329 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-299.** DPC Control Register
> <img src="figures/chapter_07/fig_1329_1_tight.png" width="700">


**Table 7-263. DPC Control Register | 表 7-263. DPC 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 1:0 | DPC Trigger Enable - This field enables DPC and controls the conditions that cause DPC to be triggered. Defined encodings are: 00b = DPC is disabled; 01b = DPC is enabled and is triggered when the Downstream Port detects an unmasked uncorrectable error or when the Downstream Port receives an ERR_FATAL Message; 10b = DPC is enabled and is triggered when the Downstream Port detects an unmasked uncorrectable error or when the Downstream Port receives an ERR_NONFATAL or ERR_FATAL Message; 11b = Reserved. Default value of this field is 00b. | RW |
| 2 | DPC Completion Control - This bit controls the Completion Status for Completions formed during DPC. See § Section 2.9.3. Defined encodings are: 0b = Completer Abort (CA) Completion Status; 1b = Unsupported Request (UR) Completion Status. Default value of this bit is 0b. | RW |
| 3 | DPC Interrupt Enable - When Set, this bit enables the generation of an interrupt to indicate that DPC has been triggered. See § Section 6.2.11.1. Default value of this bit is 0b. | RW |
| 4 | DPC ERR_COR Enable - When Set, this bit enables the sending of an ERR_COR Message to indicate that DPC has been triggered. See § Section 6.2.11.2. Default value of this bit is 0b. | RW |

---

<a id="sec-7-9-14-3"></a>
## 7.9.14.3 DPC Control Register (Offset 06h) | DPC 控制寄存器（偏移 06h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.3 DPC Control Register (Offset 06h)

</td>
<td style="background-color:#e8e8e8">

7.9.14.3 DPC 控制寄存器（DPC Control Register，偏移 06h）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1330 -->
---

**Table 7-263 (cont.). DPC Control Register | 表 7-263（续）. DPC 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 5 | Poisoned TLP Egress Blocking Enable - This bit must be RW if the Poisoned TLP Egress Blocking Supported bit is Set; otherwise, it is permitted to be hardwired to 0b. Software must not Set this bit unless the Poisoned TLP Egress Blocking Supported bit is Set. When Set, this bit enables the associated Egress Port to block the transmission of poisoned TLPs. See § Section 2.7.2.1. Default value of this bit is 0b. | RW/RO |
| 6 | DPC Software Trigger - This bit must be RW if the DPC Software Triggering Supported bit is Set; otherwise, it is permitted to be hardwired to 0b. If DPC is enabled and the DPC Trigger Status bit is Clear, when software writes 1b to this bit, DPC is triggered. Otherwise, software writing a 1b to this bit has no effect. It is permitted to write 1b to this bit while simultaneously writing updated values to other fields in this register, notably the DPC Trigger Enable field. For this case, the DPC Software Trigger semantics are based on the updated value of the DPC Trigger Enable field. This bit always returns 0b when read. | RW/RO |
| 7 | DL_Active ERR_COR Enable - This bit must be RW if the DL_Active ERR_COR Signaling Supported bit is Set; otherwise, it is permitted to be hardwired to 0b. Software must not Set this bit unless the DL_Active ERR_COR Signaling Supported bit is Set. When Set, this bit enables the associated Downstream Port to signal with ERR_COR when the Link transitions to the DL_Active state. See § Section 6.2.11.5. Default value of this bit is 0b. | RW/RO |
| 8 | DPC SIG_SFW Enable - This bit must be implemented if the ERR_COR Subclass Capable bit in the Device Capabilities Register is Set; otherwise, it is permitted to be hardwired to 0b. If the ERR_COR Subclass Capable bit is Clear and software Sets this bit, the behavior is undefined. When Set, this bit enables sending an ERR_COR Message to indicate a DPC event that's been enabled for ERR_COR signaling. See § Section 6.2.11.2 and § Section 6.2.11.5. This is an additional and alternative way to enable overall DPC ERR_COR signaling beyond the Correctable Error Reporting Enable bit in the Device Control Register. This bit does not affect a Function's ability to send ERR_COR Messages other than the ECS SIG_SFW subclass. Default value of this bit is 0b. | RW/RO |

---

<!-- 📄 Page 1331 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="background-color:#e8e8e8">

</td>
</tr>
</tbody>
</table>

> **Figure 7-300.** DPC Status Register
> <img src="figures/chapter_07/fig_1331_1_tight.png" width="700">


---

<a id="sec-7-9-14-4"></a>
## 7.9.14.4 DPC Status Register (Offset 08h) | DPC 状态寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.4 DPC Status Register (Offset 08h)

</td>
<td style="background-color:#e8e8e8">

7.9.14.4 DPC 状态寄存器（DPC Status Register，偏移 08h）

</td>
</tr>
</tbody>
</table>

---

**Table 7-264. DPC Status Register | 表 7-264. DPC 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | DPC Trigger Status - When Set, this bit indicates that DPC has been triggered, and by definition the Port is "in DPC". DPC is event triggered. While this bit is Set, hardware must direct the LTSSM to the Disabled State. This bit must be cleared before the LTSSM can be released from the Disabled State, after which the Port is no longer in DPC, and the LTSSM must transition to the Detect State. See § Section 6.2.11 for requirements on how long software must leave the Downstream Port in DPC. Once these requirements are met, software is permitted to clear this bit regardless of the state of other status bits associated with the triggering event. After clearing this bit, software must honor timing requirements defined in § Section 6.6.1 with respect to the first Configuration Read following a Conventional Reset. Default value of this bit is 0b. | RW1CS |
| 2:1 | DPC Trigger Reason - This field indicates why DPC has been triggered. Defined encodings are: 00b = DPC was triggered due to an unmasked uncorrectable error; 01b = DPC was triggered due to receiving an ERR_NONFATAL; 10b = DPC was triggered due to receiving an ERR_FATAL; 11b = DPC was triggered due to a reason that is indicated by the DPC Trigger Reason Extension field. This field is valid only when the DPC Trigger Status bit is Set; otherwise the value of this field is undefined. | ROS |
| 3 | DPC Interrupt Status - This bit is Set if DPC is triggered while the DPC Interrupt Enable bit is Set. This may cause the generation of an interrupt. See § Section 6.2.11.1. Default value of this bit is 0b. | RW1CS |

---

<!-- 📄 Page 1332 -->
---

**Table 7-264 (cont.). DPC Status Register | 表 7-264（续）. DPC 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4 | DPC RP Busy - When the DPC Trigger Status bit is Set and this bit is Set, the Root Port is busy with internal activity that must complete before software is permitted to Clear the DPC Trigger Status bit. If software Clears the DPC Trigger Status bit while this bit is Set, the behavior is undefined. This field is valid only when the DPC Trigger Status bit is Set; otherwise the value of this field is undefined. This bit is applicable only for Root Ports that support RP Extensions for DPC, and is Reserved for Switch Downstream Ports. Default value of this bit is undefined. | RO/RsvdZ |
| 6:5 | DPC Trigger Reason Extension - This field serves as an extension to the DPC Trigger Reason field. When that field is valid and has a value of 11b, this field indicates why DPC has been triggered. Defined encodings are: 00b = DPC was triggered due to an RP PIO error; 01b = DPC was triggered due to the DPC Software Trigger bit; 10b = Reserved; 11b = Reserved. This field is valid only when the DPC Trigger Status bit is Set and the value of the DPC Trigger Reason field is 11b; otherwise the value of this field is undefined. | ROS |
| 12:8 | RP PIO First Error Pointer - The value of this field identifies a bit position in the RP PIO Status Register, and this field is considered valid when that bit is Set. When this field is valid, and software writes a 1b to the indicated RP PIO Status bit (thus clearing it), this field must revert to its default value. This field is applicable only for Root Ports that support RP Extensions for DPC, and otherwise is Reserved. If this field is not Reserved, its default value is 1 1111b, indicating a permanently Reserved RP PIO Status bit, thus guaranteeing that this field is not considered valid. | ROS/RsvdZ |
| 13 | DPC SIG_SFW Status - If the Function supports ERR_COR Subclass capability, this bit must be implemented; otherwise, it must be hardwired to 0b. If implemented, this bit is Set when a SIG_SFW ERR_COR Message is sent to signal a DPC event. See § Section 6.2.11.2 and § Section 6.2.11.5. Default value of this bit is 0b. | RW1CS/RsvdZ |

---

<a id="sec-7-9-14-5"></a>
## 7.9.14.5 DPC Error Source ID Register (Offset 0Ah) | DPC 错误源 ID 寄存器（偏移 0Ah）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.5 DPC Error Source ID Register (Offset 0Ah)

</td>
<td style="background-color:#e8e8e8">

7.9.14.5 DPC 错误源 ID 寄存器（DPC Error Source ID Register，偏移 0Ah）

</td>
</tr>
</tbody>
</table>

> **Figure 7-301.** DPC Error Source ID Register
> <img src="figures/chapter_07/fig_1332_1_tight.png" width="700">


---

<!-- 📄 Page 1333 -->
---

**Table 7-265. DPC Error Source ID Register | 表 7-265. DPC 错误源 ID 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | DPC Error Source ID - When the DPC Trigger Reason field indicates that DPC was triggered due to the reception of an ERR_NONFATAL or ERR_FATAL, this register contains the Requester ID of the received Message. Otherwise, the value of this register is undefined. | ROS |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This register is present only in Root Ports that support RP Extensions for DPC. See § Section 6.2.11.3.

</td>
<td style="background-color:#e8e8e8">

此寄存器仅在支持 DPC RP 扩展（RP Extensions for DPC）的根端口中存在。参见 § Section 6.2.11.3。

</td>
</tr>
</tbody>
</table>

> **Figure 7-302.** RP PIO Status Register
> <img src="figures/chapter_07/fig_1333_1_tight.png" width="700">


---

**Table 7-266. RP PIO Status Register | 表 7-266. RP PIO 状态寄存器**

| Bit Location | Register Description | Attributes | Default |
|--------------|----------------------|------------|---------|
| 0 | Cfg UR Cpl - Configuration Request received UR Completion | RW1CS | 0b |
| 1 | Cfg CA Cpl - Configuration Request received CA Completion | RW1CS | 0b |
| 2 | Cfg CTO - Configuration Request Completion Timeout | RW1CS | 0b |
| 8 | I/O UR Cpl - I/O Request received UR Completion | RW1CS | 0b |
| 9 | I/O CA Cpl - I/O Request received CA Completion | RW1CS | 0b |
| 10 | I/O CTO - I/O Request Completion Timeout | RW1CS | 0b |
| 16 | Mem UR Cpl - Memory Request received UR Completion | RW1CS | 0b |
| 17 | Mem CA Cpl - Memory Request received CA Completion | RW1CS | 0b |
| 18 | Mem CTO - Memory Request Completion Timeout | RW1CS | 0b |
| 31 | Permanently_Reserved - Permanently Reserved, since the default RP PIO First Error Pointer field value points to it. | RsvdZ | 0b |

---

<a id="sec-7-9-14-6"></a>
## 7.9.14.6 RP PIO Status Register (Offset 0Ch) | RP PIO 状态寄存器（偏移 0Ch）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.14.6 RP PIO Status Register (Offset 0Ch)

</td>
<td style="background-color:#e8e8e8">

7.9.14.6 RP PIO 状态寄存器（RP PIO Status Register，偏移 0Ch）

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1334 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This register is present only in Root Ports that support RP Extensions for DPC. See § Section 6.2.11.3.

</td>
<td style="background-color:#e8e8e8">

此寄存器仅在支持 DPC RP 扩展（RP Extensions for DPC）的根端口中存在。参见 § Section 6.2.11.3。

</td>
</tr>
</tbody>
</table>

> **Figure 7-303.** RP PIO Mask Register
> <img src="figures/chapter_07/fig_1334_1_tight.png" width="700">


---

**Table 7-267. RP PIO Mask Register | 表 7-267. RP PIO 屏蔽寄存器**

| Bit Location | Register Description | Attributes | Default |
|--------------|----------------------|------------|---------|
| 0 | Cfg UR Cpl - Configuration Request received UR Completion | RWS | 1b |
| 1 | Cfg CA Cpl - Configuration Request received CA Completion | RWS | 1b |
| 2 | Cfg CTO - Configuration Request Completion Timeout | RWS | 1b |
| 8 | I/O UR Cpl - I/O Request received UR Completion | RWS | 1b |
| 9 | I/O CA Cpl - I/O Request received CA Completion | RWS | 1b |
| 10 | I/O CTO - I/O Request Completion Timeout | RWS | 1b |
| 16 | Mem UR Cpl - Memory Request received UR Completion | RWS | 1b |
| 17 | Mem CA Cpl - Memory Request received CA Completion | RWS | 1b |
| 18 | Mem CTO - Memory Request Completion Timeout | RWS | 1b |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This register is present only in Root Ports that support RP Extensions for DPC. See § Section 6.2.11.3.

</td>
<td style="background-color:#e8e8e8">

此寄存器仅在支持 DPC RP 扩展（RP Extensions for DPC）的根端口中存在。参见 § Section 6.2.11.3。

</td>
</tr>
</tbody>
</table>

---

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

---

<a id="sec-7-9-14-7"></a>
## 7.9.14.7 RP PIO Mask Register (Offset 10h) | RP PIO 屏蔽寄存器 (偏移 10h)

<!-- 📄 Page 1335 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Reserved for future definition.

</td>
<td style="background-color:#e8e8e8">

保留供未来定义使用。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-8"></a>
## 7.9.14.8 RP PIO Severity Register (Offset 14h) | RP PIO 严重程度寄存器 (偏移 14h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Figure 7-304 RP PIO Severity Register**

> <img src="figures/chapter_07/fig_1335_1_tight.png" width="700">

**Table 7-268 RP PIO Severity Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 0 | Cfg UR Cpl - Configuration Request received UR Completion | RWS | 0b |
| 1 | Cfg CA Cpl - Configuration Request received CA Completion | RWS | 0b |
| 2 | Cfg CTO - Configuration Request Completion Timeout | RWS | 0b |
| 8 | I/O UR Cpl - I/O Request received UR Completion | RWS | 0b |
| 9 | I/O CA Cpl - I/O Request received CA Completion | RWS | 0b |
| 10 | I/O CTO - I/O Request Completion Timeout | RWS | 0b |
| 16 | Mem UR Cpl - Memory Request received UR Completion | RWS | 0b |
| 17 | Mem CA Cpl - Memory Request received CA Completion | RWS | 0b |
| 18 | Mem CTO - Memory Request Completion Timeout | RWS | 0b |

This register is present only in Root Ports that support RP Extensions for DPC. See § Section 6.2.11.3.

</td>
<td style="background-color:#e8e8e8">

**图 7-304 RP PIO 严重程度寄存器**


**表 7-268 RP PIO 严重程度寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 0 | Cfg UR Cpl —— 配置请求接收到 UR 完成报文 | RWS | 0b |
| 1 | Cfg CA Cpl —— 配置请求接收到 CA 完成报文 | RWS | 0b |
| 2 | Cfg CTO —— 配置请求完成超时 | RWS | 0b |
| 8 | I/O UR Cpl —— I/O 请求接收到 UR 完成报文 | RWS | 0b |
| 9 | I/O CA Cpl —— I/O 请求接收到 CA 完成报文 | RWS | 0b |
| 10 | I/O CTO —— I/O 请求完成超时 | RWS | 0b |
| 16 | Mem UR Cpl —— 内存请求接收到 UR 完成报文 | RWS | 0b |
| 17 | Mem CA Cpl —— 内存请求接收到 CA 完成报文 | RWS | 0b |
| 18 | Mem CTO —— 内存请求完成超时 | RWS | 0b |

此寄存器仅存在于支持 DPC 的 RP 扩展 (RP Extensions for DPC) 的根端口 (Root Port) 中。参见 § 第 6.2.11.3 节。

<img src="figures/chapter_07/fig_1335_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-9"></a>
## 7.9.14.9 RP PIO SysError Register (Offset 18h) | RP PIO 系统错误寄存器 (偏移 18h)

<!-- 📄 Page 1336 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Figure 7-305 RP PIO SysError Register**

> <img src="figures/chapter_07/fig_1336_1_tight.png" width="700">

**Table 7-269 RP PIO SysError Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 0 | Cfg UR Cpl - Configuration Request received UR Completion | RWS | 0b |
| 1 | Cfg CA Cpl - Configuration Request received CA Completion | RWS | 0b |
| 2 | Cfg CTO - Configuration Request Completion Timeout | RWS | 0b |
| 8 | I/O UR Cpl - I/O Request received UR Completion | RWS | 0b |
| 9 | I/O CA Cpl - I/O Request received CA Completion | RWS | 0b |
| 10 | I/O CTO - I/O Request Completion Timeout | RWS | 0b |
| 16 | Mem UR Cpl - Memory Request received UR Completion | RWS | 0b |
| 17 | Mem CA Cpl - Memory Request received CA Completion | RWS | 0b |
| 18 | Mem CTO - Memory Request Completion Timeout | RWS | 0b |

This register is present only in Root Ports that support RP Extensions for DPC. See § Section 6.2.11.3.

</td>
<td style="background-color:#e8e8e8">

**图 7-305 RP PIO 系统错误寄存器**


**表 7-269 RP PIO 系统错误寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 0 | Cfg UR Cpl —— 配置请求接收到 UR 完成报文 | RWS | 0b |
| 1 | Cfg CA Cpl —— 配置请求接收到 CA 完成报文 | RWS | 0b |
| 2 | Cfg CTO —— 配置请求完成超时 | RWS | 0b |
| 8 | I/O UR Cpl —— I/O 请求接收到 UR 完成报文 | RWS | 0b |
| 9 | I/O CA Cpl —— I/O 请求接收到 CA 完成报文 | RWS | 0b |
| 10 | I/O CTO —— I/O 请求完成超时 | RWS | 0b |
| 16 | Mem UR Cpl —— 内存请求接收到 UR 完成报文 | RWS | 0b |
| 17 | Mem CA Cpl —— 内存请求接收到 CA 完成报文 | RWS | 0b |
| 18 | Mem CTO —— 内存请求完成超时 | RWS | 0b |

此寄存器仅存在于支持 DPC 的 RP 扩展 (RP Extensions for DPC) 的根端口 (Root Port) 中。参见 § 第 6.2.11.3 节。

<img src="figures/chapter_07/fig_1336_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-10"></a>
## 7.9.14.10 RP PIO Exception Register (Offset 1Ch) | RP PIO 异常寄存器 (偏移 1Ch)

<!-- 📄 Page 1337 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Figure 7-306 RP PIO Exception Register**

> <img src="figures/chapter_07/fig_1337_1_tight.png" width="700">

**Table 7-270 RP PIO Exception Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 0 | Cfg UR Cpl - Configuration Request received UR Completion | RWS | 0b |
| 1 | Cfg CA Cpl - Configuration Request received CA Completion | RWS | 0b |
| 2 | Cfg CTO - Configuration Request Completion Timeout | RWS | 0b |
| 8 | I/O UR Cpl - I/O Request received UR Completion | RWS | 0b |
| 9 | I/O CA Cpl - I/O Request received CA Completion | RWS | 0b |
| 10 | I/O CTO - I/O Request Completion Timeout | RWS | 0b |
| 16 | Mem UR Cpl - Memory Request received UR Completion | RWS | 0b |
| 17 | Mem CA Cpl - Memory Request received CA Completion | RWS | 0b |
| 18 | Mem CTO - Memory Request Completion Timeout | RWS | 0b |

This register is implemented only in Root Ports that support RP Extensions for DPC. The RP PIO Header Log Register contains the header from the Request TLP associated with a recorded RP PIO error. Refer to § Section 6.2.11.3 for further details. In Non-Flit Mode, this register is 16 bytes. In Flit Mode, this register is between 52 and 76 bytes and is split into two portions at Offset 20h and Offset 34h. In both Flit Mode and Non-Flit Mode, this register is formatted identically to the Header Log register in AER. See § Section 7.8.4.8.

</td>
<td style="background-color:#e8e8e8">

**图 7-306 RP PIO 异常寄存器**


**表 7-270 RP PIO 异常寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 0 | Cfg UR Cpl —— 配置请求接收到 UR 完成报文 | RWS | 0b |
| 1 | Cfg CA Cpl —— 配置请求接收到 CA 完成报文 | RWS | 0b |
| 2 | Cfg CTO —— 配置请求完成超时 | RWS | 0b |
| 8 | I/O UR Cpl —— I/O 请求接收到 UR 完成报文 | RWS | 0b |
| 9 | I/O CA Cpl —— I/O 请求接收到 CA 完成报文 | RWS | 0b |
| 10 | I/O CTO —— I/O 请求完成超时 | RWS | 0b |
| 16 | Mem UR Cpl —— 内存请求接收到 UR 完成报文 | RWS | 0b |
| 17 | Mem CA Cpl —— 内存请求接收到 CA 完成报文 | RWS | 0b |
| 18 | Mem CTO —— 内存请求完成超时 | RWS | 0b |

此寄存器仅在支持 DPC 的 RP 扩展 (RP Extensions for DPC) 的根端口 (Root Port) 中实现。RP PIO Header Log 寄存器包含与所记录的 RP PIO 错误相关联的请求 TLP (Request TLP) 的包头 (Header)。详见 § 第 6.2.11.3 节。在非 Flit 模式 (Non-Flit Mode) 下,此寄存器为 16 字节。在 Flit 模式 (Flit Mode) 下,此寄存器大小介于 52 与 76 字节之间,并被拆分为偏移 20h 和偏移 34h 两部分。在 Flit 模式和非 Flit 模式下,此寄存器的格式与 AER 中的 Header Log 寄存器完全相同。参见 § 第 7.8.4.8 节。

<img src="figures/chapter_07/fig_1337_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-11"></a>
## 7.9.14.11 RP PIO Header Log Register (Offset 20h) | RP PIO Header Log 寄存器 (偏移 20h)

<!-- 📄 Page 1338 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Figure 7-307 RP PIO Header Log Register**

> <img src="figures/chapter_07/fig_1338_1_tight.png" width="700">

**Table 7-271 RP PIO Header Log Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 127:0 | TLP Header - of the TLP associated with the error | ROS | 0 |

This register is permitted to be implemented only in Root Ports that support RP Extensions for DPC. The RP PIO ImpSpec Log Register, if implemented, contains implementation specific information associated with the recorded error, e.g., indicating the source of the Request TLP. Space is allocated for this register if the value of the RP PIO Log Size field is 5 or greater. If space is allocated for the register, but the register is not implemented, the bits must be hardwired to 0b.

**Figure 7-308 RP PIO ImpSpec Log Register**


**Table 7-272 RP PIO ImpSpec Log Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 31:0 | RP PIO ImpSpec Log | ROS | 0 |

This register is permitted to be implemented only in Root Ports that support RP Extensions for DPC.

In Non-Flit Mode, the RP PIO TLP Prefix Log Register contains any End-End TLP Prefixes from the TLP corresponding to a recorded RP PIO error. Refer to § Section 6.2.11.3 for further details.

In Flit Mode, the RP PIO TLP Prefix Log Register does not exist and this configration space is a contination of the RP PIO TLP Header Log Register.

</td>
<td style="background-color:#e8e8e8">

**图 7-307 RP PIO Header Log 寄存器**


**表 7-271 RP PIO Header Log 寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 127:0 | TLP Header —— 与该错误相关联的 TLP 的包头 | ROS | 0 |

此寄存器仅允许在支持 DPC 的 RP 扩展 (RP Extensions for DPC) 的根端口 (Root Port) 中实现。如果实现 RP PIO ImpSpec Log 寄存器,则其包含与所记录错误相关的实现特定信息,例如指明请求 TLP (Request TLP) 的来源。当 RP PIO Log Size 字段的值大于等于 5 时,会为此寄存器分配空间。如果已为此寄存器分配空间但未实现,则这些位必须硬连线 (hardwired) 为 0b。

**图 7-308 RP PIO ImpSpec Log 寄存器**


**表 7-272 RP PIO ImpSpec Log 寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 31:0 | RP PIO ImpSpec Log | ROS | 0 |

此寄存器仅允许在支持 DPC 的 RP 扩展 (RP Extensions for DPC) 的根端口 (Root Port) 中实现。

在非 Flit 模式 (Non-Flit Mode) 下,RP PIO TLP Prefix Log 寄存器包含与所记录 RP PIO 错误对应的 TLP 中的所有端到端 TLP 前缀 (End-End TLP Prefixes)。详见 § 第 6.2.11.3 节。

在 Flit 模式 (Flit Mode) 下,不存在 RP PIO TLP Prefix Log 寄存器,该配置空间是 RP PIO TLP Header Log 寄存器的延续。

<img src="figures/chapter_07/fig_1338_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-12"></a>
## 7.9.14.12 RP PIO ImpSpec Log Register (Offset 30h) | RP PIO ImpSpec Log 寄存器 (偏移 30h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

See § Section 7.9.14.11 above for the register description.

</td>
<td style="background-color:#e8e8e8">

寄存器描述见上文 § 第 7.9.14.11 节。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-14-13"></a>

<!-- 📄 Page 1339 -->
---

## 7.9.14.13 RP PIO TLP Prefix Log Register (Offset 34h) | RP PIO TLP Prefix Log 寄存器 (偏移 34h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

If the Root Port supports tracking Non-Posted Requests that contain End-End TLP Prefixes, this register must be implemented, and must be of sufficient size to record the maximum number of End-End TLP Prefixes for any tracked Request. See § Section 2.9.3. The allocated size in DWORDs of the RP PIO TLP Prefix Log Register is the RP PIO Log Size minus 5 if the RP PIO Log Size is 9 or less, or 4 if the RP PIO Log Size is greater than 9. The implemented size of the TLP Prefix Log must be less than or equal to the Root Port's Max End-End TLP Prefixes field value. For the case where the Root Port never transmits Non-Posted Requests containing End-End TLP Prefixes, the allocated and implemented size of the TLP Prefix Log is permitted to be 0. Any DWORDs allocated but not implemented must be hardwired to zero.

This register is formatted identically to the TLP Prefix Log register in AER, although this register's allocated size is variable, whereas the register in AER is always 4 DWORDs. See § Section 7.8.4.12. The First TLP Prefix Log register contains the first End-End TLP Prefix from the TLP, the Second TLP Prefix Log register contains the second End-End TLP Prefix, and so forth. If the TLP contains fewer TLP Prefixes than this register accommodates, any remaining TLP Prefix Log registers must contain zero.

**Figure 7-309 RP PIO TLP Prefix Log Register**

> <img src="figures/chapter_07/fig_1339_1_tight.png" width="700">

**Table 7-273 RP PIO TLP Prefix Log Register**

| Bit Location | Register Description | Attributes | Default |
|---|---|---|---|
| 127:0 | RP PIO TLP Prefix Log | ROS | 0 |

</td>
<td style="background-color:#e8e8e8">

如果根端口 (Root Port) 支持跟踪包含端到端 TLP 前缀 (End-End TLP Prefixes) 的 Non-Posted 请求,则必须实现此寄存器,且其大小必须足以记录任何被跟踪请求的最大端到端 TLP 前缀数。参见 § 第 2.9.3 节。RP PIO TLP Prefix Log 寄存器以 DWORD 为单位分配的大小为:当 RP PIO Log Size 小于等于 9 时,为 RP PIO Log Size 减 5;当 RP PIO Log Size 大于 9 时,为 RP PIO Log Size 减 4。TLP Prefix Log 的实现大小必须小于或等于根端口 (Root Port) 的 Max End-End TLP Prefixes 字段值。对于根端口 (Root Port) 从不发送包含端到端 TLP 前缀 (End-End TLP Prefixes) 的 Non-Posted 请求的情况,TLP Prefix Log 的分配大小和实现大小均允许为 0。任何已分配但未实现的 DWORD 必须硬连线 (hardwired) 为零。

此寄存器的格式与 AER 中的 TLP Prefix Log 寄存器完全相同,但此寄存器的分配大小是可变的,而 AER 中的寄存器始终为 4 个 DWORD。参见 § 第 7.8.4.12 节。First TLP Prefix Log 寄存器包含 TLP 中的第一个端到端 TLP 前缀 (End-End TLP Prefix),Second TLP Prefix Log 寄存器包含第二个端到端 TLP 前缀,依此类推。如果 TLP 包含的 TLP 前缀数量少于本寄存器所能容纳的数量,则任何剩余的 TLP Prefix Log 寄存器必须为零。

**图 7-309 RP PIO TLP Prefix Log 寄存器**


**表 7-273 RP PIO TLP Prefix Log 寄存器**

| 位位置 | 寄存器描述 | 属性 | 默认值 |
|---|---|---|---|
| 127:0 | RP PIO TLP Prefix Log | ROS | 0 |

<img src="figures/chapter_07/fig_1339_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-15"></a>

<!-- 📄 Page 1340 -->
---

## 7.9.15 Precision Time Measurement Extended Capability (PTM Extended Capability) | 精确时间测量扩展能力 (PTM Extended Capability)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Precision Time Measurement Extended Capability is an optional Extended Capability for discovering and controlling the distribution of a PTM Hierarchy. For Root Complexes, this Capability is required in any Root Port, RCiEP, or RCRB that supports PTM. For Functions associated with an Upstream Port that support PTM, this Capability is required in exactly one Function of that Upstream Port and that Capability controls the PTM behavior of all PTM capable Functions associated with that Upstream Port. For Switch Downstream Ports, PTM behavior is controlled by the same PTM Capability that controls the associated Switch Upstream Port. The PTM Capability is not permitted in Bridges, Switch Downstream Ports, and Root Complex Event Collectors.

For Switches, a single instance of this Capability controls behavior for the entire Switch. If the Upstream Port of the Switch is associated with an MFD, it is not required that the controlling Function be the Function corresponding to the Switch Upstream Port. For a given Switch, if this Capability is present, all Downstream Ports of the Switch must implement the requirements defined in § Section 6.21.3.2.

**Figure 7-310 PTM Extended Capability Structure**

> <img src="figures/chapter_07/fig_1340_1_tight.png" width="700">

**Figure 7-311 PTM Extended Capability Header**

> <img src="figures/chapter_07/fig_1340_2_tight.png" width="700">

**Table 7-274 PTM Extended Capability Header**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. PCI Express Extended Capability ID for the Precision Time Measurement Capability is 001Fh. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. | RO |

</td>
<td style="background-color:#e8e8e8">

精确时间测量 (Precision Time Measurement, PTM) 扩展能力是一种可选的扩展能力,用于发现和控制 PTM 层级 (PTM Hierarchy) 的分布。对于根复合体 (Root Complex),任何支持 PTM 的根端口 (Root Port)、RCiEP 或 RCRB 都必须具备此能力。对于与支持 PTM 的上游端口 (Upstream Port) 相关联的 Function,此上游端口中必须恰好有一个 Function 具备此能力,且该能力控制与该上游端口相关联的所有具备 PTM 能力的 Function 的 PTM 行为。对于交换机 (Switch) 的下游端口 (Downstream Port),其 PTM 行为由控制该关联交换机上游端口 (Switch Upstream Port) 的同一 PTM 能力来控制。桥 (Bridge)、交换机下游端口 (Switch Downstream Port) 以及根复合体事件收集器 (Root Complex Event Collector) 不允许使用 PTM 能力。

对于交换机 (Switch),此能力的一个单一实例控制整个交换机的行为。如果交换机的上游端口 (Upstream Port) 与 MFD 相关联,则不要求控制 Function 为对应于交换机上游端口 (Switch Upstream Port) 的 Function。对于给定的交换机,如果存在此能力,则该交换机的所有下游端口 (Downstream Port) 必须实现 § 第 6.21.3.2 节中定义的要求。

**图 7-310 PTM 扩展能力结构**


**图 7-311 PTM 扩展能力包头**


**表 7-274 PTM 扩展能力包头**

| 位位置 | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID —— 该字段是由 PCI-SIG 定义的 ID 号,用于指示扩展能力的性质和格式。精确时间测量 (PTM) 能力的 PCI Express 扩展能力 ID 为 001Fh。 | RO |
| 19:16 | Capability Version —— 该字段是由 PCI-SIG 定义的版本号,用于指示所存在能力结构的版本。对于本版本的规范,必须为 1h。 | RO |
| 31:20 | Next Capability Offset —— 该字段包含指向下一个 PCI Express 扩展能力结构的偏移地址;如果链表中的能力已无其他项,则为 000h。 | RO |

<img src="figures/chapter_07/fig_1340_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-15-1"></a>
## 7.9.15.1 PTM Extended Capability Header (Offset 00h) | PTM 扩展能力包头 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

See § Section 7.9.15 above and § Figure 7-311 / § Table 7-274 for the register description.

</td>
<td style="background-color:#e8e8e8">

寄存器描述见上文 § 第 7.9.15 节及 § 图 7-311 / § 表 7-274。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-15-2"></a>

<!-- 📄 Page 1341 -->
---

## 7.9.15.2 PTM Capability Register (Offset 04h) | PTM 能力寄存器 (偏移 04h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This register describes a Function's support for Precision Time Measurement. Not all fields within this register apply to all Functions capable of implementing PTM.

**Figure 7-312 PTM Capability Register**

> <img src="figures/chapter_07/fig_1341_1_tight.png" width="700">

**Table 7-275 PTM Capability Register**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 0 | PTM Requester Capable - Indicates the Function implements the PTM Requester role (see § Section 6.21.3.1). Endpoints and RCiEPs are permitted to Set this bit to indicate that they implement the PTM Requester role. Switch Upstream Ports must Set this bit if the Switch contains one or more of the following: <br/> • A Downstream Port that implements the PTM Responder role. <br/> • An additional Function that implements the PTM Requester role. | HwInit |
| 1 | PTM Responder Capable - Root Ports and RCRBs are permitted to, and Switches supporting PTM must, Set this bit to indicate they implement the PTM Responder role (see § Section 6.21.3.2). If PTM Root Capable is Set, then this bit must be Set. | HwInit |
| 2 | PTM Root Capable - Root Ports, RCRBs, and Switches are permitted to Set this bit if they are capable of being a source of PTM Master Time (see § Section 6.21.1). All other Functions must hardwire this bit to 0b. | HwInit |
| 3 | ePTM Capable - If Set, indicates that this device supports Enhanced Precision Time Measurement (ePTM). This bit MUST@FLIT be Set in all PTM Devices. | HwInit |
| 4 | PTM Propagation Delay Adaptation Capable – When Set, this field indicates the Port supports the PTM Propagation Delay Adaptation Capability, controlled via the PTM Propagation Delay Adaptation Interpretation B bit in the Link Control Register. For a Switch, when Set in the Upstream Port of the Switch, indicates that the Upstream Port and all Downstream Ports of the Switch support the PTM Propagation Delay Adaptation Capability, controlled per Port via the PTM Propagation Delay Adaptation Interpretation B bit in the Link Control Register of each Port. | HwInit |
| 15:8 | Local Clock Granularity - Encodings are: <br/> 0000 0000b: Time Source does not implement a local clock. It simply propagates timing information obtained from further Upstream in the PTM Hierarchy when responding to PTM Request messages. <br/> 0000 0001b to 1111 1110b: Indicates the period of this Time Source's local clock in ns. <br/> 1111 1111b: Indicates the period of this Time Source's local clock is greater than 254 ns. | HwInit/RsvdP |

</td>
<td style="background-color:#e8e8e8">

该寄存器描述 Function 对精确时间测量 (PTM) 的支持情况。该寄存器中的字段并非全部适用于所有能够实现 PTM 的 Function。

**图 7-312 PTM 能力寄存器**


**表 7-275 PTM 能力寄存器**

| 位位置 | 寄存器描述 | 属性 |
|---|---|---|
| 0 | PTM Requester Capable —— 指示该 Function 实现了 PTM Requester 角色 (参见 § 第 6.21.3.1 节)。允许端点 (Endpoint) 和 RCiEP 置位 (Set) 此位以指示其实现了 PTM Requester 角色。如果交换机 (Switch) 包含以下一项或多项,则其上游端口 (Switch Upstream Port) 必须置位 (Set) 此位: <br/> • 实现了 PTM Responder 角色的下游端口 (Downstream Port)。 <br/> • 另一个实现了 PTM Requester 角色的 Function。 | HwInit |
| 1 | PTM Responder Capable —— 允许根端口 (Root Port) 和 RCRB 置位 (Set) 此位,支持 PTM 的交换机 (Switch) 必须置位 (Set) 此位,以指示其实现了 PTM Responder 角色 (参见 § 第 6.21.3.2 节)。如果 PTM Root Capable 被置位 (Set),则此位必须被置位 (Set)。 | HwInit |
| 2 | PTM Root Capable —— 根端口 (Root Port)、RCRB 和交换机 (Switch) 如果能够作为 PTM 主时间 (PTM Master Time) 的源,则允许置位 (Set) 此位 (参见 § 第 6.21.1 节)。所有其他 Function 必须将此位硬连线 (hardwired) 为 0b。 | HwInit |
| 3 | ePTM Capable —— 置位 (Set) 时,指示该设备支持增强型精确时间测量 (Enhanced Precision Time Measurement, ePTM)。在所有 PTM 设备中,此位 MUST@FLIT 被置位 (Set)。 | HwInit |
| 4 | PTM Propagation Delay Adaptation Capable —— 置位 (Set) 时,该字段指示端口 (Port) 支持 PTM 传播延迟适配能力 (PTM Propagation Delay Adaptation Capability),该能力通过 Link Control 寄存器中的 PTM Propagation Delay Adaptation Interpretation B 位进行控制。对于交换机 (Switch),在其上游端口 (Switch Upstream Port) 中置位 (Set) 时,指示该上游端口 (Upstream Port) 和交换机的所有下游端口 (Downstream Port) 均支持 PTM 传播延迟适配能力,该能力通过每个端口 (Port) 的 Link Control 寄存器中的 PTM Propagation Delay Adaptation Interpretation B 位按端口 (Port) 进行控制。 | HwInit |
| 15:8 | Local Clock Granularity —— 编码方式如下: <br/> 0000 0000b:时间源 (Time Source) 未实现本地时钟,仅在响应 PTM 请求消息时转发从 PTM 层级 (PTM Hierarchy) 中更上游获取的定时信息。 <br/> 0000 0001b 至 1111 1110b:指示该时间源 (Time Source) 的本地时钟周期(单位:ns)。 <br/> 1111 1111b:指示该时间源 (Time Source) 的本地时钟周期大于 254 ns。 | HwInit/RsvdP |

<img src="figures/chapter_07/fig_1341_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-15-3"></a>

<!-- 📄 Page 1342 -->
---

## 7.9.15.3 PTM Control Register (Offset 08h) | PTM 控制寄存器 (偏移 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

If the PTM Root Select bit is Set, this local clock is used to provide PTM Master Time. Otherwise, the Time Source uses this local clock to locally track PTM Master Time received from further Upstream within a PTM Hierarchy.

This field is RsvdP if the PTM Root Capable bit is 0b.

This register controls a Function's participation in the Precision Time Measurement mechanism. Not all fields within this register apply to all Functions capable of implementing PTM.

**Figure 7-313 PTM Control Register**

> <img src="figures/chapter_07/fig_1342_1_tight.png" width="700">

**Table 7-276 PTM Control Register**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 0 | PTM Enable - When Set, this Function is permitted to participate in the PTM mechanism according to its selected role(s) (see § Section 6.21.2). Default value is 0b. | RW |
| 1 | Root Select - When Set, if the PTM Enable bit is also Set, this Time Source is the PTM Root. Within each PTM Hierarchy, it is recommended that system software select only the furthest Upstream Time Source to be the PTM Root. Default value is 0b. If the value of the PTM Root Capable bit is 0b, this bit is permitted to be hardwired to 0b. | RW/RO |
| 15:8 | Effective Granularity - For Functions implementing the PTM Requester Role, this field provides information relating to the expected accuracy of the PTM clock, but does not otherwise affect the PTM mechanism. <br/> For Endpoints, system software must program this field to the value representing the maximum Local Clock Granularity reported by the PTM Root and all intervening PTM Time Sources. <br/> For RCiEPs, system software must set this field to the value reported in the Local Clock Granularity field by the associated PTM Time Source. <br/> Permitted values: <br/> 0000 0000b: Unknown PTM granularity - one or more Switches between this Function and the PTM Root reported a Local Clock Granularity value of 0000 0000b. <br/> 0000 0001b to 1111 1110b: Indicates the effective PTM granularity in ns. <br/> 1111 1111b: Indicates the effective PTM granularity is greater than 254 ns. <br/> Default value is 0000 0000b. If PTM Requester Capable is Clear, this field is permitted to be hardwired to 0000 0000b. | RW/RO |

</td>
<td style="background-color:#e8e8e8">

如果 PTM Root Select 位置位 (Set),则使用该本地时钟提供 PTM 主时间 (PTM Master Time)。否则,时间源 (Time Source) 使用该本地时钟在本地跟踪从 PTM 层级 (PTM Hierarchy) 中更上游接收到的 PTM 主时间 (PTM Master Time)。

如果 PTM Root Capable 位为 0b,则该字段为 RsvdP。

该寄存器控制 Function 对精确时间测量 (PTM) 机制的参与。该寄存器中的字段并非全部适用于所有能够实现 PTM 的 Function。

**图 7-313 PTM 控制寄存器**


**表 7-276 PTM 控制寄存器**

| 位位置 | 寄存器描述 | 属性 |
|---|---|---|
| 0 | PTM Enable —— 置位 (Set) 时,该 Function 允许根据其所选定的角色参与 PTM 机制 (参见 § 第 6.21.2 节)。默认值为 0b。 | RW |
| 1 | Root Select —— 置位 (Set) 时,如果 PTM Enable 位也被置位 (Set),则该时间源 (Time Source) 为 PTM Root。在每个 PTM 层级 (PTM Hierarchy) 中,建议系统软件仅选择最上游的时间源 (Time Source) 作为 PTM Root。默认值为 0b。如果 PTM Root Capable 位的值为 0b,则允许将此位硬连线 (hardwired) 为 0b。 | RW/RO |
| 15:8 | Effective Granularity —— 对于实现 PTM Requester 角色的 Function,该字段提供与 PTM 时钟预期精度相关的信息,但不会以其他方式影响 PTM 机制。 <br/> 对于端点 (Endpoint),系统软件必须将该字段编程为由 PTM Root 及所有中间 PTM 时间源 (Time Source) 所报告的最大本地时钟粒度 (Local Clock Granularity) 所对应的值。 <br/> 对于 RCiEP,系统软件必须将该字段设置为关联的 PTM 时间源 (Time Source) 在 Local Clock Granularity 字段中报告的值。 <br/> 允许值: <br/> 0000 0000b:未知 PTM 粒度 —— 该 Function 与 PTM Root 之间的一个或多个交换机 (Switch) 报告了 Local Clock Granularity 值为 0000 0000b。 <br/> 0000 0001b 至 1111 1110b:指示有效 PTM 粒度(单位:ns)。 <br/> 1111 1111b:指示有效 PTM 粒度大于 254 ns。 <br/> 默认值为 0000 0000b。如果 PTM Requester Capable 为清零 (Clear),则允许将该字段硬连线 (hardwired) 为 0000 0000b。 | RW/RO |

<img src="figures/chapter_07/fig_1342_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-16"></a>

<!-- 📄 Page 1343 -->
---

## 7.9.16 Readiness Time Reporting Extended Capability | 就绪时间报告扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Readiness Time Reporting Extended Capability provides an optional mechanism for describing the time required for a Device or Function to become Configuration-Ready. In the indicated situations, software is permitted to issue Requests to the Device or Function after waiting for the time advertised in this capability and need not wait for the (longer) times required elsewhere.

Software is permitted to issue requests upon the earliest of:
- Receiving a Readiness Notifications message (see § Section 6.22).
- Waiting the appropriate time as specified in this document or in applicable specifications including the [PCI] and the [PCI-PM].
- Waiting the time indicated in the associated field of this capability.
- Waiting the time defined by system software or firmware[^184].

Software is permitted to cache values from this capability and to use those cached values as long as the same device operating in the same manner has not changed.

This capability is permitted to be implemented in all Functions.

The capability is optional for PFs and VFs. However, if a VF associated with a given PF contains the capability, all VFs associated with that PF must contain the capability and report the same time values.

For VFs, see § Section 5.10.1). Other Functions must be Configuration-Ready if:
- The Immediate Readiness bit is Clear and at least Reset Time has elapsed after the completion of Conventional Reset
  - If the Immediate Readiness bit is Set, Reset Time does not apply, and is Reserved
- The Function is associated with an Upstream Port and at least DL_Up Time has elapsed after the Downstream Port above that Function reported Data Link Layer Link Active (see § Section 7.5.3.8).
- The Function supports Function Level Reset and at least FLR Time has elapsed after that Function was issued a Function Level Reset.
- Immediate_Readiness_on_Return_to_D0 is Clear and at least D3Hot to D0 Time has elapsed after that Function was directed to the D0 state from D3Hot.
  - If the Immediate_Readiness_on_Return_to_D0 bit is Set, D3Hot to D0 Time does not apply, and is Reserved

When Immediate_Readiness_on_Return_to_D0 is Clear, a Function must be Configuration-Ready when at least D3Hot to D0 Time has elapsed after the Function was directed to the D0 state from D3Hot. In addition, the Function must be in either the D0uninitialized or D0active state, depending on the value of the No_Soft_Reset bit.

[^184]: For example, using ACPI tables to provide the equivalent of this capability.

</td>
<td style="background-color:#e8e8e8">

就绪时间报告 (Readiness Time Reporting) 扩展能力提供了一种可选机制,用于描述设备 (Device) 或 Function 变为配置就绪 (Configuration-Ready) 所需的时间。在所述情况下,软件在等待该能力中所通告的时间后,即允许向设备 (Device) 或 Function 发出请求 (Requests),而无需等待其他位置规定的(更长的)时间。

允许软件在满足以下最早一项条件时发出请求:
- 收到 Readiness Notifications 消息 (参见 § 第 6.22 节)。
- 等待本文档或适用规范 (包括 [PCI] 和 [PCI-PM]) 中规定的相应时间。
- 等待本能力相关字段中指示的时间。
- 等待由系统软件或固件定义的时间[^184]。

允许软件缓存来自该能力的值,并在相同设备以相同方式运行且未发生变化期间一直使用这些缓存值。

允许在所有 Function 中实现该能力。

该能力对于 PF 和 VF 是可选的。然而,如果与给定 PF 关联的某个 VF 包含该能力,则与该 PF 关联的所有 VF 都必须包含该能力,并报告相同的时间值。

对于 VF,参见 § 第 5.10.1 节。其他 Function 在满足下列条件时必须处于配置就绪 (Configuration-Ready) 状态:
- Immediate Readiness 位为清零 (Clear),且常规复位 (Conventional Reset) 完成之后至少已过去 Reset Time(复位时间)
  - 如果 Immediate Readiness 位置位 (Set),则 Reset Time 不适用,且为保留
- Function 与上游端口 (Upstream Port) 相关联,且在该 Function 上游的下游端口 (Downstream Port) 报告数据链路层链路活跃 (Data Link Layer Link Active) 之后至少已过去 DL_Up Time (参见 § 第 7.5.3.8 节)。
- Function 支持功能级复位 (Function Level Reset),且在该 Function 发出功能级复位 (Function Level Reset) 之后至少已过去 FLR Time。
- Immediate_Readiness_on_Return_to_D0 为清零 (Clear),且在该 Function 从 D3Hot 转入 D0 状态后至少已过去 D3Hot to D0 Time。
  - 如果 Immediate_Readiness_on_Return_to_D0 位置位 (Set),则 D3Hot to D0 Time 不适用,且为保留

当 Immediate_Readiness_on_Return_to_D0 为清零 (Clear) 时,在 Function 从 D3Hot 转入 D0 状态后,必须至少经过 D3Hot to D0 Time 后该 Function 才进入配置就绪 (Configuration-Ready) 状态。此外,根据 No_Soft_Reset 位的值,该 Function 必须处于 D0uninitialized 或 D0active 状态。

[^184]: 例如,使用 ACPI 表提供与该能力等效的信息。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-16-1"></a>

<!-- 📄 Page 1344 -->
---

## 7.9.16.1 Readiness Time Reporting Extended Capability Header (Offset 00h) | 就绪时间报告扩展能力包头 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

If the above conditions do not apply, Function behavior is not determined by the Readiness Time Reporting Extended Capability, and the Function must respond as defined elsewhere (including, for example, no response or a response with Configuration Retry Status).

The time values reported are determined by implementation specific mechanisms. A Valid bit is defined in this capability to permit a device to defer reporting time values, for example to allow hardware initialization through driver-based mechanisms. If the Valid bit remains Clear and 1 minute has elapsed after device driver(s) have started, software is permitted to assume that no values will be reported.

Registers and fields in the Readiness Time Reporting Extended Capability are shown in § Figure 7-314. Time values are encoded in floating point as shown in § Figure 7-315. The actual time value is Value × Multiplier[Scale]. For example, the value A1Eh represents about 1 second (actually 1.006 sec) and the value 80Ah represents about 10 ms (actually 10.240 ms).

**Figure 7-314 Readiness Time Reporting Extended Capability**

> <img src="figures/chapter_07/fig_1344_1_tight.png" width="700">

**Figure 7-315 Readiness Time Encoding**

> <img src="figures/chapter_07/fig_1344_2_tight.png" width="700">

<!-- 📄 Page 1345 -->
---

§ Figure 7-316 and § Table 7-278 detail allocation of fields in the Extended Capability header.

**Figure 7-316 Readiness Time Reporting Extended Capability Header**

> <img src="figures/chapter_07/fig_1345_1_tight.png" width="700">

**Table 7-278 Readiness Time Reporting Extended Capability Header**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the Readiness Time Reporting Extended Capability is 0022h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

</td>
<td style="background-color:#e8e8e8">

如果上述条件不适用,则 Function 的行为不由就绪时间报告 (Readiness Time Reporting) 扩展能力确定,该 Function 必须按照其他位置定义的方式响应 (包括例如,无响应或返回 Configuration Retry Status 的响应)。

所报告的时间值由实现特定机制决定。该能力中定义了一个 Valid 位,以允许设备延迟报告时间值,例如允许通过基于驱动程序的机制进行硬件初始化。如果 Valid 位保持清零 (Clear),且自设备驱动程序启动后已过去 1 分钟,则软件可假设不会再报告任何值。

就绪时间报告 (Readiness Time Reporting) 扩展能力中的寄存器和字段如 § 图 7-314 所示。时间值按 § 图 7-315 所示的浮点格式编码。实际时间值为 Value × Multiplier[Scale]。例如,值 A1Eh 表示约 1 秒 (实际为 1.006 秒),值 80Ah 表示约 10 ms (实际为 10.240 ms)。

**图 7-314 就绪时间报告扩展能力**


**图 7-315 就绪时间编码**


§ 图 7-316 和 § 表 7-278 详细说明了扩展能力包头中字段的分配。

**图 7-316 就绪时间报告扩展能力包头**


**表 7-278 就绪时间报告扩展能力包头**

| 位位置 | 寄存器描述 | 属性 |
|---|---|---|
| 15:0 | PCI Express Extended Capability ID —— 该字段是由 PCI-SIG 定义的 ID 号,用于指示扩展能力的性质和格式。就绪时间报告 (Readiness Time Reporting) 扩展能力的扩展能力 ID 为 0022h。 | RO |
| 19:16 | Capability Version —— 该字段是由 PCI-SIG 定义的版本号,用于指示所存在能力结构的版本。对于本版本的规范,必须为 1h。 | RO |
| 31:20 | Next Capability Offset —— 该字段包含指向下一个 PCI Express 能力结构的偏移地址;如果链表中的能力已无其他项,则为 000h。对于在配置空间 (Configuration Space) 中实现的扩展能力,该偏移地址相对于 PCI 兼容配置空间 (PCI-compatible Configuration Space) 的起始位置,因此必须始终为 000h (用于终止能力链表) 或大于 0FFh。 | RO |

<img src="figures/chapter_07/fig_1344_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

§ Figure 7-317 and § Table 7-279 detail allocation of fields in the Readiness Time Reporting 1 Register.

**Figure 7-317 Readiness Time Reporting 1 Register**

> <img src="figures/chapter_07/fig_1345_2_tight.png" width="700">

**Table 7-279 Readiness Time Reporting 1 Register**

| Bit Location | Register Description | Attributes |
|---|---|---|
| 11:0 | Reset Time - is the time a non-VF Function requires to become Configuration-Ready after the completion of Conventional Reset. For VF semantics, see § Section 9.3.3.3.1. This field is RsvdP if the Immediate Readiness bit is Set. This field is undefined when the Valid bit is Clear. This field must be less than or equal to the encoded value A1Eh. | HwInit/RsvdP || 11:0 | Reset Time - is the time a non-VF Function requires to become Configuration-Ready after the completion of Conventional Reset. For VF semantics, see § Section 9.3.3.3.1. This field is RsvdP if the Immediate Readiness bit is Set. This field is undefined when the Valid bit is Clear. This field must be less than or equal to the encoded value A1Eh. | HwInit/RsvdP |

---

<a id="sec-7-9-16-2"></a>
## 7.9.16.2 Readiness Time Reporting 1 Register (Offset 04h) | 就绪时间报告 1 寄存器（偏移 04h）


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1346 -->
---

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 23:12 | **DL_Up Time** - is the time the Function requires to become Configuration-Ready after the Downstream Port above the Function reports Data Link Layer Link Active. <br>This field is RsvdP in Functions that are not associated with an Upstream Port. <br>For VFs, this field is not applicable and is RsvdP. <br>This field is undefined when the Valid bit is Clear. <br>This field must be less than or equal to the encoded value A1Eh. | HwInit/RsvdP <br>VF RsvdP |
| 31 | **Valid** - If Set, indicates that all time values in this capability are valid. If Clear, indicates that the time values in this capability are not yet available. <br>Time values may depend on device configuration. Device specific mechanisms, possibly involving the device driver(s), could be involved in determining time values. <br>If this bit remains Clear and 1 minute has elapsed after all associated device driver(s) have started, software is permitted to assume that this bit will never be set. | HwInit |

Figure 7-318 and Table 7-280 detail allocation of fields in the Readiness Time Reporting 2 Register.

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1346 -->
---

| 比特位置 | 寄存器描述 | 属性 |
|----------|------------|------|
| 23:12 | **DL_Up Time（DL_Up 时间）** — 是该 Function 在其上游的 Downstream Port 报告数据链路层（Data Link Layer）链路激活（Link Active）之后，达到 Configuration-Ready 状态所需的时间。 <br>对于不与 Upstream Port 关联的 Function，此字段为 RsvdP。 <br>对于 VF，该字段不适用且为 RsvdP。 <br>当 Valid 位为 0 时，此字段未定义。 <br>此字段必须小于或等于编码值 A1Eh。 | HwInit/RsvdP <br>VF RsvdP |
| 31 | **Valid（有效）** — 若置 1，表示本能力结构中的所有时间值有效。若为 0，表示本能力结构中的时间值尚不可用。 <br>时间值可能依赖于设备配置。设备特定的机制（可能涉及设备驱动程序）可能参与确定时间值。 <br>如果该位在所有相关设备驱动程序启动后 1 分钟内仍保持为 0，则软件可假定该位将永远不会被置 1。 | HwInit |

图 7-318 和表 7-280 详细说明了 Readiness Time Reporting 2 寄存器中各字段的分配。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-16-fig-318"></a>
## Figure 7-318. Readiness Time Reporting 2 Register | 图 7-318. 就绪时间报告 2 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```
 0          11        23       31
+-----------+---------+--------+
|  FLR Time | D3Hot to| RsvdP  |
|           | D0 Time |        |
+-----------+---------+--------+
```

**Figure 7-318 Readiness Time Reporting 2 Register**

</td>
<td style="background-color:#e8e8e8">

```
 0          11        23       31
+-----------+---------+--------+
|  FLR Time | D3Hot to| 保留   |
|           | D0 Time |        |
+-----------+---------+--------+
```

**图 7-318 就绪时间报告 2 寄存器**

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-16-3"></a>
## 7.9.16.3 Readiness Time Reporting 2 Register (Offset 08h) | 就绪时间报告 2 寄存器（偏移 08h）


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Table 7-280 Readiness Time Reporting 2 Register**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 11:0 | **FLR Time** - is the time that the Function requires to become Configuration-Ready after it was issued an FLR. <br>This field is RsvdP when the Function Level Reset Capability bit is Clear (see § Section 7.5.3.3). <br>This field is undefined when the Valid bit is Clear. <br>This field must be less than or equal to the encoded value A1Eh. | HwInit/RsvdP |
| 23:12 | **D3Hot to D0 Time** - If Immediate_Readiness_on_Return_to_D0 is Clear, D3Hot to D0 Time is the time that a non-VF Function requires after it is directed from D3Hot to D0 before it is Configuration-Ready and has returned to either D0uninitialized or D0active state. For VF semantics, see § Section 5.10.1. <br>This field is RsvdP if the Immediate_Readiness_on_Return_to_D0 bit is Set. <br>For a VF that does not implement the PCI Power Management Capability, this field is undefined. <br>This field is undefined when the Valid bit is Clear. <br>This field must be less than or equal to the encoded value 80Ah. | HwInit/RsvdP |

</td>
<td style="background-color:#e8e8e8">

**表 7-280 就绪时间报告 2 寄存器**

| 比特位置 | 寄存器描述 | 属性 |
|----------|------------|------|
| 11:0 | **FLR Time（FLR 时间）** — 是该 Function 在被发出 FLR 之后，达到 Configuration-Ready 状态所需的时间。 <br>当 Function Level Reset Capability 位为 0 时（参见 § 第 7.5.3.3 节），此字段为 RsvdP。 <br>当 Valid 位为 0 时，此字段未定义。 <br>此字段必须小于或等于编码值 A1Eh。 | HwInit/RsvdP |
| 23:12 | **D3Hot to D0 Time（D3Hot 到 D0 时间）** — 如果 Immediate_Readiness_on_Return_to_D0 为 0，则 D3Hot 到 D0 时间是非 VF Function 在被指示从 D3Hot 转换到 D0 之后，达到 Configuration-Ready 并返回到 D0uninitialized 或 D0active 状态所需的时间。有关 VF 语义，请参见 § 第 5.10.1 节。 <br>如果 Immediate_Readiness_on_Return_to_D0 位置 1，则此字段为 RsvdP。 <br>对于未实现 PCI Power Management Capability 的 VF，此字段未定义。 <br>当 Valid 位为 0 时，此字段未定义。 <br>此字段必须小于或等于编码值 80Ah。 | HwInit/RsvdP |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17"></a>
## 7.9.17 Hierarchy ID Extended Capability | 层级 ID 扩展能力（Hierarchy ID Extended Capability）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1347 -->
---

The Hierarchy ID Extended Capability provides an optional mechanism for passing a unique identifier to Functions within a Hierarchy. At most one instance of this capability is permitted in a Function. This capability is not applicable to Bridges, Root Complex Event Collectors, and RCRBs.

This capability takes three forms:

**In Upstream Ports:**

- This capability is permitted any Function associated with an Upstream Port.
- This capability is optional in Switch Upstream Ports. Support in Switch Upstream and Downstream Ports is independently optional.
- This capability is mandatory in Functions that use the Hierarchy ID Message. This includes use by the Function's driver.
- Functions, other than VFs, that have Hierarchy ID Writeable Clear, must report the Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID fields from the most recently received Hierarchy ID Message.
- All VFs that have Hierarchy ID Writeable Clear, must report the same Hierarchy ID Valid, Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID values as their associated PF.
- PFs must implement this capability if any of their VFs implement this capability.
- Functions that have Hierarchy ID Writeable Set must report the Hierarchy ID Valid, Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID values programmed by software.

**In Downstream Ports:**

- This capability is permitted in any Downstream Port. It is recommended that it be implemented in Root Ports.
- When present in a Switch Downstream Port, this capability must be implemented in all Downstream Ports of the Switch. Support in Switch Upstream and Downstream Ports is independently optional.
- In Downstream Ports, the Hierarchy ID, System GUID Authority ID, and System GUID fields are Read / Write and contain the values to send in the Hierarchy ID Message.
- A Hierarchy ID capability is not affected by Hierarchy ID Messages forwarded through the associated Downstream Port.

**In RCiEPs:**

- VFs that have Hierarchy ID Writeable Clear must report the same Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID values as their associated PF.
- PFs must implement this capability if any of their VFs implement this capability.
- Functions, other than VFs, that have Hierarchy ID Writeable Clear, must report the same Hierarchy ID Valid, Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID values. The source of this information is outside the scope of this specification.
- Functions that have Hierarchy ID Writeable Set must report the Hierarchy ID Valid, Message Requester ID, Hierarchy ID, System GUID Authority ID, and System GUID values programmed by software.

Figure 7-319 details the layout of the Hierarchy ID Extended Capability.

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1347 -->
---

层级 ID 扩展能力（Hierarchy ID Extended Capability）提供了一种可选机制，用于将唯一标识符传递给层级（Hierarchy）内的 Function。每个 Function 中最多允许此能力的一个实例。该能力不适用于桥（Bridge）、根复合体事件收集器（Root Complex Event Collector）以及 RCRB。

该能力有三种形式：

**在 Upstream Port 中：**

- 任何与 Upstream Port 关联的 Function 都允许实现此能力。
- 在 Switch Upstream Port 中此能力是可选的。Switch 上 Upstream Port 和 Downstream Port 中的支持彼此独立可选。
- 使用 Hierarchy ID Message 的 Function 必须实现此能力。这包括由 Function 的驱动程序使用的情况。
- 除 VF 之外、且 Hierarchy ID Writeable 为 0 的 Function，必须报告从最近接收到的 Hierarchy ID Message 中获取的 Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 字段。
- 所有 Hierarchy ID Writeable 为 0 的 VF，必须报告与其关联 PF 相同的 Hierarchy ID Valid、Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 值。
- 如果 PF 的任何 VF 实现了此能力，则 PF 必须实现此能力。
- Hierarchy ID Writeable 为 1 的 Function，必须报告由软件编程的 Hierarchy ID Valid、Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 值。

**在 Downstream Port 中：**

- 任何 Downstream Port 都允许实现此能力。建议在根端口（Root Port）中实现。
- 当 Switch Downstream Port 中存在此能力时，Switch 的所有 Downstream Port 必须实现此能力。Switch 上 Upstream Port 和 Downstream Port 中的支持彼此独立可选。
- 在 Downstream Port 中，Hierarchy ID、System GUID Authority ID 和 System GUID 字段为读/写（Read/Write），其包含要在 Hierarchy ID Message 中发送的值。
- 层级 ID 能力不受通过其关联 Downstream Port 转发的 Hierarchy ID Message 的影响。

**在 RCiEP 中：**

- Hierarchy ID Writeable 为 0 的 VF，必须报告与其关联 PF 相同的 Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 值。
- 如果 PF 的任何 VF 实现了此能力，则 PF 必须实现此能力。
- 除 VF 之外、且 Hierarchy ID Writeable 为 0 的 Function，必须报告相同的 Hierarchy ID Valid、Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 值。此信息的来源不在本规范的范围内。
- Hierarchy ID Writeable 为 1 的 Function，必须报告由软件编程的 Hierarchy ID Valid、Message Requester ID、Hierarchy ID、System GUID Authority ID 和 System GUID 值。

图 7-319 详细说明了 Hierarchy ID 扩展能力的布局。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-319"></a>
## Figure 7-319. Hierarchy ID Extended Capability | 图 7-319. 层级 ID 扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```
Byte Offset   0               3
              +---------------+
+000h         | PCI Express Extended Capability Header |
              +---------------+
+004h         | Hierarchy ID Status Register           |
              +---------------+
+008h         | Hierarchy ID Data Register              |
              +---------------+
+00Ch         | Hierarchy ID GUID 1 Register            |
              +---------------+
+010h         | Hierarchy ID GUID 2 Register            |
              +---------------+
+014h         | Hierarchy ID GUID 3 Register            |
              +---------------+
+018h         | Hierarchy ID GUID 4 Register            |
              +---------------+
+01Ch         | Hierarchy ID GUID 5 Register            |
              +---------------+
```

**Figure 7-319 Hierarchy ID Extended Capability**

Figure 7-320 and Table 7-281 detail allocation of fields in the Hierarchy ID Extended Capability Header.

</td>
<td style="background-color:#e8e8e8">

```
字节偏移     0               3
              +---------------+
+000h         | PCI Express 扩展能力头                  |
              +---------------+
+004h         | 层级 ID 状态寄存器                       |
              +---------------+
+008h         | 层级 ID 数据寄存器                       |
              +---------------+
+00Ch         | 层级 ID GUID 1 寄存器                   |
              +---------------+
+010h         | 层级 ID GUID 2 寄存器                   |
              +---------------+
+014h         | 层级 ID GUID 3 寄存器                   |
              +---------------+
+018h         | 层级 ID GUID 4 寄存器                   |
              +---------------+
+01Ch         | 层级 ID GUID 5 寄存器                   |
              +---------------+
```

**图 7-319 层级 ID 扩展能力**

> <img src="figures/chapter_07/fig_1348_1_tight.png" width="700">


图 7-320 和表 7-281 详细说明了层级 ID 扩展能力头中各字段的分配。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-320"></a>
## Figure 7-320. Hierarchy ID Extended Capability Header | 图 7-320. 层级 ID 扩展能力头

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1348 -->
---

```
 0           15  16      19  20              31
+-------------+---+-------+------------------+
| Extended    |   | Cap.  | Next Capability  |
| Capability  |   | Vers. | Offset           |
| ID          |   |       |                  |
+-------------+---+-------+------------------+
```

**Figure 7-320 Hierarchy ID Extended Capability Header**

**Table 7-281 Hierarchy ID Extended Capability Header**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 15:0 | **Extended Capability ID** - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. <br>PCI Express Extended Capability ID for the Hierarchy ID Extended Capability is 0028h. | RO |
| 19:16 | **Capability Version** - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. <br>Must be 1h for this version of the specification. | RO |
| 31:20 | **Next Capability Offset** - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities in configuration space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating the list of Capabilities) or greater than 0FFh. | RO |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1348 -->
---

```
 0           15  16      19  20              31
+-------------+---+-------+------------------+
| 扩展能力    |   | 能力  | 下一能力偏移     |
| ID          |   | 版本  |                  |
+-------------+---+-------+------------------+
```

**图 7-320 层级 ID 扩展能力头**

> <img src="figures/chapter_07/fig_1348_2_tight.png" width="700">


**表 7-281 层级 ID 扩展能力头**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 15:0 | **Extended Capability ID（扩展能力 ID）** — 此字段是 PCI-SIG 定义的 ID 编号，用于指示扩展能力的性质和格式。 <br>层级 ID 扩展能力的 PCI Express 扩展能力 ID 为 0028h。 | RO |
| 19:16 | **Capability Version（能力版本）** — 此字段是 PCI-SIG 定义的版本号，用于指示当前能力结构的版本。 <br>对于本版本的规范必须为 1h。 | RO |
| 31:20 | **Next Capability Offset（下一能力偏移）** — 此字段包含到下一个 PCI Express 扩展能力结构的偏移量，如果链接的能力列表中没有其他项则为 000h。对于配置空间中的扩展能力，此偏移相对于 PCI 兼容配置空间的起始位置，因此必须始终为 000h（用于终止能力列表）或大于 0FFh。 | RO |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-1"></a>
## 7.9.17.1 Hierarchy ID Extended Capability Header (Offset 00h) | 层级 ID 扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-320 and Table 7-281 for field allocation details of the Hierarchy ID Extended Capability Header.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID 扩展能力头的字段分配详细信息，请参见图 7-320 和表 7-281。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-321"></a>
## Figure 7-321. Hierarchy ID Status Register | 图 7-321. 层级 ID 状态寄存器


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1349 -->
---

```
 0           15  16      27  28  29             30   31
+-------------+---+-------+----+----------------+----+
| Message     |   | RsvdZ |    | Hierarchy ID   | H  | H
| Requester   |   |       |    | Writeable      | V  | I
| ID          |   |       |    |                | F  | D
|             |   |       |    |                | C  |   |
|             |   |       |    |                |    | V  |
+-------------+---+-------+----+----------------+----+
```

**Figure 7-321 Hierarchy ID Status Register**

**Table 7-282 Hierarchy ID Status Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 15:0 | **Message Requester ID** - In an Upstream Port, this field contains the Requester ID from the most recently received Hierarchy ID Message. This field is meaningful only if Hierarchy ID Valid is 1b. This value identifies the Downstream Port (within this Hierarchy) that sent the Hierarchy ID Message. This information is not considered part of the Hierarchy ID as it can vary within the Hierarchy (e.g., different Root Ports of one Root Complex), but helps in debug situations to identify the provenance of the Hierarchy ID information. <br>In a Downstream Port, this field is RsvdZ. <br>For RCiEPs, this field is RsvdZ. <br>This field defaults to 0000h. | RO/RsvdZ |
| 28 | **Hierarchy ID Writeable** - This bit is Set to indicate that the Hierarchy ID Data and GUID registers are read/write. This bit is Clear to indicate that the Hierarchy ID and GUID registers are read only. <br>In Downstream Ports this bit is hardwired to 1b. <br>In Upstream Ports, Functions that are not VFs must hardwire this bit to 0b. <br>RCiEPs that are not VFs, must hardwire this bit to either 0b or 1b. <br>VFs in an Upstream Port and Root Complex Integrated VFs are permitted to either: <br>• hardwire this bit to 0b or <br>• implement this bit as read / write with a default value of 0b. | RW/RO |
| 29 | **Hierarchy ID VF Configurable** - This bit indicates that Hierarchy ID Writeable can be configured. <br>If Hierarchy ID Writeable is implemented as read / write, this bit is 1b. Otherwise this bit is 0b. | RO |
| 30 | **Hierarchy ID Pending** - In Downstream Ports this requests the transmittion of a Hierarchy ID Message. Setting it requests transmission of a message based on the Hierarchy Data and GUID registers in this capability. This bit is cleared when either the transmit request is satisfied or the Link enters DL_Down. <br>Behavior is undefined if the Hierarchy Data or GUID registers in this capability are written while this bit is Set. <br>In Downstream Ports, this bit is Read / Write defaulting to 0b. <br>In all other Functions, this bit is RsvdZ. | RW/RsvdZ |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1349 -->
---

```
 0           15  16      27  28  29             30   31
+-------------+---+-------+----+----------------+----+
| Message     |   | 保留  |    | 层级 ID        | H  | H
| Requester   |   |       |    | 可写           | V  | I
| ID          |   |       |    |                | F  | D
|             |   |       |    |                | C  |   |
|             |   |       |    |                |    | V  |
+-------------+---+-------+----+----------------+----+
```

**图 7-321 层级 ID 状态寄存器**

> <img src="figures/chapter_07/fig_1349_1_tight.png" width="700">


**表 7-282 层级 ID 状态寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 15:0 | **Message Requester ID（消息请求者 ID）** — 在 Upstream Port 中，此字段包含最近接收到的 Hierarchy ID Message 中的 Requester ID。仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。此值标识发送 Hierarchy ID Message 的（本层级内的）Downstream Port。此信息不视为层级 ID 的一部分，因为它在同一层级内可能变化（例如同一根复合体（Root Complex）的不同根端口），但有助于在调试时识别层级 ID 信息的来源。 <br>在 Downstream Port 中，此字段为 RsvdZ。 <br>对于 RCiEP，此字段为 RsvdZ。 <br>此字段默认值为 0000h。 | RO/RsvdZ |
| 28 | **Hierarchy ID Writeable（层级 ID 可写）** — 该位置 1 表示 Hierarchy ID Data 和 GUID 寄存器为读/写。该位为 0 表示 Hierarchy ID 和 GUID 寄存器为只读。 <br>在 Downstream Port 中，该位硬连线为 1b。 <br>在 Upstream Port 中，非 VF 的 Function 必须将该位硬连线为 0b。 <br>非 VF 的 RCiEP 必须将该位硬连线为 0b 或 1b。 <br>Upstream Port 中的 VF 和根复合体集成 VF（Root Complex Integrated VF）可任选以下方式： <br>• 将该位硬连线为 0b； <br>• 将该位实现为读/写，默认值为 0b。 | RW/RO |
| 29 | **Hierarchy ID VF Configurable（层级 ID VF 可配置）** — 此位表示 Hierarchy ID Writeable 可以被配置。 <br>如果 Hierarchy ID Writeable 被实现为读/写，则此位为 1b；否则此位为 0b。 | RO |
| 30 | **Hierarchy ID Pending（层级 ID 待处理）** — 在 Downstream Port 中，此位用于请求发送 Hierarchy ID Message。置 1 时将基于本能力中的 Hierarchy Data 和 GUID 寄存器请求发送消息。当发送请求被满足或链路（Link）进入 DL_Down 时，该位被清零。 <br>当此位被置 1 时，若写入本能力中的 Hierarchy Data 或 GUID 寄存器，则行为未定义。 <br>在 Downstream Port 中，此位为读/写，默认值为 0b。 <br>在其他所有 Function 中，此位为 RsvdZ。 | RW/RsvdZ |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-2"></a>
## 7.9.17.2 Hierarchy ID Status Register (Offset 04h) | 层级 ID 状态寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-321 and Table 7-282 for field allocation details of the Hierarchy ID Status Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID 状态寄存器的字段分配详细信息，请参见图 7-321 和表 7-282。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-322"></a>
## Figure 7-322. Hierarchy ID Data Register (continued) | 图 7-322. 层级 ID 数据寄存器（续）


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1350 -->
---

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31 | **Hierarchy ID Valid** - This bit indicates that the remaining fields in this capability are meaningful. <br>In Downstream Ports, this bit is hardwired to 1b. <br>In all other Functions, the following rules apply: <br>• If Hierarchy ID Writeable is Set, this bit is read/write, default 0b. <br>• If Hierarchy ID Writeable is Clear, this bit is read only, default 0b. <br>&nbsp;&nbsp;◦ In VFs, this bit contains the same value as the associated PF. <br>&nbsp;&nbsp;◦ In Functions other than VFs that are associated with an Upstream Port, this bit is Set when a Hierarchy ID Message is received, and Cleared when the Link is DL_Down. <br>&nbsp;&nbsp;◦ In RCiEPs other than VFs, this bit contains a system provided value. The mechanism for determining this value is outside the scope of this specification. | RW/RO |

Figure 7-322 and Table 7-283 detail allocation of fields in the Hierarchy ID Data Register.

```
 0           7   8        15  16              31
+-------------+---+-------+------------------+
| System GUID |   | RsvdP | Hierarchy ID     |
| Authority   |   |       |                  |
| ID          |   |       |                  |
+-------------+---+-------+------------------+
```

**Figure 7-322 Hierarchy ID Data Register**

**Table 7-283 Hierarchy ID Data Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 7:0 | **System GUID Authority ID** - This field corresponds to the System GUID Authority ID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 00h. | RO/RW |
| 31:16 | **Hierarchy ID** - This field corresponds to the Hierarchy ID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1350 -->
---

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 31 | **Hierarchy ID Valid（层级 ID 有效）** — 此位表示本能力中其余字段是否有意义。 <br>在 Downstream Port 中，此位硬连线为 1b。 <br>在其他所有 Function 中，适用以下规则： <br>• 如果 Hierarchy ID Writeable 被置 1，则此位为读/写，默认值为 0b。 <br>• 如果 Hierarchy ID Writeable 为 0，则此位为只读，默认值为 0b。 <br>&nbsp;&nbsp;◦ 在 VF 中，此位包含与关联 PF 相同的值。 <br>&nbsp;&nbsp;◦ 在与 Upstream Port 关联的非 VF Function 中，收到 Hierarchy ID Message 时该位被置 1，当链路为 DL_Down 时该位被清零。 <br>&nbsp;&nbsp;◦ 在非 VF 的 RCiEP 中，此位包含由系统提供的值。用于确定此值的机制不在本规范范围内。 | RW/RO |

图 7-322 和表 7-283 详细说明了层级 ID 数据寄存器中各字段的分配。

```
 0           7   8        15  16              31
+-------------+---+-------+------------------+
| System GUID |   | 保留  | 层级 ID          |
| Authority   |   |       |                  |
| ID          |   |       |                  |
+-------------+---+-------+------------------+
```

**图 7-322 层级 ID 数据寄存器**

> <img src="figures/chapter_07/fig_1350_1_tight.png" width="700">


**表 7-283 层级 ID 数据寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 7:0 | **System GUID Authority ID（系统 GUID 授权 ID）** — 此字段对应于 Hierarchy ID Message 中的 System GUID Authority ID 字段。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 00h。 | RO/RW |
| 31:16 | **Hierarchy ID（层级 ID）** — 此字段对应于 Hierarchy ID Message 中的 Hierarchy ID 字段。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-3"></a>
## 7.9.17.3 Hierarchy ID Data Register (Offset 08h) | 层级 ID 数据寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-322 and Table 7-283 for field allocation details of the Hierarchy ID Data Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID 数据寄存器的字段分配详细信息，请参见图 7-322 和表 7-283。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-323"></a>
## Figure 7-323. Hierarchy ID GUID 1 Register | 图 7-323. 层级 ID GUID 1 寄存器


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1351 -->
---

```
 0           15  16              31
+-------------+---+---------------+
| System      |   |  RsvdP        |
| GUID 1      |   |               |
+-------------+---+---------------+
```

**Figure 7-323 Hierarchy ID GUID 1 Register**

**Table 7-284 Hierarchy ID GUID 1 Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 15:0 | **System GUID 1** - This field corresponds to bits [143:128] of the System GUID in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1351 -->
---

```
 0           15  16              31
+-------------+---+---------------+
| System      |   |  保留         |
| GUID 1      |   |               |
+-------------+---+---------------+
```

**图 7-323 层级 ID GUID 1 寄存器**

**表 7-284 层级 ID GUID 1 寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 15:0 | **System GUID 1（系统 GUID 1）** — 此字段对应于 Hierarchy ID Message 中 System GUID 的 [143:128] 位。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-324"></a>
## Figure 7-324. Hierarchy ID GUID 2 Register | 图 7-324. 层级 ID GUID 2 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```
 0                       31
+-------------------------+
|       System GUID 2     |
+-------------------------+
```

**Figure 7-324 Hierarchy ID GUID 2 Register**

**Table 7-285 Hierarchy ID GUID 2 Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31:0 | **System GUID 2** - This field corresponds to bits [127:96] of the System GUID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

```
 0                       31
+-------------------------+
|       System GUID 2     |
+-------------------------+
```

**图 7-324 层级 ID GUID 2 寄存器**

**表 7-285 层级 ID GUID 2 寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 31:0 | **System GUID 2（系统 GUID 2）** — 此字段对应于 Hierarchy ID Message 中 System GUID 字段的 [127:96] 位。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-4"></a>
## 7.9.17.4 Hierarchy ID GUID 1 Register (Offset 0Ch) | 层级 ID GUID 1 寄存器（偏移 0Ch）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-323 and Table 7-284 for field allocation details of the Hierarchy ID GUID 1 Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID GUID 1 寄存器的字段分配详细信息，请参见图 7-323 和表 7-284。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-5"></a>
## 7.9.17.5 Hierarchy ID GUID 2 Register (Offset 10h) | 层级 ID GUID 2 寄存器（偏移 10h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-324 and Table 7-285 for field allocation details of the Hierarchy ID GUID 2 Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID GUID 2 寄存器的字段分配详细信息，请参见图 7-324 和表 7-285。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-325"></a>
## Figure 7-325. Hierarchy ID GUID 3 Register | 图 7-325. 层级 ID GUID 3 寄存器


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1352 -->
---

```
 0                       31
+-------------------------+
|       System GUID 3     |
+-------------------------+
```

**Figure 7-325 Hierarchy ID GUID 3 Register**

**Table 7-286 Hierarchy ID GUID 3 Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31:0 | **System GUID 3** - This field corresponds to bits [95:64] of the System GUID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1352 -->
---

```
 0                       31
+-------------------------+
|       System GUID 3     |
+-------------------------+
```

**图 7-325 层级 ID GUID 3 寄存器**

**表 7-286 层级 ID GUID 3 寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 31:0 | **System GUID 3（系统 GUID 3）** — 此字段对应于 Hierarchy ID Message 中 System GUID 字段的 [95:64] 位。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-326"></a>
## Figure 7-326. Hierarchy ID GUID 4 Register | 图 7-326. 层级 ID GUID 4 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```
 0                       31
+-------------------------+
|       System GUID 4     |
+-------------------------+
```

**Figure 7-326 Hierarchy ID GUID 4 Register**

**Table 7-287 Hierarchy ID GUID 4 Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31:0 | **System GUID 4** - This field corresponds to bits [63:32] of the System GUID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

```
 0                       31
+-------------------------+
|       System GUID 4     |
+-------------------------+
```

**图 7-326 层级 ID GUID 4 寄存器**

**表 7-287 层级 ID GUID 4 寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 31:0 | **System GUID 4（系统 GUID 4）** — 此字段对应于 Hierarchy ID Message 中 System GUID 字段的 [63:32] 位。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-6"></a>
## 7.9.17.6 Hierarchy ID GUID 3 Register (Offset 14h) | 层级 ID GUID 3 寄存器（偏移 14h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-325 and Table 7-286 for field allocation details of the Hierarchy ID GUID 3 Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID GUID 3 寄存器的字段分配详细信息，请参见图 7-325 和表 7-286。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-7"></a>
## 7.9.17.7 Hierarchy ID GUID 4 Register (Offset 18h) | 层级 ID GUID 4 寄存器（偏移 18h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Refer to Figure 7-326 and Table 7-287 for field allocation details of the Hierarchy ID GUID 4 Register.

</td>
<td style="background-color:#e8e8e8">

有关层级 ID GUID 4 寄存器的字段分配详细信息，请参见图 7-326 和表 7-287。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-17-fig-327"></a>
## Figure 7-327. Hierarchy ID GUID 5 Register | 图 7-327. 层级 ID GUID 5 寄存器


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

<!-- 📄 Page 1353 -->
---

```
 0                       31
+-------------------------+
|       System GUID 5     |
+-------------------------+
```

**Figure 7-327 Hierarchy ID GUID 5 Register**

**Table 7-288 Hierarchy ID GUID 5 Register**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31:0 | **System GUID 5** - This field corresponds to bits [31:0] of the System GUID field in the Hierarchy ID Message. See § Section 6.25 for details. <br>This field is meaningful only if Hierarchy ID Valid is 1b. <br>If Hierarchy ID Writeable is Set, this field is read-write and contains the value programmed by software. <br>If Hierarchy ID Writeable is Clear, this field is read only. The value is determined using the rules defined in § Section 7.9.17. <br>This field defaults to 0000 0000h. | RO/RW |

</td>
<td style="background-color:#e8e8e8">

<!-- 📄 Page 1353 -->
---

```
 0                       31
+-------------------------+
|       System GUID 5     |
+-------------------------+
```

**图 7-327 层级 ID GUID 5 寄存器**

**表 7-288 层级 ID GUID 5 寄存器**

| 比特位置 | 描述 | 属性 |
|----------|------|------|
| 31:0 | **System GUID 5（系统 GUID 5）** — 此字段对应于 Hierarchy ID Message 中 System GUID 字段的 [31:0] 位。详情参见 § 第 6.25 节。 <br>仅当 Hierarchy ID Valid 为 1b 时此字段才有意义。 <br>如果 Hierarchy ID Writeable 被置 1，则此字段为读/写，并包含由软件编程的值。 <br>如果 Hierarchy ID Writeable 为 0，则此字段为只读。该值使用 § 第 7.9.17 节中定义的规则确定。 <br>此字段默认值为 0000 0000h。 | RO/RW |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-18-vpd-intro"></a>
## 7.9.18 Vital Product Data (VPD) Capability | 重要产品数据（VPD）能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Support of VPD is optional. All Functions are permitted to contain the capability. This includes all Functions of a Multi-Function Device associated with an Upstream Port as well as RCiEPs. This also includes PFs and VFs.

Vital Product Data (VPD) is information that uniquely identifies hardware and, potentially, software elements of a system. The VPD can provide the system with information on various Field Replaceable Units such as part number, serial number, and other detailed information. The objective from a system point of view is to make this information available to the system owner and service personnel. VPD typically resides in a storage device (for example, a serial EEPROM) associated with the Function.

VFs and PFs that implement the VPD Capability must ensure that there can be no "data leakage" between VFs and/or PFs via the VPD Capability.

Details of the VPD Data is defined in § Section 6.27.

Access to the VPD is provided using the Capabilities List in Configuration Space. The VPD Capability structure is shown in Figure 7-328.

</td>
<td style="background-color:#e8e8e8">

对 VPD 的支持是可选的。允许所有 Function 包含该能力。这包括与 Upstream Port 关联的多功能设备（Multi-Function Device）的所有 Function 以及 RCiEP。这同样包括 PF 和 VF。

重要产品数据（VPD, Vital Product Data）是用于唯一标识系统中的硬件以及可能的软件元素的信息。VPD 可向系统提供有关各种现场可更换单元（FRU, Field Replaceable Unit）的信息，例如部件编号、序列号以及其他详细信息。从系统角度看，其目标是将此信息提供给系统所有者和服务人员。VPD 通常驻留在与该 Function 关联的存储设备（例如串行 EEPROM）中。

实现 VPD 能力的 VF 和 PF 必须确保不会通过 VPD 能力在 VF 和/或 PF 之间发生"数据泄漏"。

VPD 数据的详细信息在 § 第 6.27 节中定义。

对 VPD 的访问通过配置空间（Configuration Space）中的能力列表（Capabilities List）提供。VPD 能力结构如图 7-328 所示。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


---

<a id="sec-7-9-17-8"></a>
## 7.9.17.8 Hierarchy ID GUID 5 Register (Offset 1Ch) | 层级 ID GUID 5 寄存器 (偏移 1Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.17.8 Hierarchy ID GUID 5 Register (Offset 1Ch) §

</td>
<td style="background-color:#e8e8e8">

7.9.17.8 层级 ID GUID 5 寄存器 (偏移 1Ch) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-18"></a>
## 7.9.18 Vital Product Data Capability (VPD Capability) | 重要产品数据能力 (VPD Capability)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.18 Vital Product Data Capability (VPD Capability) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.18 重要产品数据能力 (VPD Capability) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1354 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset
Capability ID
Next Capability Pointer
VPD Address Register
VPD Data Register
+000h
+004h
Figure 7-328 VPD Capability Structure

</td>
<td style="background-color:#e8e8e8">

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
字节偏移
Capability ID
Next Capability Pointer
VPD Address 寄存器
VPD Data 寄存器
+000h
+004h
图 7-328 VPD 能力结构

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The following protocols are used transfer data between the VPD Data field and the VPD storage component.

• To read VPD information:
1. Issue single write to the VPD Address Register writing the flag bit (F) to 0b and VPD Address with the address to read.
2. The hardware device will set F to 1b when 4 bytes of data from the storage component have been transferred to VPD Data.
3. Software can monitor F and, after it becomes 1b, read the VPD information from VPD Data.
Behavior is undefined if either the VPD Address or VPD Data is written, prior to the flag bit becoming 1b.

• To write VPD information to the read/write portion of the VPD space:
1. Write the data to VPD Data
2. Then issue a single write to the VPD Address Register with F set to 1b and VPD Address set to the address where the VPD Data is to be stored.
3. The software then monitors F and when it is set to 0b (by device hardware), the VPD Data (all 4 bytes) has been transferred from VPD Data to the storage component.
If either the VPD Address or VPD Data is written, prior to F being becoming 0b, the results of the write operation to the storage component are unpredictable.
Behavior is undefined if a read or write of the storage component is requested and VPD Address is outside the range of the storage component.

The VPD (both the read only items and the read/write fields) is stored information and will have no direct control of any device operations.

The VPD Address Register is used to request a read or write of the VPD storage component.

</td>
<td style="background-color:#e8e8e8">

以下协议用于在 VPD Data 字段与 VPD 存储组件之间传输数据。

• 读取 VPD 信息:
1. 向 VPD Address 寄存器发起单次写入,将标志位 (F) 写为 0b,并将 VPD Address 写为要读取的地址。
2. 当来自存储组件的 4 字节数据已传输到 VPD Data 时,硬件设备会将 F 置为 1b。
3. 软件可以监控 F,在 F 变为 1b 之后,从 VPD Data 读取 VPD 信息。
如果在标志位变为 1b 之前对 VPD Address 或 VPD Data 进行写入,则行为未定义。

• 将 VPD 信息写入 VPD 空间的读/写部分:
1. 将数据写入 VPD Data。
2. 然后向 VPD Address 寄存器发起单次写入,F 置为 1b,VPD Address 置为 VPD Data 要存储的目标地址。
3. 随后软件监控 F,当 F 被设备硬件清为 0b 时,表示 VPD Data(全部 4 字节)已从 VPD Data 传输到存储组件。
如果在 F 变为 0b 之前对 VPD Address 或 VPD Data 进行写入,则对存储组件的写入操作结果不可预测。
如果请求对存储组件进行读或写时,VPD Address 超出存储组件的地址范围,则行为未定义。

VPD(包括只读项和读/写字段)是被存储的信息,不会对任何设备操作进行直接控制。

VPD Address 寄存器用于请求对 VPD 存储组件进行读或写。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-18-1"></a>
## 7.9.18.1 VPD Address Register | VPD Address 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.18.1 VPD Address Register §
§

</td>
<td style="background-color:#e8e8e8">

7.9.18.1 VPD Address 寄存器 §
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1355 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
14
VPD Address
15
F

</td>
<td style="background-color:#e8e8e8">

0
14
VPD Address
15
F

</td>
</tr>
</tbody>
</table>

> **Figure 7-329.** VPD Address Register
> <img src="figures/chapter_07/fig_1355_1_tight.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-289. VPD Address Register | 表 7-289. VPD Address 寄存器**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 14:0 | VPD Address - DWORD-aligned byte address of the VPD to be accessed. Behavior is undefined if the lowest 2 bits of this field are non-zero. The lowest two bits of the field must be either RW, or RO with a value of 00b. The remaining bits of the field must be RW.<br>Default is implementation specific. | RW/RO (see description) |
| 15 | F - The F bit is always written along with VPD Address. The value of F indicates the direction of transfer being requested (0b = read, 1b = write). When the transfer is complete, the F bit value changes to indicate completion (1b = read complete, 0b = write complete).<br>Default is implementation specific. | RW |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
31
VPD Data

</td>
<td style="background-color:#e8e8e8">

0
31
VPD Data

</td>
</tr>
</tbody>
</table>

> **Figure 7-330.** VPD Data Register


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-290. VPD Data Register | 表 7-290. VPD Data 寄存器**

| Bit Location | Description | Attributes |
|--------------|-------------|------------|
| 31:0 | VPD Data - VPD Data can be read through this register. The least significant byte of this register (at offset 04h in this capability structure) corresponds to the byte of VPD at the address specified by VPD Address. Behavior is undefined for any read or write of this register with Byte Enables other than 1111b.<br>Default is implementation specific. | RW |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Native PCIe Enclosure Management Extended (NPEM) Capability is an optional extended capability that is permitted to be implemented by Root Ports, Switch Downstream Ports, and Endpoints.

</td>
<td style="background-color:#e8e8e8">

原生 PCIe 机框管理扩展 (Native PCIe Enclosure Management Extended, NPEM) 能力是一个可选的扩展能力,允许由根端口 (Root Port)、交换机下游端口 (Switch Downstream Port) 以及端点 (Endpoint) 实现。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-18-2"></a>
## 7.9.18.2 VPD Data Register | VPD Data 寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.18.2 VPD Data Register §

</td>
<td style="background-color:#e8e8e8">

7.9.18.2 VPD Data 寄存器 §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19"></a>
## 7.9.19 Native PCIe Enclosure Management Extended Capability (NPEM Extended Capability) | 原生 PCIe 机框管理扩展能力 (NPEM 扩展能力)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.19 Native PCIe Enclosure Management Extended Capability (NPEM Extended Capability) §
§
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.19 原生 PCIe 机框管理扩展能力 (NPEM 扩展能力) §
§
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1356 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset
PCI Express Extended Capability Header
NPEM Capability Register
NPEM Control Register
NPEM Status Register
+000h
+004h
+008h
+00Ch

</td>
<td style="background-color:#e8e8e8">

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
字节偏移
PCI Express 扩展能力头 (Extended Capability Header)
NPEM Capability 寄存器
NPEM Control 寄存器
NPEM Status 寄存器
+000h
+004h
+008h
+00Ch

</td>
</tr>
</tbody>
</table>

> **Figure 7-331.** NPEM Extended Capability
> <img src="figures/chapter_07/fig_1356_1_tight.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
15
PCI Express Extended Capability ID
0029h
16
19
Capability Version
20
31
Next Capability Offset

</td>
<td style="background-color:#e8e8e8">

0
15
PCI Express 扩展能力 ID (Extended Capability ID)
0029h
16
19
能力版本 (Capability Version)
20
31
下一能力偏移 (Next Capability Offset)

</td>
</tr>
</tbody>
</table>

> **Figure 7-332.** NPEM Extended Capability Header
> <img src="figures/chapter_07/fig_1356_2_tight.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-291. NPEM Extended Capability Header | 表 7-291. NPEM 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the extended capability. PCI Express Extended Capability ID for the NPEM Extended Capability is 0029h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of capabilities. | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The NPEM Capability Register contains an overall NPEM Capable bit and a bit map of states supported in the implementation. Implementations are required to support OK, Locate, Fail, and Rebuild states if NPEM Capable bit is Set. All other states are optional.

</td>
<td style="background-color:#e8e8e8">

NPEM Capability 寄存器包含一个总的 NPEM Capable 位,以及实现所支持状态的位图。如果 NPEM Capable 位被置位,则实现必须支持 OK、Locate、Fail 和 Rebuild 状态。其他所有状态都是可选的。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19-1"></a>
## 7.9.19.1 NPEM Extended Capability Header (Offset 00h) | NPEM 扩展能力头 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.19.1 NPEM Extended Capability Header (Offset 00h) §

</td>
<td style="background-color:#e8e8e8">

7.9.19.1 NPEM 扩展能力头 (偏移 00h) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19-2"></a>
## 7.9.19.2 NPEM Capability Register (Offset 04h) | NPEM Capability 寄存器 (偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.19.2 NPEM Capability Register (Offset 04h) §
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.19.2 NPEM Capability 寄存器 (偏移 04h) §
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1357 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
NPEM Capable
1
NPEM Reset Capable
2
NPEM OK Capable
3
NPEM Locate Capable
4
NPEM Fail Capable
5
NPEM Rebuild Capable
6
NPEM PFA Capable
7
NPEM Hot Spare Capable
8
NPEM In A Critical Array Capable
9
NPEM In A Failed Array Capable
10
NPEM Invalid Device Type Capable
11
NPEM Disabled Capable
12
23
RsvdP
24
31
Enclosure-specific Capabilities

</td>
<td style="background-color:#e8e8e8">

0
NPEM Capable
1
NPEM Reset Capable
2
NPEM OK Capable
3
NPEM Locate Capable
4
NPEM Fail Capable
5
NPEM Rebuild Capable
6
NPEM PFA Capable
7
NPEM Hot Spare Capable
8
NPEM In A Critical Array Capable
9
NPEM In A Failed Array Capable
10
NPEM Invalid Device Type Capable
11
NPEM Disabled Capable
12
23
RsvdP
24
31
Enclosure-specific Capabilities(机框专用能力)

</td>
</tr>
</tbody>
</table>

> **Figure 7-333.** NPEM Capability Register
> <img src="figures/chapter_07/fig_1357_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-292. NPEM Capability Register | 表 7-292. NPEM Capability 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | NPEM Capable - When Set, this bit indicates that the enclosure has NPEM functionality. | HwInit |
| 1 | NPEM Reset Capable - A value of 1b indicates support for the optional NPEM Reset mechanism described in § Section 6.28. This capability is independently optional. | HwInit |
| 2 | NPEM OK Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM OK state. This bit must be Set if NPEM Capable is also Set. | HwInit |
| 3 | NPEM Locate Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM Locate state. This bit must be Set if NPEM Capable is also Set. | HwInit |
| 4 | NPEM Fail Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM Fail state. This bit must be Set if NPEM Capable is also Set. | HwInit |
| 5 | NPEM Rebuild Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM Rebuild state. This bit must be Set if NPEM Capable is also Set. | HwInit |
| 6 | NPEM PFA Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM PFA state. This capability is independently optional. | HwInit |
| 7 | NPEM Hot Spare Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM Hot Spare state. This capability is independently optional. | HwInit |
| 8 | NPEM In A Critical Array Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM In A Critical Array state. This capability is independently optional. | HwInit |
| 9 | NPEM In A Failed Array Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM In A Failed Array state. This capability is independently optional. | HwInit |
| 10 | NPEM Invalid Device Type Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM_Invalid_Device_Type state. This capability is independently optional. | HwInit |
| § | | |
| § | | |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1358 -->
---

**Table 7-292. NPEM Capability Register (continued) | 表 7-292. NPEM Capability 寄存器 (续)**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 11 | NPEM Disabled Capable - When Set, this bit indicates that enclosure has the ability to indicate the NPEM_Disabled state. This capability is independently optional. | HwInit |
| 31:24 | Enclosure-specific Capabilities - The definition of enclosure-specific bits is outside the scope of this specification. | HwInit |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The NPEM Control Register contains an overall NPEM Enable bit and a bit map of states that software controls.

Use of Enclosure-specific bits is outside the scope of this specification.

All writes to this register, including writes that do not change the register value, are NPEM commands and should eventually result in a command completion indication in the NPEM Status Register.

</td>
<td style="background-color:#e8e8e8">

NPEM Control 寄存器包含一个总的 NPEM Enable 位,以及软件所控制状态的位图。

机框专用位的使用超出本规范的范围。

对该寄存器的所有写入(包括不改变寄存器值的写入)都是 NPEM 命令,并最终应在 NPEM Status 寄存器中产生命令完成指示。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19-3"></a>
## 7.9.19.3 NPEM Control Register (Offset 08h) | NPEM Control 寄存器 (偏移 08h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
NPEM Enable
1
NPEM Initiate Reset
2
NPEM OK Control
3
NPEM Locate Control
4
NPEM Fail Control
5
NPEM Rebuild Control
6
NPEM PFA Control
7
NPEM Hot Spare Control
8
NPEM In A Critical Array Control
9
NPEM In A Failed Array Control
10
NPEM Invalid Device Type Control
11
NPEM Disabled Control
12
23
RsvdP
24
31
Enclosure-specific Controls

</td>
<td style="background-color:#e8e8e8">

0
NPEM Enable
1
NPEM Initiate Reset
2
NPEM OK Control
3
NPEM Locate Control
4
NPEM Fail Control
5
NPEM Rebuild Control
6
NPEM PFA Control
7
NPEM Hot Spare Control
8
NPEM In A Critical Array Control
9
NPEM In A Failed Array Control
10
NPEM Invalid Device Type Control
11
NPEM Disabled Control
12
23
RsvdP
24
31
Enclosure-specific Controls(机框专用控制)

</td>
</tr>
</tbody>
</table>

> **Figure 7-334.** NPEM Control Register
> <img src="figures/chapter_07/fig_1358_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-293. NPEM Control Register | 表 7-293. NPEM Control 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | NPEM Enable - When Set, this bit enables the NPEM capability. When Clear, this bit disables the NPEM capability. Default value of this bit is 0b.<br>When enabled, this capability operates as defined in this specification. When disabled, the other bits in this capability have no effect and any associated indications are outside the scope of this specification. | RW |
| 1 | NPEM Initiate Reset - If NPEM Reset Capable bit is 1b, then a write of 1b to this bit initiates NPEM Reset. If NPEM Reset Capable bit is 0b, then this bit is permitted to be read-only with a value of 0b.<br>The value read by software from this bit must always be 0b. | RW/RO |
| 2 | NPEM OK Control - When Set, this bit specifies that the NPEM OK indication be turned ON. When Clear, this bit specifies that the NPEM OK indication be turned OFF. | RW/RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19-3-detail"></a>
## 7.9.19.3 NPEM Control Register (Offset 08h) - continued | NPEM Control 寄存器 (偏移 08h) - 续

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.19.3 NPEM Control Register (Offset 08h) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.19.3 NPEM Control 寄存器 (偏移 08h) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1359 -->
---

**Table 7-293. NPEM Control Register (continued) | 表 7-293. NPEM Control 寄存器 (续)**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2 (cont.) | If NPEM OK Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 3 | NPEM Locate Control - When Set, this bit specifies that the NPEM Locate indication be turned ON. When Clear, this bit specifies that the NPEM Locate indication be turned OFF.<br>If NPEM Locate Capable bit in the NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 4 | NPEM Fail Control - When Set, this bit specifies that the NPEM Fail indication be turned ON. When Clear, this bit specifies that the NPEM Fail indication be turned OFF.<br>If NPEM Fail Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 5 | NPEM Rebuild Control - When Set, this bit specifies that the NPEM Rebuild indication be turned ON. When Clear, this bit specifies that the NPEM Rebuild indication be turned OFF.<br>If NPEM Rebuild Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 6 | NPEM PFA Control - When Set, this bit specifies that the NPEM PFA indication be turned ON. When Clear, this bit specifies that the NPEM PFA indication be turned OFF.<br>If NPEM PFA Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 7 | NPEM Hot Spare Control - When Set, this bit specifies that the NPEM Hot Spare indication be turned ON. When Clear, this bit specifies that the NPEM Hot Spare indication be turned OFF.<br>If NPEM Hot Spare Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 8 | NPEM In A Critical Array Control - When Set, this bit specifies that the NPEM In A Critical Array indication be turned ON. When Clear, this bit specifies that the NPEM In A Ciritical Array indication be turned OFF.<br>If NPEM In A Critical Array Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 9 | NPEM In A Failed Array Control - When Set, this bit specifies that the NPEM In A Failed Array indication be turned ON. When Clear, this bit specifies that the NPEM In A Failed Array indication be turned OFF.<br>If NPEM In A Failed Array Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 10 | NPEM Invalid Device Type Control - When Set, this bit specifies that the NPEM Invaild Device Type indication be turned ON. When Clear, this bit specifies that the NPEM Invalid Device Type indication be turned OFF. | RW/RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1360 -->
---

**Table 7-293. NPEM Control Register (continued) | 表 7-293. NPEM Control 寄存器 (续)**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 10 (cont.) | If NPEM Invalid Device Type Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 11 | NPEM Disabled Control - When Set, this bit specifies that the NPEM Disabled indication be turned ON. When Clear, this bit specifies that the NPEM Disabled indication be turned OFF.<br>If NPEM Disabled Capable bit in NPEM Capability Register is 0b, this bit is permitted to be read-only with a value of 0b. Default value of this bit is 0b. | RW/RO |
| 31:24 | Enclosure-specific Controls - The definition of enclosure-specific bits is outside the scope of this specification. Enclosure-specific software is permitted to change the value of this field. Other software must preserve the existing value when writing this register. Default value of this field is 00h. | RW/RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
NPEM Command Completed
1
23
RsvdZ
24
31
Enclosure-specific Status

</td>
<td style="background-color:#e8e8e8">

0
NPEM Command Completed
1
23
RsvdZ
24
31
Enclosure-specific Status(机框专用状态)

</td>
</tr>
</tbody>
</table>

> **Figure 7-335.** NPEM Status Register
> <img src="figures/chapter_07/fig_1360_1.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-294. NPEM Status Register | 表 7-294. NPEM Status 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | NPEM Command Completed - This bit is Set when an NPEM command has completed, and the NPEM controller is ready to accept a subsequent command.<br>This bit is permitted to be hardwired to 1b if the enclosure is able to accept writes that update any portion of the NPEM Control register without any delay between successive writes.<br>Default value of this bit is 0b.<br>Software must wait for an NPEM command to complete before issuing the next NPEM command. However, if this bit is not set within 1 second limit on command execution, software is permitted to repeat the NPEM command or issue the next NPEM command. If software issues a write before the Port has completed processing of the previous command and before the 1 second time limit has expired, the Port is permitted to either accept or discard the write. Such a write is considered a programming error, and could result in a discrepancy between the NPEM Control Register and the enclosure element state. To recover from such a programming error and return the enclosure to a consistent state, software must issue a write to the NPEM Control Register which conforms to the NPEM command completion rules. | RW1C / RO |
| 31:24 | Enclosure-specific Status - The definition of enclosure specific bits is outside the scope of this specification. Enclosure specific software is permitted to write non-zero values to this field. Other software must write 00h to this field. | RsvdZ/RO/RW1C |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-19-4"></a>
## 7.9.19.4 NPEM Status Register (Offset 0Ch) | NPEM Status 寄存器 (偏移 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.19.4 NPEM Status Register (Offset 0Ch) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.19.4 NPEM Status 寄存器 (偏移 0Ch) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1361 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The default value of this field is enclosure-specific.
This field is permitted to be hardwired to 00h.

The Alternate Protocol Extended Capability structure is optional in components that implement Alternate Protocol Negotiation. It is only permitted in:
• A Function associated with a Downstream Port.
• Function 0 (and only Function 0) of a Device associated with an Upstream Port.
§ Figure 7-336 details allocation of register fields in the Alternate Protocol Extended Capability structure.

</td>
<td style="background-color:#e8e8e8">

该字段的默认值是机框专用的。
该字段允许硬连线为 00h。

Alternate Protocol 扩展能力结构在实现了 Alternate Protocol Negotiation 的组件中是可选的。它仅允许出现在:
• 与下游端口 (Downstream Port) 关联的 Function 中。
• 与上游端口 (Upstream Port) 关联的 Device 的 Function 0(且仅为 Function 0)。
§ 图 7-336 详细说明了 Alternate Protocol 扩展能力结构中各寄存器的字段分配。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-20"></a>
## 7.9.20 Alternate Protocol Extended Capability | Alternate Protocol 扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.20 Alternate Protocol Extended Capability §

</td>
<td style="background-color:#e8e8e8">

7.9.20 Alternate Protocol 扩展能力 §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-20-1"></a>
## 7.9.20.1 Alternate Protocol Extended Capability Header (Offset 00h) | Alternate Protocol 扩展能力头 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.20.1 Alternate Protocol Extended Capability Header (Offset 00h) §
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.20.1 Alternate Protocol 扩展能力头 (偏移 00h) §
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Byte Offset
PCI Express Extended Capability Header
Alternate Protocol Capabilities Register
Alternate Protocol Control Register
Alternate Protocol Data 1 Register
Alternate Protocol Data 2 Register
+000h
+004h
+008h
+00Ch
+010h

</td>
<td style="background-color:#e8e8e8">

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
字节偏移
PCI Express 扩展能力头 (Extended Capability Header)
Alternate Protocol Capabilities 寄存器
Alternate Protocol Control 寄存器
Alternate Protocol Data 1 寄存器
Alternate Protocol Data 2 寄存器
+000h
+004h
+008h
+00Ch
+010h

</td>
</tr>
</tbody>
</table>

> **Figure 7-336.** Alternate Protocol Extended Capability
> <img src="figures/chapter_07/fig_1361_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-337.** Alternate Protocol Extended Capability Header
> <img src="figures/chapter_07/fig_1361_2_tight.png" width="700">

0
15
PCI Express Extended Capability ID
002Bh
16
19
Capability Version
20
31
Next Capability Offset

</td>
<td style="background-color:#e8e8e8">


0
15
PCI Express 扩展能力 ID (Extended Capability ID)
002Bh
16
19
能力版本 (Capability Version)
20
31
下一能力偏移 (Next Capability Offset)

<img src="figures/chapter_07/fig_1361_2_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-295. Alternate Protocol Extended Capability Header | 表 7-295. Alternate Protocol 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1362 -->
---

**Table 7-295. Alternate Protocol Extended Capability Header (continued) | 表 7-295. Alternate Protocol 扩展能力头 (续)**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 (cont.) | The Extended Capability ID for the Alternate Protocol Capability is 002Bh. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
7
Alternate Protocol Count
8
Alternate Protocol Selective Enable Supported
9
31
RsvdP

</td>
<td style="background-color:#e8e8e8">

0
7
Alternate Protocol Count
8
Alternate Protocol Selective Enable Supported
9
31
RsvdP

</td>
</tr>
</tbody>
</table>

> **Figure 7-338.** Alternate Protocol Capabilities Register
> <img src="figures/chapter_07/fig_1362_1_tight.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-296. Alternate Protocol Capabilities Register | 表 7-296. Alternate Protocol Capabilities 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Alternate Protocol Count - Indicates the number of Alternate Protocols or protocols that support Training Set Messages on one or more Lanes of this Link.<br>The value of this field must be greater than or equal to 0. | HwInit |
| 8 | Alternate Protocol Selective Enable Supported - If Set, the Alternate Protocol Selective Enable Mask Register is present. If Clear, the Alternate Protocol Selective Enable Mask Register is not present and Alternate Protocol Negotiation is controlled soley by the Alternate Protocol Negotiation Global Enable bit.<br>In Upstream Ports, this bit is hardwired to 0b.<br>In Downstream Ports, this bit is HwInit with an implementation specific default value. | RO/HwInit |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0
7
Alternate Protocol Index Select
8
Alternate Protocol Negotiation Global Enable
9
31
RsvdP

</td>
<td style="background-color:#e8e8e8">

0
7
Alternate Protocol Index Select
8
Alternate Protocol Negotiation Global Enable
9
31
RsvdP

</td>
</tr>
</tbody>
</table>

> **Figure 7-339.** Alternate Protocol Control Register
> <img src="figures/chapter_07/fig_1362_2_tight.png" width="700">


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-20-2"></a>
## 7.9.20.2 Alternate Protocol Capabilities Register (Offset 04h) | Alternate Protocol Capabilities 寄存器 (偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.20.2 Alternate Protocol Capabilities Register (Offset 04h) §

</td>
<td style="background-color:#e8e8e8">

7.9.20.2 Alternate Protocol Capabilities 寄存器 (偏移 04h) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

---

<a id="sec-7-9-20-3"></a>
## 7.9.20.3 Alternate Protocol Control Register (Offset 08h) | 替代协议控制寄存器（偏移量 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1363 -->
---

**Table 7-297. Alternate Protocol Control Register | 表 7-297. 替代协议控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Alternate Protocol Index Select - This field determines which Lane and which Alternate Protocol of that Lane is visible in Alternate Protocol Data 1 Register and Alternate Protocol Data 2 Register. The default value of this field is 00h. Unused bits in this field are permitted to be hardwired to 0b. If Alternate Protocol Count is 01h, this field is permitted to be hardwired to 00h. Behavior is undefined if this field is greater than Alternate Protocol Count. Specific Alternate Protocol Index Select values are permitted to be disabled without renumbering other protocol index values. Disabled entries return an Alternate Protocol Vendor ID of FFFFh. | RW |
| 8 | Alternate Protocol Negotiation Global Enable - When this bit is Set, Alternate Protocol Negotiation is enabled for this Link. When this bit is Clear, Alternate Protocol Negotiation is disabled for this Link. This bit is RW for Downstream Ports. It is HwInit for Upstream Ports. Default is 0b. | RW/HwInit (see description) |

<a id="sec-7-9-20-4"></a>
## 7.9.20.4 Alternate Protocol Data 1 Register (Offset 0Ch) | 替代协议数据 1 寄存器（偏移量 0Ch）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1364 -->
---

> **Figure 7-340. Alternate Protocol Data 1 Register | 替代协议数据 1 寄存器**
> <img src="figures/chapter_07/fig_1364_1.png" width="700">

**Table 7-298. Alternate Protocol Data 1 Register | 表 7-298. 替代协议数据 1 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2:0 | Alternate Protocol Usage Information - This field contains the Modified TS Usage associated alternate protocol associated with the Alternate Protocol Index Select value. If Alternate Protocol Vendor ID is FFFFh, the value of this field is undefined. | RO |
| 15:5 | Alternate Protocol Details - This field contains the Alternate Protocol Details associated alternate protocol associated with the Alternate Protocol Index Select value. If Alternate Protocol Vendor ID is FFFFh, the value of this field is undefined. | RO |
| 31:16 | Alternate Protocol Vendor ID - This field contains the Vendor ID associated alternate protocol associated with the Alternate Protocol Index Select value. Bits 7:0 of this field contain bits 7:0 of Vendor ID (Symbol 10). Bits 15:8 of this field contain bits 15:8 of Vendor ID (Symbol 11). If Alternate Protocol Index Select is greater than or equal to Alternate Protocol Count, this field contains FFFFh. If Alternate Protocol Index Select is associated with a disabled alternate protocol, this field contains FFFFh. | RO |

<a id="sec-7-9-20-5"></a>
## 7.9.20.5 Alternate Protocol Data 2 Register (Offset 10h) | 替代协议数据 2 寄存器（偏移量 10h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

</td>
<td style="background-color:#e8e8e8">

§

</td>
</tr>
</tbody>
</table>

> **Figure 7-341. Alternate Protocol Data 2 Register | 替代协议数据 2 寄存器**

**Table 7-299. Alternate Protocol Data 2 Register | 表 7-299. 替代协议数据 2 寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 23:0 | Modified TS Information 2 - This field contains the value for symbols 12 throught 14 for the alternate protocol associated with the Alternate Protocol Index Select value. If Alternate Protocol Vendor ID is FFFFh, the value of this field is undefined. Bits 7:0 contain the value of Symbol 12. Bits 16:8 contain the value of Symbol 13. Bits 23:16 contain the value of Symbol 14. | RO |

<a id="sec-7-9-20-6"></a>
## 7.9.20.6 Alternate Protocol Selective Enable Mask Register (Offset 14h) | 替代协议选择性使能掩码寄存器（偏移量 14h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1365 -->
---

This register is present if Alternate Protocol Selective Enable Supported is Set.

This register consists of a bit mask of size Alternate Protocol Count bits. Each bit corresponds to a valid value of Alternate Protocol Index Select. This register is an integral number of DWORDs in size.

When Alternate Protocol Negotiation Global Enable is Set, a particular bit in this register is Set, and the corresponding Alternate Protocol is not disabled (see Alternate Protocol Index Select), the next Alternate Protocol negotiation is permitted to consider using that Alternate Protocol. When a particular bit in this register is Clear, the next Alternate Protocol negotiation is not permitted to consider using the corresponding Alternate Protocol.

Changes to this field will affect the next Alternate Protocol negotiation and have no effect on current operation of the Link (regardless of current protocol).

> **Figure 7-342. Alternate Protocol Selective Enable Mask Register | 替代协议选择性使能掩码寄存器**
> <img src="figures/chapter_07/fig_1365_1_tight.png" width="700">

**Table 7-300. Alternate Protocol Selective Enable Mask Register | 表 7-300. 替代协议选择性使能掩码寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Alternate Protocol Selective Enable Mask - PCI Express - The PCI Express Protocol is always index 00h. The default value of this bit is 1b (i.e., PCI Express is always enabled by default). | RWS |
| 31:1 | Alternate Protocol Selective Enable Mask - Others - Other bits in this register represent protocols other than PCI Express. The default values of these "other" bits is implementation specific. The width of this field is shown here as 32 bits. The actual width depends on Alternate Protocol Count. Bits in this field corresponding to disabled Alternate Protocol Index values are permitted to be hardwired to 0b. Bits in this field corresponding to Alternate Protocol Index Select values above Alternate Protocol Count are permitted to be hardwired to 0b. | RWS |

<a id="sec-7-9-21"></a>
## 7.9.21 Conventional PCI Advanced Features Capability (AF) | Conventional PCI 高级功能能力结构 (AF)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

This capability is optional. It is permitted only in Conventional PCI Functions that are integrated into a Root Complex (根复合体). A Function may contain at most one instance of this capability.

§ Figure 7-343 shows the layout of this capability.

Note: Due to document production limitations, this figure shows an 8 byte capability while the actual capability is only 6 bytes long. Bytes 6 and 7 in the figure are not part of the capability.

</td>
<td style="background-color:#e8e8e8">

此能力结构是可选的。仅允许在集成于根复合体 (Root Complex) 中的 Conventional PCI 功能中使用。一个功能最多只能包含此能力结构的一个实例。

§ 图 7-343 展示了此能力结构的布局。

注：由于文档制作限制，此图显示为 8 字节的能力结构，而实际能力结构仅为 6 字节长。图中的第 6 和第 7 字节不属于该能力结构。

</td>
</tr>
</tbody>
</table>

> **Figure 7-343. Conventional PCI Advanced Features Capability (AF) | Conventional PCI 高级功能能力结构 (AF)**
> <img src="figures/chapter_07/fig_1365_2_tight.png" width="700">

<a id="sec-7-9-21-1"></a>
## 7.9.21.1 Advanced Features Capability Header (Offset 00h) | 高级功能能力结构头部（偏移量 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1366 -->
---

> **Figure 7-344. Advanced Features Capability Header | 高级功能能力结构头部**
> <img src="figures/chapter_07/fig_1366_1.png" width="700">

**Table 7-301. Advanced Features Capability Header | 表 7-301. 高级功能能力结构头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | CAP_ID - The value of 13h in this field identifies the Function as being AF capable. | RO |
| 15:8 | NXT_PTR - Pointer to the next item in the capabilities list. Must be 00h for the final item in the list. | RO |
| 23:16 | LENGTH - AF Structure Length (Bytes). Shall return a value of 06h. | RO |

<a id="sec-7-9-21-2"></a>
## 7.9.21.2 AF Capabilities Register (Offset 03h) | AF 能力寄存器（偏移量 03h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

</td>
<td style="background-color:#e8e8e8">

§

</td>
</tr>
</tbody>
</table>

> **Figure 7-345. AF Capabilities Register | AF 能力寄存器**

**Table 7-302. AF Capabilities Register | 表 7-302. AF 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | TP_CAP - Set to indicate support for the Transactions Pending (TP) bit. TP_CAP must be Set if FLR_CAP is Set. | HwInit |
| 1 | FLR_CAP - Set to indicate support for Function Level Reset (INITIATE_FLR). | HwInit |
| 7:2 | Reserved - Shall be implemented as read only returning a value of 000 0000b. | RO |

<a id="sec-7-9-21-3"></a>
## 7.9.21.3 Conventional PCI Advanced Features Control Register (Offset 04h) | Conventional PCI 高级功能控制寄存器（偏移量 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1367 -->
---

> **Figure 7-346. Conventional PCI Advanced Features Control Register | Conventional PCI 高级功能控制寄存器**
> <img src="figures/chapter_07/fig_1367_1_tight.png" width="700">

**Table 7-303. Conventional PCI Advanced Features Control Register | 表 7-303. Conventional PCI 高级功能控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Function Level Reset (INITIATE_FLR) - A write of 1b initiates a Function Level Reset (FLR). Registers and state information that do not apply to Conventional PCI are exempt from the FLR requirements in this specification (see § Section 6.6.2). The value read by software from this bit shall always be 0b. | RW |
| 7:1 | Reserved - Shall be implemented as read only returning a value of 000 0000b. | RO |

<a id="sec-7-9-21-4"></a>
## 7.9.21.4 AF Status Register (Offset 05h) | AF 状态寄存器（偏移量 05h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

</td>
<td style="background-color:#e8e8e8">

§

</td>
</tr>
</tbody>
</table>

> **Figure 7-347. AF Status Register | AF 状态寄存器**

**Table 7-304. AF Status Register | 表 7-304. AF 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Transactions Pending (TP) - A value of 1b indicates that the Function has issued one or more non-posted transactions which have not been completed, including non-posted transactions that a target has terminated with Retry. A value 0b indicates that all non-posted transactions have been completed. | RO |
| 7:1 | Reserved - Shall be implemented as read only returning a value of 000 0000b. | RO |

<a id="sec-7-9-22"></a>
## 7.9.22 SFI Extended Capability | SFI 扩展能力结构

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1368 -->
---

The SFI (System Firmware Intermediary) Extended Capability is an optional capability that provides system firmware with enhanced control over primarily hot-plug mechanisms, and enables system firmware to operate as an intermediary between certain events and the operating system (see § Section 6.7.4). This capability may be implemented by a Root Port or a Switch Downstream Port. It is not applicable to any other Device/Port type.

If a Downstream Port implements the SFI Extended Capability, that Port must support ERR_COR Subclass capability, and indicate so by Setting the ERR_COR Subclass Capable bit in the Device Capabilities Register. See see § Section 7.5.3.3.

> **Figure 7-348. SFI Extended Capability | SFI 扩展能力结构**
> <img src="figures/chapter_07/fig_1368_1_tight.png" width="700">

<a id="sec-7-9-22-1"></a>
## 7.9.22.1 SFI Extended Capability Header (Offset 00h) | SFI 扩展能力结构头部（偏移量 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

</td>
</tr>
</tbody>
</table>

§ Figure 7-349 and § Table 7-305 detail allocation of fields in the Extended Capability header.

<!-- 📄 Page 1369 -->
---

> **Figure 7-349. SFI Extended Capability Header | SFI 扩展能力结构头部**
> <img src="figures/chapter_07/fig_1369_1_tight.png" width="700">

**Table 7-305. SFI Extended Capability Header | 表 7-305. SFI 扩展能力结构头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the SFI Extended Capability is 002Ch. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

<a id="sec-7-9-22-2"></a>
## 7.9.22.2 SFI Capability Register (Offset 04h) | SFI 能力寄存器（偏移量 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

</td>
<td style="background-color:#e8e8e8">

§

</td>
</tr>
</tbody>
</table>

> **Figure 7-350. SFI Capability Register | SFI 能力寄存器**

**Table 7-306. SFI Capability Register | 表 7-306. SFI 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | SFI OOB PD Supported - When Set, this bit indicates that this slot supports reporting the out-of-band presence detect state. If this Downstream Port has no implemented slot (as indicated by the Slot Implemented bit in the PCI Express Capabilities Register), then the value of this bit must be 0b. | HwInit |
| 15:1 | RsvdP | |

<a id="sec-7-9-22-3"></a>
## 7.9.22.3 SFI Control Register (Offset 06h) | SFI 控制寄存器（偏移量 06h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§

§

§

§

</td>
<td style="background-color:#e8e8e8">

§

§

§

§

</td>
</tr>
</tbody>
</table>

<!-- 📄 Page 1370 -->
---

> **Figure 7-351. SFI Control Register | SFI 控制寄存器**
> <img src="figures/chapter_07/fig_1370_1.png" width="700">

**Table 7-307. SFI Control Register | 表 7-307. SFI 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | SFI PD State Mask - When Set, this bit masks the Presence Detect State bit in the Slot Status Register, making its value 0b, regardless of the actual presence detect state. Otherwise, its value indicates the actual state. If the value of the Presence Detect State bit changes when the SFI PD State Mask bit value changes, this must cause a Presence Detect Changed event (see § Section 6.7.3). Default value of this bit is 0b. | RW |
| 1 | SFI DLL State Mask - When Set, this bit masks the Data Link Layer Link Active bit in the Link Status Register, making its value 0b, regardless of the actual Data Link Layer state. Otherwise, its value indicates the actual state. If the value of the Data Link Layer Link Active State bit changes when the SFI DLL State Mask bit value changes, this must cause a Data Link Layer State Changed event (see § Section 6.7.3). Default value of this bit is 0b. | RW |
| 2 | SFI OOB PD Changed Enable - When Set, this bit enables sending an ERR_COR Message for the SFI OOB PD Changed event. See § Section 6.7.4.1 for other necessary conditions. This bit must be RW if the SFI OOB PD Supported bit is Set; otherwise, it is permitted to be hardwired to 0b. If the SFI OOB PD Supported bit is Clear and software Sets this bit, the behavior is undefined. Default value of this bit is 0b. | RW/RO |
| 3 | SFI DLL State Changed Enable - When Set, this bit enables sending an ERR_COR Message for the SFI DLL State Changed event. See § Section 6.7.4.1 for other necessary conditions. Default value of this bit is 0b. | RW |
| 5:4 | SFI DPF Control - This field controls the level of Downstream Port Filtering (DPF) enabled on the Downstream Port, governing which Request TLPs targeting Downstream Components get filtered; that is, handled as if the Link is in DL_Down. See § Section 6.7.4.2. Defined encodings are: 00b Disabled, 01b Filter all Request TLPs, 10b Filter only Configuration Request TLPs, 11b Reserved. Default value of this field is 00b. | RW |
| 6 | SFI HPS Suppress - When Set, this bit forces the Hot-Plug Surprise (HPS) bit in the Slot Capabilities Register to be Clear and disables associated Hot-Plug Surprise functionality. See § Section 6.7.4.4. Default value of this bit is 0b. | RW |
| 7 | SFI DRS Mask - When Set, this bit masks the DRS Message Received bit in the Link Status 2 Register, making its value 0b, regardless of the actual DRS Message Received state. Otherwise, its value indicates the actual state. If the value of the DRS Message Received bit changes from Clear to Set when the SFI DRS Mask bit is Cleared, this must trigger any notification enabled by the DRS Signaling Control field in the Link Control Register (see § Section 7.5.3.7). Default value of this bit is 0b. | RW |
| 8 | SFI DRS Signaling Enable - When Set, this bit enables sending an ERR_COR Message for the SFI DRS Received event. See § Section 6.7.4.1 for other necessary conditions. Default value of this bit is 0b. | RW |
| 9 | SFI DRS Trigger - If the SFI DRS Mask bit is Clear, when software writes a 1b to this bit, the Downstream Port must behave as if a DRS Message was received. Otherwise, software writing a 1b to this bit has no effect. | RW |
| 15:10 | RsvdP | |

<!-- 📄 Page 1371 -->
---

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| (continued) | It is permitted to write 1b to this bit while simultaneously writing updated values to other fields in this register, notably the SFI DRS Mask bit. For this case, the SFI DRS Trigger semantics are based on the updated value of the SFI DRS Mask bit. This bit always returns 0b when read. | |

> **Figure 7-352. SFI Status Register | SFI 状态寄存器**
> <img src="figures/chapter_07/fig_1371_1_tight.png" width="700">

**Table 7-308. SFI Status Register | 表 7-308. SFI 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | SFI PD State - This bit always indicates the actual presence detect state associated with the Presence Detect State bit in the Slot Status Register, even when the value of that bit is being masked by the SFI PD State Mask bit. | RO |
| 1 | SFI OOB PD State - This bit indicates the out-of-band presence detect state, independent of the in-band presence detect state. This bit must be implemented if the SFI OOB PD Supported bit is Set; otherwise, it is permitted to be hardwired to 0b. | RO |
| 2 | SFI OOB PD Changed - This bit is Set when the value reported in the SFI OOB PD State bit is changed. | RW1C |
| 3 | SFI DLL State - This bit always indicates the actual link state associated with the Data Link Layer Link Active bit in the Link Status Register, even when the value of that bit is being masked by the SFI DLL State Mask bit. | RO |
| 4 | SFI DLL State Changed - This bit is Set when the value reported in the SFI DLL State bit is changed. | RW1C |
| 5 | SFI DRS Received - This bit always indicates the actual state associated with the DRS Message Received bit in the Link Status 2 Register, even when the value of that bit is being masked by the SFI PD State Mask bit. Clearing the SFI DRS Received bit (by writing a 1b to it) must also cause the actual state associated with the DRS Message Received bit to be Cleared. | RW1C |
| 15:6 | RsvdZ | |

---

<a id="sec-7-9-22-4"></a>
## 7.9.22.4 SFI Status Register (Offset 08h) | SFI 状态寄存器 (偏移 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.22.4 SFI Status Register (Offset 08h) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.22.4 SFI 状态寄存器 (偏移 08h) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1372 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-353. SFI CAM Address Register**
> <img src="figures/chapter_07/fig_1372_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-309 SFI CAM Address Register | 表 7-309 SFI CAM 地址寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 27:0 | SFI CAM Address - This field specifies the target Bus, Device, and Function Numbers, along with the Extended Register Number and Register Number, in the format specified by § Table 7-1. | RW |
| 31:28 | RsvdP | RsvdP |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-354. SFI CAM Data Register**

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-310 SFI CAM Data Register | 表 7-310 SFI CAM 数据寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 31:0 | SFI CAM Data - When this field is read, the SFI CAM generates and transmits a Configuration Read Request on the Link below this Port. When this field is written, the SFI CAM generates and transmits a Configuration Write Request on the Link below this Port. In both cases, the target of the Configuration Request is determined by the value of the SFI CAM Address Register. See § Section 6.7.4.3 . | RW |


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Subsystem ID and Subsystem Vendor ID Capability is an optional capability used to uniquely identify the add-in card or subsystem where the PCI device resides. It provides a mechanism for add-in card vendors to distinguish their add-in cards from one another even though the add-in cards may have the same PCI bridge on them (and, therefore, the same Vendor ID and Device ID). The format of the capability is shown in § Figure 7-355. The fields are described in § Table 7-311 and § Table 7-312.

This capability is only permitted in Functions with Type 1 Configuration Space Headers.

</td>
<td style="background-color:#e8e8e8">

Subsystem ID 和 Subsystem Vendor ID Capability(子系统 ID 与子系统厂商 ID 能力)是一种可选能力,用于唯一标识 PCI 设备所在的扩展卡或子系统。它为扩展卡厂商提供了一种机制,使其能够区分各自的扩展卡,即使这些扩展卡可能搭载相同的 PCI 桥(因此具有相同的 Vendor ID 和 Device ID)。该能力的格式如 § Figure 7-355 所示,字段说明见 § Table 7-311 和 § Table 7-312。

该能力仅允许在具有 Type 1 配置空间头部的 Function(功能)中使用。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-22-5"></a>
## 7.9.22.5 SFI CAM Address Register (Offset 0Ch) | SFI CAM 地址寄存器 (偏移 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.22.5 SFI CAM Address Register (Offset 0Ch) §

</td>
<td style="background-color:#e8e8e8">

7.9.22.5 SFI CAM 地址寄存器 (偏移 0Ch) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-22-6"></a>
## 7.9.22.6 SFI CAM Data Register (Offset 10h) | SFI CAM 数据寄存器 (偏移 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.22.6 SFI CAM Data Register (Offset 10h) §

</td>
<td style="background-color:#e8e8e8">

7.9.22.6 SFI CAM 数据寄存器 (偏移 10h) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-23"></a>
## 7.9.23 Subsystem ID and Subsystem Vendor ID Capability | Subsystem ID 与 Subsystem Vendor ID 能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.23 Subsystem ID and Subsystem Vendor ID Capability §
§
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.23 Subsystem ID 与 Subsystem Vendor ID 能力 §
§
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1373 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-355. Subsystem ID and Subsystem Vendor ID Capability**
> <img src="figures/chapter_07/fig_1373_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-356. Subsystem ID and Subsystem Vendor ID Capability Header**
> <img src="figures/chapter_07/fig_1373_2_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-311 Subsystem ID and Subsystem Vendor ID Capability Header | 表 7-311 Subsystem ID 与 Subsystem Vendor ID 能力头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Capability ID - Indicates the PCI Express Capability structure. This field must return a Capability ID of 0Dh indicating that this is a Subsystem ID and Subsystem Vendor ID Capability structure. | RO |
| 15:8 | Next Capability Pointer - This field contains the offset to the next PCI Capability structure or 00h if no other items exist in the linked list of Capabilities. | RO |
| 31:16 | RsvdP | RsvdP |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-357. Subsystem ID and Subsystem Vendor ID Capability Data**
> <img src="figures/chapter_07/fig_1373_3_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-312 Subsystem ID and Subsystem Vendor ID Capability Data | 表 7-312 Subsystem ID 与 Subsystem Vendor ID 能力数据**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | SSVID - The SSVID identifies the manufacturer of the add-in card or subsystem. The SSVID is assigned by PCI-SIG to insure uniqueness (the Vendor ID is used as the SSVID also). This field is read-only. | HwInit |
| 31:16 | SSID - The SSID identifies the particular add-in card or subsystem and is assigned by the vendor. This field is read-only. | HwInit |

<a id="sec-7-9-23-1"></a>
## 7.9.23.1 Subsystem ID and Subsystem Vendor ID Capability Header (Offset 00h) | Subsystem ID 与 Subsystem Vendor ID 能力头部 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.23.1 Subsystem ID and Subsystem Vendor ID Capability Header (Offset 00h) §

</td>
<td style="background-color:#e8e8e8">

7.9.23.1 Subsystem ID 与 Subsystem Vendor ID 能力头部 (偏移 00h) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-23-2"></a>
## 7.9.23.2 Subsystem ID and Subsystem Vendor ID Capability Data (Offset 04h) | Subsystem ID 与 Subsystem Vendor ID 能力数据 (偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.23.2 Subsystem ID and Subsystem Vendor ID Capability Data (Offset 04h) §
§
§
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.23.2 Subsystem ID 与 Subsystem Vendor ID 能力数据 (偏移 04h) §
§
§
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1374 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Data Object Exchange (DOE) Extended Capability is an optional Extended Capability for discovering and controlling a mechanism for the exchange of data objects (see § Section 6.30 ). It is permitted for a Function to implement more than one instance of this Extended Capability.

§ Figure 7-358 illustrates the Data Object Exchange Extended Capability structure.

</td>
<td style="background-color:#e8e8e8">

Data Object Exchange (DOE, 数据对象交换)扩展能力是一种可选的扩展能力,用于发现和控制数据对象交换机制(参见 § Section 6.30)。允许某个 Function 实现该扩展能力的多份实例。

§ Figure 7-358 描述了 Data Object Exchange 扩展能力的结构。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-358. Data Object Exchange Extended Capability**
> <img src="figures/chapter_07/fig_1374_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-359. DOE Extended Capability Header**
> <img src="figures/chapter_07/fig_1374_2_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-313 DOE Extended Capability Header | 表 7-313 DOE 扩展能力头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID – This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. The Extended Capability ID for the Data Object Exchange Extended Capability is 002Eh. | RO |
| 19:16 | Capability Version – This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 2h for this version of the specification. New implementations compliant to the older version of this specification must indicate Capability Version 1h. | RO |
| 31:20 | Next Capability Offset – This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. | RO |

<a id="sec-7-9-24"></a>
## 7.9.24 Data Object Exchange Extended Capability | Data Object Exchange 扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24 Data Object Exchange Extended Capability §

</td>
<td style="background-color:#e8e8e8">

7.9.24 Data Object Exchange 扩展能力 §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-24-1"></a>
## 7.9.24.1 DOE Extended Capability Header (Offset 00h) | DOE 扩展能力头部 (偏移 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.1 DOE Extended Capability Header (Offset 00h) §
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.24.1 DOE 扩展能力头部 (偏移 00h) §
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1375 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-360. DOE Capabilities Register**
> <img src="figures/chapter_07/fig_1375_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-314 DOE Capabilities Register | 表 7-314 DOE 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | DOE Interrupt Support – When Set, this bit indicates DOE support of software notification of DOE events using MSI/MSI-X. | HwInit |
| 11:1 | DOE Interrupt Message Number - When the DOE Interrupt Support bit is Set, this field indicates which MSI/MSI-X vector is used for the interrupt message generated in association with DOE. For MSI, the value in this field indicates the offset between the base Message Data and the interrupt message that is generated. Hardware is required to update this field so that it is correct if the number of MSI Messages assigned to the Function changes when software writes to the Multiple Message Enable field in the Message Control Register for MSI. For MSI-X, the value in this field indicates which MSI-X Table entry is used to generate the interrupt message. For a given MSI-X implementation, the entry must remain constant. If both MSI and MSI-X are implemented, they are permitted to use different vectors, though software is permitted to enable only one mechanism at a time. If MSI-X is enabled, the value in this field must indicate the vector for MSI-X. If MSI is enabled or neither is enabled, the value in this field must indicate the vector for MSI. If software enables both MSI and MSI-X at the same time, the value in this field is undefined. When the DOE Interrupt Support bit is Clear the value in this field is undefined. | RO |
| 12 | DOE Attention Mechanism Support – This bit, when Set, indicates the DOE instance supports the optional DOE Attention mechanism. | HwInit |
| 13 | DOE Async Message Support – This bit, when Set, indicates the DOE instance supports the optional DOE Async Message mechanism. | HwInit |
| 31:14 | RsvdP | RsvdP |

<a id="sec-7-9-24-2"></a>
## 7.9.24.2 DOE Capabilities Register (Offset 04h) | DOE 能力寄存器 (偏移 04h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.2 DOE Capabilities Register (Offset 04h) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.24.2 DOE 能力寄存器 (偏移 04h) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1376 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-361. DOE Control Register**
> <img src="figures/chapter_07/fig_1376_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-315 DOE Control Register | 表 7-315 DOE 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | DOE Abort – A write of 1b to this bit must cause all data object transfer operations associated with this DOE instance to be aborted. Reads from this bit must always return 0b. | RW (see description) |
| 1 | DOE Interrupt Enable – When this bit is Set, the DOE Interrupt Support bit is Set, and MSI/MSI-X is enabled, the DOE instance must issue an MSI/MSI-X interrupt as defined in § Section 6.30.3 . When DOE Interrupt Support is Clear, this bit is permitted to be Reserved. Default value of this bit is 0b. | RW/RsvdP |
| 2 | DOE Attention Not Needed – When DOE Attention Mechanism Support is Set, this bit when Set enables the DOE instance to enter and stay in a state where it is not immediately available for use. When this bit is Clear the DOE instance must remain in a responsive state. When DOE Attention Mechanism Support is Clear, this bit is permitted to be Reserved. Default value of this bit is 0b. | RW/RsvdP |
| 3 | DOE Async Message Enable – If DOE Async Message Support is Set, this bit, when Set, enables the use of the DOE Async Message mechanism. When DOE Async Message Support is Clear, this bit is permitted to be Reserved. Default value of this bit is 0b. | RW/RsvdP |
| 30:4 | RsvdP | RsvdP |
| 31 | DOE Go – A write of 1b to this bit indicates to the DOE instance that it can start consuming the data object transferred through the DOE Write Data Mailbox Register. Behavior is undefined if the DOE Go bit is Set before the entire data object has been written to the DOE Write Data Mailbox Register. Behavior is undefined if the DOE Go bit is written with 1b when the DOE Busy bit is Set. Reads from this bit must always return 0b. | RW (see description) |

<a id="sec-7-9-24-3"></a>
## 7.9.24.3 DOE Control Register (Offset 08h) | DOE 控制寄存器 (偏移 08h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.3 DOE Control Register (Offset 08h) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.24.3 DOE 控制寄存器 (偏移 08h) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1377 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-362. DOE Status Register**
> <img src="figures/chapter_07/fig_1377_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-316 DOE Status Register | 表 7-316 DOE 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | DOE Busy — When Set, this bit indicates the DOE instance is temporarily unable to receive a new data object through the DOE Write Data Mailbox Register. The DOE instance must Set this bit when processing a received data object, and Clear this bit when it is able to receive a new data object. The DOE instance must Set this bit following an abort or reset if, as a result of the abort/reset, it is temporarily unable to receive a data object, and then must Clear this bit when it is able to receive a new data object. | RO |
| 1 | DOE Interrupt Status – If DOE Interrupt Support is Set, then this bit must be Set when an interrupt-triggering event occurs. If DOE Interrupt Support is Clear, this bit is Reserved. Default value of this bit is 0b. | RW1C/RsvdZ |
| 2 | DOE Error – This bit, when Set, indicates that there has been an internal error associated with a data object received, or that a data object has been received for which the DOE instance is unable to provide a response. The DOE instance must Clear this bit, if it is not already Clear, when 1b is written to the DOE Abort bit in the DOE Control Register. Writing 1b to the DOE Abort bit is the only mechanism for software to Clear this bit. The transition of this bit from Clear to Set is an interrupt triggering event. Default value of this bit is 0b. | RO |
| 3 | DOE Async Message Status – If DOE Async Message Support is Set, this bit, when Set, indicates the DOE instance has one or more asynchronous messages to transfer. The transition of this bit from Clear to Set is an interrupt triggering event. If DOE Async Message Support is Clear, this bit is Reserved. Default value of this bit is 0b. | RO/RsvdZ |
| 4 | DOE At Attention – When DOE Attention Mechanism Support is Set, this bit, when Set, indicates the DOE interface is presently in a state of readiness. The transition of this bit from Clear to Set is an interrupt triggering event. | RO |
| 30:5 | RsvdZ | RsvdZ |
| 31 | Data Object Ready – When Set, this bit indicates the DOE instance has a data object available to be read by system firmware/software. | RO |

<a id="sec-7-9-24-4"></a>
## 7.9.24.4 DOE Status Register (Offset 0Ch) | DOE 状态寄存器 (偏移 0Ch)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.4 DOE Status Register (Offset 0Ch) §
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.24.4 DOE 状态寄存器 (偏移 0Ch) §
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1378 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4 | DOE At Attention (continued) – When DOE Attention Mechanism Support is Clear, this bit is Reserved. | RO |
| 31 | Data Object Ready (continued) – If there is no additional data object ready for transfer, the DOE instance must clear this bit after the entire data object has been transferred, as indicated by software writing to the DOE Read Data Mailbox Register after reading the final DW of the data object. The DOE instance must clear this bit, if not already clear, upon a write of 1b to the DOE Abort bit in the DOE Control Register. The transition of this bit from Clear to Set is an interrupt triggering event. Default value of this bit is 0b. | RO |

</td>
<td style="background-color:#e8e8e8">

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 4 | DOE At Attention(续) – 当 DOE Attention Mechanism Support 位为 Clear 时,该位为 Reserved。 | RO |
| 31 | Data Object Ready(续) – 如果没有其他数据对象准备传输,则在软件读取完数据对象最后一个 DW 后写入 DOE Read Data Mailbox Register 时,DOE 实例必须清除该位。当对 DOE Control Register 中的 DOE Abort 位写入 1b 时,如果该位尚未清除,DOE 实例也必须清除它。该位由 Clear 到 Set 的跳变是中断触发事件。该位的默认值为 0b。 | RO |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-363. DOE Write Data Mailbox Register**
> <img src="figures/chapter_07/fig_1378_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-317 DOE Write Data Mailbox Register | 表 7-317 DOE 写数据邮箱寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 31:0 | DOE Write Data Mailbox – The DOE instance receives data objects via writes to this register. A successfully completed write to this register adds one DW to the incoming data object. Setting the DOE Go bit in the DOE Control Register indicates to the DOE Instance that the final DW of the data object has been written to this register. Reads of this register must return all 0's. | RW (see description) |

<a id="sec-7-9-24-5"></a>
## 7.9.24.5 DOE Write Data Mailbox Register (Offset 10h) | DOE 写数据邮箱寄存器 (偏移 10h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.5 DOE Write Data Mailbox Register (Offset 10h) §

</td>
<td style="background-color:#e8e8e8">

7.9.24.5 DOE 写数据邮箱寄存器 (偏移 10h) §

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-24-6"></a>
## 7.9.24.6 DOE Read Data Mailbox Register (Offset 14h) | DOE 读数据邮箱寄存器 (偏移 14h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.24.6 DOE Read Data Mailbox Register (Offset 14h) §
§
§
§

</td>
<td style="background-color:#e8e8e8">

7.9.24.6 DOE 读数据邮箱寄存器 (偏移 14h) §
§
§
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1379 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-364. DOE Read Data Mailbox Register**
> <img src="figures/chapter_07/fig_1379_1.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-318 DOE Read Data Mailbox Register | 表 7-318 DOE 读数据邮箱寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 31:0 | DOE Read Data Mailbox – If the Data Object Ready bit is Set, a read of this register returns the current DW of the data object. A write of any value to this register indicates a successful transfer of the current data object DW, and the DOE instance must return the next DW in the data object upon the next read of this register as long as the Data Object Ready bit remains Set. It is permitted for multiple data objects to be read from this register back-to-back. When this scenario occurs, the Data Object Ready bit will remain Set until this register is written after the final DW is read. A write of any value to this register when the Data Object Ready bit is Clear must have no effect. The value read from this register when the Data Object Ready bit is Clear must be 0000 0000h. | RW (see description) |


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Unimplemented Functions possess Transaction ID resources by virtue of their Bus/Device/Function Number space, and therefore associated Requester ID space, and associated Tags, even though there is no Function implemented there to use them. The Shadow Functions Extended Capability is an optional capability that permits a Requester to use the Transaction ID resources of another otherwise unimplemented Function to generate more outstanding Requests than it would otherwise be able to using only the Transaction ID resources of the Function it is associated with. The Requester generates some of its Requests via the Function it is associated with and generates other Requests via the Shadow Function. If the Requester exceeds the Transaction ID resources of a single Function, it is permitted to implement this capability and split its Transaction ID space across that Function and additional Shadow Functions defined by this capability.

A Requester implementing a Shadow Function uses the characteristics and attributes of the Function containing this capability. Requests made via the associated Function will use the associated Function's BDF to populate the Requester ID. Requests made via the Shadow Function will use the BDF calculated from the value in the Shadow Function Number field of the corresponding Shadow Function Instance register entry to populate the Requester ID. Other characteristics and attributes of the Shadow Function are taken from the associated Function's Configuration Space.

The Shadow Function Number field in the Shadow Function Instance register entry for each Shadow Function is used to calculate the value of the Bus/Device/Function number (Bus/Function number for ARI devices) (BDF) for that Shadow Function. That BDF space assigned to the Shadow Function must be available, that is it corresponds to an otherwise unimplemented Function.

</td>
<td style="background-color:#e8e8e8">

未实现的 Function 凭借其 Bus/Device/Function Number(总线/设备/功能号)空间,以及由此关联的 Requester ID(请求者 ID)空间和 Tag(标签),拥有 Transaction ID(事务 ID)资源,即使这些 Function 实际上并未实现,不会使用这些资源。Shadow Functions Extended Capability(影子功能扩展能力)是一种可选能力,它允许 Requester(请求者)使用另一个未实现 Function 的 Transaction ID 资源,从而生成比仅使用其关联 Function 自身 Transaction ID 资源更多的未完成请求。Requester 通过其关联 Function 发起部分请求,通过 Shadow Function(影子功能)发起其他请求。如果 Requester 超出单个 Function 的 Transaction ID 资源,可实现此能力并将其 Transaction ID 空间拆分到该 Function 和由本能力定义的附加 Shadow Function 之间。

实现 Shadow Function 的 Requester 使用包含此能力的 Function 的特性和属性。通过关联 Function 发出的请求将使用关联 Function 的 BDF 来填充 Requester ID。通过 Shadow Function 发出的请求将使用从对应 Shadow Function Instance 寄存器的 Shadow Function Number 字段计算所得的 BDF 来填充 Requester ID。Shadow Function 的其他特性和属性取自关联 Function 的配置空间。

每个 Shadow Function 的 Shadow Function Instance 寄存器条目中的 Shadow Function Number 字段用于计算该 Shadow Function 的 Bus/Device/Function 号(ARI 设备为 Bus/Function 号)(BDF)。分配给该 Shadow Function 的 BDF 空间必须可用,即对应于一个未实现的 Function。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Additional requirements for implementing Shadow Functions are:

- Any access to the Configuration Space region of the BDF associated with the Shadow Function, without errors that would have different behavior, must be responded to with a Completion with UR status.
- For non-ARI Devices, the Shadow Function must reside in the same Device as the Function it is shadowing. ARI must be supported if the Shadow Function Number is greater than 7.
- A Function is permitted to have more than one Shadow Function.
- A Function is permitted to have at most one instance of this capability.
- This capability is permitted to be implemented in any Function capable of operating as a Requester.
- For VFs, the Shadow Functions must be assigned in a manner that accommodates the VF Discovery algorithm (see § Section 9.2.1.2 ).
- Requesters are permitted to generate Posted Requests that are not Message Signaled Interrupt (MSI/MSI-X) Requests using the Transaction ID space of a Shadow Function.

</td>
<td style="background-color:#e8e8e8">

实现 Shadow Function 的其他要求如下:

- 对 Shadow Function 关联的 BDF 配置空间区域进行的任何访问,在没有会导致不同行为的错误时,必须以 UR(Unsupported Request,不支持的请求)状态的 Completion(完成报文)响应。
- 对于非 ARI 设备,Shadow Function 必须驻留于其影子所对应的 Function 所在的同一 Device 中。如果 Shadow Function Number 大于 7,则必须支持 ARI。
- 允许一个 Function 具有多个 Shadow Function。
- 允许一个 Function 最多具有本能力的一个实例。
- 允许在任何能够作为 Requester 工作的 Function 中实现本能力。
- 对于 VF,Shadow Function 的分配方式必须与 VF 发现算法相适应(参见 § Section 9.2.1.2)。
- 允许 Requester 使用 Shadow Function 的 Transaction ID 空间生成不是消息信号中断(MSI/MSI-X)请求的 Posted Requests(有数据,无完成请求)。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-25-2"></a>
## 7.9.25 Shadow Functions Extended Capability | Shadow Functions 扩展能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

7.9.25 Shadow Functions Extended Capability §
§

</td>
<td style="background-color:#e8e8e8">

7.9.25 Shadow Functions 扩展能力 §
§

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1380 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

- Requesters are not permitted to generate Message Signaled Interrupt (MSI/MSI-X) Requests using the Transaction ID space of a Shadow Function.
- Functions utilizing Shadow Functions must be aware that accesses utilizing the Shadow Function's Transaction ID resources appear to the rest of the system with the same semantics as if the access was from any independent Function and deal with those implications.
- The software for the Translation Agent is responsible for maintaining the integrity of address translation resources. Behavior is undefined if address translation resources are not updated before the Shadow Function's Requester makes a Request.
- Translation Requests issued by a Shadow Function are cached in the ATC associated with the main Function. When enabled, Functions are permitted to use translations across the "main" and Shadow Functions regardless of which Function issued the associated Translation Request. See § Section 10.2 .
- The software for handling Page Request Messages is responsible for coordinating usage across Shadow Functions. See § Section 10.4.1 and § Section 10.5.2.5 .
- Behavior is undefined if software enabling FPB configures a Shadow Function to use the same Requester ID as another Function.
- For a Multi-Function Device that supports ACS P2P Egress Control, any enabled Shadow Functions must be taken into account when configuring the Egress Control Vector to allow P2P traffic between the Requester and its Shadow Functions, and other Functions in the Device.

</td>
<td style="background-color:#e8e8e8">

- 不允许 Requester 使用 Shadow Function 的 Transaction ID 空间生成消息信号中断(MSI/MSI-X)请求。
- 使用 Shadow Function 的 Function 必须意识到,使用 Shadow Function 的 Transaction ID 资源进行的访问对系统其余部分呈现的语义与来自任何独立 Function 的访问相同,必须处理这些影响。
- Translation Agent(转换代理)的软件负责维护地址转换资源的完整性。如果 Shadow Function 的 Requester 发起请求之前地址转换资源未更新,则行为是未定义的。
- 由 Shadow Function 发出的 Translation Request(转换请求)缓存在与主 Function 关联的 ATC(Address Translation Cache,地址转换缓存)中。启用后,允许 Function 在"主"Function 与 Shadow Function 之间共用转换结果,无论该 Translation Request 由哪个 Function 发出。参见 § Section 10.2。
- 处理 Page Request Message(页请求消息)的软件负责协调跨 Shadow Function 的使用。参见 § Section 10.4.1 和 § Section 10.5.2.5。
- 如果启用 FPB 的软件将 Shadow Function 配置为使用与其他 Function 相同的 Requester ID,则行为是未定义的。
- 对于支持 ACS P2P Egress Control(ACS 对等出口控制)的多功能设备,在配置 Egress Control Vector(出口控制向量)以允许 Requester 与其 Shadow Function 以及设备中其他 Function 之间的 P2P 流量时,必须考虑所有已使能的 Shadow Function。

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Multiple Shadow Functions for a Function are permitted to be assigned by this Capability. The Number of Shadow Functions field in the Shadow Functions Capability register defines the number of Shadow Functions assigned and the number of Shadow Function Instance register entries in the Capability and therefore the length of the Capability structure.

§ Figure 7-365 shows the Shadow Functions Extended Capability structure.

</td>
<td style="background-color:#e8e8e8">

本能力允许为一个 Function 分配多个 Shadow Function。Shadow Functions Capability 寄存器中的 Number of Shadow Functions 字段定义所分配的 Shadow Function 数量,以及本能力中 Shadow Function Instance 寄存器条目的数量,从而决定能力结构的长度。

§ Figure 7-365 展示了 Shadow Functions 扩展能力的结构。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **IMPLEMENTATION NOTE:**
> **SHADOW FUNCTION NUMBER PROGRAMMING**
>
> The value programmed into the Shadow Function Number field should place the Shadow Function on the same Bus Number as the Function declaring it. Otherwise, ACS Source Validation might not operate appropriately, Completions targeting the Shadow Function might not be routed correctly, or other misbehaviors might occur.

</td>
<td style="background-color:#e8e8e8">

> **实现说明:**
> **SHADOW FUNCTION NUMBER 编程**
>
> 编程到 Shadow Function Number 字段中的值应将 Shadow Function 置于与声明它的 Function 相同的 Bus Number 上。否则,ACS Source Validation 可能无法正常工作,发往 Shadow Function 的 Completion 可能无法被正确路由,或可能出现其他异常行为。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<!-- 📄 Page 1381 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

N = the value of the Number of Shadow Functions field.

</td>
<td style="background-color:#e8e8e8">

N = Number of Shadow Functions 字段的值。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-365. Shadow Functions Extended Capability Structure**
> <img src="figures/chapter_07/fig_1381_1_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

§ Figure 7-366 details allocation of the register fields in the Shadow Functions Extended Capability Header; § Table 7-319 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

§ Figure 7-366 详细说明了 Shadow Functions 扩展能力头部寄存器字段的分配;§ Table 7-319 给出相应的位定义。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-366. Shadow Functions Extended Capability Header**
> <img src="figures/chapter_07/fig_1381_2_tight.png" width="700">

</td>
<td style="background-color:#e8e8e8">


</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Table 7-319 Shadow Functions Extended Capability Header | 表 7-319 Shadow Functions 扩展能力头部**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | Shadow Functions Extended Capability ID - Indicates the Shadow Functions Extended Capability structure. This field must return a Capability ID of 002Dh indicating that this is a Shadow Functions Extended Capability structure. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | Next Capability Offset - The offset to the next PCI Extended Capability structure or 000h if no other items exist in the linked list of capabilities. | RO |

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


---

<a id="sec-7-9-25-1"></a>
## 7.9.25.1 Shadow Functions Extended Capability Header (Offset 00h) | Shadow Functions 扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Shadow Functions Extended Capability Header (Offset 00h)

</td>
<td style="background-color:#e8e8e8">

Shadow Functions 扩展能力头（偏移 00h）

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-25"></a>
## 7.9.25 Shadow Functions Capability | Shadow Functions 能力

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

[figures/chapter_07/fig_1382_1.png]

Figure 7-367 details the allocation of register bits of the Shadow Functions Capability register; Table 7-320 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

[figures/chapter_07/fig_1382_1.png]

图 7-367 详述了 Shadow Functions Capability 寄存器的位分配；表 7-320 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-367. Shadow Functions Capability Register | 图 7-367. Shadow Functions 能力寄存器**

**Table 7-320. Shadow Functions Capability Register | 表 7-320. Shadow Functions 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | Number of Shadow Functions – This is one less than the number of Shadow Functions implemented by this Function. This defines the number of Shadow Function Instance register entries that are in the Capability, and therefore the length of the Capability structure.<br>The default value for this field is 00h. | HwInit |
| 31:8 | RsvdP | RsvdP |

[figures/chapter_07/fig_1382_1.png](figures/chapter_07/fig_1382_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-368 details the allocation of register bits of the Shadow Functions Control register; Table 7-321 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-368 详述了 Shadow Functions Control 寄存器的位分配；表 7-321 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-368. Shadow Functions Control Register | 图 7-368. Shadow Functions 控制寄存器**

**Table 7-321. Shadow Functions Control Register | 表 7-321. Shadow Functions 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Shadow Functions Enable - When Set, permits the Requester to generate Requests using the Transaction ID resources of all of the Shadow Functions defined by this Capability. See Section 7.9.25 for limitations on the type of Requests permitted.<br>When Clear, the Requester is not permitted to generate Requests using the Transaction ID resources of any of the Shadow Functions defined by this Capability.<br>Behavior is undefined when this bit is Set in Functions with the Phantom Functions Enabled bit Set.<br>Behavior is undefined if the value of this bit is changed while the Function has outstanding Non-Posted Requests.<br>Default is 0b. | RW |
| 31:1 | RsvdP | RsvdP |

[figures/chapter_07/fig_1382_1.png](figures/chapter_07/fig_1382_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-25-2"></a>
## 7.9.25.2 Shadow Functions Capability Register (Offset 04h) | Shadow Functions 能力寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Shadow Functions Capability Register (Offset 04h)

</td>
<td style="background-color:#e8e8e8">

Shadow Functions 能力寄存器（偏移 04h）

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-25-3"></a>
## 7.9.25.3 Shadow Functions Control Register (Offset 08h) | Shadow Functions 控制寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Shadow Functions Control Register (Offset 08h)

</td>
<td style="background-color:#e8e8e8">

Shadow Functions 控制寄存器（偏移 08h）

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-25-4"></a>
## 7.9.25.4 Shadow Functions Instance Register Entry | Shadow Functions 实例寄存器项

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-369 details the allocation of register bits of the Shadow Functions Control register; Table 7-322 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-369 详述了 Shadow Functions Control 寄存器的位分配；表 7-322 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-369. Shadow Functions Instance Register Entry | 图 7-369. Shadow Functions 实例寄存器项**

**Table 7-322. Shadow Functions Instance Register Entry | 表 7-322. Shadow Functions 实例寄存器项**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | Shadow Function Number - This is the Bus/Device/Function offset (Bus/Function offset for ARI Devices) of the Shadow Function. Add this value to BDF of the Function with this capability using unsigned, 16-bit arithmetic, ignoring any carry. | HwInit |
| 31:16 | RsvdP | RsvdP |

[figures/chapter_07/fig_1382_1.png](figures/chapter_07/fig_1382_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26"></a>
## 7.9.26 IDE Extended Capability | IDE 扩展能力


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

All Ports that implement IDE (完整性与数据加密, Integrity and Data Encryption) must implement the IDE Extended Capability. The IDE Extended Capability must consist of the IDE Extended Capability Header, the IDE Capability Register, and the IDE Control Register, followed by zero to 8 Link IDE register blocks, followed by zero to 255 Selective IDE register blocks (see Figure 7-370). All Ports that implement IDE must implement the IDE Extended Capability. The IDE Extended Capability must consist of the IDE Extended Capability Header, the IDE Capability Register, and the IDE Control Register, followed by zero to 8 Link IDE register blocks, followed by zero to 255 Selective IDE register blocks (see Figure 7-370).

It is permitted to implement this extended capability in Functions associated with Downstream Ports, and in Function 0 associated with an Upstream Port. Multi-Function Devices associated with Upstream Ports, including cases where one or more Functions represent the Upstream Port of a Switch (交换机), must be implemented such that Function 0 implements this extended capability representing the Multi-Function Device as a whole.

</td>
<td style="background-color:#e8e8e8">

所有实现 IDE (完整性与数据加密, Integrity and Data Encryption) 的端口必须实现 IDE 扩展能力。IDE 扩展能力必须由 IDE 扩展能力头、IDE 能力寄存器、IDE 控制寄存器组成，其后跟随 0 到 8 个 Link IDE 寄存器块，再其后跟随 0 到 255 个 Selective IDE 寄存器块（见图 7-370）。所有实现 IDE 的端口必须实现 IDE 扩展能力。IDE 扩展能力必须由 IDE 扩展能力头、IDE 能力寄存器、IDE 控制寄存器组成，其后跟随 0 到 8 个 Link IDE 寄存器块，再其后跟随 0 到 255 个 Selective IDE 寄存器块（见图 7-370）。

允许在以下位置实现此扩展能力：与下游端口 (Downstream Port) 关联的功能中，以及与上游端口 (Upstream Port) 关联的 Function 0 中。与上游端口关联的多功能设备（包括一个或多个功能表示交换机 (Switch) 上游端口的情况）必须按如下方式实现：Function 0 实现此扩展能力以代表整个多功能设备。

</td>
</tr>
</tbody>
</table>
</div>


**Figure 7-370. IDE Extended Capability Structure | 图 7-370. IDE 扩展能力结构**

[figures/chapter_07/fig_1383_1.png](figures/chapter_07/fig_1383_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-1"></a>
## 7.9.26.1 IDE Extended Capability Header (Offset 00h) | IDE 扩展能力头（偏移 00h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Extended Capability ID for the Integrity and Data Encryption (IDE) Exchange Extended Capability is 0030h.

</td>
<td style="background-color:#e8e8e8">

完整性数据加密 (Integrity and Data Encryption, IDE) 交换扩展能力的扩展能力 ID 为 0030h。

</td>
</tr>
</tbody>
</table>

**Figure 7-371. IDE Extended Capability Header | 图 7-371. IDE 扩展能力头**

**Table 7-323. IDE Extended Capability Header | 表 7-323. IDE 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | PCI Express Extended Capability ID – This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability.<br>The Extended Capability ID for the Integrity and Data Encryption (IDE) Exchange Extended Capability is 0030h. | HwInit |
| 19:16 | Capability Version – This field is a PCI-SIG defined version number that indicates the version of the Capability structure present.<br>Must be 1h for this version of the specification. | HwInit |
| 31:20 | Next Capability Offset – This field contains the offset to the next PCI Express Extended Capability structure or 000h if no other items exist in the linked list of Capabilities. | HwInit |

[figures/chapter_07/fig_1383_1.png](figures/chapter_07/fig_1383_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-2"></a>
## 7.9.26.2 IDE Capability Register (Offset 04h) | IDE 能力寄存器（偏移 04h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-372 details the allocation of register bits of the IDE Capability Register; Table 7-324 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-372 详述了 IDE 能力寄存器的位分配；表 7-324 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-372. IDE Capability Register | 图 7-372. IDE 能力寄存器**

**Table 7-324. IDE Capability Register | 表 7-324. IDE 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Link IDE Stream Supported – When Set, indicates that the Port supports Link IDE Streams, and that one or more Link IDE Stream Registers block(s) immediately follow the IDE Control Register, per the value in the Number of TCs Supported for Link IDE field.<br>When Clear, there must be no Link IDE Stream Register blocks present. | HwInit / RsvdP |
| 1 | Selective IDE Streams Supported – When Set, indicates that the Port support Selective IDE Streams, and that one or more Selective IDE Stream Register block(s) are implemented, per the value in the Number of Selective IDE Streams Supported field.<br>When Clear, there must be no Selective IDE Stream Register blocks present. | HwInit / RsvdP |
| 2 | Flow-Through IDE Stream Supported – For a Switch or Root Port, when Set indicates support for passing Selective IDE Streams to all other Switch or Root Ports.<br>If this bit is Set and both Link IDE Stream Supported and Selective IDE Streams Supported are Clear, then no Link IDE register blocks or Selective IDE register blocks are required.<br>Reserved for Endpoints. | HwInit / RsvdP |
| 3 | Partial Header Encryption Supported – If Link IDE Stream Supported or Selective IDE Streams Supported are Set, then this bit, when Set, indicates the Port supports partial header encryption.<br>Undefined if Link IDE Stream Supported and Selective IDE Streams Supported are both Clear. | HwInit |
| 4 | Aggregation Supported – If Link IDE Stream Supported or Selective IDE Streams Supported are Set, then this bit, when Set, indicates the Port supports aggregation.<br>Undefined if Link IDE Stream Supported and Selective IDE Streams Supported are both Clear. | HwInit |
| 5 | PCRC Supported – When Set, indicates that the Port supports the generation and checking of PCRC. | HwInit |
| 6 | IDE_KM Protocol Supported – When Set, indicates that the Port supports the IDE_KM protocol in the responder role as defined in Section 6.33.3 | HwInit |
| 7 | Selective IDE for Configuration Requests Supported – For a Root Port, Switch Upstream Port, or Endpoint Upstream Port, if Selective IDE Streams Supported is Set, then this bit, if Set, indicates that the Port supports the assocation of Configuration Requests with Selective IDE Streams.<br>For a Switch Upstream Port, when Set, this bit indicates the Switch supports Selective IDE for Configuration Requests targeting all Functions of the Switch.<br>This bit is Reserved for Switch Downstream Ports.<br>If Selective IDE Streams Supported is Clear, this bit is Reserved. | HwInit / RsvdP |
| 12:8 | Supported Algorithms – Indicates the supported algorithms for securing IDE TLPs, encoded as:<br>0 0000b = AES-GCM 256 key size, 96b MAC<br>Others = Reserved | HwInit |
| 15:13 | Number of TCs Supported for Link IDE – If Link IDE Stream Supported is Set, indicates the number of TCs supported for Link IDE Streams encoded as:<br>000b = One TC supported<br>001b = 2 TCs supported<br>010b = 3 TCs supported<br>011b = 4 TCs supported<br>100b = 5 TCs supported<br>101b = 6 TCs supported<br>110b = 7 TCs supported<br>111b = 8 TCs supported<br>If Link IDE Stream Supported is Clear, this field is undefined. | HwInit |
| 23:16 | Number of Selective IDE Streams Supported – If Selective IDE Streams Supported is Set then this field indicates number of Selective IDE Streams Supported such that 0=1 Stream.<br>A corresponding number of Selective IDE Stream Register Block(s) must be implemented. If Link IDE Stream Supported is Clear, then these blocks must immediately follow the IDE Control Register. If Link IDE Stream Supported is Set, then these blocks must immediately follow the Link IDE Stream Control and Status Registers.<br>If Selective IDE Streams Supported is Clear, this field is undefined. | HwInit / RsvdP |
| 24 | TEE-Limited Stream Supported – When Set, indicates that the TEE-Limited Stream control mechanism is supported.<br>If Selective IDE Streams Supported is Clear, this bit is Reserved. | HwInit / RsvdP |
| 31:25 | RsvdP | RsvdP |

[figures/chapter_07/fig_1385_1.png](figures/chapter_07/fig_1385_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-3"></a>
## 7.9.26.3 IDE Control Register (Offset 08h) | IDE 控制寄存器（偏移 08h）

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-373 details the allocation of register bits of the IDE Control Register; Table 7-325 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-373 详述了 IDE 控制寄存器的位分配；表 7-325 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-373. IDE Control Register | 图 7-373. IDE 控制寄存器**

**Table 7-325. IDE Control Register | 表 7-325. IDE 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2 | Flow-Through IDE Stream Enabled – For Switch Ports and Root Ports, Enables the Port for flow-through operation of TLPs associated with Selective IDE Streams.<br>Reserved for Upstream Ports associated with Endpoints. | RW / RsvdP |
| 31:3 | RsvdP | RsvdP |

[figures/chapter_07/fig_1387_1.png](figures/chapter_07/fig_1387_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-4"></a>
## 7.9.26.4 Link IDE Register Block | Link IDE 寄存器块

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

A Link IDE register block must consist of one Link IDE Stream Control Register followed by one Link IDE Stream Status Register. If the Link IDE Stream Supported bit in the IDE Capability Register is Set, then this register block must be instantiated once for each Traffic Class (TC) supported as indicated in the Number of TCs Supported for Link IDE field.

</td>
<td style="background-color:#e8e8e8">

Link IDE 寄存器块必须由一个 Link IDE Stream Control 寄存器和一个 Link IDE Stream Status 寄存器组成。如果 IDE 能力寄存器中的 Link IDE Stream Supported 位被置位，则该寄存器块必须为 Number of TCs Supported for Link IDE 字段所指示的每个流量类 (Traffic Class, TC) 实例化一次。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-4-1"></a>
## 7.9.26.4.1 Link IDE Stream Control Register | Link IDE Stream 控制寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-374 details the allocation of register bits of the Link IDE Stream Control Register; Table 7-326 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-374 详述了 Link IDE Stream Control 寄存器的位分配；表 7-326 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-374. Link IDE Stream Control Register | 图 7-374. Link IDE Stream 控制寄存器**

**Table 7-326. Link IDE Stream Control Register | 表 7-326. Link IDE Stream 控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | Link IDE Stream Enable – When Set, enables Link IDE Stream such that IDE operation will start when triggered by means of the IDE_KM protocol (see Section 6.33.3). When Cleared, must immediately transition the Stream to Insecure.<br>Software must not modify the PCRC Enable bit while this bit is Set; otherwise, the result is undefined.<br>It is permitted for the default value to be 1b if and only if implementation specific means can ensure that the Link IDE Stream will default into a state where operation in the Secure state is possible, otherwise the default value must be 0b. | RW |
| 3:2 | Tx Aggregation Mode NPR – If Aggregation Supported is Set then this field selects the level of aggregation for Transmitted Non-Posted Requests for this Stream, encoded as:<br>00b = No aggregation<br>01b = Up to 2 Non-Posted Requests<br>10b = Up to 4 Non-Posted Requests<br>11b = Up to 8 Non-Posted Requests<br>Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |
| 5:4 | Tx Aggregation Mode PR – If Aggregation Supported is Set then this field selects the level of aggregation for Transmitted Posted Requests for this Stream, encoded as:<br>00b = No aggregation<br>01b = Up to 2 Posted Requests<br>10b = Up to 4 Posted Requests<br>11b = Up to 8 Posted Requests<br>Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |
| 7:6 | Tx Aggregation Mode CPL – If Aggregation Supported is Set then this field selects the level of aggregation for Trasmitted Completions for this Stream, encoded as:<br>00b = No aggregation<br>01b = Up to 2 Completions<br>10b = Up to 4 Completions<br>11b = Up to 8 Completions<br>Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |
| 8 | PCRC Enable – When Set, Transmitted IDE TLPs associated with this Stream that include P content must include PCRC, and Received TLPs must be checked for PCRC failure.<br>Reserved if PCRC Supported is Clear.<br>Default value is 0b. | RW / RsvdP |
| 13:10 | Partial Header Encryption Mode – Selects the mode to be used for partial header encryption of IDE TLPs for this IDE Stream. Must be programmed to the same value in both the Partner Ports. Must be configured while Link IDE Stream Enable is Clear. When Link IDE Stream Enable is Set, the setting is sampled, and this field becomes RO with reads returning the sampled value.<br>0000b = No partial header encryption<br>0001b = Address[17:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0010b = Address[25:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0011b = Address[33:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0100b = Address[41:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>Others = Reserved<br>If Partial Header Encryption Supported is Clear, this field is Reserved. | RW / RO / RsvdP |
| 18:14 | Selected Algorithm – Selects the algorithm to be used for securing IDE TLPs for this IDE Stream. Must be programmed to the same value in both the Upstream and Downstream Ports. Must be configured while Link IDE Stream Enable is Clear. When Link IDE Stream Enable is Set, the setting is sampled, and this field becomes RO with reads returning the sampled value.<br>0 0000b = AES-GCM 256 key size, 96b MAC<br>Others = Reserved | RW / RO |
| 21:19 | TC – System firmware/software must program this field to indicate the TC associated with this Link IDE Register block.<br>Default value is 000b | RW / RsvdP |
| 31:24 | Stream ID – Indicates the Stream ID associated with this Link IDE Stream. Software must program the same Stream ID into both Ports associated with a given Link IDE Stream. Default value is 00h. | RW |

[figures/chapter_07/fig_1387_1.png](figures/chapter_07/fig_1387_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-4-2"></a>
## 7.9.26.4.2 Link IDE Stream Status Register | Link IDE Stream 状态寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-375 details the allocation of register bits of the Link IDE Stream Status Register; Table 7-327 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-375 详述了 Link IDE Stream Status 寄存器的位分配；表 7-327 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-375. Link IDE Stream Status Register | 图 7-375. Link IDE Stream 状态寄存器**

**Table 7-327. Link IDE Stream Status Register | 表 7-327. Link IDE Stream 状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 3:0 | Link IDE Stream State – When Link IDE Stream Enable is Set, this field indicates the state of the Port. Encodings:<br>0000b = Insecure<br>Others = Secure<br>Reserved – Software must handle reserved values as indicating unknown state<br>When Link IDE Stream Enable is Clear, the value of this field must be 0000b. | RO |
| 30:4 | RsvdZ | RsvdZ |
| 31 | Received IDE Fail Message – When Set, indicates that one or more IDE Fail Message(s) have been Received for this Stream. | RW1C |

[figures/chapter_07/fig_1389_1.png](figures/chapter_07/fig_1389_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5"></a>
## 7.9.26.5 Selective IDE Stream Register Block | Selective IDE Stream 寄存器块


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

A Selective IDE Stream register block must consist of one Selective IDE Stream Capability Register, followed by one Selective IDE Stream Control Register, followed by one Selective IDE Stream Status Register, followed by one Selective IDE RID Association register Block, followed by zero or more Selective IDE Address Association Register Block(s). If the Selective IDE Streams Supported bit in the IDE Capability Register is Set, then this register block must be instantiated once for each Selective IDE Stream supported as indicated in the Number of Selective IDE Streams Supported field.

</td>
<td style="background-color:#e8e8e8">

Selective IDE Stream 寄存器块必须由一个 Selective IDE Stream Capability 寄存器、一个 Selective IDE Stream Control 寄存器、一个 Selective IDE Stream Status 寄存器、一个 Selective IDE RID Association 寄存器块以及零个或多个 Selective IDE Address Association 寄存器块组成。如果 IDE 能力寄存器中的 Selective IDE Streams Supported 位被置位，则该寄存器块必须为 Number of Selective IDE Streams Supported 字段所指示的每个 Selective IDE Stream 实例化一次。

</td>
</tr>
</tbody>
</table>
</div>


**Figure 7-376. Selective IDE Stream Capability Register | 图 7-376. Selective IDE Stream 能力寄存器**

**Table 7-328. Selective IDE Stream Capability Register | 表 7-328. Selective IDE Stream 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 3:0 | Number of Address Association Register Blocks – Indicates the number of Selective IDE Address Association register blocks for this Selective IDE Stream.<br>The number of Selective IDE Address Association register blocks for a given IDE Stream is hardware implementation specific, and is permitted to be any number between 0 and 15. | RO |
| 31:4 | RsvdP | RsvdP |

[figures/chapter_07/fig_1390_1.png](figures/chapter_07/fig_1390_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

**Figure 7-377. Selective IDE Stream Control Register | 图 7-377. Selective IDE Stream 控制寄存器**

[figures/chapter_07/fig_1390_1.png](figures/chapter_07/fig_1390_1.png)

[⬆️ 返回目录](#-本章目录-table-of-contents)

---


---

<a id="sec-7-9-26-5-1"></a>
## 7.9.26.5.1 Selective IDE Stream Capability Register | 选择性 IDE 流能力寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

(Register definition is referenced from the Selective IDE Stream Extended Capability structure; this sub-section introduces the Capability register layout. Refer to the Selective IDE Stream Extended Capability structure for the overall arrangement.)

</td>
<td style="background-color:#e8e8e8">

(寄存器定义引用自 Selective IDE Stream 扩展能力结构；本小节介绍 Capability 寄存器的布局。整体安排请参阅 Selective IDE Stream 扩展能力结构。)

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-2"></a>
## 7.9.26.5.2 Selective IDE Stream Control Register | 选择性 IDE 流控制寄存器

<!-- 📄 Page 1391 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Table 7-329. Selective IDE Stream Control Register**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 0 | Selective IDE Stream Enable – When Set, enables this IDE Stream such that IDE operation will start when triggered by means of the IDE_KM protocol (see § Section 6.33.3 ). When Cleared, must immediately transition the Stream to Insecure. Software must configure the following before Setting this bit, and must not modify them while this bit is Set; otherwise, the result is undefined:<br>• Selected Algorithm (below)<br>• PCRC Enable<br>• Requester ID Limit in IDE RID Association Register 1<br>• Requester ID Base, and Segment Base if applicable, in IDE RID Association Register 2<br>• V bit in IDE RID Association Register 2<br>If this bit is Set when the V bit is Clear, the IDE Stream must transition to Insecure.<br>When Cleared, must immediately transition the Stream to Insecure.<br>It is strongly recommended that the IDE Address Association Registers, and the Default Stream bit (if applicable), also be programmed prior to Setting this bit.<br>Default value is 0b. | RW |
| 3:2 | Tx Aggregation Mode NPR – If Aggregation Supported is Set then this field selects the level of aggregation for Transmitted Non-Posted Requests for this Stream, encoded as:<br>00b – No aggregation<br>01b – Up to 2 Non-Posted Requests<br>10b – Up to 4 Non-Posted Requests<br>11b – Up to 8 Non-Posted Requests<br>00b – Reserved If Aggregation Supported is Clear.<br>01b – Reserved If Aggregation Supported is Clear.<br>10b – Reserved If Aggregation Supported is Clear.<br>11b – Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |
| 5:4 | Tx Aggregation Mode PR – If Aggregation Supported is Set then this field selects the level of aggregation for Transmitted Posted Requests for this Stream, encoded as:<br>00b – No aggregation<br>01b – Up to 2 Posted Requests<br>10b – Up to 4 Posted Requests<br>11b – Up to 8 Posted Requests<br>00b – Reserved If Aggregation Supported is Clear.<br>01b – Reserved If Aggregation Supported is Clear.<br>10b – Reserved If Aggregation Supported is Clear.<br>11b – Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |
| 7:6 | Tx Aggregation Mode CPL – If Aggregation Supported is Set then this field selects the level of aggregation for Trasmitted Completions for this Stream, encoded as:<br>00b – No aggregation<br>01b – Up to 2 Completions<br>10b – Up to 4 Completions<br>11b – Up to 8 Completions<br>00b – Reserved If Aggregation Supported is Clear.<br>01b – Reserved If Aggregation Supported is Clear.<br>10b – Reserved If Aggregation Supported is Clear.<br>11b – Reserved If Aggregation Supported is Clear.<br>Default value is 00b | RW / RsvdP |

</td>
<td style="background-color:#e8e8e8">

**表 7-329. 选择性 IDE 流控制寄存器 (Selective IDE Stream Control Register)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Selective IDE Stream Enable(选择性 IDE 流使能)— 置 1 时,使能此 IDE 流,使得 IDE 操作在通过 IDE_KM 协议触发时启动(见 § Section 6.33.3 )。清零时,必须立即将流迁移到 Insecure(不安全)状态。软件必须在置位此位之前配置以下内容,且在此位置 1 期间不得修改,否则结果是未定义的:<br>• Selected Algorithm(见下文)<br>• PCRC Enable<br>• IDE RID Association Register 1 中的 Requester ID Limit<br>• IDE RID Association Register 2 中的 Requester ID Base,以及 Segment Base(若适用)<br>• IDE RID Association Register 2 中的 V 位<br>如果 V 位为 0 时此位被置 1,则 IDE 流必须迁移到 Insecure 状态。<br>当清零时,必须立即将流迁移到 Insecure 状态。<br>强烈建议在置位此位之前也编程 IDE Address Association Registers 以及 Default Stream 位(若适用)。<br>默认值为 0b。 | RW |
| 3:2 | Tx Aggregation Mode NPR(发送聚合模式 — Non-Posted 请求)— 如果 Aggregation Supported 置 1,则此字段为此流的发送 Non-Posted 请求选择聚合级别,编码如下:<br>00b — 无聚合<br>01b — 最多 2 个 Non-Posted 请求<br>10b — 最多 4 个 Non-Posted 请求<br>11b — 最多 8 个 Non-Posted 请求<br>00b — 若 Aggregation Supported 为 0 则保留。<br>01b — 若 Aggregation Supported 为 0 则保留。<br>10b — 若 Aggregation Supported 为 0 则保留。<br>11b — 若 Aggregation Supported 为 0 则保留。<br>默认值为 00b | RW / RsvdP |
| 5:4 | Tx Aggregation Mode PR(发送聚合模式 — Posted 请求)— 如果 Aggregation Supported 置 1,则此字段为此流的发送 Posted 请求选择聚合级别,编码如下:<br>00b — 无聚合<br>01b — 最多 2 个 Posted 请求<br>10b — 最多 4 个 Posted 请求<br>11b — 最多 8 个 Posted 请求<br>00b — 若 Aggregation Supported 为 0 则保留。<br>01b — 若 Aggregation Supported 为 0 则保留。<br>10b — 若 Aggregation Supported 为 0 则保留。<br>11b — 若 Aggregation Supported 为 0 则保留。<br>默认值为 00b | RW / RsvdP |
| 7:6 | Tx Aggregation Mode CPL(发送聚合模式 — 完成报文)— 如果 Aggregation Supported 置 1,则此字段为此流的发送 Completion 选择聚合级别,编码如下:<br>00b — 无聚合<br>01b — 最多 2 个 Completion<br>10b — 最多 4 个 Completion<br>11b — 最多 8 个 Completion<br>00b — 若 Aggregation Supported 为 0 则保留。<br>01b — 若 Aggregation Supported 为 0 则保留。<br>10b — 若 Aggregation Supported 为 0 则保留。<br>11b — 若 Aggregation Supported 为 0 则保留。<br>默认值为 00b | RW / RsvdP |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-2-cont"></a>
## 7.9.26.5.2 Selective IDE Stream Control Register (continued) | 选择性 IDE 流控制寄存器(续)

<!-- 📄 Page 1392 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Table 7-329. Selective IDE Stream Control Register (continued)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 8 | PCRC Enable – When Set, Transmitted IDE TLPs associated with this Stream that include P content must include PCRC, and Received TLPs must be checked for PCRC failure.<br>Reserved if PCRC Supported is Clear.<br>Default value is 0b. | RW / RsvdP |
| 9 | Selective IDE for Configuration Requests Enable –<br>For Root Ports, if Selective IDE for Configuration Requests Supported is Set, then this bit, when Set, must cause the Port to transmit as IDE TLPs associated with this Selective IDE Stream all Configuration Requests for which the destination RID is greater than or equal to the RID Base and less than or equal to the RID Limit in the Selective IDE RID Association Register Block.<br>For Ports other than Root Ports, this bit is Reserved.<br>If Selective IDE for Configuration Requests Supported is Clear, this bit is Reserved.<br>Default value is 0b. | RW / RsvdP |
| 13:10 | Partial Header Encryption Mode – Selects the mode to be used for partial header encryption of IDE TLPs for this IDE Stream. Must be programmed to the same value in both the Partner Ports. Must be configured while Selective IDE Stream Enable is Clear. When Selective IDE Stream Enable is Set, the setting is sampled, and this field becomes RO with reads returning the sampled value.<br>0000b – No partial header encryption<br>0001b – Address[17:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0010b – Address[25:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0011b – Address[33:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>0100b – Address[41:2] Encrypted, and, if present, the First DW BE and Last DW BE fields<br>Others – Reserved<br>If Partial Header Encryption Supported is Clear, this field is Reserved. | RW / RO / RsvdP |
| 18:14 | Selected Algorithm – Selects the algorithm to be used for securing IDE TLPs for this IDE Stream. Must be programmed to the same value in both Partner Ports. Must be configured while Selective IDE Stream Enable is Clear. When Selective IDE Stream Enable is Set, the setting is sampled, and this field becomes RO with reads returning the sampled value.<br>0 0000b – AES-GCM 256 key size, 96b MAC<br>Others – Reserved | RW / RO |
| 21:19 | TC – System firmware/software must program this field to indicate the TC associated with this Selective IDE Register block.<br>Default value is 000b | RW |
| 22 | Default Stream – When Set, TLPs using the Traffic Class indicated in the TC field are associated with this Stream, unless the TLP matches some other Selective IDE Stream for the indicated TC. A Default Stream must have the hierarchy domain's Root Port as its Partner Port; otherwise, the result is undefined<br>It is not permitted to configure more than one Default Stream to be associated with the same TC. If this is done, hardware must select one of the Streams to be associated with the TC – the selection is implementation specific.<br>Applicable for Endpoint Upstream Ports only. Reserved for other Port types.<br>Default value is 0b. | RW / RsvdP |
| 23 | TEE-Limited Stream – When Set, requires that, for Requests, only those that have the T bit Set are permitted to be associated with this Stream. | RW / RO / RsvdP |

</td>
<td style="background-color:#e8e8e8">

**表 7-329. 选择性 IDE 流控制寄存器 (Selective IDE Stream Control Register)(续)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 8 | PCRC Enable(PCRC 使能)— 置 1 时,与此流关联且包含 P 内容的发送 IDE TLP 必须包含 PCRC,且对接收的 TLP 必须检查 PCRC 错误。<br>若 PCRC Supported 为 0 则保留。<br>默认值为 0b。 | RW / RsvdP |
| 9 | Selective IDE for Configuration Requests Enable(选择性 IDE 配置请求使能)—<br>对于 Root Port(根端口),若 Selective IDE for Configuration Requests Supported 置 1,则当此位置 1 时,必须使端口将所有目标 RID 大于等于 RID Base 且小于等于 Selective IDE RID Association Register Block 中 RID Limit 的 Configuration Request(配置请求),作为与此 Selective IDE 流关联的 IDE TLP 进行发送。<br>对于非 Root Port,此位保留。<br>若 Selective IDE for Configuration Requests Supported 为 0,则此位保留。<br>默认值为 0b。 | RW / RsvdP |
| 13:10 | Partial Header Encryption Mode(部分包头加密模式)— 选择用于此 IDE 流的 IDE TLP 的部分包头加密模式。必须在两个 Partner Port 中编程为相同的值。必须在 Selective IDE Stream Enable 为 0 时配置。当 Selective IDE Stream Enable 置 1 时,该设置被采样,该字段变为 RO,读取返回采样值。<br>0000b — 无部分包头加密<br>0001b — Address[17:2] 加密,且若存在则 First DW BE 和 Last DW BE 字段也加密<br>0010b — Address[25:2] 加密,且若存在则 First DW BE 和 Last DW BE 字段也加密<br>0011b — Address[33:2] 加密,且若存在则 First DW BE 和 Last DW BE 字段也加密<br>0100b — Address[41:2] 加密,且若存在则 First DW BE 和 Last DW BE 字段也加密<br>Others — 保留<br>若 Partial Header Encryption Supported 为 0,则此字段保留。 | RW / RO / RsvdP |
| 18:14 | Selected Algorithm(所选算法)— 选择用于保护此 IDE 流的 IDE TLP 的算法。必须在两个 Partner Port 中编程为相同的值。必须在 Selective IDE Stream Enable 为 0 时配置。当 Selective IDE Stream Enable 置 1 时,该设置被采样,该字段变为 RO,读取返回采样值。<br>0 0000b — AES-GCM 256 密钥长度,96b MAC<br>Others — 保留 | RW / RO |
| 21:19 | TC(流量类)— 系统固件/软件必须编程此字段以指示与此 Selective IDE 寄存器块关联的 TC。<br>默认值为 000b | RW |
| 22 | Default Stream(默认流)— 置 1 时,使用 TC 字段指示的流量类的 TLP 将与此流关联,除非该 TLP 与指定 TC 的其他 Selective IDE 流匹配。Default Stream 必须将层级域的 Root Port 作为其 Partner Port;否则结果是未定义的。<br>不允许将多于一个 Default Stream 配置为与同一 TC 关联。如果这样做,硬件必须选择其中一个流与该 TC 关联——选择是实现特定的。<br>仅适用于 Endpoint(端点)Upstream Port。其他端口类型保留。<br>默认值为 0b。 | RW / RsvdP |
| 23 | TEE-Limited Stream(TEE 限制流)— 置 1 时,要求仅允许 T 位置 1 的请求与此流关联。 | RW / RO / RsvdP |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-2-finish"></a>
## 7.9.26.5.2 Selective IDE Stream Control Register (continued) | 选择性 IDE 流控制寄存器(续)

<!-- 📄 Page 1393 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

**Table 7-329. Selective IDE Stream Control Register (continued)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 23 (cont.) | TEE-Limited Stream – Must be configured while Selective IDE Stream Enable is Clear, during which time this bit is RW. When Selective IDE Stream Enable is Set set to 1b, the setting is sampled, and this field bit becomes RO with reads returning the sampled value, during the time when Selective IDE Stream Enable remains Set.<br>Reserved if TEE-Limited Stream Supported is Clear.<br>Default value is 0b. | RW / RO / RsvdP |
| 31:24 | Stream ID – Indicates the Stream ID associated with this Selective IDE Stream. Software must program the same Stream ID into both Ports associated with a given Selective IDE Stream. Default value is 00h. | RW |

</td>
<td style="background-color:#e8e8e8">

**表 7-329. 选择性 IDE 流控制寄存器 (Selective IDE Stream Control Register)(续)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 23(续) | TEE-Limited Stream(TEE 限制流)— 必须在 Selective IDE Stream Enable 为 0 时配置,此时该位为 RW。当 Selective IDE Stream Enable 置 1 后,该设置被采样,该字段位变为 RO,在 Selective IDE Stream Enable 保持置 1 期间读取返回采样值。<br>若 TEE-Limited Stream Supported 为 0 则保留。<br>默认值为 0b。 | RW / RO / RsvdP |
| 31:24 | Stream ID(流 ID)— 指示与此 Selective IDE 流关联的 Stream ID。软件必须将与同一 Selective IDE 流关联的两个端口编程为相同的 Stream ID。默认值为 00h。 | RW |

</td>
</tr>
</tbody>
</table>
</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-3"></a>
## 7.9.26.5.3 Selective IDE Stream Status Register | 选择性 IDE 流状态寄存器

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-378.** Selective IDE Stream Status Register
> <img src="figures/chapter_07/fig_1393_1_tight.png" width="700">

> **Figure 7-378 (Register Layout).** Selective IDE Stream Status Register
>
> | Bits 31 | Bits 30:4 | Bits 3:0 |
> |---------|-----------|----------|
> | Received IDE Fail Message | RsvdZ | Selective IDE Stream State |

**Table 7-330. Selective IDE Stream Status Register**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 3:0 | Selective IDE Stream State – When Selective IDE Stream Enable is Set, this field indicates the state of the Port. Encodings:<br>0000b – Insecure<br>0001b – Secure<br>0010b – Reserved – Software must handle reserved values as indicating unknown state<br>Others – Reserved – Software must handle reserved values as indicating unknown state<br>When Selective IDE Stream Enable is Clear, the value of this field must be 0000b. | RO |
| 31 | Received IDE Fail Message – When Set, indicates that one or more IDE Fail Message(s) have been Received for this Stream. | RW1C |

</td>
<td style="background-color:#e8e8e8">


> **图 7-378(寄存器布局)。** 选择性 IDE 流状态寄存器
>
> | 位 31 | 位 30:4 | 位 3:0 |
> |-------|---------|--------|
> | Received IDE Fail Message(已接收 IDE 失败消息) | RsvdZ | Selective IDE Stream State(选择性 IDE 流状态) |

**表 7-330. 选择性 IDE 流状态寄存器 (Selective IDE Stream Status Register)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 3:0 | Selective IDE Stream State(选择性 IDE 流状态)— 当 Selective IDE Stream Enable 置 1 时,此字段指示端口的状态。编码:<br>0000b — Insecure(不安全)<br>0001b — Secure(安全)<br>0010b — 保留 — 软件必须将保留值视为指示未知状态<br>Others — 保留 — 软件必须将保留值视为指示未知状态<br>当 Selective IDE Stream Enable 为 0 时,此字段的值必须为 0000b。 | RO |
| 31 | Received IDE Fail Message(已接收 IDE 失败消息)— 置 1 时,指示已为此流接收到一条或多条 IDE Fail Message。 | RW1C |

<img src="figures/chapter_07/fig_1393_1_tight.png" width="700">
</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-4"></a>
## 7.9.26.5.4 Selective IDE RID Association Register Block | 选择性 IDE RID 关联寄存器块

<!-- 📄 Page 1394 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

A Selective IDE RID Association register must consist of one IDE RID Association Register 1 followed by one IDE RID Association Register 2.

</td>
<td style="background-color:#e8e8e8">

一个 Selective IDE RID Association 寄存器必须由一个 IDE RID Association Register 1 后跟一个 IDE RID Association Register 2 组成。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-4-1"></a>
## 7.9.26.5.4.1 IDE RID Association Register 1 | IDE RID 关联寄存器 1


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-379 (Register Layout).** IDE RID Association Register 1 (Offset +00h)
>
> | Bits 31:24 | Bits 23:8 | Bits 7:0 |
> |-----------|-----------|----------|
> | RsvdP | RID Limit | RsvdP |

**Table 7-331. IDE RID Association Register 1 (Offset +00h)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 23:8 | RID Limit – Indicates the highest value RID in the range associated with this Stream ID at the IDE Partner Port.<br>The Segment Number associated with this field is contained in Segment Base in the IDE RID Association Register 2. | RW |

</td>
<td style="background-color:#e8e8e8">

> **图 7-379(寄存器布局)。** IDE RID 关联寄存器 1 (Offset +00h)
>
> | 位 31:24 | 位 23:8 | 位 7:0 |
> |----------|---------|--------|
> | RsvdP | RID Limit(RID 上限) | RsvdP |

**表 7-331. IDE RID 关联寄存器 1 (Offset +00h)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 23:8 | RID Limit(RID 上限)— 指示在 IDE Partner Port 与此 Stream ID 关联的范围内最高的 RID 值。<br>与此字段关联的 Segment Number 包含在 IDE RID Association Register 2 的 Segment Base 中。 | RW |

</td>
</tr>
</tbody>
</table>

> **Figure 7-379.** IDE RID Association Register 1 (Offset +00h)
> <img src="figures/chapter_07/fig_1394_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-4-2"></a>
## 7.9.26.5.4.2 IDE RID Association Register 2 | IDE RID 关联寄存器 2

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-380 (Register Layout).** IDE RID Association Register 2 (Offset +04h)
>
> | Bits 31:24 | Bits 23:8 | Bits 7:1 | Bit 0 |
> |-----------|-----------|---------|-------|
> | Segment Base | RID Base | RsvdP | Valid (V) |

**Table 7-332. IDE RID Association Register 2 (Offset +04h)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 0 | Valid (V) – When Set, indicates the Segment Base, RID Base and RID Limit fields have been programmed.<br>Default is 0b | RW |
| 23:8 | RID Base – Indicates the lowest value RID in the range associated with this Stream ID at the IDE Partner Port.<br>The Segment Number associated with this field is contained in Segment Base. | RW |
| 31:24 | Segment Base – In Flit Mode, Indicates the Segment value associated with this Stream ID at the IDE Partner Port.<br>Reserved if Flit Mode is not supported.<br>If this Selective IDE Stream is within an FM subtree whose Segment Captured bits are Clear, software must set this field to 00h, regardless of the Segment Number value associated with the subtree's RP.<br>Default value is 00h. | RW / RsvdP |

</td>
<td style="background-color:#e8e8e8">


> **图 7-380(寄存器布局)。** IDE RID 关联寄存器 2 (Offset +04h)

> <img src="figures/chapter_07/fig_1077_1_tight.png" width="700">

>
> | 位 31:24 | 位 23:8 | 位 7:1 | 位 0 |
> |----------|---------|---------|------|
> | Segment Base(Segment 基址) | RID Base(RID 基址) | RsvdP | Valid (V)(有效位) |

**表 7-332. IDE RID 关联寄存器 2 (Offset +04h)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 0 | Valid (V)(有效位)— 置 1 时,指示 Segment Base、RID Base 和 RID Limit 字段已被编程。<br>默认为 0b | RW |
| 23:8 | RID Base(RID 基址)— 指示在 IDE Partner Port 与此 Stream ID 关联的范围内最低的 RID 值。<br>与此字段关联的 Segment Number 包含在 Segment Base 中。 | RW |
| 31:24 | Segment Base(Segment 基址)— 在 Flit Mode(Flit 模式)下,指示在 IDE Partner Port 与此 Stream ID 关联的 Segment 值。<br>如果不支持 Flit Mode 则保留。<br>如果此 Selective IDE Stream 位于 Segment Captured 位为 0 的 FM 子树内,软件必须将此字段设置为 00h,与子树 RP 关联的 Segment Number 值无关。<br>默认值为 00h。 | RW / RsvdP |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-5"></a>
## 7.9.26.5.5 Selective IDE Address Association Register Block | 选择性 IDE 地址关联寄存器块

<!-- 📄 Page 1395 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

A Selective IDE Address Association register must consist of one IDE Address Association Register 1, followed by one IDE Address Association Register 2, followed by one IDE Address Association Register 3.

</td>
<td style="background-color:#e8e8e8">

一个 Selective IDE Address Association 寄存器必须由一个 IDE Address Association Register 1 后跟一个 IDE Address Association Register 2 再跟一个 IDE Address Association Register 3 组成。

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-5-1"></a>
## 7.9.26.5.5.1 IDE Address Association Register 1 | IDE 地址关联寄存器 1


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-381 (Register Layout).** IDE Address Association Register 1 (Offset +00h)
>
> | Bits 31:20 | Bits 19:8 | Bits 7:1 | Bit 0 |
> |-----------|-----------|---------|-------|
> | Memory Limit Lower | Memory Base Lower | RsvdP | V (Valid) |

**Table 7-333. IDE Address Association Register 1 (Offset +00h)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 31:20 | Memory Limit Lower – Corresponds to Address bits [31:20]. Address bits [19:0] are implicitly F_FFFFh. | RW |
| 19:8 | Memory Base Lower – Corresponds to Address bits [31:20]. Address[19:0] bits are implicitly 0_0000h. | RW |
| 0 | V (Valid) – When Set, indicates this IDE Stream Association Block is valid, that the address range defined by Memory Base and Memory Limit corresponding to a range of memory addresses assigned to the IDE Partner Port, and that all Transmitted Address Routed TLPs within this address range must be associated with this IDE Stream, subject to rules stated in § Section 6.33.4 .<br>Hardware behavior is undefined if overlapping address ranges are assigned for different IDE Streams.<br>Default is 0b | RW |

</td>
<td style="background-color:#e8e8e8">

> **图 7-381(寄存器布局)。** IDE 地址关联寄存器 1 (Offset +00h)
>
> | 位 31:20 | 位 19:8 | 位 7:1 | 位 0 |
> |----------|---------|---------|------|
> | Memory Limit Lower(内存下限低位) | Memory Base Lower(内存基址低位) | RsvdP | V (Valid)(有效位) |

**表 7-333. IDE 地址关联寄存器 1 (Offset +00h)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 31:20 | Memory Limit Lower(内存下限低位)— 对应地址位 [31:20]。地址位 [19:0] 隐含为 F_FFFFh。 | RW |
| 19:8 | Memory Base Lower(内存基址低位)— 对应地址位 [31:20]。地址位 [19:0] 隐含为 0_0000h。 | RW |
| 0 | V (Valid)(有效位)— 置 1 时,指示此 IDE Stream Association Block 有效,由 Memory Base 和 Memory Limit 定义的地址范围对应分配给 IDE Partner Port 的一段内存地址范围,且该地址范围内的所有发送地址路由 TLP 必须与此 IDE 流关联,前提是遵循 § Section 6.33.4 中所述的规则。<br>如果为不同的 IDE Stream 分配了重叠的地址范围,硬件行为未定义。<br>默认为 0b | RW |

</td>
</tr>
</tbody>
</table>

> **Figure 7-381.** IDE Address Association Register 1 (Offset +00h)
> <img src="figures/chapter_07/fig_1395_1.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-5-2"></a>
## 7.9.26.5.5.2 IDE Address Association Register 2 | IDE 地址关联寄存器 2

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-382 (Register Layout).** IDE Address Association Register 2 (Offset +04h)
>
> | Bits 31:0 |
> |-----------|
> | Memory Limit Upper |

**Table 7-334. IDE Address Association Register 2 (Offset +04h)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 31:0 | Memory Limit Upper – Corresponds to Address bits [63:32] | RW |

</td>
<td style="background-color:#e8e8e8">


> **图 7-382(寄存器布局)。** IDE 地址关联寄存器 2 (Offset +04h)
>
> | 位 31:0 |
> |---------|
> | Memory Limit Upper(内存上限高位) |

**表 7-334. IDE 地址关联寄存器 2 (Offset +04h)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 31:0 | Memory Limit Upper(内存上限高位)— 对应地址位 [63:32] | RW |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-26-5-5-3"></a>
## 7.9.26.5.5.3 IDE Address Association Register 3 | IDE 地址关联寄存器 3


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

> **Figure 7-383 (Register Layout).** IDE Address Association Register 3 (Offset +04h)
>
> | Bits 31:0 |
> |-----------|
> | Memory Base Upper |

**Table 7-335. IDE Address Association Register 3 (Offset +04h)**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 31:0 | Memory Base Upper – Corresponds to Address bits [63:32] | RW |

</td>
<td style="background-color:#e8e8e8">

> **图 7-383(寄存器布局)。** IDE 地址关联寄存器 3 (Offset +04h)
>
> | 位 31:0 |
> |---------|
> | Memory Base Upper(内存基址高位) |

**表 7-335. IDE 地址关联寄存器 3 (Offset +04h)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 31:0 | Memory Base Upper(内存基址高位)— 对应地址位 [63:32] | RW |

</td>
</tr>
</tbody>
</table>

> **Figure 7-383.** IDE Address Association Register 3 (Offset +04h)
> <img src="figures/chapter_07/fig_1396_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-27"></a>
## 7.9.27 Null Capability | 空能力

<!-- 📄 Page 1396 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Null Capability is a capability structure in PCI-compatible Configuration Space (first 256 bytes) as shown in § Figure 7-384.

The Null Capability contains no registers. This capability is present in the linked list (Next Capability Pointer), but should otherwise be ignored by software. The layout of the information is shown in § Figure 7-384.

A single PCI Express Function is permitted to contain multiple Null Capability structures.

> **Figure 7-384 (Register Layout).** Null Capability
>
> | Bits 15:8 | Bits 7:0 |
> |-----------|----------|
> | Next Capability Pointer | Capability ID = 00h |

**Table 7-336. Null Capability**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 7:0 | Capability ID - Indicates the PCI Express Capability structure. This field must return a Capability ID of 00h indicating that this is a Null Capability structure. | RO |
| 15:8 | Next Capability Pointer - This field contains the offset to the next PCI Capability structure or 00h if no other items exist in the linked list of Capabilities. | RO |

</td>
<td style="background-color:#e8e8e8">

Null Capability(空能力)是位于 PCI 兼容配置空间(前 256 字节)中的一种能力结构,如 § Figure 7-384 所示。

Null Capability 不包含任何寄存器。该能力出现在链表(Next Capability Pointer)中,但软件应忽略其内容。信息的布局如 § Figure 7-384 所示。

允许单个 PCI Express Function(功能)包含多个 Null Capability 结构。

> **图 7-384.** 空能力 (Null Capability)
> <img src="figures/chapter_07/fig_1396_1_tight.png" width="700">

> **图 7-384(寄存器布局)。** 空能力
>
> | 位 15:8 | 位 7:0 |
> |---------|---------|
> | Next Capability Pointer(下一能力指针) | Capability ID = 00h |

**表 7-336. 空能力 (Null Capability)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 7:0 | Capability ID(能力 ID)— 指示 PCI Express Capability 结构。此字段必须返回 00h 的 Capability ID,以指示这是一个 Null Capability 结构。 | RO |
| 15:8 | Next Capability Pointer(下一能力指针)— 此字段包含指向下一个 PCI Capability 结构的偏移,若链表中不存在其他项则为 00h。 | RO |

</td>
</tr>
</tbody>
</table>

[⬆️ 返回目录](#-本章目录-table-of-contents)

---

<a id="sec-7-9-28"></a>
## 7.9.28 Null Extended Capability | 空扩展能力

<!-- 📄 Page 1397 -->
---


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The Null Extended Capability is an optional Extended Capability that is permitted to be implemented by any PCI Express Function or RCRB. This capability contains no registers. This capability is present in the linked list (Next Capability Offset) but should otherwise be ignored by software.

A single PCI Express Function or RCRB is permitted to contain multiple Null Extended Capability structures.

§ Figure 7-385 details allocation of register fields in the Null Extended Capability; § Table 7-337 provides the respective bit definitions. The Extended Capability ID for the Null Extended Capability is 0000h.

> **Figure 7-385 (Register Layout).** Null Extended Capability
>
> | Bits 31:20 | Bits 19:16 | Bits 15:0 |
> |-----------|------------|-----------|
> | Next Capability Offset | Capability Version | PCI Express Extended Capability ID = 0000h |

**Table 7-337. Null Extended Capability**

| Bit Location | Register Description | Attributes |
|--------------|---------------------|------------|
| 15:0 | PCI Express Extended Capability ID - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability.<br>Extended Capability ID for the Null Extended Capability is 0000h. | RO |
| 19:16 | Capability Version - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present.<br>This field is permitted to contain any value. | RO |
| 31:20 | Next Capability Offset - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities.<br>For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

The Streamlined Virtual Channel (SVC) Extended Capability is an optional Extended Capability required for Ports that support capabilities associated with this structure, including UIO. It is permitted, but not required, for Functions in a Port to implement the SVC Extended Capability as well as the MFVC Extended Capability and/or VC Capabilities. See § Section 6.3.5 .

UIO requires the use of the SVC capability and is not supported by the VC or MFVC capabilities. UIO is supported only in Flit Mode, but in Non-Flit Mode the SVC capability can be used by non-UIO traffic.

For an Upstream Port, the SVC Extended Capability structure is permitted to be implemented only in Function 0, and that instance applies to all Functions associated with that Port. The SVC Extended Capability structure is permitted to be implemented in any Downstream Port, or in an RCRB. If the SVC Extended Capability structure is implemented in a USP

</td>
<td style="background-color:#e8e8e8">

Null Extended Capability(空扩展能力)是一种可选的扩展能力,允许由任何 PCI Express Function 或 RCRB 实现。该能力不包含任何寄存器。该能力出现在链表(Next Capability Offset)中,但软件应忽略其内容。

允许单个 PCI Express Function 或 RCRB 包含多个 Null Extended Capability 结构。

§ Figure 7-385 详述了 Null Extended Capability 中各寄存器字段的分配;§ Table 7-337 给出了相应的位定义。Null Extended Capability 的 Extended Capability ID 为 0000h。

> **图 7-385(寄存器布局)。** 空扩展能力
>
> | 位 31:20 | 位 19:16 | 位 15:0 |
> |----------|----------|---------|
> | Next Capability Offset(下一能力偏移) | Capability Version(能力版本) | PCI Express Extended Capability ID = 0000h |

**表 7-337. 空扩展能力 (Null Extended Capability)**

| 位位置 | 寄存器描述 | 属性 |
|--------|------------|------|
| 15:0 | PCI Express Extended Capability ID(PCI Express 扩展能力 ID)— 此字段是由 PCI-SIG 定义的 ID 编号,用于指示扩展能力的性质和格式。<br>Null Extended Capability 的 Extended Capability ID 为 0000h。 | RO |
| 19:16 | Capability Version(能力版本)— 此字段是由 PCI-SIG 定义的版本号,用于指示所呈现的能力结构的版本。<br>此字段允许包含任意值。 | RO |
| 31:20 | Next Capability Offset(下一能力偏移)— 此字段包含指向下一个 PCI Express Capability 结构的偏移,若链表中不存在其他项则为 000h。<br>对于在配置空间中实现的扩展能力,此偏移相对于 PCI 兼容配置空间的起始处,因此必须始终为 000h(用于终止能力列表)或大于 0FFh。 | RO |

Streamlined Virtual Channel(SVC,精简虚通道)Extended Capability 是一种可选的扩展能力,对于支持与此结构相关的能力(包括 UIO)的端口是必需的。允许(但不要求)端口中的功能同时实现 SVC Extended Capability 与 MFVC Extended Capability 和/或 VC Capabilities。参见 § Section 6.3.5 。

UIO 要求使用 SVC 能力,且 VC 或 MFVC 能力不支持 UIO。UIO 仅在 Flit Mode(Flit 模式)下受支持,但在 Non-Flit Mode(非 Flit 模式)下,SVC 能力可被非 UIO 流量使用。

对于 Upstream Port(上游端口),SVC Extended Capability 结构允许仅在 Function 0 中实现,且该实例适用于与该端口关联的所有功能。SVC Extended Capability 结构允许在任何 Downstream Port(下游端口)或 RCRB 中实现。如果 SVC Extended Capability 结构在 USP 中实现

</td>
</tr>
</tbody>
</table>

> **Figure 7-385.** Null Extended Capability
> <img src="figures/chapter_07/fig_1397_1_tight.png" width="700">

</div>


[⬆️ 返回目录](#-本章目录-table-of-contents)

---

---

7.9.29 Streamlined Virtual Channel Extended Capability (SVC) §
§
§

<!-- 📄 Page 1398 -->
---

<a id="sec-7-9-29"></a>
## 7.9.29 Streamlined Virtual Channel Extended Capability (SVC) | 精简虚通道扩展能力 (SVC)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

containing one or more Switch USP Functions, it must be implemented in all associated Switch DSP Functions. A Root Complex is permitted to implement the Extended Capability structure in some Root Ports and not others.

The number of (extended) Virtual Channels is indicated by the SVC Extended VC Count field in the SVC Port VC Capability Register 1. Software must interpret this field to determine the availability of extended SVC Resource registers.

</td>
<td style="background-color:#e8e8e8">

如果某个 交换机 (Switch) 包含一个或多个 USP (上游端口) Function,则其所有关联的 DSP (下游端口) Function 中都必须实现该扩展能力结构。根复合体 (Root Complex) 允许在某些 Root Port 上实现该扩展能力结构,而在其他 Root Port 上不实现。

(扩展的)虚通道 (Virtual Channel) 数量由 SVC Port VC Capability Register 1 中的 SVC Extended VC Count 字段指示。软件必须解释该字段以确定扩展 SVC Resource 寄存器的可用性。

</td>
</tr>
</tbody>
</table>

---

**Figure 7-386. Streamlined Virtual Channel Extended Capability Structure | 图 7-386. 精简虚通道扩展能力结构**

> 7-386 图展示了精简虚通道扩展能力 (Streamlined Virtual Channel Extended Capability) 结构的布局。

<a id="sec-7-9-29-1"></a>
## 7.9.29.1 Streamlined Virtual Channel Extended Capability Header (Offset 00h) | 精简虚通道扩展能力头 (偏移量 00h)

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-387 details allocation of register fields in the Streamlined Virtual Channel Extended Capability Header; Table 7-338 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-387 详细说明了精简虚通道扩展能力头 (Streamlined Virtual Channel Extended Capability Header) 中寄存器字段的分配;表 7-338 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

**Figure 7-387. Streamlined Virtual Channel Extended Capability Header | 图 7-387. 精简虚通道扩展能力头**

```
0                                                                              15
+--------------------------------------------------+
|     PCI Express Extended Capability ID          |   0035h
+--------------------------------------------------+
16            19                       20                                       31
+----------------+--------------------------------------------------+
|  Capability    |        Next Capability Offset                     |
|   Version      |                                                  |
+----------------+--------------------------------------------------+
```

**Table 7-338. Streamlined Virtual Channel Extended Capability Header | 表 7-338. 精简虚通道扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | **PCI Express Extended Capability ID** - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the Streamlined Virtual Channel Extended Capability is 0035h. | RO |
| 19:16 | **Capability Version** - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | **Next Capability Offset** - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. | RO |


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh.

The SVC Port Capability Register 1 describes the configuration of the Virtual Channels associated with a PCI Express Port.

Figure 7-388 details allocation of register fields in the SVC Port Capability Register 1; Table 7-339 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

对于在配置空间 (Configuration Space) 中实现的扩展能力,该偏移量相对于 PCI 兼容 (PCI-Compatible) 配置空间的起始地址,因此必须始终为 000h(用于终止能力链表)或大于 0FFh。

SVC Port Capability Register 1 描述与一个 PCI Express 端口 (Port) 关联的虚通道 (Virtual Channel) 的配置。

图 7-388 详细说明了 SVC Port Capability Register 1 中寄存器字段的分配;表 7-339 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>
</div>


---

<a id="sec-7-9-29-2"></a>
## 7.9.29.2 SVC Port Capability Register 1 (Offset 04h) | SVC 端口能力寄存器 1 (偏移量 04h)

**Figure 7-388. SVC Port Capability Register 1 | 图 7-388. SVC 端口能力寄存器 1**

```
0           2                  3                                                   31
+-----------+-------------------------------------------------------+
| SVC Ext.  |                                                       |
|  VC Count |                      RsvdP                           |
+-----------+-------------------------------------------------------+
```

**Table 7-339. SVC Port Capability Register 1 | 表 7-339. SVC 端口能力寄存器 1**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2:0 | **SVC Extended VC Count** – Indicates the number of Virtual Channels supported in addition to VC0. This value indicates the number of SVC Resource Capability, Control, and Status registers present in this structure in addition to those for VC0. The minimum value of this field is 0, for devices that only support the default VC. | HwInit |
| 31:3 | This register is RsvdP. | |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Table 7-340 details allocation of register fields in the SVC Port Control Register; Table 7-340 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

表 7-340 详细说明了 SVC Port Control Register 中寄存器字段的分配;表 7-340 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-29-3"></a>
## 7.9.29.3 SVC Port Capability Register 2 (Offset 08h) | SVC 端口能力寄存器 2 (偏移量 08h)

<a id="sec-7-9-29-4"></a>
## 7.9.29.4 SVC Port Control Register (Offset 0Ch) | SVC 端口控制寄存器 (偏移量 0Ch)

**Figure 7-389. SVC Port Control Register | 图 7-389. SVC 端口控制寄存器**

```
0                       1                                                         31
+------+--------------------------------------------------------------------------+
| VC   |                                                                          |
| Enab.|                            RsvdP                                        |
|Compl.|                                                                          |
+------+--------------------------------------------------------------------------+
```

**Table 7-340. SVC Port Control Register | 表 7-340. SVC 端口控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | **VC Enablement Completed** – Setting this bit indicates that software has completed enabling all VCs that are to be used by the Port. Setting this bit is optional. If this bit remains Clear, the Port and all enabled VCs must operate correctly. Default value of this bit is 0b. | RW |
| 31:1 | Reserved (RsvdP). | |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Table 7-341 details allocation of register fields in the SVC Port Status Register; Table 7-341 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

表 7-341 详细说明了 SVC Port Status Register 中寄存器字段的分配;表 7-341 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1400 -->
---

**Figure 7-390. SVC Port Status Register | 图 7-390. SVC 端口状态寄存器**

```
0                       1                                                         31
+--------+------------------------------------------------------------------------+
| Use VC/|                                                                        |
|  MFVC  |                            RsvdP                                      |
+--------+------------------------------------------------------------------------+
```

**Table 7-341. SVC Port Status Register | 表 7-341. SVC 端口状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 0 | **Use VC/MFVC** – This bit enables or disables multiple specific VCs in SVC, VC, and MFVC capabilities as required for Section 6.3.5. When this bit is Set, the VC Enable bit for VC0 in each VC/MFVC capability (VC Resource Control Register or MFVC VC Resource Control Register) must be Set, and the SVC VC Enable bit for each VC in its SVC Resource Control Register must be Clear. When this bit is Cleared, the VC Enable bit for each VC resource in each VC/MFVC capability (VC Resource Control Register or MFVC VC Resource Control Register) must immediately be Cleared, and the SVC VC Enable bit for VC0 in its SVC Resource Control Register must immediately be Set. If this Port implements any VC or MFVC capabilities, this bit must have a default value of 1b, and if Cleared, it must remain Clear until the next Conventional Reset. If this Port implements no VC or MFVC capabilities, this bit must be 0b. | RW1C/HwInit |

---

<a id="sec-7-9-29-5"></a>
## 7.9.29.5 SVC Port Status Register (Offset 10h) | SVC 端口状态寄存器 (偏移量 10h)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Encoded values for the SVC VC Protocols Supported field:

- **0000b**: Supports same TLP Types and protocols as VC0
- **0001b**: Supports same TLP Types and protocols as VC0, except for those that are restricted by this document to using only VC0
- **0010b**: It is permitted to enable UIO on this VC resource; it is not permitted to use non-UIO TLP Types on this VC resource.
- **0011b**: It is permitted to enable UIO on this VC resource, or to use as a 0001b VC resource, but not both at the same time.
- **0100b to 1110b**: Reserved
- **1111b**: Vendor-defined use (outside the scope of this specification)

Figure 7-391 details allocation of register fields in the SVC Resource Capability Register; Table 7-342 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

SVC VC Protocols Supported 字段的编码值:

- **0000b**: 支持与 VC0 相同的 TLP 类型和协议
- **0001b**: 支持与 VC0 相同的 TLP 类型和协议,例外是本规范限制只能使用 VC0 的那些类型
- **0010b**: 允许在该 VC 资源上启用 UIO;不允许在该 VC 资源上使用非 UIO TLP 类型。
- **0011b**: 允许在该 VC 资源上启用 UIO,或作为 0001b VC 资源使用,但不能同时使用两者。
- **0100b 至 1110b**: 保留
- **1111b**: 厂商自定义使用(超出本规范范围)

图 7-391 详细说明了 SVC Resource Capability Register 中寄存器字段的分配;表 7-342 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>
</div>


---

<!-- 📄 Page 1401 -->
---

<a id="sec-7-9-29-6"></a>
## 7.9.29.6 SVC Resource Capability Register | SVC 资源能力寄存器

**Figure 7-391. SVC Resource Capability Register | 图 7-391. SVC 资源能力寄存器**

```
0                       7        8                  11    12         14    15                                 31
+-----------------------+--------+-----------------------+-------------+-------------------------------------+
|       RsvdP           |        | SVC VC Protocols      |  SVC VC ID  |              RsvdP                  |
+-----------------------+--------+-----------------------+-------------+-------------------------------------+
```

**Table 7-342. SVC Resource Capability Register | 表 7-342. SVC 资源能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 11:8 | **SVC VC Protocols Supported** – Indicates UIO and non-UIO Transaction support for this VC, encoded as: <br>• 0000b - Supports same TLP Types and protocols as VC0 <br>• 0001b - Supports same TLP Types and protocols as VC0, except for those that are restricted by this document to using only VC0 <br>• 0010b - It is permitted to enable UIO on this VC resource; it is not permitted to use non-UIO TLP Types on this VC resource. <br>• 0011b - It is permitted to enable UIO on this VC resource, or to use as a 0001b VC resource, but not both at the same time. <br>• 0100b to 1110b - Reserved <br>• 1111b - Vendor-defined use (outside the scope of this specification) <br>For VC0, must be 0000b. For VC3, if UIO is supported, must be 0010b or 0011b. For VC4, if UIO and VC4 are supported, must be 0010b or 0011b. | HwInit/RsvdP |
| 14:12 | **SVC VC ID** – This field indicates the VC ID to the VC resource. For the first of SVC Resource Capability Register, this field must be 000b. For other SVC Resource Capability Registers, this field may contain any non-zero value. This field value must be unique across all SVC Resource Capability Registers. | HwInit/RsvdP |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-392 details allocation of register fields in the SVC Resource Control Register; Table 7-343 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-392 详细说明了 SVC Resource Control Register 中寄存器字段的分配;表 7-343 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-29-7"></a>
## 7.9.29.7 SVC Resource Control Register | SVC 资源控制寄存器

**Figure 7-392. SVC Resource Control Register | 图 7-392. SVC 资源控制寄存器**

```
0                       7        8                  11    12                            26    27       29    30         31
+-----------------------+--------+-----------------------+--------------------------------+---+----------+--------+----------+
|    SVC TC/VC Map      |        | SVC VC Protocol       |              RsvdP              |   |SVC Shared| SVC Sh.|  SVC VC  |
|                       |        |     Selected          |                                |   | FC Usage |  FC Us.|  Enable  |
|                       |        |                       |                                |   |  Limit   | Lim En.|          |
+-----------------------+--------+-----------------------+--------------------------------+---+----------+--------+----------+
```

**Table 7-343. SVC Resource Control Register | 表 7-343. SVC 资源控制寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 7:0 | **SVC TC/VC Map** – This field indicates the TCs that are mapped to the VC resource. This field is valid for all Functions. Bit locations within this field correspond to TC values. In order to remove one or more TCs from the TC/VC Map of an enabled VC, software must ensure that no new or outstanding Requests with the TC labels are targeted at the given Link. Bit 0 of this field must be read-only. It must be Set for the default VC0 and Clear for all other enabled VCs. Default value of this field must be consistent with Table 2-46. | RW / RO |
| 11:8 | **SVC VC Protocol Selected** – Determines the TLP Types and Protocols to be used with this VC, encoded as: <br>• 0000b - TLP Types and protocols as VC0 (required for VC0 and permitted only for VC0) <br>• 0001b - TLP Types and protocols as VC0, except for those that are restricted by this document to using only VC0 <br>• 0010b - UIO TLP Types and protocols <br>• 0011b to 1110b - Reserved <br>• 1111b - Vendor-defined use (outside the scope of this specification) <br>For VC0, must be hardwired to 0000b. Default value is implementation specific. | RW / RO / RsvdP |
| 29:27 | **SVC Shared Flow Control Usage Limit** – This field controls what percentage of the available Shared Flow Control a given FC/VC is permitted to consume. This limit is applied independently for each Flow Control credit type. For example, if this field contains 101b and SVC Shared Flow Control Usage Limit Enable is Set, a Posted TLP may not pass the Tx Gate if doing so would cause that VC to consume more than 62.5% of the available Shared Posted Header credits or if doing so would cause that VC to consume more than 62.5% of the available Shared Data credits. If SVC Shared Flow Control Usage Limit Enable is Clear, this field must be ignored, and this VC is permitted to consume all of the shared credits, unless the Transmitter has implementation-specific policy mechanisms to constrain shared credit use. When SVC Shared Flow Control Usage Limit Enable is Set, and this field contains 000b, this VC is not permitted to consume any shared credits. Behavior is undefined when all VCs have SVC Shared Flow Control Usage Limit Enable Set and the sum of the SVC Shared Flow Control Limit values for all VCs is less than 100%. Encodings are: <br>• 000b - 0% <br>• 001b - 12.5% <br>• 010b - 25% <br>• 011b - 37.5% <br>• 100b - 50% <br>• 101b - 62.5% <br>• 110b - 75% <br>• 111b - 87.5% <br>Behavior is undefined if this field changes value while SVC VC Enable and SVC Shared Flow Control Usage Limit Enable are both Set. When SVC Extended VC Count is 0, this field is permitted to be hardwired to any value. When this field is RW, the default value is implementation specific. | RW / RO / RsvdP |
| 30 | **SVC Shared Flow Control Usage Limit Enable** – When Set, this bit enables use of control of Shared Flow Control consumption at the transmitter for this Virtual Channel. Behavior is undefined of the value of this bit changes while SVC VC Enable is Set. This bit is RsvdP when Flit Mode Supported is Clear. When SVC Extended VC Count is 0, this bit is permitted to be hardwired to 0b. When this bit is RW, the default value is implementation specific. | RW / RO / RsvdP |
| 31 | **SVC VC Enable** – This bit, when Set, enables this Virtual Channel. The Virtual Channel is disabled when this bit is cleared. Software must use the SVC VC Negotiation Pending bit to check whether the VC negotiation is complete. For VC0, the attribute is RO, and this bit must always have the opposite value from the Use VC/MFVC bit in the SVC Port Status Register. See Section 6.3.5. For other VCs, the default value of this bit is 0b and the attribute is RW. To enable a Virtual Channel in a Port using SVC mechanisms, the SVC VC Enable bit for that Virtual Channel must be Set. The corresponding Virtual Channel in the Link partner Port must be enabled as well, and that Virtual Channel may be in an SVC, VC, or MFVC capability. To disable a Virtual Channel, the Virtual Channel must be disabled in both components on the Link. Software must ensure that no traffic is using a Virtual Channel at the time it is disabled. Software must fully disable a Virtual Channel in both components on a Link before re-enabling the Virtual Channel. | RW / RO |

---

<!-- 📄 Page 1402 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Table 7-344 details allocation of register fields in the VC Resource Status Register; Table 7-344 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

表 7-344 详细说明了 SVC Resource Status Register 中寄存器字段的分配;表 7-344 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1403 -->
---

<a id="sec-7-9-29-8"></a>
## 7.9.29.8 SVC Resource Status Register | SVC 资源状态寄存器

**Figure 7-393. SVC Resource Status Register | 图 7-393. SVC 资源状态寄存器**

```
0                       1                                                         31
+-----------------------+----------------------------------------------------------+
|       RsvdP           |        SVC VC Negotiation Pending          |    RsvdP   |
+-----------------------+----------------------------------------------------------+
```

<!-- 📄 Page 1404 -->
---

**Table 7-344. SVC Resource Status Register | 表 7-344. SVC 资源状态寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 1 | **SVC VC Negotiation Pending** – This bit indicates whether the Virtual Channel negotiation (initialization or disabling) is in pending state. This bit is valid for all Functions. The value of this bit is defined only when the Link is in the DL_Active state and the corresponding SVC VC Enable bit is Set. This bit is Set by hardware to indicate that the VC resource has not completed the process of negotiation. This bit is Cleared by hardware after the VC negotiation is complete (on exit from the FC_INIT2 state). For VC0, this bit is permitted to be hardwired to 0b. Before using a Virtual Channel, software must check whether the SVC VC Negotiation Pending bits for that Virtual Channel are Clear in both components on the Link. | RO |

---

<a id="sec-7-9-30"></a>
## 7.9.30 MMIO Register Block Locator Extended Capability (MRBL) | MMIO 寄存器块定位器扩展能力 (MRBL)


<div style="overflow-x: auto; max-width: 100%;">
<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

The MMIO Register Block Locator Extended Capability (MRBL) is an optional Extended Capability for discovering register blocks in Memory Space that can be used to exchange various types of data structures between system software and a Function (See Section 6.35 Section 6.35).

It is permitted to implement the MRBL Extended Capability in any type of Function. A single PCI Express Function is permitted to contain at most one instance of this capability.

The number of register blocks included the MRBL structure is described in the MRBL Capabilities Register (Section 7.9.30.2 Section 7.9.30.2). A Function that implements the MRBL Extended Capability shall support at least one MRBL Locator Register (Section 7.9.30.3).

Each register block is described by a MRBL Locator Register (Section 7.9.30.3) to specify the location and type of the registers within Memory Space. Each register block must be contained within the address range covered by the associated BAR. Figure 7-394 illustrates the MRBL Extended Capability structure.

</td>
<td style="background-color:#e8e8e8">

MMIO 寄存器块定位器扩展能力 (MMIO Register Block Locator Extended Capability, MRBL) 是一项可选的扩展能力,用于发现内存空间 (Memory Space) 中的寄存器块,这些寄存器块可用于在系统软件和 Function 之间交换各种类型的数据结构(参见第 6.35 节 第 6.35 节)。

允许在任何类型的 Function 中实现 MRBL 扩展能力。单个 PCI Express Function 允许包含至多一个该能力的实例。

MRBL 结构中包含的寄存器块数量在 MRBL Capabilities Register 中描述(第 7.9.30.2 节 第 7.9.30.2 节)。实现 MRBL 扩展能力的 Function 应至少支持一个 MRBL Locator Register(第 7.9.30.3 节)。

每个寄存器块由一个 MRBL Locator Register(第 7.9.30.3 节)描述,以指定内存空间中寄存器的位置和类型。每个寄存器块必须包含在关联的 BAR (基址寄存器, Base Address Register) 所覆盖的地址范围内。图 7-394 说明了 MRBL 扩展能力结构。

</td>
</tr>
</tbody>
</table>
</div>


---

**Figure 7-394. MRBL Extended Capability | 图 7-394. MRBL 扩展能力**

```
Byte Offset       Contents
+--------+
+000h    |  PCI Express Extended Capability Header
+004h    |  MRBL Capabilities Register
+008h    |  MRBL Locator Register (Register Block 1)
+00Ch    |  MRBL Locator Register (Register Block 2)
+010h    |  ...
+014h
+018h
+--------+
```

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-395 details allocation of register fields in the MRBL Extended Capability Header; Table 7-345 provides the respective bit definitions. Refer to Section 7.6.3 for a description of the PCI Express Extended Capability Header. The Extended Capability ID for the MRBL Extended Capability is 0036h.

</td>
<td style="background-color:#e8e8e8">

图 7-395 详细说明了 MRBL Extended Capability Header 中寄存器字段的分配;表 7-345 给出了相应的位定义。有关 PCI Express 扩展能力头的描述,请参见第 7.6.3 节。MRBL 扩展能力的扩展能力 ID 为 0036h。

</td>
</tr>
</tbody>
</table>

---

<!-- 📄 Page 1405 -->
---

<a id="sec-7-9-30-1"></a>
## 7.9.30.1 MRBL Extended Capability Header (Offset 00h) | MRBL 扩展能力头 (偏移量 00h)

**Figure 7-395. MRBL Extended Capability Header | 图 7-395. MRBL 扩展能力头**

```
0                                                                              15
+--------------------------------------------------+
|     PCI Express Extended Capability ID          |   0036h
+--------------------------------------------------+
16            19                       20                                       31
+----------------+--------------------------------------------------+
|  Capability    |        Next Capability Offset                     |
|   Version      |                                                  |
+----------------+--------------------------------------------------+
```

**Table 7-345. MRBL Extended Capability Header | 表 7-345. MRBL 扩展能力头**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 15:0 | **PCI Express Extended Capability ID** - This field is a PCI-SIG defined ID number that indicates the nature and format of the Extended Capability. Extended Capability ID for the MMIO Register Block Locator Extended Capability is 0036h. | RO |
| 19:16 | **Capability Version** - This field is a PCI-SIG defined version number that indicates the version of the Capability structure present. Must be 1h for this version of the specification. | RO |
| 31:20 | **Next Capability Offset** - This field contains the offset to the next PCI Express Capability structure or 000h if no other items exist in the linked list of Capabilities. For Extended Capabilities implemented in Configuration Space, this offset is relative to the beginning of PCI-compatible Configuration Space and thus must always be either 000h (for terminating list of Capabilities) or greater than 0FFh. | RO |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-396 details allocation of register fields in the MRBL Capabilities Register; Table 7-346 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-396 详细说明了 MRBL Capabilities Register 中寄存器字段的分配;表 7-346 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-30-2"></a>
## 7.9.30.2 MRBL Capabilities Register (Offset 04h) | MRBL 能力寄存器 (偏移量 04h)

**Figure 7-396. MRBL Capabilities Register | 图 7-396. MRBL 能力寄存器**

```
0                                                                              11                                    31
+--------------------------------------------------------------------------------------------------------+
|                              MRBL Structure Length                                                     |
+--------------------------------------------------------------------------------------------------------+
```

<!-- 📄 Page 1406 -->
---

**Table 7-346. MRBL Capabilities Register | 表 7-346. MRBL 能力寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 11:0 | **MRBL Structure Length** – This field indicates the overall size of the MRBL Extended Capability in bytes: 08h + (n*08h) where n is the number of MRBL Locator Registers implemented. | HWInit |

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Figure 7-397 details allocation of register fields in the MRBL Locator Register; Table 7-347 provides the respective bit definitions.

</td>
<td style="background-color:#e8e8e8">

图 7-397 详细说明了 MRBL Locator Register 中寄存器字段的分配;表 7-347 给出了相应的位定义。

</td>
</tr>
</tbody>
</table>

---

<a id="sec-7-9-30-3"></a>
## 7.9.30.3 MRBL Locator Register (Offset Varies) | MRBL 定位寄存器 (偏移量可变)

**Figure 7-397. MRBL Locator Register | 图 7-397. MRBL 定位寄存器**

```
0                       2                  3        7        8                          15    16                              31
+-----------------------+-----------------------+--------+-----------------------------+---------------------------------------+
|    Register BIR       |        RsvdP          |                Register Block ID      |     Register Block Offset Low         |
+-----------------------+-----------------------+--------+-----------------------------+---------------------------------------+
32                                                                                      63
+--------------------------------------------------------------------------------------+
|                            Register Block Offset High                                |
+--------------------------------------------------------------------------------------+
```

**Table 7-347. MRBL Locator Register | 表 7-347. MRBL 定位寄存器**

| Bit Location | Register Description | Attributes |
|--------------|----------------------|------------|
| 2:0 | **Register BIR** – Indicates which one of a Function's Base Address Registers, or entry in the Enhanced Allocation capability with a matching BAR Equivalent Indicator (BEI), is used for this register block. Defined encodings are: <br>• 00h - Base Address Register 10h <br>• 01h - Base Address Register 14h <br>• 02h - Base Address Register 18h <br>• 03h - Base Address Register 1Ch <br>• 04h - Base Address Register 20h <br>• 05h - Base Address Register 24h <br>• 06h - Reserved <br>• 07h - Reserved <br>For a 64-bit Base Address Register, the Register BIR indicates the lower DWORD. For Functions with Type 1 Configuration Space headers, BIR values 2 through 5 are Reserved. | HWInit |
| 15:8 | **Register Block ID** – Identifies the type of registers contained in this register block. Defined encodings are: <br>• 00h - Empty/invalid register block <br>• 01h - MMIO Capabilities Register Block (MCAP) (Section 6.35.1) <br>• 02h-FEh - Reserved <br>• FFh - MMIO Designated Vendor-Specific Register Block (MDVS) (Section 6.35.2) | HWInit |
| 31:16 | **Register Block Offset Low** – Contains bits [31:16] of the register block address offset within the BAR/BEI indicated by Register BIR. Offset bits [15:0] are 0000h. The value in this field must be ignored if Register Block ID is 00h. | HWInit |
| 63:32 | **Register Block Offset High** – Contains bits [63:32] of the register block address offset within the BAR/BEI indicated by Register BIR. The value in this field must be ignored if Register Block ID is 00h. | HWInit |

---

<!-- 📄 Page 1407 -->
---

<table>
<thead>
<tr>
<th width="50%">🇬🇧 English</th>
<th width="50%" style="background-color:#e8e8e8">🏆 中文</th>
</tr>
</thead>
<tbody>
<tr>
<td>

(Continued from MRBL Locator Register description – Register Block Offset High field detail.)

</td>
<td style="background-color:#e8e8e8">

(接 MRBL 定位寄存器描述 – Register Block Offset High 字段细节。)

</td>
</tr>
</tbody>
</table>


---

<!-- 📄 Page 1408 -->
---

---

## 📑 本章目录 (Table of Contents) — Auto-Generated

- [7. Software Initialization and Configuration § | 7. 软件初始化与配置 §](#sec-7)
- [7.1 Configuration Topology § | 7.1 配置拓扑 §](#sec-7-1)
- [7.2 PCI Express Configuration Mechanisms § | 7.2 PCI Express 配置机制 §](#sec-7-2)
- [7.2.1 PCI-compatible Configuration Mechanism § | 7.2.1 PCI 兼容配置机制 §](#sec-7-2-1)
- [7.2.2 PCI Express Enhanced Configuration Access Mechanism (ECAM) § | 7.2.2 PCI Express 增强配置访问机制 (ECAM) §](#sec-7-2-2)
- [7.2.2.1 Host Bridge Requirements § | 7.2.2.1 主桥 (Host Bridge) 要求 §](#sec-7-2-2-1)
- [7.2.2.2 PCI Express Device Requirements § | 7.2.2.2 PCI Express 设备要求 §](#sec-7-2-2-2)
- [7.2.3 Root Complex Register Block (RCRB) § | 7.2.3 根复合体寄存器块 (RCRB) §](#sec-7-2-3)
- [7.3 Configuration Transaction Rules § | 7.3 配置事务规则 §](#sec-7-3)
- [7.3.1 Device Number § | 7.3.1 设备号 (Device Number) §](#sec-7-3-1)
- [7.3.2 Configuration Transaction Addressing | 配置事务寻址](#sec-7-3-2)
- [7.3.3 Configuration Request Routing Rules | 配置请求路由规则](#sec-7-3-3)
- [7.3.4 PCI Special Cycles | PCI 特殊周期](#sec-7-3-4)
- [7.4 Configuration Register Types | 配置寄存器类型](#sec-7-4)
- [7.5 PCI and PCIe Capabilities Required by the Base Spec for all Ports | 基础规范要求所有端口支持的 PCI 和 PCIe 能力](#sec-7-5)
- [7.5.1 PCI-Compatible Configuration Registers | PCI 兼容配置寄存器](#sec-7-5-1)
- [7.5.1.1 Type 0/1 Common Configuration Space | Type 0/1 公共配置空间](#sec-7-5-1-1)
- [7.5.1.1.1 Vendor ID Register (Offset 00h) | Vendor ID 寄存器（偏移 00h）](#sec-7-5-1-1-1)
- [7.5.1.1.2 Device ID Register (Offset 02h) | Device ID 寄存器（偏移 02h）](#sec-7-5-1-1-2)
- [7.5.1.1.3 Command Register (Offset 04h) | Command 寄存器（偏移 04h）](#sec-7-5-1-1-3)
- [7.5.1.1.4 Status Register (Offset 06h) | Status 寄存器（偏移 06h）](#sec-7-5-1-1-4)
- [7.5.1.1.4 Status Register (Offset 06h) | 状态寄存器（偏移量 06h）](#sec-7-5-1-1-4)
- [7.5.1.1.5 Revision ID Register (Offset 08h) | 修订版本 ID 寄存器（偏移量 08h）](#sec-7-5-1-1-5)
- [7.5.1.1.6 Class Code Register (Offset 09h) | 类别代码寄存器（偏移量 09h）](#sec-7-5-1-1-6)
- [7.5.1.1.7 Cache Line Size Register (Offset 0Ch) | Cache 行大小寄存器（偏移量 0Ch）](#sec-7-5-1-1-7)
- [7.5.1.1.8 Latency Timer Register (Offset 0Dh) | 延迟定时器寄存器（偏移量 0Dh）](#sec-7-5-1-1-8)
- [7.5.1.1.9 Header Type Register (Offset 0Eh) | 头类型寄存器（偏移量 0Eh）](#sec-7-5-1-1-9)
- [7.5.1.1.10 BIST Register (Offset 0Fh) | BIST 寄存器（偏移量 0Fh）](#sec-7-5-1-1-10)
- [7.5.1.1.11 Capabilities Pointer (Offset 34h) | 能力指针（偏移量 34h）](#sec-7-5-1-1-11)
- [7.5.1.1.12 Interrupt Line Register (Offset 3Ch) | 中断线寄存器（偏移量 3Ch）](#sec-7-5-1-1-12)
- [7.5.1.1.13 Interrupt Pin Register (Offset 3Dh) | 中断引脚寄存器（偏移量 3Dh）](#sec-7-5-1-1-13)
- [7.5.1.1.14 Error Control/Status Register Summary | 错误控制/状态寄存器总结](#sec-7-5-1-1-14)
- [7.5.1.1.14 Error Registers | 错误寄存器](#sec-7-5-1-1-14)
- [7.5.1.2 Type 0 Configuration Space Header | Type 0 配置空间头](#sec-7-5-1-2)
- [7.5.1.2.1 Base Address Registers (Offset 10h - 24h) | 基址寄存器 (BAR) (偏移 10h - 24h)](#sec-7-5-1-2-1)
- [7.5.1.2.2 Cardbus CIS Pointer Register (Offset 28h) | Cardbus CIS 指针寄存器 (偏移 28h)](#sec-7-5-1-2-2)
- [7.5.1.2.3 Subsystem Vendor ID Register/Subsystem ID Register (Offset 2Ch/2Eh) | 子系统供应商 ID 寄存器/子系统 ID 寄存器 (偏移 2Ch/2Eh)](#sec-7-5-1-2-3)
- [7.5.1.2.4 Expansion ROM Base Address Register (Offset 30h) | 扩展 ROM 基址寄存器 (偏移 30h)](#sec-7-5-1-2-4)
- [7.5.1.2.5 Min_Gnt Register/Max_Lat Register (Offset 3Eh/3Fh) | Min_Gnt 寄存器/Max_Lat 寄存器 (偏移 3Eh/3Fh)](#sec-7-5-1-2-5)
- [7.5.1.3 Type 1 Configuration Space Header | Type 1 配置空间头](#sec-7-5-1-3)
- [7.5.1.3.1 Type 1 Base Address Registers (Offset 10h-14h) | Type 1 基址寄存器 (偏移 10h-14h)](#sec-7-5-1-3-1)
- [7.5.1.3.7 Secondary Status Register (Offset 1Eh) | Secondary Status 寄存器 (偏移 1Eh)](#sec-7-5-1-3-7)
- [7.5.1.3.8 Memory Base Register/Memory Limit Register (Offset 20h/22h) | Memory Base 寄存器 / Memory Limit 寄存器 (偏移 20h/22h)](#sec-7-5-1-3-8)
- [7.5.1.3.10 Prefetchable Base Upper 32 Bits/Prefetchable Limit Upper 32 Bits Registers (Offset 28h/2Ch) | Prefetchable Base Upper 32 Bits / Prefetchable Limit Upper 32 Bits 寄存器 (偏移 28h/2Ch)](#sec-7-5-1-3-10)
- [7.5.1.3.11 I/O Base Upper 16 Bits/I/O Limit Upper 16 Bits Registers (Offset 30h/32h) | I/O Base Upper 16 Bits / I/O Limit Upper 16 Bits 寄存器 (偏移 30h/32h)](#sec-7-5-1-3-11)
- [7.5.1.3.12 Expansion ROM Base Address Register (Offset 38h) | Expansion ROM 基址寄存器 (偏移 38h)](#sec-7-5-1-3-12)
- [7.5.1.3.13 Bridge Control Register (Offset 3Eh) | Bridge Control 寄存器 (偏移 3Eh)](#sec-7-5-1-3-13)
- [7.5.1.4 PCI Power Management Capability Structure | PCI 电源管理能力结构](#sec-7-5-1-4)
- [7.5.2 PCI Power Management Capability Structure | PCI 电源管理能力结构](#sec-7-5-2)
- [7.5.2.1 Power Management Capabilities Register (Offset 00h) | 电源管理能力寄存器（偏移量 00h）](#sec-7-5-2-1)
- [7.5.2.2 Power Management Control/Status Register (Offset 04h) | 电源管理控制/状态寄存器（偏移量 04h）](#sec-7-5-2-2)
- [7.5.2.3 Power Management Data Register (Offset 07h) | 电源管理数据寄存器（偏移量 07h）](#sec-7-5-2-3)
- [7.5.3 PCI Express Capability Structure | PCI Express 能力结构](#sec-7-5-3)
- [7.5.3.1 PCI Express Capability List Register (Offset 00h) | PCI Express 能力列表寄存器（偏移量 00h）](#sec-7-5-3-1)
- [7.5.3.2 PCI Express Capabilities Register (Offset 02h) | PCI Express 能力寄存器（偏移量 02h）](#sec-7-5-3-2)
- [7.5.3.3 Device Capabilities Register (Offset 04h) | 设备能力寄存器 (Device Capabilities Register) (偏移量 04h)](#sec-7-5-3-3)
- [7.5.3.4 Device Control Register (Offset 08h) | 设备控制寄存器 (Device Control Register) (偏移量 08h)](#sec-7-5-3-4)
- [7.5.3.5 Device Status Register (Offset 0Ah) | 设备状态寄存器 (Device Status Register) (偏移量 0Ah)](#sec-7-5-3-5)
- [7.5.3.6 Link Capabilities Register (Offset 0Ch) | 链路能力寄存器 (Link Capabilities Register) (偏移量 0Ch)](#sec-7-5-3-6)
- [7.5.3.7 Link Control Register (Offset 10h) | 链路控制寄存器（偏移 10h）](#sec-7-5-3-7)
- [7.5.3.8 Link Status Register (Offset 12h) | 链路状态寄存器（偏移 12h）](#sec-7-5-3-8)
- [7.5.3.9 Slot Capabilities Register (Offset 14h) | 插槽能力寄存器（偏移 14h）](#sec-7-5-3-9)
- [7.5.3.10 Slot Control Register | 插槽控制寄存器 (Offset 18h)](#sec-7-5-3-10)
- [7.5.3.11 Slot Status Register | 插槽状态寄存器 (Offset 1Ah)](#sec-7-5-3-11)
- [7.5.3.12 Root Control Register | 根复合体控制寄存器 (Offset 1Ch)](#sec-7-5-3-12)
- [7.5.3.13 Root Capabilities Register | 根复合体能力寄存器 (Offset 1Eh)](#sec-7-5-3-13)
- [7.5.3.14 Root Status Register | 根复合体状态寄存器 (Offset 20h)](#sec-7-5-3-14)
- [7.5.3.15 Device Capabilities 2 Register | 设备能力 2 寄存器 (Offset 24h)](#sec-7-5-3-15)
- [7.5.3.16 Device Control 2 Register (Offset 28h) | Device Control 2 寄存器(偏移 28h)](#sec-7-5-3-16)
- [7.5.3.17 Device Status 2 Register (Offset 2Ah) | Device Status 2 寄存器(偏移 2Ah)](#sec-7-5-3-17)
- [7.5.3.18 Link Capabilities 2 Register (Offset 2Ch) | Link Capabilities 2 寄存器(偏移 2Ch)](#sec-7-5-3-18)
- [7.5.3.19 Link Control 2 Register (Offset 30h) | Link Control 2 寄存器(偏移 30h)](#sec-7-5-3-19)
- [7.5.3.20 Link Status 2 Register (Offset 32h) | Link Status 2 寄存器(偏移 32h)](#sec-7-5-3-20)
- [7.5.3.21 Slot Capabilities 2 Register (Offset 34h) | Slot Capabilities 2 寄存器 (偏移 34h)](#sec-7-5-3-21)
- [7.6 PCI Express Extended Capabilities | PCI Express 扩展能力](#sec-7-6)
- [7.6.1 Extended Capabilities in Configuration Space | 配置空间中的扩展能力](#sec-7-6-1)
- [7.6.2 Extended Capabilities in the Root Complex Register Block | 根复合体寄存器块中的扩展能力](#sec-7-6-2)
- [7.6.3 PCI Express Extended Capability Header | PCI Express 扩展能力头](#sec-7-6-3)
- [7.7 PCI and PCIe Capabilities Required by the Base Spec in Some Situations | 基础规范在某些情况下要求的 PCI 和 PCIe 能力](#sec-7-7)
- [7.7.1 MSI Capability Structures | MSI 能力结构](#sec-7-7-1)
- [7.7.1.1 MSI Capability Header (Offset 00h) | MSI 能力头 (偏移 00h)](#sec-7-7-1-1)
- [7.7.1.2 Message Control Register for MSI (Offset 02h) | MSI 的消息控制寄存器 (偏移 02h)](#sec-7-7-1-2)
- [7.7.1.3 Message Address Register for MSI (Offset 04h) | MSI 的消息地址寄存器 (偏移 04h)](#sec-7-7-1-3)
- [7.7.1.4 Message Upper Address Register for MSI (Offset 08h) | MSI 的消息高地址寄存器 (偏移 08h)](#sec-7-7-1-4)
- [7.7.1.5 Message Data Register for MSI (Offset 08h or 0Ch) | MSI 的消息数据寄存器 (偏移 08h 或 0Ch)](#sec-7-7-1-5)
- [7.7.1.6 Extended Message Data Register for MSI (Optional) | MSI 扩展消息数据寄存器(可选)](#sec-7-7-1-6)
- [7.7.1.7 Mask Bits Register for MSI (Offset 0Ch or 10h) | MSI Mask Bits 寄存器(偏移 0Ch 或 10h)](#sec-7-7-1-7)
- [7.7.1.8 Pending Bits Register for MSI (Offset 10h or 14h) | MSI Pending Bits 寄存器(偏移 10h 或 14h)](#sec-7-7-1-8)
- [7.7.2 MSI-X Capability and Table Structure | MSI-X 能力结构与表结构](#sec-7-7-2)
- [7.7.2.1 MSI-X Capability Header (Offset 00h) | MSI-X Capability Header(偏移 00h)](#sec-7-7-2-1)
- [7.7.2.2 Message Control Register for MSI-X (Offset 02h) | MSI-X Message Control 寄存器(偏移 02h)](#sec-7-7-2-2)
- [7.7.2.3 Table Offset/Table BIR Register for MSI-X (Offset 04h) | MSI-X Table Offset/Table BIR 寄存器(偏移 04h)](#sec-7-7-2-3)
- [7.7.2.4 PBA Offset/PBA BIR Register for MSI-X (Offset 08h) | MSI-X PBA Offset/PBA BIR 寄存器(偏移 08h)](#sec-7-7-2-4)
- [7.7.2.5 Message Address Register for MSI-X Table Entries | MSI-X Table 条目 Message Address 寄存器](#sec-7-7-2-5)
- [7.7.2.6 Message Upper Address Register for MSI-X Table Entries | MSI-X Table 条目 Message Upper Address 寄存器](#sec-7-7-2-6)
- [7.7.2.7 Message Data Register for MSI-X Table Entries | MSI-X 表条目的消息数据寄存器](#sec-7-7-2-7)
- [7.7.2.8 Vector Control Register for MSI-X Table Entries | MSI-X 表条目的向量控制寄存器](#sec-7-7-2-8)
- [7.7.2.9 Pending Bits Register for MSI-X PBA Entries | MSI-X PBA 条目的挂起位寄存器](#sec-7-7-2-9)
- [7.7.3 Secondary PCI Express Extended Capability | 次级 PCI Express 扩展能力](#sec-7-7-3)
- [7.7.3.1 Secondary PCI Express Extended Capability Header (Offset 00h) | 次级 PCI Express 扩展能力头（偏移 00h）](#sec-7-7-3-1)
- [7.7.3.2 Link Control 3 Register (Offset 04h) | 链路控制 3 寄存器（偏移 04h）](#sec-7-7-3-2)
- [7.7.3.3 Lane Error Status Register (Offset 08h) | 通道错误状态寄存器（偏移 08h）](#sec-7-7-3-3)
- [7.7.3.4 Lane Equalization Control Register (Offset 0Ch) | 通道均衡控制寄存器（偏移 0Ch）](#sec-7-7-3-4)
- [7.7.4 Data Link Feature Extended Capability | 数据链路特性扩展能力](#sec-7-7-4)
- [7.7.4.1 Data Link Feature Extended Capability Header (Offset 00h) | 数据链路特性扩展能力头（偏移 00h）](#sec-7-7-4-1)
- [7.7.4.2 Data Link Feature Capabilities Register (Offset 04h) | 数据链路特性能力寄存器（偏移 04h）](#sec-7-7-4-2)
- [7.7.4.3 Data Link Feature Status Register (Offset 08h) | 数据链路特性状态寄存器(偏移量 08h)](#sec-7-7-4-3)
- [7.7.5 Physical Layer 16.0 GT/s Extended Capability | 物理层 16.0 GT/s 扩展能力结构](#sec-7-7-5)
- [7.7.5.1 Physical Layer 16.0 GT/s Extended Capability Header (Offset 00h) | 物理层 16.0 GT/s 扩展能力结构头(偏移量 00h)](#sec-7-7-5-1)
- [7.7.5.2 16.0 GT/s Capabilities Register (Offset 04h) | 16.0 GT/s 能力寄存器(偏移量 04h)](#sec-7-7-5-2)
- [7.7.5.3 16.0 GT/s Control Register (Offset 08h) | 16.0 GT/s 控制寄存器(偏移量 08h)](#sec-7-7-5-3)
- [7.7.5.4 16.0 GT/s Status Register (Offset 0Ch) | 16.0 GT/s 状态寄存器(偏移量 0Ch)](#sec-7-7-5-4)
- [7.7.5.5 16.0 GT/s Local Data Parity Mismatch Status Register (Offset 10h) | 16.0 GT/s 本地数据奇偶校验不匹配状态寄存器(偏移量 10h)](#sec-7-7-5-5)
- [7.7.5.6 16.0 GT/s First Retimer Data Parity Mismatch Status Register (Offset 14h) | 16.0 GT/s 第一个重定时器数据奇偶校验不匹配状态寄存器(偏移量 14h)](#sec-7-7-5-6)
- [7.7.5.7 16.0 GT/s Second Retimer Data Parity Mismatch Status Register (Offset 18h) | 16.0 GT/s 第二个重定时器数据奇偶校验不匹配状态寄存器(偏移量 18h)](#sec-7-7-5-7)
- [7.7.5.8 Physical Layer 16.0 GT/s Reserved (Offset 1Ch) | 物理层 16.0 GT/s 保留(偏移量 1Ch)](#sec-7-7-5-8)
- [7.7.5.9 16.0 GT/s Lane Equalization Control Register (Offsets 20h to 3Ch) | 16.0 GT/s 通道均衡控制寄存器(偏移量 20h 至 3Ch)](#sec-7-7-5-9)
- [7.7.6 Physical Layer 32.0 GT/s Extended Capability | 物理层 32.0 GT/s 扩展能力](#sec-7-7-6)
- [7.7.6.1 Physical Layer 32.0 GT/s Extended Capability Header (Offset 00h) | 物理层 32.0 GT/s 扩展能力头（偏移 00h）](#sec-7-7-6-1)
- [7.7.6.2 32.0 GT/s Capabilities Register (Offset 04h) | 32.0 GT/s 能力寄存器（偏移 04h）](#sec-7-7-6-2)
- [7.7.6.3 32.0 GT/s Control Register (Offset 08h) | 32.0 GT/s 控制寄存器（偏移 08h）](#sec-7-7-6-3)
- [7.7.6.4 32.0 GT/s Status Register (Offset 0Ch) | 32.0 GT/s 状态寄存器（偏移 0Ch）](#sec-7-7-6-4)
- [7.7.6.5 Received Modified TS Data 1 Register (Offset 10h) | 接收 Modified TS 数据 1 寄存器（偏移 10h）](#sec-7-7-6-5)
- [7.7.6.6 Received Modified TS Data 2 Register (Offset 14h) | 接收 Modified TS 数据 2 寄存器（偏移 14h）](#sec-7-7-6-6)
- [7.7.6.7 Transmitted Modified TS Data 1 Register (Offset 18h) | 发送 Modified TS 数据 1 寄存器（偏移 18h）](#sec-7-7-6-7)
- [7.7.6.8 Transmitted Modified TS Data 2 Register (Offset 1Ch) | 发送 Modified TS 数据 2 寄存器（偏移 1Ch）](#sec-7-7-6-8)
- [7.7.6.9 32.0 GT/s Lane Equalization Control Register (Offset 20h) | 32.0 GT/s 通道均衡控制寄存器(偏移 20h)](#sec-7-7-6-9)
- [7.7.7 Physical Layer 64.0 GT/s Extended Capability | 7.7.7 物理层 64.0 GT/s 扩展能力](#sec-7-7-7)
- [7.7.7.1 Physical Layer 64.0 GT/s Extended Capability Header (Offset 00h) | 7.7.7.1 物理层 64.0 GT/s 扩展能力 Header(偏移 00h)](#sec-7-7-7-1)
- [7.7.7.2 64.0 GT/s Capabilities Register (Offset 04h) | 7.7.7.2 64.0 GT/s 能力寄存器(偏移 04h)](#sec-7-7-7-2)
- [7.7.7.3 64.0 GT/s Control Register (Offset 08h) | 7.7.7.3 64.0 GT/s 控制寄存器(偏移 08h)](#sec-7-7-7-3)
- [7.7.7.4 64.0 GT/s Status Register (Offset 0Ch) | 7.7.7.4 64.0 GT/s 状态寄存器(偏移 0Ch)](#sec-7-7-7-4)
- [7.7.7.5 64.0 GT/s Lane Equalization Control Register (Offset 10h) | 7.7.7.5 64.0 GT/s 通道均衡控制寄存器(偏移 10h)](#sec-7-7-7-5)
- [7.7.8 Flit Logging Extended Capability | 7.7.8 Flit 日志扩展能力](#sec-7-7-8)
- [7.7.8.1 Flit Logging Extended Capability Header (Offset 00h) | 7.7.8.1 Flit 日志扩展能力 Header(偏移 00h)](#sec-7-7-8-1)
- [7.7.8.2 Flit Error Log 1 Register (Offset 04h) | 7.7.8.2 Flit 错误日志 1 寄存器(偏移 04h)](#sec-7-7-8-2)
- [7.7.8.3 Flit Error Log 2 Register (Offset 08h) | Flit 错误日志 2 寄存器（偏移 08h）](#sec-7-7-8-3)
- [7.7.8.4 Flit Error Counter Control Register (Offset 0Ch) | Flit 错误计数控制寄存器（偏移 0Ch）](#sec-7-7-8-4)
- [7.7.8.5 Flit Error Counter Status Register (Offset 0Eh) | Flit 错误计数状态寄存器（偏移 0Eh）](#sec-7-7-8-5)
- [7.7.8.6 FBER Measurement Control Register (Offset 10h) | FBER 测量控制寄存器（偏移 10h）](#sec-7-7-8-6)
- [7.7.8.7 FBER Measurement Status 1 Register (Offset 14h) | FBER 测量状态 1 寄存器（偏移 14h）](#sec-7-7-8-7)
- [7.7.8.8 FBER Measurement Status 2 Register (Offset 18h) | FBER 测量状态 2 寄存器（偏移 18h）](#sec-7-7-8-8)
- [7.7.8.9 FBER Measurement Status 3 Register (Offset 1Ch) | FBER 测量状态 3 寄存器（偏移 1Ch）](#sec-7-7-8-9)
- [7.7.8.10 FBER Measurement Status 4 Register (Offset 20h) | FBER 测量状态 4 寄存器（偏移 20h）](#sec-7-7-8-10)
- [7.7.8.11 FBER Measurement Status 5 Register (Offset 24h) | FBER 测量状态 5 寄存器（偏移 24h）](#sec-7-7-8-11)
- [7.7.8.12 FBER Measurement Status 6 Register (Offset 28h) | FBER 测量状态 6 寄存器（偏移 28h）](#sec-7-7-8-12)
- [7.7.8.13 FBER Measurement Status 7 Register (Offset 2Ch) | FBER 测量状态 7 寄存器（偏移 2Ch）](#sec-7-7-8-13)
- [7.7.8.14 FBER Measurement Status 8 Register (Offset 30h) | FBER 测量状态 8 寄存器（偏移 30h）](#sec-7-7-8-14)
- [7.7.8.15 FBER Measurement Status 9 Register (Offset 34h) | FBER 测量状态 9 寄存器（偏移 34h）](#sec-7-7-8-15)
- [7.7.8.16 FBER Measurement Status 10 Register (Offset 38h) | FBER 测量状态 10 寄存器（偏移 38h）](#sec-7-7-8-16)
- [7.7.9 Device 3 Extended Capability Structure | Device 3 扩展能力结构](#sec-7-7-9)
- [7.7.9.2 Device Capabilities 3 Register (Offset 04h) | Device 能力 3 寄存器 (偏移 04h)](#sec-7-7-9-2)
- [7.7.9.3 Device Control 3 Register (Offset 08h) | Device 控制 3 寄存器 (偏移 08h)](#sec-7-7-9-3)
- [7.7.9.4 Device Status 3 Register (Offset 0Ch) | Device 状态 3 寄存器 (偏移 0Ch)](#sec-7-7-9-4)
- [7.7.10 Lane Margining at the Receiver Extended Capability | 接收器通道裕度扩展能力 (Lane Margining at the Receiver Extended Capability)](#sec-7-7-10)
- [7.7.10.1 Lane Margining at the Receiver Extended Capability Header (Offset 00h) | 接收器通道裕度扩展能力头 (偏移 00h)](#sec-7-7-10-1)
- [7.7.10.2 Margining Port Capabilities Register (Offset 04h) | 裕度端口能力寄存器 (偏移 04h)](#sec-7-7-10-2)
- [7.7.10.3 Margining Port Status Register (Offset 06h) | 裕度端口状态寄存器 (偏移 06h)](#sec-7-7-10-3)
- [7.7.10.4 Margining Lane Control Register (Offset 08h) | Margining Lane 控制寄存器（偏移 08h）](#sec-7-7-10-4)
- [7.7.10.5 Margining Lane Status Register (Offset 0Ah) | Margining Lane 状态寄存器（偏移 0Ah）](#sec-7-7-10-5)
- [7.7.11 ACS Extended Capability | ACS 扩展能力（Access Control Services）](#sec-7-7-11)
- [7.7.11.1 ACS Extended Capability Header (Offset 00h) | ACS 扩展能力头（偏移 00h）](#sec-7-7-11-1)
- [7.7.11.2 ACS Capability Register (Offset 04h) | ACS 能力寄存器（偏移 04h）](#sec-7-7-11-2)
- [7.7.11.3 ACS Control Register (Offset 06h) | ACS 控制寄存器（偏移 06h）](#sec-7-7-11-3)
- [7.7.11.4 Egress Control Vector Register (Offset 08h) | Egress Control Vector 寄存器（偏移 08h）](#sec-7-7-11-4)
- [7.8 Common PCI and PCIe Capabilities | 通用 PCI 与 PCIe 能力](#sec-7-8)
- [7.8.1 Power Budgeting Extended Capability | 功耗预算（Power Budgeting）扩展能力](#sec-7-8-1)
- [7.8.1.1 Power Budgeting Extended Capability Header (Offset 00h) | 功耗预算扩展能力头(偏移 00h)](#sec-7-8-1-1)
- [7.8.1.2 Power Budgeting Data Select Register (Offset 04h) | 功耗预算数据选择寄存器(偏移 04h)](#sec-7-8-1-2)
- [7.8.1.3 Power Budgeting Control Register (Offset 06h) | 功耗预算控制寄存器(偏移 06h)](#sec-7-8-1-3)
- [7.8.1.4 Power Budgeting Data Register (Offset 08h) | 功耗预算数据寄存器(偏移 08h)](#sec-7-8-1-4)
- [7.8.1.5 Power Budgeting Capability Register (Offset 0Ch) | 功耗预算能力寄存器(偏移 0Ch)](#sec-7-8-1-5)
- [7.8.1.6 Power Budgeting Sense Detect Register (Offset 0Dh) | 功耗预算感应检测寄存器(偏移 0Dh)](#sec-7-8-1-6)
- [7.8.2 Latency Tolerance Reporting (LTR) Extended Capability | 延迟容忍报告 (LTR) 扩展能力](#sec-7-8-2)
- [7.8.2.1 LTR Extended Capability Header (Offset 00h) | LTR 扩展能力头(偏移 00h)](#sec-7-8-2-1)
- [7.8.2.2 Max Snoop Latency Register (Offset 04h) | 最大监听延迟寄存器(偏移 04h)](#sec-7-8-2-2)
- [7.8.2.3 Max No-Snoop Latency Register (Offset 06h) | 最大非监听延迟寄存器(偏移 06h)](#sec-7-8-2-3)
- [7.8.3 L1 PM Substates Extended Capability | L1 PM 子状态扩展能力](#sec-7-8-3)
- [7.8.3.1 L1 PM Substates Extended Capability Header (Offset 00h) | L1 PM 子状态扩展能力头(偏移 00h)](#sec-7-8-3-1)
- [7.8.3.2 L1 PM Substates Capabilities Register (Offset 04h) | L1 PM 子状态能力寄存器(偏移 04h)](#sec-7-8-3-2)
- [7.8.3.3 L1 PM Substates Control 1 Register (Offset 08h) | L1 PM 子状态控制 1 寄存器(偏移 08h)](#sec-7-8-3-3)
- [7.8.3.4 L1 PM Substates Control 2 Register (Offset 0Ch) | L1 PM 子状态控制 2 寄存器(偏移 0Ch)](#sec-7-8-3-4)
- [7.8.3.5 L1 PM Substates Status Register (Offset 10h) | L1 PM 子状态寄存器(偏移 10h)](#sec-7-8-3-5)
- [7.8.4 Advanced Error Reporting Extended Capability | 高级错误报告扩展能力](#sec-7-8-4)
- [7.8.4.1 Advanced Error Reporting Extended Capability Header (Offset 00h) | 高级错误报告扩展能力头(偏移 00h)](#sec-7-8-4-1)
- [7.8.4.2 Uncorrectable Error Status Register (Offset 04h) | 不可纠正错误状态寄存器（偏移 04h）](#sec-7-8-4-2)
- [7.8.4.9 Root Error Command Register (Offset 2Ch) | 根错误命令寄存器（偏移 2Ch）](#sec-7-8-4-9)
- [7.8.4.10 Root Error Status Register (Offset 30h) | 根错误状态寄存器（偏移 30h）](#sec-7-8-4-10)
- [7.8.4.11 Error Source Identification Register (Offset 34h) | 错误源标识寄存器（偏移 34h）](#sec-7-8-4-11)
- [7.8.4.12 TLP Prefix Log Register (Offset 38h) | TLP 前缀日志寄存器（偏移 38h）](#sec-7-8-4-12)
- [7.8.5 Enhanced Allocation Capability Structure (EA) | 增强分配能力结构（EA）](#sec-7-8-5)
- [7.8.5.1 Enhanced Allocation Capability First DW (Offset 00h) | 增强分配能力首 DW（偏移 00h）](#sec-7-8-5-1)
- [7.8.5.2 Enhanced Allocation Capability Second DW (Offset 04h) [Type 1 Functions Only] | 增强分配能力第二 DW（偏移 04h）[仅 Type 1 功能]](#sec-7-8-5-2)
- [7.8.5.3 Enhanced Allocation Per-Entry Format (Offset 04h or 08h) | 增强分配逐条目格式（偏移 04h 或 08h）](#sec-7-8-5-3)
- [7.8.6 Resizable BAR Extended Capability | 可调整 BAR 扩展能力（Resizable BAR Extended Capability）](#sec-7-8-6)
- [7.8.6.1 Resizable BAR Extended Capability Header (Offset 00h) | 可变大小 BAR 扩展能力头（偏移 00h）](#sec-7-8-6-1)
- [7.8.6.2 Resizable BAR Capability Register | 可变大小 BAR 能力寄存器](#sec-7-8-6-2)
- [7.8.6.3 Resizable BAR Control Register | 可变大小 BAR 控制寄存器](#sec-7-8-6-3)
- [7.8.7 VF Resizable BAR Extended Capability | VF 可变大小 BAR 扩展能力](#sec-7-8-7)
- [7.8.7.1 VF Resizable BAR Extended Capability Header (Offset 00h) | VF 可变大小 BAR 扩展能力头（偏移 00h）](#sec-7-8-7-1)
- [7.8.7.2 VF Resizable BAR Capability Register (Offset 04h) | VF 可变大小 BAR 能力寄存器（偏移 04h）](#sec-7-8-7-2)
- [7.8.7.3 VF Resizable BAR Control Register (Offset 08h) | VF 可变大小 BAR 控制寄存器（偏移 08h）](#sec-7-8-7-3)
- [7.8.8 ARI Extended Capability | ARI 扩展能力](#sec-7-8-8)
- [7.8.8.1 ARI Extended Capability Header (Offset 00h) | ARI 扩展能力头（偏移 00h）](#sec-7-8-8-1)
- [7.8.8.2 ARI Capability Register (Offset 04h) | ARI 能力寄存器（偏移 04h）](#sec-7-8-8-2)
- [7.8.8.3 ARI Control Register (Offset 06h) | ARI 控制寄存器（偏移 06h）](#sec-7-8-8-3)
- [7.8.9 PASID Extended Capability Structure | PASID 扩展能力结构](#sec-7-8-9)
- [7.8.9.1 PASID Extended Capability Header (Offset 00h) | PASID 扩展能力头（偏移 00h）](#sec-7-8-9-1)
- [7.8.9.2 PASID Capability Register (Offset 04h) | PASID 能力寄存器（偏移 04h）](#sec-7-8-9-2)
- [7.8.9.3 PASID Control Register (Offset 06h) | PASID 控制寄存器（偏移 06h）](#sec-7-8-9-3)
- [7.8.10 FRS Queueing Extended Capability | FRS 排队扩展能力](#sec-7-8-10)
- [7.8.10.1 FRS Queueing Extended Capability Header (Offset 00h) | FRS 排队扩展能力头（偏移 00h）](#sec-7-8-10-1)
- [7.8.10.2 FRS Queueing Capability Register (Offset 04h) | FRS 排队能力寄存器（偏移 04h）](#sec-7-8-10-2)
- [7.8.10.3 FRS Queueing Status Register (Offset 08h) | FRS 排队状态寄存器（偏移 08h）](#sec-7-8-10-3)
- [7.8.10.4 FRS Queueing Control Register (Offset 0Ah) | FRS 排队控制寄存器 (Offset 0Ah)](#sec-7-8-10-4)
- [7.8.10.5 FRS Message Queue Register (Offset 0Ch) | FRS 报文队列寄存器 (Offset 0Ch)](#sec-7-8-10-5)
- [7.8.11 Flattening Portal Bridge (FPB) Capability | 7.8.11 扁平化门户桥 (FPB) 能力](#sec-7-8-11)
- [7.8.11.1 FPB Capability Header (Offset 00h) | 7.8.11.1 FPB 能力头 (Offset 00h)](#sec-7-8-11-1)
- [7.8.11.2 FPB Capabilities Register (Offset 04h) | 7.8.11.2 FPB 能力寄存器 (Offset 04h)](#sec-7-8-11-2)
- [7.8.11.3 FPB RID Vector Control 1 Register (Offset 08h) | 7.8.11.3 FPB RID 向量控制 1 寄存器 (Offset 08h)](#sec-7-8-11-3)
- [7.8.11.4 FPB RID Vector Control 2 Register (Offset 0Ch) | 7.8.11.4 FPB RID 向量控制 2 寄存器 (Offset 0Ch)](#sec-7-8-11-4)
- [7.8.11.5 FPB MEM Low Vector Control Register (Offset 10h) | 7.8.11.5 FPB MEM Low 向量控制寄存器 (Offset 10h)](#sec-7-8-11-5)
- [7.8.11.6 FPB MEM High Vector Control 1 Register (Offset 14h) | 7.8.11.6 FPB MEM High 向量控制 1 寄存器 (Offset 14h)](#sec-7-8-11-6)
- [7.8.11.7 FPB MEM High Vector Control 2 Register (Offset 18h) | 7.8.11.7 FPB MEM High 向量控制 2 寄存器 (Offset 18h)](#sec-7-8-11-7)
- [7.8.11.8 FPB Vector Access Control Register (Offset 1Ch) | 7.8.11.8 FPB 向量访问控制寄存器 (Offset 1Ch)](#sec-7-8-11-8)
- [7.8.11.9 FPB Vector Access Data Register (Offset 20h) | 7.8.11.9 FPB 向量访问数据寄存器 (Offset 20h)](#sec-7-8-11-9)
- [7.8.12 Flit Performance Measurement Extended Capability | Flit 性能测量扩展能力](#sec-7-8-12)
- [7.8.12.1 Flit Performance Measurement Extended Capability Header (Offset 00h) | Flit 性能测量扩展能力头（偏移 00h）](#sec-7-8-12-1)
- [7.8.12.2 Flit Performance Measurement Capability Register (Offset 04h) | Flit 性能测量能力寄存器（偏移 04h）](#sec-7-8-12-2)
- [7.8.12.3 Flit Performance Measurement Control Register (Offset 08h) | Flit 性能测量控制寄存器（偏移 08h）](#sec-7-8-12-3)
- [7.8.13 Flit Error Injection Extended Capability | Flit 错误注入扩展能力](#sec-7-8-13)
- [7.9 Additional PCI and PCIe Capabilities | 7.9 其他 PCI 和 PCIe 能力](#sec-7-9)
- [7.9.1 Virtual Channel Extended Capability | 7.9.1 虚通道扩展能力](#sec-7-9-1)
- [7.9.1.3 Port VC Capability Register 2 (Offset 08h) | 端口 VC 能力寄存器 2 (偏移量 08h)](#sec-7-9-1-3)
- [7.9.1.4 Port VC Control Register (Offset 0Ch) | 端口 VC 控制寄存器 (偏移量 0Ch)](#sec-7-9-1-4)
- [7.9.1.5 Port VC Status Register (Offset 0Eh) | 端口 VC 状态寄存器 (偏移量 0Eh)](#sec-7-9-1-5)
- [7.9.1.6 VC Resource Capability Register | VC 资源能力寄存器](#sec-7-9-1-6)
- [7.9.1.7 VC Resource Control Register | VC 资源控制寄存器](#sec-7-9-1-7)
- [7.9.1.8 VC Resource Status Register | VC 资源状态寄存器](#sec-7-9-1-8)
- [7.9.1.9 VC Arbitration Table | VC 仲裁表](#sec-7-9-1-9)
- [7.9.1.10 Port Arbitration Table | 端口仲裁表](#sec-7-9-1-10)
- [7.9.2 Multi-Function Virtual Channel Extended Capability | 多功能虚通道扩展能力](#sec-7-9-2)
- [7.9.2.1 MFVC Extended Capability Header (Offset 00h) | MFVC 扩展能力头 (偏移量 00h)](#sec-7-9-2-1)
- [7.9.2.2 MFVC Port VC Capability Register 1 (Offset 04h) | MFVC 端口 VC 能力寄存器 1 (偏移量 04h)](#sec-7-9-2-2)
- [7.9.2.3 MFVC Port VC Capability Register 2 (Offset 08h) | MFVC 端口 VC 能力寄存器 2 (偏移量 08h)](#sec-7-9-2-3)
- [7.9.2.4 MFVC Port VC Control Register (Offset 0Ch) | MFVC 端口 VC 控制寄存器 (偏移量 0Ch)](#sec-7-9-2-4)
- [7.9.2.5 MFVC Port VC Status Register (Offset 0Eh) | MFVC 端口 VC 状态寄存器 (偏移量 0Eh)](#sec-7-9-2-5)
- [7.9.2.6 MFVC VC Resource Capability Register | MFVC VC 资源能力寄存器](#sec-7-9-2-6)
- [7.9.2.7 MFVC VC Resource Control Register | MFVC VC 资源控制寄存器](#sec-7-9-2-7)
- [7.9.2.8 MFVC VC Resource Status Register | MFVC VC 资源状态寄存器](#sec-7-9-2-8)
- [7.9.2.9 MFVC VC Arbitration Table | MFVC VC 仲裁表](#sec-7-9-2-9)
- [7.9.2.10 Function Arbitration Table | Function 仲裁表](#sec-7-9-2-10)
- [7.9.3 Device Serial Number Extended Capability | 设备序列号扩展能力](#sec-7-9-3)
- [7.9.3 Device Serial Number Extended Capability | 设备序列号扩展能力](#sec-7-9-3)
- [7.9.3.1 Device Serial Number Extended Capability Header (Offset 00h) | 设备序列号扩展能力包头(偏移 00h)](#sec-7-9-3-1)
- [7.9.3.2 Serial Number Register (Offset 04h) | 序列号寄存器(偏移 04h)](#sec-7-9-3-2)
- [7.9.4 Vendor-Specific Capability | 厂商特定能力](#sec-7-9-4)
- [7.9.5 Vendor-Specific Extended Capability | 厂商特定扩展能力](#sec-7-9-5)
- [7.9.5.1 Vendor-Specific Extended Capability Header (Offset 00h) | 厂商特定扩展能力包头(偏移 00h)](#sec-7-9-5-1)
- [7.9.5.2 Vendor-Specific Header (Offset 04h) | 厂商特定包头(偏移 04h)](#sec-7-9-5-2)
- [7.9.6 Designated Vendor-Specific Extended Capability (DVSEC) | 指定厂商特定扩展能力 (DVSEC)](#sec-7-9-6)
- [7.9.6.1 Designated Vendor-Specific Extended Capability Header (Offset 00h) | 指定厂商特定扩展能力包头(偏移 00h)](#sec-7-9-6-1)
- [7.9.6.2 Designated Vendor-Specific Header 1 (Offset 04h) | 指定厂商特定包头 1(偏移 04h)](#sec-7-9-6-2)
- [7.9.6.3 Designated Vendor-Specific Header 2 (Offset 08h) | 指定厂商特定包头 2(偏移 08h)](#sec-7-9-6-3)
- [7.9.7 RCRB Header Extended Capability | RCRB 头扩展能力](#sec-7-9-7)
- [7.9.8 Root Complex Link Declaration Extended Capability](#sec-7-9-8)
- [7.9.8 Root Complex Link Declaration Extended Capability（根复合体链路声明扩展能力）](#sec-7-9-8)
- [7.9.9 Root Complex Internal Link Control Extended Capability](#sec-7-9-9)
- [7.9.9 Root Complex Internal Link Control Extended Capability（根复合体内部链路控制扩展能力）](#sec-7-9-9)
- [7.9.9.1 Root Complex Internal Link Control Extended Capability Header (Offset 00h) | 根复合体内部链路控制扩展能力头(偏移量 00h)](#sec-7-9-9-1)
- [7.9.9.2 Root Complex Link Capabilities Register (Offset 04h) | 根复合体链路能力寄存器(偏移量 04h)](#sec-7-9-9-2)
- [7.9.9.3 Root Complex Link Control Register (Offset 08h) | 根复合体链路控制寄存器(偏移量 08h)](#sec-7-9-9-3)
- [7.9.9.4 Root Complex Link Status Register (Offset 0Ah) | 根复合体链路状态寄存器(偏移量 0Ah)](#sec-7-9-9-4)
- [7.9.10 Root Complex Event Collector Endpoint Association Extended Capability | 根复合体事件收集器端点关联扩展能力](#sec-7-9-10)
- [7.9.10.1 Root Complex Event Collector Endpoint Association Extended Capability Header (Offset 00h) | 根复合体事件收集器端点关联扩展能力头(偏移量 00h)](#sec-7-9-10-1)
- [7.9.10.2 Association Bitmap for RCiEPs (Offset 04h) | RCiEP 关联位图(偏移量 04h)](#sec-7-9-10-2)
- [7.9.10.3 RCEC Associated Bus Numbers Register (Offset 08h) | RCEC 关联总线号寄存器(偏移量 08h)](#sec-7-9-10-3)
- [7.9.11 Multicast Extended Capability | 组播扩展能力](#sec-7-9-11)
- [7.9.11.1 Multicast Extended Capability Header (Offset 00h) | 组播扩展能力头(偏移量 00h)](#sec-7-9-11-1)
- [7.9.11.2 Multicast Capability Register (Offset 04h) | 组播能力寄存器(偏移量 04h)](#sec-7-9-11-2)
- [7.9.11.3 Multicast Control Register (Offset 06h) | 多播控制寄存器（偏移 06h）](#sec-7-9-11-3)
- [7.9.11.4 MC_Base_Address Register (Offset 08h) | MC_Base_Address 寄存器（偏移 08h）](#sec-7-9-11-4)
- [7.9.11.5 MC_Receive Register (Offset 10h) | MC_Receive 寄存器（偏移 10h）](#sec-7-9-11-5)
- [7.9.11.6 MC_Block_All Register (Offset 18h) | MC_Block_All 寄存器（偏移 18h）](#sec-7-9-11-6)
- [7.9.11.7 MC_Block_Untranslated Register (Offset 20h) | MC_Block_Untranslated 寄存器（偏移 20h）](#sec-7-9-11-7)
- [7.9.11.8 MC_Overlay_BAR Register (Offset 28h) | MC_Overlay_BAR 寄存器（偏移 28h）](#sec-7-9-11-8)
- [7.9.12 Dynamic Power Allocation Extended Capability (DPA Capability) | 动态功率分配扩展能力（DPA 能力）](#sec-7-9-12)
- [7.9.12.1 DPA Extended Capability Header (Offset 00h) | DPA 扩展能力头（偏移 00h）](#sec-7-9-12-1)
- [7.9.12.2 DPA Capability Register (Offset 04h) | DPA 能力寄存器（偏移 04h）](#sec-7-9-12-2)
- [7.9.12.3 DPA Latency Indicator Register (Offset 08h) | DPA 延迟指示寄存器（偏移 08h）](#sec-7-9-12-3)
- [7.9.12.4 DPA Status Register (Offset 0Ch) | DPA 状态寄存器（偏移 0Ch）](#sec-7-9-12-4)
- [7.9.12.5 DPA Control Register (Offset 0Eh) | DPA 控制寄存器（偏移 0Eh）](#sec-7-9-12-5)
- [7.9.12.6 DPA Power Allocation Array | DPA 功率分配数组](#sec-7-9-12-6)
- [7.9.13 TPH Requester Extended Capability | TPH 请求者扩展能力](#sec-7-9-13)
- [7.9.13.1 TPH Requester Extended Capability Header (Offset 00h) | TPH 请求者扩展能力头（偏移 00h）](#sec-7-9-13-1)
- [7.9.13.2 TPH Requester Capability Register (Offset 04h) | TPH 请求者能力寄存器（偏移 04h）](#sec-7-9-13-2)
- [7.9.13.3 TPH Requester Control Register (Offset 08h) | TPH 请求者控制寄存器（偏移 08h）](#sec-7-9-13-3)
- [7.9.13.4 TPH ST Table (Starting from Offset 0Ch) | TPH ST 表（起始偏移 0Ch）](#sec-7-9-13-4)
- [7.9.14 DPC Extended Capability | DPC 扩展能力](#sec-7-9-14)
- [7.9.14.1 DPC Extended Capability Header (Offset 00h) | DPC 扩展能力头（偏移 00h）](#sec-7-9-14-1)
- [7.9.14.2 DPC Capability Register (Offset 04h) | DPC 能力寄存器（偏移 04h）](#sec-7-9-14-2)
- [7.9.14.3 DPC Control Register (Offset 06h) | DPC 控制寄存器（偏移 06h）](#sec-7-9-14-3)
- [7.9.14.4 DPC Status Register (Offset 08h) | DPC 状态寄存器（偏移 08h）](#sec-7-9-14-4)
- [7.9.14.5 DPC Error Source ID Register (Offset 0Ah) | DPC 错误源 ID 寄存器（偏移 0Ah）](#sec-7-9-14-5)
- [7.9.14.6 RP PIO Status Register (Offset 0Ch) | RP PIO 状态寄存器（偏移 0Ch）](#sec-7-9-14-6)
- [7.9.14.7 RP PIO Mask Register (Offset 10h) | RP PIO 屏蔽寄存器 (偏移 10h)](#sec-7-9-14-7)
- [7.9.14.8 RP PIO Severity Register (Offset 14h) | RP PIO 严重程度寄存器 (偏移 14h)](#sec-7-9-14-8)
- [7.9.14.9 RP PIO SysError Register (Offset 18h) | RP PIO 系统错误寄存器 (偏移 18h)](#sec-7-9-14-9)
- [7.9.14.10 RP PIO Exception Register (Offset 1Ch) | RP PIO 异常寄存器 (偏移 1Ch)](#sec-7-9-14-10)
- [7.9.14.11 RP PIO Header Log Register (Offset 20h) | RP PIO Header Log 寄存器 (偏移 20h)](#sec-7-9-14-11)
- [7.9.14.12 RP PIO ImpSpec Log Register (Offset 30h) | RP PIO ImpSpec Log 寄存器 (偏移 30h)](#sec-7-9-14-12)
- [7.9.15.1 PTM Extended Capability Header (Offset 00h) | PTM 扩展能力包头 (偏移 00h)](#sec-7-9-15-1)
- [7.9.16.2 Readiness Time Reporting 1 Register (Offset 04h) | 就绪时间报告 1 寄存器（偏移 04h）](#sec-7-9-16-2)
- [7.9.16.3 Readiness Time Reporting 2 Register (Offset 08h) | 就绪时间报告 2 寄存器（偏移 08h）](#sec-7-9-16-3)
- [7.9.17 Hierarchy ID Extended Capability | 层级 ID 扩展能力（Hierarchy ID Extended Capability）](#sec-7-9-17)
- [7.9.17.1 Hierarchy ID Extended Capability Header (Offset 00h) | 层级 ID 扩展能力头（偏移 00h）](#sec-7-9-17-1)
- [7.9.17.2 Hierarchy ID Status Register (Offset 04h) | 层级 ID 状态寄存器（偏移 04h）](#sec-7-9-17-2)
- [7.9.17.3 Hierarchy ID Data Register (Offset 08h) | 层级 ID 数据寄存器（偏移 08h）](#sec-7-9-17-3)
- [7.9.17.4 Hierarchy ID GUID 1 Register (Offset 0Ch) | 层级 ID GUID 1 寄存器（偏移 0Ch）](#sec-7-9-17-4)
- [7.9.17.5 Hierarchy ID GUID 2 Register (Offset 10h) | 层级 ID GUID 2 寄存器（偏移 10h）](#sec-7-9-17-5)
- [7.9.17.6 Hierarchy ID GUID 3 Register (Offset 14h) | 层级 ID GUID 3 寄存器（偏移 14h）](#sec-7-9-17-6)
- [7.9.17.7 Hierarchy ID GUID 4 Register (Offset 18h) | 层级 ID GUID 4 寄存器（偏移 18h）](#sec-7-9-17-7)
- [7.9.17.8 Hierarchy ID GUID 5 Register (Offset 1Ch) | 层级 ID GUID 5 寄存器 (偏移 1Ch)](#sec-7-9-17-8)
- [7.9.18 Vital Product Data Capability (VPD Capability) | 重要产品数据能力 (VPD Capability)](#sec-7-9-18)
- [7.9.18.1 VPD Address Register | VPD Address 寄存器](#sec-7-9-18-1)
- [7.9.18.2 VPD Data Register | VPD Data 寄存器](#sec-7-9-18-2)
- [7.9.19 Native PCIe Enclosure Management Extended Capability (NPEM Extended Capability) | 原生 PCIe 机框管理扩展能力 (NPEM 扩展能力)](#sec-7-9-19)
- [7.9.19.1 NPEM Extended Capability Header (Offset 00h) | NPEM 扩展能力头 (偏移 00h)](#sec-7-9-19-1)
- [7.9.19.2 NPEM Capability Register (Offset 04h) | NPEM Capability 寄存器 (偏移 04h)](#sec-7-9-19-2)
- [7.9.19.3 NPEM Control Register (Offset 08h) | NPEM Control 寄存器 (偏移 08h)](#sec-7-9-19-3)
- [7.9.19.4 NPEM Status Register (Offset 0Ch) | NPEM Status 寄存器 (偏移 0Ch)](#sec-7-9-19-4)
- [7.9.20 Alternate Protocol Extended Capability | Alternate Protocol 扩展能力](#sec-7-9-20)
- [7.9.20.1 Alternate Protocol Extended Capability Header (Offset 00h) | Alternate Protocol 扩展能力头 (偏移 00h)](#sec-7-9-20-1)
- [7.9.20.2 Alternate Protocol Capabilities Register (Offset 04h) | Alternate Protocol Capabilities 寄存器 (偏移 04h)](#sec-7-9-20-2)
- [7.9.20.3 Alternate Protocol Control Register (Offset 08h) | 替代协议控制寄存器（偏移量 08h）](#sec-7-9-20-3)
- [7.9.20.4 Alternate Protocol Data 1 Register (Offset 0Ch) | 替代协议数据 1 寄存器（偏移量 0Ch）](#sec-7-9-20-4)
- [7.9.20.5 Alternate Protocol Data 2 Register (Offset 10h) | 替代协议数据 2 寄存器（偏移量 10h）](#sec-7-9-20-5)
- [7.9.20.6 Alternate Protocol Selective Enable Mask Register (Offset 14h) | 替代协议选择性使能掩码寄存器（偏移量 14h）](#sec-7-9-20-6)
- [7.9.21 Conventional PCI Advanced Features Capability (AF) | Conventional PCI 高级功能能力结构 (AF)](#sec-7-9-21)
- [7.9.21.1 Advanced Features Capability Header (Offset 00h) | 高级功能能力结构头部（偏移量 00h）](#sec-7-9-21-1)
- [7.9.21.2 AF Capabilities Register (Offset 03h) | AF 能力寄存器（偏移量 03h）](#sec-7-9-21-2)
- [7.9.21.3 Conventional PCI Advanced Features Control Register (Offset 04h) | Conventional PCI 高级功能控制寄存器（偏移量 04h）](#sec-7-9-21-3)
- [7.9.21.4 AF Status Register (Offset 05h) | AF 状态寄存器（偏移量 05h）](#sec-7-9-21-4)
- [7.9.22 SFI Extended Capability | SFI 扩展能力结构](#sec-7-9-22)
- [7.9.22.1 SFI Extended Capability Header (Offset 00h) | SFI 扩展能力结构头部（偏移量 00h）](#sec-7-9-22-1)
- [7.9.22.2 SFI Capability Register (Offset 04h) | SFI 能力寄存器（偏移量 04h）](#sec-7-9-22-2)
- [7.9.22.3 SFI Control Register (Offset 06h) | SFI 控制寄存器（偏移量 06h）](#sec-7-9-22-3)
- [7.9.22.4 SFI Status Register (Offset 08h) | SFI 状态寄存器 (偏移 08h)](#sec-7-9-22-4)
- [7.9.22.5 SFI CAM Address Register (Offset 0Ch) | SFI CAM 地址寄存器 (偏移 0Ch)](#sec-7-9-22-5)
- [7.9.22.6 SFI CAM Data Register (Offset 10h) | SFI CAM 数据寄存器 (偏移 10h)](#sec-7-9-22-6)
- [7.9.23 Subsystem ID and Subsystem Vendor ID Capability | Subsystem ID 与 Subsystem Vendor ID 能力](#sec-7-9-23)
- [7.9.23.1 Subsystem ID and Subsystem Vendor ID Capability Header (Offset 00h) | Subsystem ID 与 Subsystem Vendor ID 能力头部 (偏移 00h)](#sec-7-9-23-1)
- [7.9.23.2 Subsystem ID and Subsystem Vendor ID Capability Data (Offset 04h) | Subsystem ID 与 Subsystem Vendor ID 能力数据 (偏移 04h)](#sec-7-9-23-2)
- [7.9.24 Data Object Exchange Extended Capability | Data Object Exchange 扩展能力](#sec-7-9-24)
- [7.9.24.1 DOE Extended Capability Header (Offset 00h) | DOE 扩展能力头部 (偏移 00h)](#sec-7-9-24-1)
- [7.9.24.2 DOE Capabilities Register (Offset 04h) | DOE 能力寄存器 (偏移 04h)](#sec-7-9-24-2)
- [7.9.24.3 DOE Control Register (Offset 08h) | DOE 控制寄存器 (偏移 08h)](#sec-7-9-24-3)
- [7.9.24.4 DOE Status Register (Offset 0Ch) | DOE 状态寄存器 (偏移 0Ch)](#sec-7-9-24-4)
- [7.9.24.5 DOE Write Data Mailbox Register (Offset 10h) | DOE 写数据邮箱寄存器 (偏移 10h)](#sec-7-9-24-5)
- [7.9.24.6 DOE Read Data Mailbox Register (Offset 14h) | DOE 读数据邮箱寄存器 (偏移 14h)](#sec-7-9-24-6)
- [7.9.25 Shadow Functions Extended Capability | Shadow Functions 扩展能力](#sec-7-9-25)
- [7.9.25.1 Shadow Functions Extended Capability Header (Offset 00h) | Shadow Functions 扩展能力头（偏移 00h）](#sec-7-9-25-1)
- [7.9.25 Shadow Functions Capability | Shadow Functions 能力](#sec-7-9-25)
- [7.9.25.2 Shadow Functions Capability Register (Offset 04h) | Shadow Functions 能力寄存器（偏移 04h）](#sec-7-9-25-2)
- [7.9.25.3 Shadow Functions Control Register (Offset 08h) | Shadow Functions 控制寄存器（偏移 08h）](#sec-7-9-25-3)
- [7.9.25.4 Shadow Functions Instance Register Entry | Shadow Functions 实例寄存器项](#sec-7-9-25-4)
- [7.9.26 IDE Extended Capability | IDE 扩展能力](#sec-7-9-26)
- [7.9.26.1 IDE Extended Capability Header (Offset 00h) | IDE 扩展能力头（偏移 00h）](#sec-7-9-26-1)
- [7.9.26.2 IDE Capability Register (Offset 04h) | IDE 能力寄存器（偏移 04h）](#sec-7-9-26-2)
- [7.9.26.3 IDE Control Register (Offset 08h) | IDE 控制寄存器（偏移 08h）](#sec-7-9-26-3)
- [7.9.26.4 Link IDE Register Block | Link IDE 寄存器块](#sec-7-9-26-4)
- [7.9.26.4.1 Link IDE Stream Control Register | Link IDE Stream 控制寄存器](#sec-7-9-26-4-1)
- [7.9.26.4.2 Link IDE Stream Status Register | Link IDE Stream 状态寄存器](#sec-7-9-26-4-2)
- [7.9.26.5 Selective IDE Stream Register Block | Selective IDE Stream 寄存器块](#sec-7-9-26-5)
- [7.9.26.5.1 Selective IDE Stream Capability Register | 选择性 IDE 流能力寄存器](#sec-7-9-26-5-1)
- [7.9.26.5.2 Selective IDE Stream Control Register | 选择性 IDE 流控制寄存器](#sec-7-9-26-5-2)
- [7.9.26.5.3 Selective IDE Stream Status Register | 选择性 IDE 流状态寄存器](#sec-7-9-26-5-3)
- [7.9.26.5.4 Selective IDE RID Association Register Block | 选择性 IDE RID 关联寄存器块](#sec-7-9-26-5-4)
- [7.9.26.5.4.1 IDE RID Association Register 1 | IDE RID 关联寄存器 1](#sec-7-9-26-5-4-1)
- [7.9.26.5.4.2 IDE RID Association Register 2 | IDE RID 关联寄存器 2](#sec-7-9-26-5-4-2)
- [7.9.26.5.5 Selective IDE Address Association Register Block | 选择性 IDE 地址关联寄存器块](#sec-7-9-26-5-5)
- [7.9.26.5.5.1 IDE Address Association Register 1 | IDE 地址关联寄存器 1](#sec-7-9-26-5-5-1)
- [7.9.26.5.5.2 IDE Address Association Register 2 | IDE 地址关联寄存器 2](#sec-7-9-26-5-5-2)
- [7.9.26.5.5.3 IDE Address Association Register 3 | IDE 地址关联寄存器 3](#sec-7-9-26-5-5-3)
- [7.9.27 Null Capability | 空能力](#sec-7-9-27)
- [7.9.28 Null Extended Capability | 空扩展能力](#sec-7-9-28)
- [7.9.29 Streamlined Virtual Channel Extended Capability (SVC) | 精简虚通道扩展能力 (SVC)](#sec-7-9-29)
- [7.9.29.1 Streamlined Virtual Channel Extended Capability Header (Offset 00h) | 精简虚通道扩展能力头 (偏移量 00h)](#sec-7-9-29-1)
- [7.9.29.2 SVC Port Capability Register 1 (Offset 04h) | SVC 端口能力寄存器 1 (偏移量 04h)](#sec-7-9-29-2)
- [7.9.29.3 SVC Port Capability Register 2 (Offset 08h) | SVC 端口能力寄存器 2 (偏移量 08h)](#sec-7-9-29-3)
- [7.9.29.4 SVC Port Control Register (Offset 0Ch) | SVC 端口控制寄存器 (偏移量 0Ch)](#sec-7-9-29-4)
- [7.9.29.5 SVC Port Status Register (Offset 10h) | SVC 端口状态寄存器 (偏移量 10h)](#sec-7-9-29-5)
- [7.9.29.6 SVC Resource Capability Register | SVC 资源能力寄存器](#sec-7-9-29-6)
- [7.9.29.7 SVC Resource Control Register | SVC 资源控制寄存器](#sec-7-9-29-7)
- [7.9.29.8 SVC Resource Status Register | SVC 资源状态寄存器](#sec-7-9-29-8)
- [7.9.30 MMIO Register Block Locator Extended Capability (MRBL) | MMIO 寄存器块定位器扩展能力 (MRBL)](#sec-7-9-30)
- [7.9.30.1 MRBL Extended Capability Header (Offset 00h) | MRBL 扩展能力头 (偏移量 00h)](#sec-7-9-30-1)
- [7.9.30.2 MRBL Capabilities Register (Offset 04h) | MRBL 能力寄存器 (偏移量 04h)](#sec-7-9-30-2)
- [7.9.30.3 MRBL Locator Register (Offset Varies) | MRBL 定位寄存器 (偏移量可变)](#sec-7-9-30-3)

