#!/usr/bin/env python3
"""
为 ch01-ch12 生成 CXL 3.2 风格的索引表

输出:
- Section | 小节 | Page 索引表
- Figure | Title | 图标题 | Page 索引表
- Table | Title | 表标题 | Page 索引表

从 MD 文件中提取:
- 章节标题 (## N.X, ### N.X.X)
- Figure 标题 (> **Figure X-NN.** ...)
- Table 标题 (> **Table X-NN.** ...)
- 页面标记 (<!-- 📄 Page NNN -->)
"""
import re
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('.')
CHAPTERS = range(1, 13)

# 抓取页面标记的位置, 用于计算每个元素的 page
def extract_page_markers(text):
    """Find page markers and their line numbers."""
    lines = text.split('\n')
    markers = []  # (line_idx, page_num)
    for i, line in enumerate(lines):
        m = re.search(r'<!--\s*📄\s*Page\s*(\d+)\s*-->', line)
        if m:
            markers.append((i, int(m.group(1))))
    return markers


def page_of_line(line_idx, page_markers):
    """Find page number for a given line index."""
    page = 0
    for marker_line, page_num in page_markers:
        if marker_line <= line_idx:
            page = page_num
        else:
            break
    return page


def extract_indexes(ch):
    md = next(ROOT.glob(f'PCIe6.2_Spec_ch{ch:02d}_*.md'), None)
    if not md:
        return None
    with open(md) as f: text = f.read()
    lines = text.split('\n')

    page_markers = extract_page_markers(text)

    sections = []  # (sec_id, sec_title_en, sec_title_zh, page)
    figures = []  # (fig_num, title_en, title_zh, page)
    tables = []   # (tbl_num, title_en, title_zh, page)

    for i, line in enumerate(lines):
        # Section headings ## N.X or ### N.X.X
        m = re.match(r'^##+ (\d+\.\d+(?:\.\d+)*)\s+(.+)$', line)
        if m:
            sec_id = m.group(1)
            sec_title_full = m.group(2)
            if ' | ' in sec_title_full:
                en, zh = sec_title_full.split(' | ', 1)
            else:
                en = sec_title_full
                zh = ''
            # Filter only ch X.Y for the current chapter
            if sec_id.startswith(f'{ch}.'):
                page = page_of_line(i, page_markers)
                sections.append((sec_id, en.strip(), zh.strip(), page))
        # Figure titles
        m = re.match(r'^>\s*\*\*Figure\s+(\d+)-(\d+)\.\*\*\s*(.+?)\*?\*?\s*$', line)
        if m:
            ch_n = int(m.group(1))
            fnum = int(m.group(2))
            title_en = m.group(3).strip()
            if ch_n == ch:
                page = page_of_line(i, page_markers)
                title_zh = ''
                # Look in next 10 lines for combined or separate Chinese title
                for j in range(i+1, min(len(lines), i+10)):
                    m2 = re.match(r'^>\s*\*\*图\s*\d+-\d+\s*(.+?)\*?\*?\s*$', lines[j])
                    if m2:
                        title_zh = m2.group(1).strip()
                        break
                    # Combined: **Figure X-NN | 图 X-NN**: 中文title (...)
                    m3 = re.match(r'^\*\*Figure\s+\d+-\d+\s*\|\s*图\s*\d+-\d+\*\*\s*[:：]?\s*(.+)', lines[j])
                    if m3:
                        title_zh = m3.group(1).strip()
                        # Remove trailing parenthetical English
                        title_zh = re.sub(r'\s*\([^)]*\)\s*$', '', title_zh)
                        break
                figures.append((fnum, title_en, title_zh, page))
        # Table titles - multiple formats
        # Format 1: > **Table X-NN.** English title (block quote)
        m = re.match(r'^>\s*\*\*Table\s+(\d+)-(\d+)\.\*\*\s*(.+?)\*?\*?\s*$', line)
        # Format 2: **Table X-NN. Title | 表 X-NN. 中文** (combined, plain)
        m2 = re.match(r'^\*\*Table\s+(\d+)-(\d+)\.\s+(.+?)\*\*\s*$', line)
        # Format 3: **表 X-NN 中文** standalone
        m3 = re.match(r'^\*\*表\s*(\d+)-(\d+)\s+(.+?)\*\*\s*$', line)
        if m and not m.group(3).startswith('|'):
            ch_n = int(m.group(1))
            tnum = int(m.group(2))
            title_en = m.group(3).strip()
            if ch_n == ch:
                page = page_of_line(i, page_markers)
                title_zh = ''
                # Look for combined or separate Chinese title
                for j in range(i+1, min(len(lines), i+5)):
                    m4 = re.match(r'^\*\*表\s*\d+-\d+\s*(.+?)\*\*\s*$', lines[j])
                    if m4:
                        title_zh = m4.group(1).strip()
                        break
                tables.append((tnum, title_en, title_zh, page))
        elif m2:
            ch_n = int(m2.group(1))
            tnum = int(m2.group(2))
            # Split title by |
            full_title = m2.group(3)
            if ' | ' in full_title:
                en, zh = full_title.split(' | ', 1)
                en = en.strip()
                zh = re.sub(r'^表\s*\d+-\d+\.\s*', '', zh).strip()
            else:
                en = full_title
                zh = ''
            if ch_n == ch:
                page = page_of_line(i, page_markers)
                tables.append((tnum, en, zh, page))
        elif m3:
            ch_n = int(m3.group(1))
            tnum = int(m3.group(2))
            title_zh = m3.group(3).strip()
            if ch_n == ch:
                page = page_of_line(i, page_markers)
                # Look for English in adjacent line
                title_en = ''
                for j in range(max(0, i-2), min(len(lines), i+3)):
                    m4 = re.match(r'^\*\*Table\s+\d+-\d+\.\s+(.+?)(?:\s*\|\s*表\s*\d+-\d+\.)?', lines[j])
                    if m4:
                        title_en = m4.group(1).strip()
                        break
                tables.append((tnum, title_en, title_zh, page))

    return sections, figures, tables


def format_section_table(sections):
    """Generate CXL 3.2 style section index table."""
    if not sections:
        return ''
    lines = [
        '| # | Section | 小节 | Page |',
        '|:-:|:--------|:-----|:----:|',
    ]
    for sec_id, en, zh, page in sections:
        page_str = f'p.{page}' if page else '—'
        zh_short = zh[:30] + '…' if len(zh) > 30 else zh
        en_short = en[:35] + '…' if len(en) > 35 else en
        lines.append(f'| {sec_id} | {en_short} | {zh_short} | {page_str} |')
    return '\n'.join(lines)


def format_figure_table(figures):
    """Generate CXL 3.2 style figure index table."""
    if not figures:
        return ''
    lines = [
        '| Figure | Title | 图标题 | Page |',
        '|:------:|:------|:-------|:----:|',
    ]
    for fnum, en, zh, page in figures:
        page_str = f'p.{page}' if page else '—'
        en_short = en[:30] + '…' if len(en) > 30 else en
        zh_short = zh[:30] + '…' if len(zh) > 30 else zh
        lines.append(f'| {fnum} | {en_short} | {zh_short} | {page_str} |')
    return '\n'.join(lines)


def format_table_table(tables):
    """Generate CXL 3.2 style table index table."""
    if not tables:
        return ''
    lines = [
        '| Table | Title | 表标题 | Page |',
        '|:-----:|:------|:-------|:----:|',
    ]
    for tnum, en, zh, page in tables:
        page_str = f'p.{page}' if page else '—'
        en_short = en[:30] + '…' if len(en) > 30 else en
        zh_short = zh[:30] + '…' if len(zh) > 30 else zh
        lines.append(f'| {tnum} | {en_short} | {zh_short} | {page_str} |')
    return '\n'.join(lines)


def insert_indexes(ch, sections, figures, tables):
    """Insert index tables into MD file."""
    md = next(ROOT.glob(f'PCIe6.2_Spec_ch{ch:02d}_*.md'), None)
    with open(md) as f: text = f.read()

    sec_tbl = format_section_table(sections)
    fig_tbl = format_figure_table(figures)
    tbl_tbl = format_table_table(tables)

    new_section = ''
    if sec_tbl:
        new_section += '\n## 📑 章节索引 (Sections)\n\n' + sec_tbl + '\n'
    if fig_tbl:
        new_section += '\n## 🖼 本章图表 (Figures)\n\n' + fig_tbl + '\n'
    if tbl_tbl:
        new_section += '\n## 📊 本章表格 (Tables)\n\n' + tbl_tbl + '\n'

    lines = text.split('\n')
    # Find first TOC-style heading
    toc_start = None
    for i, line in enumerate(lines):
        if line.startswith('## 📑 本章目录') or line.startswith('## 📑 章节索引'):
            toc_start = i
            break
    if toc_start is None:
        return False
    # Find end: next '---' that is followed by '# ' or '## '
    toc_end = None
    for i in range(toc_start, len(lines)):
        if lines[i].strip() == '---':
            # Check if next non-blank is a chapter heading
            for j in range(i+1, min(len(lines), i+5)):
                if lines[j].strip().startswith('# '):
                    toc_end = i
                    break
            if toc_end is not None:
                break
    if toc_end is None:
        return False
    # Replace
    before = '\n'.join(lines[:toc_start])
    after = '\n'.join(lines[toc_end:])
    new_text = before.rstrip() + '\n\n' + new_section + '\n---\n\n' + after
    with open(md, 'w') as f: f.write(new_text)
    return True


def main():
    for ch in CHAPTERS:
        result = extract_indexes(ch)
        if not result:
            print(f'Ch{ch:02d}: skipped')
            continue
        sections, figures, tables = result
        ok = insert_indexes(ch, sections, figures, tables)
        print(f'Ch{ch:02d}: {len(sections)} sections, {len(figures)} figs, {len(tables)} tables. Insert: {"OK" if ok else "FAIL"}')


if __name__ == '__main__':
    main()
