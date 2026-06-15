#!/usr/bin/env python3
"""
Cleanup pass for the new single-column format.

Fixes:
1. Remove duplicate figure blocks (same img, one EN one ZH caption) — keep EN
2. Remove stray </div> tags from removed overflow wrappers
3. Update H1 header text to reflect new format
4. Clean up extra blank lines
"""
import re
from pathlib import Path

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHAPTERS = sorted(OUT_ROOT.glob('PCIe6.2_Spec_ch*.md'))


def cleanup(content):
    n_figs_removed = 0

    # 1. Remove duplicate figure blocks
    # Pattern: > **Figure X-X.** English\n> <img src=...>\n\n followed by:
    #         > **Figure X-X.** 中文\n> <img src=...>
    # We want to remove the second (Chinese caption) block when both have same src.
    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        # Look for a Figure block start
        line = lines[i]
        if re.match(r'>\s*\*\*Figure\s+[\w\.\-]+\.\*\*', line):
            # Found a figure caption line
            # Check if next non-empty line is the img tag
            j = i + 1
            img_src = None
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines):
                m = re.search(r'<img\s+src="([^"]+)"', lines[j])
                if m:
                    img_src = m.group(1)
                    # Skip the img line
                    j += 1

            # Now check the NEXT figure block — if it has the same src, skip it
            if img_src:
                # Look ahead for next non-blank, non-closing-marker
                k = j
                while k < len(lines) and lines[k].strip() == '':
                    k += 1
                if k < len(lines) and re.match(r'>\s*\*\*Figure\s+[\w\.\-]+\.\*\*', lines[k]):
                    # Check if the line after this caption has the same src
                    m2 = re.search(r'<img\s+src="([^"]+)"', lines[k+1]) if k+1 < len(lines) else None
                    if m2 and m2.group(1) == img_src:
                        # This is a duplicate — skip the entire block (caption + img + blank)
                        # Skip: i (caption), j-1 (img), and continue
                        i = j  # i now points to line after our img
                        # Skip the duplicate
                        # Skip: k (caption), k+1 (img)
                        i = k + 2
                        n_figs_removed += 1
                        # Skip trailing blank lines
                        while i < len(lines) and lines[i].strip() == '':
                            i += 1
                        continue

            new_lines.append(line)
            i += 1
        else:
            new_lines.append(line)
            i += 1

    content = '\n'.join(new_lines)

    # 2. Remove stray </div> tags (orphans from removed overflow wrappers)
    content = re.sub(r'\n*</div>\s*\n*(\n+)*', '\n\n', content)

    # 3. Update H1 header to reflect new format
    content = re.sub(
        r'🎨 \*\*Format\*\*: 中英对照双语 · 图表原始保留 · 中文背景色灰色',
        '🎨 **Format**: 中英对照双语 · 表格单列 (EN + ZH 上下) · 中文背景色灰色',
        content
    )

    # 4. Clean up extra blank lines (3+ → 2)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # 5. Remove stray <th> gray bg that was left over
    content = re.sub(
        r'<th[^>]*style="background-color:#e8e8e8"[^>]*>',
        '<th>',
        content,
    )

    return content, n_figs_removed


def main():
    for ch in CHAPTERS:
        name = ch.stem
        content = ch.read_text()
        new_content, n_figs = cleanup(content)
        if new_content != content:
            ch.write_text(new_content)
            print(f"📄 {name[:50]}: {n_figs} duplicate figures removed")
        else:
            print(f"✓ {name[:50]}: no change")


if __name__ == '__main__':
    main()
