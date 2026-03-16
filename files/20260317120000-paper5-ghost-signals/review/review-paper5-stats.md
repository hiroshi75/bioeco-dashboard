# Statistical Review Report: Paper 5 "Ghost Signals"
## Reviewer: Rev-C (Biostatistics)
## Date: 2026-03-16

---

## Statistical Methods Summary

| Method | Application | Appropriateness |
|---|---|---|
| GLS-AR1 (Cochrane-Orcutt) | Phenological trend estimation | Appropriate |
| One-sample t-test | Mean slope ≠ 0 across stations | Appropriate |
| Two-sample t-test | Urban/rural, SoJ/Pacific comparisons | Appropriate |
| Fisher's exact test | Animal vs plant delay proportions | Appropriate |
| Binomial test | 0/10 animals advanced | Appropriate |
| Pearson/Spearman correlation | Latitudinal gradient, farmland abandonment | Appropriate |
| Multivariate OLS | Combined alternative hypothesis test | Appropriate (added in v4) |

## Overall Statistical Assessment: Minor Concerns

The statistical framework is generally sound. GLS-AR1 is an appropriate choice for autocorrelated time series, and the Cochrane-Orcutt procedure is a standard estimator. The systematic approach to alternative hypothesis testing is commendable. However, several issues require attention.

---

## Major Statistical Issues

### M1. GLS-AR1 vs more flexible time-series models
**Issue**: GLS-AR1 assumes a linear trend and first-order autocorrelation. For 67-year ecological time series, this may be overly restrictive. Population declines are unlikely to be linear—they may show acceleration, threshold effects, or regime shifts.
**Impact**: If the true trend is nonlinear (e.g., steeper decline post-1990), the linear slope (+5.3 days/decade) understates recent rates and overstates early rates.
**Recommendation**: (1) Fit GAM with penalized spline to assess nonlinearity. (2) Compare AIC/BIC of GLS-AR1 vs ARIMA(p,d,q) vs GAM. (3) At minimum, report whether residuals from GLS-AR1 show remaining temporal structure (e.g., Ljung-Box test).

### M2. OLS vs GLS discrepancy reporting
**Issue**: The methods state "9 of 33 species showed significant trends under GLS (compared to 10 under OLS)" but the specific species that gained/lost significance are not clearly identified in the main text. Three species lost significance, two gained — the net change masks composition.
**Impact**: Readers cannot assess whether OLS-to-GLS transitions affect the core narrative.
**Recommendation**: Add a column to Table S1 flagging species where OLS→GLS changed significance. Discuss whether any delayed animal species lost significance under GLS.

### M3. Independent validation uses different species
**Issue**: The paper validates tree frog (*Dryophytes japonicus*) phenological delays using brown frog (*Rana japonica/R. ornativentris*) population data. These are different families (Hylidae vs Ranidae).
**Impact**: The "independent validation" is at the order level (Anura), not species level. The authors acknowledge this (Section 2.5), but the abstract and conclusions overstate the validation strength.
**Recommendation**: (1) Soften language from "confirm" to "corroborate" in abstract. (2) Explicitly state the taxonomic gap in Discussion limitations. (3) If any *Dryophytes* abundance data exist (even anecdotal), cite them.

### M4. Frog decline not significant (p = 0.094)
**Issue**: The Japanese brown frog decline (−58% decade⁻¹, p = 0.094) is presented alongside the significant firefly decline as if both support the hypothesis equally.
**Impact**: At n = 28 sites, this is a power issue, but the p-value is still above α = 0.05. The narrative should be more cautious.
**Recommendation**: (1) Report a power analysis: what sample size would be needed to detect a 58% decline at 80% power? (2) Consider presenting the frog result as a separate, suggestive finding rather than a confirmation.

---

## Minor Statistical Issues

### m1. Latitudinal gradient: n = 4 at high latitudes
**Issue**: The latitudinal gradient (ρ = 0.49, p = 0.001) is driven partly by Hokkaido stations (n = 4, 100% delayed). With only 4 stations above 41°N, the apparent gradient could be heavily influenced by these few points.
**Recommendation**: (1) Report the correlation excluding Hokkaido (n = 37). (2) Use a leverage diagnostic (Cook's distance) to assess influence of extreme-latitude stations.

### m2. Fisher's exact test underpowered
**Issue**: The Fisher's test (p = 0.37) comparing animal vs plant delay proportions has very low power with n = 10 + 23. The paper appropriately notes this, but the binomial test (p = 0.001) is a stronger argument and should be foregrounded.
**Recommendation**: Lead with the binomial test result in the Results section; present the Fisher test as supplementary.

### m3. Multiple testing across 6 alternative hypotheses
**Issue**: The authors argue that no family-wise correction is needed because each hypothesis addresses a "distinct scientific question" (citing Rothman 1990). While this is defensible, the Rothman argument is controversial. The BH-corrected Table S3 is a good safeguard.
**Recommendation**: The current approach (report uncorrected in main text, BH in supplement) is acceptable. Consider noting in the methods that with 6 tests at α = 0.05, the probability of ≥1 false positive under complete null is 1 − 0.95⁶ = 0.26.

### m4. Effect size reporting incomplete
**Issue**: Cohen's d or equivalent effect sizes are not reported for the t-tests (urban/rural, SoJ/Pacific). Only p-values are given.
**Recommendation**: Add effect sizes (Cohen's d with 95% CI) for all group comparisons, following current reporting standards.

### m5. "Table S1: 1,341 station-species combinations"
**Issue**: The supplement mentions 1,341 combinations but the main text analyzes only 33 species. The relationship between these numbers should be clarified (multiple stations per species).
**Recommendation**: State clearly in methods: "33 species × [mean N] stations = 1,341 station-species combinations."

### m6. Annual-aggregate vs station-level mean discrepancy
**Issue**: Fig. 2 note mentions +3.1 days/decade (annual aggregate) vs +5.3 (station-level mean). This discrepancy needs explanation.
**Recommendation**: Explain that station composition changes over time create a Simpson's paradox-like effect. Justify why station-level mean is preferred.

---

## Reproducibility Assessment

**Strengths**:
- All analysis in Python (scipy, statsmodels, numpy)
- Random seed recorded (42)
- Public JMA data source cited
- Code promised for public repository upon acceptance

**Concerns**:
- Ueta et al. (2025) data DOI is TBD — data accessibility not yet guaranteed
- No specific version pinning for Python packages
- No containerization (Docker) mentioned

**Recommendation**: Pin Python package versions in requirements.txt. Ensure Ueta data deposit is completed before submission.

---

## Recommendations

1. **Required**: Report nonlinearity assessment (GAM or similar) alongside GLS-AR1
2. **Required**: Soften "independent validation" language given taxonomic mismatch
3. **Required**: Add power analysis for the non-significant frog decline
4. **Strongly recommended**: Report effect sizes for all group comparisons
5. **Recommended**: Assess latitudinal gradient robustness (exclude Hokkaido sensitivity test)
6. **Recommended**: Explain annual-aggregate vs station-level slope discrepancy in methods
