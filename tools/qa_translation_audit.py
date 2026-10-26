#!/usr/bin/env python3
"""Translation-quality audit for the bilingual PCIe 6.2 markdown.

Parses depth-1 bilingual <td> cells (EN then ZH), then reports:
  - untranslated / truncated translations
  - numeric-token loss (values dropped in ZH)
  - untranslated English sentences leaking into the ZH column
  - half-width punctuation in Chinese prose
  - term drift against glossary.json + a variant watchlist
  - blacklisted renderings

Usage: python3 tools/qa_translation_audit.py [--json out.json] ch01 ch02 ...
"""
from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = {
    "ch01": "PCIe6.2_Spec_ch01_Introduction_引言.md",
    "ch02": "PCIe6.2_Spec_ch02_Transaction_Layer_Specification_事务层规范.md",
    "ch03": "PCIe6.2_Spec_ch03_Data_Link_Layer_Specification_数据链路层规范.md",
    "ch04": "PCIe6.2_Spec_ch04_Physical_Layer_Logical_Block_物理层逻辑块.md",
    "ch05": "PCIe6.2_Spec_ch05_Power_Management_电源管理.md",
    "ch06": "PCIe6.2_Spec_ch06_System_Architecture_系统架构.md",
    "ch07": "PCIe6.2_Spec_ch07_Software_Initialization_and_Configuration_软件初始化与配置.md",
    "ch08": "PCIe6.2_Spec_ch08_Electrical_Sub_Block_电气子块.md",
    "ch09": "PCIe6.2_Spec_ch09_Single_Root_I_O_Virtualization_and_Sharing_单根IO虚拟化与共享SRIOV.md",
    "ch10": "PCIe6.2_Spec_ch10_Address_Translation_Services_地址转换服务ATS.md",
    "ch11": "PCIe6.2_Spec_ch11_TEE_Device_Interface_Security_Protocol_TEE设备接口安全协议TDISP.md",
    "ch12": "PCIe6.2_Spec_ch12_Architectural_Out_of_Band_Management_架构带外管理.md",
}

BLACKLIST = ["有序集合", "热插入", "流量控制", "SR-ROV", "根复杂体"]
# Pairs whose mixed use in one project signals drift. (preferred, variant)
VARIANTS = [
    ("根复合体", "根联合体"), ("根复合体", "根复杂体"), ("根复合体", "根复合器"),
    ("端点", "终端"), ("交换机", "交换器"), ("交换机", "交换设备"),
    ("流控", "流量控制"), ("热插拔", "热插入"), ("有序集", "有序集合"),
    ("通道", "通路"), ("链路", "链接"), ("功能", "函数"),
    ("请求者", "请求方"), ("完成者", "完成方"), ("接收方", "接收者"),
    ("发送方", "发送者"), ("事务层", "传输层"), ("数据链路层", "数据链接层"),
    ("物理层", "实体层"), ("设备", "器件"), ("寄存器", "暂存器"),
    ("描述符", "描述子"), ("带宽", "频宽"), ("吞吐量", "吞吐率"),
    ("时钟", "时脉"), ("复位", "重置"), ("中断", "插断"),
]

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
NUM_RE = re.compile(r"(?<![\w.])(0[xX][0-9A-Fa-f]+|\d+(?:\.\d+)?)(?![\w.])")
CJK_RE = re.compile(r"[一-鿿]")
ENGLISH_SENTENCE_RE = re.compile(
    r"(?:(?<![A-Za-z])[A-Za-z][A-Za-z'’\-]*[ ,]+){6,}[A-Za-z][A-Za-z'’\-]*"
)
EN_STOPWORDS = {"the", "of", "and", "is", "are", "to", "that", "with", "for", "in", "on", "as", "by", "be", "this", "from", "or", "which", "shall", "may", "must", "not"}


def clean(text: str) -> str:
    return WS_RE.sub(" ", html.unescape(TAG_RE.sub(" ", text))).strip()


def parse_tables(path: Path):
    """Yield dicts describing each depth-1 table and its bilingual cells."""
    lines = path.read_text(encoding="utf-8").splitlines()
    depth = 0
    i = 0
    n = len(lines)
    table = None
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if "<table" in line:
            depth += line.count("<table")
            if depth == 1:
                table = {"line": i + 1, "cells": [], "end_line": None, "bilingual": False}
        if depth == 1 and table is not None and "🇬🇧" in line:
            table["bilingual"] = True
        if depth == 1 and stripped in ('<td>', '<td style="background-color:#e8e8e8">'):
            kind = "EN" if stripped == "<td>" else "ZH"
            start = i + 1
            j = start
            inner = 0
            buf = []
            while j < n:
                cur = lines[j]
                inner += cur.count("<table")
                inner -= cur.count("</table>")
                if inner == 0 and cur.strip() == "</td>":
                    break
                buf.append(cur)
                j += 1
            table["cells"].append({"line": start + 1, "kind": kind, "text": "\n".join(buf)})
            i = j
        if "</table>" in line:
            depth -= line.count("</table>")
            if depth == 0 and table is not None:
                table["end_line"] = i + 1
                yield table
                table = None
        i += 1
    if table is not None:
        yield table


def parse_cells(path: Path):
    """Yield (line_no, kind, text) for depth-1 bilingual cells."""
    for table in parse_tables(path):
        for cell in table["cells"]:
            yield cell["line"], cell["kind"], cell["text"]


def numeric_tokens(text: str) -> Counter:
    return Counter(NUM_RE.findall(text))


def english_sentences(text: str):
    out = []
    for m in ENGLISH_SENTENCE_RE.finditer(text):
        run = m.group(0).strip()
        words = set(re.findall(r"[A-Za-z']+", run.lower()))
        if words & EN_STOPWORDS:
            out.append(run)
    return out


def audit_tables(path: Path):
    """Structural checks on each bilingual table."""
    issues = []
    for table in parse_tables(path):
        if not table["bilingual"]:
            continue
        kinds = [c["kind"] for c in table["cells"]]
        cells = table["cells"]
        if not cells:
            continue
        alternating = len(kinds) % 2 == 0 and kinds[::2] == ["EN"] * (len(kinds) // 2) and kinds[1::2] == ["ZH"] * (len(kinds) // 2)
        if not alternating:
            issues.append({
                "line": table["line"], "type": "table_structure",
                "detail": f"cells={kinds} lines={[c['line'] for c in cells]}",
            })
            # still audit the first pair if present
            if len(cells) < 2 or cells[0]["kind"] != "EN" or cells[1]["kind"] != "ZH":
                continue
        en_clean, zh_clean = clean(cells[0]["text"]), clean(cells[1]["text"])
        en_cjk, zh_cjk = len(CJK_RE.findall(en_clean)), len(CJK_RE.findall(zh_clean))
        if en_cjk > 20 and zh_cjk < 5:
            issues.append({"line": table["line"], "type": "columns_swapped",
                           "detail": f"EN has {en_cjk} CJK, ZH has {zh_cjk}"})
        if len(en_clean) > 8000 or re.search(r"<a id=|<table", cells[0]["text"]):
            issues.append({"line": table["line"], "type": "en_cell_swallowed",
                           "detail": f"EN cell {len(en_clean)} chars, structure inside"})
        if re.search(r"(?m)^(##|###) ", cells[0]["text"]):
            issues.append({"line": table["line"], "type": "heading_in_cell",
                           "detail": re.search(r"(?m)^(##|###) .*", cells[0]["text"]).group(0)[:100]})
        if len(zh_clean) < 10:
            issues.append({"line": table["line"], "type": "empty_zh_cell", "detail": en_clean[:100]})
        if zh_clean == en_clean and len(en_clean) > 100:
            issues.append({"line": table["line"], "type": "zh_equals_en", "detail": en_clean[:100]})
    return issues


def audit_pair(en: str, zh: str):
    flags: list[dict] = []
    en_clean, zh_clean = clean(en), clean(zh)
    en_len, zh_len = len(en_clean), len(zh_clean)
    zh_cjk = len(CJK_RE.findall(zh_clean))

    if en_len > 200 and zh_cjk < 10:
        flags.append({"type": "untranslated", "detail": f"EN {en_len} chars, ZH CJK {zh_cjk}"})
    elif en_len > 300 and zh_len < 0.18 * en_len and zh_cjk > 10:
        flags.append({"type": "short_ratio", "detail": f"ZH/EN={zh_len / en_len:.2f}"})

    missing = numeric_tokens(en_clean) - numeric_tokens(zh_clean)
    # Ignore bare 1-2 digit values inside figure/table refs and years; keep everything else.
    significant = {k: v for k, v in missing.items() if not re.fullmatch(r"\d{1,2}", k)}
    if significant and en_len > 80:
        flags.append({"type": "numbers_missing", "detail": dict(list(significant.items())[:12])})

    sentences = english_sentences(zh_clean)
    if sentences:
        flags.append({"type": "english_leak", "detail": sentences[:3]})

    ascii_comma = zh_clean.count(",")
    full_comma = zh_clean.count("，")
    if zh_cjk > 30 and ascii_comma > max(3, full_comma):
        flags.append({"type": "ascii_comma", "detail": f",={ascii_comma} ，={full_comma}"})

    for bad in BLACKLIST:
        if bad in zh_clean:
            flags.append({"type": "blacklist", "detail": bad})
    return flags


def build_pairs(path: Path):
    cells = list(parse_cells(path))
    pairs = []
    pending = None
    for line_no, kind, text in cells:
        if kind == "EN":
            if pending is not None:
                pairs.append((pending[0], pending[1], None))  # EN without ZH
            pending = (line_no, text)
        else:
            if pending is None:
                pairs.append((line_no, None, text))  # ZH without EN
            else:
                pairs.append((pending[0], pending[1], text))
                pending = None
    if pending is not None:
        pairs.append((pending[0], pending[1], None))
    return pairs


def load_glossary():
    data = json.loads((ROOT / "glossary.json").read_text(encoding="utf-8"))
    terms = []
    for t in data.get("terms", []):
        src, tgt = t.get("source", ""), t.get("target", "")
        if not src or not tgt or not CJK_RE.search(tgt):
            continue
        # Short protocol names are intentionally kept in English.
        if re.fullmatch(r"[A-Za-z0-9/.\- ]+", src) and len(src) <= 6:
            continue
        # Glossary targets often carry an English gloss: "规范 (Specification)".
        # Some are reversed: "Configuration (配置)" — take whichever part has CJK.
        parts = re.split(r"[（(]", tgt, maxsplit=1)
        core = parts[0].strip()
        if not CJK_RE.search(core) and len(parts) > 1:
            core = re.sub(r"[)）].*", "", parts[1]).strip() or core
        terms.append({"source": src, "target": core, "category": t.get("category", ""), "confidence": t.get("confidence", "")})
    return terms


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*", default=["ch01", "ch02", "ch04", "ch05", "ch06", "ch07", "ch11"])
    ap.add_argument("--json", default="qa_translation_audit.json")
    args = ap.parse_args()
    chapters = args.chapters or ["ch01", "ch02", "ch04", "ch05", "ch06", "ch07", "ch11"]

    glossary = load_glossary()
    report = {"chapters": {}, "variant_counts": {}, "glossary_coverage": []}
    all_text = {}

    for ch in chapters:
        path = ROOT / FILES[ch]
        pairs = build_pairs(path)
        findings = audit_tables(path)
        stats = {"pairs": 0, "missing_zh": 0, "missing_en": 0, "flag_counts": Counter()}
        for f in findings:
            stats["flag_counts"][f["type"]] += 1
        zh_all = []
        term_hits = defaultdict(lambda: {"en_cells": 0, "zh_with_target": 0, "zh_with_source": 0, "zh_neither": 0})
        for line_no, en, zh in pairs:
            if en is None:
                stats["missing_en"] += 1
                findings.append({"line": line_no, "type": "missing_en"})
                continue
            if zh is None:
                stats["missing_zh"] += 1
                findings.append({"line": line_no, "type": "missing_zh", "en": clean(en)[:160]})
                continue
            stats["pairs"] += 1
            zh_clean = clean(zh)
            zh_all.append(zh_clean)
            for f in audit_pair(en, zh):
                f["line"] = line_no
                f["en"] = clean(en)[:160]
                f["zh"] = zh_clean[:160]
                findings.append(f)
                stats["flag_counts"][f["type"]] += 1

            en_clean = clean(en)
            for t in glossary:
                src = t["source"]
                # word-ish boundary for Latin terms; plain substring for mixed terms
                if re.fullmatch(r"[A-Za-z0-9/.\-+ ]+", src):
                    if not re.search(r"(?<![A-Za-z0-9])" + re.escape(src) + r"(?![A-Za-z0-9])", en_clean, re.I):
                        continue
                elif src not in en_clean:
                    continue
                rec = term_hits[src]
                rec["en_cells"] += 1
                if t["target"] in zh_clean:
                    rec["zh_with_target"] += 1
                elif src.lower() in zh_clean.lower():
                    rec["zh_with_source"] += 1
                else:
                    rec["zh_neither"] += 1

        text = "\n".join(zh_all)
        all_text[ch] = text
        for t in glossary:
            key = t["source"]
            rec = term_hits.get(key)
            if rec and rec["en_cells"] >= 5:
                covered = rec["zh_with_target"] + rec["zh_with_source"]
                report["glossary_coverage"].append({
                    "chapter": ch, **t, "en_cells": rec["en_cells"],
                    "coverage": round(covered / rec["en_cells"], 3),
                    "neither": rec["zh_neither"],
                })
        report["chapters"][ch] = {
            "file": FILES[ch], "stats": {**stats, "flag_counts": dict(stats["flag_counts"])},
            "findings": findings,
        }

    for preferred, variant in VARIANTS:
        report["variant_counts"][preferred] = {}
        report["variant_counts"][variant] = {}
        for ch, text in all_text.items():
            report["variant_counts"][preferred][ch] = text.count(preferred)
            report["variant_counts"][variant][ch] = text.count(variant)

    out = ROOT / args.json
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote {out}")
    for ch, data in report["chapters"].items():
        s = data["stats"]
        print(f"{ch}: pairs={s['pairs']} missing_zh={s['missing_zh']} missing_en={s['missing_en']} flags={s['flag_counts']}")
    print("\n-- variant drift (preferred vs variant) --")
    for preferred, variant in VARIANTS:
        cp = sum(report["variant_counts"][preferred].values())
        cv = sum(report["variant_counts"][variant].values())
        if cp and cv:
            print(f"  {preferred}={cp} | {variant}={cv}")
    print("\n-- glossary low coverage (<0.75, n>=5) --")
    low = [g for g in report["glossary_coverage"] if g["coverage"] < 0.75]
    low.sort(key=lambda g: (g["coverage"], -g["en_cells"]))
    for g in low[:30]:
        print(f"  {g['chapter']} {g['source']} -> {g['target']}: {g['coverage']} ({g['en_cells']} cells, neither={g['neither']})")


if __name__ == "__main__":
    main()
