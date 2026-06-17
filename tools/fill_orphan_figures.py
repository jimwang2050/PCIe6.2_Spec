#!/usr/bin/env python3
"""
为每章补全 figure img 引用

策略:
1. 加载 ch{N}_tight_crops.json (figure → page/file)
2. 扫描 MD 中所有 Figure X-NN 引用
3. 找出 MD 中已引用但缺 img 的 figure
4. 找最接近 figure caption 的位置,插入 img

注意: 不破坏现有结构,只在 caption 下方追加 img
"""
import re
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('.')
CHAPTERS = range(1, 13)


def load_map(ch):
    f = ROOT / ('ch4_tight_crops.json' if ch == 4 else f'ch{ch}_tight_crops.json')
    if not f.exists():
        return None
    with open(f) as fp:
        return json.load(fp)


def build_fig_index(ch, ch_map):
    """Build: figure_num → (page, file, caption)"""
    idx = {}
    if not ch_map:
        return idx
    for k, v in ch_map['figures'].items():
        m = re.match(r'Figure (\d+)-(\d+)', k)
        if m:
            fnum = int(m.group(2))
            idx[fnum] = (v.get('page'), v.get('file'), v.get('caption', ''))
    return idx


def find_orphan_figures(ch, md_text, fig_idx):
    """Find figure numbers referenced in text but with no img."""
    # Find all Figure X-NN references
    refs = re.findall(r'Figure (\d+)-(\d+)', md_text)
    ch_refs = set(int(n) for c, n in refs if int(c) == ch)
    # Find all imgs and what figure they correspond to
    img_re = re.compile(r'<img\s+src="figures/chapter_\d+/fig_(\d{4})_(\d+)(?:_tight)?\.png"')
    img_figs = set()
    for m in img_re.finditer(md_text):
        page = int(m.group(1))
        idx = int(m.group(2))
        # Find the figure num for (page, idx)
        for fnum, (p, f, c) in fig_idx.items():
            if p == page:
                m2 = re.match(r'fig_(\d+)_(\d+)', f)
                if m2 and int(m2.group(2)) == idx:
                    img_figs.add(fnum)
                    break
    orphans = ch_refs - img_figs
    return orphans


def insert_orphan_imgs(ch, md_path, fig_idx):
    """Find and insert imgs for orphan figures."""
    with open(md_path) as f:
        text = f.read()
    orphans = find_orphan_figures(ch, text, fig_idx)
    if not orphans:
        return 0, []

    # For each orphan, find the best location to insert the img
    lines = text.split('\n')
    insertions = []  # (line_idx, content_to_insert, fig_num)
    used_lines = set()

    for fnum in sorted(orphans):
        if fnum not in fig_idx:
            continue
        page, fname, caption = fig_idx[fnum]
        # Find the line with this figure's caption (English or Chinese)
        # Pattern: "**Figure X-NN.**" or "**图 X-NN"
        cap_patterns = [
            rf'\*\*Figure {ch}-{fnum}\.\*\*',
            rf'\*\*Figure {ch}-{fnum}\*\*',
            rf'\*\*图\s*{ch}-{fnum}',
        ]
        for i, line in enumerate(lines):
            if i in used_lines:
                continue
            for pat in cap_patterns:
                if re.search(pat, line):
                    insertions.append((i + 1, fname, fnum, caption))
                    used_lines.add(i)
                    break
            else:
                continue
            break

    # Apply insertions in reverse order (to keep line numbers stable)
    for line_idx, fname, fnum, caption in sorted(insertions, reverse=True):
        img_line = f'\n> <img src="figures/chapter_{ch:02d}/{fname}" width="700">\n'
        lines.insert(line_idx, img_line)

    if insertions:
        with open(md_path, 'w') as f:
            f.write('\n'.join(lines))

    return len(insertions), [f for _, _, f, _ in insertions]


def main():
    total = 0
    for ch in CHAPTERS:
        ch_map = load_map(ch)
        fig_idx = build_fig_index(ch, ch_map)
        md = next(ROOT.glob(f'PCIe6.2_Spec_ch{ch:02d}_*.md'), None)
        if not md:
            continue
        n_inserted, figs = insert_orphan_imgs(ch, md, fig_idx)
        print(f'Ch{ch:02d}: inserted {n_inserted} imgs for figures {figs}')
        total += n_inserted
    print(f'\nTotal: {total} imgs inserted')


if __name__ == '__main__':
    main()
