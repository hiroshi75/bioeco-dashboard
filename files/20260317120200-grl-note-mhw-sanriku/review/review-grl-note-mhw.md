# Statistical Review Report: GRL Note "KE Meander MHW"
## Reviewer: Rev-C (Biostatistics)
## Date: 2026-03-16

---

## Statistical Methods Summary

| Method | Application | Appropriateness |
|---|---|---|
| Hobday et al. (2016) MHW detection | MHW identification & classification | Standard, appropriate |
| 30-year baseline climatology | Threshold calculation | Appropriate |
| GLS-AR1 (Cochrane-Orcutt) | SST component decomposition | Appropriate with caveats |
| z-score standardization | Residual extremity assessment | Appropriate |
| Return period estimation | Rarity of January 2024 event | Requires caution |

## Overall Statistical Assessment: Major Concerns

The GRL Note presents a clear physical oceanography analysis, but the SST component decomposition raises significant statistical concerns regarding overfitting, residual interpretation, and causal attribution.

---

## Major Statistical Issues

### M1. R² = 0.898 with seasonal dummies: overfitting risk
**Issue**: The M4 model achieves R² = 0.898 with 8 predictors (intercept, PDO, ONI, ONI_lag1, trend, 3 seasonal dummies) on n = 175 quarterly observations. The seasonal dummies alone likely explain most variance (SST has ~15°C annual cycle). The "explained" R² is dominated by seasonality, not by PDO/ONI/trend.
**Impact**: Claiming "climate modes explain 40% of the anomaly" is misleading when the model's high R² is largely from seasonal adjustment. The 40% figure comes from the decomposition of the 2023 July anomaly specifically, but readers may confuse model-level R² with anomaly attribution.
**Recommendation**:
(1) **Required**: Report R² with and without seasonal dummies. Report partial R² or ΔR² for PDO/ONI/trend block.
(2) **Required**: Use anomaly-based regression (SST − climatology ~ PDO + ONI + ONI_lag + trend) to remove the seasonality inflation of R².
(3) Compare the anomaly-based R² with the current full-model R².

### M2. Residual = KE meander proxy: attribution concern
**Issue**: The paper defines KE_index = regression residual, then attributes this to "Kuroshio Extension meander dynamics." However, the residual contains ALL unexplained variance: measurement error, other unmodeled climate modes (AMO is mentioned in data but not in the regression), mesoscale eddies, internal variability, model misspecification, etc.
**Impact**: Attributing 60% of the anomaly to "KE meander" is a strong causal claim based on a residual. This is the single biggest concern with the paper.
**Recommendation**:
(1) **Required**: Rename from "KE meander contribution" to "unexplained residual" or "non-climate-mode component" throughout.
(2) **Required**: Include AMO in the regression to reduce residual.
(3) **Required**: Provide independent evidence linking the residual to KE position (e.g., correlation with satellite altimetry KE latitude index).
(4) Without direct KE meander data in the regression, the "60% KE" claim should be softened to "up to 60% is not explained by PDO/ONI/trend."

### M3. Return period > 1,000 years from 43-year record
**Issue**: The January 2024 z = 3.99 is stated to have "an estimated return period exceeding 1,000 years under the 1982–2011 climate." Estimating 1,000-year return periods from 43 years of data requires extreme value theory (e.g., GEV/GPD), not simple z-score conversion.
**Impact**: z-score-based return periods assume Gaussianity, which is unlikely for residuals from a nonlinear ocean system.
**Recommendation**:
(1) Either apply formal EVT (fit GPD to exceedances) or remove the return period claim entirely.
(2) At minimum, test residual normality (Shapiro-Wilk, Q-Q plot) and report the result.

### M4. Trend not significant (p = 0.145) but climate change implied
**Issue**: The long-term warming trend is not significant in the quarterly regression (p = 0.145). The paper notes this might be a power issue (n = 175 quarterly). However, the narrative implies anthropogenic warming as a component of the MHW.
**Impact**: If the trend is not detectable, its contribution to the 40% "explained" fraction is uncertain.
**Recommendation**:
(1) Report the contribution of trend alone (separate from PDO/ONI) to the 2023 anomaly.
(2) The monthly regression (n = 515, Table S5) should be reported in main text if it resolves the trend significance.

---

## Minor Statistical Issues

### m1. Cochrane-Orcutt AR(1) ρ = −0.294: negative autocorrelation
**Issue**: Negative AR(1) in quarterly SST residuals is unusual and may indicate model misspecification (e.g., over-differencing via seasonal dummies, or aliased higher-frequency processes).
**Recommendation**: Report Durbin-Watson statistic. Consider whether quarterly aggregation creates artifactual negative autocorrelation. Test AR(2) and compare AIC.

### m2. Single grid point (40°N, 144°E)
**Issue**: All main results are from a single 0.25° grid point. Spatial averaging (38-42°N, 141-147°E) is mentioned for "sensitivity analysis" but results are not shown.
**Recommendation**: Report the spatial-average results in Supporting Information at minimum. A single grid point is vulnerable to local SST artifacts.

### m3. "Observed only twice since 1950" — sample size for regime rarity
**Issue**: The claim that the negative-PDO + El Niño regime was "observed only twice since 1950" (1972 and 2023) is descriptive, not statistical. No formal test of regime rarity is provided.
**Recommendation**: This is acceptable as a descriptive statement. Consider adding a joint probability estimate (P(PDO < −1) × P(ONI > 0.5) under independence, then note observed frequency for comparison).

### m4. Hobday baseline: 30-year vs 21-year comparison
**Issue**: "Exceedance rates changed by <1 percentage point when extending from 21 to 30 years" — this is reassuring but the test is weak. The difference between 21- and 30-year baselines may be negligible when both include recent warming.
**Recommendation**: Report the exact exceedance rates for both baselines in Table S1. Consider a detrended baseline as additional sensitivity test.

### m5. No confidence intervals on decomposition fractions
**Issue**: The "40% explained / 60% unexplained" decomposition has no uncertainty bounds.
**Recommendation**: Use bootstrap (resample quarters, re-run regression, re-compute decomposition) to provide 95% CI on the explained fraction.

---

## Reproducibility Assessment

**Strengths**:
- NOAA OISST v2.1 is public and well-documented
- Climate indices publicly available
- Analysis code exists (Rin's workspace)
- Hobday detection framework is standardized

**Concerns**:
- Code not yet deposited publicly
- Single-point analysis limits independent replication to that exact coordinate
- Cochrane-Orcutt implementation is custom (not statsmodels) — potential implementation bugs

**Recommendation**: Validate Cochrane-Orcutt results against statsmodels.GLS or R's nlme::gls. Pin Python versions.

---

## Recommendations

1. **Required**: Rename "KE meander contribution" to "unexplained residual" or provide independent KE position data
2. **Required**: Report R² without seasonal dummies; or use anomaly-based regression
3. **Required**: Remove or properly justify the 1,000-year return period claim (use EVT or delete)
4. **Strongly recommended**: Include AMO in the regression
5. **Strongly recommended**: Bootstrap CI on decomposition fractions
6. **Recommended**: Report spatial-average sensitivity results
7. **Recommended**: Investigate negative AR(1) coefficient
