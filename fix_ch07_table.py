#!/usr/bin/env python3
"""Fix ch07 Table 7-19 HTML nesting issues."""
import subprocess, re

# Get the clean GitHub version
content = subprocess.check_output(
    ['git', 'show', 'HEAD:PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md']
).decode('utf-8')

original = content

# ─── Fix 1: Remove orphan </td> and empty <td style...> before ZH markdown table ───
#   ...EN footnote...
#   </td>           <- orphan
#   <td style="background-color:#e8e8e8">  <- orphan empty ZH cell opening
#   | Bit Location | ZH table header...
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

# ─── Fix 2: Remove orphan </td></tr> after ZH footnote ───
old2 = (
    "\n<sup>163</sup>. 该字段本应更好地命名为 \"Function Type\"，但出于历史原因被命名为 Device/Port Type。\n\n"
    "</td>\n"
    "</tr>"
)
new2 = (
    "\n<sup>163</sup>. 该字段本应更好地命名为 \"Function Type\"，但出于历史原因被命名为 Device/Port Type。\n"
)
content = content.replace(old2, new2, 1)

fixed = content != original
print(f"Changes made: {fixed}")
if fixed:
    print(f"  Original: {len(original):,} bytes -> New: {len(content):,} bytes")
    # Write back
    with open('PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved.")

    # Verify
    for tag in ['<table>', '</table>', '<tr>', '</tr>', '<td>', '</td>']:
        print(f"  {tag}: {content.count(tag)}")
else:
    print("No changes.")
