#!/usr/bin/env python3
"""Phase 3: Auto-translate and insert missing Chinese figure captions."""

import json, re, glob, sys

# Load glossary
with open('glossary.json', 'r') as f:
    glossary = json.load(f)

en_to_zh = {}
for term in glossary['terms']:
    if term.get('confidence') == 'high':
        src = term.get('source', '')
        tgt = term.get('target', '')
        if src and tgt and len(src) > 3:
            en_to_zh[src.lower()] = tgt

# Override bad mappings
en_to_zh['flit'] = 'Flit'

# Remove shorter terms that are substrings of longer multi-word terms
# This prevents double-translation like "Flow Control" → "流控 (流 Control)"
multi_word = {k for k in en_to_zh if ' ' in k}
to_remove = set()
for single_k in list(en_to_zh.keys()):
    if ' ' not in single_k:
        for mw in multi_word:
            if single_k in mw.split():
                to_remove.add(single_k)
                break
for k in to_remove:
    del en_to_zh[k]

sorted_terms = sorted(en_to_zh.items(), key=lambda x: len(x[0]), reverse=True)

# Remove Chinese parenthetical from targets to avoid nested duplication
# e.g., "流控 (Flow Control)" → "流控",  "根复合体 (Root Complex)" → "根复合体"
for k in list(en_to_zh.keys()):
    v = en_to_zh[k]
    # Remove trailing (EN text) or （EN text） parenthetical
    v = re.sub(r'\s*[\(（][A-Za-z0-9\s\-\./,]+[\)）]\s*$', '', v)
    v = v.strip()
    en_to_zh[k] = v

CAPS_RE = re.compile(r'^[A-Z0-9\s\-,\./\+\(\)\[\]≥≤:;]+$')

def translate_caption(en_title):
    """Translate a figure caption preserving acronyms."""
    result = en_title

    # Multi-word glossary matches first
    for en_term, zh_term in sorted_terms:
        if ' ' in en_term:
            result = re.sub(re.escape(en_term), zh_term, result, flags=re.IGNORECASE)

    # Single-word glossary matches
    words = result.split(' ')
    new_words = []
    for w in words:
        stripped = w.strip('.,;:()[]')
        lower = stripped.lower()
        if CAPS_RE.match(stripped) and any(c.isalpha() for c in stripped):
            new_words.append(w)
        elif re.match(r'^[\d\.,xX]+$', stripped):
            new_words.append(w)
        elif lower in en_to_zh:
            new_words.append(w.replace(stripped, en_to_zh[lower]))
        else:
            new_words.append(w)
    result = ' '.join(new_words)

    # Caption-specific replacements
    caption_rules = [
        (r'\bExample (?:Illustrating|Showing|of)\b', '示例'),
        (r'\bDiagram of\b', ''),
        (r'\bDiagram\b', '图'),
        (r'\bBlock Diagram\b', '框图'),
        (r'\bHighlighting\b', ':'),
        (r'\bShowing\b', ':'),
        (r'\bIllustrating\b', ':'),
        (r'\bFlowchart\b', '流程图'),
        (r'\bConceptual Flow\b', '概念性流程'),
        (r'\bPseudo Logic\b', '伪逻辑'),
        (r'\bwith\b', '含'),
        (r'\bwithout\b', '无'),
        (r'\band\b', '与'),
        (r'\bfor\b', ''),
        (r'\bof\b', ''),
        (r'\bthe\b', ''),
        (r'\ba\b', ''),
        (r'\ban\b', ''),
        (r'\bto\b', ''),
        (r'\bfrom\b', ''),
        (r'\busing\b', ''),
        (r'\bbetween\b', ''),
        (r'\bNon-Flit Mode\b', '非 Flit 模式'),
        (r'\bFlit Mode\b', 'Flit 模式'),
        (r'\bRepresentation\b', '表示'),
        (r'\bOperations\b', '操作'),
        (r'\bOverview\b', '概述'),
        (r'\bFormat\b', '格式'),
        (r'\bMapping\b', '映射'),
        (r'\bFlow\b', '流'),
        (r'\bSequence\b', '序列'),
        (r'\bCalculation\b', '计算'),
        (r'\bArchitecture\b', '架构'),
    ]
    for pat, repl in caption_rules:
        result = re.sub(pat, repl, result, flags=re.IGNORECASE)

    # Cleanup
    result = re.sub(r'\s+', ' ', result).strip()
    result = re.sub(r'\s([,.)\]])', r'\1', result)
    result = re.sub(r'\(\s', '(', result)
    result = re.sub(r'\s:', ':', result)
    result = re.sub(r':\s+', ': ', result)
    # Remove leading/trailing artifacts
    result = result.strip(' ,:')

    return result


def process_file(fpath, dry_run=False):
    with open(fpath, 'r') as f:
        content = f.read()

    # Find all EN figure captions: > **Figure N-XX.** Title
    en_figs = list(re.finditer(r'> \*\*Figure (\d+-\d+)\.\*\*\s*(.+)', content))

    # Find all ZH figure captions for checking
    zh_figs = set(m.group(1) for m in re.finditer(r'> \*\*图 (\d+-\d+)\.\*\*', content))

    # For each missing ZH, find the caption block and insert ZH
    insertions = []  # (position, zh_block)

    for m in en_figs:
        fig_num = m.group(1)
        en_title = m.group(2).strip()

        if fig_num in zh_figs:
            continue  # Already has ZH caption

        zh_title = translate_caption(en_title)

        # Find the end of this figure block (after img tags)
        end_pos = m.end()
        remaining = content[end_pos:end_pos+500]
        img_end = 0
        for img_m in re.finditer(r'> <img src="[^"]+" width="\d+">', remaining):
            img_end = max(img_end, img_m.end())

        # Check if we're inside a table context
        before = content[:end_pos]
        table_opens = len(re.findall(r'<table[^>]*>', before))
        table_closes = before.count('</table>')
        inside_table = table_opens > table_closes

        insert_pos = end_pos + img_end

        if inside_table:
            # Find the next </table> after this figure
            next_table_close = content.find('</table>', end_pos)
            if next_table_close >= 0:
                insert_pos = next_table_close + len('</table>')

        # Build ZH caption block
        zh_block = f'\n> **图 {fig_num}.** {zh_title}'
        # Copy img tags from EN side
        img_section = remaining[:img_end]
        if img_section.strip():
            zh_block += '\n' + img_section

        insertions.append((insert_pos, zh_block, fig_num, en_title, zh_title))

    if dry_run:
        return insertions

    # Apply insertions in reverse order (to preserve positions)
    new_content = content
    for pos, zh_block, fig_num, en_title, zh_title in sorted(insertions, key=lambda x: x[0], reverse=True):
        new_content = new_content[:pos] + zh_block + new_content[pos:]

    if insertions:
        with open(fpath, 'w') as f:
            f.write(new_content)

    return insertions


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv

    # Accept specific files as arguments, or default to all
    target_files = [a for a in sys.argv[1:] if a.endswith('.md')]
    if target_files:
        files = target_files
    else:
        files = sorted(glob.glob("PCIe6.2_Spec_ch*.md"))
        files = [f for f in files if 'Part_' not in f]

    total = 0
    for fpath in files:
        results = process_file(fpath, dry_run=dry)
        if results:
            ch = re.search(r'ch(\d+)', fpath).group(1)
            print(f"ch{ch}: {len(results)} 个 Figure ZH 标题{' (预览)' if dry else ' ✓'}")
            for _, _, num, en, zh in results[:3]:
                print(f"  Figure {num}: {zh[:70]}")
            if len(results) > 3:
                print(f"  ... 还有 {len(results)-3} 个")
            total += len(results)

    print(f"\n{'预览' if dry else '补全'}合计: {total} 个 Figure")
    if dry:
        print("使用 --apply 参数执行实际写入")
