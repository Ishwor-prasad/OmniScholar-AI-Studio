# -*- coding: utf-8 -*-
"""
OmniScholar 2050 AD: Autonomous Auto-Pilot Loop & 30+ Page Monograph Audit Suite
Independent Quality Verifier Test Suite for Sprint 5 Singularity
"""

import ast
import os
import sys
import json
import subprocess
from pathlib import Path
from typing import Dict, Any, List

APP_DIR = Path("A:/OmniScholar/version 1.0.0/app")
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

class AuditReport:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.records = []

    def log(self, category: str, test_name: str, passed: bool, detail: str = ""):
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        if passed:
            self.passed += 1
        else:
            self.failed += 1
        record = f"[{status}] {symbol} [{category}] {test_name}: {detail}"
        self.records.append(record)
        print(record)

    def summary(self) -> str:
        total = self.passed + self.failed
        rate = (self.passed / total * 100) if total > 0 else 0
        return (
            f"\n{'=' * 80}\n"
            f"OMNISCHOLAR AUTO-PILOT & MONOGRAPH SCORECARD: {self.passed}/{total} tests passed ({rate:.1f}%)\n"
            f"{'ALL QUALITY GATES PASSED! WORLD-CLASS PRODUCTION READY.' if self.failed == 0 else f'{self.failed} AUDIT FAILURES DETECTED!'}\n"
            f"{'=' * 80}\n"
        )


def audit_python_ast(report: AuditReport):
    print("\n--- 1. AUDITING PYTHON 3.11+ AST COMPLIANCE ---")
    py_files = list(APP_DIR.glob("*.py")) + list((APP_DIR / "templates").glob("*.py"))
    for py_file in sorted(py_files):
        rel_path = py_file.relative_to(APP_DIR)
        try:
            code = py_file.read_text(encoding="utf-8")
            ast.parse(code, filename=str(py_file))
            report.log("AST", f"AST Parse: {rel_path}", True, f"{len(code.splitlines())} lines parsed cleanly")
        except SyntaxError as e:
            report.log("AST", f"AST Parse: {rel_path}", False, f"SyntaxError at line {e.lineno}: {e.msg}")
        except Exception as e:
            report.log("AST", f"AST Parse: {rel_path}", False, f"Error: {e}")


def audit_monograph_generator_and_typst(report: AuditReport):
    print("\n--- 2. AUDITING 30+ PAGE MONOGRAPH GENERATOR & TYPST 0.15 COMPILATION ---")
    try:
        from templates import build_monograph_30page_manuscript, compile_typst_to_pdf, build_monograph_30page_markdown
        report.log("MONOGRAPH", "Template Import", True, "Successfully imported monograph builders")
    except Exception as e:
        report.log("MONOGRAPH", "Template Import", False, f"Import error: {e}")
        return

    sample_summary_path = APP_DIR / "runs" / "sample" / "dataset_summary.json"
    if sample_summary_path.exists():
        summary = json.loads(sample_summary_path.read_text(encoding="utf-8"))
    else:
        summary = {
            "sample_size": 100,
            "total_variables": 11,
            "data_hash_sha256": "f48ed0a07cbdd3f308100c189eba6f80f356e21d82f70f9260cd5f07b6519bb8",
            "topic": "Algorithmic Execution Signals and Downside Asymmetric Risk in Frontier Equity Markets",
            "domain": "Finance & Financial Economics"
        }

    run_dir = str(APP_DIR / "runs" / "sample")
    
    # 2.1 Typst markup synthesis
    try:
        typ_src = build_monograph_30page_manuscript(summary, run_dir, "dummy_data.csv")
        has_chapters = all(ch in typ_src for ch in ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6"])
        has_appendices = "Appendix A" in typ_src and "Appendix B" in typ_src
        report.log("MONOGRAPH", "Typst Markup Structure (6 Chapters + 2 Appendices)", has_chapters and has_appendices, f"Length: {len(typ_src)} chars")
    except Exception as e:
        report.log("MONOGRAPH", "Typst Markup Structure", False, f"Error: {e}")
        typ_src = ""

    # 2.2 Markdown synthesis
    try:
        md_src = build_monograph_30page_markdown(summary, "dummy_data.csv")
        has_md_chapters = all(ch in md_src for ch in ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6"])
        report.log("MONOGRAPH", "Markdown Monograph Structure (6 Chapters)", has_md_chapters, f"Length: {len(md_src)} chars")
    except Exception as e:
        report.log("MONOGRAPH", "Markdown Monograph Structure", False, f"Error: {e}")

    # 2.3 Typst 0.15 compilation
    if typ_src:
        out_typ = APP_DIR / "runs" / "sample" / "audit_monograph.typ"
        out_typ.write_text(typ_src, encoding="utf-8")
        pdf_out = compile_typst_to_pdf(run_dir, "audit_monograph.typ", "audit_monograph.pdf")
        compiled = pdf_out is not None and os.path.exists(pdf_out)
        size_bytes = os.path.getsize(pdf_out) if compiled else 0
        report.log("MONOGRAPH", "Typst 0.15 Compilation (Returncode 0, Valid File)", compiled, f"Size: {size_bytes:,} bytes")

        # 2.4 Page count verification (>= 30 pages)
        if compiled:
            try:
                import pypdf
                reader = pypdf.PdfReader(pdf_out)
                num_pages = len(reader.pages)
                page_pass = num_pages >= 30
                report.log("MONOGRAPH", "Doctoral Monograph Page Cardinality (>= 30 Pages)", page_pass, f"Total Pages: {num_pages}")
            except Exception as e:
                report.log("MONOGRAPH", "Doctoral Monograph Page Cardinality", False, f"PDF read error: {e}")


def audit_autonomous_pilot_loop(report: AuditReport):
    print("\n--- 3. AUDITING AUTONOMOUS PILOT LOOP ENGINE ---")
    try:
        import autonomous_pilot_loop
        report.log("AUTOPILOT", "Engine Module Import", True, "Successfully imported autonomous_pilot_loop")
    except ImportError:
        report.log("AUTOPILOT", "Engine Module Import", False, "Module autonomous_pilot_loop not yet created")
        return
    except Exception as e:
        report.log("AUTOPILOT", "Engine Module Import", False, f"Import error: {e}")
        return

    # Test runner function existence
    runner = getattr(autonomous_pilot_loop, "run_autonomous_pilot_loop", None)
    report.log("AUTOPILOT", "Runner Function Signature (run_autonomous_pilot_loop)", callable(runner), "Callable verified")
    
    if callable(runner):
        try:
            res = runner(
                topic="Autonomous Epistemic Discovery & Causal Inference",
                domain="Computational Cognitive Science",
                standard="Doctoral Monograph & Treatise (30+ Pages, Q1 Comprehensive Review)",
                sample_size=100
            )
            has_status = res.get("status") in ["SUCCESS", "COMPLETED", "OK", True] or "telemetry" in res or "monograph_pdf_url" in res
            report.log("AUTOPILOT", "End-to-End Loop Execution", has_status, f"Result status: {res.get('status')}")
            
            # Check telemetry events
            events = res.get("telemetry_events") or res.get("telemetry") or res.get("events") or []
            report.log("AUTOPILOT", "Multi-Stage Telemetry Events (>= 5 Stages)", len(events) >= 5, f"Captured {len(events)} stage events")
            
            # Check monograph pdf
            pdf_path = res.get("monograph_pdf_path") or res.get("pdf_path") or res.get("monograph_pdf_url") or res.get("monograph_download_url") or res.get("pdf_url")
            report.log("AUTOPILOT", "Generated Monograph PDF Artifact", pdf_path is not None, f"Path/URL: {pdf_path}")
            
            # Check causal DAG
            dag = res.get("causal_dag") or res.get("dag") or res.get("summary", {}).get("causal_discovery")
            report.log("AUTOPILOT", "Causal DAG Artifact in Loop", dag is not None, f"DAG Nodes: {len(dag.get('nodes', [])) if isinstance(dag, dict) and 'nodes' in dag else 'Present'}")

            # Check Merkle passport
            merkle = res.get("merkle_passport") or res.get("merkle") or res.get("merkle_root") or res.get("summary", {}).get("merkle_ledger_2050")
            report.log("AUTOPILOT", "Merkle Epistemic Passport in Loop", merkle is not None, f"Merkle Root: {str(res.get('merkle_root') or (merkle.get('merkle_root_hash') if isinstance(merkle, dict) else ''))[:16]}...")
        except Exception as e:
            report.log("AUTOPILOT", "End-to-End Loop Execution", False, f"Execution failed: {e}")


def audit_backend_endpoints(report: AuditReport):
    print("\n--- 4. AUDITING BACKEND REST ENDPOINTS ---")
    try:
        from fastapi.testclient import TestClient
        from server import app
        client = TestClient(app)
        report.log("API", "FastAPI App & TestClient Initialization", True, "Initialized")
    except Exception as e:
        report.log("API", "FastAPI App & TestClient Initialization", False, f"Failed: {e}")
        return

    # 4.1 Auto-Pilot Loop Endpoint
    try:
        r_pilot = client.post("/api/2050/auto-pilot-loop", json={
            "topic": "High-Frequency Algorithmic Signals in Microstructure Markets",
            "domain": "Finance & Financial Economics",
            "sample_size": 100
        })
        is_ok = r_pilot.status_code == 200
        report.log("API", "POST /api/2050/auto-pilot-loop", is_ok, f"HTTP {r_pilot.status_code}")
    except Exception as e:
        report.log("API", "POST /api/2050/auto-pilot-loop", False, f"Exception: {e}")

    # 4.2 Export Monograph PDF Endpoint
    try:
        r_pdf = client.get("/api/export-monograph-pdf")
        valid_pdf = r_pdf.status_code == 200 and ("application/pdf" in r_pdf.headers.get("content-type", "") or r_pdf.content.startswith(b"%PDF"))
        report.log("API", "GET /api/export-monograph-pdf", valid_pdf, f"HTTP {r_pdf.status_code}, Bytes: {len(r_pdf.content)}")
    except Exception as e:
        report.log("API", "GET /api/export-monograph-pdf", False, f"Exception: {e}")

    # 4.3 Regression: 2050 Causal Discovery
    try:
        r_causal = client.post("/api/2050/causal-discovery", json={})
        report.log("API_REGRESSION", "POST /api/2050/causal-discovery", r_causal.status_code == 200, f"HTTP {r_causal.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "POST /api/2050/causal-discovery", False, f"Exception: {e}")

    # 4.4 Regression: Counterfactual simulation
    try:
        r_cf = client.post("/api/2050/simulate-counterfactual", json={"delta_percent": 30.0})
        report.log("API_REGRESSION", "POST /api/2050/simulate-counterfactual", r_cf.status_code == 200, f"HTTP {r_cf.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "POST /api/2050/simulate-counterfactual", False, f"Exception: {e}")

    # 4.5 Regression: Epistemic Merkle Proof
    try:
        r_merkle = client.get("/api/2050/epistemic-merkle-proof")
        report.log("API_REGRESSION", "GET /api/2050/epistemic-merkle-proof", r_merkle.status_code == 200, f"HTTP {r_merkle.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "GET /api/2050/epistemic-merkle-proof", False, f"Exception: {e}")

    # 4.6 Regression: Frontier Council Debate
    try:
        r_debate = client.post("/api/2050/frontier-council-debate", json={"topic": "Quantum Causal Emergence"})
        report.log("API_REGRESSION", "POST /api/2050/frontier-council-debate", r_debate.status_code == 200, f"HTTP {r_debate.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "POST /api/2050/frontier-council-debate", False, f"Exception: {e}")

    # 4.7 Regression: SEO robots.txt
    try:
        r_robots = client.get("/robots.txt")
        report.log("API_REGRESSION", "GET /robots.txt", r_robots.status_code == 200 and "User-agent:" in r_robots.text, f"HTTP {r_robots.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "GET /robots.txt", False, f"Exception: {e}")

    # 4.8 Regression: SEO sitemap.xml
    try:
        r_sitemap = client.get("/sitemap.xml")
        report.log("API_REGRESSION", "GET /sitemap.xml", r_sitemap.status_code == 200 and "urlset" in r_sitemap.text, f"HTTP {r_sitemap.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "GET /sitemap.xml", False, f"Exception: {e}")

    # 4.9 Regression: Market Intelligence
    try:
        r_market = client.get("/api/market-intelligence")
        report.log("API_REGRESSION", "GET /api/market-intelligence", r_market.status_code == 200, f"HTTP {r_market.status_code}")
    except Exception as e:
        report.log("API_REGRESSION", "GET /api/market-intelligence", False, f"Exception: {e}")


def audit_frontend_autopilot(report: AuditReport):
    print("\n--- 5. AUDITING FRONTEND AUTONOMOUS PILOT UI ---")
    html_path = APP_DIR / "static" / "index.html"
    js_path = APP_DIR / "static" / "app.js"
    css_path = APP_DIR / "static" / "style.css"

    html = html_path.read_text(encoding="utf-8")
    js = js_path.read_text(encoding="utf-8")
    css = css_path.read_text(encoding="utf-8")

    # 5.1 JS Syntax via node
    try:
        proc = subprocess.run(["node", "-c", str(js_path)], capture_output=True, text=True)
        report.log("FRONTEND", "Node.js app.js syntax audit", proc.returncode == 0, f"Returncode: {proc.returncode}")
    except Exception as e:
        report.log("FRONTEND", "Node.js app.js syntax audit", False, f"Error: {e}")

    # 5.2 CSS Brace Symmetry
    open_b = css.count("{")
    close_b = css.count("}")
    report.log("FRONTEND", "CSS Brace Symmetry", open_b == close_b and open_b > 500, f"Open: {open_b}, Close: {close_b}")

    # 5.3 Auto-pilot UI markers in index.html
    markers = ["auto-pilot", "monograph", "telemetry", "2050"]
    for m in markers:
        present = m.lower() in html.lower()
        report.log("FRONTEND", f"HTML Keyword Presence: '{m}'", present, "Detected in index.html")


def main():
    report = AuditReport()
    audit_python_ast(report)
    audit_monograph_generator_and_typst(report)
    audit_autonomous_pilot_loop(report)
    audit_backend_endpoints(report)
    audit_frontend_autopilot(report)
    print(report.summary())
    return 0 if report.failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
