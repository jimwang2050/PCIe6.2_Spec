#!/usr/bin/env python3
"""
Submit each PDF chunk to MinerU API and poll for completion.

For each chunk in tools/pdf_chunks/:
1. Submit via /api/v4/file-urls/batch (local file upload)
2. PUT file to returned URL
3. Poll /api/v4/extract-results/batch/{batch_id}
4. Download full_zip_url when state="done"
5. Unzip to tools/mineru_results/chunk_NN/

MinerU token from env MINERU_TOKEN.
"""
import json
import os
import sys
import time
import zipfile
from pathlib import Path

import requests

OUT_ROOT = Path('/Users/jianmingwang/Downloads/00_study/02_work/01_book/pcie_cxl/PCIe6.2_zh')
CHUNKS_DIR = OUT_ROOT / 'tools' / 'pdf_chunks'
RESULTS_DIR = OUT_ROOT / 'tools' / 'mineru_results'
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

API_BASE = 'https://mineru.net/api/v4'
TOKEN = os.environ.get('MINERU_TOKEN')
if not TOKEN:
    print("Error: MINERU_TOKEN not set")
    sys.exit(1)

HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def submit_local_file(pdf_path):
    """Submit a local file via the file-urls/batch endpoint."""
    name = pdf_path.name
    data_id = pdf_path.stem
    body = {
        'files': [{'name': name, 'data_id': data_id, 'is_ocr': True}],
        'model_version': 'pipeline',
        'enable_formula': False,
        'enable_table': True,
        'language': 'en',
    }
    r = requests.post(
        f'{API_BASE}/file-urls/batch',
        headers=HEADERS,
        json=body,
        timeout=60,
    )
    if r.status_code != 200:
        print(f"  submit error: {r.status_code} {r.text[:200]}")
        return None
    resp = r.json()
    if resp.get('code') != 0:
        print(f"  submit failed: {resp}")
        return None
    return resp['data']  # Contains batch_id, file_urls


def upload_file(pdf_path, upload_url):
    """PUT the local file to the presigned URL."""
    with open(pdf_path, 'rb') as f:
        r = requests.put(upload_url, data=f, timeout=600)
    return r.status_code in (200, 204)


def poll_batch(batch_id, max_wait=3600, poll_interval=30):
    """Poll until done/failed or timeout."""
    start = time.time()
    while time.time() - start < max_wait:
        r = requests.get(
            f'{API_BASE}/extract-results/batch/{batch_id}',
            headers=HEADERS,
            timeout=30,
        )
        if r.status_code != 200:
            print(f"  poll error: {r.status_code} {r.text[:200]}")
            time.sleep(poll_interval)
            continue
        resp = r.json()
        if resp.get('code') != 0:
            print(f"  poll failed: {resp}")
            time.sleep(poll_interval)
            continue
        data = resp['data']
        results = data.get('extract_result', [])
        if not results:
            time.sleep(poll_interval)
            continue
        state = results[0].get('state')
        print(f"  state: {state} (elapsed {int(time.time()-start)}s)")
        if state == 'done':
            return results
        if state == 'failed':
            print(f"  FAILED: {results[0].get('err_msg')}")
            return None
        time.sleep(poll_interval)
    print(f"  TIMEOUT after {max_wait}s")
    return None


def download_and_unzip(zip_url, out_dir):
    """Download result ZIP and extract."""
    r = requests.get(zip_url, timeout=300)
    if r.status_code != 200:
        print(f"  download error: {r.status_code}")
        return False
    zip_path = out_dir / 'result.zip'
    zip_path.write_bytes(r.content)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(out_dir)
    zip_path.unlink()
    return True


def process_chunk(pdf_path, chunk_idx):
    chunk_name = pdf_path.stem
    out_dir = RESULTS_DIR / chunk_name
    if (out_dir / 'full.md').exists():
        print(f"[{chunk_idx}] Already processed: {chunk_name}")
        return True

    print(f"[{chunk_idx}] Submitting: {pdf_path.name}")
    data = submit_local_file(pdf_path)
    if not data:
        return False

    batch_id = data['batch_id']
    print(f"  batch_id: {batch_id}")

    file_urls = data.get('file_urls', [])
    if not file_urls:
        print(f"  no file_urls in response: {data}")
        return False
    upload_url = file_urls[0].get('url') if isinstance(file_urls[0], dict) else file_urls[0]
    print(f"  uploading to presigned URL...")
    if not upload_file(pdf_path, upload_url):
        print(f"  upload failed")
        return False
    print(f"  uploaded, polling...")

    results = poll_batch(batch_id)
    if not results:
        return False

    zip_url = results[0].get('full_zip_url')
    if not zip_url:
        print(f"  no zip url in result")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"  downloading result...")
    if not download_and_unzip(zip_url, out_dir):
        return False
    print(f"  ✓ done: {chunk_name}")
    return True


def main():
    chunks = sorted(CHUNKS_DIR.glob('chunk_*.pdf'))
    if not chunks:
        print(f"No chunks found in {CHUNKS_DIR}")
        return

    print(f"Found {len(chunks)} chunks to process")
    print(f"Token: {TOKEN[:8]}...{TOKEN[-8:]}\n")

    n_ok = 0
    n_fail = 0
    for i, pdf in enumerate(chunks, 1):
        ok = process_chunk(pdf, i)
        if ok:
            n_ok += 1
        else:
            n_fail += 1
        print()

    print(f"\n=== Summary ===")
    print(f"  Success: {n_ok}")
    print(f"  Failed:  {n_fail}")


if __name__ == '__main__':
    main()
