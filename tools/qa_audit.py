#!/usr/bin/env python3
"""
QA audit on the merged PCIe 6.2 chapter MDs.

Checks:
1. HTML table balance (open/close tags)
2. Gray-bg Chinese cells (`style="background-color:#e8e8e8"`)
3. Glossary term frequency
4. ZH/EN character ratio per chapter
5. Section anchors
6. Empty/untranslated rows
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))
GLOSSARY_PATH = OUT_ROOT / 'glossary.json'


def main():
    print("=" * 70)
    print("PCIe 6.2 Spec 中英对照翻译 — QA 审计报告")
    print("=" * 70)
    print()

    # Load glossary for term check
    with open(GLOSSARY_PATH) as f:
        glossary = json.load(f)
    key_terms = [
        'Root Complex', 'Switch', 'Endpoint', 'TLP', 'DLLP', 'Flit',
        'BAR', 'VC', 'TC', 'Power Management', 'Hot-Plug',
        'Configuration Space', 'Memory Space', 'Completion',
        'PCI Express', 'PCIe', 'Gen5', 'Gen6', 'LTSSM', 'PAM4',
        'Forward Error Correction', 'FEC', 'Replay', 'NAK', 'ACK',
        'Physical Layer', 'Data Link Layer', 'Transaction Layer',
        'Flow Control', 'Posted', 'Non-Posted', 'MSI', 'MSI-X',
        'ARI', 'SR-IOV', 'PF', 'VF', 'ATS', 'IOMMU', 'PRI',
        'TDISP', 'TEE', 'IDE', 'Retimer', 'Interposer',
    ]

    summary = []
    total_open = 0
    total_close = 0
    total_gray = 0
    total_imgs = 0

    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()

        # Counts
        n_open_table = len(re.findall(r'<table\b', content))
        n_close_table = len(re.findall(r'</table>', content))
        n_gray = len(re.findall(r'background-color:#e8e8e8', content))
        n_imgs = len(re.findall(r'<img\s+src=', content))
        n_sections = len(re.findall(r'<a id="sec-', content))
        n_anchors_back = len(re.findall(r'\[⬆️ 返回目录\]', content))

        # ZH chars
        zh_chars = sum(1 for c in content if '一' <= c <= '鿿')
        en_chars = sum(1 for c in content if c.isalpha() and ord(c) < 128)
        total_chars = len(content)
        zh_pct = zh_chars / total_chars * 100

        # Empty rows (placeholder rows)
        n_empty = len(re.findall(r'<tr>\s*<td></td>\s*<td[^>]*></td>\s*</tr>', content))

        # TODO markers
        n_todo = len(re.findall(r'⚠️\s*TODO', content))

        total_open += n_open_table
        total_close += n_close_table
        total_gray += n_gray
        total_imgs += n_imgs

        balance = '✓' if n_open_table == n_close_table else '✗ MISMATCH'

        summary.append({
            'ch': name,
            'tables_open': n_open_table,
            'tables_close': n_close_table,
            'gray_cells': n_gray,
            'imgs': n_imgs,
            'sections': n_sections,
            'zh_chars': zh_chars,
            'en_chars': en_chars,
            'zh_pct': zh_pct,
            'todo': n_todo,
            'empty': n_empty,
        })

        print(f"📄 {name}")
        print(f"   文件大小:     {total_chars:>9,} chars")
        print(f"   中文字符:     {zh_chars:>9,} ({zh_pct:.1f}%)")
        print(f"   英文字符:     {en_chars:>9,}")
        print(f"   Section 锚点: {n_sections:>9,}")
        print(f"   <table> 开:   {n_open_table:>9,}")
        print(f"   </table> 闭:  {n_close_table:>9,}  {balance}")
        print(f"   灰底中文单元: {n_gray:>9,}")
        print(f"   图片引用:     {n_imgs:>9,}")
        print(f"   TODO 标记:    {n_todo:>9,}")
        if n_todo > 0:
            print(f"   ⚠️  有未翻译段")
        print()

    # Term frequency
    print("=" * 70)
    print("关键术语频次 (跨 12 章)")
    print("=" * 70)
    all_content = ''.join(ch.read_text() for ch in CHAPTERS)
    term_counts = []
    for term in key_terms:
        c = all_content.count(term)
        term_counts.append((term, c))
    term_counts.sort(key=lambda x: -x[1])
    for term, c in term_counts:
        bar = '█' * min(50, c // 10)
        print(f"  {term:30s} {c:>5}  {bar}")
    print()

    # Total summary
    print("=" * 70)
    print("总计 (12 章合计)")
    print("=" * 70)
    print(f"  章节数:         12")
    print(f"  <table> 平衡:   {total_open} 开 / {total_close} 闭 {'✓' if total_open == total_close else '✗'}")
    print(f"  灰底中文单元:   {total_gray:,}")
    print(f"  图片引用:       {total_imgs:,}")
    print(f"  中文字符:       {sum(s['zh_chars'] for s in summary):,}")
    print(f"  英文字符:       {sum(s['en_chars'] for s in summary):,}")
    total = sum(s['zh_chars'] + s['en_chars'] for s in summary)
    zh_total = sum(s['zh_chars'] for s in summary)
    print(f"  ZH/(ZH+EN) 比:  {zh_total/total*100:.1f}%")
    print()

    # Save report
    with open(OUT_ROOT / 'qa_report.json', 'w') as f:
        json.dump({
            'summary': summary,
            'term_counts': dict(term_counts),
            'totals': {
                'tables_open': total_open,
                'tables_close': total_close,
                'tables_balanced': total_open == total_close,
                'gray_cells': total_gray,
                'image_refs': total_imgs,
                'zh_chars': zh_total,
                'en_chars': sum(s['en_chars'] for s in summary),
                'zh_pct': zh_total / total * 100,
            }
        }, f, indent=2, ensure_ascii=False)

    print(f"📊 详细报告已保存: {OUT_ROOT/'qa_report.json'}")


if __name__ == '__main__':
    main()
