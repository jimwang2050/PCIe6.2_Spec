# 修复报告：全局 emoji 替换

**日期**: 2026-06-28
**问题**: 表头中文列使用 🇨🇳 而非规范规定的 🏆
**修复**: 全局替换 `🇨🇳 中文` → `🏆 中文`
**备份**: `.backup_20260628010625/`

---

## 替换结果

| 章节 | 文件 | 替换数 |
|------|------|--------|
| ch01 | `PCIe6.2_Spec_ch01_Introduction_引言.md` | 24 |
| ch02 | `PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md` | 243 |
| ch03 | `PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md` | 27 |
| ch04 | `PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md` | 353 |
| ch05 | `PCIe6.2_Spec_ch05_Power_Management_电源管理.md` | 59 |
| ch06 | `PCIe6.2_Spec_ch06_System_Architecture_系统架构.md` | 411 |
| ch07 | `PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md` | 711 |
| ch08 | `PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md` | 196 |
| ch09 | `PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md` | 39 |
| ch10 | `PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md` | 55 |
| ch11 | `PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md` | 29 |
| ch12 | `PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md` | 53 |
| **合计** | **12 文件** | **2200** |

---

## 验证

替换后全部 12 章 🇨🇳 计数 = 0，🏆 计数与替换数完全一致。

## 回滚（如需）

```bash
# 方法1: 从备份恢复
cp -r .backup_20260628010625/* .

# 方法2: 逆向替换
python3 -c "
import glob
for f in sorted(glob.glob('PCIe6.2_Spec_ch*.md')):
    with open(f, encoding='utf-8') as fh: c = fh.read()
    c = c.replace('🏆 中文', '🇨🇳 中文')
    with open(f, 'w', encoding='utf-8') as fh: fh.write(c)
    print(f'Restored: {f}')
"
```
