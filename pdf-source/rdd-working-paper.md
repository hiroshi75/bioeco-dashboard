# Do Protected Areas Protect Biodiversity? A Spatial RDD Pilot with Dual Outcomes

BioEco Agent Lab | Working Paper | 2026-03-17

## Abstract

We apply Regression Discontinuity Design (RDD) to protected area boundaries in Japan to estimate the causal effect of protection on bird species richness and Community Temperature Index (CTI). Using 22,285 GBIF bird occurrence records around Oze National Park (IUCN Category II, 372 km2), we estimate species richness and CTI discontinuities at the park boundary. Raw species count RDD suggests a +56 species advantage inside (p=0.023), but rarefaction analysis reveals this as a density artifact caused by 23x observation effort asymmetry. After rarefaction correction, outside species richness exceeds inside (d=-0.64, p<0.001). CTI-RDD results are confounded by elevation (inside: 1400-2300m vs outside: 400-1000m) and STI quality (site-specific match rate = 23%, below the 50% prohibition threshold). These findings demonstrate that (1) rarefaction is essential for GBIF-based RDD, (2) polygon definition critically determines RDD conclusions, and (3) site-specific STI match rates must be computed. A pooled analysis of 10 low-elevation protected areas is underway to test the dual-outcome (richness + CTI) hypothesis with minimal elevation confounding.

## 1. Introduction

Protected areas cover 17% of global land area and are central to the Kunming-Montreal 30x30 target. However, rigorous causal evidence for their effectiveness on biodiversity outcomes remains limited. Neal (2024) applied spatial RDD to global protected area boundaries using forest cover as the outcome, finding an average 30% effectiveness. We extend this framework to bird species richness and CTI — outcomes that have not been tested with RDD.

## 2. Methods

### 2.1 Data
- WDPA Japan protected area polygons (IUCN Category II: Oze National Park, 372 km2)
- GBIF bird occurrence records within 20 km of park boundary (n=22,285)
- WorldClim BIO1 (2.5 arc-minute) for temperature baseline

### 2.2 RDD Specification
Running variable: signed distance to nearest park boundary (km). Positive = outside, negative = inside. Local polynomial regression with rdrobust (Calonico, Cattaneo & Titiunik 2014).

### 2.3 Rarefaction
Rarefied species richness (n=2,447) to correct for 23x density asymmetry (inside 72% of records but only 4% of area — Ken version using WDPA polygon WDPA_PID=555575152).

### 2.4 CTI-RDD
Community Temperature Index calculated using (a) Katayama temp_pos (42/180 species, 23% site-specific match) and (b) WorldClim bird STI (211/212 species, 99.5% match, 97% High confidence).

## 3. Results

### 3.1 Species Richness RDD
| Test | Estimate | p | Interpretation |
|---|---|---|---|
| Raw RDD | +56 species | 0.023 | Density artifact |
| Placebo (density) | — | 0.180 | 23x asymmetry |
| Rarefied RDD | d=-0.64 | <0.001 | Outside >= Inside |

### 3.2 CTI-RDD (Dual-STI)
| STI Source | Match Rate | CTI d | Direction |
|---|---|---|---|
| Katayama 42sp | 23% (site) | -1.62 | Inside cooler |
| WorldClim 211sp | 99.5% | +2.61 | Inside warmer |

**CTI direction reverses with STI quality — the 6th STI artifact detected by BioEco.**

### 3.3 Robustness Checks
- McCrary density test: PASS (p=0.48)
- Bandwidth sensitivity: CTI direction robust across 4-15 km bandwidths
- Species richness sensitive to bandwidth (sign change at 4 vs 6 km)

## 4. Discussion

### 4.1 Rarefaction is Essential for GBIF-based RDD
Raw GBIF occurrence counts create false "protection effects" due to birdwatcher concentration inside parks. Rarefaction is the only method that detects this density artifact.

### 4.2 Polygon Definition Determines RDD Conclusions
Ken version (single WDPA polygon, inside=4%) and Sora version (45-polygon union, inside=72%) gave opposite conclusions. This methodological finding has implications for all protected area RDD studies.

### 4.3 STI Quality as a Universal Concern
Six instances across four analyses demonstrate that input data quality determines conclusions. Site-specific STI match rates must be computed; aggregate rates mask local problems.

### 4.4 Low-Elevation Parks as the Critical Test
Oze National Park's high elevation (1400-2300m) creates structural confounding for both species richness and CTI. Low-elevation parks (Rokko, Suzuka, etc.) minimize this confounding and represent the true test of the dual-outcome hypothesis.

## 5. Next Steps
- Pooled 10-site RDD with WorldClim STI (211 species, 99.5% match)
- Category-specific RDD (IUCN II vs Ib vs V)
- CTI × protection interaction as climate debt test
- Global expansion using WDPA 240K+ protected areas

## References
- Calonico, Cattaneo & Titiunik (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. Econometrica.
- Cazalis et al. (2020). Effectiveness of protected areas in conserving tropical forest birds. Nature Communications.
- Neal (2024). The effectiveness of protected forests. J Environmental Economics and Management.
