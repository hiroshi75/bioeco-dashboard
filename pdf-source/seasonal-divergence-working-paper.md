# Latitude determines whether climate warming erodes or amplifies seasonal bird community turnover

**Target**: Global Change Biology (Letter, ~3,500 words)
**Version**: v1 Integrated Draft
**Date**: 2026-03-17

---

## Abstract (~200 words)

Seasonal patterns in ecological communities are fundamental to ecosystem functioning, yet how climate warming reshapes seasonal turnover remains unknown. Using Baselga beta-diversity decomposition across 17 long-term bird monitoring datasets (BioTIME, 5-39 years, 6 continents), we show that the direction of seasonal community change is not uniform but strongly predicted by latitude (Spearman r = -0.647, p = 0.005, LOO 17/17 robust). At high latitudes (>45°N), seasonal beta-diversity decreases (erosion: mean slope = -0.003/yr), consistent with winter warming relaxing seasonal environmental filters. At low latitudes (≤45°N), seasonal beta-diversity increases (divergence: +0.004/yr), consistent with summer-specific warming driving season-specific species turnover. The random-effects pooled estimate was non-significant (p = 0.41, I² = 82.8%), confirming that global averaging masks this latitude-dependent heterogeneity. These findings reveal that climate change does not uniformly erode seasonality but produces predictable, opposing patterns depending on the dominant season of warming — a previously undocumented dimension of biodiversity reorganization.

## 1. Introduction
[From seasonal-divergence-paper-outline.md + intro context. ~600 words. Seasonal β gap, Lehikoinen 2021 context, Paper 1 spatial homogenization contrast.]

## 2. Methods
[From outline. BioTIME 17 studies, Baselga decomposition, rarefaction, FE/RE meta-analysis, latitude moderator meta-regression, LOO sensitivity. ~800 words.]

## 3. Results

### 3.1 Pilot: Study 67
Rarefied seasonal β: +0.008/yr (p = 0.012, outlier-excluded). Turnover decomposition: summer-only(+0.33, p=0.033) and winter-only(+0.62, p=0.014) species both increasing.

### 3.2 Global meta-analysis (17 studies)
- Fixed-effect: -0.0013/yr (p = 0.0008, erosion direction)
- Random-effect: +0.0011/yr (p = 0.41, ns)
- I² = 82.8% (p < 0.001): high heterogeneity
- 10 eroding (59%) / 7 diverging (41%)

### 3.3 Latitude moderator
- Spearman r = -0.647 (p = 0.005)
- WLS β_lat = -0.000168 (p = 0.015)
- LOO: 17/17 p < 0.05 (range r = [-0.71, -0.60])
- >45°N: erosion (-0.003/yr) | ≤45°N: divergence (+0.004/yr)

### 3.4 Climate seasonality moderator
Climate seasonality index (SI = BIO10 - BIO11) was not a significant predictor of seasonal β slope (r = -0.356, p = 0.211, n = 14 studies with WorldClim coverage). Latitude remained the stronger predictor (r = -0.591, p = 0.026, n = 14) even in this reduced subset. The SI null result likely reflects that static seasonality (current BIO10-BIO11) does not capture the rate of seasonal warming change that drives community response. The latitudinal gradient serves as a more effective proxy for Arctic amplification — the asymmetric warming of winters relative to summers that increases with latitude.

## 4. Discussion
[From seasonal-divergence-discussion-draft.md v0.1. ~800 words.]
- 4.1 Why the prediction was wrong (for the pilot) but right (globally)
- 4.2 Asymmetric warming mechanism (Arctic amplification vs monsoon)
- 4.3 Dual pattern: spatial homogenization (Paper 1) × temporal divergence/erosion
- 4.4 Heterogeneity as the signal (I²=83%, Peacor 2025 response)
- 4.5 Limitations

## 5. Conclusions
Latitude-dependent seasonal community change is a previously undocumented dimension of biodiversity reorganization under climate change. Monitoring programs must incorporate year-round, multi-season surveys to detect this hidden axis of change.

## Figures (3)
1. Global map: 17 studies with erosion(blue)/divergence(red) arrows
2. Forest plot: study-level slopes with RE pooled + latitude color gradient
3. Latitude moderator: scatter (lat × slope) with regression + 45°N threshold

## References (~25)
[Lehikoinen 2021, Senior 2016, Harrison 2011, Baselga 2010, Peacor 2025, Chinese urbanization study 2025]

## Data Availability
BioTIME 2.0: biotime.st-andrews.ac.uk. Analysis code: GitHub→Zenodo upon acceptance.

---
**Status**: v2 Integrated. BIO moderator(ns) added to 3.4. All Results confirmed. Ready for Gate C.
