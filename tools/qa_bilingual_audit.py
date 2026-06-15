#!/usr/bin/env python3
"""
Refined bilingual row audit.

A bilingual row = a <tr> with exactly 2 <td> cells, where the second has
the gray-bg Chinese styling. We check if BOTH cells have meaningful content.
"""
import json
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def main():
    print("=" * 70)
    print("PCIe 6.2 — 真正的双语行审计 (Bilingual Row Audit)")
    print("=" * 70)
    print()
    grand_total = {'rows': 0, 'both_text': 0, 'en_only': 0, 'zh_only': 0,
                   'imbalanced': 0, 'both_empty': 0}

    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        # Find bilingual rows
        bilingual_rows = re.findall(
            r'<tr>\s*<td>(.*?)</td>\s*<td[^>]*background-color:#e8e8e8[^>]*>(.*?)</td>\s*</tr>',
            content, re.DOTALL
        )

        n_both = n_en = n_zh = n_imb = n_empty = 0
        for en, zh in bilingual_rows:
            en_text = re.sub(r'<[^>]+>', '', en).strip()
            zh_text = re.sub(r'<[^>]+>', '', zh).strip()
            if not en_text and not zh_text:
                n_empty += 1
            elif en_text and not zh_text:
                n_en += 1
            elif not en_text and zh_text:
                n_zh += 1
            else:
                n_both += 1
                if len(en_text) > 100 and len(zh_text) < 20:
                    n_imb += 1

        n_rows = len(bilingual_rows)
        completion = n_both / n_rows * 100 if n_rows else 0
        grand_total['rows'] += n_rows
        grand_total['both_text'] += n_both
        grand_total['en_only'] += n_en
        grand_total['zh_only'] += n_zh
        grand_total['imbalanced'] += n_imb
        grand_total['both_empty'] += n_empty

        marker = '✓' if n_en == 0 and n_imb == 0 else '⚠️'
        print(f"{marker} {name[:50]}")
        print(f"   双语行: {n_rows:>5}  |  完整: {n_both:>5} ({completion:.1f}%)  |  EN-only: {n_en:>3}  |  ZH-only: {n_zh:>3}  |  失衡: {n_imb:>3}")
        if n_en > 0 or n_imb > 0:
            print(f"   ⚠️  需要关注")
        print()

    print("=" * 70)
    print("总计")
    print("=" * 70)
    pct = grand_total['both_text'] / grand_total['rows'] * 100
    print(f"  双语行: {grand_total['rows']}")
    print(f"  完整翻译 (EN+ZH 都有): {grand_total['both_text']} ({pct:.2f}%)")
    print(f"  EN-only: {grand_total['en_only']}")
    print(f"  ZH-only: {grand_total['zh_only']}")
    print(f"  失衡 (EN>>ZH): {grand_total['imbalanced']}")
    print(f"  双空: {grand_total['both_empty']}")

    # Save
    with open(OUT_ROOT / 'qa_bilingual_report.json', 'w') as f:
        json.dump(grand_total, f, indent=2)


if __name__ == '__main__':
    main()
