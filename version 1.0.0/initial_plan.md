# Version 1.0.0: Initial Product Plan & Launch Blueprint

**Product Name:** OmniScholar MVP (v1.0.0)  
**Target Release:** 6 Weeks from Kickoff  
**Core Objective:** Launch the fastest, most reliable "CSV-to-Publication Results & Methodology" web SaaS in the market.

---

## 1. Product Scope for Version 1.0.0 (The Killer Wedge)

In Version 1.0.0, we do **not** try to build everything. We focus with laser intensity on the single most acute pain point every empirical researcher faces: **converting a raw dataset into verified, publication-grade statistical tables, high-resolution figures, and an academic results chapter.**

### Core User Journey (The "Magic Moment" in < 90 Seconds):
1. **Upload:** User drops in their survey or experimental dataset (`CSV` or `Excel`).
2. **Variable Mapping:** System automatically detects data types:
   - Nominal/Categorical (e.g. Roles, Gender, Treatment Group)
   - Ordinal/Likert (e.g. 1-to-5 scale)
   - Continuous/Numeric (e.g. Price, Returns, Age, Test Scores)
3. **One-Click Execution:** The user clicks **"Run Empirical Analysis"**:
   - Backend executes our verified statistical scripts in a secure Python sandbox.
   - Computes descriptive statistics (Mean, Median, SD, Skewness, Kurtosis, Frequency counts).
   - Automatically selects the right tests (Kruskal-Wallis, Mann-Whitney U, ANOVA, Spearman/Pearson correlation).
4. **Instant Publication Deliverables:**
   - **Interactive Figures:** 300 DPI publication plots (Pie charts, distribution bar charts, correlation heatmaps).
   - **LaTeX `booktabs` & Word Tables:** Zero-error, beautifully formatted tables.
   - **Drafted Academic Text:** Formal IMRaD Results and Methodology paragraphs written strictly from the empirical numbers.
   - **Download Package:** Download as a complete `.zip` or compiled PDF.

---

## 2. Six-Week Engineering Sprint Schedule

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              VERSION 1.0.0 SPRINT TIMELINE                             │
├──────────────┬──────────────┬──────────────┬──────────────┬──────────────┬─────────────┤
│ WEEK 1       │ WEEK 2       │ WEEK 3       │ WEEK 4       │ WEEK 5       │ WEEK 6      │
│ Backend API  │ Next.js Web  │ Execution    │ Document &   │ Closed Beta  │ Public      │
│ & Scrapers   │ Frontend     │ Sandboxing   │ PDF Exporter │ (Students)   │ Launch      │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────┴─────────────┘
```

### Week 1: Backend Foundation & API Engine
- Set up **FastAPI** backend repository with async endpoints.
- Port our tested Python analytics pipeline (`run_statistical_analytics.py`) into modular service classes:
  - `DataAuditorService`: Inspects columns, missing values, and data types.
  - `StatisticalEngineService`: Executes descriptive, correlation, and inferential computations.
  - `VisualizationService`: Headless matplotlib/seaborn generation at 300 DPI.
- Define JSON schemas for dataset summaries and analytical responses.

### Week 2: Next.js Modern Frontend
- Initialize **Next.js 14+ (App Router)** frontend with Tailwind CSS and modern dark/light UI.
- Build clean, intuitive drag-and-drop file upload component.
- Build interactive variable mapper: allows users to confirm column roles (e.g. Grouping variable vs Target variable).
- Build the results dashboard: dynamic statistical summary cards and tabbed navigation.

### Week 3: Sandboxing & Real-Time Visualization
- Integrate **E2B sandbox** or lightweight Docker runner for 100% isolated Python execution.
- Implement real-time WebSocket progress updates (`"Auditing columns..."` $\to$ `"Running Kruskal-Wallis..."` $\to$ `"Rendering 300 DPI Heatmaps..."`).
- Build interactive chart viewer with one-click "Download High-Res 300 DPI PNG" and "Download SVG Vector".

### Week 4: LaTeX/Typst & Document Export Engine
- Integrate **Typst CLI / Tectonic engine** for sub-second PDF generation.
- Build the one-click exporter:
  - Generates `main.tex` with standard `booktabs` tables and linked figures.
  - Generates formatted Word document (`.docx`) for researchers who do not use LaTeX.
  - Compiles ready-to-view PDF summary.

### Week 5: Closed Beta with Student Cohort (Private Alpha)
- Onboard 30 of your active students and research peers.
- Have them upload their actual thesis / research datasets.
- Fix UI friction, edge cases (e.g. datasets with weird character encodings or null values).
- Collect video testimonials and case studies.

### Week 6: Public Launch & Payment Gateway Integration
- Integrate **Stripe** (or LemonSqueezy for global international billing).
- Launch pricing:
  - **Single Paper Pass:** $15 (one-time analysis + export).
  - **Researcher Pro:** $29/month (unlimited analyses, live editor, priority sandbox).
- Launch on Product Hunt, LinkedIn, Twitter/X, and academic subreddits (r/GradSchool, r/PhD, r/Professors).

---

## 3. Go-To-Market Execution: Securing First 100 Paying Users

You have an unfair advantage: **you already teach AI for researchers.**

### The 30-Day Conversion Playbook:
1. **Host a Free Live Masterclass:**
   - Title: *"How to Complete Your Empirical Methodology & Results Section in Under 2 Hours (Without Hallucinations or Coding)."*
   - Target: Graduate students, thesis writers, university faculties.
2. **The Live Demo:**
   - In the masterclass, take a messy real-world CSV file live on screen.
   - Run OmniScholar v1.0.0.
   - In 90 seconds, show the complete statistical results, APA 7th tables, and 300 DPI figures generated with zero errors.
3. **The Offer:**
   - Give attendees an exclusive early-bird founder price: **$19/month** or **$149/year**.
   - With 300-500 students in your network, converting 100 paying customers ($1,900 to $5,000 MRR) in the first 30 days is extremely realistic.

---

## 4. Key Metrics for Version 1.0.0 Success
- **Time to First Value:** Less than 90 seconds from CSV upload to rendered results.
- **Statistical Accuracy:** 100% match against R and SPSS gold standards.
- **Customer Conversion Rate:** $\ge 15\%$ from free trial dataset to paid tier.
- **Target MRR by End of Month 2:** **$5,000+ MRR** (proving product-market fit before raising seed capital).
