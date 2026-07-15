#!/usr/bin/env python3
"""
Fix ch07: remove orphaned </td> tags that appear immediately before
markdown table header rows (a leftover from the HTML→Markdown migration).
"""
import re, subprocess

content = subprocess.check_output(
    ['git', 'show', 'HEAD:PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md']
).decode('utf-8')

# First apply the two targeted fixes from fix_ch07_table.py
# Fix 1: orphan </td> and empty <td> before ZH markdown table (Table 7-19)
old1 = (
    "\n<sup>163</sup>. This field would be better named 'Function Type' "
    "but for historical reasons is named Device/Port Type.\n\n"
    "</td>\n"
    '<td style="background-color:#e8e8e8">\n'
)
new1 = (
    "\n<sup>163</sup>. This field would be better named 'Function Type' "
    "but for historical reasons is named Device/Port Type.\n"
)
content = content.replace(old1, new1, 1)

# Fix 2: orphan </td></tr> after ZH footnote (Table 7-19)
old2 = (
    "\n<sup>163</sup>. 该字段本应更好地命名为 \"Function Type\"，"
    "但出于历史原因被命名为 Device/Port Type。\n\n"
    "</td>\n"
    "</tr>"
)
new2 = (
    "\n<sup>163</sup>. 该字段本应更好地命名为 \"Function Type\"，"
    "但出于历史原因被命名为 Device/Port Type。\n"
)
content = content.replace(old2, new2, 1)

# Fix 3: orphan </tbody></table> after ZH footnote
old3 = "\n</tbody>\n</table>\n\n[⬆️ 返回目录]"
new3 = "\n\n[⬆️ 返回目录]"
content = content.replace(old3, new3, 1)

# Fix 4: remove ALL orphan </td> tags that appear immediately before
#         a markdown table header row (| ... | ... |)
# Strategy: split by lines, scan for pattern:
#   line = '</td>' AND next_nonempty_line matches markdown table row
lines = content.splitlines(keepends=True)
new_lines = []
i = 0
fixed = 0

while i < len(lines):
    line = lines[i]
    new_lines.append(line)

    if line.strip() == '</td>' and i + 1 < len(lines):
        # Look ahead for next non-empty line
        j = i + 1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        if j < len(lines) and re.match(r'^\|[^\n]+\|$', lines[j].strip()):
            # This </td> is orphan - skip it (don't add it)
            new_lines.pop()  # remove the </td> we just added
            fixed += 1
            # Also skip any empty lines between </td> and the table
            while i + 1 < len(lines) and lines[i+1].strip() == '':
                i += 1
    i += 1

new_content = ''.join(new_lines)
print(f"Orphan </td> removed: {fixed}")

if fixed > 0:
    # Write
    with open('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    content = new_content

# Final verification
print("\nFinal counts:")
for tag in ['<table>', '</table>', '<tr>', '</tr>', '<td>', '</td>', '<tbody>', '</tbody>']:
    print(f"  {tag}: {content.count(tag)}")

# Check nesting
depth_map = {'table': 0, 'tr': 0, 'td': 0, 'th': 0, 'thead': 0, 'tbody': 0}
issues = []
for i, line in enumerate(content.splitlines()):
    for tag in depth_map:
        opens = len(re.findall(rf'<{tag}[ \->]', line))
        closes = line.count(f'</{tag}>')
        depth_map[tag] += opens - closes
        if depth_map[tag] < 0:
            issues.append((i+1, tag, repr(line[:50])))
            depth_map[tag] = 0

print(f"\nNesting issues: {len(issues)}")
for idx, tag, ctx in issues[:5]:
    print(f"  L{idx} ({tag}): {ctx}")

# Check for orphan </td> remaining
orphan = sum(
    1 for i, line in enumerate(content.splitlines())
    if line.strip() == '</td>'
)
print(f"\nOrphan </td> remaining: {orphan}")
print(f"Total size: {len(content):,} bytes")
