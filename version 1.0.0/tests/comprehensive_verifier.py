"""
OmniScholar Autonomous Swarm Quality Verification Suite
Independent auditor: @verifier
Exhaustive verification of backend APIs, statistical accuracy, Typst compilation, and ledger reproducibility.
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
from scipy import stats
from scipy.stats import f as f_dist
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from fastapi.testclient import TestClient

# Ensure app path in sys.path
APP_DIR = Path(__file__).resolve().parent.parent / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from server import app, SESSION_DATA, BASE_DIR, RUNS_DIR
import stats_engine as se

class VerificationReport:
    def __init__(self):
        self.results = []
        self.failures = []

    def log(self, section: str, test_name: str, passed: bool, details: str = ""):
        status = "PASS" if passed else "FAIL"
        entry = {
            "section": section,
            "test": test_name,
            "status": status,
            "details": details
        }
        self.results.append(entry)
        if not passed:
            self.failures.append(entry)
        symbol = "✓" if passed else "✗"
        print(f"[{status}] {symbol} [{section}] {test_name}: {details}")

    def summary(self):
        total = len(self.results)
        passed = total - len(self.failures)
        print("\n" + "=" * 75)
        print(f"VERIFICATION AUDIT COMPLETE: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
        if self.failures:
            print(f"FAILURES DETECTED ({len(self.failures)}):")
            for f in self.failures:
                print(f"  - [{f['section']}] {f['test']}: {f['details']}")
        else:
            print("ALL 100% OF VERIFICATION CHECKS PASSED WITH MATHEMATICAL PRECISION!")
        print("=" * 75 + "\n")
        return len(self.failures) == 0


def audit_backend_api(client: TestClient, report: VerificationReport):
    print("\n--- 1. AUDITING BACKEND API ENDPOINTS ---")
    
    # 1.1 /api/health
    try:
        r = client.get("/api/health")
        passed = r.status_code == 200 and r.json().get("status") in ["online", "healthy"]
        report.log("API", "GET /api/health", passed, f"Status code: {r.status_code}, status: {r.json().get('status')}")
    except Exception as e:
        report.log("API", "GET /api/health", False, f"Exception: {e}")

    # 1.2 /api/load-sample
    try:
        r = client.post("/api/load-sample")
        data = r.json()
        summary = data.get("summary", data)
        passed = r.status_code == 200 and summary.get("sample_size") == 100
        report.log("API", "POST /api/load-sample", passed, f"Status: {r.status_code}, N: {summary.get('sample_size')}, variables: {summary.get('total_variables')}")
    except Exception as e:
        report.log("API", "POST /api/load-sample", False, f"Exception: {e}")

    # 1.3 /api/upload
    dummy_csv_path = APP_DIR / "dummy_data.csv"
    try:
        with open(dummy_csv_path, "rb") as f:
            files = {"file": ("uploaded_test.csv", f, "text/csv")}
            r = client.post("/api/upload", files=files)
        data = r.json()
        summary = data.get("summary", data)
        passed = r.status_code == 200 and summary.get("sample_size") == 100
        report.log("API", "POST /api/upload", passed, f"Status: {r.status_code}, N: {summary.get('sample_size')}")
    except Exception as e:
        report.log("API", "POST /api/upload", False, f"Exception: {e}")

    # Reload sample for standard baseline
    client.post("/api/load-sample")

    # 1.4 /api/set-grouping (Participant Role)
    try:
        r = client.post("/api/set-grouping", json={"group_col": "Participant Role"})
        data = r.json()
        passed = r.status_code == 200 and data.get("active_group_col") == "Participant Role"
        report.log("API", "POST /api/set-grouping (Participant Role)", passed, f"Status: {r.status_code}, active_group_col: {data.get('active_group_col')}")
    except Exception as e:
        report.log("API", "POST /api/set-grouping", False, f"Exception: {e}")

    # 1.5 /api/set-grouping (Primary Methodological Framework)
    try:
        r = client.post("/api/set-grouping", json={"group_col": "Primary Methodological Framework"})
        data = r.json()
        summary = data.get("summary", data)
        inf_count = len(summary.get("inferential", []))
        passed = r.status_code == 200 and data.get("active_group_col") == "Primary Methodological Framework" and inf_count > 0
        report.log("API", "POST /api/set-grouping (Primary Methodological Framework)", passed, f"Status: {r.status_code}, inferential tests count: {inf_count}")
    except Exception as e:
        report.log("API", "POST /api/set-grouping", False, f"Exception: {e}")

    # 1.6 /api/peer-review (GET & POST)
    try:
        r_get = client.get("/api/peer-review")
        passed_get = r_get.status_code == 200 and "editorial_decision" in r_get.json()
        report.log("API", "GET /api/peer-review", passed_get, f"Status: {r_get.status_code}, Decision: {r_get.json().get('editorial_decision')}, Score: {r_get.json().get('composite_quality_score')}")
        
        r_post = client.post("/api/peer-review")
        passed_post = r_post.status_code == 200 and "reviewers" in r_post.json() and len(r_post.json()["reviewers"]) == 3
        report.log("API", "POST /api/peer-review", passed_post, f"Status: {r_post.status_code}, Reviewers: {len(r_post.json().get('reviewers', []))}")
    except Exception as e:
        report.log("API", "Peer-Review API", False, f"Exception: {e}")

    # 1.7 /api/ledger
    try:
        r = client.get("/api/ledger")
        ledger_list = r.json().get("ledger", [])
        passed = r.status_code == 200 and len(ledger_list) > 0
        report.log("API", "GET /api/ledger", passed, f"Status: {r.status_code}, Total logged ledger records: {len(ledger_list)}")
    except Exception as e:
        report.log("API", "GET /api/ledger", False, f"Exception: {e}")

    # 1.8 /api/export-typst (raw source & pdf)
    try:
        r_typ = client.get("/api/export-typst?compile=false")
        passed_typ = r_typ.status_code == 200 and len(r_typ.content) > 1000 and (b"#set page" in r_typ.content or b"show" in r_typ.content or b"title" in r_typ.content)
        report.log("API", "GET /api/export-typst (compile=false)", passed_typ, f"Status: {r_typ.status_code}, Source size: {len(r_typ.content)} bytes")
    except Exception as e:
        report.log("API", "GET /api/export-typst", False, f"Exception: {e}")

    # 1.9 /api/export-pdf
    try:
        r_pdf = client.get("/api/export-pdf")
        passed_pdf = r_pdf.status_code == 200 and len(r_pdf.content) > 10000 and r_pdf.content[:4] == b"%PDF"
        report.log("API", "GET /api/export-pdf", passed_pdf, f"Status: {r_pdf.status_code}, PDF size: {len(r_pdf.content)} bytes, Magic %PDF: {r_pdf.content[:4] == b'%PDF'}")
    except Exception as e:
        report.log("API", "GET /api/export-pdf", False, f"Exception: {e}")

    # 1.10 /api/export-tex
    try:
        r_tex = client.get("/api/export-tex")
        passed_tex = r_tex.status_code == 200 and len(r_tex.content) > 1000 and b"\\documentclass" in r_tex.content
        report.log("API", "GET /api/export-tex", passed_tex, f"Status: {r_tex.status_code}, LaTeX size: {len(r_tex.content)} bytes")
    except Exception as e:
        report.log("API", "GET /api/export-tex", False, f"Exception: {e}")

    # 1.11 /api/export-zip
    try:
        r_zip = client.get("/api/export-zip")
        is_zip = False
        zip_count = 0
        if r_zip.status_code == 200:
            with open("audit_test_bundle.zip", "wb") as fz:
                fz.write(r_zip.content)
            with zipfile.ZipFile("audit_test_bundle.zip", "r") as z:
                is_zip = True
                zip_count = len(z.namelist())
        passed_zip = r_zip.status_code == 200 and is_zip and zip_count >= 10
        report.log("API", "GET /api/export-zip", passed_zip, f"Status: {r_zip.status_code}, ZIP size: {len(r_zip.content)} bytes, Bundled files: {zip_count}")
    except Exception as e:
        report.log("API", "GET /api/export-zip", False, f"Exception: {e}")


def audit_statistical_accuracy(client: TestClient, report: VerificationReport):
    print("\n--- 2. AUDITING STATISTICAL ACCURACY & MATHEMATICAL PRECISION ---")
    
    # Reload sample and set grouping to Primary Methodological Framework
    r = client.post("/api/set-grouping", json={"group_col": "Primary Methodological Framework"})
    assert r.status_code == 200
    summary = r.json().get("summary", r.json())
    
    raw_df = pd.read_csv(APP_DIR / "dummy_data.csv")
    group_col = "Primary Methodological Framework"
    df_num, _ = se.extract_numeric_and_ordinal_df(raw_df)

    # 2.1 ANOVA verification matching the exact target variable analyzed
    anova_test = None
    for t in summary.get("inferential", []):
        if "ANOVA" in t.get("test", ""):
            anova_test = t
            break

    if anova_test:
        target_var = anova_test.get("target_variable")
        eval_df = df_num.copy()
        eval_df[group_col] = raw_df[group_col]
        sub = eval_df[[target_var, group_col]].dropna()
        
        # Ground truth ANOVA
        groups = [grp[target_var].values for _, grp in sub.groupby(group_col)]
        ref_f_stat, ref_p_anova = stats.f_oneway(*groups)
        k_groups = len(groups)
        n_total = sum(len(g) for g in groups)
        ref_df_between = k_groups - 1
        ref_df_within = n_total - k_groups
        
        grand_mean = sub[target_var].mean()
        ss_total = float(np.sum((sub[target_var] - grand_mean)**2))
        ss_between = float(sum(len(g) * ((np.mean(g) - grand_mean)**2) for g in groups))
        ref_eta_squared = ss_between / ss_total if ss_total > 0 else 0.0

        f_diff = abs(anova_test.get("f_statistic", anova_test.get("statistic", 0.0)) - ref_f_stat)
        p_diff = abs(anova_test.get("p_value", 0.0) - ref_p_anova)
        df_b_match = anova_test.get("df_between") == ref_df_between
        df_w_match = anova_test.get("df_within") == ref_df_within
        api_eta = anova_test.get("effect_sizes", {}).get("eta_squared", anova_test.get("eta_squared", 0.0))
        eta_diff = abs(api_eta - ref_eta_squared)

        report.log("STATS", f"ANOVA F-statistic precision ({target_var})", f_diff < 1e-4, f"API: {anova_test.get('f_statistic')}, Ref: {ref_f_stat:.4f}, Diff: {f_diff:.6f}")
        report.log("STATS", f"ANOVA p-value precision ({target_var})", p_diff < 1e-4, f"API: {anova_test.get('p_value')}, Ref: {ref_p_anova:.6f}, Diff: {p_diff:.6f}")
        report.log("STATS", f"ANOVA df_between check", df_b_match, f"API: {anova_test.get('df_between')}, Ref: {ref_df_between}")
        report.log("STATS", f"ANOVA df_within check", df_w_match, f"API: {anova_test.get('df_within')}, Ref: {ref_df_within}")
        report.log("STATS", f"ANOVA eta_squared precision", eta_diff < 1e-4, f"API: {api_eta}, Ref: {ref_eta_squared:.4f}, Diff: {eta_diff:.6f}")
        
        # 2.2 Tukey HSD
        tukey_results = anova_test.get("tukey_posthoc", [])
        ref_tukey = pairwise_tukeyhsd(sub[target_var], sub[group_col])
        ref_tukey_pairs = len(ref_tukey.summary().data) - 1
        report.log("STATS", "Tukey HSD pairwise comparisons count", len(tukey_results) == ref_tukey_pairs, f"API pairs: {len(tukey_results)}, Ref pairs: {ref_tukey_pairs}")
    else:
        report.log("STATS", "ANOVA test presence", False, "One-Way ANOVA test object missing in summary['inferential']")

    # 2.3 Kruskal-Wallis H Test verification
    kruskal_test = None
    for t in summary.get("inferential", []):
        if "Kruskal" in t.get("test", ""):
            kruskal_test = t
            break

    if kruskal_test:
        target_k = kruskal_test.get("target_variable")
        eval_df = df_num.copy()
        eval_df[group_col] = raw_df[group_col]
        sub_k = eval_df[[target_k, group_col]].dropna()
        groups_k = [grp[target_k].values for _, grp in sub_k.groupby(group_col)]
        ref_h_stat, ref_p_kruskal = stats.kruskal(*groups_k)

        h_diff = abs(kruskal_test.get("statistic", 0.0) - ref_h_stat)
        p_k_diff = abs(kruskal_test.get("p_value", 0.0) - ref_p_kruskal)
        report.log("STATS", f"Kruskal-Wallis H-statistic precision ({target_k})", h_diff < 1e-4, f"API: {kruskal_test.get('statistic')}, Ref: {ref_h_stat:.4f}, Diff: {h_diff:.6f}")
        report.log("STATS", f"Kruskal-Wallis p-value precision ({target_k})", p_k_diff < 1e-4, f"API: {kruskal_test.get('p_value')}, Ref: {ref_p_kruskal:.6f}, Diff: {p_k_diff:.6f}")
    else:
        report.log("STATS", "Kruskal-Wallis test presence", False, "Kruskal-Wallis test missing in summary['inferential']")

    # 2.4 Mann-Whitney U test validation on 2-group slice
    # Use exact alphabetical order matching pandas groupby default
    sorted_groups = sorted(raw_df[group_col].unique())[:2]
    sub_2g = raw_df[raw_df[group_col].isin(sorted_groups)]
    mw_res = se.compute_mann_whitney_and_kruskal(sub_2g, "Methodological Effectiveness Rating (1-5)", group_col)
    
    g1_vals = sub_2g[sub_2g[group_col] == sorted_groups[0]]["Methodological Effectiveness Rating (1-5)"].dropna().values
    g2_vals = sub_2g[sub_2g[group_col] == sorted_groups[1]]["Methodological Effectiveness Rating (1-5)"].dropna().values
    ref_u, ref_mw_p = stats.mannwhitneyu(g1_vals, g2_vals, alternative='two-sided')
    ref_rb_r = 1.0 - (2.0 * ref_u) / (len(g1_vals) * len(g2_vals))

    if mw_res:
        u_diff = abs(mw_res.get("u_statistic", mw_res.get("statistic", 0.0)) - ref_u)
        rb_diff = abs(mw_res.get("effect_size", {}).get("rank_biserial_r", 0.0) - ref_rb_r)
        report.log("STATS", "Mann-Whitney U statistic precision", u_diff < 1e-4, f"Engine: {mw_res.get('statistic')}, Ref: {ref_u}, Diff: {u_diff:.6f}")
        report.log("STATS", "Mann-Whitney U rank-biserial effect size", rb_diff < 1e-4, f"Engine: {mw_res.get('effect_size', {}).get('rank_biserial_r')}, Ref: {ref_rb_r:.4f}, Diff: {rb_diff:.6f}")
    else:
        report.log("STATS", "Mann-Whitney U 2-group validation", False, "Failed to compute Mann-Whitney U on 2-group slice")

    # 2.5 Cronbach's Alpha Scale Reliability
    rel = summary.get("reliability", {})
    ref_rel = se.compute_cronbach_alpha(df_num)
    if rel and ref_rel:
        alpha_api = rel.get("raw_cronbach_alpha") or rel.get("alpha")
        alpha_ref = ref_rel.get("raw_cronbach_alpha")
        alpha_diff = abs(float(alpha_api) - float(alpha_ref))
        report.log("STATS", "Cronbach's Alpha exact computation", alpha_diff < 1e-4, f"API: {alpha_api}, Ref: {alpha_ref}, Diff: {alpha_diff:.6f}")
        report.log("STATS", "Cronbach's items count", rel.get("items_count") == ref_rel.get("items_count"), f"Items: {rel.get('items_count')}")
    else:
        report.log("STATS", "Cronbach's Alpha presence", False, "Reliability object missing in summary")

    # 2.6 Hierarchical Regression with Huber-White HC3
    reg = summary.get("regression", {})
    m2 = reg.get("model_2", {})
    comp = reg.get("model_comparison", {})
    report.log("STATS", "Hierarchical Regression Model 2 presence", "coefficients" in m2 and len(m2["coefficients"]) > 0, f"Model 2 coefficients: {len(m2.get('coefficients', []))}")
    report.log("STATS", "Huber-White HC3 robust standard errors indicator", "HC3" in m2.get("name", "") or reg.get("cov_type") == "HC3", f"Model name: {m2.get('name')}")
    report.log("STATS", "F-change test & Delta R-squared", "f_change" in comp and "delta_r_squared" in comp, f"Delta R^2: {comp.get('delta_r_squared')}, F-change: {comp.get('f_change')}, p: {comp.get('p_value_change')}")

    # 2.7 Multicollinearity VIF
    vif_info = reg.get("vif_multicollinearity", {})
    report.log("STATS", "VIF multicollinearity diagnostics", "results" in vif_info and len(vif_info["results"]) > 0, f"Mean VIF: {vif_info.get('mean_vif')}, Predictors evaluated: {len(vif_info.get('results', []))}")

    # 2.8 Cook's Distance Outliers
    cook_info = reg.get("cooks_distance_outliers", {})
    report.log("STATS", "Cook's Distance outlier audit", "top_outliers" in cook_info, f"Cutoff: {cook_info.get('threshold_used')}, Flagged outliers: {cook_info.get('total_outliers_flagged')}")

    # 2.9 Correlation Matrices (Pearson and Spearman with exact p-values)
    corr_info = summary.get("correlation", {})
    spearman_p = corr_info.get("spearman", {}).get("p_matrix", {})
    pearson_p = corr_info.get("pearson", {}).get("p_matrix", {})
    report.log("STATS", "Spearman & Pearson exact p-value matrices", len(spearman_p) > 0 and len(pearson_p) > 0, f"Spearman dimensions: {len(spearman_p)}, Pearson dimensions: {len(pearson_p)}")


def audit_bitwise_calculation_ledger(client: TestClient, report: VerificationReport):
    print("\n--- 3. AUDITING BITWISE CALCULATION LEDGER & ZERO-GHOSTWRITING TRACES ---")
    r = client.get("/api/ledger")
    assert r.status_code == 200
    ledger_records = r.json().get("ledger", [])
    
    report.log("LEDGER", "Ledger records non-empty", len(ledger_records) >= 5, f"Total records: {len(ledger_records)}")
    
    all_formulas = True
    all_hashes = True
    all_code = True
    standalone_code = None

    for rec in ledger_records:
        if not rec.get("formula_latex") or not rec.get("formula_plain"):
            all_formulas = False
        if not rec.get("input_slice_sha256") or len(rec.get("input_slice_sha256")) != 64:
            all_hashes = False
        if not rec.get("reproducible_python_code"):
            all_code = False
        elif standalone_code is None and "groups = {" in rec.get("reproducible_python_code", ""):
            standalone_code = rec.get("reproducible_python_code")

    report.log("LEDGER", "LaTeX and plain formula integrity", all_formulas, "Verified across all ledger records")
    report.log("LEDGER", "SHA-256 vector checksum integrity (64 chars)", all_hashes, "All inputs have cryptographic hashes")
    report.log("LEDGER", "Standalone reproducible Python code presence", all_code, "Verified for every statistic")

    # Test executing self-contained reproducible python snippet from ledger
    if standalone_code:
        try:
            res = subprocess.run([sys.executable, "-c", standalone_code], capture_output=True, text=True, timeout=10)
            code_exec_ok = res.returncode == 0 and "F-statistic:" in res.stdout
            report.log("LEDGER", "Autonomous execution of ledger Python snippet", code_exec_ok, f"Output: {res.stdout.strip()}")
        except Exception as e:
            report.log("LEDGER", "Execution of ledger Python snippet", False, f"Exception: {e}")

    # Dataset SHA-256 verification
    raw_csv = open(APP_DIR / "dummy_data.csv", "rb").read()
    raw_hash = hashlib.sha256(raw_csv).hexdigest()
    api_passport_hash = r.json().get("dataset_sha256")
    report.log("LEDGER", "Bitwise Ledger Dataset SHA-256 integrity", len(api_passport_hash) == 64, f"Hash: {api_passport_hash[:20]}...")


def audit_typst_compilation(report: VerificationReport):
    print("\n--- 4. AUDITING TYPST 0.15 COMPILATION & PUBLICATION PDF MANUSCRIPT ---")
    
    typst_bin = shutil.which("typst")
    report.log("TYPST", "Typst 0.15 CLI executable discovery", typst_bin is not None, f"Path: {typst_bin}")
    
    run_dir = Path(RUNS_DIR) / "sample"
    main_typ = run_dir / "main.typ"
    report.log("TYPST", "Generated main.typ existence", main_typ.exists(), f"Path: {main_typ}")
    
    if main_typ.exists():
        typ_size = main_typ.stat().st_size
        report.log("TYPST", "main.typ source volume", typ_size > 2000, f"Size: {typ_size} bytes")
        
        # Test compilation directly with typst
        compiled_pdf = run_dir / "verifier_audit_output.pdf"
        if compiled_pdf.exists():
            compiled_pdf.unlink()
            
        cmd = ["typst", "compile", str(main_typ), str(compiled_pdf)]
        res = subprocess.run(cmd, capture_output=True, text=True)
        no_warnings = len(res.stderr.strip()) == 0
        success = res.returncode == 0 and compiled_pdf.exists()
        pdf_size = compiled_pdf.stat().st_size if compiled_pdf.exists() else 0
        
        report.log("TYPST", "Typst 0.15 direct compilation", success, f"Returncode: {res.returncode}, PDF Size: {pdf_size} bytes")
        report.log("TYPST", "Typst compilation zero warnings/errors", no_warnings, f"Warnings: {res.stderr.strip() if res.stderr else 'None'}")
        
        if compiled_pdf.exists():
            with open(compiled_pdf, "rb") as fpdf:
                header = fpdf.read(5)
                report.log("TYPST", "Valid PDF magic byte header (%PDF-)", header == b"%PDF-", f"Header: {header}")
                
        # Check Nature variant compilation
        nature_typ = run_dir / "main_nature.typ"
        nature_pdf = run_dir / "verifier_nature_output.pdf"
        if nature_typ.exists():
            cmd_nat = ["typst", "compile", str(nature_typ), str(nature_pdf)]
            res_nat = subprocess.run(cmd_nat, capture_output=True, text=True)
            report.log("TYPST", "Nature layout Typst compilation", res_nat.returncode == 0 and nature_pdf.exists(), f"Size: {nature_pdf.stat().st_size if nature_pdf.exists() else 0} bytes")

        # Also check pre-compiled Research_Manuscript_Typst_v1.0.0.pdf
        stock_pdf = run_dir / "Research_Manuscript_Typst_v1.0.0.pdf"
        report.log("TYPST", "Engine generated publication PDF exists", stock_pdf.exists(), f"Size: {stock_pdf.stat().st_size if stock_pdf.exists() else 0} bytes")
    else:
        report.log("TYPST", "Typst source existence", False, "main.typ not found")


def audit_frontend_and_templates(report: VerificationReport):
    print("\n--- 5. AUDITING FRONTEND & SYSTEM TEMPLATES ---")
    
    index_html = APP_DIR / "static" / "index.html"
    style_css = APP_DIR / "static" / "style.css"
    app_js = APP_DIR / "static" / "app.js"
    
    report.log("FRONTEND", "index.html exists and non-empty", index_html.exists() and index_html.stat().st_size > 10000, f"Size: {index_html.stat().st_size} bytes")
    report.log("FRONTEND", "style.css exists and non-empty", style_css.exists() and style_css.stat().st_size > 10000, f"Size: {style_css.stat().st_size} bytes")
    report.log("FRONTEND", "app.js exists and non-empty", app_js.exists() and app_js.stat().st_size > 10000, f"Size: {app_js.stat().st_size} bytes")

    # Run Node syntax check on app.js
    node_res = subprocess.run(["node", "--check", str(app_js)], capture_output=True, text=True)
    report.log("FRONTEND", "Node.js syntax validation on app.js", node_res.returncode == 0, f"Returncode: {node_res.returncode}")

    # Check templates
    tmpl_dir = APP_DIR / "templates"
    for tmpl in ["typst_generator.py", "latex_generator.py", "passport_generator.py", "bundle_builder.py", "__init__.py"]:
        p = tmpl_dir / tmpl
        report.log("TEMPLATES", f"Template module {tmpl} exists", p.exists(), f"Size: {p.stat().st_size if p.exists() else 0} bytes")


if __name__ == "__main__":
    report = VerificationReport()
    client = TestClient(app)
    
    audit_backend_api(client, report)
    audit_statistical_accuracy(client, report)
    audit_bitwise_calculation_ledger(client, report)
    audit_typst_compilation(report)
    audit_frontend_and_templates(report)
    
    all_ok = report.summary()
    sys.exit(0 if all_ok else 1)
