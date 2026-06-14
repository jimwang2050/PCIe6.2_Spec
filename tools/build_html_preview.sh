#!/bin/bash
# Generate HTML preview for each chapter + combined book.html
# Uses pandoc with CXL 3.2 style CSS (gray-bg Chinese cell)

set -e
cd /Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh

mkdir -p preview

# Use the CXL_zh CSS for consistent styling
CSS_FILE="/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/CXL_zh/pdf-style.css"
if [ ! -f "$CSS_FILE" ]; then
    # Fallback minimal CSS
    cat > /tmp/pcie62_style.css <<'EOF'
body { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 1400px; margin: 20px auto; padding: 0 20px; line-height: 1.6; }
h1 { border-bottom: 3px solid #1a73e8; padding-bottom: 8px; }
h2 { border-bottom: 1px solid #ccc; padding-bottom: 4px; margin-top: 24px; }
table { border-collapse: collapse; margin: 12px 0; }
th, td { border: 1px solid #ddd; padding: 8px 12px; vertical-align: top; }
th { background-color: #f0f0f0; }
img { max-width: 100%; height: auto; border: 1px solid #ddd; }
blockquote { background: #f5f5f5; padding: 8px 12px; border-left: 3px solid #888; }
code { background: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-family: "SF Mono", Menlo, monospace; }
pre { background: #f5f5f5; padding: 12px; border-radius: 4px; overflow-x: auto; }
EOF
    CSS_FILE="/tmp/pcie62_style.css"
fi

# 1. Per-chapter HTML
echo "=== Generating per-chapter HTML ==="
for md in PCIe6.2_Spec_ch*.md; do
    name=$(basename "$md" .md)
    pandoc "$md" -f gfm -t html5 \
        --standalone \
        --css="$(basename $CSS_FILE)" \
        --metadata title="$name" \
        -o "preview/${name}.html" \
        --quiet
    size=$(stat -f%z "preview/${name}.html" 2>/dev/null || echo 0)
    printf "  %-90s %8d bytes\n" "$name.html" "$size"
done

# 2. Combined book.md (concatenate all chapters)
echo ""
echo "=== Building combined book.md ==="
cat > book.md <<'HEADER'
# 📚 PCIe 6.2 Spec 中英对照翻译 (完整版)

> **PCI Express® Base Specification — Revision 6.2, Version 1.0 — January 25, 2024**
> 📄 2111 pages, 12 chapters + appendices
> 🎨 Format: 中英对照双语 Markdown, CXL 3.2 表格格式 (灰底中文)
> 📐 翻译模板: [CXL 3.2 Spec](https://github.com/jimwang2050/CXL_3.2_Spec)
> 🐙 GitHub: https://github.com/jimwang2050/PCIe6.2_Spec

## 📑 目录

HEADER

# Build TOC with links
for md in $(ls PCIe6.2_Spec_ch*.md | sort); do
    name=$(basename "$md" .md)
    # Extract H1 title (first line)
    title=$(grep -m1 "^# " "$md" | sed 's/^# //' | sed 's/"/\\"/g')
    echo "- [${title}](#${name})" >> book.md
done

echo "" >> book.md
echo "---" >> book.md
echo "" >> book.md

# Append each chapter
for md in $(ls PCIe6.2_Spec_ch*.md | sort); do
    name=$(basename "$md" .md)
    echo "" >> book.md
    echo "<a id=\"${name}\"></a>" >> book.md
    echo "" >> book.md
    cat "$md" >> book.md
done

# 3. Combined book.html
echo ""
echo "=== Building combined book.html ==="
pandoc book.md -f gfm -t html5 \
    --standalone \
    --css="$(basename $CSS_FILE)" \
    --toc --toc-depth=2 \
    --metadata title="PCIe 6.2 Spec 中英对照翻译" \
    -o "preview/book.html" \
    --quiet

# Copy CSS to preview dir if it's not the local one
if [ "$CSS_FILE" != "/tmp/pcie62_style.css" ]; then
    cp "$CSS_FILE" preview/
fi
[ -f /tmp/pcie62_style.css ] && cp /tmp/pcie62_style.css preview/pcie62_style.css

# 4. Build a single book PDF if possible (not required)
echo ""
echo "=== Summary ==="
ls -la preview/ | head -20
echo ""
echo "book.md size: $(wc -c < book.md) bytes ($(wc -l < book.md) lines)"
echo "preview/book.html size: $(wc -c < preview/book.html) bytes"
echo ""
echo "✓ Done. Open preview/book.html in your browser to read the full translation."
