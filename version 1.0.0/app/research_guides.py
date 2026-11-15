"""
OmniScholar v1.0.1 — Master Research Guides Knowledge Base
Comprehensive, publication-grade guidance for 40 research paradigms and methodological traditions.
Targeted specifically for normal researchers, graduate scholars, and doctoral investigators.
"""

RESEARCH_GUIDES = [
    {
        "id": "academic",
        "name": "Academic Research",
        "category": "Purpose & Domain",
        "summary": "Research conducted within universities and academic institutions aimed at advancing theoretical frontiers, testing foundational assumptions, and contributing to the global body of peer-reviewed literature.",
        "when_to_use": [
            "When pursuing thesis, dissertation, or scholarly journal publication (Q1/Q2).",
            "When the primary objective is intellectual rigor, theoretical extension, and reproducibility rather than immediate commercial profit.",
            "When rigorous peer-review and institutional ethics compliance (IRB/ERB) are mandatory."
        ],
        "epistemology": "Epistemic pluralism (Positivism, Critical Realism, or Interpretivism) prioritizing open-science verification and citation lineage.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate a tight research question addressing a defined literature gap.",
            "Phase 2: Conduct a systematic literature review (PRISMA framework) synthesizing incumbent models.",
            "Phase 3: Secure IRB ethical clearance and specify theoretical framework (deductive or inductive).",
            "Phase 4: Design validated instrumentation (Likert scales, psychometric constructs, or interview guides).",
            "Phase 5: Execute closed-sandbox analysis with robust inferential testing (e.g., OLS HC3, ANOVA, Thematic Analysis).",
            "Phase 6: Structure manuscript adhering strictly to target journal format (IMRaD, IEEE, APA 7th)."
        ],
        "data_collection_techniques": "Standardized survey instruments, controlled experiments, validated psychometric inventories, or semi-structured interviews.",
        "data_analysis_methods": "Inferential statistics (ANOVA, OLS with HC3 robust SEs), effect size reporting (eta^2, Cohen's d), or reflexive thematic coding.",
        "pitfalls_and_red_flags": [
            "Failing to articulate a clear theoretical gap beyond mere geographic replication.",
            "P-hacking or reporting uncorrected Family-Wise Error Rates across multi-hypothesis batteries.",
            "Using generative AI text without verifiable raw-data mathematical provenance (causes immediate desk-rejection)."
        ],
        "q1_checklist": [
            "Explicit literature gap stated in Introduction Movement 3.",
            "Power analysis verifying sample adequacy (1 - beta >= 0.80).",
            "Full reporting of degrees of freedom, exact p-values, and 95% confidence intervals.",
            "Zero ghostwriting guarantee with raw vector provenance."
        ],
        "recommended_tools": "Python (SciPy, Statsmodels), R, Typst 0.15, Zotero, LaTeX."
    },
    {
        "id": "industrial",
        "name": "Industrial / Applied R&D",
        "category": "Purpose & Domain",
        "summary": "Research conducted by corporate R&D teams or commercial enterprises to optimize products, improve operational processes, reduce manufacturing defects, or create proprietary commercial advantages.",
        "when_to_use": [
            "When the goal is measurable return on investment (ROI), customer retention, or latency reduction.",
            "When decision-makers require actionable empirical recommendations rather than theoretical debates.",
            "When optimizing A/B tests, machine learning deployment pipelines, or operational bottlenecks."
        ],
        "epistemology": "Pragmatism: what works in practice is true; utility and actionable predictive power take precedence over abstract theory.",
        "step_by_step_roadmap": [
            "Phase 1: Define key performance indicators (KPIs) and operational problem statement.",
            "Phase 2: Benchmark current baseline performance against competitor or historical metrics.",
            "Phase 3: Design pilot intervention or feature experiment (A/B testing framework).",
            "Phase 4: Collect telemetry, production logs, or customer behavior vectors.",
            "Phase 5: Perform difference-in-differences, uplifts modeling, or multivariate regression.",
            "Phase 6: Synthesize executive white paper and engineering deployment roadmap."
        ],
        "data_collection_techniques": "Production telemetry logs, user session tracking, structured customer feedback, operational sensor data.",
        "data_analysis_methods": "A/B hypothesis testing, survival analysis, cohort retention decay, uplift modeling, regression discontinuity.",
        "pitfalls_and_red_flags": [
            "Confusing statistical correlation with operational business causality.",
            "Ignoring selection bias in user cohorts opting into new features.",
            "Optimizing short-term vanity metrics at the expense of long-term user trust."
        ],
        "q1_checklist": [
            "Clear pre-intervention vs post-intervention baseline comparison.",
            "Accounting for seasonality and confounding external market shocks.",
            "Cost-benefit analysis quantifying practical significance."
        ],
        "recommended_tools": "Python (Pandas, Scikit-learn), SQL, Grafana, Typst."
    },
    {
        "id": "basic_pure",
        "name": "Basic / Pure Research",
        "category": "Purpose & Domain",
        "summary": "Fundamental inquiry designed to expand human understanding of universal laws, mechanisms, and phenomena without immediate commercial or practical applications.",
        "when_to_use": [
            "When investigating fundamental physical, computational, or cognitive principles.",
            "When seeking to understand 'how' and 'why' phenomena operate at their most granular level.",
            "When establishing foundational axioms upon which applied sciences will build decades later."
        ],
        "epistemology": "Realism / Rationalism: belief in an objective external reality governed by discoverable structural laws.",
        "step_by_step_roadmap": [
            "Phase 1: Identify an unexplained theoretical anomaly or mathematical contradiction.",
            "Phase 2: Deduce formal mathematical or logical hypotheses from first principles.",
            "Phase 3: Design highly controlled experimental or computational simulation protocols.",
            "Phase 4: Isolate confounding variables using strict laboratory or synthetic controls.",
            "Phase 5: Measure micro-interactions with high-precision instrumentation.",
            "Phase 6: Publish mathematical proofs, foundational models, and replication datasets."
        ],
        "data_collection_techniques": "Precision laboratory sensors, particle detectors, mathematical derivations, simulated Monte Carlo systems.",
        "data_analysis_methods": "Differential equations, Fourier transforms, spectral analysis, deterministic simulation validation.",
        "pitfalls_and_red_flags": [
            "Over-fitting mathematical models to synthetic artifacts rather than empirical reality.",
            "Ignoring edge boundary conditions and non-linear phase transitions."
        ],
        "q1_checklist": [
            "Complete mathematical derivation provided in supplementary appendices.",
            "Independent replication code sandbox included.",
            "Sensitivity analysis across extreme boundary conditions."
        ],
        "recommended_tools": "Python (NumPy, SymPy), Mathematica, Typst."
    },
    {
        "id": "applied",
        "name": "Applied Research",
        "category": "Purpose & Domain",
        "summary": "Systematic empirical inquiry aimed directly at solving an immediate, concrete practical problem facing individuals, organizations, or society.",
        "when_to_use": [
            "When policymakers or practitioners require evidence-based answers to pressing crises.",
            "When existing scientific theories must be adapted to a specific localized domain.",
            "When evaluating the real-world effectiveness of clinical, educational, or technological interventions."
        ],
        "epistemology": "Pragmatic Realism: theoretical models are valued by their diagnostic and problem-solving utility in natural settings.",
        "step_by_step_roadmap": [
            "Phase 1: Identify concrete stakeholder pain-point and articulate intervention objective.",
            "Phase 2: Review existing academic literature for candidate solutions and mechanisms.",
            "Phase 3: Adapt theoretical framework to local contextual constraints.",
            "Phase 4: Deploy intervention across target cohort with pre-post or quasi-experimental controls.",
            "Phase 5: Measure outcome variance, side-effects, and implementation fidelity.",
            "Phase 6: Deliver policy brief, clinical guideline, or operational implementation protocol."
        ],
        "data_collection_techniques": "Pre- and post-intervention surveys, clinical biomarker tracking, organizational performance audits.",
        "data_analysis_methods": "Paired samples t-test, ANCOVA (controlling for baseline scores), Hierarchical OLS with robust standard errors.",
        "pitfalls_and_red_flags": [
            "Lack of a control group leading to historical confounding (placebo effect).",
            "High attrition rate among participants distorting post-test results."
        ],
        "q1_checklist": [
            "Pre-test equivalence established between intervention and control cohorts.",
            "Intention-to-treat (ITT) analysis conducted for missing follow-up data.",
            "Practical effect sizes (Cohen's d, NNT) reported alongside p-values."
        ],
        "recommended_tools": "Python (Statsmodels), SPSS, Typst."
    },
    {
        "id": "exploratory",
        "name": "Exploratory Research",
        "category": "Inquiry & Goal",
        "summary": "Initial investigation into a novel, emergent, or poorly understood topic where formal hypotheses cannot yet be derived due to an absence of prior literature.",
        "when_to_use": [
            "When studying newly emerged technologies (e.g. generative agent swarms, novel pandemics).",
            "When existing theories fail to explain surprising anomalies.",
            "When the objective is to generate candidate hypotheses and conceptual categories for subsequent testing."
        ],
        "epistemology": "Constructivism / Inductivism: meaning and theoretical structures emerge from inductive immersion in the empirical field.",
        "step_by_step_roadmap": [
            "Phase 1: Frame open-ended exploratory research questions (avoid directional hypotheses).",
            "Phase 2: Cast a wide methodological net using qualitative interviews, pilot surveys, or exploratory data mining.",
            "Phase 3: Sample maximally diverse participants or heterogeneous case environments.",
            "Phase 4: Conduct iterative open coding and thematic clustering.",
            "Phase 5: Synthesize an emergent conceptual framework with postulated directional arrows.",
            "Phase 6: Publish exploratory findings and formulate testable hypotheses for future confirmatory studies."
        ],
        "data_collection_techniques": "Unstructured/semi-structured interviews, open-ended focus groups, participant field observations, web scraping.",
        "data_analysis_methods": "Reflexive thematic analysis, open coding, exploratory factor analysis (EFA), hierarchical clustering.",
        "pitfalls_and_red_flags": [
            "Pretending post-hoc exploratory findings were pre-stated confirmatory hypotheses (HARKing).",
            "Over-generalizing small exploratory qualitative samples to universal populations."
        ],
        "q1_checklist": [
            "Explicitly labeled as 'Exploratory' to prevent accusations of HARKing.",
            "Transparent documentation of coding decisions and thematic codebook.",
            "Conceptual model clearly diagrammed with proposed future hypotheses."
        ],
        "recommended_tools": "NVivo, Python (SciPy clustering), Typst."
    },
    {
        "id": "descriptive",
        "name": "Descriptive Research",
        "category": "Inquiry & Goal",
        "summary": "Research designed to accurately and systematically document the characteristics, frequency, prevalence, or behavioral profiles of a population or phenomenon without manipulating variables.",
        "when_to_use": [
            "When answering 'What is happening?', 'Who is affected?', and 'How frequently does it occur?'",
            "When establishing national or demographic census baselines (e.g., retail investor demographics).",
            "When a clear snapshot of an empirical distribution is required before causal studies begin."
        ],
        "epistemology": "Empirical Positivism: reality can be faithfully represented through objective, quantified measurement of observable properties.",
        "step_by_step_roadmap": [
            "Phase 1: Define target population and precise operational definitions of all variables.",
            "Phase 2: Determine statistically representative probability sample size (Cochran formula / Yamane).",
            "Phase 3: Standardize structured survey questionnaire or objective observational tally sheets.",
            "Phase 4: Collect observational records with strict quality control against duplicate entries.",
            "Phase 5: Compute central tendency (Mean, Median), dispersion (SD, IQR), and skewness-kurtosis.",
            "Phase 6: Present publication-grade frequency distributions, cross-tabulations, and 300 DPI histograms."
        ],
        "data_collection_techniques": "Cross-sectional census surveys, structured observational checklists, demographic registries.",
        "data_analysis_methods": "Descriptive statistics (M, SD, Mdn, IQR), skewness/kurtosis, frequency percentages, chi-square goodness-of-fit.",
        "pitfalls_and_red_flags": [
            "Making unsubstantiated causal claims from purely descriptive cross-tabulations.",
            "Ignoring severe non-response bias distorting demographic representativeness."
        ],
        "q1_checklist": [
            "Sample size justified with formal statistical sampling formula (e.g. 95% CI, e = 5%).",
            "Response rate reported with non-response bias wave analysis (Armstrong & Overton, 1977).",
            "Booktabs tables reporting both absolute frequency (n) and valid percentage (%)."
        ],
        "recommended_tools": "Python (Pandas, Seaborn), SPSS, Typst."
    },
    {
        "id": "explanatory_causal",
        "name": "Explanatory / Causal Research",
        "category": "Inquiry & Goal",
        "summary": "Rigorous scientific investigation aimed at identifying cause-and-effect relationships, isolating causal mechanisms, and ruling out confounding variables.",
        "when_to_use": [
            "When testing directional causal hypotheses ('Does X cause Y?').",
            "When evaluating the mediating mechanisms (M) through which X influences Y, and moderating boundary conditions (W).",
            "When scientific progress demands establishing strict empirical causality (temporal precedence, covariation, non-spuriousness)."
        ],
        "epistemology": "Post-Positivism / Critical Realism: seeks underlying generative mechanisms governing observable empirical regularities.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate formal directional hypotheses based on established theoretical mechanisms.",
            "Phase 2: Establish temporal ordering (X measured before Y, or controlled experimental manipulation).",
            "Phase 3: Identify potential confounding covariates (Z) and common method variance markers.",
            "Phase 4: Collect multi-source or multi-wave panel data to eliminate cross-sectional common method bias.",
            "Phase 5: Execute Hierarchical OLS with Huber-White HC3 robust standard errors or Structural Equation Modeling (SEM).",
            "Phase 6: Conduct sensitivity tests (causal mediation analysis, Instrumental Variables, propensity score matching)."
        ],
        "data_collection_techniques": "Multi-wave longitudinal surveys, randomized controlled laboratory experiments, instrumental variable datasets.",
        "data_analysis_methods": "Hierarchical OLS (HC3 standard errors), Mediation analysis (Preacher & Hayes bootstrap), Instrumental Variables (2SLS).",
        "pitfalls_and_red_flags": [
            "Asserting causality from purely simultaneous cross-sectional correlation without endogeneity controls.",
            "Ignoring omitted variable bias or reverse causality (simultaneity bias)."
        ],
        "q1_checklist": [
            "Three conditions of causality verified: temporal precedence, empirical covariation, isolation of non-spuriousness.",
            "Heteroskedasticity controlled using Huber-White HC3 robust standard errors.",
            "Bootstrapped mediation indirect effects reported with 95% bias-corrected confidence intervals."
        ],
        "recommended_tools": "Python (Statsmodels, Linearmodels), R (lavaan), Typst."
    },
    {
        "id": "correlational",
        "name": "Correlational Research",
        "category": "Design & Control",
        "summary": "Non-experimental research measuring the statistical association, direction, and magnitude of relationships between two or more variables without experimental manipulation.",
        "when_to_use": [
            "When experimental manipulation is ethically prohibited or practically impossible.",
            "When screening a large battery of psychometric or economic variables for latent dependencies.",
            "When predicting outcome variance based on naturally occurring behavioral predictors."
        ],
        "epistemology": "Empirical Positivism: observable quantitative co-variation reflects latent lawful dependencies.",
        "step_by_step_roadmap": [
            "Phase 1: Select continuous or ordinal variables with established theoretical linkages.",
            "Phase 2: Administer standardized survey battery with validated Likert scales.",
            "Phase 3: Screen data for univariate and multivariate outliers (Mahalanobis distance, Cook's D).",
            "Phase 4: Test assumptions of bivariate normality and homoskedasticity.",
            "Phase 5: Compute Pearson product-moment r (parametric) and Spearman rank-order rho (non-parametric) with exact p-values.",
            "Phase 6: Construct publication-grade correlation matrix with Fisher z 95% confidence intervals."
        ],
        "data_collection_techniques": "Multi-construct Likert scale questionnaires, observational registries, archival time-series.",
        "data_analysis_methods": "Pearson r, Spearman rho, Kendall's tau-b, Fisher z-transformation confidence intervals, Bonferroni-Holm adjustment.",
        "pitfalls_and_red_flags": [
            "Conflating high correlation with causation ('Correlation does not imply causation').",
            "Failing to report exact p-values or reporting p = .000 instead of p < .001."
        ],
        "q1_checklist": [
            "Bivariate correlation matrix reports sample size, exact two-tailed p-values, and 95% CIs.",
            "Scale reliability (Cronbach's alpha) reported along diagonal.",
            "Common Method Variance (CMV) evaluated via Harman's one-factor test or marker variable."
        ],
        "recommended_tools": "Python (SciPy, Pandas), SPSS, Typst."
    },
    {
        "id": "experimental",
        "name": "Experimental Research",
        "category": "Design & Control",
        "summary": "The gold standard of causal scientific inquiry, featuring random assignment of subjects, active manipulation of independent variables, and strict laboratory or environmental controls.",
        "when_to_use": [
            "When proving that an intervention (drug, algorithm, teaching method) directly causes an outcome.",
            "When random assignment to treatment and control groups is ethically and logistically feasible.",
            "When ruling out all threats to internal validity (history, maturation, selection bias)."
        ],
        "epistemology": "Classical Positivism: truth is verified through active intervention, controlled counterfactual comparison, and replication.",
        "step_by_step_roadmap": [
            "Phase 1: Define treatment manipulation (independent variable) and primary outcome metrics.",
            "Phase 2: Calculate statistical power (G*Power) to determine minimum sample size per cell.",
            "Phase 3: Randomly assign participants to Treatment and Control (or Placebo) groups.",
            "Phase 4: Administer pre-test baseline measurement across all groups.",
            "Phase 5: Apply double-blind intervention protocol under controlled parameters.",
            "Phase 6: Administer post-test and execute Two-Way Repeated Measures ANOVA or ANCOVA."
        ],
        "data_collection_techniques": "Randomized controlled trials (RCT), controlled laboratory setups, computerized task experiments.",
        "data_analysis_methods": "Independent samples t-test, One-Way and Factorial ANOVA, ANCOVA (with baseline covariate), Tukey HSD post-hoc.",
        "pitfalls_and_red_flags": [
            "Failure of randomization check (pre-existing baseline differences between groups).",
            "Hawthorne or Pygmalion effects caused by lack of proper blinding."
        ],
        "q1_checklist": [
            "CONSORT flowchart documenting participant enrollment, allocation, follow-up, and analysis.",
            "Effect sizes (partial eta-squared, Cohen's d) reported with confidence intervals.",
            "Ethical review board approval number explicitly stated."
        ],
        "recommended_tools": "Python (SciPy, Statsmodels), PsychoPy, Typst."
    },
    {
        "id": "quasi_experimental",
        "name": "Quasi-Experimental Research",
        "category": "Design & Control",
        "summary": "Empirical studies estimating causal impacts of an intervention on target populations without random assignment, utilizing naturally occurring or pre-matched cohorts.",
        "when_to_use": [
            "When random assignment is unethical (e.g. assigning smoking or poverty) or practically impossible.",
            "When studying policy changes implemented in specific geographic districts or school systems.",
            "When evaluating retrospective patient cohorts in clinical healthcare settings."
        ],
        "epistemology": "Critical Realism: causality can be inferred in open natural systems through statistical adjustment for selection bias.",
        "step_by_step_roadmap": [
            "Phase 1: Identify existing treatment group and carefully matched comparison group.",
            "Phase 2: Collect comprehensive baseline covariates to model selection propensity.",
            "Phase 3: Execute Propensity Score Matching (PSM) or coarsened exact matching.",
            "Phase 4: Administer Difference-in-Differences (DiD) measurement across pre- and post-periods.",
            "Phase 5: Test parallel trends assumption to confirm valid counterfactual trajectory.",
            "Phase 6: Estimate treatment effect using two-way fixed effects regression models."
        ],
        "data_collection_techniques": "Archival institutional registries, hospital patient records, educational test databases.",
        "data_analysis_methods": "Difference-in-Differences (DiD), Propensity Score Matching (PSM), Regression Discontinuity Design (RDD).",
        "pitfalls_and_red_flags": [
            "Violation of the parallel trends assumption invalidating DiD estimators.",
            "Hidden unobserved confounders driving both treatment selection and outcome."
        ],
        "q1_checklist": [
            "Pre-treatment parallel trends graphically demonstrated with leads-and-lags model.",
            "Propensity score covariate balance diagnostics (standardized mean differences < 0.10).",
            "Robustness checks against placebo treatment dates and synthetic control permutations."
        ],
        "recommended_tools": "Python (Linearmodels, CausalInference), R (MatchIt), Typst."
    },
    {
        "id": "quantitative",
        "name": "Quantitative Empirical Research",
        "category": "Methodological Paradigm",
        "summary": "Methodology based on numerical measurement, formal statistical modeling, mathematical deductive reasoning, and probabilistic inference over representative samples.",
        "when_to_use": [
            "When testing pre-formulated directional hypotheses derived from theoretical models.",
            "When quantifying population prevalence, effect sizes, variance explained (R^2), or odds ratios.",
            "When peer-reviewed publication requires reproducible, bitwise mathematical auditing."
        ],
        "epistemology": "Positivism / Post-Positivism: empirical facts exist independently of observer perceptions and can be quantified with measurable error margins.",
        "step_by_step_roadmap": [
            "Phase 1: Operationalize theoretical constructs into validated numerical measurement scales.",
            "Phase 2: Execute sample size determination based on statistical power analysis (1 - beta >= 0.80).",
            "Phase 3: Administer structured survey instrument with Likert, rating, or interval measures.",
            "Phase 4: Audit dataset integrity (missing values, extreme outliers, normality checks).",
            "Phase 5: Run parametric (ANOVA, OLS HC3) and non-parametric (Mann-Whitney, Kruskal-Wallis) tests.",
            "Phase 6: Compile findings into standard booktabs tables with exact degrees of freedom and p-values."
        ],
        "data_collection_techniques": "Standardized Likert questionnaires, economic transaction datasets, clinical biomarker panels.",
        "data_analysis_methods": "One-Way ANOVA with Tukey HSD, Hierarchical OLS with Huber-White HC3 SEs, Pearson/Spearman matrices, Cronbach's alpha.",
        "pitfalls_and_red_flags": [
            "Applying parametric tests (ANOVA, OLS) to severely skewed or heteroskedastic data without robust corrections.",
            "Reporting p-values without corresponding effect sizes (Cohen's d, eta^2, R^2)."
        ],
        "q1_checklist": [
            "Degrees of freedom and exact test statistics reported for every hypothesis.",
            "Heteroskedasticity-consistent covariance matrix (HC3) implemented.",
            "Zero ghostwriting verified via Bitwise Calculation Ledger."
        ],
        "recommended_tools": "Python (SciPy, Statsmodels, Pandas), R, Typst."
    },
    {
        "id": "qualitative",
        "name": "Qualitative Interpretive Research",
        "category": "Methodological Paradigm",
        "summary": "In-depth investigation exploring the meanings, experiences, perspectives, and social processes constructed by human participants using verbal, textual, or visual data.",
        "when_to_use": [
            "When answering 'How do participants experience X?' or 'Why does this process unfold this way?'",
            "When exploring complex subjective realities (e.g. mental health, organizational culture, coping mechanisms).",
            "When numerical categories would over-simplify rich psychological nuances."
        ],
        "epistemology": "Interpretivism / Social Constructivism: reality is socially constructed through language, culture, and intersubjective meaning-making.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate open-ended, non-directional qualitative research questions.",
            "Phase 2: Select purposive or snowball sampling strategy to recruit information-rich participants.",
            "Phase 3: Conduct semi-structured, audio-recorded interviews using an iterative interview guide.",
            "Phase 4: Transcribe verbatim and execute Braun & Clarke 6-phase reflexive thematic analysis.",
            "Phase 5: Verify empirical thematic saturation using Francis et al. (2010) 10+3 stopping rule.",
            "Phase 6: Draft qualitative findings with transparent codebook and verbatim participant extracts."
        ],
        "data_collection_techniques": "In-depth semi-structured interviews, focus group discussions, participant observation field logs.",
        "data_analysis_methods": "Reflexive thematic analysis (Braun & Clarke), inductive open coding, constant comparative method.",
        "pitfalls_and_red_flags": [
            "Claiming 'saturation' without stating the exact interview number where zero new themes emerged.",
            "Smoothing participant quotes with AI, stripping regional idioms and authentic voice."
        ],
        "q1_checklist": [
            "Full compliance with the 32-Item COREQ Qualitative Reporting Checklist.",
            "Researcher reflexivity statement articulating potential authorial biases.",
            "Verbatim quotes cited with unique anonymized participant IDs [e.g. P014, Age 24, Female]."
        ],
        "recommended_tools": "NVivo, MAXQDA, Python (QualCoder), Typst."
    },
    {
        "id": "mixed_methods",
        "name": "Mixed Methods Research",
        "category": "Methodological Paradigm",
        "summary": "Advanced research methodology that rigorously integrates quantitative and qualitative research approaches within a single study to provide a comprehensive, multi-dimensional understanding.",
        "when_to_use": [
            "When quantitative numbers reveal 'what' happened, but qualitative narratives are required to explain 'why' and 'how'.",
            "When developing a new measurement instrument (qualitative exploration $\to$ quantitative validation).",
            "When contradictory statistical findings require qualitative deep-dive investigation."
        ],
        "epistemology": "Pragmatism: integrates pluralistic methodologies to best answer multi-faceted research questions.",
        "step_by_step_roadmap": [
            "Phase 1: Determine mixed methods design (Convergent Parallel, Explanatory Sequential, or Exploratory Sequential).",
            "Phase 2: Formulate separate quantitative, qualitative, and hybrid integration research questions.",
            "Phase 3: Execute quantitative phase (structured survey, N=100+, inferential statistics).",
            "Phase 4: Execute qualitative phase (interviews with outlying or representative participants).",
            "Phase 5: Integrate data strands using a Joint Display Matrix comparing statistical metrics with qualitative quotes.",
            "Phase 6: Synthesize meta-inferences discussing points of convergence, expansion, or discordance."
        ],
        "data_collection_techniques": "Concurrent or sequential administration of numerical questionnaires and in-depth interview transcripts.",
        "data_analysis_methods": "Joint display matrices, statistical regression coupled with thematic coding, side-by-side comparison tables.",
        "pitfalls_and_red_flags": [
            "Conducting two isolated studies in parallel without genuine methodological integration (the 'silo effect').",
            "Failing to explain discrepancies when quantitative and qualitative findings directly contradict each other."
        ],
        "q1_checklist": [
            "Diagram of mixed methods workflow showing priority (QUAN -> qual, or QUAL + QUAN).",
            "Joint Display Matrix explicitly mapping statistical effect sizes to thematic participant voices.",
            "Grammar of Mixed Methods compliance (Creswell & Plano Clark, 2018)."
        ],
        "recommended_tools": "Python (Statsmodels + NLP), NVivo, Typst."
    },
    {
        "id": "primary",
        "name": "Primary Empirical Research",
        "category": "Data Source & Time",
        "summary": "Research conducted through the direct, original collection of first-hand empirical data tailored specifically to answer the author's proprietary research questions.",
        "when_to_use": [
            "When secondary published datasets do not contain the specific variables or constructs needed.",
            "When investigating current, localized, or real-time behavioral phenomena.",
            "When the investigator requires complete control over measurement validity and sampling fidelity."
        ],
        "epistemology": "Direct Empiricism: original observational evidence gathered at the point of origin provides the highest evidentiary validity.",
        "step_by_step_roadmap": [
            "Phase 1: Design customized, pre-tested data collection instruments (surveys, sensor probes, interview protocols).",
            "Phase 2: Define strict inclusion and exclusion criteria for participant recruitment.",
            "Phase 3: Administer informed consent and collect first-hand responses.",
            "Phase 4: Audit raw dataset for missingness, unengaged responses (straight-lining), and duplicate IPs.",
            "Phase 5: Compute scale psychometrics, construct validity, and inferential models.",
            "Phase 6: Deposit anonymized raw data into open-science repository with DOI."
        ],
        "data_collection_techniques": "Google Forms / Qualtrics surveys, lab measurements, direct field interviews, sensor logging.",
        "data_analysis_methods": "Exploratory & confirmatory factor analysis (CFA), ANOVA, OLS regressions with HC3 robust SEs.",
        "pitfalls_and_red_flags": [
            "Inadequate sample size failing statistical power thresholds.",
            "Common method variance introduced when all variables are self-reported by a single informant."
        ],
        "q1_checklist": [
            "Exact participant response rate and completion time distributions reported.",
            "Full survey questionnaire items included in supplementary materials.",
            "Data availability statement with cryptographic hash."
        ],
        "recommended_tools": "Python, Google Apps Script, Typst."
    },
    {
        "id": "secondary",
        "name": "Secondary Data Research",
        "category": "Data Source & Time",
        "summary": "Investigation based on the systematic analysis, synthesis, or re-examination of existing, previously published datasets, institutional registries, or national censuses.",
        "when_to_use": [
            "When analyzing massive longitudinal panel datasets (e.g. World Bank, SEC filings, DSE equity records).",
            "When primary data collection across decades or continents is cost-prohibitive.",
            "When testing modern econometric techniques on historical market or public health archives."
        ],
        "epistemology": "Archival Empiricism: existing institutional records reflect objective historical realities suitable for rigorous secondary modeling.",
        "step_by_step_roadmap": [
            "Phase 1: Identify reputable open-access or licensed secondary database repository.",
            "Phase 2: Evaluate data dictionary, sampling frame, and variable coding conventions.",
            "Phase 3: Extract, clean, and harmonize data subsets into analysis-ready panel structure.",
            "Phase 4: Address structural missingness, survivor bias, and changes in accounting/registry definitions over time.",
            "Phase 5: Apply panel econometric models (fixed-effects, random-effects, instrumental variables).",
            "Phase 6: Report empirical estimates with full citation to primary data repository."
        ],
        "data_collection_techniques": "Archival databases, government census registries, financial exchange order books, clinical EHR archives.",
        "data_analysis_methods": "Panel data regression (fixed/random effects), Generalized Method of Moments (GMM), survival analysis.",
        "pitfalls_and_red_flags": [
            "Measurement mismatch: trying to force a proxy variable in the dataset to represent an unmeasured theoretical construct.",
            "Ignoring survivor bias in commercial financial databases (delisted firms dropped)."
        ],
        "q1_checklist": [
            "Primary database source, release version, and download date explicitly cited.",
            "Sample attrition and filtering steps documented with flow table.",
            "Replication script reproducing exact dataset filtering from raw archival files."
        ],
        "recommended_tools": "Python (Pandas, Linearmodels), R, Stata, Typst."
    },
    {
        "id": "deductive",
        "name": "Deductive Research (Top-Down)",
        "category": "Inquiry & Reasoning",
        "summary": "Top-down scientific reasoning that begins with an established theory, derives specific directional hypotheses, and designs empirical tests to confirm or falsify those predictions.",
        "when_to_use": [
            "When mature theoretical frameworks already exist in the literature (e.g. Efficient Market Hypothesis, TAM, TRA).",
            "When testing whether an established universal law holds in a new context or demographic boundary.",
            "When scientific progress requires Popperian falsification of competing theoretical claims."
        ],
        "epistemology": "Critical Rationalism (Karl Popper): scientific theories cannot be proven definitively, but can be tested and corroborated through rigorous attempts at empirical falsification.",
        "step_by_step_roadmap": [
            "Phase 1: Identify foundational theory and conceptual model.",
            "Phase 2: Deduce precise directional hypotheses (H1: Beta > 0, p < .05).",
            "Phase 3: Operationalize constructs into standardized measurement instruments.",
            "Phase 4: Collect empirical data from representative sample.",
            "Phase 5: Execute hypothesis tests comparing empirical test statistics against critical thresholds.",
            "Phase 6: Conclude whether empirical findings corroborate or falsify the theoretical predictions."
        ],
        "data_collection_techniques": "Pre-structured survey scales, randomized experiments, objective performance measures.",
        "data_analysis_methods": "Null Hypothesis Significance Testing (NHST), OLS regression, ANOVA, Structural Equation Modeling.",
        "pitfalls_and_red_flags": [
            "Confirmation bias: dismissing anomalous findings that contradict the pre-stated theory.",
            "Vague, non-directional hypotheses (e.g. 'There is a relationship between X and Y') that cannot be falsified."
        ],
        "q1_checklist": [
            "All hypotheses derived explicitly from named theoretical literature before data analysis.",
            "Formal directional language utilized (e.g. 'positively predicts', 'moderates by attenuating').",
            "Summary table comparing each pre-stated hypothesis with empirical decision (Supported / Rejected)."
        ],
        "recommended_tools": "Python (Statsmodels), R, Typst."
    },
    {
        "id": "inductive",
        "name": "Inductive Research (Bottom-Up)",
        "category": "Inquiry & Reasoning",
        "summary": "Bottom-up reasoning that begins with open empirical observations, detects recurring patterns and regularities, and synthesizes these insights into new conceptual models or emergent theories.",
        "when_to_use": [
            "When existing theoretical frameworks are non-existent, obsolete, or inadequate to explain a phenomenon.",
            "When exploring complex psychological, interpersonal, or cultural dynamics.",
            "When seeking to understand participant lived realities from their own insider vocabulary."
        ],
        "epistemology": "Constructivism / Grounded Realism: theoretical structures are abstracted inductively from grounded empirical observation.",
        "step_by_step_roadmap": [
            "Phase 1: Immerse in empirical context with an open, non-prescriptive inquiry posture.",
            "Phase 2: Gather rich, descriptive qualitative transcripts, observational logs, or case documents.",
            "Phase 3: Conduct line-by-line initial open coding to capture verbatim participant concepts.",
            "Phase 4: Group codes into higher-order conceptual categories through constant comparison.",
            "Phase 5: Identify core unifying category and diagram relationships between constructs.",
            "Phase 6: Formalize an emergent grounded theoretical framework."
        ],
        "data_collection_techniques": "Unstructured interviews, participant observation, ethnographic journals, historical records.",
        "data_analysis_methods": "Constant comparative method, open/axial/selective coding, thematic abstraction.",
        "pitfalls_and_red_flags": [
            "Imposing pre-conceived theoretical categories onto data while claiming inductive emergence.",
            "Stopping data collection prematurely before achieving genuine conceptual saturation."
        ],
        "q1_checklist": [
            "Theoretical sampling rationale clearly explained.",
            "Audit trail documenting the progression from raw quotes to first-order codes to grand themes.",
            "Substantive theory diagrammed with clear conceptual linkages."
        ],
        "recommended_tools": "NVivo, MAXQDA, Typst."
    },
    {
        "id": "grounded_theory",
        "name": "Grounded Theory Methodology",
        "category": "Qualitative Traditions",
        "summary": "Rigorous qualitative methodology (Glaser & Strauss / Charmaz) designed to systematically generate an explanatory substantive theory of social or psychological processes directly grounded in empirical data.",
        "when_to_use": [
            "When developing an explanatory process model where no current theory exists.",
            "When studying interpersonal or organizational adaptations over time.",
            "When peer-reviewed social science or clinical journals demand strict qualitative rigor."
        ],
        "epistemology": "Symbolic Interactionism & Constructivism: meaning is continuously negotiated through social interaction.",
        "step_by_step_roadmap": [
            "Phase 1: Begin simultaneous data collection and constant comparative analysis.",
            "Phase 2: Open Coding: dissect data into discrete analytical fragments.",
            "Phase 3: Axial Coding: assemble categories around conditions, context, and consequences.",
            "Phase 4: Theoretical Sampling: recruit new participants specifically to test emerging conceptual categories.",
            "Phase 5: Theoretical Saturation: continue sampling until additional interviews yield zero new category properties.",
            "Phase 6: Synthesize substantive grounded theoretical model with core category."
        ],
        "data_collection_techniques": "Iterative semi-structured interviews, observational field notes, theoretical memos.",
        "data_analysis_methods": "Constant comparative analysis, theoretical memo-writing, open, axial, and selective coding.",
        "pitfalls_and_red_flags": [
            "Treating grounded theory as mere generic thematic analysis without theoretical sampling.",
            "Neglecting theoretical memos, resulting in shallow descriptive summaries rather than explanatory theory."
        ],
        "q1_checklist": [
            "Theoretical sampling progression explicitly mapped in a recruitment table.",
            "Sample theoretical memos excerpted in manuscript body.",
            "Clear core category identified with directional process flowchart."
        ],
        "recommended_tools": "NVivo, Atlas.ti, Typst."
    },
    {
        "id": "phenomenological",
        "name": "Phenomenological Research",
        "category": "Qualitative Traditions",
        "summary": "Qualitative inquiry focused on exploring and understanding the universal essence of a lived human experience or psychological phenomenon as perceived by those who directly experienced it.",
        "when_to_use": [
            "When investigating profound, transformative, or traumatic lived experiences (e.g. chronic illness, grief, burnout, extreme market panic).",
            "When the research goal is to understand 'what was the experience like' from the first-person perspective.",
            "When psychological, clinical, or nursing research requires capturing experiential depth."
        ],
        "epistemology": "Phenomenology (Husserl / Heidegger / Merleau-Ponty): reality is experienced consciousness; knowledge is accessed through hermeneutic reduction.",
        "step_by_step_roadmap": [
            "Phase 1: Identify focal phenomenon and bracket prior researcher presuppositions (Epoché).",
            "Phase 2: Recruit purposive sample of 8-15 participants with direct, vivid lived experience.",
            "Phase 3: Conduct lengthy, unstructured phenomenological interviews.",
            "Phase 4: Read transcripts for overall holistic sense of experiential meaning.",
            "Phase 5: Extract significant statements and formulate meaning units (horizonalization).",
            "Phase 6: Synthesize structural and textural descriptions into the composite essence of the phenomenon."
        ],
        "data_collection_techniques": "Long in-depth interviews (60-120 minutes), reflective participant diaries, creative artifacts.",
        "data_analysis_methods": "Moustakas (1994) phenomenological reduction, Colaizzi (1978) or Giorgi (2009) thematic analysis.",
        "pitfalls_and_red_flags": [
            "Failing to execute and declare Epoché (bracketing), contaminating findings with authorial assumptions.",
            "Treating participant statements as objective factual claims rather than subjective lived meanings."
        ],
        "q1_checklist": [
            "Formal Epoché / Bracketing statement documented.",
            "Table of significant statements, formulated meanings, and theme clusters.",
            "Rich composite textural and structural description of the phenomenon's essence."
        ],
        "recommended_tools": "MAXQDA, NVivo, Typst."
    },
    {
        "id": "case_study",
        "name": "Case Study Methodology",
        "category": "Design & Control",
        "summary": "In-depth, multi-faceted empirical investigation of a contemporary phenomenon within its real-world context (a 'bounded system'), utilizing multiple sources of rich qualitative and quantitative evidence.",
        "when_to_use": [
            "When answering 'How' and 'Why' questions about a contemporary event over which the researcher has zero control.",
            "When the boundaries between the phenomenon and the context are not clearly evident (Yin, 2018).",
            "When analyzing an exceptional organization, crisis, patient, or institutional turnaround."
        ],
        "epistemology": "Critical Realism: cases exist in complex, contingent social ecologies requiring multi-level causal explanation.",
        "step_by_step_roadmap": [
            "Phase 1: Define the case and establish strict bounding criteria (spatial, temporal, institutional).",
            "Phase 2: Determine case design: single holistic, single embedded, or multiple comparative cases.",
            "Phase 3: Construct case study protocol and multi-source evidence database.",
            "Phase 4: Collect triangulated data: interviews, archival records, internal memos, direct observation.",
            "Phase 5: Perform pattern matching, explanation building, and chronological time-series analysis.",
            "Phase 6: Write thick, narrative case description followed by cross-case analytical synthesis."
        ],
        "data_collection_techniques": "Key informant interviews, archival documents, internal financial reports, direct observation.",
        "data_analysis_methods": "Pattern matching, explanation building, cross-case synthesis, timeline matrix analysis.",
        "pitfalls_and_red_flags": [
            "Relying on a single informant without triangulating across documentary or observational sources.",
            "Lacking a clear bounding definition, causing the scope of the case to diffuse uncontrollably."
        ],
        "q1_checklist": [
            "Case bounding criteria explicitly declared (geographic boundaries, time period, organizational unit).",
            "Triangulation table demonstrating convergence across at least 3 distinct data sources.",
            "Rival explanations explicitly tested and systematically ruled out."
        ],
        "recommended_tools": "NVivo, Typst, LaTeX."
    },
    {
        "id": "longitudinal",
        "name": "Longitudinal Panel Research",
        "category": "Data Source & Time",
        "summary": "Observational research design involving repeated empirical measurements of the exact same variables and participant cohorts across extended intervals of time.",
        "when_to_use": [
            "When studying growth trajectories, developmental changes, habituation, or decay curves.",
            "When establishing temporal precedence to prove causal ordering.",
            "When measuring the long-term impact or sustainability of an economic, educational, or clinical policy."
        ],
        "epistemology": "Temporal Realism: processes unfold in real time; time-series variance isolates true causality from static noise.",
        "step_by_step_roadmap": [
            "Phase 1: Determine optimal time spacing between measurement waves based on theoretical event horizon.",
            "Phase 2: Establish rigorous participant retention and tracking protocols to minimize panel attrition.",
            "Phase 3: Administer identical measurement instruments at Wave 1 (baseline), Wave 2, and Wave 3+.",
            "Phase 4: Conduct panel attrition analysis comparing dropouts to continuing participants.",
            "Phase 5: Fit Latent Growth Curve Models (LGCM), Cross-Lagged Panel Models (CLPM), or Two-Way Fixed Effects.",
            "Phase 6: Report trajectories, within-person vs between-person variance, and lag effects."
        ],
        "data_collection_techniques": "Repeated panel surveys, wearable sensor tracking, quarterly financial balance sheets.",
        "data_analysis_methods": "Random-effects and fixed-effects regression, Latent Growth Curve Modeling, autoregressive cross-lagged models.",
        "pitfalls_and_red_flags": [
            "Selective panel attrition systematically distorting long-term estimates.",
            "Conflating age effects, cohort effects, and period historical shocks."
        ],
        "q1_checklist": [
            "Attrition analysis confirming whether dropout was Missing Completely at Random (MCAR).",
            "Full reporting of between-person (inter-individual) and within-person (intra-individual) variance.",
            "Measurement invariance across time waves established before modeling trajectories."
        ],
        "recommended_tools": "Python (Statsmodels), R (lavaan, plm), Typst."
    },
    {
        "id": "cross_sectional",
        "name": "Cross-Sectional Research",
        "category": "Data Source & Time",
        "summary": "Observational research design analyzing empirical data collected from a population or representative subset at one specific, single point in time.",
        "when_to_use": [
            "When determining the current prevalence, incidence, or distribution of conditions across cohorts.",
            "When time and budgetary constraints prohibit multi-year longitudinal tracking.",
            "When conducting preliminary correlation screening before launching expensive longitudinal panels."
        ],
        "epistemology": "Empirical Positivism: snapshot observations provide valid estimates of population states at that specific epoch.",
        "step_by_step_roadmap": [
            "Phase 1: Define target population and sampling frame for the single observational window.",
            "Phase 2: Select stratified random or quota sampling to ensure demographic parity.",
            "Phase 3: Deploy standardized survey battery or physical testing protocol simultaneously.",
            "Phase 4: Collect observational records and audit for response speed (speeding) and straight-lining.",
            "Phase 5: Run cross-tabulations, chi-square tests, correlation matrices, and multivariate regression.",
            "Phase 6: Present snapshot findings with candid limitations regarding causal directionality."
        ],
        "data_collection_techniques": "Single-administration online surveys, intercept questionnaires, cross-sectional biomarkers.",
        "data_analysis_methods": "Descriptive statistics, Chi-square tests of independence, Multiple OLS regression, Logistic regression.",
        "pitfalls_and_red_flags": [
            "Making aggressive causal claims from single-point cross-sectional snapshots.",
            "Susceptibility to severe Common Method Variance (CMV) when all constructs are measured on one survey."
        ],
        "q1_checklist": [
            "STROBE cross-sectional reporting guidelines satisfied.",
            "Common Method Variance addressed using Harman's single-factor test or marker variables.",
            "Limitations section explicitly acknowledges inability to prove temporal precedence."
        ],
        "recommended_tools": "Python (Pandas, Statsmodels), SPSS, Typst."
    },
    {
        "id": "comparative",
        "name": "Comparative Research",
        "category": "Inquiry & Goal",
        "summary": "Systematic empirical comparison of two or more distinct groups, countries, institutions, or systems to discover empirical variance, commonalities, and causal drivers of divergence.",
        "when_to_use": [
            "When evaluating why policy X succeeded in Country A but failed in Country B.",
            "When comparing investor behaviors across frontier vs developed stock markets.",
            "When identifying institutional and cultural boundary conditions."
        ],
        "epistemology": "Comparative Institutionalism: macro differences between systems reveal underlying structural dependencies.",
        "step_by_step_roadmap": [
            "Phase 1: Select cases using 'Most Similar Systems' (MSSD) or 'Most Different Systems' (MDSD) logic.",
            "Phase 2: Harmonize variable operational definitions across different languages, currencies, and cultures.",
            "Phase 3: Collect standardized datasets from both cohorts/systems.",
            "Phase 4: Test measurement invariance to ensure constructs mean the exact same thing across groups.",
            "Phase 5: Execute independent samples t-tests, MANOVA, or Qualitative Comparative Analysis (QCA).",
            "Phase 6: Synthesize comparative matrices articulating structural mechanisms explaining divergence."
        ],
        "data_collection_techniques": "Harmonized international surveys, multi-country statistical registries, institutional policy audits.",
        "data_analysis_methods": "Independent samples t-test, MANOVA, multi-group SEM, fuzzy-set Qualitative Comparative Analysis (fsQCA).",
        "pitfalls_and_red_flags": [
            "Equivalence failure: assuming a question or measure carries identical psychological meaning in different cultures.",
            "Galton's problem: treating compared countries as independent units when they cross-influence each other."
        ],
        "q1_checklist": [
            "Clear justification for comparative case selection (MSSD vs MDSD).",
            "Measurement invariance (configural, metric, scalar) verified across groups.",
            "Comparative summary table highlighting key systemic contrasts."
        ],
        "recommended_tools": "Python (Statsmodels), R, Typst."
    },
    {
        "id": "action_research",
        "name": "Action Research",
        "category": "Qualitative Traditions",
        "summary": "Participatory, collaborative inquiry wherein researchers and practitioners simultaneously investigate an organizational or educational challenge while actively intervening to solve it in real time.",
        "when_to_use": [
            "When teachers, clinical nurses, or managers want to improve their own direct professional practice.",
            "When traditional external research is too detached from the real-life practitioners.",
            "When iterative, reflective cyclical change is the direct objective."
        ],
        "epistemology": "Pragmatic Constructivism: knowledge is generated through active participatory action and critical reflection.",
        "step_by_step_roadmap": [
            "Phase 1: Identify practical professional problem in the workplace.",
            "Phase 2: Plan: design a targeted pedagogical, clinical, or workflow intervention.",
            "Phase 3: Act: implement the intervention in real-time practice.",
            "Phase 4: Observe: systematically record outcome telemetry, participant feedback, and field logs.",
            "Phase 5: Reflect: critically evaluate what worked, what failed, and identify unintended consequences.",
            "Phase 6: Re-plan and initiate Cycle 2 of the spiral."
        ],
        "data_collection_techniques": "Reflective teacher/practitioner journals, classroom observations, student work artifacts, audio recordings.",
        "data_analysis_methods": "Iterative thematic reflection, pre-post descriptive score changes, qualitative feedback coding.",
        "pitfalls_and_red_flags": [
            "Subjective confirmation bias: researcher's dual role as intervention designer and evaluator.",
            "Treating routine professional troubleshooting as academic research without systematic data collection."
        ],
        "q1_checklist": [
            "Detailed documentation of at least two complete iterative Action-Reflection cycles.",
            "Participant co-researcher collaboration and feedback documented.",
            "Clear differentiation between research findings and standard administrative management."
        ],
        "recommended_tools": "Typst, Markdown, Word."
    },
    {
        "id": "ethnographic",
        "name": "Ethnographic Field Research",
        "category": "Qualitative Traditions",
        "summary": "Immersion methodology derived from cultural anthropology involving prolonged participant observation and field living to decipher the shared cultural norms, rituals, and practices of a distinct group.",
        "when_to_use": [
            "When understanding the implicit, unwritten 'rules of the game' inside a high-frequency trading desk, hospital ward, or digital subculture.",
            "When survey questions fail because participants do not realize their own tacit cultural assumptions.",
            "When thick, holistic contextual description is essential."
        ],
        "epistemology": "Cultural Relativism & Social Constructionism: human action can only be interpreted within its local cultural web of meaning.",
        "step_by_step_roadmap": [
            "Phase 1: Select cultural setting and negotiate gatekeeper access.",
            "Phase 2: Establish rapport and identify key cultural informants.",
            "Phase 3: Conduct prolonged participant observation (months to years) in the natural setting.",
            "Phase 4: Write exhaustive, contemporaneous field notes separating direct observation from personal reflection.",
            "Phase 5: Triangulate field notes with informal interviews and cultural artifacts.",
            "Phase 6: Compose thick ethnographic narrative detailing cultural rituals, vocabulary, and social structures."
        ],
        "data_collection_techniques": "Prolonged participant observation, handwritten field diaries, unrecorded informal conversations, cultural artifacts.",
        "data_analysis_methods": "Thick description (Geertz), domain and taxonomic analysis, cultural thematic coding.",
        "pitfalls_and_red_flags": [
            "'Going native': losing authorial analytical distance and becoming uncritical advocates.",
            "Over-interpreting idiosyncratic anecdotes as universal cultural norms."
        ],
        "q1_checklist": [
            "Detailed account of total hours and duration spent in the field.",
            "Deep researcher reflexivity section addressing observer impact on the group.",
            "Excerpts of raw field notes included in the text."
        ],
        "recommended_tools": "Field Notes, Typst."
    },
    {
        "id": "evaluative",
        "name": "Evaluative Research",
        "category": "Inquiry & Goal",
        "summary": "Applied systematic inquiry assessing the design, implementation, and overall worth, merit, or societal efficacy of an intervention, social program, or policy.",
        "when_to_use": [
            "When international donors, governments, or corporations demand proof of program efficacy.",
            "When deciding whether to scale up, modify, or terminate a clinical or educational initiative.",
            "When conducting cost-effectiveness or social return on investment (SROI) analyses."
        ],
        "epistemology": "Pragmatic Empiricism: policies and programs must be judged by their verifiable outcomes and societal value.",
        "step_by_step_roadmap": [
            "Phase 1: Construct the Program Logic Model (Inputs -> Activities -> Outputs -> Outcomes -> Impact).",
            "Phase 2: Formulate specific evaluative criteria (e.g. OECD-DAC: Relevance, Coherence, Effectiveness, Efficiency, Impact, Sustainability).",
            "Phase 3: Design mixed-methods evaluation matrix.",
            "Phase 4: Measure baseline vs endline indicators across targeted beneficiaries and control communities.",
            "Phase 5: Execute cost-benefit analysis and process fidelity audits.",
            "Phase 6: Publish comprehensive evaluation report with actionable policy recommendations."
        ],
        "data_collection_techniques": "Beneficiary surveys, key informant stakeholder interviews, program budget ledgers, monitoring logs.",
        "data_analysis_methods": "Difference-in-differences, cost-effectiveness ratios, thematic implementation analysis, fidelity audits.",
        "pitfalls_and_red_flags": [
            "Focusing solely on program activities (outputs) while failing to measure real changes in beneficiary condition (outcomes).",
            "Ignoring stakeholder politics and selective reporting by program managers."
        ],
        "q1_checklist": [
            "Clear Logic Model diagram included in methodology.",
            "Both quantitative impact metrics and qualitative process fidelity analyzed.",
            "Cost-effectiveness ratio or economic sustainability quantified."
        ],
        "recommended_tools": "Python, Typst."
    },
    {
        "id": "predictive",
        "name": "Predictive Modeling Research",
        "category": "Inquiry & Goal",
        "summary": "Quantitative computational inquiry leveraging historical data, econometric modeling, and machine learning algorithms to accurately forecast future trends, behaviors, or risk probabilities.",
        "when_to_use": [
            "When the primary goal is out-of-sample forecasting accuracy rather than historical description.",
            "When predicting financial distress, patient mortality, equipment failure, or macroeconomic recessions.",
            "When comparing the predictive power of econometric OLS vs machine learning algorithms."
        ],
        "epistemology": "Instrumentalism: the validity of a scientific model is judged strictly by its out-of-sample predictive accuracy.",
        "step_by_step_roadmap": [
            "Phase 1: Define prediction target (continuous variable or classification label) and forecast horizon.",
            "Phase 2: Split data strictly into Train, Validation, and Holdout Test partitions (or Rolling Window Time-Series).",
            "Phase 3: Engineer features avoiding look-ahead data leakage.",
            "Phase 4: Train competing econometric (ARIMA, Vector Autoregression) and ML models.",
            "Phase 5: Evaluate out-of-sample metrics (RMSE, MAE, AUC-ROC, Brier score, F1-score).",
            "Phase 6: Conduct Diebold-Mariano test to verify whether model differences are statistically significant."
        ],
        "data_collection_techniques": "High-frequency transaction logs, historical registry time-series, longitudinal patient vitals.",
        "data_analysis_methods": "K-fold cross-validation, Diebold-Mariano predictive accuracy test, OLS vs Ridge/Lasso, Random Forests, XGBoost.",
        "pitfalls_and_red_flags": [
            "Data leakage: allowing future information into predictor variables during feature engineering.",
            "Evaluating models solely on in-sample training R^2 rather than out-of-sample holdout test sets."
        ],
        "q1_checklist": [
            "Zero data leakage verified; rolling out-of-sample cross-validation implemented.",
            "Baseline comparison against naive random-walk or mean forecast.",
            "Diebold-Mariano or DeLong test confirming statistical superiority of final model."
        ],
        "recommended_tools": "Python (Scikit-Learn, Statsmodels, XGBoost), Typst."
    },
    {
        "id": "adversarial",
        "name": "Adversarial / Red-Team Research",
        "category": "Inquiry & Reasoning",
        "summary": "Critical, adversarial scientific investigation wherein independent researchers deliberately attempt to stress-test, debunk, reproduce, or find edge-case failure modes in an established theory, claim, or algorithm.",
        "when_to_use": [
            "When verifying whether an influential landmark paper's claims hold under independent scrutiny.",
            "When red-teaming AI models, algorithmic trading shields, or cryptographic security protocols.",
            "When challenging dogmatic scientific consensus with adversarial empirical counter-examples."
        ],
        "epistemology": "Critical Falsificationism: scientific robustness is established only when claims survive deliberate, well-funded adversarial attacks.",
        "step_by_step_roadmap": [
            "Phase 1: Identify specific published target claim, algorithm, or theoretical model.",
            "Phase 2: Acquire or reconstruct exact original code, data, and testing environments.",
            "Phase 3: Attempt direct exact replication to confirm baseline numbers.",
            "Phase 4: Design adversarial stress-tests (extreme market shocks, corrupted data vectors, out-of-distribution inputs).",
            "Phase 5: Measure points of failure, parameter sensitivity, and performance collapse.",
            "Phase 6: Publish adversarial audit documenting boundary limitations and counter-evidence."
        ],
        "data_collection_techniques": "Adversarial perturbation vectors, stress-testing logs, independently audited historical datasets.",
        "data_analysis_methods": "Robustness checks, extreme value theory, sensitivity curves, Monte Carlo perturbation testing.",
        "pitfalls_and_red_flags": [
            "Attacking a straw-man version of the original theory rather than its strongest formulation.",
            "Ad hominem hostility: scientific criticism must target empirical claims and mathematical models, not personalities."
        ],
        "q1_checklist": [
            "Direct replication attempted and documented before introducing adversarial tests.",
            "Full code repository released allowing original authors to verify failure modes.",
            "Fair, objective academic tone adhering to premier editorial rebuttal standards."
        ],
        "recommended_tools": "Python, Typst, Git."
    },
    {
        "id": "developmental",
        "name": "Developmental Research",
        "category": "Temporal & Growth",
        "summary": "Studies systematic change, progression, growth trajectories, or evolution over time (e.g., child cognitive development, software lifecycle maturity, organoid morphogenesis).",
        "when_to_use": [
            "When investigating how cognitive, biological, psychological, or organizational capabilities mature across defined chronological stages.",
            "When establishing developmental milestones, growth curve benchmarks, or learning curve asymptotes.",
            "When evaluating the persistence of early childhood or early-stage organizational interventions."
        ],
        "epistemology": "Developmental Positivism / Ecological Systems Theory: biological and environmental systems interact systematically across chronological maturation.",
        "step_by_step_roadmap": [
            "Phase 1: Define developmental construct and establish operational maturity indices.",
            "Phase 2: Select temporal tracking design (cross-sectional age slicing, longitudinal panel, or time-lagged design).",
            "Phase 3: Standardize repeated measurement instrumentation across age/maturity cohorts.",
            "Phase 4: Collect longitudinal time-series or multi-age cohort measurements.",
            "Phase 5: Estimate Latent Growth Curve Models (LGCM) or multi-level growth trajectories.",
            "Phase 6: Synthesize developmental milestone charts and predictive maturity curves."
        ],
        "data_collection_techniques": "Standardized psychometric milestones, physiological metrics, longitudinal observational scoring, developmental inventories.",
        "data_analysis_methods": "Latent Growth Curve Modeling (LGCM), Hierarchical Linear Modeling (HLM), Repeated Measures ANOVA, Survival/Event History Analysis.",
        "pitfalls_and_red_flags": [
            "Conflating cohort effects (generational differences) with true developmental maturation.",
            "Instrumentation drift: survey questions meaning different things to different age groups.",
            "Non-random panel attrition biasing late-stage trajectory estimates."
        ],
        "q1_checklist": [
            "Clear separation of age, period, and cohort effects documented.",
            "Measurement invariance (configural, metric, scalar) established across time points.",
            "Attrition analysis demonstrating missing data is Missing At Random (MAR) or Missing Completely At Random (MCAR)."
        ],
        "recommended_tools": "Python (Statsmodels), R (lavaan, nlme), Mplus, Typst."
    },
    {
        "id": "non_experimental_observational",
        "name": "Non-Experimental / Observational Research",
        "category": "Intervention Level",
        "summary": "Systematically measures variables and natural behaviors without active experimental manipulation or artificial environmental intervention.",
        "when_to_use": [
            "When ethical or practical barriers prohibit random assignment or artificial manipulation (e.g., studying health impacts of smoking or toxic emissions).",
            "When investigating high-ecological-validity natural behavior in wild or unconstrained operational settings.",
            "When testing associative hypotheses in preexisting epidemiological or market populations."
        ],
        "epistemology": "Post-Positivist Naturalism: observation of unconstrained nature reveals true ecological relationships that laboratory manipulation risks distorting.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate non-directional or directional associative hypothesis based on theoretical gap.",
            "Phase 2: Identify target population and prospective vs. retrospective observational registry.",
            "Phase 3: Design blind observational coding rubrics or unobtrusive telemetry instruments.",
            "Phase 4: Gather cross-sectional or cohort observational records with strict inter-rater reliability.",
            "Phase 5: Apply econometric confounder controls (Propensity Score Matching, Instrumental Variables, Multivariable Regression).",
            "Phase 6: Report STROBE-compliant observational manuscript with explicit causal disclaimers."
        ],
        "data_collection_techniques": "Automated telemetry, behavioral video coding, public registry extraction, structured naturalistic field logs.",
        "data_analysis_methods": "Propensity score matching (PSM), multivariable regression with HC3 robust standard errors, structural equation modeling, instrumental variables (IV).",
        "pitfalls_and_red_flags": [
            "Making unwarranted causal claims from purely observational associations (omitted variable bias).",
            "Observer bias or Hawthorne effect altering subject behavior during observation.",
            "Collider stratification bias creating spurious statistical dependencies."
        ],
        "q1_checklist": [
            "Adherence to STROBE (Strengthening the Reporting of Observational Studies in Epidemiology) guidelines.",
            "Detailed sensitivity analysis for unmeasured confounding (e.g., E-values).",
            "Explicit causal disclaimer highlighting non-interventional boundary."
        ],
        "recommended_tools": "Python (Statsmodels, scikit-learn), R (MatchIt), Typst."
    },
    {
        "id": "historical",
        "name": "Historical Research",
        "category": "Evidence & Sources",
        "summary": "Examines, verifies, and interprets past events, archival documents, oral testimonies, and physical records to reconstruct historical developments and derive contextual meaning.",
        "when_to_use": [
            "When examining the historical origins, evolution, or policy trajectory of a contemporary institution or scientific idea.",
            "When analyzing newly declassified archives, diplomatic correspondence, or legislative transcripts.",
            "When contextualizing past economic crises, pandemics, or technological revolutions to draw contemporary parallels."
        ],
        "epistemology": "Historicism / Hermeneutic Realism: historical facts must be understood within their temporal, linguistic, and socio-political context, subject to rigorous source criticism.",
        "step_by_step_roadmap": [
            "Phase 1: Identify historical anomaly, neglected event, or historiographical debate.",
            "Phase 2: Conduct exhaustive archival inventory across physical repositories, declassified collections, and digitised databases.",
            "Phase 3: Execute External Source Criticism (authenticity, provenance, authorship, physical integrity).",
            "Phase 4: Execute Internal Source Criticism (credibility, authorial bias, contemporaneous intent, corroboration).",
            "Phase 5: Synthesize chronological and thematic narrative linking empirical primary evidence to historiographical paradigm.",
            "Phase 6: Publish peer-reviewed historical monograph or analytical treatise."
        ],
        "data_collection_techniques": "Archival accession, diplomatic cables, private diaries, legal deeds, parliamentary records, oral history interviews.",
        "data_analysis_methods": "Hermeneutic text interpretation, historical source criticism, content analysis, prosopography (collective biography), discourse tracing.",
        "pitfalls_and_red_flags": [
            "Presentism: judging historical actors using modern moral, technical, or philosophical values.",
            "Cherry-picking isolated quotes while ignoring counter-evidence in surrounding archival folders.",
            "Failing to distinguish between primary eyewitness records and secondary hearsay accounts."
        ],
        "q1_checklist": [
            "Strict differentiation between primary archival sources and secondary scholarly interpretations.",
            "Complete archival citations including repository name, box, folder, and accession numbers.",
            "Systematic internal and external source verification documented."
        ],
        "recommended_tools": "Zotero, NVivo, Tesseract OCR, Typst 0.15."
    },
    {
        "id": "philosophical",
        "name": "Philosophical Research",
        "category": "Reasoning & Logic",
        "summary": "Employs formal logic, conceptual analysis, dialectics, and critical thought experiments to clarify concepts, evaluate fundamental assumptions, and formulate normative ethical principles.",
        "when_to_use": [
            "When analyzing conceptual confusion or semantic ambiguity in scientific terminology (e.g., definition of 'consciousness' or 'algorithmic fairness').",
            "When evaluating ethical implications of emerging technologies (e.g., autonomous lethal weapons, genetic editing).",
            "When challenging epistemic foundations of reigning scientific paradigms."
        ],
        "epistemology": "Rationalism & Conceptual Realism: fundamental conceptual structures, logical validity, and normative ethics can be discovered through rigorous deductive inquiry.",
        "step_by_step_roadmap": [
            "Phase 1: Identify foundational concept, moral dilemma, or ontological contradiction.",
            "Phase 2: Formalize prevailing philosophical arguments into explicit premises and syllogisms.",
            "Phase 3: Formulate counter-examples or thought experiments (Gedankenexperiment) testing premise validity.",
            "Phase 4: Analyze semantic ambiguities, hidden presuppositions, or category mistakes.",
            "Phase 5: Synthesize novel conceptual framework or normative ethical rubric.",
            "Phase 6: Defend thesis against leading philosophical objections in a structured treatise."
        ],
        "data_collection_techniques": "Philosophical treatises, canonical literature, formal logical proofs, thought experiment frameworks.",
        "data_analysis_methods": "Formal propositional and modal logic, conceptual analysis, dialectical counter-argumentation, reflective equilibrium.",
        "pitfalls_and_red_flags": [
            "Begging the question (petitio principii) or circular reasoning in foundational premises.",
            "Constructing unassailable tautologies that offer no actionable conceptual differentiation.",
            "Ignoring empirical scientific findings that directly constrain the conceptual space."
        ],
        "q1_checklist": [
            "Formal representation of core arguments with premises and conclusions numbered.",
            "Anticipation and rebuttal of at least three serious counter-arguments.",
            "Clarity of definitions with avoidance of unnecessary obscurantist jargon."
        ],
        "recommended_tools": "LaTeX, Typst 0.15, Truth Table Solvers, Stanford Encyclopedia of Philosophy."
    },
    {
        "id": "sequential",
        "name": "Sequential Research",
        "category": "Temporal & Longitudinal",
        "summary": "Combines cross-sectional and longitudinal cohort designs over time to disentangle age maturation, cohort effects, and historical time-of-measurement period effects.",
        "when_to_use": [
            "When studying long-term psychological or sociological trends where generational shifts might confound age-related maturation.",
            "When validating educational or cognitive interventions across successive student generations.",
            "When longitudinal studies alone take too long to produce initial policy insights."
        ],
        "epistemology": "Schaie's Most Efficient Design: human development is a multi-dimensional matrix of ontogenetic age changes and sociological generational shifts.",
        "step_by_step_roadmap": [
            "Phase 1: Select initial cross-sectional sample spanning multiple age cohorts (e.g., ages 20, 30, 40 at Time 1).",
            "Phase 2: Collect baseline psychometric or behavioral metrics across all cohorts.",
            "Phase 3: Re-measure the original cohorts at Time 2 (longitudinal follow-up) while concurrently enrolling a new baseline cohort of age 20.",
            "Phase 4: Repeat sequence across Time 3, Time 4 to build a complete age-by-cohort matrix.",
            "Phase 5: Run Schaie's Sequential Analysis partitioning variance into Age, Cohort, and Time of Measurement.",
            "Phase 6: Synthesize unified developmental manuscript isolating true maturation from historical cultural shifts."
        ],
        "data_collection_techniques": "Multi-cohort repeated survey batteries, cognitive tests, physiological monitoring across rolling decades.",
        "data_analysis_methods": "Cohort-Sequential Modeling, Age-Period-Cohort (APC) models, Multilevel Linear Growth Modeling, Time-Lagged Cross-Correlations.",
        "pitfalls_and_red_flags": [
            "Identification problem: perfect collinearity among Age = Period - Cohort requiring constrained estimators.",
            "Unequal attrition rates between older and younger cohorts distorting long-term comparisons.",
            "Significant cost and multi-year management overhead across changing investigator teams."
        ],
        "q1_checklist": [
            "Rigorous handling of the APC identification problem (e.g., intrinsic estimator or bounding methods).",
            "Longitudinal measurement equivalence verified across cohorts and re-test sessions.",
            "Practice effects (re-testing gains) formally modeled and separated from developmental gains."
        ],
        "recommended_tools": "R (apc package, lavaan), Python (Statsmodels), Typst."
    },
    {
        "id": "field_research",
        "name": "Field Research",
        "category": "Setting & Environment",
        "summary": "Conducts empirical investigation directly within natural, real-world environments without artificial laboratory constraints, maximizing ecological validity.",
        "when_to_use": [
            "When laboratory settings induce artificial behavior or Hawthorne bias (e.g., consumer retail choices, wildlife ecology, emergency room workflows).",
            "When capturing complex environmental context, social rituals, or spontaneous interactions is paramount.",
            "When conducting geological, ecological, or community sociological fieldwork."
        ],
        "epistemology": "Ecological Realism: biological, cognitive, and social phenomena cannot be understood in isolation from the complex, messy physical habitats in which they naturally occur.",
        "step_by_step_roadmap": [
            "Phase 1: Select natural field site, negotiate community gatekeeper access, and secure institutional ethics.",
            "Phase 2: Deploy robust mobile instrumentation (weatherproof sensors, mobile telemetry, audio/video recorders).",
            "Phase 3: Establish baseline observational periods to acclimatize subjects and reduce observer disruption.",
            "Phase 4: Collect contextual field notes, environmental telemetry, and spontaneous behavioral recordings.",
            "Phase 5: Triangulate qualitative field observations with quantitative sensor logging and GPS spatial mapping.",
            "Phase 6: Synthesize high-fidelity ecological monograph with full environmental context parameters."
        ],
        "data_collection_techniques": "Naturalistic observation logs, mobile GPS telemetry, environmental sensors, field audio interviews, photovoice.",
        "data_analysis_methods": "Spatial GIS analysis, contextual thematic coding, environmental interaction matrices, situational behavioral density estimation.",
        "pitfalls_and_red_flags": [
            "Uncontrollable environmental confounders (weather, unexpected public interruptions, site contamination).",
            "Investigator safety and legal vulnerabilities in remote or hazardous field environments.",
            "High risk of subjective observer interpretation without standardized double-blind verification rubrics."
        ],
        "q1_checklist": [
            "Thorough documentation of site entry permits, community consent, and environmental impact audits.",
            "GPS spatial coordinates and ambient environmental conditions recorded alongside data points.",
            "Clear discussion of trade-offs between high ecological validity and reduced internal control."
        ],
        "recommended_tools": "QGIS, Python (GeoPandas, Folium), Epicollect5, Typst."
    },
    {
        "id": "laboratory_research",
        "name": "Laboratory Research",
        "category": "Setting & Environment",
        "summary": "Conducts investigation in tightly controlled artificial laboratory environments to isolate precise causal mechanisms, manipulate independent variables, and eliminate extraneous noise.",
        "when_to_use": [
            "When establishing definitive physical, chemical, neurobiological, or psychophysical cause-and-effect relationships.",
            "When testing high-precision mechanistic hypotheses that require calibration to microsecond or nanometer precision.",
            "When minimizing ambient temperature, light, sound, or electromagnetic interference is required."
        ],
        "epistemology": "Positivist Reductionism: isolating components under closed boundary conditions allows uncovering universal fundamental physical or behavioral laws.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate mechanistic hypothesis and calibrate precision laboratory apparatus.",
            "Phase 2: Standardize environmental parameters (ambient temperature, humidity, acoustic isolation, light cycle).",
            "Phase 3: Randomly assign subjects or experimental units to experimental vs. vehicle control conditions.",
            "Phase 4: Execute standardized experimental protocol with automated data acquisition hardware.",
            "Phase 5: Run ANOVA, dose-response curve fitting, signal detection analysis, or multivariate regression.",
            "Phase 6: Author lab report adhering to ARRIVE or physical science reproducibility guidelines."
        ],
        "data_collection_techniques": "Spectroscopy, automated high-throughput assays, EEG/fMRI bio-amplifiers, eye-tracking, oscilloscope logs.",
        "data_analysis_methods": "Dose-response non-linear regression, repeated measures ANOVA, signal-to-noise ratio (SNR) filtering, bootstrap error modeling.",
        "pitfalls_and_red_flags": [
            "Sterile laboratory conditions failing to generalize to complex, messy real-world conditions (low ecological validity).",
            "Demand characteristics: human subjects guessing the experimenter's hypothesis and modifying actions.",
            "Subtle equipment calibration drift across long testing sessions introducing artifactual variance."
        ],
        "q1_checklist": [
            "Adherence to ARRIVE guidelines for animal studies or standard physical reporting checklists.",
            "Detailed equipment specifications including manufacturer, serials, calibration standards, and firmware version.",
            "Blind outcome assessment and negative/positive control curves reported."
        ],
        "recommended_tools": "LabVIEW, Python (NumPy, SciPy, MNE), MATLAB, Typst."
    },
    {
        "id": "conceptual",
        "name": "Conceptual Research",
        "category": "Reasoning & Theory",
        "summary": "Develops, synthesizes, and refines abstract theoretical models, conceptual frameworks, and taxonomy systems by critically integrating existing literature without gathering primary empirical data.",
        "when_to_use": [
            "When an academic field suffers from fragmented definitions, conflicting models, or contradictory empirical findings.",
            "When synthesizing cross-disciplinary insights into a unified paradigm (e.g., combining neuroscience with behavioral economics).",
            "When establishing a foundational taxonomy or conceptual architecture to guide future empirical research."
        ],
        "epistemology": "Theoretical Coherentism: theoretical maturity is achieved when conceptual constructs exhibit internal logical consistency, parsimony, and broad explanatory scope.",
        "step_by_step_roadmap": [
            "Phase 1: Identify terminological confusion, contradictory models, or conceptual vacuum in the target literature.",
            "Phase 2: Conduct an extensive multi-disciplinary literature survey mapping how core constructs have been operationalized.",
            "Phase 3: Identify latent contradictions, overlaps, and boundary limitations in prevailing theories.",
            "Phase 4: Formulate novel conceptual framework: define core dimensions, boundary conditions, and relational propositions.",
            "Phase 5: Draw visual conceptual architecture diagram and derive formal, falsifiable testable propositions.",
            "Phase 6: Structure conceptual review paper (e.g., for Academy of Management Review or Nature Reviews)."
        ],
        "data_collection_techniques": "Exhaustive scholarly literature corpus, canonical texts, patent databases, conceptual meta-syntheses.",
        "data_analysis_methods": "Conceptual scoping, integrative synthesis, taxonomic differentiation, axiomatic deduction, propositional modeling.",
        "pitfalls_and_red_flags": [
            "Producing trivial repackaging of existing models without genuine intellectual novelty or theoretical contribution.",
            "Failing to formulate explicit, testable, and falsifiable propositions for future empirical researchers.",
            "Lack of clear boundary conditions: claiming the conceptual model applies universally without stating when it breaks down."
        ],
        "q1_checklist": [
            "Visual conceptual model diagram clearly delineating constructs, mediators, and moderators.",
            "Explicit numbered theoretical propositions (P1, P2, P3...) ready for empirical testing.",
            "Clear demarcation of theoretical contribution against prior landmark conceptual papers."
        ],
        "recommended_tools": "Draw.io, Typst 0.15, Zotero, Connected Papers, Scopus."
    },
    {
        "id": "empirical",
        "name": "Empirical Research",
        "category": "Evidence & Sources",
        "summary": "Derives scientific knowledge and tests hypotheses through direct, verifiable observation, measurement, and sensory experimentation, adhering strictly to reproducible data vectors.",
        "when_to_use": [
            "When verifying whether theoretical predictions or common assumptions actually hold in observable reality.",
            "When quantifying exact effect sizes, regression coefficients, or prevalence rates in real populations.",
            "When generating reproducible evidentiary benchmarks for science, policy, or clinical practice."
        ],
        "epistemology": "Scientific Empiricism / Critical Realism: genuine scientific knowledge must be anchored in sensory observation, empirical measurement, and falsifiable mathematical testing.",
        "step_by_step_roadmap": [
            "Phase 1: Formulate falsifiable empirical hypothesis derived from literature or inductive observation.",
            "Phase 2: Operationalize abstract constructs into measurable indicators (survey items, physical sensors, financial logs).",
            "Phase 3: Formulate rigorous sampling and data collection protocol with institutional review clearance.",
            "Phase 4: Collect raw empirical observations, ensuring complete audit trails and cryptographic integrity.",
            "Phase 5: Conduct hypothesis testing (ANOVA, robust OLS, non-parametric tests) and report exact p-values.",
            "Phase 6: Compile empirical paper with data availability statement and replication scripts."
        ],
        "data_collection_techniques": "Sensor arrays, calibrated laboratory instruments, psychometric questionnaires, financial transaction databases.",
        "data_analysis_methods": "Descriptive statistics, inferential hypothesis testing, effect size estimation (Cohen's d, eta^2), confidence intervals, regression diagnostics.",
        "pitfalls_and_red_flags": [
            "HARK-ing (Hypothesizing After Results are Known): retrofitting hypotheses to match accidental statistical anomalies.",
            "Selective reporting of statistically significant outcomes while hiding non-significant null results.",
            "Failing to deposit raw data or analysis scripts for independent peer replication."
        ],
        "q1_checklist": [
            "Full Open Science Framework (OSF) pre-registration or explicit data availability statement.",
            "Power calculations verifying adequate statistical power (>= 0.80) to detect targeted effect sizes.",
            "Zero ghostwriting guarantee with cryptographically signed analysis scripts."
        ],
        "recommended_tools": "Python (SciPy, Statsmodels), R, Typst 0.15, GitHub, OSF."
    },
    {
        "id": "strategic",
        "name": "Strategic Research",
        "category": "Purpose & Domain",
        "summary": "Focuses on generating actionable foresight, competitive intelligence, and long-range intelligence to inform high-stakes enterprise governance, public policy, and national competitiveness.",
        "when_to_use": [
            "When charting multi-year technology roadmaps, national defense priorities, or enterprise digital transformations.",
            "When evaluating geopolitical, macroeconomic, or technological disruptions over a 5 to 20-year horizon.",
            "When synthesizing competitive market positioning and scenario planning matrices for executive boards."
        ],
        "epistemology": "Strategic Pragmatism: research is judged by its ability to mitigate existential risk, seize asymmetric competitive opportunities, and enhance long-term organizational viability.",
        "step_by_step_roadmap": [
            "Phase 1: Define strategic scope, critical uncertainties, and institutional decision horizons.",
            "Phase 2: Scan macroeconomic, technological, regulatory, and demographic macro-trends (PESTLE framework).",
            "Phase 3: Formulate multi-scenario matrix (e.g., 2x2 uncertainty axes) detailing plausible future operating worlds.",
            "Phase 4: Model strategic options, war-gaming contingencies, and stress-test core institutional assumptions.",
            "Phase 5: Identify early warning indicator tripwires to monitor real-time migration toward specific scenarios.",
            "Phase 6: Synthesize executive strategic briefing with concrete, prioritized resource-allocation recommendations."
        ],
        "data_collection_techniques": "Delphi expert consensus panels, patent intelligence, competitive benchmarking, geopolitical risk indices, macroeconomic forecasts.",
        "data_analysis_methods": "Scenario planning, Delphi method, SWOT/PESTLE matrix synthesis, game-theoretic payoff modeling, cross-impact analysis.",
        "pitfalls_and_red_flags": [
            "Status quo bias: assuming prevailing market or geopolitical conditions will continue indefinitely.",
            "Groupthink: executive confirmation bias suppressing contrarian intelligence or emerging disruptive threats.",
            "Vague, generic strategic recommendations that fail to specify clear trade-offs, timelines, or capital allocations."
        ],
        "q1_checklist": [
            "Explicit 2x2 uncertainty matrix or multi-scenario framework presented.",
            "Delphi expert consensus methodology with panel qualification criteria and consensus thresholds defined.",
            "Actionable strategic roadmap linking scenario indicators to resource-allocation decisions."
        ],
        "recommended_tools": "Typst 0.15, Python (Pandas, Matplotlib), Miro, Zotero."
    },
    {
        "id": "collaborative",
        "name": "Collaborative / Multi-Institutional Research",
        "category": "Organizational Structure",
        "summary": "Unites researchers across multiple academic departments, international institutions, or public-private consortia to tackle grand challenges requiring distributed expertise and shared infrastructure.",
        "when_to_use": [
            "When addressing complex grand challenges (e.g., climate change, genomics, particle physics) beyond single-lab capabilities.",
            "When clinical or epidemiological trials require multi-center patient recruitment across diverse geographic sites.",
            "When securing international consortium grants (Horizon Europe, NIH U-series, NSF Large Facilities)."
        ],
        "epistemology": "Interdisciplinary Synergy & Transdisciplinary Synthesis: complex real-world systems require transcending siloed disciplinary boundaries through collaborative convergence.",
        "step_by_step_roadmap": [
            "Phase 1: Establish consortium governance charter, authorship agreements (Vancouver ICMJE rules), and intellectual property agreements.",
            "Phase 2: Design unified cross-institutional research protocol and standardize data-gathering instruments across all participating sites.",
            "Phase 3: Secure reciprocal IRB/ethics approvals across all partner institutions and deploy secure federated data repository.",
            "Phase 4: Execute coordinated data collection with continuous cross-site quality audits and inter-site calibration checks.",
            "Phase 5: Conduct centralized statistical analysis on harmonized multi-site datasets with site-random-effect modeling.",
            "Phase 6: Co-author multi-institutional manuscript with standardized CRediT contributor taxonomy."
        ],
        "data_collection_techniques": "Multi-center electronic health records (EHR), distributed sensor networks, harmonized multi-lingual survey registries, federated biobanks.",
        "data_analysis_methods": "Multilevel Mixed-Effects Models (clustering by site/institution), meta-analysis, federated machine learning, harmonized survival curves.",
        "pitfalls_and_red_flags": [
            "Authorship disputes: lack of pre-agreed contributor taxonomy leading to conflicts during manuscript submission.",
            "Batch effects: uncontrolled site-specific measurement variance obscuring true biological or social signals.",
            "Communication breakdowns and delayed milestones due to time-zone and organizational culture friction."
        ],
        "q1_checklist": [
            "Complete CRediT (Contributor Roles Taxonomy) author contribution statement published.",
            "Statistical modeling explicitly accounting for multi-site clustering variance (e.g., random intercepts for site).",
            "Pre-agreed Data Transfer Agreements (DTA) and open-science repository access verified."
        ],
        "recommended_tools": "Git, Typst 0.15, Python (Statsmodels mixedlm), REDCap, OSF."
    }

]

def get_all_guides():
    return RESEARCH_GUIDES

def get_guide_by_id(guide_id: str):
    for g in RESEARCH_GUIDES:
        if g["id"] == guide_id or g["id"] in guide_id:
            return g
    return RESEARCH_GUIDES[0]
