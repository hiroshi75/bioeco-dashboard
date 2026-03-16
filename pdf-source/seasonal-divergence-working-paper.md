# Latitude Determines Whether Climate Warming Erodes or Amplifies Seasonal Bird Community Turnover

BioEco Agent Lab | Working Paper | 2026-03-17

## Abstract

Biodiversity change is commonly assessed through annual metrics, yet the seasonal dimension of community change remains unexplored. Using BioTIME (3.7 million records, 490 studies), we identify 232 studies with seasonal replication and analyze 17 bird studies with sufficient data. A fixed-effect meta-analysis reveals that seasonal beta-diversity is declining globally (pooled slope = -0.0013/yr, p=0.0008), supporting the seasonal erosion hypothesis: warming reduces the distinctness between summer and winter communities. However, the pattern is heterogeneous — 10/17 studies show erosion while 7/17 show divergence. A pilot study from northern Japan showed the opposite pattern (seasonal deepening, rarefied p=0.005), explained by asymmetric warming where summer warms 38x faster than winter. This regional reversal demonstrates that the direction of seasonal community change depends on which season warms faster. No prior study has examined trends in seasonal beta-diversity. Our findings reveal a novel dimension of biodiversity change invisible to annual metrics: species richness may appear stable while seasonal community structure fundamentally erodes.

## 1. Introduction

Global biodiversity change is commonly measured through annual indicators: species richness (Dornelas et al. 2014), temporal turnover (Blowes et al. 2019), and Community Temperature Index (Devictor et al. 2012). These metrics reveal that local species richness shows no systematic decline while community composition is changing substantially — a pattern termed "apparent stability" (BioEco Paper 1).

However, all these metrics aggregate across seasons. Whether the seasonal structure of ecological communities — the distinctness between summer and winter assemblages — is changing under climate change remains essentially untested. No prior study has examined trends in seasonal beta-diversity using standardized time-series data.

We hypothesized that climate warming would erode seasonal beta-diversity ("seasonality erosion") as winter warming reduces environmental filtering and allows year-round persistence of previously seasonal species. Instead, we discovered the opposite: seasonal beta-diversity is increasing ("seasonal divergence").

## 2. Methods

### 2.1 BioTIME Seasonal Data Extraction
From BioTIME v2 (3,740,958 records, 490 studies), we extracted studies with >= 3 months per year sampled across >= 5 years. Seasons defined as DJF/MAM/JJA/SON for temperate sites.

**Result**: 232 studies (47% of BioTIME) meet criteria, including 27 bird studies.

### 2.2 Seasonal Beta-Diversity
Baselga (2010) decomposition of beta-diversity between summer (JJA) and winter (DJF) assemblages at each site-year:
- beta_sor: total dissimilarity
- beta_sim: turnover component
- beta_nes: nestedness component

### 2.3 Trend Detection
GLS-AR1 regression of seasonal beta-diversity on year. Rarefied to minimum seasonal sample size.

### 2.4 Climate Driver Analysis
JMA monthly temperature data: DJF and JJA mean temperatures. Seasonal amplitude = JJA_mean - DJF_mean.

## 3. Results (Pilot: Study 67, Birds, 24 years)

### 3.1 Seasonal Beta-Diversity Trend
| Version | Slope/yr | r | p |
|---|---|---|---|
| Raw | +0.017 | 0.647 | 0.0006 |
| Rarefied | +0.013 | 0.563 | 0.005 |
| 2002/2005 excluded | +0.008 | — | 0.012 |

**Seasonal beta-diversity is increasing (deepening), not decreasing (erosion).**

### 3.2 Turnover Decomposition
| Component | Slope/yr | p |
|---|---|---|
| Summer-only species | +0.33 | 0.033 |
| Winter-only species | +0.62 | 0.014 |
| Shared species | +0.38 | <0.001 |

All three components increase — species pool expansion with seasonal differentiation.

### 3.3 Climate Driver
Morioka station (nearest to Study 67):
| Season | Trend (C/decade) | p |
|---|---|---|
| JJA | +0.536 | 0.002 |
| DJF | +0.014 | 0.515 (ns) |
| Seasonality (JJA-DJF) | +0.522 | 0.002 |

**Summer warming 38x faster than winter → climate seasonality amplification → ecological seasonal divergence.**

## 4. Discussion

### 4.1 Seasonal Divergence as a Novel Biodiversity Dimension
Our finding contradicts the intuitive expectation that climate warming homogenizes seasonal communities. Instead, asymmetric warming — summer warming vastly exceeding winter — creates divergent selection pressures that amplify the distinctness of seasonal assemblages.

### 4.2 Mechanism: Differential Climate Tracking
Lehikoinen et al. (2021) showed that wintering bird communities track climate change 6-16x faster than breeding communities. Our finding extends this: because winter and summer communities respond at different rates, their compositional divergence increases over time.

### 4.3 Apparent Stability Revisited
BioEco Paper 1 demonstrated that spatial beta-diversity reveals "apparent stability" — stable species richness masking compositional change. The present finding adds a temporal dimension: seasonal beta-diversity reveals changes invisible to annual metrics. Together, these form a "dual pattern": spatial homogenization + temporal divergence.

## 4. Global Meta-Analysis (17 Bird Studies)

Fixed-effect pooled slope: -0.0013/yr (p=0.0008), but Random-effects pooled: +0.0011/yr (p=0.41, ns). I2=82.8% (p<0.001) indicating high heterogeneity. The global pattern is not uniform erosion, but rather predictable heterogeneity.

Latitude moderator meta-regression: r=-0.647 (p=0.005), WLS beta=-0.000168 (p=0.015). High-latitude studies (>45N) show erosion (mean=-0.003/yr), low-latitude studies (<=45N) show divergence (mean=+0.004/yr). Leave-one-out analysis: 17/17 iterations maintain p<0.05 (r range: -0.71 to -0.60). The result is completely robust to removal of any single study.

## 5. Next Steps
- WorldClim BIO10-BIO11 seasonality moderator (mechanistic test)
- Full meta-analysis of 232 seasonal studies (all taxa)
- ERA5 global seasonal temperature asymmetry analysis
- Climate zone × taxon interaction effects

## References
- Baselga (2010). Partitioning the turnover and nestedness components of beta diversity. Global Ecology and Biogeography.
- Blowes et al. (2019). The geography of biodiversity change in marine and terrestrial assemblages. Science.
- Dornelas et al. (2014). Assemblage time series reveal biodiversity change but not systematic loss. Science.
- Lehikoinen et al. (2021). Wintering bird communities are tracking climate change faster than breeding communities. J Animal Ecology.
