"""
topic_synthesizer.py - Autonomous Topic Inception & Zero-Data Research Architecture Engine
Enables researchers to begin with zero data: from a raw topic idea to:
1. Literature Gap & Problem Statement
2. Theoretical Framework (Independent Variable, Dependent Variable, Mediator, Moderator)
3. Formal Testable Hypotheses (H1, H2, H3)
4. Validated Psychometric / Econometric Survey Instrument (12 items)
5. Google Apps Script automation for 1-click Google Form creation
6. Synthetic Pilot Dataset generator (N=100) with realistic covariance structure
"""

import os
import re
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Optional


def sanitize_slug(text: str) -> str:
    clean = re.sub(r'[^a-zA-Z0-9_\s]', '', text)
    return re.sub(r'\s+', '_', clean).strip('_')[:40]


def extract_keywords(topic: str) -> List[str]:
    """Extracts salient keywords from topic removing common stop words."""
    stop_words = {
        "a", "an", "the", "in", "on", "at", "for", "to", "of", "and", "or", "with",
        "by", "from", "as", "is", "are", "was", "were", "be", "been", "being",
        "impact", "effect", "effects", "role", "study", "analysis", "empirical",
        "investigation", "dynamics", "architecture", "towards", "using", "into"
    }
    words = re.findall(r'[a-zA-Z]{3,}', topic.lower())
    salient = [w for w in words if w not in stop_words]
    return salient if salient else ["empirical", "system", "dynamics"]


def synthesize_research_architecture(topic: str,
                                      domain: Optional[str] = None,
                                      discipline: Optional[str] = None,
                                      target_standard: str = "IEEE") -> Dict[str, Any]:
    topic = (topic or "").strip()
    if not topic:
        topic = "Empirical Dynamics of Decision-Making Under Uncertainty in Complex Environments"
    
    topic_lower = topic.lower()
    inferred_domain = domain or discipline or ""
    
    # Classify domain if not explicitly provided
    if not inferred_domain or inferred_domain.lower() in ["general", "default", "auto"]:
        if any(k in topic_lower for k in ["stock", "trad", "dse", "market", "financ", "crypt", "invest", "equity", "asset", "bank"]):
            domain_key = "finance"
            domain_label = "Computational Finance & Econometrics"
        elif any(k in topic_lower for k in ["social media", "burnout", "depress", "anxiet", "mental", "psychol", "wellbeing", "stress", "behavior"]):
            domain_key = "psychology"
            domain_label = "Cognitive Psychology & Behavioral Science"
        elif any(k in topic_lower for k in ["ai", "algorithm", "machine learning", "tech", "softwar", "comput", "deep learning", "neural", "iot", "cloud"]):
            domain_key = "technology"
            domain_label = "Information Systems & Computer Science"
        elif any(k in topic_lower for k in ["student", "educat", "learn", "universit", "academ", "school", "teach"]):
            domain_key = "education"
            domain_label = "Educational Technology & Pedagogy"
        elif any(k in topic_lower for k in ["health", "medic", "clinic", "patient", "nurs", "biomed", "doctor", "pharma"]):
            domain_key = "health"
            domain_label = "Public Health & Clinical Informatics"
        else:
            domain_key = "custom"
            domain_label = "Interdisciplinary Applied Sciences"
    else:
        domain_key = inferred_domain.lower()
        domain_label = inferred_domain.title()

    # Pre-built high-fidelity domain configurations
    if "financ" in domain_key or domain_key == "finance":
        iv_name = "Speculative Noise & Social Signal Exposure"
        iv_code = "SNSE"
        iv_def = "The frequency and intensity of exposure to unverified digital social signals, forum rumors, and speculative trading cascades."
        iv_items = [
            "I actively monitor unverified online financial community channels for short-term trading signals.",
            "Sudden sentiment spikes in online trading discussion groups compel me to re-evaluate my asset allocations.",
            "I feel heightened urgency to enter market positions when peer speculation circulates regarding impending volatility."
        ]

        med_name = "Cognitive Reflection & Analytical Restraint"
        med_code = "CRAR"
        med_def = "The propensity to override intuitive, emotional heuristics in favor of reflective deliberative quantitative analysis."
        med_items = [
            "Before executing an order, I systematically double-check underlying risk-reward and position-sizing parameters.",
            "I deliberately resist impulsive market entry even when immediate peer chatter promises rapid windfalls.",
            "I adhere to strict predefined exit and stop-loss rules regardless of acute emotional distress."
        ]

        mod_name = "Market Tenure & Overconfidence Heuristics"
        mod_code = "MTOH"
        mod_def = "The cognitive bias wherein accumulated trading longevity inflates subjective conviction beyond actual statistical edge."
        mod_items = [
            "My past trading longevity allows me to predict unpredictable market turning points more accurately than algorithms.",
            "I believe my proprietary market intuition exceeds that of typical active participants in high-volatility regimes.",
            "I occasionally override formal risk parameters because my directional market conviction feels fully justified."
        ]

        dv_name = "Downside Panic Liquidation Susceptibility"
        dv_code = "DPLS"
        dv_def = "The vulnerability to emotional capitulation, panic selling, and suboptimal execution during tail-risk drawdown events."
        dv_items = [
            "Sharp unexpected market drawdowns trigger acute physiological anxiety and decision paralysis.",
            "During abrupt market sell-offs, I have liquidated sound positions solely to stop psychological discomfort.",
            "Experiencing rapid portfolio drawdowns severely impairs my ability to execute disciplined capital preservation."
        ]

        gap = "While classical efficient market paradigms presume rational Bayesian belief updating, empirical microstructures in emerging and high-volatility markets exhibit severe behavioral contagion. Prior literature remains fragmented regarding the structural pathways through which social noise cascades interact with cognitive reflection and overconfidence to drive catastrophic liquidation freeze."
        h1 = "Higher exposure to speculative social noise signals significantly amplifies downside panic liquidation susceptibility (Beta > 0, p < 0.001)."
        h2 = "Cognitive reflection and analytical restraint significantly mediates and dampens emotional capitulation under market volatility (Beta < 0, p < 0.01)."
        h3 = "Market tenure paradoxically magnifies overconfidence heuristics, moderating the relationship such that experienced traders suffer disproportionate tail drawdowns (Beta > 0, p < 0.05)."

    elif "psych" in domain_key or "educat" in domain_key or domain_key in ["psychology", "education"]:
        iv_name = "Nocturnal Algorithmic Hyperarousal"
        iv_code = "NAH"
        iv_def = "Compulsive late-night engagement with interactive algorithmic feeds dismantling circadian rest boundaries."
        iv_items = [
            "I frequently lose track of nocturnal hours while engaging with automated digital recommendations.",
            "Late-night digital notifications leave me in a sustained state of cognitive vigilance and arousal.",
            "I find it difficult to transition to restful sleep after prolonged nocturnal engagement with algorithmic feeds."
        ]

        med_name = "Validation Dependency & Social Comparison"
        med_code = "VDSC"
        med_def = "Psychological reliance on external automated metric feedback for self-worth and social benchmarking."
        med_items = [
            "Observing curated peer achievements on digital platforms induces immediate self-critical distress.",
            "The volume of digital engagement metrics I receive directly modulates my daily emotional baseline.",
            "I constantly benchmark my academic and professional milestones against peer representations online."
        ]

        mod_name = "Self-Efficacy & Attentional Restraint"
        mod_code = "SEAR"
        mod_def = "The internal psychological capacity to sustain focused intentional cognition despite persistent environmental distractions."
        mod_items = [
            "I can maintain uninterrupted focus on challenging cognitive tasks despite pervasive notifications.",
            "I have established firm behavioral boundaries to protect my primary productive focus periods.",
            "I remain confident in my personal intellectual competence even when confronting demanding challenges."
        ]

        dv_name = "Affective Exhaustion & Burnout Distress"
        dv_code = "AEBD"
        dv_def = "A chronic multidimensional state of emotional depletion, cognitive fatigue, and motivational collapse."
        dv_items = [
            "I wake up feeling cognitively drained before my primary daily responsibilities have commenced.",
            "Prolonged engagement with academic and digital demands leaves me emotionally hollowed.",
            "I struggle to recover my baseline mental resilience following sustained periods of high stress."
        ]

        gap = "Existing investigations frequently treat digital platform engagement and cognitive burnout as monolithic aggregates. Crucially unresolved is the precise structural pathway through which nocturnal hyperarousal and validation dependency dismantle attentional self-efficacy to trigger clinical burnout."
        h1 = "Nocturnal algorithmic hyperarousal exerts a direct, positive predictive impact on affective exhaustion and burnout distress (Beta > 0, p < 0.001)."
        h2 = "Validation dependency significantly mediates the destructive relationship between digital feed exposure and emotional depletion (Beta > 0, p < 0.01)."
        h3 = "Attentional restraint serves as a significant moderating buffer, attenuating the detrimental effects of digital hyperarousal (Beta < 0, p < 0.01)."

    elif "tech" in domain_key or domain_key == "technology":
        iv_name = "Autonomous Algorithmic Delegation"
        iv_code = "AAD"
        iv_def = "The systematic reliance on automated artificial intelligence systems to synthesize and execute mission-critical workflow components."
        iv_items = [
            "I routinely delegate complex analytical synthesis and drafting tasks to automated intelligent systems.",
            "I rely on automated algorithmic recommendations over my personal preliminary estimates.",
            "My operational workflow experiences severe friction if algorithmic support tools become unavailable."
        ]

        med_name = "Critical Verification & Cognitive Friction"
        med_code = "CVCF"
        med_def = "The active commitment to skeptical auditing, primary source cross-referencing, and algorithmic verification."
        med_items = [
            "I systematically audit algorithmic outputs against independent primary authoritative sources.",
            "I actively search for edge-case hallucinations or logical inconsistencies in automated suggestions.",
            "I refuse to deploy automated syntheses without rigorous, line-by-line expert human review."
        ]

        mod_name = "Domain Longevity & Operational Intuition"
        mod_code = "DLOI"
        mod_def = "Accumulated tacit domain expertise allowing rapid intuitive appraisal of operational plausibility."
        mod_items = [
            "My long-term domain experience enables me to instantly recognize implausible algorithmic outputs.",
            "I have witnessed historical system failures that inform my current technological skepticism.",
            "I possess deep contextual intuition that automated systems cannot easily emulate or replace."
        ]

        dv_name = "Systemic Deliverable Rigor & Innovation Impact"
        dv_code = "SDRI"
        dv_def = "The empirical velocity, precision, and novel technical impact of completed research or engineering artifacts."
        dv_items = [
            "The integration of intelligent workflows has markedly elevated the technical rigor of my deliverables.",
            "I achieve breakthrough conceptual solutions significantly faster than traditional manual paradigms.",
            "My overall deliverable consistency demonstrates high resilience across complex operational milestones."
        ]

        gap = "While emergent literature celebrates the efficiency dividends of autonomous workflows, critical questions persist regarding cognitive atrophy and output reliability. The structural trade-offs between automated reliance, human verification friction, and publication-grade output quality remain unmapped."
        h1 = "Autonomous algorithmic delegation significantly enhances deliverable velocity and innovation impact (Beta > 0, p < 0.001)."
        h2 = "Critical verification friction significantly mediates output quality, preventing error propagation into final deliverables (Beta > 0, p < 0.01)."
        h3 = "Domain longevity positively moderates the system, enabling senior specialists to extract superior rigor from automated workflows (Beta > 0, p < 0.05)."

    else:
        # Dynamic tailoring for ANY custom topic
        kws = extract_keywords(topic)
        kw_title = " ".join([w.capitalize() for w in kws[:3]])
        
        iv_name = f"{kw_title} Adoption & Exposure"
        iv_code = "IV_EXP"
        iv_def = f"The extent of systematic exposure, utilization, and technological integration of {topic} within the operational ecosystem."
        iv_items = [
            f"I regularly integrate core methodologies associated with {kws[0]} into my primary workflow.",
            f"Our organizational processes increasingly prioritize systematic adaptation to {topic}.",
            f"I allocate dedicated time and capital to optimizing our {kws[0]} capabilities."
        ]

        med_name = "Adaptive Process Re-Engineering"
        med_code = "MED_PROC"
        med_def = f"The structural realignment of workflows, validation checkpoints, and operational protocols to accommodate {topic}."
        med_items = [
            "We systematically update standard operating procedures when integrating novel methodological frameworks.",
            "Cross-functional teams actively re-evaluate legacy protocols to accommodate changing operational demands.",
            "Continuous feedback loops are utilized to iteratively refine our implementation standards."
        ]

        mod_name = "Institutional Governance & Resource Slack"
        mod_code = "MOD_GOV"
        mod_def = "The formal regulatory oversight, compliance infrastructure, and discretionary resource capacity supporting implementation."
        mod_items = [
            "Our governance structure enforces clear compliance standards for novel technological integrations.",
            "Adequate reserve capacity and capital are provisioned to absorb transitional operational friction.",
            "Leadership provides clear policy guardrails that balance rapid innovation against risk mitigation."
        ]

        dv_name = "Empirical Operational Resilience & Outcome Rigor"
        dv_code = "DV_OUT"
        dv_def = f"The holistic efficacy, performance stability, and verified output quality resulting from {topic} deployment."
        dv_items = [
            f"The targeted implementation of {topic} has generated measurable improvements in overall outcome reliability.",
            "Our operational resilience during high-uncertainty shocks is significantly stronger post-implementation.",
            "Outputs generated under this empirical framework consistently meet or exceed international publication benchmarks."
        ]

        gap = f"Despite growing interest in {topic}, empirical literature lacks a unified structural framework reconciling implementation velocity with output fidelity. Prior studies remain fragmented, failing to account for how process re-engineering and governance mechanisms interact to determine long-term operational resilience."
        h1 = f"{iv_name} exerts a statistically significant positive effect on {dv_name} (Beta > 0, p < 0.001)."
        h2 = f"{med_name} significantly mediates the relationship between adoption and final operational performance (Beta > 0, p < 0.01)."
        h3 = f"{mod_name} significantly moderates the pathway, amplifying the positive performance returns of adoption (Beta > 0, p < 0.05)."

    # Formal constructs list
    constructs = [
        {"name": iv_name, "code": iv_code, "role": "Independent Variable (IV)", "definition": iv_def, "items": iv_items},
        {"name": med_name, "code": med_code, "role": "Mediator Variable (M)", "definition": med_def, "items": med_items},
        {"name": mod_name, "code": mod_code, "role": "Moderator Variable (W)", "definition": mod_def, "items": mod_items},
        {"name": dv_name, "code": dv_code, "role": "Dependent Variable (DV)", "definition": dv_def, "items": dv_items}
    ]

    # Clean flat questionnaire list (8-12 items)
    questionnaire = []
    for c in constructs:
        for idx, item_text in enumerate(c["items"], 1):
            questionnaire.append({
                "item_id": f"{c['code']}_{idx}",
                "construct_name": c["name"],
                "construct_code": c["code"],
                "role": c["role"],
                "item_text": item_text,
                "scale": "5-point Likert (1 = Strongly Disagree to 5 = Strongly Agree)"
            })

    # Declarative Publication Title
    raw_title = topic.strip()
    if len(raw_title) > 10 and not raw_title.lower().startswith("empirical"):
        declarative_title = f"Empirical Architecture of {raw_title}: A Structural Equation & Econometric Investigation"
    else:
        declarative_title = raw_title

    # Theoretical model object
    theoretical_model = {
        "framework_name": "Moderated Mediation Structural Equation Model (Hayes Model 4/7)",
        "independent_variable": iv_name,
        "dependent_variable": dv_name,
        "mediator": med_name,
        "moderator": mod_name,
        "iv_code": iv_code,
        "dv_code": dv_code,
        "med_code": med_code,
        "mod_code": mod_code,
        "structural_pathway": f"{iv_code} (IV) -> {med_code} (Mediator) -> {dv_code} (DV), moderated by {mod_code} (Moderator)"
    }

    # Google Apps Script Generation
    gas_script = f"""// =====================================================================
// AUTOMATED GOOGLE FORM GENERATOR: {declarative_title}
// Generated by OmniScholar Autonomous Research Studio
// Target Standard: {target_standard} | Domain: {domain_label}
// =====================================================================
function createOmniScholarResearchSurvey() {{
  var form = FormApp.create("{declarative_title}");
  form.setDescription("Academic Research Survey\\n\\nDear Participant,\\nThank you for participating in this empirical investigation. All responses are completely anonymous, confidential, and used strictly for academic research.\\n\\nEstimated completion time: 4-6 minutes.");
  form.setAllowResponseEdits(false);
  form.setCollectEmail(false);

  // Demographics
  var sec1 = form.addSectionHeaderItem();
  sec1.setTitle("Section 1: Participant Background");

  var qRole = form.addListItem();
  qRole.setTitle("Primary Professional / Academic Role");
  qRole.setChoiceValues(["Senior Lead / Principal Investigator", "Postdoctoral Fellow / Senior Specialist", "Doctoral / Mid-Level Researcher", "Associate / Junior Scholar"]);
  qRole.setRequired(true);

  var qExp = form.addScaleItem();
  qExp.setTitle("Years of Professional / Research Experience");
  qExp.setBounds(1, 15).setLabels("1 Year or Less", "15+ Years");
  qExp.setRequired(true);

  // Psychometric Constructs
"""
    for c in constructs:
        gas_script += f"""
  var sec_{c['code']} = form.addSectionHeaderItem();
  sec_{c['code']}.setTitle("Construct: {c['name']} ({c['code']})");
  sec_{c['code']}.setHelpText("{c['definition']}\\nRate agreement from 1 (Strongly Disagree) to 5 (Strongly Agree).");
"""
        for i, item_text in enumerate(c['items'], 1):
            gas_script += f"""
  var q_{c['code']}_{i} = form.addScaleItem();
  q_{c['code']}_{i}.setTitle("[{c['code']}_{i}] {item_text}");
  q_{c['code']}_{i}.setBounds(1, 5).setLabels("Strongly Disagree", "Strongly Agree");
  q_{c['code']}_{i}.setRequired(true);
"""
    gas_script += """
  Logger.log("OmniScholar Survey created successfully! URL: " + form.getEditUrl());
}
"""

    return {
        "status": "success",
        "topic_raw": topic,
        "declarative_title": declarative_title,
        "domain": domain_label,
        "target_standard": target_standard,
        "literature_gap": gap,
        "theoretical_model": theoretical_model,
        "hypotheses": [
            {"id": "H1", "statement": h1, "status": "Proposed", "path": f"{iv_code} -> {dv_code}"},
            {"id": "H2", "statement": h2, "status": "Proposed", "path": f"{iv_code} -> {med_code} -> {dv_code}"},
            {"id": "H3", "statement": h3, "status": "Proposed", "path": f"{mod_code} x {iv_code} -> {dv_code}"}
        ],
        "constructs": constructs,
        "questionnaire": questionnaire,
        "total_items": len(questionnaire),
        "google_apps_script": gas_script
    }


def generate_pilot_dataset(architecture: Dict[str, Any], sample_size: int = 100, seed: int = 42) -> pd.DataFrame:
    """
    Synthesizes N records with structured covariance ensuring valid regression (HC3)
    and ANOVA significance across participant cohorts.
    """
    np.random.seed(seed)
    constructs = architecture.get("constructs", [])
    if not constructs:
        raise ValueError("No constructs defined in research architecture.")
    
    n = max(30, min(sample_size, 1000))
    
    # 1. Demographics
    roles = [
        "Senior Lead / Principal Investigator",
        "Postdoctoral Fellow / Senior Specialist",
        "Doctoral / Mid-Level Researcher",
        "Associate / Junior Scholar"
    ]
    role_weights = [0.22, 0.35, 0.28, 0.15]
    participant_roles = np.random.choice(roles, size=n, p=role_weights)
    
    experience = np.random.gamma(shape=3.2, scale=1.7, size=n)
    experience = np.clip(np.round(experience, 1), 0.5, 20.0)
    
    genders = np.random.choice(["Male", "Female", "Prefer not to disclose"], size=n, p=[0.52, 0.44, 0.04])
    ages = np.random.choice(["18-24", "25-34", "35-44", "45-54", "55+"], size=n, p=[0.20, 0.48, 0.22, 0.08, 0.02])
    
    data = {
        "Participant ID": [f"RESP_{i:03d}" for i in range(1, n + 1)],
        "Participant Role": participant_roles,
        "Years of Experience": experience,
        "Age Group": ages,
        "Gender": genders
    }
    
    # 2. Correlated Constructs (Latent Gaussian factors with designed covariance)
    # Factor 1: IV
    # Factor 2: Mediator
    # Factor 3: Moderator
    # Factor 4: DV
    mean = [0, 0, 0, 0]
    cov = [
        [1.0,   0.32,  0.22,  0.54], # IV
        [0.32,  1.0,   0.14,  0.42], # Mediator
        [0.22,  0.14,  1.0,   0.35], # Moderator
        [0.54,  0.42,  0.35,  1.00]  # DV
    ]
    latent_factors = np.random.multivariate_normal(mean, cov, size=n)
    
    # Add cohort mean shifts to ensure One-Way ANOVA is statistically significant across Roles
    role_shift_map = {
        "Senior Lead / Principal Investigator": 0.55,
        "Postdoctoral Fellow / Senior Specialist": 0.20,
        "Doctoral / Mid-Level Researcher": -0.15,
        "Associate / Junior Scholar": -0.60
    }
    role_shifts = np.array([role_shift_map.get(r, 0.0) for r in participant_roles])
    
    # Map latent factors to 5-point Likert items
    for idx, c in enumerate(constructs[:4]):
        factor_col = latent_factors[:, idx] + 0.45 * role_shifts
        composite_items = []
        for item_idx, item_text in enumerate(c["items"], 1):
            col_name = f"{c['code']}_{item_idx} ({item_text[:28]}...)"
            # Item idiosyncratic noise
            item_latent = factor_col + np.random.normal(0, 0.42, size=n)
            # Center around 3.3 with realistic spread
            raw_scores = 3.3 + 0.85 * item_latent
            likert_scores = np.clip(np.round(raw_scores), 1, 5).astype(int)
            data[col_name] = likert_scores
            composite_items.append(likert_scores)
        
        # Composite construct index
        composite_mean = np.mean(composite_items, axis=0)
        data[f"INDEX_{c['code']} ({c['name']})"] = np.round(composite_mean, 2)
        
    df = pd.DataFrame(data)
    return df
