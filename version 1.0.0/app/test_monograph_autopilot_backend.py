# -*- coding: utf-8 -*-
"""
OmniScholar 2050 Monograph & Auto-Pilot Backend Test Suite
Tests endpoints:
- GET & POST /api/2050/auto-pilot-loop
- GET & HEAD /api/export-monograph-pdf (inline and download attachment)
- GET /api/export-zip
- GET /api/health
"""

import sys
import os
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("[TEST 1/6] Testing GET /api/health ...")
    r = requests.get(f"{BASE_URL}/api/health", timeout=10)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data["features"].get("auto_pilot_loop_2050") is True, "auto_pilot_loop_2050 flag missing"
    assert data["features"].get("export_monograph_pdf") is True, "export_monograph_pdf flag missing"
    assert data["features"].get("doctoral_monograph_30page") is True, "doctoral_monograph_30page flag missing"
    print("  -> Health endpoint verified OK with 2050 Singularity flags.")

def test_head_monograph_pdf():
    print("[TEST 2/6] Testing HEAD /api/export-monograph-pdf ...")
    r = requests.head(f"{BASE_URL}/api/export-monograph-pdf", timeout=30)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    assert "application/pdf" in r.headers.get("Content-Type", ""), f"Unexpected Content-Type: {r.headers.get('Content-Type')}"
    assert "inline" in r.headers.get("Content-Disposition", ""), f"Expected inline disposition: {r.headers.get('Content-Disposition')}"
    print(f"  -> HEAD monograph PDF OK (Content-Type: {r.headers.get('Content-Type')}, Content-Disposition: {r.headers.get('Content-Disposition')})")

def test_get_monograph_pdf():
    print("[TEST 3/6] Testing GET /api/export-monograph-pdf (inline preview) ...")
    r = requests.get(f"{BASE_URL}/api/export-monograph-pdf", timeout=30)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    assert "application/pdf" in r.headers.get("Content-Type", "")
    assert "inline" in r.headers.get("Content-Disposition", "")
    assert r.content.startswith(b"%PDF-"), "Invalid PDF signature"
    print(f"  -> GET monograph PDF verified OK ({len(r.content):,} bytes, valid %PDF- magic bytes)")

def test_get_monograph_pdf_download():
    print("[TEST 4/6] Testing GET /api/export-monograph-pdf?download=true (attachment) ...")
    r = requests.get(f"{BASE_URL}/api/export-monograph-pdf?download=true", timeout=30)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    assert "attachment" in r.headers.get("Content-Disposition", ""), f"Expected attachment disposition: {r.headers.get('Content-Disposition')}"
    assert r.content.startswith(b"%PDF-"), "Invalid PDF signature"
    print(f"  -> GET monograph download attachment verified OK: {r.headers.get('Content-Disposition')}")

def test_auto_pilot_loop_post():
    print("[TEST 5/6] Testing POST /api/2050/auto-pilot-loop ...")
    payload = {
        "topic": "Quantum Causal Emergence in Asymmetric High-Frequency Algorithmic Equity Trading",
        "domain": "Finance & Financial Economics",
        "standard": "Doctoral Monograph & Treatise (30+ Pages, Q1 Comprehensive Review)",
        "sample_size": 100
    }
    r = requests.post(f"{BASE_URL}/api/2050/auto-pilot-loop", json=payload, timeout=90)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"
    data = r.json()
    assert data["status"] == "SUCCESS", f"Expected SUCCESS, got {data.get('status')}"
    assert data["page_count"] >= 30, f"Expected >= 30 pages, got {data.get('page_count')}"
    assert data["pages_certified"] is True, "pages_certified flag is False"
    assert data["merkle_root"], "Merkle root hash is empty"
    assert data["council_score"] >= 90.0, f"Council score low: {data.get('council_score')}"
    assert "ACCEPT" in data["council_verdict"], f"Unexpected verdict: {data.get('council_verdict')}"
    assert "causal_ate" in data, "causal_ate missing"
    assert len(data.get("telemetry", [])) >= 5, f"Insufficient telemetry stages: {len(data.get('telemetry', []))}"
    print(f"  -> Auto-Pilot Loop SUCCESS: {data['page_count']} pages compiled in {data['execution_time_seconds']}s")
    print(f"     Merkle Root: {data['merkle_root'][:16]}... | Council Verdict: {data['council_verdict']} ({data['council_score']}%)")

def test_export_zip():
    print("[TEST 6/6] Testing GET /api/export-zip ...")
    r = requests.get(f"{BASE_URL}/api/export-zip", timeout=30)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    assert "application/zip" in r.headers.get("Content-Type", "")
    assert len(r.content) > 1000, "ZIP bundle empty"
    
    import zipfile
    import io
    zf = zipfile.ZipFile(io.BytesIO(r.content))
    namelist = zf.namelist()
    has_pdf = any("monograph" in f.lower() or f.endswith(".pdf") for f in namelist)
    assert has_pdf, f"No PDF or Monograph in zip: {namelist[:10]}"
    print(f"  -> Export ZIP verified OK ({len(r.content):,} bytes, {len(namelist)} archive members including monographs/PDFs)")

if __name__ == "__main__":
    print("=" * 70)
    print("OMNISCHOLAR 2050 BACKEND VERIFICATION SUITE")
    print("=" * 70)
    test_health()
    test_head_monograph_pdf()
    test_get_monograph_pdf()
    test_get_monograph_pdf_download()
    test_auto_pilot_loop_post()
    test_export_zip()
    print("=" * 70)
    print("ALL 6 BACKEND TESTS PASSED (100% SUCCESS RATE)")
    print("=" * 70)
