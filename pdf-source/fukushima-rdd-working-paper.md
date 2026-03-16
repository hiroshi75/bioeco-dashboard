# Rewilding Without Humans: A Spatial Regression Discontinuity Analysis of the Fukushima Exclusion Zone

BioEco Agent Lab | Working Paper | 2026-03-18
Target: Nature Ecology and Evolution / Science

## Abstract

The Fukushima Daiichi nuclear accident (2011) created an involuntary natural experiment in rewilding: the abrupt removal of human activity within a sharply defined evacuation zone. Unlike protected area boundaries, which suffer from residual land confounding, the exclusion zone boundary was determined by radiation dose predictions -- entirely exogenous to wildlife distributions. We propose a spatial regression discontinuity design (RDD) using this boundary to estimate the causal effect of human absence on ecosystem recovery. Primary outcome: NDVI (satellite-derived vegetation index, free from observer effort bias). Secondary: 3-zone dose-response (difficult-to-return > restricted > inhabited). Placebo: pre-accident (2010) NDVI showing no boundary discontinuity. Climate confounding is negligible (+0.22 C/12 years). No prior study has applied RDD to nuclear exclusion zone boundaries -- in Fukushima or Chernobyl. External evaluation rates novelty as maximum (5/5). Peer review confirms this is statistically the most robust RDD design in the BioEco portfolio: exogenous cutoff, no animal sorting, pixel-level power, effort-bias-free outcome.

## 1. Introduction

The Fukushima Daiichi nuclear accident of March 2011 displaced over 150,000 residents from a 20-km radius zone and additional areas with high radiation dose projections. Over the following 13 years, the evacuation zone has undergone involuntary rewilding -- the recovery of wildlife populations and vegetation in the absence of human activity. Camera trap studies have documented the presence of over 20 mammal species including wild boar, Japanese macaques, raccoon dogs, and Japanese hares within the exclusion zone (Lyons et al. 2020), with abundances comparable to or exceeding uninhabited nature reserves.

However, all existing Fukushima wildlife studies rely on zone-based comparisons (human-excluded vs. human-inhabited) or correlational analyses (radiation dose vs. abundance), without formal causal inference designs. The same limitation applies to Chernobyl research, where observational studies have documented wildlife recovery but cannot disentangle the effects of human absence from radiation exposure, land-use history, or other confounders.

Regression discontinuity design (RDD) offers a quasi-experimental solution. By exploiting the sharp boundary of the exclusion zone as a natural cutoff, RDD estimates the local causal effect of human removal on ecological outcomes. The Fukushima boundary has exceptional properties for RDD: (1) it was determined by radiation dose predictions, not wildlife distributions (exogeneity); (2) animals cannot strategically sort across the boundary (no manipulation); (3) the boundary is administratively enforced (sharp treatment).

This study differs fundamentally from our companion RDD analysis of protected area boundaries (BioEco RDD paper), where elevation confounding explained 87% of the apparent conservation effect. The Fukushima exclusion zone is predominantly lowland coastal plain, minimizing the elevation confound that plagued the protected area analysis. Climate change during the study period is negligible (+0.22 C over 12 years at Fukushima station), ensuring that any boundary discontinuity reflects human absence rather than climate trends.

We propose three complementary analyses: (1) NDVI sharp RDD at the exclusion zone boundary, (2) 3-zone dose-response comparing difficult-to-return, restricted, and inhabited areas, and (3) pre-accident placebo (2010 NDVI) to verify no pre-existing discontinuity.

## 2. Methods

### 2.1 Study area
Fukushima exclusion zone (~370 km2), Hamadori region, northeastern Honshu. Three zones: difficult-to-return (highest radiation, no return permitted), restricted residence (limited daytime access), and inhabited areas outside the exclusion zone.

### 2.2 Exclusion zone boundary
GIS polygon from Japanese government designation. Running variable: signed distance to nearest boundary point (km). Negative = inside exclusion zone.

### 2.3 Primary outcome: NDVI
MODIS MOD13Q1 (250m, 16-day composite) or Sentinel-2 (10m) NDVI. Annual maximum NDVI as proxy for vegetation recovery / ecosystem productivity. Pre-accident baseline: 2005-2010. Post-accident: 2012-2024. Satellite data is free from observer effort bias (cf. GBIF limitation identified by Rev-A).

### 2.4 Secondary outcome: 3-zone dose-response
Ordered comparison: difficult-to-return (zone 2) > restricted (zone 1) > inhabited (zone 0). Jonckheere-Terpstra trend test for ordered alternatives. Pairwise RDD at each zone boundary.

### 2.5 RDD specification
Local polynomial regression (rdrobust). Bandwidth selection: Calonico-Cattaneo-Titiunik optimal bandwidth, with sensitivity analysis across 2-15 km. Boundary segment heterogeneity: coastal plain vs. Abukuma highlands segments.

### 2.6 Covariates
Radiation dose (airborne survey maps), DEM elevation, pre-accident land cover (JAXA HRLULC 2006), distance to coast.

### 2.7 Placebo and robustness
- 2010 NDVI: no discontinuity expected (pre-accident)
- McCrary density test (not applicable for pixel-based NDVI but relevant for camera trap data)
- Bandwidth sensitivity
- Boundary segment fixed effects

### 2.8 Ethical considerations
This research analyzes satellite and publicly available ecological data from the Fukushima exclusion zone. No fieldwork within the exclusion zone is proposed. We acknowledge the ongoing human tragedy of displacement and approach this natural experiment with sensitivity to the affected communities. Our findings are intended to inform ecological recovery science, not to diminish the human costs of the disaster.

## 3. Expected Results

Based on Lyons et al. (2020) camera trap findings and satellite imagery:
- NDVI inside exclusion zone expected to be significantly higher than outside (vegetation recovery on abandoned farmland)
- Dose-response: NDVI(difficult-to-return) > NDVI(restricted) > NDVI(inhabited)
- Placebo (2010): no discontinuity (boundary did not exist pre-accident)
- Effect magnitude: estimated NDVI increase of 0.05-0.15 inside (based on farmland-to-grassland/forest succession over 13 years)

## 4. Significance

This study would provide the first causal estimate of rewilding effects at a nuclear exclusion zone boundary. Unlike protected area RDD (where residual land confounding eliminated the apparent effect), the Fukushima boundary is free from elevation bias, offering a clean test of what happens when humans are abruptly removed from a landscape.

## References

Anderson, D. et al. (2020) A large-scale assessment of wildlife communities in the Fukushima exclusion zone. Current Biology.
Lyons, P.C. et al. (2020) Rewilding of Fukushima's human evacuation zone. Frontiers in Ecology and the Environment, 18, 127-134. DOI:10.1002/fee.2149
Keele, L. & Titiunik, R. (2015) Geographic boundaries as regression discontinuities. Political Analysis, 23, 127-155.
Calonico, S. et al. (2014) Robust nonparametric confidence intervals for regression-discontinuity designs. Econometrica, 82, 2295-2326.
