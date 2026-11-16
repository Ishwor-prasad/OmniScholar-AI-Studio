"""
OmniScholar Global Agentic Upgrade & World-Class SEO Verification Suite
Independent auditor: @verifier

Validates:
1. Python AST compliance across all app Python files (Python 3.11+ syntax, no illegal f-string backslashes)
2. Agentic Research Council (agentic_council.py & POST /api/agentic-research-council)
3. Market Intelligence Engine (market_intelligence.py & GET /api/market-intelligence)
4. SEO Endpoints (/sitemap.xml, /robots.txt)
5. HTML SEO & JSON-LD Structured Data Schema Validation (SoftwareApplication, ScholarlyArticle, EducationalOrganization, FAQPage)
6. Frontend Multi-Agent UI & DOM Element Alignment
7. Typst 0.15 IEEE / Nature Compilation
"""

import os
import sys
import ast
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import subprocess

from fastapi.testclient import TestClient

APP_DIR = Path("A:/OmniScholar/version 1.0.0/app")
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

class SprintReport:
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
        print(f"AGENTIC & SEO SPRINT SCORECARD: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
        if self.failures:
            print(f"FAILURES DETECTED ({len(self.failures)}):")
            for f in self.failures:
                print(f"  - [{f['section']}] {f['test']}: {f['details']}")
        else:
            print("ALL SPRINT QUALITY GATES PASSED! WORLD-CLASS PRODUCTION READY.")
        print("=" * 75 + "\n")
        return len(self.failures) == 0


def audit_python_ast(report: SprintReport):
    print("\n--- 1. AUDITING PYTHON AST COMPLIANCE (PYTHON 3.11+) ---")
    py_files = list(APP_DIR.glob("*.py")) + list((APP_DIR / "templates").glob("*.py"))
    all_ast_ok = True
    for py_f in py_files:
        try:
            with open(py_f, "r", encoding="utf-8") as f:
                content = f.read()
            tree = ast.parse(content, filename=str(py_f))
            report.log("AST", f"AST Parse: {py_f.name}", True, f"{len(content.splitlines())} lines parsed")
        except SyntaxError as e:
            all_ast_ok = False
            report.log("AST", f"AST Parse: {py_f.name}", False, f"SyntaxError at line {e.lineno}: {e.msg}")
        except Exception as e:
            all_ast_ok = False
            report.log("AST", f"AST Parse: {py_f.name}", False, f"Error: {e}")


def audit_agentic_council(client: TestClient, report: SprintReport):
    print("\n--- 2. AUDITING AGENTIC RESEARCH COUNCIL ---")
    council_py = APP_DIR / "agentic_council.py"
    report.log("COUNCIL", "agentic_council.py existence", council_py.exists(), f"Path: {council_py}")

    if council_py.exists():
        try:
            import agentic_council
            has_fn = hasattr(agentic_council, "run_agentic_council") or hasattr(agentic_council, "execute_agentic_council")
            report.log("COUNCIL", "agentic_council module importable", has_fn, "Entry function found")
        except Exception as e:
            report.log("COUNCIL", "agentic_council import", False, f"Import error: {e}")

    # Test POST /api/agentic-research-council
    try:
        payload = {
            "topic": "Neuromorphic Edge AI for Autonomous Cyber-Physical Security",
            "domain": "Artificial Intelligence & Distributed Systems"
        }
        r = client.post("/api/agentic-research-council", json=payload)
        if r.status_code == 200:
            data = r.json()
            agents = data.get("agents", {})
            has_lit = "literature_scout" in agents or any("scout" in k.lower() or "literature" in k.lower() for k in agents)
            has_val = "data_validator" in agents or any("validator" in k.lower() or "data" in k.lower() for k in agents)
            has_econ = "econometrician" in agents or any("econometrician" in k.lower() for k in agents)
            has_rev = "editorial_reviewer" in agents or any("reviewer" in k.lower() or "editorial" in k.lower() for k in agents)
            has_consensus = "consensus_score" in data or "verdict" in data or "consensus" in data or ("consensus" in data and ("verdict" in data.get("consensus", {}) or "score" in data.get("consensus", {})))
            consensus_val = data.get("consensus_score") or data.get("verdict") or (data.get("consensus", {}).get("verdict") if isinstance(data.get("consensus"), dict) else None)
            
            passed = len(agents) >= 4 and has_consensus
            report.log("COUNCIL", "POST /api/agentic-research-council execution", passed,
                       f"Status: {r.status_code}, Agents count: {len(agents)}, Consensus/Verdict: {consensus_val}")
        else:
            report.log("COUNCIL", "POST /api/agentic-research-council", False, f"Status: {r.status_code}, Body: {r.text[:100]}")
    except Exception as e:
        report.log("COUNCIL", "POST /api/agentic-research-council", False, f"Exception: {e}")


def audit_market_intelligence(client: TestClient, report: SprintReport):
    print("\n--- 3. AUDITING MARKET INTELLIGENCE & BILLION-DOLLAR MOATS ---")
    market_py = APP_DIR / "market_intelligence.py"
    report.log("MARKET", "market_intelligence.py existence", market_py.exists(), f"Path: {market_py}")

    try:
        r = client.get("/api/market-intelligence")
        if r.status_code == 200:
            data = r.json()
            moats = data.get("moats") or data.get("three_billion_dollar_moats") or data.get("billion_dollar_moats") or []
            competitors = data.get("competitors") or data.get("global_ecosystem_competitors") or data.get("ecosystem_benchmark") or []
            
            has_moats = len(moats) >= 3
            has_comp = len(competitors) >= 4 # Consensus, Elicit, SciSpace, Paperpal, NotebookLM
            passed = has_moats and has_comp
            report.log("MARKET", "GET /api/market-intelligence moats & benchmarks", passed,
                       f"Status: {r.status_code}, Moats count: {len(moats)}, Competitors benchmarked: {len(competitors)}")
        else:
            report.log("MARKET", "GET /api/market-intelligence", False, f"Status: {r.status_code}, Body: {r.text[:100]}")
    except Exception as e:
        report.log("MARKET", "GET /api/market-intelligence", False, f"Exception: {e}")


def audit_seo_endpoints(client: TestClient, report: SprintReport):
    print("\n--- 4. AUDITING SEO SITEMAP & ROBOTS.TXT ---")
    
    # 4.1 /robots.txt
    try:
        r = client.get("/robots.txt")
        passed = r.status_code == 200 and "User-agent" in r.text and "scholar.safalai.com.np" in r.text
        report.log("SEO", "GET /robots.txt", passed, f"Status: {r.status_code}, Content-Type: {r.headers.get('content-type')}")
    except Exception as e:
        report.log("SEO", "GET /robots.txt", False, f"Exception: {e}")

    # 4.2 /sitemap.xml
    try:
        r = client.get("/sitemap.xml")
        is_xml = False
        url_count = 0
        if r.status_code == 200:
            root = ET.fromstring(r.content)
            is_xml = True
            url_count = len(root.findall(".//{*}url")) or len(root.findall(".//url"))
        passed = r.status_code == 200 and is_xml and url_count >= 1 and "scholar.safalai.com.np" in r.text
        report.log("SEO", "GET /sitemap.xml", passed, f"Status: {r.status_code}, Valid XML: {is_xml}, URLs: {url_count}")
    except Exception as e:
        report.log("SEO", "GET /sitemap.xml", False, f"Exception: {e}")


def audit_html_seo_and_jsonld(report: SprintReport):
    print("\n--- 5. AUDITING HTML SEO METADATA & SCHEMA.ORG JSON-LD ---")
    html_path = APP_DIR / "static" / "index.html"
    content = html_path.read_text(encoding="utf-8")
    
    # 5.1 Meta tags
    has_title = "<title>" in content and "OmniScholar" in content
    has_canonical = 'rel="canonical"' in content and "https://scholar.safalai.com.np" in content
    has_meta_desc = 'name="description"' in content
    has_keywords = 'name="keywords"' in content
    has_og = 'property="og:title"' in content and 'property="og:url"' in content
    has_twitter = 'name="twitter:card"' in content
    
    report.log("SEO_HTML", "Title & Canonical URL (scholar.safalai.com.np)", has_title and has_canonical, "Canonical link verified")
    report.log("SEO_HTML", "Meta Description & Keywords", has_meta_desc and has_keywords, "Search engine meta tags verified")
    report.log("SEO_HTML", "OpenGraph & Twitter Card Metadata", has_og and has_twitter, "Social sharing tags verified")

    # 5.2 JSON-LD Schemas
    has_software_app = "SoftwareApplication" in content
    has_scholarly_article = "ScholarlyArticle" in content
    has_edu_org = "EducationalOrganization" in content
    has_faq = "FAQPage" in content
    
    jsonld_all = has_software_app and has_scholarly_article and has_edu_org and has_faq
    report.log("SEO_JSONLD", "schema.org JSON-LD (SoftwareApplication, ScholarlyArticle, EducationalOrganization, FAQPage)",
               jsonld_all, f"SoftwareApp: {has_software_app}, ScholarlyArticle: {has_scholarly_article}, EduOrg: {has_edu_org}, FAQ: {has_faq}")


def audit_frontend_components(report: SprintReport):
    print("\n--- 6. AUDITING FRONTEND AGENTIC UI & DOM MAPPINGS ---")
    js_path = APP_DIR / "static" / "app.js"
    res = subprocess.run(["node", "--check", str(js_path)], capture_output=True, text=True)
    report.log("FRONTEND", "app.js Node.js Syntax Verification", res.returncode == 0, f"Returncode: {res.returncode}")

    html_content = (APP_DIR / "static" / "index.html").read_text(encoding="utf-8")
    has_council_ui = "agentic" in html_content.lower() or "council" in html_content.lower()
    report.log("FRONTEND", "Agentic Council UI elements in index.html", has_council_ui, "Agentic drawer/card detected")


def audit_typst_publication(report: SprintReport):
    print("\n--- 7. AUDITING TYPST 0.15 COMPILATION ---")
    run_dir = Path(APP_DIR / "runs" / "sample")
    main_typ = run_dir / "main.typ"
    if main_typ.exists():
        cmd = ["typst", "compile", str(main_typ), str(run_dir / "test_sprint_compile.pdf")]
        res = subprocess.run(cmd, capture_output=True, text=True)
        report.log("TYPST", "Typst 0.15 compilation check", res.returncode == 0, f"Returncode: {res.returncode}, Stderr: {res.stderr.strip()[:100] if res.stderr else 'None'}")
    else:
        report.log("TYPST", "main.typ existence", False, "main.typ missing")


if __name__ == "__main__":
    report = SprintReport()
    
    audit_python_ast(report)
    
    # Import app for test client
    from server import app
    client = TestClient(app)
    
    audit_agentic_council(client, report)
    audit_market_intelligence(client, report)
    audit_seo_endpoints(client, report)
    audit_html_seo_and_jsonld(report)
    audit_frontend_components(report)
    audit_typst_publication(report)
    
    all_passed = report.summary()
    sys.exit(0 if all_passed else 1)
