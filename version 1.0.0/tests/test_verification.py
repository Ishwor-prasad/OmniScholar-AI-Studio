import os
import sys
import json
import hashlib
import zipfile
import subprocess
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.multicomp import pairwise_tukeyhsd

class _SMCompat:
    OLS = OLS
    add_constant = staticmethod(add_constant)

sm = _SMCompat()

print("=" * 70)
print("  OmniScholar Independent Swarm Quality Verification Suite")
print("=" * 70)

APP_DIR = Path(__file__).resolve().parent.parent / "app"
CSV_PATH = APP_DIR / "dummy_data.csv"

def compute_cronbach_alpha(items_df: pd.DataFrame) -> float:
    # Drop rows with NaN
    df_clean = items_df.dropna()
    k = df_clean.shape[1]
    if k < 2:
        return 0.0
    item_variances = df_clean.var(axis=0, ddof=1).sum()
    total_variance = df_clean.sum(axis=1).var(ddof=1)
    if total_variance == 0:
        return 0.0
    alpha = (k / (k - 1)) * (1.0 - (item_variances / total_variance))
    return float(alpha)

def run_ground_truth_stats():
    print("\n[STEP 1] Computing Ground Truth Statistical Diagnostics on dummy_data.csv...")
    assert CSV_PATH.exists(), f"Sample data missing: {CSV_PATH}"
    df = pd.read_csv(CSV_PATH)
    print(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    print(f"Numeric columns ({len(numeric_cols)}): {numeric_cols}")
    
    # Check Cronbach's alpha on numeric columns
    alpha = compute_cronbach_alpha(df[numeric_cols])
    print(f"Reference Cronbach's alpha: {alpha:.4f}")
    
    # Check Pearson & Spearman correlation matrices
    pearson_corr = df[numeric_cols].corr(method='pearson')
    spearman_corr = df[numeric_cols].corr(method='spearman')
    print("Computed reference Pearson & Spearman matrices.")
    
    # Pick a categorical grouping column: e.g. "Primary Methodological Framework" or "Participant Role"
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    print(f"Categorical columns: {cat_cols}")
    group_col = "Primary Methodological Framework"
    target_num = numeric_cols[0]
    
    # Ground truth ANOVA & Kruskal
    groups = [group[target_num].dropna().values for _, group in df.groupby(group_col)]
    f_stat, p_val_anova = stats.f_oneway(*groups)
    k_stat, p_val_kruskal = stats.kruskal(*groups)
    
    # Degrees of freedom for ANOVA
    k_groups = len(groups)
    n_total = sum(len(g) for g in groups)
    df_between = k_groups - 1
    df_within = n_total - k_groups
    
    # Eta squared
    ss_total = np.sum((df[target_num] - df[target_num].mean())**2)
    grand_mean = df[target_num].mean()
    ss_between = sum(len(g) * (np.mean(g) - grand_mean)**2 for g in groups)
    eta_squared = ss_between / ss_total if ss_total > 0 else 0.0
    
    print(f"ANOVA Reference for '{target_num}' grouped by '{group_col}':")
    print(f"  F({df_between}, {df_within}) = {f_stat:.4f}, p = {p_val_anova:.6f}, eta^2 = {eta_squared:.4f}")
    print(f"Kruskal-Wallis Reference: H = {k_stat:.4f}, p = {p_val_kruskal:.6f}")
    
    # Tukey HSD
    clean_sub = df[[group_col, target_num]].dropna()
    tukey = pairwise_tukeyhsd(clean_sub[target_num], clean_sub[group_col])
    print(f"Tukey HSD computed: {len(tukey.summary().data) - 1} pairwise comparisons.")
    
    return {
        "df": df,
        "alpha": alpha,
        "f_stat": f_stat,
        "p_val_anova": p_val_anova,
        "df_between": df_between,
        "df_within": df_within,
        "eta_squared": eta_squared,
        "k_stat": k_stat,
        "p_val_kruskal": p_val_kruskal,
        "numeric_cols": numeric_cols
    }

if __name__ == "__main__":
    gt = run_ground_truth_stats()
    print("\nGround truth baseline calculated successfully.")

