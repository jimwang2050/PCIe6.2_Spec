#!/usr/bin/env python3
"""Fix each chapter's 📑 TOC: add [Title](#anchor) links to table cells.

Columns: | # | Section | 小节 | Page |
- Empty leading | makes section number land in cols[1]
"""
import re, glob

files = sorted(glob.glob('PCIe6.2_Spec_ch*.md'))
grand_added = 0

for fname in files:
    with open(fname, encoding='utf-8') as f:
        content = f.read()

    ch_match = re.search(r'ch(\d+)', fname)
    if not ch_match:
        continue
    ch = ch_match.group(1)

    defined = set(re.findall(r'<a id="([^"]+)"', content))

    toc_start = content.find('## 📑 章节索引 (Sections)')
    if toc_start < 0:
        print(f"ch{ch:>2}: NO TOC")
        continue

    next_h = content.find('\n## ', toc_start + 10)
    toc_end = next_h if next_h > 0 else len(content)
    toc_body = content[toc_start:toc_end]
    lines = toc_body.splitlines(keepends=True)

    new_lines = []
    added = 0
    missing_anchors = []

    for line in lines:
        stripped = line.strip()
        # Table data rows: start with | followed by section number pattern
        if not re.match(r'^\|\s*\d+\.\d+', stripped):
            new_lines.append(line)
            continue

        # Parse: | (empty) | sec_num | en_title | zh_title | page |
        cols = [c.strip() for c in line.rstrip().rstrip('|').split('|')]
        if len(cols) < 3:
            new_lines.append(line)
            continue

        sec_num  = cols[1].strip()   # cols[0]=empty, cols[1]=#/section_num
        en_title = cols[2].strip() if len(cols) > 2 else ''
        zh_title = cols[3].strip() if len(cols) > 3 else ''
        page_col = cols[4].strip() if len(cols) > 4 else '—'

        # Skip separator rows like |:-:|...|
        if re.match(r'[:\-\s|]+', sec_num) or not sec_num or sec_num == '#':
            new_lines.append(line)
            continue

        anchor = 'sec-' + sec_num.replace('.', '-')

        # If anchor missing, try to add it to the corresponding heading
        if anchor not in defined:
            body_after = content[toc_end:]
            for hm in re.finditer(
                rf'^(#{1,3})\s+{re.escape(sec_num)}[\s\.]+([^\n|]{{3,80}})\|',
                body_after, re.MULTILINE
            ):
                h_pos = toc_end + hm.start()
                check = content[max(0, h_pos-30):h_pos+10]
                if f'<a id="{anchor}"></a>' not in check:
                    content = content[:h_pos] + f'<a id="{anchor}"></a>\n' + content[h_pos:]
                    defined.add(anchor)
                    toc_end += len(f'<a id="{anchor}"></a>\n')
                    break
            else:
                missing_anchors.append((sec_num, en_title[:30], anchor))
                new_lines.append(line)
                continue

        en_link = f'[{en_title}](#{anchor})'
        zh_link = f'[{zh_title}](#{anchor})'
        new_lines.append(f'|  | {sec_num} | {en_link} | {zh_link} | {page_col} |\n')
        added += 1

    new_content = content[:toc_start] + ''.join(new_lines) + content[toc_end:]

    if added > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"ch{ch:>2}: +{added} links", end='')
        if missing_anchors:
            print(f", {len(missing_anchors)} missing anchors (skipped)", end='')
            for s, t, a in missing_anchors[:2]:
                print(f"\n        {s}: {t[:25]} -> {a}", end='')
        print()
        grand_added += added
    else:
        print(f"ch{ch:>2}: no changes")

print(f"\nTotal: +{grand_added} TOC links added")
