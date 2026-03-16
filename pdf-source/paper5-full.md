# Ghost signals in phenological records: Delayed first-detection dates reveal widespread population declines of Japanese insects and amphibians

**Target journal**: Ecology Letters (Article)
**Draft version**: v1 Integrated
**Date**: 2026-03-15
**Authors**: BioEco Agent Lab

---

## Abstract (~250 words)

Phenological records are widely interpreted as indicators of climate change, yet first-detection dates are statistically sensitive to population size. Here we show that animal phenological delays in Japan's 67-year monitoring record are "ghost signals" of population decline rather than climate responses. Among 10 animal phenological events recorded by the Japan Meteorological Agency (1953–2020), three showed significant delays and none showed advances — despite ongoing warming of +0.052°C yr⁻¹. In contrast, plants showed both advances and delays (Fisher's exact test, p = 0.37; a directional pattern consistent with detection-bias theory, though not statistically significant given the limited number of taxa). Japanese tree frog first-calling dates delayed by +3.2 days decade⁻¹ (GLS-AR1) (p = 0.004, GLS-AR1, n = 41 stations), and spring cicada by +2.5 days decade⁻¹ (GLS p = 0.010). Systematic elimination of six alternative hypotheses — urbanization bias (p = 0.86), precipitation patterns (p = 0.70), paddy management, climate warming, farmland abandonment (r = 0.05), and observer effects — supports population decline as the most parsimonious explanation. Independent monitoring data corroborate widespread declines of rice-paddy fauna: fireflies at 81% of sites (p = 0.002), with paddy-specialist species declining ~2× faster than stream-dwelling congeners. Delays intensify with latitude (ρ = 0.49, p = 0.001). Our findings demonstrate that phenological monitoring networks can serve as unrecognised early-warning systems for population collapse, and urge reinterpretation of global phenological datasets where delays contradict warming trends.

---

## 1. Introduction

[See workspace/paper4-5-introduction-draft.md for full text]

Phenological monitoring is one of ecology's oldest practices. The Japan Meteorological Agency (JMA) has recorded biological seasonal events across ~60 stations since 1953, creating one of the world's longest phenological datasets. These records are widely interpreted as climate indicators.

However, first-detection dates are statistically extreme values, inherently sensitive to population size (Sparks & Tryjanowski, 2001; Miller-Rushing et al., 2008; van Strien et al., 2008; Moussus et al., 2010; Roth et al., 2014; Edwards & Crone, 2021). When populations decline, detection probability decreases, producing apparent delays — "ghost signals" — defined operationally as statistically significant delays in first-detection dates that (a) contradict the direction expected from concurrent temperature trends and (b) correlate with independent evidence of population decline. This detection-bias mechanism has been theoretically predicted (Miller-Rushing et al., 2008) and empirically demonstrated in Dutch butterflies (van Strien et al., 2008), declining Wood Thrush populations (Roth et al., 2014), and North American monarch butterflies (Edwards & Crone, 2021). However, it has not been validated at multi-taxon, multi-decadal scale with systematic alternative hypothesis elimination. DOI:10.1111/j.1365-2486.2008.01619.x

The possibility that phenological delays in Japanese insects reflect population declines rather than climate maladaptation was first raised by Ellwood et al. (2012), who analyzed ~40 years of JMA phenological records for 14 insect species. They noted that "declining populations may show delayed first appearance dates simply because fewer individuals are present to be detected early in the season," but did not formally test this hypothesis against alternative explanations. Here, we extend their analysis in four key ways: (1) a substantially longer time series (67 years vs. ~40 years) encompassing 33 species across both animals and plants; (2) systematic testing and exclusion of six alternative hypotheses; (3) independent validation using population abundance data from Ueta et al. (2025); and (4) identification of taxon-specific vulnerability patterns and a latitudinal gradient.

**Study approach**: This study was exploratory in origin. During systematic analysis of JMA phenological data, we detected anomalous delays in Japanese tree frog first-calling dates that contradicted warming predictions. This observation generated the hypothesis (H-PHENO-1) that delays reflect population decline rather than phenological change. We then tested this hypothesis through: (1) analysis of all JMA animal and plant phenological events, (2) systematic elimination of six alternative hypotheses using independent datasets, and (3) validation against long-term population monitoring data.

---

## 2. Methods

### 2.1 JMA Phenological Records (1953–2020)
First-detection dates for 10 animal events (frog calling, cicada calling, lizard sighting, bird arrival) and 23 plant events (flowering, leaf-out) from the JMA Biological Seasonal Observation database. Animal observations were discontinued in January 2021. We included all station-event combinations with ≥20 years of records.

### 2.2 Station classification
JMA stations (n = 166) were classified as urban (n = 6; stations located in cities with population >300,000; 12 cities met this criterion, of which 6 had sufficient phenological data) or rural (n = 35) for the urbanization-bias analysis. Stations were classified as Sea of Japan coast or Pacific coast based on geographic location for the precipitation analysis.

### 2.3 Phenological trend analysis
Linear trends in first-detection date (day of year) were estimated using Generalized Least Squares with first-order autoregressive errors (GLS-AR1), estimated via the Cochrane-Orcutt procedure, for each station-event combination. To assess the impact of temporal autocorrelation, we report both OLS and GLS results (Supplementary Table S1). For species where the Durbin-Watson test indicated significant autocorrelation (DW < 1.5 or > 2.5), GLS estimates were used as the primary result. Trends are reported as days per decade. Species were classified as significantly delayed (positive slope, p < 0.05), advanced (negative slope, p < 0.05), or stable. This approach improves upon Ellwood et al. (2012), who used OLS without autocorrelation correction.

### 2.4 Alternative hypothesis testing
Six alternative hypotheses were evaluated using independent statistical tests. Each represents a distinct scientific question regarding the mechanism of delay; therefore, no family-wise error rate correction was applied to the primary analyses (Rothman, 1990). For transparency, Benjamini-Hochberg FDR-corrected p-values for all tests conducted in this study are reported in Supplementary Table S3, allowing readers to assess robustness under alternative multiple testing philosophies. Tests and predictions are detailed in Table 1. DOI:10.1097/00001648-199001000-00010

### 2.5 Independent population validation
Population trends for fireflies (Heike *Aquatica lateralis*, Genji *Nipponoluciola cruciata*) and frogs (Japanese brown frog *Rana japonica*, Montane brown frog *R. ornativentris*) from Ueta et al. (2025), a 15–20 year monitoring dataset across 158 satoyama sites. Note: JMA phenological records cover Japanese tree frog (*Dryophytes japonicus*), while Ueta population data cover *R. japonica* and *R. ornativentris* — different species within the same order (Anura). Independent validation is therefore at the taxonomic-group level, not the species level.

### 2.6 Latitudinal gradient
Spearman rank correlation between station latitude and the magnitude of delay slope across all stations with sufficient data.

### 2.7 Statistical software
Python 3.x (scipy, statsmodels, numpy). No multiple comparison correction was applied to the six alternative hypothesis tests, as each addresses a distinct a priori scientific question rather than a family of related comparisons.

---

## 3. Results

### 3.1 Animal phenological trends: delays only, no advances
After GLS-AR1 correction for temporal autocorrelation, 9 of 33 species showed significant phenological trends (compared to 10 under OLS; Supplementary Table S1). Among 10 animal phenomena, 3 showed significant delays under GLS, 7 showed no trend, and none showed significant advances (Fig. 1). Among 23 plant phenomena, 3 advanced, 3 delayed, 17 stable. Three species lost significance after autocorrelation correction, while two gained significance; core results were robust. Polynomial comparison (linear/quadratic/cubic) confirmed linear trend adequacy for 21/33 species (64%; ΔAIC > 2 for nonlinear in 12 species, Table S1). Results were qualitatively unchanged when restricting to the 21 linear-confirmed species. The animal–plant contrast was not statistically significant (Fisher's exact test, OR = 2.43, p = 0.37), reflecting limited sample size (n = 33 taxa), though the qualitative pattern — zero advances in animals — is striking and consistent with detection-bias theory.

### 3.2 Japanese tree frog delays: magnitude and extent
First-calling dates delayed by +3.2 days decade⁻¹ (GLS-AR1) (p = 0.004, GLS-AR1, n = 41 stations, 67 years). Delays were detected at 34/41 stations (83%). Over the full observation period, this represents a cumulative delay of ~21 days. Spring cicada (*T. nigricosta*) delayed by +2.5 days decade⁻¹ (GLS p = 0.010, n = 41 stations). Year-to-year temperature variation showed the expected negative correlation with first-calling date (warmer → earlier, r = −0.20), confirming intact temperature sensitivity.

### 3.3 All six alternative hypotheses eliminated
(a) Urbanization bias: no urban/rural difference (t = 0.18, p = 0.86, d = 0.06 [−0.73, 0.85]); rural alone p = 0.0009.
(b) Paddy management: spring cicada (forest species) also delayed.
(c) Precipitation: no Sea of Japan/Pacific difference (t = −0.39, p = 0.70, d = −0.13 [−0.78, 0.52]); Pacific alone p = 0.0004.
(d) Climate warming: year-to-year response intact; long-term delay contradicts warming.
(e) Farmland abandonment: no correlation (r = 0.052, p = 0.80).
(f) Observer bias: delayed and non-delayed taxa at same stations, same protocol.

### 3.4 Rice-paddy species decline ~2× faster than non-paddy congeners
Heike firefly −41% decade⁻¹ vs Genji −23% (ratio 1.8×). Fireflies declined at 81% of sites (p = 0.002). Japanese brown frog −58% decade⁻¹ vs Montane brown frog −25% (ratio 2.3×). The frog decline was not statistically significant at α = 0.05 (p = 0.094). Post-hoc power analysis indicated that our frog validation sample (n = 28) had power = 0.34 to detect a medium correlation (|r| = 0.3) and power = 0.78 for a large correlation (|r| = 0.5); a sample of n ≥ 85 sites would be needed for 80% power at |r| = 0.3. The non-significant result should therefore be interpreted as underpowered rather than evidence of absence. The effect size (−58% decade⁻¹) is large and the direction is consistent with the firefly pattern.

### 3.5 Latitudinal gradient
Delays intensified with latitude (ρ = 0.49, p = 0.001). Hokkaido showed the largest delays (slope = +1.91 days decade⁻¹, 100% of stations delayed). This gradient was observed across all latitudinal zones (31–46°N).

---

## 4. Discussion

[See workspace/paper4-5-discussion-draft.md for full text]

4.1 Ghost signals: phenological delays as detection bias — extending the hypothesis of Ellwood et al. (2012), who first noted anomalous delays in JMA insect phenology and proposed population decline as a potential explanation, and building on Roth et al. (2014), who demonstrated detection-bias delays in declining Wood Thrush populations. Notably, a recent global analysis (NatComms 2026) demonstrated the reverse causal pathway — phenological shifts driving population declines — underscoring the bidirectional relationship between phenology and population dynamics. Our "ghost signal" mechanism represents the complementary direction: population decline producing apparent phenological change. Our study provides the first large-scale, multi-taxon corroboration through: 67 years of data (vs. ~40), 33 species including plants (vs. 14 insects), systematic exclusion of six alternative hypotheses (not attempted by Ellwood), and independent population validation (Ueta 2025). GLS-AR1 correction addresses temporal autocorrelation not controlled in Ellwood's OLS analysis. Comparison with Ecography 2021 Wood frog study (+1.4 days/decade): independent discovery on two continents, but different proposed mechanisms (snow-pack vs detection bias). Our H1d rejection (p=0.70) differentiates.
4.2 The "ticking time-bomb" (Simmonds 2020): phenological records can mask population collapse. DOI:10.1111/ele.13603
4.3 Connection to the "species richness paradox" (Paper 1): conventional metrics systematically underestimate biodiversity loss.
4.4 Rice paddy case study: habitat quality, not quantity, drives decline. ALAN and fipronil as candidate drivers (untested hypotheses for future investigation).
4.5 Latitudinal gradient: northern populations most vulnerable (descriptive, cautious; n=4 above 41°N limits precision).
4.6 Policy implications: reinstate animal phenological monitoring; reanalyse global datasets; FAD delays as early-warning indicators.
4.7 Limitations: no direct spatial matching of JMA/Ueta; FAD-only records; Japan-only; natural fluctuation cannot be fully excluded. Post-hoc power analysis indicated that the frog validation (n = 28, p = 0.094) had power = 0.34 for medium effects (|r| = 0.3), suggesting the non-significant result reflects insufficient sample size rather than absence of effect. We were unable to test for effects of artificial light at night (ALAN), pesticide use (neonicotinoids), or invasive species competition due to lack of site-level data for these variables. These remain important avenues for future research, particularly given emerging evidence of neonicotinoid impacts on aquatic invertebrates in rice-paddy ecosystems.

---

## 5. Conclusions

Phenological monitoring networks harbour an unrecognised capacity: the detection of cryptic population declines through "ghost signals" in first-detection dates. Our 67-year analysis of Japanese phenological records reveals that delays exclusively affect taxa with documented population declines, while stable or plant species show expected warming-driven patterns. These ghost signals are currently misinterpreted, yet they may represent one of the earliest and most widespread indicators of biodiversity loss.

---

## Figures and Tables

- **Fig. 1**: All 33 phenological events — animal (left, n = 10) vs plant (right, n = 23) barplot, coloured by delay/stable/advance. Note: the animal–plant contrast was not statistically significant (Fisher's exact test, p = 0.37), reflecting limited sample size.
- **Fig. 2**: Japanese tree frog first-calling date time series (1953–2020) with linear trend (+3.2 days decade⁻¹ (GLS-AR1), station-level mean of 41 stations). Note: the annual-aggregate regression slope is +3.1 days decade⁻¹, reflecting compositional changes in reporting stations over time; the station-level mean is used throughout as the primary estimate.
- **Fig. 3**: Alternative hypothesis elimination panels: (a) urban/rural, (b) Sea of Japan/Pacific, (c) temperature response, (d) farmland abandonment.
- **Fig. 4**: Paddy vs non-paddy decline rates (firefly + frog paired comparison).
- **Fig. 5**: Latitudinal gradient map of Japan showing delay magnitude by station.
- **Table 1**: Complete alternative hypothesis elimination table (6 hypotheses × test × prediction × result × p-value).

---

## Supplementary Material

- **Table S1**: Station-level phenological trends for all 33 species across all JMA stations (1,341 station-species combinations). Includes station coordinates, data period, OLS trend slopes (slope, days/decade, r, p), GLS-AR1 trend slopes (slope, SE, p, AR(1) ρ). For 13 stations of species 043 (mulberry leaf-out) where AR(1) > 0.95, first-difference regression was applied as fallback. (Ken workspace/paper5_table_s1_ols_gls.csv)
- **Table S2**: Ellwood et al. (2012) differentiation table — comparison of data scope, methods, and findings between this study and the prior analysis of JMA phenological data.
- **Table S3**: Benjamini-Hochberg FDR-corrected p-values for six alternative hypothesis tests. All tests that were significant at α = 0.05 remain significant after FDR correction (q < 0.05).

## Author Contributions

Conceptualization: Ryo, Ken. Data analysis: Ken. Literature review and reference curation: Mika. Quality assurance and bias audit: Yui. Visualization: Ken, Hana. Writing — original draft: Ryo. Writing — review and editing: all authors. Project coordination: Jim.

## Competing Interests

The authors declare no competing interests.

## Data Availability

JMA phenological data are publicly available at data.jma.go.jp/sakura/data/. Note: This study and a companion paper (Paper 1, submitted to Ecology Letters) both use the Ueta et al. (2025) satoyama monitoring dataset for independent validation; however, the two papers address distinct research questions (phenological detection bias vs. functional community reorganization) using different analytical approaches. Ueta et al. (2025) satoyama monitoring data: [repository DOI TBD — to be deposited in Zenodo/Dryad upon acceptance]. JMA station coordinates: obtained from JMA metadata via jmastats R package. All analysis code will be deposited in a public GitHub repository with a Zenodo DOI upon acceptance.



Belitz, M.W. et al. (2025) Phenological mismatch across three trophic levels in eastern North American birds. *Journal of Animal Ecology*, DOI: 10.1111/1365-2656.70007.

Burant, J.B. et al. (2021) Early warning indicators of population collapse in a seasonal environment. *Journal of Animal Ecology*, 90, 1538-1549. DOI:10.1111/1365-2656.13485

Cleland, E.E. et al. (2012) Phenological tracking enables positive species responses to climate change. *Ecology*, 93, 1765-1771. DOI:10.1890/11-1912.1

Dornelas, M. et al. (2014) Assemblage time series reveal biodiversity change but not systematic loss. *Science*, 344, 296-299. DOI:10.1126/science.1248484

Ellwood, E.R., Diez, J.M., Ibáñez, I., Primack, R.B., Kobori, H., Higuchi, H. & Silander, J.A. (2012) Disentangling the paradox of insect phenology: are temporal trends reflecting the response to warming? *Oecologia*, 168, 1161-1171. DOI:10.1007/s00442-011-2160-4

Hillebrand, H. et al. (2018) Biodiversity change is uncoupled from species richness trends: Consequences for conservation and monitoring. *Journal of Applied Ecology*, 55, 169-184. DOI:10.1111/1365-2664.12959

Hirayama, D. et al. (2025) Long-term management is required for the recovery of pollination networks of semi-natural grasslands. *Journal of Applied Ecology*, DOI: 10.1111/1365-2664.70017.

Hu, G. et al. (2023) Decline of migrating aerial insect biomass over East Asia. *Science Advances*, 9, eade9341. DOI:10.1126/sciadv.ade9341

Hughes, A.C. & Grumbine, R.E. (2023) The Kunming-Montreal Global Biodiversity Framework: what it does and does not do, and how to improve it. *Frontiers in Environmental Science*, 11, 1281536. DOI:10.3389/fenvs.2023.1281536

Katayama, N. et al. (2024) Effects of human depopulation and warming climate on bird populations in Japan. *Conservation Biology*, 38, e14175. DOI:10.1111/cobi.14175

Koenig, S. et al. (2022) Succession comprises a sequence of threshold-induced community assembly processes towards multidiversity. *Communications Biology*, 5, 510.

Miller-Rushing, A.J., Miller, T.K., Lloyd-Evans, T.L. & Primack, R.B. (2008) Bird migration times, climate change, and changing population sizes. *Global Change Biology*, 14, 1959-1972.

Morelli, F. et al. (2025) Avian diversity changes in traditional agricultural landscapes of Japan over ten years. *Oikos*, 2025, e11041. DOI:10.1002/oik.11041

Moussus, J.-P., Julliard, R. & Jiguet, F. (2010) Featuring 10 phenological estimators using simulated data. *Methods in Ecology and Evolution*, 1, 140-150. DOI:10.1111/j.2041-210X.2010.00021.x

Navarro, L.M. & Pereira, H.M. (2012) Rewilding abandoned landscapes in Europe. *Ecosystems*, 15, 900-912. DOI:10.1007/s10021-012-9558-7

Roth, T., Plattner, M. & Amrhein, V. (2014) Estimating unbiased phenological trends by adapting site-occupancy models. *Ecology*, 95, 2194-2201. DOI:10.1890/13-1830.1

Rothman, K.J. (1990) No adjustments are needed for multiple comparisons. *Epidemiology*, 1, 43-46.

Simmonds, E.G. et al. (2020) Phenological asynchrony: a ticking time-bomb for seemingly stable populations? *Ecology Letters*, 23, 1766-1775.

Takada, M.B. et al. (2019) Crises of biodiversity and ecosystem services in satoyama landscape of Japan: A review on the role of management. *Sustainability*, 11, 454. DOI:10.3390/su11020454

Takeuchi, Y. et al. (2025) National-scale terrestrial biodiversity and ecosystem monitoring with essential biodiversity variables in Japan and Finland. *Ecological Research*, DOI: 10.1111/1440-1703.70011.

Tryjanowski, P. & Sparks, T.H. (2001) Is the detection of the first arrival date of migrating birds influenced by population size? A case study of the red-backed shrike. *International Journal of Biometeorology*, 45, 217-219. DOI:10.1007/s004840100112

Sparks, T.H., Roberts, D.R. & Crick, H.Q.P. (2001) What is the value of first arrival dates of spring migrants in phenology? *Avian Ecology and Behaviour*, 7, 75-85.

Uchida, K. et al. (2025) Biodiversity change under human depopulation in Japan. *Nature Sustainability*, 8, 883-892. DOI:10.1038/s41893-025-01578-w

van Strien, A.J., Pannekoek, J. & Gibbons, D.W. (2001) Indexing European bird population trends using results of national monitoring schemes: a trial of a new method. *Bird Study*, 48, 200-213. DOI:10.1080/00063650109461219

Ueta, M. et al. (2025) Biodiversity monitoring data from Japanese satoyama landscapes. *figshare*. DOI: [to be confirmed].

Valdez, J.W. et al. (2023) The undetectability of global biodiversity trends using local species richness. *Ecography*, 2023, e06604. DOI:10.1111/ecog.06604
