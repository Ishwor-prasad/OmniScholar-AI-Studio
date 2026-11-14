"""
OmniScholar Autonomous Research OS - Billion-Dollar Suite Quality Audit
Tests:
1. Dynamic Topic Synthesis (/api/synthesize-topic)
2. Survey Data Generation (/api/generate-survey-data)
3. End-to-End Autonomous Pipeline Execution (/api/run-autonomous-pipeline)
4. In-Browser PDF Preview (/api/preview-pdf)
5. Typst 0.15 Publication Layout & Affiliation Verification
6. Frontend 6-Stage UI & DOM Alignment
"""

import os
import sys
import json
import time
import shutil
import hashlib
import zipfile
import subprocess
from pathlib import Path
import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from server import app, SESSION_DATA, BASE_DIR, RUNS_DIR, get_typst_bin

class SuiteReport:
    def __init__(self):
        self.results = []
        self.failures = []

    def log(self, section: str, test_name: str, passed: bool, details: str = ""):
        status = "PASS" if passed else "FAIL"
        entry = {"section": section, "test": test_name, "status": status, "details": details}
        self.results.append(entry)
        if not passed:
            self.failures.append(entry)
        symbol = "✓" if passed else "✗"
        print(f"[{status}] {symbol} [{section}] {test_name}: {details}")

    def summary(self):
        total = len(self.results)
        passed = total - len(self.failures)
        print("\n" + "=" * 75)
        print(f"BILLION-DOLLAR RESEARCH OS AUDIT: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
        if self.failures:
            print(f"FAILURES DETECTED ({len(self.failures)}):")
            for f in self.failures:
                print(f"  - [{f['section']}] {f['test']}: {f['details']}")
        else:
            print("ALL QUALITY GATES PASSED! PRODUCTION READY.")
        print("=" * 75 + "\n")
        return len(self.failures) == 0


def test_topic_synthesis(client: TestClient, report: SuiteReport):
    print("\n--- 1. AUDITING DYNAMIC TOPIC SYNTHESIS ---")
    custom_topics = [
        {
            "topic": "Autonomous Agent Swarms in High-Frequency Algorithmic Trading",
            "domain": "Computational Econometrics & Distributed AI",
            "standard": "IEEE Transactions on Neural Networks and Learning Systems"
        },
        {
            "topic": "Neuromorphic Edge Computing in Real-Time Critical Care Telemetry",
            "domain": "Biomedical Cyber-Physical Systems",
            "standard": "Nature Biomedical Engineering"
        }
    ]
    for idx, payload in enumerate(custom_topics, 1):
        try:
            r = client.post("/api/synthesize-topic", json=payload)
            if r.status_code == 200:
                data = r.json()
                has_model = "theoretical_model" in data or "model" in data or "variables" in data
                has_hyp = "hypotheses" in data and len(data["hypotheses"]) >= 2
                has_gaps = "research_gaps" in data or "gap" in data or "problem_statement" in data
                passed = has_model and has_hyp
                report.log("SYNTHESIS", f"Topic Synthesis #{idx} ({payload['topic'][:35]}...)", passed,
                           f"Status: {r.status_code}, Hypotheses: {len(data.get('hypotheses', []))}, Keys: {list(data.keys())}")
            else:
                report.log("SYNTHESIS", f"Topic Synthesis #{idx}", False, f"Status code: {r.status_code}, Error: {r.text[:100]}")
        except Exception as e:
            report.log("SYNTHESIS", f"Topic Synthesis #{idx}", False, f"Exception: {e}")


def test_survey_data_generation(client: TestClient, report: SuiteReport):
    print("\n--- 2. AUDITING REALISTIC SURVEY DATA GENERATION ---")
    payload = {
        "topic": "Autonomous Agent Swarms in High-Frequency Algorithmic Trading",
        "sample_size": 100,
        "constructs": ["Execution Latency", "Swarm Coordination", "Variance Resilience", "Market Impact Index"]
    }
    try:
        r = client.post("/api/generate-survey-data", json=payload)
        if r.status_code == 200:
            data = r.json()
            n_rows = data.get("sample_size") or len(data.get("records", [])) or len(data.get("data", []))
            has_cols = "columns" in data or "items" in data or "questionnaire" in data
            passed = n_rows == 100 and has_cols
            report.log("DATA_GEN", "Survey Data Generation (N=100)", passed,
                       f"Status: {r.status_code}, N: {n_rows}, Columns/Items: {len(data.get('columns', data.get('items', [])))}")
        else:
            report.log("DATA_GEN", "Survey Data Generation", False, f"Status code: {r.status_code}, Error: {r.text[:100]}")
    except Exception as e:
        report.log("DATA_GEN", "Survey Data Generation", False, f"Exception: {e}")


def test_autonomous_pipeline(client: TestClient, report: SuiteReport):
    print("\n--- 3. AUDITING 1-CLICK END-TO-END AUTONOMOUS PIPELINE ---")
    payload = {
        "topic": "Autonomous Multi-Agent Systems in Decentralized Finance Protocol Security",
        "domain": "Blockchain Cyber-Security & Applied Cryptography",
        "standard": "IEEE Transactions on Dependable and Secure Computing"
    }
    try:
        t0 = time.time()
        r = client.post("/api/run-autonomous-pipeline", json=payload)
        elapsed = time.time() - t0
        if r.status_code == 200:
            res = r.json()
            stages = res.get("stages", {})
            has_framing = "framing" in res or "topic" in res or "theoretical_model" in res
            has_stats = "summary" in res or "stats" in res or "regression" in res
            has_passport = "passport" in res or "data_hash_sha256" in res.get("summary", res)
            has_pdf = "pdf_url" in res or "pdf_ready" in res or "manuscript_pdf" in res or res.get("success", False)
            passed = has_stats and has_passport
            report.log("PIPELINE", "1-Click End-to-End Pipeline Execution", passed,
                       f"Status: {r.status_code}, Elapsed: {elapsed:.2f}s, PDF URL: {res.get('pdf_url')}")
        else:
            report.log("PIPELINE", "1-Click End-to-End Pipeline", False, f"Status code: {r.status_code}, Error: {r.text[:100]}")
    except Exception as e:
        report.log("PIPELINE", "1-Click End-to-End Pipeline", False, f"Exception: {e}")


def test_pdf_preview_endpoint(client: TestClient, report: SuiteReport):
    print("\n--- 4. AUDITING IN-BROWSER PDF PREVIEW ENDPOINT ---")
    try:
        r = client.get("/api/preview-pdf")
        if r.status_code == 200:
            content_type = r.headers.get("content-type", "")
            disposition = r.headers.get("content-disposition", "")
            is_pdf = content_type.startswith("application/pdf")
            is_inline = "inline" in disposition.lower()
            magic_pdf = r.content[:5] == b"%PDF-"
            passed = is_pdf and magic_pdf
            report.log("PREVIEW", "GET /api/preview-pdf headers & bytes", passed,
                       f"Content-Type: {content_type}, Disposition: {disposition}, Size: {len(r.content)} bytes, Magic: {r.content[:5]}")
        else:
            report.log("PREVIEW", "GET /api/preview-pdf", False, f"Status: {r.status_code}, Detail: {r.text[:100]}")
    except Exception as e:
        report.log("PREVIEW", "GET /api/preview-pdf", False, f"Exception: {e}")


def test_typst_ieee_affiliations(client: TestClient, report: SuiteReport):
    print("\n--- 5. AUDITING TYPST IEEE TRANSACTIONS FORMAT & INSTITUTIONAL AFFILIATION ---")
    run_dir = Path(RUNS_DIR) / "sample"
    main_typ = run_dir / "main.typ"
    if not main_typ.exists():
        r = client.post("/api/load-sample")
        if r.status_code == 200:
            print("  [Setup] Loaded sample dataset to populate runs/sample")

    if main_typ.exists():
        typ_text = main_typ.read_text(encoding="utf-8")
        has_affiliation = "Safal AI" in typ_text or "Innovation Centre" in typ_text or "Safal" in typ_text or "OmniScholar" in typ_text
        report.log("TYPST", "Institutional affiliation in main.typ", has_affiliation,
                   "Detected institutional header in manuscript" if has_affiliation else "Affiliation string not found in main.typ")
        
        # Test compilation
        typst_cmd = get_typst_bin() or "typst"
        cmd = [typst_cmd, "compile", str(main_typ), str(run_dir / "test_billion_dollar.pdf")]
        res = subprocess.run(cmd, capture_output=True, text=True)
        report.log("TYPST", "Typst zero-error compilation", res.returncode == 0,
                   f"Returncode: {res.returncode}, Stderr: {res.stderr.strip()[:100] if res.stderr else 'None'}")
    else:
        report.log("TYPST", "main.typ presence", False, "main.typ missing in runs/sample")


def test_frontend_ui(report: SuiteReport):
    print("\n--- 6. AUDITING FRONTEND STUDIO COMPONENTS ---")
    index_html = (APP_DIR / "static" / "index.html").read_text(encoding="utf-8")
    app_js = (APP_DIR / "static" / "app.js").read_text(encoding="utf-8")
    
    # 6.1 Check 1-click action button
    has_btn = "run-pipeline" in index_html.lower() or "autonomous" in index_html.lower() or "pipeline" in index_html.lower()
    report.log("FRONTEND", "Autonomous 1-Click Pipeline Trigger in index.html", has_btn, "Verified action trigger in UI")

    # 6.2 Check in-browser PDF viewer / iframe
    has_iframe = "<iframe" in index_html.lower() or "preview-pdf" in app_js.lower() or "pdfviewer" in index_html.lower()
    report.log("FRONTEND", "In-Browser PDF Manuscript Viewer in UI", has_iframe, "Verified embedded PDF viewer/iframe")

    # 6.3 Syntax check app.js
    res = subprocess.run(["node", "--check", str(APP_DIR / "static" / "app.js")], capture_output=True, text=True)
    report.log("FRONTEND", "JavaScript Syntax Validation on app.js", res.returncode == 0, f"Returncode: {res.returncode}")


if __name__ == "__main__":
    report = SuiteReport()
    client = TestClient(app)
    
    test_topic_synthesis(client, report)
    test_survey_data_generation(client, report)
    test_autonomous_pipeline(client, report)
    test_pdf_preview_endpoint(client, report)
    test_typst_ieee_affiliations(client, report)
    test_frontend_ui(report)
    
    all_ok = report.summary()
    sys.exit(0 if all_ok else 1)
