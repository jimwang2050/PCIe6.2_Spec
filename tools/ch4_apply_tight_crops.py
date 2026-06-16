#!/usr/bin/env python3
"""
将 ch04 MD 文件中所有 <img src="figures/chapter_04/fig_PPPP_NN.png">
自动替换为 <img src="figures/chapter_04/fig_PPPP_NN_tight.png">

策略:
- 如果 _tight.png 存在,替换
- 如果 _tight.png 不存在,保留全页图(兜底)
- 统计哪些 figure 成功升级为精裁图

注意:多图同页时(_1, _2, _3 编号)同样适用
"""
import re
from pathlib import Path

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
MD = ROOT / 'PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md'
FIG_DIR = ROOT / 'figures' / 'chapter_04'

# Match <img src="figures/chapter_04/fig_PPPP_NN.png" ...>
img_re = re.compile(r'(<img\s+src="figures/chapter_04/fig_(\d{4})_(\d+)\.png")(\s[^>]*>)')

def main():
    with open(MD) as f:
        text = f.read()

    upgraded = []   # (page, idx, old, new)
    kept = []       # (page, idx, old)

    def repl(m):
        old_src, page, idx, rest = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        tight_path = FIG_DIR / f'fig_{page:04d}_{idx}_tight.png'
        if tight_path.exists():
            # old_src ends with `.png"` (5 chars). Replace .png" with _tight.png"
            new_src = old_src[:-5] + '_tight.png"'
            upgraded.append((page, idx, old_src, new_src))
            return new_src + rest
        else:
            kept.append((page, idx, old_src))
            return m.group(0)

    new_text, n_subs = img_re.subn(repl, text)
    print(f"=== ch4 MD Image Reference Upgrade ===")
    print(f"Total <img> tags matched: {n_subs}")
    print(f"Upgraded to tight crops: {len(upgraded)}")
    print(f"Kept as full-page (no tight available): {len(kept)}")

    # Group by page
    by_page = {}
    for page, idx, old, new in upgraded:
        by_page.setdefault(page, []).append((idx, old, new))

    print(f"\n=== Upgraded pages ({len(by_page)} pages) ===")
    for page in sorted(by_page):
        items = by_page[page]
        print(f"  p.{page}: {len(items)} images")
        for idx, old, new in items:
            print(f"    {old.split('/')[-1]} → {new.split('/')[-1]}")

    if kept:
        print(f"\n=== Kept full-page (no tight crop) ===")
        seen = set()
        for page, idx, old in kept:
            key = (page, idx)
            if key in seen: continue
            seen.add(key)
            print(f"  p.{page} idx {idx}: {old.split('/')[-1]}")

    # Write back
    if n_subs > 0:
        with open(MD, 'w') as f:
            f.write(new_text)
        print(f"\n✓ File updated: {MD.name}")
    else:
        print(f"\nNo changes made.")


if __name__ == '__main__':
    main()
