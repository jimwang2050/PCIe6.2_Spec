#!/usr/bin/env python3
"""
通用化: 将章节 MD 文件中所有 <img src=".../fig_PPPP_NN.png">
替换为 <img src=".../fig_PPPP_NN_tight.png"> (如果 _tight.png 存在)

支持任意章节,通过命令行参数指定: python3 chx_apply_tight.py 5
或批量: python3 chx_apply_tight.py 1-12
"""
import re
import sys
from pathlib import Path

ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')


def get_chapter_files(ch_num):
    """Find MD and figures dir for a chapter."""
    mds = list(ROOT.glob(f'PCIe6.2_Spec_ch{ch_num:02d}_*.md'))
    if not mds:
        return None, None
    fig_dir = ROOT / 'figures' / f'chapter_{ch_num:02d}'
    return mds[0], fig_dir


def apply(ch_num):
    md, fig_dir = get_chapter_files(ch_num)
    if not md:
        print(f"Ch{ch_num}: MD not found, skip")
        return
    if not fig_dir.exists():
        print(f"Ch{ch_num}: figures dir not found, skip")
        return

    with open(md) as f:
        text = f.read()

    # Match both _tight and non-tight variants to find non-tight and upgrade
    img_re = re.compile(
        r'(<img\s+src="figures/chapter_\d{2,3}/fig_(\d{4})_(\d+))(\.png")(\s[^>]*>)'
    )

    upgraded = []
    kept = []

    def repl(m):
        prefix, page, idx, suffix, rest = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4), m.group(5)
        tight_path = fig_dir / f'fig_{page:04d}_{idx}_tight.png'
        if tight_path.exists():
            # Add _tight before .png"
            new_src = prefix + '_tight' + suffix
            upgraded.append((page, idx))
            return new_src + rest
        else:
            kept.append((page, idx))
            return m.group(0)

    new_text, n = img_re.subn(repl, text)
    print(f"Ch{ch_num:02d} ({md.name}): {n} <img> matched, {len(upgraded)} upgraded, {len(kept)} kept full-page")

    if n > 0 and upgraded:
        with open(md, 'w') as f:
            f.write(new_text)


def main():
    args = sys.argv[1:] or ['1-12']
    chs = []
    for arg in args:
        if '-' in arg:
            s, e = arg.split('-')
            chs.extend(range(int(s), int(e)+1))
        elif ',' in arg:
            chs.extend(int(x) for x in arg.split(',') if x.strip().isdigit())
        else:
            chs.append(int(arg))
    for c in chs:
        apply(c)


if __name__ == '__main__':
    main()
