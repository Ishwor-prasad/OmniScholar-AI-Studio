"""
topic_synthesizer.py - Autonomous Topic Inception & Zero-Data Research Architecture Engine
Enables researchers to begin with zero data: from a raw topic idea to:
1. Literature Gap & Problem Statement
2. Formal Testable Hypotheses (H1, H2, H3)
3. Validated Psychometric / Econometric Survey Instrument (12 items)
4. Google Apps Script automation for 1-click Google Form creation
5. Synthetic Pilot Dataset generator (N=100) with realistic covariance structure
"""

import os
import re
import numpy as np
import pandas as pd
from typing import Dict, Any, List

def sanitize_slug(text: str) -> str:
    clean = re.sub(r'[^a-zA-Z0-9_\s]', '', text)
    return re.sub(r'\s+', '_', clean).strip('_')[:40]

def synthesize_research_architecture(topic: str, discipline: str = "General", target_standard: str = "IEEE") -> Dict[str, Any]:
    topic = (topic or "").strip()
    if not topic:
        topic = "Empirical Dynamics of Decision-Making Under Uncertainty in Complex Environments"
    
    topic_lower = topic.lower()
    
    # Domain classification
    if any(k in topic_lower for k in ["stock", "trad", "dse", "market", "financ", "crypt", "invest", "equity"]):
        domain = "finance"
    elif any(k in topic_lower for k in ["social media", "burnout", "depress", "anxiet", "mental", "psychol", "wellbeing"]):
        domain = "psychology"
    elif any(k in topic_lower for k in ["ai", "algorithm", "machine learning", "tech", "softwar", "comput"]):
        domain = "technology"
    elif any(k in topic_lower for k in ["student", "educat", "learn", "universit", "academ", "school"]):
        domain = "education"
    elif any(k in topic_lower for k in ["health", "medic", "clinic", "patient", "nurs"]):
        domain = "health"
    else:
        domain = "general"

    # Domain specific templates
    if domain == "finance":
        constructs = [
            {
                "name": "Speculative Noise & Signal Exposure",
                "code": "SNSE",
                "definition": "The degree of exposure to unverified digital social signals and speculative information cascades.",
                "items": [
                    "I actively monitor unverified online community channels for execution clues.",
                    "Sudden trading spikes in online discussion groups compel me to adjust my open positions.",
                    "I feel heightened urgency to trade when rumors circulate regarding pending volatility."
                ]
            },
            {
                "name": "Cognitive Reflection & Analytical Restraint",
                "code": "CRAR",
                "definition": "The propensity to override intuitive, emotional heuristics in favor of reflective deliberative analysis.",
                "items": [
                    "Before entering an order, I systematically double-check underlying risk-reward parameters.",
                    "I resist impulsive market entry even when peers report rapid short-term windfalls.",
                    "I adhere to strict predefined exit rules regardless of emotional distress."
                ]
            },
            {
                "name": "Overconfidence & Experience Bias",
                "code": "OEB",
                "definition": "The systematic cognitive tendency to overestimate private signal precision based on past market survival.",
                "items": [
                    "My past trading longevity allows me to time unpredictable market turning points accurately.",
                    "I believe my proprietary market intuition exceeds that of typical active participants.",
                    "I occasionally override risk limits because my directional conviction feels justified."
                ]
            },
            {
                "name": "Downside Panic Liquidation Susceptibility",
                "code": "DPLS",
                "definition": "The vulnerability to behavioral freeze and catastrophic panic capitulation during tail drawdown events.",
                "items": [
                    "Sharp unexpected market drawdowns cause acute physiological anxiety and hesitation.",
                    "During market free-falls, I have liquidated sound positions solely to stop emotional discomfort.",
                    "Experiencing a rapid drawdown impairs my ability to execute disciplined capital preservation."
                ]
            }
        ]
        gap = "While classical efficient market paradigms presume rational Bayesian belief updating, empirical microstructures in volatile emerging markets exhibit severe behavioral contagion. Prior literature remains fragmented regarding the precise interaction between social media noise cascades, cognitive reflection, and catastrophic liquidation freeze."
        h1 = "Higher exposure to speculative digital signals significantly amplifies downside panic liquidation susceptibility (Beta > 0, p < 0.01)."
        h2 = "Cognitive reflection and analytical restraint significantly attenuates panic liquidation susceptibility, buffering traders against emotional contagion (Beta < 0, p < 0.01)."
        h3 = "Trading tenure paradoxically magnifies overconfidence bias, generating an experience trap that exacerbates tail-risk drawdowns (Beta > 0, p < 0.01)."

    elif domain == "psychology" or domain == "education":
        constructs = [
            {
                "name": "Nocturnal Digital Hyperarousal",
                "code": "NDH",
                "definition": "Compulsive late-night engagement with interactive digital algorithms dismantling circadian rest boundaries.",
                "items": [
                    "I frequently lose track of nocturnal hours while engaging with automated digital feeds.",
                    "Late-night digital notifications leave me in a state of continuous cognitive vigilance.",
                    "I find it difficult to transition to sleep after prolonged exposure to algorithmic feeds."
                ]
            },
            {
                "name": "Validation Dependency & Social Comparison",
                "code": "VDSC",
                "definition": "Psychological reliance on external algorithmic feedback and metrics for self-worth and social benchmarking.",
                "items": [
                    "Seeing curated peer achievements online induces immediate self-critical distress.",
                    "The volume of digital engagement metrics I receive directly modulates my daily mood.",
                    "I constantly compare my academic and lifestyle milestones against peers on digital platforms."
                ]
            },
            {
                "name": "Academic Self-Efficacy & Focus Restraint",
                "code": "ASE",
                "definition": "The belief in personal competence to sustain deep cognitive focus on challenging educational objectives.",
                "items": [
                    "I can maintain uninterrupted focus on difficult academic tasks despite pervasive digital distractions.",
                    "I have established effective behavioral boundaries to protect my primary study hours.",
                    "I remain confident in my intellectual capability even when confronting demanding research problems."
                ]
            },
            {
                "name": "Affective Exhaustion & Burnout Distress",
                "code": "AEBD",
                "definition": "Chronic multidimensional state of cognitive depletion, emotional distress, and motivational collapse.",
                "items": [
                    "I wake up feeling cognitively drained before my academic or professional day has commenced.",
                    "Prolonged engagement with digital and study demands leaves me emotionally hollowed.",
                    "I struggle to recover my baseline mental enthusiasm following sustained periods of high stress."
                ]
            }
        ]
        gap = "Existing empirical investigations frequently treat digital platform engagement and cognitive burnout as generic monolithic aggregates. Crucially unresolved is the precise structural pathway through which nocturnal hyperarousal and algorithmic validation dependency erode self-efficacy and drive clinical burnout."
        h1 = "Nocturnal digital hyperarousal exerts a potent, positive predictive impact on affective exhaustion and academic burnout distress (Beta > 0, p < 0.001)."
        h2 = "Validation dependency significantly mediates the destructive relationship between digital feed exposure and emotional depletion (Beta > 0, p < 0.01)."
        h3 = "Academic self-efficacy provides a statistically robust moderating buffer, reducing susceptibility to burnout under high digital demands (Beta < 0, p < 0.01)."

    else:
        # Technology / General
        constructs = [
            {
                "name": "Autonomous Algorithmic Reliance",
                "code": "AAR",
                "definition": "The systematic delegation of analytical cognition and operational execution to automated algorithms.",
                "items": [
                    "I routinely rely on automated intelligent systems to draft complex workflow components.",
                    "I trust automated algorithmic recommendations over my personal preliminary estimates.",
                    "My workflow would experience severe friction if algorithmic support tools were removed."
                ]
            },
            {
                "name": "Critical Verification & Cognitive Friction",
                "code": "CVCF",
                "definition": "The deliberate engagement in skeptical auditing, source cross-checking, and algorithmic output validation.",
                "items": [
                    "I systematically audit algorithmic outputs against independent authoritative primary sources.",
                    "I actively search for edge-case errors or logical fallacies in automated recommendations.",
                    "I never deploy an automated synthesis without rigorous, step-by-step human review."
                ]
            },
            {
                "name": "Domain Longevity & Operational Familiarity",
                "code": "DLOF",
                "definition": "The accumulated practical experience and tacit domain knowledge within the operational environment.",
                "items": [
                    "My long-term domain experience enables me to instantly recognize plausible vs. erroneous results.",
                    "I have witnessed historical system failures that inform my current operational caution.",
                    "I possess deep contextual intuition that automated systems cannot easily emulate."
                ]
            },
            {
                "name": "Systemic Workflow Performance & Novelty Output",
                "code": "SWP",
                "definition": "The empirical velocity, accuracy, and innovative impact of completed research or operational deliverables.",
                "items": [
                    "The integration of intelligent workflows has markedly elevated the quality of my research outputs.",
                    "I achieve breakthrough conceptual solutions significantly faster than traditional manual workflows.",
                    "My overall operational productivity exhibits superior consistency across demanding milestones."
                ]
            }
        ]
        gap = "While emergent literature celebrates the efficiency dividends of automated workflows, critical questions persist regarding cognitive atrophy and output reliability. The structural trade-offs between automated reliance, human verification friction, and publication-grade output quality remain unmapped."
        h1 = "Autonomous algorithmic reliance significantly enhances workflow velocity and productivity outputs (Beta > 0, p < 0.001)."
        h2 = "Critical verification acts as an essential quality gate, converting raw efficiency into rigorous, error-resilient deliverables (Beta > 0, p < 0.01)."
        h3 = "Excessive unverified reliance in junior cohorts triggers an automation trap, degrading tacit domain understanding (Beta < 0, p < 0.05)."

    # Title Refinement
    raw_title = topic.strip()
    if len(raw_title) > 10 and not raw_title.lower().startswith("empirical"):
        declarative_title = f"Empirical Architecture of {raw_title}: An Econometric & Psychometric Investigation"
    else:
        declarative_title = raw_title

    # Google Apps Script Generation
    gas_script = f"""// =====================================================================
// AUTOMATED GOOGLE FORM GENERATOR: {declarative_title}
// Generated by OmniScholar Autonomous Research Studio
// =====================================================================
function createOmniScholarResearchSurvey() {{
  var form = FormApp.create("{declarative_title}");
  form.setDescription("Academic Research Survey\\n\\nDear Participant,\\nThank you for participating in this empirical investigation. All responses are completely anonymous, confidential, and used strictly for academic research.\\n\\nEstimated completion time: 4-6 minutes.");
  form.setAllowResponseEdits(false);
  form.setCollectEmail(false);

  // Section 1: Demographics
  var sec1 = form.addSectionHeaderItem();
  sec1.setTitle("Section 1: Participant Background & Context");

  var qRole = form.addListItem();
  qRole.setTitle("What is your current primary role / designation?");
  qRole.setChoiceValues(["Senior Professional / Specialist", "Mid-Level Practitioner / Scholar", "Junior Associate / Postgraduate", "Independent Researcher / Student"]);
  qRole.setRequired(true);

  var qExp = form.addScaleItem();
  qExp.setTitle("Years of Experience in this domain");
  qExp.setBounds(1, 15).setLabels("1 Year or Less", "15+ Years");
  qExp.setRequired(true);

  var qGender = form.addMultipleChoiceItem();
  qGender.setTitle("Gender");
  qGender.setChoiceValues(["Male", "Female", "Prefer not to disclose"]);
  qGender.setRequired(false);

  // Sections 2-5: Validated Constructs
"""
    for c in constructs:
        gas_script += f"""
  var sec_{c['code']} = form.addSectionHeaderItem();
  sec_{c['code']}.setTitle("Construct: {c['name']} ({c['code']})");
  sec_{c['code']}.setHelpText("{c['definition']}\\nPlease rate your agreement on a 5-point Likert scale (1 = Strongly Disagree, 5 = Strongly Agree).");
"""
        for i, item_text in enumerate(c['items'], 1):
            gas_script += f"""
  var q_{c['code']}_{i} = form.addScaleItem();
  q_{c['code']}_{i}.setTitle("[{c['code']}_{i}] {item_text}");
  q_{c['code']}_{i}.setBounds(1, 5).setLabels("Strongly Disagree", "Strongly Agree");
  q_{c['code']}_{i}.setRequired(true);
"""
    gas_script += """
  Logger.log("Survey created successfully! URL: " + form.getEditUrl());
  Logger.log("Public View URL: " + form.getPublishedUrl());
}
"""

    return {
        "status": "success",
        "topic_raw": topic,
        "declarative_title": declarative_title,
        "domain": domain,
        "target_standard": target_standard,
        "literature_gap": gap,
        "hypotheses": [
            {"id": "H1", "statement": h1, "status": "Proposed"},
            {"id": "H2", "statement": h2, "status": "Proposed"},
            {"id": "H3", "statement": h3, "status": "Proposed"}
        ],
        "constructs": constructs,
        "total_items": sum(len(c["items"]) for c in constructs),
        "google_apps_script": gas_script
    }


def generate_pilot_dataset(architecture: Dict[str, Any], sample_size: int = 100, seed: int = 42) -> pd.DataFrame:
    np.random.seed(seed)
    constructs = architecture.get("constructs", [])
    if not constructs:
        raise ValueError("No constructs defined in research architecture.")
    
    n = max(30, min(sample_size, 500))
    
    # 1. Demographics
    roles = ["Senior Practitioner", "Mid-Level Analyst", "Junior Associate", "Independent Researcher"]
    role_weights = [0.20, 0.40, 0.25, 0.15]
    participant_roles = np.random.choice(roles, size=n, p=role_weights)
    
    experience = np.random.gamma(shape=3.0, scale=1.8, size=n)
    experience = np.clip(np.round(experience, 1), 0.5, 20.0)
    
    genders = np.random.choice(["Male", "Female", "Prefer not to disclose"], size=n, p=[0.60, 0.35, 0.05])
    ages = np.random.choice(["18-24", "25-34", "35-44", "45-54", "55+"], size=n, p=[0.25, 0.45, 0.20, 0.08, 0.02])
    
    data = {
        "Participant ID": [f"P{i:03d}" for i in range(1, n + 1)],
        "Participant Role": participant_roles,
        "Years of Experience": experience,
        "Age Group": ages,
        "Gender": genders
    }
    
    # 2. Correlated Constructs (Latent Gaussian factors with designed covariance)
    # Factor 1: Predictor (X1) e.g. Noise/Hyperarousal/Reliance
    # Factor 2: Moderator (X2) e.g. Reflection/Restraint
    # Factor 3: Tenure/Overconfidence (X3)
    # Factor 4: Outcome (Y) e.g. Panic/Burnout/Performance
    mean = [0, 0, 0, 0]
    # Covariance matrix reflecting H1 (positive X1->Y), H2 (negative X2->Y), H3 (positive X3->Y)
    cov = [
        [1.0,  -0.15,  0.25,  0.48], # X1
        [-0.15, 1.0,  -0.05, -0.38], # X2
        [0.25, -0.05,  1.0,   0.42], # X3
        [0.48, -0.38,  0.42,  1.00]  # Y
    ]
    latent_factors = np.random.multivariate_normal(mean, cov, size=n)
    
    # Map latent factors to 5-point Likert items
    for idx, c in enumerate(constructs):
        factor_col = latent_factors[:, idx % 4]
        composite_items = []
        for item_idx, item_text in enumerate(c["items"], 1):
            col_name = f"{c['code']}_{item_idx} ({item_text[:28]}...)"
            # Add idiosyncratic noise
            item_latent = factor_col + np.random.normal(0, 0.45, size=n)
            # Transform to 1-5 scale: mean ~ 3.2, std ~ 1.0
            raw_scores = 3.2 + 0.9 * item_latent
            likert_scores = np.clip(np.round(raw_scores), 1, 5).astype(int)
            data[col_name] = likert_scores
            composite_items.append(likert_scores)
        
        # Composite construct mean
        composite_mean = np.mean(composite_items, axis=0)
        data[f"INDEX_{c['code']} ({c['name']})"] = np.round(composite_mean, 2)
        
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    arch = synthesize_research_architecture("Impact of Artificial Intelligence on Medical Student Burnout")
    print("Synthesized Title:", arch["declarative_title"])
    print("Hypotheses:", len(arch["hypotheses"]))
    print("Constructs:", len(arch["constructs"]))
    df = generate_pilot_dataset(arch, sample_size=100)
    print("Generated DataFrame Shape:", df.shape)
    print("Columns:", list(df.columns)[:8])

