#!/usr/bin/env python3
import re, shutil, datetime, glob, os

ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_dir = f".backup_anchors_{ts}"

# Backup (exclude large dirs)
excludePatterns = ['.git', 'figures', 'chunks', 'preview', 'raw', 'tools', '.backup']
def ignore_fn(d, names):
    return [n for n in names if any(os.path.basename(n).startswith(p) or n.startswith(p) for p in excludePatterns) or n.endswith('.json') or n.endswith('.md')]

shutil.copytree('.', backup_dir, ignore=ignore_fn, dirs_exist_ok=True)
print(f"Backup: {backup_dir}/")

def add_missing_anchors(fname, anchor_map):
    with open(fname, encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines(keepends=True)
    new_lines = []
    added = []
    i = 0

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        m = re.match(r'^(#{1,3})\s+(.+?)\s*\|', line)
        if m:
            heading_text = m.group(2).strip()
            for anchor_id, pattern in anchor_map.items():
                if pattern in heading_text:
                    # Only insert if anchor not already present nearby
                    prev_content = ''.join(new_lines[-3:])
                    if f'<a id="{anchor_id}"></a>' not in prev_content and f'id="{anchor_id}"' not in line:
                        new_lines.insert(i, f'<a id="{anchor_id}"></a>\n')
                        added.append((anchor_id, heading_text[:60]))
                        i += 1
                    break
        i += 1

    if added:
        with open(fname, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"  {os.path.basename(fname):55s} +{len(added)}: {[a[0] for a in added]}")
    return added

# ---- ch01: 13 missing anchors ----
ch01_map = {
    'sec-1-0':      '1. Introduction',
    'sec-1-1':      '1.1 An Evolving',
    'sec-1-3':      '1.3 PCI Express Fabric Topology',
    'sec-1-3-1':    '1.3.1 Root Complex',
    'sec-1-3-2':    '1.3.2 Endpoints',
    'sec-1-3-2-2':  '1.3.2.2 PCI Express Endpoint Rules',
    'sec-1-3-3':    '1.3.3 Switch',
    'sec-1-3-4':    '1.3.4 Root Complex Event Collector',
    'sec-1-5':      '1.5 PCI Express Layering Overview',
    'sec-1-5-1':    '1.5.1 Transaction Layer',
    'sec-1-5-4':    '1.5.4 Layer Functions and Services',
    'sec-1-5-4-2':  '1.5.4.2 Data Link Layer Services',
    'sec-1-5-4-4':  '1.5.4.4 Inter-Layer Interfaces',
}
add_missing_anchors('PCIe6.2_Spec_ch01_Introduction_引言.md', ch01_map)

# ---- ch02: sec-2-0 missing ----
ch02_map = {
    'sec-2-0': '2. Transaction Layer Specification',
}
add_missing_anchors('PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md', ch02_map)

# ---- ch09: sec-9-0 missing ----
ch09_files = glob.glob('*SRIOV*.md')
for f in ch09_files:
    ch09_map = {
        'sec-9-0': '9. SR-IOV Architectural Overview',
    }
    add_missing_anchors(f, ch09_map)

# ---- Verify ----
print("\nVerification:")
for fname in glob.glob('PCIe6.2_Spec_ch*.md'):
    with open(fname, encoding='utf-8') as f:
        content = f.read()
    defined = set(re.findall(r'<a id="([^"]+)"', content))
    refs = set(re.findall(r'\]\(\#([^)]+)\)', content))
    broken = refs - defined - {'-本章目录-table-of-contents'}
    status = 'OK' if not broken else f'BROKEN({len(broken)})'
    print(f"  {os.path.basename(fname):55s} {status}")
