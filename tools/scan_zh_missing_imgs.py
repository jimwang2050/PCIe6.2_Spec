#!/usr/bin/env python3
"""扫描 12 章中 ZH td 缺 img 的情况。"""
import re
from pathlib import Path
md_files = sorted(Path('.').glob('PCIe6.2_Spec_ch*_*.md'))
pair_re = re.compile(r'<tr>(?:(?!<table>).)*?</tr>', re.DOTALL)
for md in md_files:
    m = re.search(r'ch(\d{2})_', md.name)
    if not m: continue
    ch = int(m.group(1))
    with open(md) as f: s = f.read()
    pairs = pair_re.findall(s)
    zh_missing = 0
    examples = []
    for tr in pairs:
        if '<table>' in tr: continue
        m2 = re.search(r'<td>(.*?)</td>\s*<td style="background-color:#e8e8e8">(.*?)</td>', tr, re.DOTALL)
        if not m2: continue
        en, zh = m2.group(1), m2.group(2)
        en_imgs = len(re.findall(r'<img', en))
        zh_imgs = len(re.findall(r'<img', zh))
        if en_imgs > 0 and zh_imgs == 0 and len(re.sub(r'<[^>]+>', '', zh).strip()) > 10:
            zh_missing += 1
            if len(examples) < 3:
                en_clean = re.sub(r'<[^>]+>', ' ', en)[:80]
                zh_clean = re.sub(r'<[^>]+>', ' ', zh)[:80]
                examples.append(f'EN: {en_clean!r} | ZH: {zh_clean!r}')
    if zh_missing > 0:
        print(f'\nCh{ch:02d}: {zh_missing} ZH td missing imgs')
        for e in examples:
            print(f'  {e}')
