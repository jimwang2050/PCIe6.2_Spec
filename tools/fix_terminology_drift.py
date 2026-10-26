#!/usr/bin/env python3
"""Terminology drift cleanup: normalize variant terms to preferred forms.

Follows the VARIANTS watchlist in tools/qa_translation_audit.py.
Genuine drift fixed here:
  重置→复位 (reset), 吞吐率→吞吐量 (throughput), 接收者→接收方 (Receiver),
  发送者→发送方 (Sender), 完成方→完成者 (Completer),
  请求方→请求者 (Requester) — ch02/ch06 only; TDISP 请求方/响应方 pairing kept.

Deliberately NOT touched (false positives of the watchlist):
  函数 (math "function"), 终端 (termination/terminus), 链接 (dependency link),
  通路 (Path), 器件 (electrical device), 传输层 (transport layer).

Usage: python3 tools/fix_terminology_drift.py [--dry-run]
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GLOBAL = {
    "重置": "复位",
    "吞吐率": "吞吐量",
    "接收者": "接收方",
    "发送者": "发送方",
    "完成方": "完成者",
}

# Requester: ch02/ch06 (PCIe transaction Requester). ch11 TDISP keeps 请求方.
REQUESTER_FILES = ("ch02", "ch06")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(ROOT.glob("PCIe6.2_Spec_ch*.md"))
    grand = {}

    for f in files:
        text = f.read_text(encoding="utf-8")
        changes = {}
        for term, repl in GLOBAL.items():
            n = text.count(term)
            if n:
                changes[term] = (n, repl)
        if any(k in f.name for k in REQUESTER_FILES):
            n = text.count("请求方")
            if n:
                changes["请求方"] = (n, "请求者")

        if not changes:
            continue
        for term, (n, repl) in changes.items():
            text = text.replace(term, repl)
            grand[term] = grand.get(term, 0) + n
        if not args.dry_run:
            f.write_text(text, encoding="utf-8")
        line = ", ".join(f"{t}->{r}x{n}" for t, (n, r) in changes.items())
        print(f"{f.name}: {line}")

    print("\nTotals:")
    for term, n in sorted(grand.items()):
        print(f"  {term} -> {GLOBAL.get(term, '请求者')}: {n}")
    print(f"\n{'DRY RUN' if args.dry_run else 'APPLIED'} — {sum(grand.values())} replacements")


if __name__ == "__main__":
    main()
