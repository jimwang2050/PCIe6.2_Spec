#!/usr/bin/env python3
"""Add missing anchors to chapter body headings, then fix TOC skipped rows."""
import re, glob

# Missing anchors from fix_toc_links.py run
missing = [
    # ch04
    ('PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md', 'sec-4-2-7-4-6', '4.2.7.4.6'),
    # ch05
    ('PCIe6.2_Spec_ch05_Power_Management_电源管理.md', 'sec-5-3-1', '5.3.1'),
    # ch06 (duplicate — EN and ZH both missing)
    ('PCIe6.2_Spec_ch06_System_Architecture_系统架构.md', 'sec-6-1-1', '6.1.1'),
    # ch07
    ('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'sec-7-5-1-3-9', '7.5.1.3.9'),
    ('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'sec-7-8-4-3', '7.8.4.3'),
    ('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'sec-7-8-4-4', '7.8.4.4'),
    ('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'sec-7-8-4-5', '7.8.4.5'),
]

# ch08 has 26 missing — handle separately
ch08_missing = [
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-1', '8.3.5.1'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-2', '8.3.5.2'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-3', '8.3.5.3'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-4', '8.3.5.4'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-5', '8.3.5.5'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-6', '8.3-5-6'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-7', '8.3-5-7'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-8', '8.3-5-8'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-9', '8.3-5-9'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-10', '8.3-5-10'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-11', '8.3-5-11'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-12', '8.3-5-12'),
    ('PCIe6.2_Spec_ch08_Electical_Sub_Block_电气子块.md', 'sec-8-3-5-13', '8.3-5-13'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-14', '8.3-5-14'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-15', '8.3-5-15'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-3-5-16', '8.3-5-16'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-1', '8.8.1'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-2', '8.8.2'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-3', '8.8.3'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-4', '8.8.4'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-5', '8.8.5'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-6', '8.8.6'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-7', '8.8.7'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-8', '8.8.8'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-9', '8.8.9'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-10', '8.8-10'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-11', '8.8-11'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-12', '8.8-12'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-13', '8.8-13'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-14', '8.8-14'),
    ('PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md', 'sec-8-8-15', '8.8-15'),
]

def add_anchor(fname, anchor_id, sec_num):
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    if f'<a id="{anchor_id}"></a>' in content:
        return False
    # Find heading
    body = content[content.find('## 📑 章节索引'):]
    m = re.search(rf'^(#{1,3})\s+{re.escape(sec_num)}[\s\.]', body, re.MULTILINE)
    if not m:
        return False
    h_pos = body.find(m.group(0))
    abs_pos = content.find('## 📑 章节索引') + h_pos
    if f'<a id="{anchor_id}"></a>' in content[max(0,abs_pos-20):abs_pos+10]:
        return False
    content = content[:abs_pos] + f'<a id="{anchor_id}"></a>\n' + content[abs_pos:]
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

# First, find actual missing anchors in ch08 by scanning the file
print("=== Discovering actual missing anchors in ch08 ===")
f08 = 'PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md'
with open(f08, encoding='utf-8') as f:
    c08 = f.read()
defined08 = set(re.findall(r'<a id="([^"]+)"', c08))
# Get TOC skipped rows info
toc_start = c08.find('## 📑 章节索引 (Sections)')
next_h = c08.find('\n## ', toc_start + 10)
toc_body = c08[toc_start:next_h if next_h > 0 else len(c08)]
lines = toc_body.splitlines(keepends=True)
ch08_actual_missing = []
for line in lines:
    stripped = line.strip()
    if not re.match(r'^\|\s*\d+\.\d+', stripped):
        continue
    cols = [c.strip() for c in line.rstrip().rstrip('|').split('|')]
    if len(cols) < 3:
        continue
    sec_num = cols[1].strip()
    if re.match(r'[:\-\s|]+', sec_num) or not sec_num or sec_num == '#':
        continue
    anchor = 'sec-' + sec_num.replace('.', '-')
    if anchor not in defined08:
        ch08_actual_missing.append((sec_num, anchor))

print(f"ch08 actual missing: {[(s,a) for s,a in ch08_actual_missing]}")

# Combine all
all_missing = missing + [(f08, a, s) for s, a in ch08_actual_missing]

added = []
for fname, anchor_id, sec_num in all_missing:
    fname = fname.replace('Electical', 'Electrical')  # typo fix
    if add_anchor(fname, anchor_id, sec_num):
        added.append((anchor_id, sec_num))

print(f"\nAdded {len(added)} anchors:")
for a, s in added:
    print(f"  {a} ({s})")
