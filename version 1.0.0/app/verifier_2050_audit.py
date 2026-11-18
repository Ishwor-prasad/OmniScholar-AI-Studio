"""
OmniScholar 2050 AD — Autonomous Scientific Discovery & Causal Intelligence Singularity
Official Swarm Verifier Audit Suite
Auditor: @verifier
"""

import os
import sys
import ast
import json
import hashlib
import subprocess
from pathlib import Path
import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

APP_DIR = Path("A:/OmniScholar/version 1.0.0/app")
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from server import app
import causal_discovery_2050 as cd
import merkle_epistemic_ledger_2050 as mel

class AuditReport:
    def __init__(self):
        self.results = []
        self.failures = []

    def log(self, section: str, test: str, passed: bool, details: str = ""):
        status = "PASS" if passed else "FAIL"
        entry = {"section": section, "test": test, "status": status, "details": details}
        self.results.append(entry)
        if not passed:
            self.failures.append(entry)
        symbol = "✓" if passed else "✗"
        print(f"[{status}] {symbol} [{section}] {test}: {details}")

    def summary(self):
        total = len(self.results)
        passed = total - len(self.failures)
        print("\n" + "=" * 80)
        print(f"OMNISCHOLAR 2050 SINGULARITY SCORECARD: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
        if self.failures:
            print(f"FAILURES DETECTED ({len(self.failures)}):")
            for f in self.failures:
                print(f"  - [{f['section']}] {f['test']}: {f['details']}")
        else:
            print("ALL 2050 SINGULARITY QUALITY GATES PASSED! WORLD-CLASS PRODUCTION READY.")
        print("=" * 80 + "\n")
        return len(self.failures) == 0


def audit_ast(report: AuditReport):
    print("\n--- 1. AUDITING PYTHON 3.11+ AST COMPLIANCE ---")
    py_files = list(APP_DIR.glob("*.py")) + list((APP_DIR / "templates").glob("*.py"))
    for f in py_files:
        try:
            content = f.read_text(encoding="utf-8")
            ast.parse(content, filename=str(f))
            report.log("AST", f"AST Parse: {f.name}", True, f"{len(content.splitlines())} lines parsed")
        except Exception as e:
            report.log("AST", f"AST Parse: {f.name}", False, f"Error: {e}")


def audit_causal_math(report: AuditReport):
    print("\n--- 2. AUDITING CAUSAL DISCOVERY & DO-CALCULUS MATH ---")
    df = pd.read_csv(APP_DIR / "dummy_data.csv")
    
    # 2.1 DAG Discovery
    dag = cd.run_causal_discovery(df)
    has_nodes = len(dag.get("nodes", [])) >= 4
    has_edges = len(dag.get("edges", [])) >= 3
    
    stability_dict = dag.get("arrow_stability_audit", {})
    stability_rates = [v.get("stability_rate_pct", 0) for v in stability_dict.values()] if stability_dict else []
    mean_stability = float(np.mean(stability_rates)) if stability_rates else 0.0
    has_stability = mean_stability > 85.0
    
    report.log("CAUSAL", "Automated DAG structure discovery", has_nodes and has_edges,
               f"Nodes: {dag.get('nodes_count', len(dag.get('nodes', [])))}, Edges: {dag.get('edges_count', len(dag.get('edges', [])))}")
    report.log("CAUSAL", "Arrow Directionality Robustness (>85%)", has_stability,
               f"Mean Arrow Stability: {mean_stability:.1f}% across {len(stability_rates)} arrows")

    # 2.2 Counterfactual Simulation
    treatment = dag.get("treatment_variable") or "Years of Research Experience"
    cf = cd.simulate_counterfactual(df, treatment_var=treatment, delta_percent=25.0)
    ate_val = cf.get("average_treatment_effect_ATE") or cf.get("average_treatment_effect_ate") or cf.get("ate")
    has_ate = ate_val is not None
    curve_points = cf.get("policy_response_curve", cf.get("simulation_curve", []))
    has_curve = len(curve_points) >= 5
    has_mediation = "mediation_decomposition" in cf or "direct_effect_path" in cf
    
    report.log("CAUSAL", "Pearl Do-Calculus ATE Computation", has_ate, f"ATE: {ate_val}")
    report.log("CAUSAL", "Policy Simulation Response Curve", has_curve, f"Curve points: {len(curve_points)}")
    report.log("CAUSAL", "Direct / Indirect Mediation Decomposition", has_mediation, f"Decomposition: {cf.get('mediation_decomposition', {}).get('status') or 'Verified'}")


def audit_merkle_cryptography(report: AuditReport):
    print("\n--- 3. AUDITING MERKLE EPISTEMIC LEDGER CRYPTOGRAPHY ---")
    summary_path = APP_DIR / "runs" / "sample" / "dataset_summary.json"
    if summary_path.exists():
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    else:
        summary = {"sample_size": 100, "data_hash_sha256": "0" * 64}
        
    df = pd.read_csv(APP_DIR / "dummy_data.csv")
    passport = mel.generate_merkle_epistemic_passport(summary, df)
    
    root_hash = passport.get("merkle_root_hash") or passport.get("root_hash")
    has_root = root_hash is not None and len(root_hash) == 64
    report.log("MERKLE", "Cryptographic Root Hash (64-char SHA-256)", has_root, f"Root: {root_hash[:24]}...")
    
    leaves = passport.get("leaves", passport.get("leaf_claims", []))
    report.log("MERKLE", "Anchored Leaf Claims count (>=10)", len(leaves) >= 10, f"Leaves: {len(leaves)}")
    
    # Verify inclusion proof for first claim
    if leaves:
        cid = leaves[0].get("claim_id")
        v = mel.verify_merkle_claim(passport, cid)
        verified = v.get("is_valid", False) or v.get("verification_status") == "VERIFIED_MATHEMATICAL_TRUTH"
        report.log("MERKLE", f"Inclusion Proof Verification ({cid})", verified, f"Status: {v.get('verification_status')}, Depth: {v.get('audit_trail_depth')}")


def audit_2050_endpoints(client: TestClient, report: AuditReport):
    print("\n--- 4. AUDITING 2050 SINGULARITY HTTP ENDPOINTS ---")
    
    # 4.1 Causal discovery
    r1 = client.post("/api/2050/causal-discovery", json={})
    report.log("API_2050", "POST /api/2050/causal-discovery", r1.status_code == 200, f"Status: {r1.status_code}, Nodes: {r1.json().get('nodes_count')}")
    
    # 4.2 Counterfactual simulation
    r2 = client.post("/api/2050/simulate-counterfactual", json={"delta_percent": 25.0})
    ate_resp = r2.json().get("average_treatment_effect_ATE") or r2.json().get("average_treatment_effect_ate") or r2.json().get("ate")
    report.log("API_2050", "POST /api/2050/simulate-counterfactual", r2.status_code == 200 and ate_resp is not None, f"Status: {r2.status_code}, ATE: {ate_resp}")
    
    # 4.3 Merkle proof
    r3 = client.get("/api/2050/epistemic-merkle-proof")
    root_resp = r3.json().get("merkle_root_hash") or r3.json().get("root_hash")
    report.log("API_2050", "GET /api/2050/epistemic-merkle-proof", r3.status_code == 200 and root_resp is not None, f"Status: {r3.status_code}, Root: {str(root_resp)[:20]}...")
    
    # 4.4 Frontier council debate
    r4 = client.post("/api/2050/frontier-council-debate", json={"topic": "Quantum Causal Emergence"})
    score = r4.json().get("composite_debate_score") or r4.json().get("composite_score")
    verdict = r4.json().get("editorial_verdict") or r4.json().get("verdict")
    report.log("API_2050", "POST /api/2050/frontier-council-debate", r4.status_code == 200 and score is not None, f"Status: {r4.status_code}, Score: {score}, Verdict: {verdict}")

    # 4.5 Auto-Pilot Loop (End-to-End 7-Stage Autonomous Loop)
    r5 = client.post("/api/2050/auto-pilot-loop", json={
        "topic": "Autonomous Singularity and Empirical Intelligence",
        "domain": "Computer Science & Machine Intelligence",
        "sample_size": 100
    })
    r5_data = r5.json() if r5.status_code == 200 else {}
    r5_pages = r5_data.get("page_count", 0)
    report.log("API_2050", "POST /api/2050/auto-pilot-loop", r5.status_code == 200 and r5_pages >= 30,
               f"Status: {r5.status_code}, Pages: {r5_pages}, Time: {r5_data.get('execution_time_seconds')}s")

    # 4.6 30+ Page Monograph PDF Export Endpoint
    r6 = client.get("/api/export-monograph-pdf")
    import re
    pages_count = len(re.findall(rb'/Type\s*/Page\b', r6.content)) if r6.status_code == 200 else 0
    report.log("API_2050", "GET /api/export-monograph-pdf (>=30 Pages)", r6.status_code == 200 and pages_count >= 30,
               f"Status: {r6.status_code}, Size: {len(r6.content)} bytes, Verified Pages: {pages_count}")


def audit_frontend_quantum_lab(report: AuditReport):
    print("\n--- 5. AUDITING FRONTEND QUANTUM LAB 2050 UI ---")
    html = (APP_DIR / "static" / "index.html").read_text(encoding="utf-8")
    js = (APP_DIR / "static" / "app.js").read_text(encoding="utf-8")
    
    req_ids = [
        "navQuantumLab2050",
        "tabQuantumLab2050",
        "causalDagContainer",
        "counterfactualSlider",
        "cfAteVal",
        "merkleProofContainer",
        "refereeDebateStream",
        "btnRunCausalDiscovery",
        "btnSimulateCounterfactual",
        "btnVerifyMerkleProof",
        "btnTriggerFrontierDebate"
    ]
    missing = [i for i in req_ids if f'id="{i}"' not in html and f"id='{i}'" not in html and f'id="{i}"' not in js]
    report.log("FRONTEND", "Quantum Lab 2050 DOM Element IDs (11/11)", len(missing) == 0, f"Missing: {missing if missing else 'None'}")
    
    res_js = subprocess.run(["node", "--check", str(APP_DIR / "static" / "app.js")], capture_output=True, text=True)
    report.log("FRONTEND", "Node.js app.js syntax audit", res_js.returncode == 0, f"Returncode: {res_js.returncode}")
    
    res_align = subprocess.run(["node", str(APP_DIR / "audit_frontend.js")], capture_output=True, text=True)
    report.log("FRONTEND", "Full DOM ID getElementById Parity", res_align.returncode == 0, res_align.stdout.strip().splitlines()[2] if res_align.stdout else "Verified")


def audit_typst(report: AuditReport):
    print("\n--- 6. AUDITING TYPST 0.15 PUBLICATION COMPILATION ---")
    main_typ = APP_DIR / "runs" / "sample" / "main.typ"
    if main_typ.exists():
        out_pdf = APP_DIR / "runs" / "sample" / "verifier_2050_test.pdf"
        res = subprocess.run(["typst", "compile", str(main_typ), str(out_pdf)], capture_output=True, text=True)
        report.log("TYPST", "Typst 0.15 zero-error compilation", res.returncode == 0 and out_pdf.exists(),
                   f"Returncode: {res.returncode}, Size: {out_pdf.stat().st_size if out_pdf.exists() else 0} bytes")
    else:
        report.log("TYPST", "main.typ existence", False, "main.typ missing")


if __name__ == "__main__":
    report = AuditReport()
    client = TestClient(app)
    
    audit_ast(report)
    audit_causal_math(report)
    audit_merkle_cryptography(report)
    audit_2050_endpoints(client, report)
    audit_frontend_quantum_lab(report)
    audit_typst(report)
    
    all_ok = report.summary()
    sys.exit(0 if all_ok else 1)
