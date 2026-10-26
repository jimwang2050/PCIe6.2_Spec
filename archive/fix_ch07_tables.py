#!/usr/bin/env python3
"""
Fix ch07 HTML table nesting issues:
1. Markdown table rows that appear INSIDE a <td> block (break rendering)
2. Orphan </td> tags that close a cell before the cell was opened
3. Extra unclosed <table> at end of file
"""
import re, glob

fname = 'PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md'
with open(fname, encoding='utf-8') as f:
    content = f.read()

original = content
lines = content.splitlines(keepends=True)

print(f"Original: {len(content)} bytes, {len(lines)} lines")

# ─── Strategy ─────────────────────────────────────────────────────────────────
# Find each <td> block that contains markdown table rows.
# The pattern: <td>...\n| header | ... (markdown table starts inside <td>)
# Fix: close </td> BEFORE the markdown table header row,
#      and start a new <td> after if there's trailing content.
#
# Pattern to detect:
#   <td ...>\n\n| Column1 | Column2 |   ← markdown table inside <td>
# ─────────────────────────────────────────────────────────────────────────────

fixed = 0
new_lines = []
i = 0

while i < len(lines):
    line = lines[i]

    # Check if this line starts a markdown table row inside a <td> block
    is_md_table_row = bool(re.match(r'^\|[^\n]+\|$', line.strip()))

    if is_md_table_row and i > 0:
        # Look back: is the previous non-empty line a <td> open tag?
        j = i - 1
        while j >= 0 and lines[j].strip() == '':
            j -= 1
        if j >= 0:
            prev = lines[j].strip()
            if prev.startswith('<td') or prev.startswith('</td>'):
                # We have: <td ...> or </td> on prev line,
                # and this line is a markdown table row.
                # Fix: insert </td> before this markdown row if prev is <td...>
                if prev.startswith('<td') and '<' in prev[3:]:
                    # It's an unclosed <td> — need to close it first
                    # Actually check: does the line BEFORE prev (j-1) close a td?
                    k = j - 1
                    while k >= 0 and lines[k].strip() == '':
                        k -= 1
                    if k >= 0 and '</td>' in lines[k]:
                        # There's a </td> before this <td>, so we need to close
                        # Insert </td> before the markdown table
                        new_lines.append('</td>\n')
                        fixed += 1
                        print(f"  Fixed: inserted </td> before markdown table at line {i+1}")
                    elif k < 0 or not re.search(r'</td>|<td', lines[k]):
                        # No previous td activity, safe to close
                        new_lines.append('</td>\n')
                        fixed += 1
                        print(f"  Fixed: inserted </td> before markdown table at line {i+1}")
                new_lines.append(line)
                i += 1
                continue

    # Check for orphan </td>: a </td> that appears without a preceding <td>
    if line.strip() == '</td>' and i > 0:
        # Scan backwards: find the last <td...> or </td>
        j = i - 1
        open_td = False
        while j >= 0:
            l = lines[j].strip()
            if l.startswith('<td'):
                open_td = True
                break
            if l.startswith('</td>') or l.startswith('<td') or l.startswith('<tr'):
                break
            j -= 1
        if not open_td:
            # Orphan </td> — skip it
            fixed += 1
            print(f"  Removed orphan </td> at line {i+1}")
            i += 1
            continue

    new_lines.append(line)
    i += 1

new_content = ''.join(new_lines)
print(f"\nFixed {fixed} issues")
print(f"New size: {len(new_content)} bytes")

if new_content != original:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Saved.")
else:
    print("No changes.")

# ─── Verify ────────────────────────────────────────────────────────────────
print("\n── Verification ──")
with open(fname, encoding='utf-8') as f:
    c = f.read()

for tag in ['<table>', '</table>', '<tr>', '</tr>', '<td>', '</td>', '<thead>', '</thead>', '<tbody>', '</tbody>']:
    print(f"  {tag}: {c.count(tag)}")

# Check for orphan </td> in context
orphan_count = 0
for i, line in enumerate(c.splitlines()):
    if line.strip() == '</td>':
        ctx_before = c.splitlines()[max(0,i-3):i]
        has_open_td = any(re.search(r'<td[^/]', l) for l in ctx_before)
        if not has_open_td:
            orphan_count += 1
            print(f"  Orphan </td> at line {i+1}")

print(f"\nOrphan </td> remaining: {orphan_count}")
