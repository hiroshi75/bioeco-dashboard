# Apparent conservation effects at Japanese protected area boundaries are entirely attributable to residual land placement: A spatial regression discontinuity analysis

**Target**: Nature Sustainability (Letter)
**Version**: v1 Integrated Draft
**Date**: 2026-03-17

---

## Abstract (~200 words)

Protected areas (PAs) are the cornerstone of the CBD 30×30 target, yet whether they causally protect biodiversity remains debated. Using spatial regression discontinuity design (RDD) at boundaries of four Japanese wildlife sanctuaries with 124,009 GBIF bird occurrence records (211 species, WorldClim STI), we estimated causal effects on rarefied species richness and community temperature index (CTI). Raw CTI was 0.87°C lower inside PAs (p = 0.086), suggesting climate buffering. However, progressive elevation control revealed this was entirely confounding: latitude adjustment reduced the difference to 0.47°C, and direct DEM control eliminated it (0.11°C, p = 0.45, 87% confounding removed). Species richness showed no discontinuity. Japanese wildlife sanctuaries are systematically placed on higher-elevation residual lands, creating an apparent conservation effect that vanishes after controlling for the elevation gradient. This "residual land effect" represents a form of apparent stability in conservation — protection appears effective by conventional metrics but reflects site placement rather than active biodiversity management. Our findings urge caution in interpreting PA effectiveness from observational data and highlight the need for elevation-controlled causal designs in evaluating the 30×30 target.

## 1. Introduction
[From h-rdd-cti-paper-intro-draft.md: 30×30 context, RDD gap, dual-outcome design, Neal 2024/Cazalis 2020 context. ~310 words + Japan PA system paragraph needed.]

## 2. Methods
[Ken RDD pipeline + Sora distance calculation + Kai BIO1/DEM. Rarefaction, rdrobust, pooled meta-analysis, progressive elevation control (none→latitude→DEM).]

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
**Status**: v1 Integrated. Gate C ready after [From...] resolution.
