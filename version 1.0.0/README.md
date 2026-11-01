# OmniScholar AI Studio — Version 1.0.0 (Production MVP)

**The Autonomous Empirical Research Operating System & Anti-Ghostwriting Engine**  
*Lead Architect & Founder:* Ishwor Prasad Dhungana  
*Current Release:* `v1.0.0`

---

## 🚀 Overview

OmniScholar v1.0.0 is the definitive "CSV/Excel-to-Publication Results & Manuscript" research platform. Built for university researchers, thesis students, and quantitative analysts, it eliminates the 40+ hours typically spent auditing messy data, computing descriptive statistics, selecting and running inferential hypothesis tests, rendering high-resolution figures, formatting LaTeX `booktabs`, and drafting academic IMRaD results chapters.

Every calculation is strictly derived from raw empirical vectors using a deterministic Python sandbox—guaranteeing **0.0% ghostwriting hallucination** with cryptographic SHA-256 provenance.

---

## 🌟 Key Capabilities in Version 1.0.0

1. **Dual Format Ingestion (CSV & Excel):**
   - Seamless drag-and-drop support for `.csv`, `.xlsx`, and `.xls` datasets.
   - Built-in instant loader for real-world Dhaka Stock Exchange ($N=100$) market trading data.

2. **Automated Variable Profiler:**
   - Detects nominal, categorical, ordinal (Likert), and continuous variables.
   - Calculates sample size ($N$), missing value percentages, mean, standard deviation ($SD$), median, interquartile range ($\text{IQR}$), min, max, skewness ($\gamma_1$), and kurtosis ($\gamma_2$).
   - Generates publication-ready 300 DPI distribution charts (pie charts and ranked frequency horizontal bar charts).

3. **Bivariate Correlation Architecture:**
   - Computes Spearman rank correlation matrix and associated statistics across all quantitative constructs.
   - Generates high-resolution (300 DPI) annotated heatmaps with customizable color ramps.

4. **Parametric & Non-Parametric Inferential Hypothesis Testing:**
   - **Dynamic Cohort Grouping:** Interactive dropdown allows instant switching between grouping constructs (e.g., Role, Experience, Strategy).
   - **Non-Parametric Tests:** Kruskal-Wallis $H$-test ($k \ge 3$ cohorts) and Mann-Whitney $U$-test ($k = 2$ cohorts) for robust evaluation without restrictive normality assumptions.
   - **Parametric Tests:** One-way ANOVA ($F$-statistic) and Welch's independent samples $t$-test.
   - Outputs test statistics, degrees of freedom ($df$), asymptotic $p$-values, and formal academic interpretations.

5. **Publication-Grade LaTeX Booktabs Generator:**
   - Auto-formats empirical distribution tables into standard `booktabs` syntax (`\toprule`, `\midrule`, `\bottomrule`).
   - One-click copy buttons for direct pasting into Overleaf or local LaTeX files.

6. **Anti-Ghostwriting Manuscript Drafter:**
   - Formulates Section 4 (Empirical Results & Diagnostics) text with exact numeric fidelity.
   - Live word count and character count monitors.

7. **Autonomous Tectonic PDF Compilation Engine:**
   - Generates complete standalone `main.tex` manuscript including abstract, provenance tables, embedded 300 DPI figures, and inferential findings.
   - Compiles sub-second vector PDF (`Research_Manuscript_v1.0.0.pdf`) on the fly using the embedded Tectonic compiler.

8. **Cryptographic Reproducibility Passport & One-Click ZIP Export:**
   - Computes SHA-256 dataset fingerprint, UTC audit timestamp, and mathematical provenance seal.
   - Exports complete ZIP archive containing the compiled PDF, raw CSV tables, high-resolution figures, LaTeX source, and reproducibility certificate.

---

## 🛠️ Technology Stack

- **Backend:** Python 3.14+, FastAPI, Uvicorn, Pandas, NumPy, SciPy, Matplotlib, Seaborn, OpenPyXL.
- **Compiler:** Tectonic 0.14.1 (Standalone Rust-based TeX engine).
- **Frontend:** Responsive HTML5 / Modern CSS3 (Dark/Light glassmorphism, responsive grid), Vanilla JavaScript ES6+.
- **Package Management:** `uv` for sub-second isolated dependency resolution.

---

## ⚡ Quickstart & Running the App

### Option A: Using PowerShell (Recommended)
```powershell
cd "E:\Nesfield\Billion dollar project\version 1.0.0\app"
.\run_server.ps1
```

### Option B: Using Windows Batch
Double-click:
```
E:\Nesfield\Billion dollar project\version 1.0.0\app\run_server.bat
```

Once started, open your web browser to:
👉 **`http://127.0.0.1:8000`**

---

## 📡 API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/health` | `GET` | Health check and verification of PDF engine status. |
| `/api/load-sample` | `POST` | Loads verified sample dataset ($N=100$) and triggers full pipeline. |
| `/api/upload` | `POST` | Uploads and analyzes custom `.csv`, `.xlsx`, or `.xls` dataset. |
| `/api/set-grouping` | `POST` | Dynamically updates cohort grouping variable and recalculates tests. |
| `/api/export-pdf` | `GET` | Streams the compiled `Research_Manuscript_v1.0.0.pdf`. |
| `/api/export-tex` | `GET` | Streams the raw LaTeX manuscript source (`main.tex`). |
| `/api/export-zip` | `GET` | Downloads the complete research bundle as `.zip`. |

