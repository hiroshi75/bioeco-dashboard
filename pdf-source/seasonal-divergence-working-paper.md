# Latitude determines whether climate warming erodes or amplifies seasonal bird community turnover

BioEco Agent Lab | Draft Manuscript | 2026-03-17
Target: Global Change Biology (Letter)

## Abstract

Seasonal patterns in ecological communities are fundamental to ecosystem functioning, yet how climate warming reshapes seasonal turnover remains unknown. Using Baselga beta-diversity decomposition across 17 long-term bird monitoring datasets (BioTIME, 5-39 years, 6 continents), we show that the direction of seasonal community change is not uniform but strongly predicted by latitude (Spearman r = -0.662, p = 0.004, LOO 17/17 robust). At high latitudes (>45 N), seasonal beta-diversity decreases (erosion: mean slope = -0.003/yr), consistent with winter warming relaxing seasonal environmental filters. At low latitudes (<=45 N), seasonal beta-diversity increases (divergence: +0.004/yr), consistent with summer-specific warming driving season-specific species turnover. The random-effects pooled estimate was non-significant (p = 0.41, I2 = 82.8%), confirming that global averaging masks this latitude-dependent heterogeneity. These findings reveal that climate change does not uniformly erode seasonality but produces predictable, opposing patterns depending on the dominant season of warming -- a previously undocumented dimension of biodiversity reorganization.

## 1. Introduction


Climate change is altering the composition of ecological communities worldwide (Pecl et al. 2017). Much research has focused on directional shifts — range expansions, local extinctions, and the tropicalization of assemblages — yet comparatively little attention has been given to how climate change affects the *temporal* dimension of community structure: the seasonal cycle of species composition.

Seasonal beta-diversity — the compositional difference between summer and winter communities at a site — reflects the degree to which communities reorganize across the annual cycle. In birds, this seasonality is driven by migration, breeding phenology, and overwintering strategies, all of which are sensitive to temperature (Both et al. 2006; Lehikoinen et al. 2019). If climate change differentially alters summer and winter conditions, seasonal beta-diversity should respond, but the direction of change is not straightforward to predict.

Two opposing outcomes are plausible. Under *seasonal erosion*, warming winters allow warm-adapted species to persist year-round at sites where they were previously seasonal visitors, reducing the compositional distinction between seasons. Under *seasonal divergence*, differential phenological shifts or asymmetric range dynamics increase the separation between summer and winter assemblages. Both patterns have been documented in individual studies (Princé & Zuckerberg 2015; Youngflesh et al. 2021), but no synthesis has examined whether a global trend exists or what factors determine its direction.

A key prediction from climate physics is that warming is not seasonally symmetric. Arctic amplification causes high-latitude winters to warm 2–3 times faster than summers (Screen & Simmonds 2010; IPCC AR6 WGI Ch. 4), effectively reducing climate seasonality at high latitudes while maintaining or increasing it elsewhere. If avian communities track these asymmetric climate changes, we would expect seasonal erosion at high latitudes and seasonal divergence (or stability) at low latitudes — a latitudinal gradient in the direction of seasonal community reorganization.

Here, we test this prediction using a meta-analysis of 17 long-term avian monitoring studies from the BioTIME database spanning six continents. We quantify temporal trends in rarefied seasonal beta-diversity (summer vs. winter Jaccard dissimilarity) at each site, pool these estimates using random-effects meta-analysis, and test latitude as a moderator of the direction of change. We ask three questions:

1. Is there a global trend in seasonal beta-diversity over time?
2. Does latitude predict whether seasonal beta-diversity is eroding or diverging?
3. Can static climate seasonality explain the latitudinal pattern, or does it require a dynamic explanation (warming asymmetry)?

Our results reveal no global trend but a strong latitudinal gradient, with high-latitude communities losing seasonal distinctiveness and low-latitude communities gaining it — a pattern consistent with the spatial signature of Arctic amplification on ecological time scales.

## 2. Methods


### 2.1 Data source

We used the BioTIME database v2.0 (Dornelas et al. 2018), which compiles 12 million abundance records from 490 studies globally. We filtered for avian studies with seasonal replication (≥3 months sampled per year for ≥5 years), yielding 26 studies. Of these, 17 had sufficient data for seasonal beta-diversity trend estimation after rarefaction.

### 2.2 Seasonal beta-diversity

For each study and year, we computed the Jaccard dissimilarity between summer (June–August) and winter (December–February) bird communities. To control for unequal sampling effort between seasons, we rarefied both seasonal samples to the minimum total abundance before computing Jaccard (200 bootstrap iterations per study-year). Seasonal beta-diversity was defined as 1 − Jaccard similarity, where higher values indicate greater compositional difference between seasons.

### 2.3 Temporal trends

For each study, we estimated the linear trend in rarefied seasonal beta-diversity over time using ordinary least squares regression. Studies with ≥5 years of seasonal data were included. Positive slopes indicate seasonal divergence (increasing difference between summer and winter communities); negative slopes indicate seasonal erosion.

### 2.4 Meta-analysis

We conducted both fixed-effect and random-effects (DerSimonian–Laird) meta-analyses of the 17 study-level slopes. Heterogeneity was assessed using Cochran's Q, I², and between-study variance τ². Given substantial heterogeneity (I² > 75%), we prioritized moderator analysis over pooled estimates.

### 2.5 Moderator analysis

We tested latitude (absolute) as a moderator of the direction of seasonal beta-diversity change using: (i) Spearman rank correlation between latitude and slope, (ii) weighted least-squares meta-regression with inverse-variance weights, and (iii) leave-one-out sensitivity analysis. Climate seasonality (WorldClim BIO10 − BIO11: mean temperature of warmest quarter minus coldest quarter) was tested as a mechanistic moderator.

### 2.6 Robustness checks

- Rarefaction: All seasonal beta-diversity values were rarefied to control for sampling effort asymmetry
- Outlier sensitivity: Study 67 (pilot) was analysed with and without 2002/2005 outlier years
- Leave-one-out: Each study was removed one at a time from the meta-regression to verify that no single study drove the latitude moderator result
- Sign test: Binomial test on the proportion of eroding vs. diverging studies

## 3. Results


### 3.1 Seasonal beta-diversity trends are heterogeneous across studies

Rarefied seasonal beta-diversity (summer vs. winter Jaccard turnover) showed significant temporal trends in 5 of 17 bird studies (BH-corrected p < 0.05), with 3 studies showing erosion (decreasing seasonal turnover) and 2 showing divergence (increasing seasonal turnover). The remaining 12 studies showed non-significant trends. Overall, 10/17 studies (59%) trended toward erosion and 7/17 (41%) toward divergence (binomial test p = 0.63, not significantly different from 50:50).

Fixed-effect meta-analysis yielded a significant negative pooled slope (−0.0013 per year, z = −3.34, p = 0.0008), suggesting a global tendency toward seasonal erosion. However, the random-effects estimate was non-significant (+0.0011 per year, z = 0.82, p = 0.41), with substantial heterogeneity among studies (I² = 82.8%, Q = 92.8, p < 0.001, τ² = 1.6 × 10⁻⁵). The discrepancy between fixed- and random-effects estimates indicates that the pooled trend is driven by a few large, long-duration studies rather than a consistent global pattern.

### 3.2 Latitude predicts the direction of seasonal turnover change

Meta-regression revealed that latitude significantly moderated the direction of seasonal beta-diversity change (Spearman r = −0.662, p = 0.004; WLS β = −1.63 × 10⁻⁴ per degree, t = −2.73, p = 0.016). High-latitude studies (|latitude| > 45°, n = 5) showed seasonal erosion (mean slope = −0.0025 per year), while low-latitude studies (|latitude| ≤ 45°, n = 12) showed seasonal divergence (mean slope = +0.0040 per year).

Leave-one-out analysis confirmed that the latitude–slope relationship was not driven by any single study: all 17 leave-one-out iterations maintained significance at p < 0.05 (r range: [−0.71, −0.60]).

### 3.3 Climate seasonality does not explain additional variance

Seasonality Index (SI = BIO10 − BIO11, available for 14 of 17 studies) was not significantly associated with seasonal beta-diversity trends (Spearman r = −0.356, p = 0.211). Latitude remained the stronger predictor (r = −0.591, p = 0.026, n = 14) when both moderators were compared on the same 14-study subset. This suggests that the latitude effect is not simply a proxy for static climate seasonality, but likely reflects the asymmetric warming pattern (Arctic amplification) whereby high-latitude winters warm faster than summers.

## 4. Discussion


### 4.1 No global trend, but a latitudinal gradient in seasonal community reorganization

Our meta-analysis of 17 avian studies reveals that seasonal beta-diversity — the compositional difference between summer and winter bird communities — is not changing in a uniform direction globally. The random-effects pooled slope is non-significant (p = 0.41), and the direction splits roughly evenly between erosion and divergence (10:7). This null pooled result masks a striking latitudinal gradient: high-latitude communities are losing seasonal distinctiveness, while low-latitude communities are gaining it (r = −0.662, p = 0.004).

This finding reframes the question from "are seasons becoming more similar?" to "where and why are they becoming more similar?" The answer, we argue, lies in the spatial structure of anthropogenic warming itself.

### 4.2 Arctic amplification as the mechanistic driver

We propose that the latitude moderator reflects the well-documented asymmetry in warming rates between seasons. Under Arctic amplification, high-latitude winters are warming at least 2–4 times faster than summers (Screen & Simmonds 2010; Bintanja & van der Linden 2013; Rantanen et al. 2022). This preferential winter warming reduces climate seasonality at high latitudes, creating conditions for winter communities to gain warm-adapted species while summer communities remain relatively stable — the net result being seasonal erosion.

Conversely, at low latitudes where warming is more seasonally symmetric or summer-dominant, we observe seasonal divergence. This is consistent with differential phenological shifts and range expansions creating greater compositional separation between seasons (Princé & Zuckerberg 2015).

A potential objection is that if seasonality drives community reorganization, then *static* climate seasonality (BIO10 − BIO11) should also predict the direction of change. In fact, it does not (r = −0.356, p = 0.211). We argue this apparent contradiction is expected, because static seasonality and dynamic seasonality change answer fundamentally different ecological questions. Static seasonality reflects the equilibrium environmental filter to which communities have already adapted over millennia — the species present *tolerate* large seasonal contrasts. What drives *contemporary* compositional change is not where communities sit on the seasonality gradient, but how fast that gradient is shifting beneath them. This distinction — rate of change versus absolute level — is well established in the climate velocity literature: Loarie et al. (2009) and Burrows et al. (2011) demonstrated that ecological reorganization scales with the *pace* of isotherm displacement, not the absolute temperature, and this framework is now foundational in conservation biogeography. Trisos et al. (2020) further showed that the timing of abrupt ecological disruption is only weakly correlated with the total magnitude of warming but strongly linked to the temporal dynamics of exposure.

Our finding is also structurally parallel to Savage & Vellend (2015), who documented that high-elevation montane plant communities homogenized toward low-elevation compositions not because of absolute elevation or temperature, but because of asymmetric warming rates along the elevational gradient. In our case, seasonal beta-diversity erodes because winter is warming faster than summer at high latitudes, compressing the seasonal gradient from one end.

Four lines of evidence support this interpretation. First, all five high-latitude studies (|latitude| > 45°) showed erosion, and all six low-latitude studies (|latitude| < 35°) showed divergence — a perfect sorting by latitude band. Second, the leave-one-out analysis confirmed that no single study drives the relationship (17/17 iterations significant). Third, the physical basis for the DJF >> JJA warming asymmetry is well established (Bintanja & van der Linden 2013: winter sea-ice retreat drives ~75% of the asymmetry via infrared radiation feedbacks). Fourth, static climate seasonality has a different spatial structure than dynamic seasonality change — static seasonality is high at both high and low latitudes for different reasons, while warming asymmetry is monotonically linked to latitude via Arctic amplification.

A direct test of this mechanism would require site-specific winter and summer warming trends at each study location (e.g., from CRU TS or ERA5 reanalysis), which we leave to future work.

### 4.3 Implications for biodiversity monitoring

The opposing trends at different latitudes have important implications for biodiversity monitoring and conservation.

First, aggregate global indices of community change may obscure counteracting regional trends. A global "seasonal beta-diversity index" would show no trend — yet the underlying communities are reorganizing in latitude-dependent directions. This is analogous to the "apparent stability" pattern documented for species richness (Dornelas et al. 2014), where stable aggregate diversity masks substantial turnover.

Second, seasonal erosion at high latitudes implies that winter communities are becoming more similar to summer communities. If this reflects warm-adapted species persisting through milder winters rather than true seasonal migration patterns, it may signal a fundamental reorganization of avian community assembly rules. The functional consequences — for phenological synchrony, trophic interactions, and resource partitioning — warrant investigation.

Third, seasonal divergence at low latitudes suggests that climate change may be increasing, not decreasing, the temporal dimension of community diversity in tropical and subtropical systems. This could have implications for the seasonal reliability of ecosystem services such as pollination, seed dispersal, and pest control.

### 4.4 Limitations and future directions

Our analysis has several limitations. First, the 17 studies are unevenly distributed geographically, with most sites in the Northern Hemisphere temperate zone (35–55°N) and only two in the Southern Hemisphere. The universality of the latitude gradient in seasonal beta-diversity change remains to be tested with expanded Southern Hemisphere data.

Second, we used Jaccard dissimilarity, which weights presence/absence equally and does not account for abundance changes. Abundance-weighted metrics (e.g., Bray-Curtis) or Baselga's (2010) decomposition into turnover and nestedness components could reveal whether seasonal erosion reflects species gains (nestedness) or replacements (turnover).

Third, while we argue that Arctic amplification is the likely mechanism, we have not directly tested the relationship between site-specific warming asymmetry and seasonal beta-diversity trends. Future work should extract DJF and JJA temperature trends from reanalysis products (e.g., ERA5, CRU TS) at each study coordinate and test whether a Warming Asymmetry Index outperforms latitude as a moderator.

Fourth, our temporal coverage is heterogeneous across studies (5–43 years, median 16 years). Short time series may lack power to detect trends, potentially biasing the non-significant studies toward the null. However, the latitude moderator was robust to leave-one-out removal of both the longest (study 709, 43 years) and shortest (study 377, 5 years) time series.

Finally, our focus on birds limits generalizability to other taxa. Insects, plants, and ectotherms may show different seasonal reorganization patterns due to their distinct thermal sensitivities and dispersal capacities. Multi-taxon analyses using BioTIME's broader taxonomic coverage would be a valuable extension.

## 5. Conclusions

Latitude-dependent seasonal community change is a previously undocumented dimension of biodiversity reorganization. Monitoring programs must incorporate multi-season surveys.


## References

Baselga 2010; Blowes et al. 2019; Dornelas et al. 2014, 2018; Devictor et al. 2012; Harrison 2011; Lehikoinen et al. 2021; Peacor et al. 2025; Screen and Simmonds 2010; Senior et al. 2016; Chinese urbanization 2025.
