# Statistical Review Report: Paper 1 "Apparent Stability"
## Reviewer: Rev-C (Biostatistics)
## Date: 2026-03-16

---

## Statistical Methods Summary

| Method | Application | Appropriateness |
|---|---|---|
| Kruskal-Wallis | 40 richness × driver tests | Appropriate (non-parametric) |
| Benjamini-Hochberg FDR | 93 global tests | Appropriate |
| Paired t-test | Native vs nonnative slopes | Appropriate |
| One-sample t-test | Nonnative ratio trend | Appropriate |
| Cohen's d + 95% CI | Effect sizes throughout | Good practice |
| PSM (nearest-neighbor) | CTI confound control | Appropriate with caveats |
| Segmented regression | Breakpoint detection | Appropriate |
| F-test | Segmented vs linear model | Appropriate |
| DiD | CTI temporal change | Appropriate |
| Sobel test | Mediation analysis | Outdated but acceptable |

## Overall Statistical Assessment: Minor Concerns

Paper 1 is the most statistically rigorous of the three, with exemplary transparency (all 93 tests listed, BH correction applied globally). The discovery of CTI confounding by baseline temperature and subsequent PSM correction demonstrates methodological sophistication. However, several issues need attention.

---

## Major Statistical Issues

### M1. Cold tertile CTI (d = 1.38): post-hoc subgroup with n = 3 abandoned sites
**Issue**: The cold-tertile CTI finding (d = 1.38, BH-adjusted p = 0.0055) is the paper's most striking result, but it is explicitly post-hoc (discovered only after the overall CTI was nullified by PSM). With only n = 3 abandoned sites in the cold tertile, the effect size is unstable and the 95% CI spans nearly 3 units [-0.034, 2.704].
**Impact**: This is a classic "garden of forking paths" concern. The CI nearly includes zero. With n = 3, a single outlier site could drive the entire effect.
**Recommendation**:
(1) **Required**: Run a leave-one-out sensitivity: report d for each combination of 2/3 abandoned cold sites.
(2) **Required**: Label this finding explicitly as "hypothesis-generating, requiring independent replication" in both Discussion and Conclusions.
(3) Consider whether the d = 1.38 should appear in the abstract at all, given the extreme sample size limitation.

### M2. PSM caliper and matching quality
**Issue**: PSM with caliper = 1.0°C and nearest-neighbor matching produced 24 pairs from 27+36 sites. Post-matching balance (p = 0.562) is adequate, but:
- No matching on other covariates (latitude, elevation, region)
- Latitude-temperature collinearity (r = -0.863) means matching on temperature implicitly partially matches on latitude
- No sensitivity analysis (e.g., Rosenbaum bounds) for unmeasured confounding
**Impact**: The PSM-nullified CTI (d = 0.176, p = 0.407) is a key result. Its robustness to specification should be demonstrated.
**Recommendation**: (1) Report Rosenbaum sensitivity analysis (Γ). (2) Try alternative matching methods (optimal matching, CEM) as robustness check. (3) Report balance on ALL covariates, not just temperature.

### M3. Breakpoint interpretation: climate-driven, not abandonment-driven
**Issue**: All 8 breakpoint tests are significant (BH-corrected), but the discrimination test shows non-abandoned sites also have breakpoints (F = 17.9, p = 0.0002). The paper correctly concludes this is climate-driven (PDO shift), but this finding weakens the paper's central thesis about abandonment effects.
**Impact**: If breakpoints are climate-driven, the paper's narrative should not imply they are relevant to the "apparent stability" story about abandonment.
**Recommendation**: Clarify in Discussion that breakpoints support climate forcing on ALL sites, independent of abandonment. Consider whether this section belongs in the main text or supplementary.

### M4. Simpson's paradox in CTI: underexplored
**Issue**: The Discussion (4.5) notes a Simpson's paradox: cold tertile d = 1.38 coexists with overall d = 0.176. This is indeed a textbook case, but the paper doesn't fully explore it.
**Impact**: The paradox could also mean the subgroup effect is an artifact of the grouping scheme.
**Recommendation**: (1) Test at least 2 alternative cutpoints (quartiles, median split). (2) Report continuous interaction: CTI_change ~ abandonment × baseline_temperature. (3) If the interaction is not significant (the H4rev3 result shows p = 0.90), this weakens the cold-tertile narrative considerably.

---

## Minor Statistical Issues

### m1. 93 tests: BH is appropriate but aggressive
**Issue**: BH controls FDR at 0.05, meaning up to 5% of "significant" results may be false positives. With ~20 significant results out of 93, this means ~1 false positive expected. This is acceptable but should be stated.
**Recommendation**: Report the expected number of false positives: q × m₁ (where m₁ is the number of rejected hypotheses).

### m2. HARKing transparency is commendable but incomplete
**Issue**: The 93-test audit classifies tests as "事前", "探索的", "事後的", "確認的". This is excellent practice. However, the paper draft doesn't fully distinguish these categories in the main text.
**Recommendation**: In the manuscript, use explicit labels: "pre-specified", "exploratory", "post-hoc" for each result.

### m3. Biotic homogenization: strong result but single-taxon
**Issue**: The nonnative ratio increase (d = 0.419, BH p < 0.001) is the paper's strongest finding, but it applies only to plants. The multi-taxon homogenization tests for birds, butterflies, frogs, and fireflies were all non-significant.
**Recommendation**: Emphasize that homogenization is plant-specific in current data. The title "multi-taxon" may overstate findings if homogenization is single-taxon.

### m4. TRIM slopes for species richness
**Issue**: TRIM (TRends and Indices for Monitoring data) slopes are mentioned but the TRIM methodology (Pannekoek & van Strien) is not described. TRIM handles missing data via Poisson regression — is this what was actually used, or were simpler linear slopes calculated?
**Recommendation**: Specify the exact trend estimation method in Methods 2.2.

### m5. Sobel test for mediation is outdated
**Issue**: Sobel test (z = 0.985, p = 0.324) assumes normality of the indirect effect, which is often violated. Bootstrap-based mediation (e.g., Hayes PROCESS) is now standard.
**Recommendation**: Replace Sobel with bootstrap CI (5000 iterations) for the mediation effect.

### m6. Baselga decomposition: statistical details missing
**Issue**: The Discussion mentions "turnover >> nestedness" and "25% species replacement" but no statistical test for turnover/nestedness partitioning significance is reported.
**Recommendation**: Report beta.SOR, beta.SIM, beta.SNE values with standard errors or permutation tests.

---

## Reproducibility Assessment

**Strengths**:
- Complete 93-test audit with raw and BH-corrected p-values
- Public data sources (Katayama figshare, Ueta figshare)
- EltonTraits matching documented (47/47, 11 synonyms)
- Random seed = 42

**Concerns**:
- Analysis scripts in Ken's workspace but not yet deposited
- PSM implementation details (package, exact algorithm) not specified
- No Docker/environment specification

---

## Recommendations

1. **Required**: Leave-one-out sensitivity for cold-tertile CTI (n = 3)
2. **Required**: Report continuous abandonment × temperature interaction alongside tertile analysis
3. **Required**: Label pre-specified vs exploratory vs post-hoc analyses in manuscript
4. **Strongly recommended**: Rosenbaum sensitivity analysis for PSM
5. **Strongly recommended**: Replace Sobel with bootstrap mediation
6. **Recommended**: Report Baselga decomposition statistical details
7. **Recommended**: Clarify TRIM methodology
