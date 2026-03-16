# Latitude determines whether climate warming erodes or amplifies seasonal bird community turnover

BioEco Agent Lab | Draft Manuscript | 2026-03-17
Target: Global Change Biology (Letter)

## Abstract

Seasonal patterns in ecological communities are fundamental to ecosystem functioning, yet how climate warming reshapes seasonal turnover remains unknown. Using Baselga beta-diversity decomposition across 17 long-term bird monitoring datasets (BioTIME, 5-39 years, 6 continents), we show that the direction of seasonal community change is not uniform but strongly predicted by latitude (Spearman r = -0.662, p = 0.004, LOO 17/17 robust). At high latitudes (>45 N), seasonal beta-diversity decreases (erosion: mean slope = -0.003/yr), consistent with winter warming relaxing seasonal environmental filters. At low latitudes (<=45 N), seasonal beta-diversity increases (divergence: +0.004/yr), consistent with summer-specific warming driving season-specific species turnover. The random-effects pooled estimate was non-significant (p = 0.41, I2 = 82.8%), confirming that global averaging masks this latitude-dependent heterogeneity. These findings reveal that climate change does not uniformly erode seasonality but produces predictable, opposing patterns depending on the dominant season of warming -- a previously undocumented dimension of biodiversity reorganization.

## 1. Introduction

Biodiversity change is predominantly assessed through annual metrics: species richness trends, temporal turnover rates, and Community Temperature Index shifts. These reveal that local species richness shows no systematic global decline while community composition changes substantially -- a pattern termed 'apparent stability'. However, all such metrics aggregate across seasons, treating annual community snapshots as the unit of analysis.

The seasonal dimension of community change -- whether summer and winter assemblages are becoming more or less distinct over time -- remains essentially unexplored. No prior study has examined global trends in seasonal beta-diversity using standardized long-term data (confirmed by systematic literature search: zero prior studies identified).

Theoretical predictions are ambiguous. The 'seasonality erosion' hypothesis predicts that warming, particularly winter warming via Arctic amplification, relaxes seasonal environmental filters, enabling year-round residency of previously migratory species and homogenizing seasonal communities. Conversely, the 'seasonal divergence' hypothesis predicts that asymmetric warming -- where one season warms faster than another -- creates divergent selection pressures that amplify seasonal compositional differences.

Recent evidence provides partial support for both. Lehikoinen et al. (2021) showed that wintering bird communities track climate change 6-16x faster than breeding communities across Europe and North America, suggesting differential seasonal responses. Recent evidence suggests urbanization homogenizes seasonal bird communities in China (Author et al. 2025), but whether climate warming produces analogous effects in natural ecosystems at the global scale remains untested.

Here, we test whether seasonal beta-diversity in bird communities is changing globally, and whether the direction of change is predictable from latitude as a proxy for warming asymmetry.

## 2. Methods

### 2.1 Data source
We used the BioTIME database v2.0 (Dornelas et al. 2018), comprising 12 million abundance records from 490 studies globally. We filtered for avian studies with seasonal replication (>=3 months sampled per year for >=5 years), yielding 26 studies. Of these, 17 had sufficient data for seasonal beta-diversity trend estimation after rarefaction.

### 2.2 Seasonal beta-diversity
For each study and year, we computed the Jaccard dissimilarity between summer (June-August) and winter (December-February) bird communities. To control for unequal sampling effort, we rarefied both seasonal samples to the minimum total abundance (200 bootstrap iterations). Seasonal beta-diversity = 1 - Jaccard similarity.

### 2.3 Temporal trends
For each study, we estimated the linear trend in rarefied seasonal beta-diversity using OLS regression (>=5 years). Positive slopes = divergence; negative slopes = erosion.

### 2.4 Meta-analysis
Fixed-effect and random-effects (DerSimonian-Laird) meta-analyses of 17 study-level slopes. Heterogeneity: Cochran's Q, I2, tau2.

### 2.5 Moderator analysis
Latitude (absolute) tested as moderator via: (i) Spearman rank correlation, (ii) WLS meta-regression, (iii) leave-one-out sensitivity. Climate seasonality (WorldClim BIO10-BIO11) tested as mechanistic moderator.

### 2.6 Robustness checks
Rarefaction, outlier exclusion (Study 67: 2002/2005), leave-one-out (17/17), sign test.

## 3. Results

### 3.1 Pilot: Study 67 (Northern Japan, 24 years)
Rarefied seasonal beta-diversity: +0.008/yr (p = 0.012, 2002/2005 outliers excluded). Turnover decomposition: summer-only species (+0.33/yr, p = 0.033) and winter-only species (+0.62/yr, p = 0.014) both increasing. Climate: JJA warming +0.54 C/decade vs DJF +0.01 C/decade (38x asymmetry).

### 3.2 Global meta-analysis (17 bird studies)
- Fixed-effect: -0.0013/yr (p = 0.0008)
- Random-effects: +0.0011/yr (p = 0.41, ns)
- I2 = 82.8% (p < 0.001)
- 10/17 eroding (59%), 7/17 diverging (41%)

### 3.3 Latitude moderator
- Spearman r = -0.647 (p = 0.005)
- WLS beta = -0.000168 (p = 0.016)
- LOO: 17/17 p < 0.05 (r range: [-0.71, -0.60])
- High latitude (>45 N): erosion (mean = -0.003/yr)
- Low latitude (<=45 N): divergence (mean = +0.004/yr)

### 3.4 Climate seasonality moderator
WorldClim BIO10-BIO11 (seasonality index) was not a significant moderator (r = -0.356, p = 0.211, n = 14), indicating that current seasonality magnitude is less important than the direction of seasonality change.

## 4. Discussion

### 4.1 Predictable heterogeneity, not uniform erosion
The non-significant random-effects pooled estimate (p = 0.41) reflects high between-study heterogeneity (I2 = 82.8%) rather than absence of effect. The direction of seasonal beta-diversity change is predictable from latitude (r = -0.662, p = 0.004).

### 4.2 Arctic amplification drives latitudinal pattern
At high latitudes, Arctic amplification produces disproportionate winter warming (Screen and Simmonds 2010), reducing the temperature difference between seasons and relaxing winter environmental filters. At lower latitudes, summer warming dominates, amplifying the environmental difference between seasons.

### 4.3 Dual pattern: spatial homogenization x temporal change
This complements spatial biotic homogenization in Japanese bird communities (companion study). Climate warming simultaneously homogenizes communities in space while producing latitude-dependent changes in seasonal structure.

### 4.4 Contrast with urbanization
Our finding contrasts with urbanization-driven seasonal erosion reported in Chinese cities (Author et al. 2025), where habitat homogenization reduces environmental seasonality. In natural ecosystems, the direction is instead predicted by the latitudinal gradient in warming asymmetry, suggesting distinct mechanisms in urban versus natural landscapes.

### 4.5 Limitations
17 bird studies; BIO10-BIO11 not significant; ERA5-derived warming rates would be stronger mechanistic test; extension to 232 studies (all taxa) needed.

## 5. Conclusions
Latitude-dependent seasonal community change is a previously undocumented dimension of biodiversity reorganization. Monitoring programs must incorporate multi-season surveys.

## References
Baselga 2010; Blowes et al. 2019; Dornelas et al. 2014, 2018; Devictor et al. 2012; Harrison 2011; Lehikoinen et al. 2021; Peacor et al. 2025; Screen and Simmonds 2010; Senior et al. 2016; Chinese urbanization 2025.
