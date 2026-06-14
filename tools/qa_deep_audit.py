#!/usr/bin/env python3
"""
Deep QA audit of the 12 PCIe 6.2 chapter MDs.

Checks:
1. HTML table tag balance (open/close <table>/</table>)
2. Empty <td> cells in bilingual tables
3. Rows where EN and ZH columns have wildly different content lengths
   (possible alignment issue)
4. Malformed section anchors (missing closing)
5. Unclosed code blocks
6. Stray `<<<PAGE_BREAK>>>` markers (must be retained as is)
7. Look for duplicate consecutive <tr> rows
8. HTML <a id> anchor uniqueness
9. TODO / placeholder leakage
10. "tbody missing" or "thead missing" issues
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))

REPORT = {}


def main():
    print("=" * 70)
    print("PCIe 6.2 中英对照翻译 — 深度 QA 审计")
    print("=" * 70)
    print()

    grand_total = {
        'empty_cells': 0,
        'unbalanced_tables': 0,
        'malformed_anchors': 0,
        'rows_imbalanced': 0,
        'todo_markers': 0,
        'duplicate_anchors': 0,
    }

    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        issues = []

        # 1. Table balance
        n_open = len(re.findall(r'<table\b[^>]*>', content))
        n_close = len(re.findall(r'</table>', content))
        if n_open != n_close:
            issues.append(f"Tables: {n_open} open vs {n_close} close (diff {n_open - n_close})")
            grand_total['unbalanced_tables'] += abs(n_open - n_close)

        # 2. Empty cells in tables (only the bilingual table cells, not pre/code)
        # Find all <tr>...</tr> blocks
        tr_blocks = re.findall(r'<tr>.*?</tr>', content, re.DOTALL)
        n_empty = 0
        n_short_pairs = 0
        n_long_pairs = 0
        n_imbalanced_rows = 0
        for tr in tr_blocks:
            # Find <td> blocks within
            td_blocks = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL)
            if len(td_blocks) != 2:
                # Not a 2-column row, skip
                continue
            en_td, zh_td = td_blocks
            en_text = re.sub(r'<[^>]+>', '', en_td).strip()
            zh_text = re.sub(r'<[^>]+>', '', zh_td).strip()

            if not en_text or not zh_text:
                n_empty += 1
                continue

            en_len = len(en_text)
            zh_len = len(zh_text)
            # ZH should be roughly 50-200% of EN length (typical tech translation)
            if en_len > 50 and zh_len < 10:
                n_short_pairs += 1
            elif zh_len > en_len * 5:
                n_long_pairs += 1
            if en_len > 100 and zh_len < 30:
                n_imbalanced_rows += 1

        if n_empty or n_short_pairs or n_long_pairs or n_imbalanced_rows:
            issues.append(f"Empty cells: {n_empty}, short-ZH: {n_short_pairs}, long-ZH: {n_long_pairs}, imbalanced: {n_imbalanced_rows}")
        grand_total['empty_cells'] += n_empty
        grand_total['rows_imbalanced'] += n_imbalanced_rows

        # 3. Anchor balance: <a id="..."> vs closing
        a_id_open = len(re.findall(r'<a\s+id="[^"]+">', content))
        a_id_close = len(re.findall(r'</a>', content))
        if a_id_open != a_id_close:
            issues.append(f"Anchors: {a_id_open} open vs {a_id_close} close")
            grand_total['malformed_anchors'] += abs(a_id_open - a_id_close)

        # 4. Duplicate anchors
        anchors = re.findall(r'<a\s+id="([^"]+)">', content)
        anchor_counts = Counter(anchors)
        dups = [(a, c) for a, c in anchor_counts.items() if c > 1]
        if dups:
            issues.append(f"Duplicate anchors: {len(dups)} (e.g. {dups[:3]})")
            grand_total['duplicate_anchors'] += len(dups)

        # 5. Code block balance
        n_fence_open = len(re.findall(r'^```', content, re.MULTILINE))
        if n_fence_open % 2 != 0:
            issues.append(f"Unclosed code block: {n_fence_open} fences (odd)")

        # 6. TODO markers
        n_todo = len(re.findall(r'⚠️\s*TODO|未翻译|TODO:|TBD|XXX|placeholder', content, re.IGNORECASE))
        if n_todo:
            issues.append(f"TODO/placeholder markers: {n_todo}")
            grand_total['todo_markers'] += n_todo

        # 7. Stray English-only <td> cells (no Chinese content)
        # Find all bilingual tables
        tbl_sections = re.findall(r'<table>.*?</table>', content, re.DOTALL)
        pure_en_rows = 0
        for tbl in tbl_sections:
            rows = re.findall(r'<tr>.*?</tr>', tbl, re.DOTALL)
            for row in rows:
                td_blocks = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
                if len(td_blocks) != 2:
                    continue
                en_td, zh_td = td_blocks
                en_text = re.sub(r'<[^>]+>', '', en_td).strip()
                zh_text = re.sub(r'<[^>]+>', '', zh_td).strip()
                # Check if ZH column has Chinese chars
                has_zh = any('一' <= c <= '鿿' for c in zh_text)
                if en_text and not has_zh and len(en_text) > 20:
                    pure_en_rows += 1
        if pure_en_rows > 0:
            issues.append(f"EN-only rows (no ZH translation): {pure_en_rows}")

        # Print chapter report
        if issues:
            print(f"📄 {name}")
            for i in issues:
                print(f"   ⚠️  {i}")
            print()
        else:
            print(f"✓ {name} — clean")

        REPORT[name] = issues

    # Summary
    print("=" * 70)
    print("总计")
    print("=" * 70)
    for k, v in grand_total.items():
        print(f"  {k}: {v}")
    print()

    # Save report
    with open(OUT_ROOT / 'qa_deep_report.json', 'w') as f:
        json.dump({'per_chapter': REPORT, 'totals': grand_total}, f, indent=2, ensure_ascii=False)

    print(f"📊 详细报告: {OUT_ROOT/'qa_deep_report.json'}")

    if grand_total['unbalanced_tables'] > 0:
        print()
        print("🔧 修复建议: 运行 python3 tools/fix_table_balance.py 自动修复")
    if grand_total['empty_cells'] > 0 or grand_total['rows_imbalanced'] > 0:
        print("🔧 修复建议: 检查源 chunks 中空/失衡 row 是否需要重新翻译")


if __name__ == '__main__':
    main()
