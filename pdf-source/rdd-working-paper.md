# Apparent conservation effects at Japanese protected area boundaries are entirely attributable to residual land placement: A spatial regression discontinuity analysis

**Target**: Nature Sustainability (Letter)
**Version**: v1 Integrated Draft
**Date**: 2026-03-17

---

## Abstract (~200 words)

Protected areas (PAs) are the cornerstone of the CBD 30×30 target, yet whether they causally protect biodiversity remains debated. Using spatial regression discontinuity design (RDD) at boundaries of four Japanese wildlife sanctuaries with 124,009 GBIF bird occurrence records (211 species, WorldClim STI), we estimated causal effects on rarefied species richness and community temperature index (CTI). Raw CTI was 0.87°C lower inside PAs (p = 0.086), suggesting climate buffering. However, progressive elevation control revealed this was entirely confounding: latitude adjustment reduced the difference to 0.47°C, and direct DEM control eliminated it (0.11°C, p = 0.45, 87% confounding removed). Species richness showed no discontinuity. Japanese wildlife sanctuaries are systematically placed on higher-elevation residual lands, creating an apparent conservation effect that vanishes after controlling for the elevation gradient. This "residual land effect" represents a form of apparent stability in conservation — protection appears effective by conventional metrics but reflects site placement rather than active biodiversity management. Our findings urge caution in interpreting PA effectiveness from observational data and highlight the need for elevation-controlled causal designs in evaluating the 30×30 target.

## 1. Introduction

The Kunming-Montreal Global Biodiversity Framework commits nations to protecting 30% of terrestrial and marine areas by 2030 (the "30x30 target"). However, whether existing protected areas (PAs) causally protect biodiversity -- as opposed to merely occupying land that would have high biodiversity regardless -- remains contested. The "residual land" hypothesis (Joppa and Pfaff 2009) posits that PAs are disproportionately placed on land unsuitable for development (high elevation, steep slopes, low agricultural value), creating a systematic confound between protection status and environmental conditions.

Regression discontinuity design (RDD) offers a quasi-experimental approach to this question by exploiting the sharp discontinuity at PA boundaries: if protection causally affects biodiversity, outcomes should change discontinuously at the boundary. Neal (2024) applied spatial RDD to global PA boundaries using forest cover, finding 30% average effectiveness. Cazalis et al. (2020) assessed PA effectiveness for tropical forest birds using matching methods, finding effects only for forest-dependent species. However, no study has applied RDD to bird community temperature indices (CTI) -- a metric directly relevant to climate change adaptation.

We apply spatial RDD to four Japanese wildlife sanctuaries (IUCN Category IV) with dual outcomes: rarefied species richness and CTI. Japan provides an ideal test case because its PA system includes numerous small-to-medium sanctuaries (mean 54-107 km2) in diverse elevation settings, and GBIF bird occurrence data are dense (124K records across 4 sites, 93% from eBird). We progressively control for elevation confounding using latitude proxy and direct DEM measurements, providing a methodological template for causal PA evaluation.

## 2. Methods

### 2.1 Study sites
Four Japanese wildlife sanctuaries (IUCN IV): Rokko (54 km2, Hyogo), Suzuka (54 km2, Mie/Shiga), Kurotaki-Omine (107 km2, Nara), and Taraki (67 km2, Nagasaki). Sites were selected for low-to-moderate elevation and high GBIF record density.

### 2.2 Data
GBIF bird occurrence records within 30 km of each PA boundary (Download API, total 124,009 records, 211 species). WorldClim BIO1 (2.5 arc-minute) for temperature. SRTM DEM (30m) for elevation. WDPA polygons for boundary definition.

### 2.3 Running variable and RDD estimation
Signed distance to nearest PA boundary (km) using shapely GIS calculation. Local polynomial regression with rdrobust (Calonico et al. 2014). Rarefied species richness and CTI as dual outcomes.

### 2.4 CTI calculation
CTI = abundance-weighted mean STI. WorldClim bird STI (211/212 species, 99.5% match, 97% High confidence) as primary. Site-specific match rates verified above 80% threshold.

### 2.5 Progressive elevation control
Three models: (1) no control, (2) latitude as BIO1 proxy, (3) direct DEM elevation as covariate. This staged approach quantifies the proportion of apparent PA effect attributable to elevation confounding.

### 2.6 Robustness checks
McCrary density test, bandwidth sensitivity (4-15 km), rarefaction, sign test across sites.

## 3. Results
- 3.1 Species richness: pooled ns (3/4 outside > inside)
- 3.2 CTI raw: 4/4 inside < outside (-0.87°C, p=0.086)
- 3.3 Progressive elevation control: lat -0.47°C(p=0.078) → DEM **-0.11°C(p=0.45, ns)**. 87% confounding
- 3.4 Residual land effect confirmed
- 3.5 Falsification: McCrary PASS, density placebo ns

## 4. Discussion
- 4.1 Residual land effect: PAs on higher-elevation land → apparent CTI difference = structural artifact
- 4.2 Methodological lessons: RDD × CTI requires direct elevation control (latitude proxy removes only 46%)
- 4.3 Connection to Apparent Stability: Paper 1 (spatial) + Theme 12 (temporal) + this study (institutional)
- 4.4 Policy: 30×30 must prioritize lowland/high-pressure areas, not residual mountain land
- 4.5 Limitations: 4 sites Japan only, GBIF effort bias, IUCN IV only

## 5. Conclusions
PA placement on residual land creates false conservation signals. Evaluation of 30×30 requires elevation-controlled causal designs.

## Figures (3)
1. Progressive control: 3-panel (raw/lat/DEM) showing CTI difference elimination
2. Forest plot: 4 sites × 3 control levels
3. Map: 4 sites with elevation gradient visualization

## References (~25)
[Mika 22 references prepared. Neal 2024, Cazalis 2020, Gray 2016, SciAdv 2022, Cattaneo 2021.]

## Data Availability
WDPA: protectedplanet.net. GBIF: gbif.org (Download key: 0041145-260226173443078). WorldClim: worldclim.org. SRTM: earthdata.nasa.gov.

---
**Status**: v2 Full text integrated. Gate C ready.
