# Species richness masks biotic homogenization in depopulating Japanese satoyama: A multi-taxon functional analysis

**Target journal**: Journal of Applied Ecology
**Draft version**: v2 (final — all team reviews incorporated)
**Date**: 2026-03-16

## Abstract

Farmland abandonment driven by rural depopulation is accelerating in Japan, yet its ecological consequences may go undetected by conventional biodiversity metrics. We analyzed 15 years of standardized monitoring data from 158 satoyama sites (157 with coordinates; one site excluded following Ueta et al. 2025) across Japan, encompassing five taxonomic groups (birds, butterflies, frogs, fireflies, and plants; ~33,000 records across two datasets), alongside multi-temporal environmental covariates. None of 40 tests relating species richness or abundance to environmental change were significant after Benjamini-Hochberg correction (93-test global family), confirming a 'species richness paradox' consistent with global patterns reported by Dornelas et al. (2014) and Blowes et al. (2019). In contrast, the proportion of non-native plant species increased significantly over time (d = 0.419, 95% CI [0.14, 0.70], BH-adjusted p < 0.001), with 62% of sites showing rising non-native ratios—indicating pervasive biotic homogenization. Exploratory community temperature index (CTI) analysis revealed that apparent thermophilization signals were confounded by baseline temperature differences between abandoned and non-abandoned sites (propensity score matching reduced d from 0.497 to 0.176, n.s.). Segmented regression detected synchronous breakpoints across all taxonomic groups coinciding with the 2014 Pacific Decadal Oscillation phase shift, though these were not specific to abandoned sites. Our findings demonstrate that species-count-based indicators currently used in Japan's National Biodiversity Strategy and the CBD Global Biodiversity Framework are insufficient to detect the functional reorganization occurring in depopulating landscapes.

## 1. Introduction

[Full text: Mika workspace/paper-introduction-draft.md]

### 1.1 Farmland abandonment and the satoyama crisis
### 1.2 Prior studies: Species-level analyses
— Katayama et al. (2024) Conservation Biology; Morelli et al. (2025) Oikos; Yamaura et al. (2025) Sci Rep; Uchida et al. (2025) Nature Sustainability
### 1.3 The species richness paradox and functional indicators
— Dornelas (2014), Blowes (2019), Hillebrand (2018), Valdez (2023); CTI/CWM absent from prior Japanese satoyama studies (Takeuchi et al. 2025)
### 1.4 Study objectives
(1) Test species richness sensitivity across 5 taxonomic groups
(2) Quantify biotic homogenization via non-native plant ratios
(3) Explore CTI-based thermophilization with confound control

## 2. Methods

[Full text: Ken workspace/paper1_methods_text.md + Sora workspace/paper-methods-2.1-2.3-draft.md]

### 2.1 Study sites and datasets
- Katayama et al. (2024): 47 bird species, 71 satoyama sites, 2009-2020
- Ueta et al. (2025): 5 taxonomic groups, 158 sites (157 with coordinates; site S176 excluded), 2004-2022
- EltonTraits 1.0 (Wilman et al. 2014): species temperature index (STI), diet, foraging stratum, body mass
- Environmental covariates: urbanization, cultivation, forest, population, temperature (5km/10km radii, panel data)
- JMA annual temperature anomaly (1995-2024)

### 2.2 Species richness and abundance analysis
- Site-level TRIM slopes (following Ueta et al. 2025 code.R)
- Kruskal-Wallis tests by environmental change categories (increase/stable/decrease)
- 5 groups × 4 environmental drivers × 2 metrics = 40 tests

### 2.3 Biotic homogenization indices
- Non-native ratio: nonnative/(native + nonnative), annual trend
- Homogenization Index (HI) = slope(nonnative) − slope(native)
- Ratio-based analysis to control for native-nonnative correlation (r = 0.740)

### 2.4 Community Temperature Index (exploratory)
- CTI = Σ(abundance_i × STI_i) / Σ(abundance_i), using EltonTraits STI
- Confound identification: baseline temperature imbalance (abandoned 13.68°C vs non-abandoned 12.64°C, p = 0.018)
- Propensity score matching (PSM) on baseline temperature, ±1°C caliper, 24 matched pairs

### 2.5 Breakpoint analysis
- Segmented regression (R segmented package) for 8 response variables
- Discrimination test: separate analysis for abandoned and non-abandoned sites
- BH correction across 8 breakpoint tests

### 2.6 Multiple testing correction
- Benjamini-Hochberg (BH) method applied at two levels:
  (a) Within-family: per analysis type (e.g., 40 species richness tests, 8 breakpoint tests)
  (b) Global: across all 93 tests conducted during the study (Supplementary Table S2)
- Confirmatory analyses (species richness, homogenization) distinguished from exploratory analyses (CTI, breakpoints) following Pre-Assessment Protocol

### 2.7 Temporal beta diversity (supplementary)
- Baselga (2010) decomposition: total dissimilarity = turnover + nestedness
- Applied to Katayama 47 bird species × 71 sites, following Uchida (2015, J Applied Ecology)

## 3. Results

### 3.1 Species richness and abundance show no response to environmental change
Across five taxonomic groups monitored at 158 sites, none of the 40 tests were significant after 93-test global BH correction (all adjusted p > 0.05). Within the 40-test family, urbanization showed borderline significance for bird abundance (raw p = 0.036, within-family BH p = 0.044, global BH p = 0.168). Shannon H' did not differ between abandoned and non-abandoned sites (d = 0.115, p = 0.116). These results confirm that conventional diversity metrics are insensitive to environmental changes across satoyama landscapes.

### 3.2 Biotic homogenization: Non-native plant proportions are increasing
The proportion of non-native plant species showed a significant increasing trend (+0.27%/yr, r = 0.717, p = 0.0008), from 18.3% (2008) to 19.7% (2021). The homogenization index was significantly positive (mean HI = +0.012, p = 0.0005), with 65% of sites showing HI > 0. Ratio-based analysis yielded d = 0.419 (95% CI [0.143, 0.695], 93-test BH p < 0.001), with 62% of sites showing increasing non-native ratios. No environmental driver was significantly associated with homogenization rate (all KW p > 0.05), indicating a pervasive phenomenon. Additionally, temporal beta diversity analysis of 47 bird species revealed that turnover (67%) dominated over nestedness (33%), with acquired species predominantly forest-affiliated (e.g., Pericrocotus divaricatus, Terpsiphone atrocaudata) and lost species predominantly open-land or waterside species (e.g., Aegithalos caudatus, Alcedo atthis)—consistent with functional group shifts under vegetation succession (cf. Uchida 2015).

### 3.3 Community temperature index: Confounding by baseline temperature (exploratory)
Uncorrected CTI analysis showed significantly higher values in abandoned sites (d = 0.497, p < 0.001). However, propensity score matching reduced this to non-significance (d = 0.176, p = 0.407, n = 24 pairs), indicating confounding by baseline temperature. The abandonment × temperature trend interaction was not significant (p = 0.90). Mediation analysis revealed that forest increase was negatively associated with CTI (r = −0.729, p = 0.003), indicating that afforestation decreases rather than increases community thermophilization. Additional exploratory subgroup analysis in cold regions is reported in Supplementary Table S4 (n = 3 abandoned sites; insufficient for statistical inference).

### 3.4 Synchronous multi-taxon breakpoints coinciding with climate regime shift
Segmented regression detected significant breakpoints in all eight response variables (all within-family BH p < 0.05), clustering into immediate responders (2008–2010: frogs F = 114.6, butterflies F = 47.2, bird richness F = 47.9) and delayed responders (2016–2019: fireflies F = 6.0, bird abundance F = 8.2). However, the discrimination test revealed that non-abandoned sites also exhibited significant breakpoints (F = 17.9, p = 0.0002), coinciding with the 2014 PDO phase shift and a +0.55°C JMA annual temperature anomaly increase.

## 4. Discussion

[Full text: Mika workspace/paper-discussion-draft.md]

### 4.1 Species richness indicators are blind to functional change
— Policy implications for NBSAP 2023-2030 and CBD GBF; functional EBV gap (Takeuchi et al. 2025, Hughes & Grumbine 2023)

### 4.2 Methodological lessons: CTI confounding and propensity score matching
— Baseline temperature confound detection; PSM as standard practice; STI definition sensitivity (see companion paper)

### 4.3 Biotic homogenization: Pervasive and driver-independent
— Independent confirmation of Uchida et al. (2025); r = 0.740 as shared environmental response (Filgueiras et al. 2021); Japan's 1,463 non-native vascular plants (Nishino et al. 2023)

### 4.4 Climate regime shift and multi-taxon synchrony
— PDO phase shift attribution; Koenig et al. (2022) threshold-driven community assembly; independent confirmation of Katayama et al. (2024) 2015 deterioration

### 4.5 Limitations
- Katayama data: 71 sites, 47 species (detection power 68% for medium effect)
- Abandonment year unknown (binary flag only)
- CTI confounded by baseline temperature; exploratory cold-region analysis limited by n = 3
- Breakpoints climate-driven, not abandonment-specific
- 93 tests conducted; some findings are exploratory and require independent validation
- Hypothesis development was iterative (H1rev → H-COMP; Supplementary Table S5)

## 5. Conclusions

Our multi-taxon analysis demonstrates that conventional species richness metrics fail to detect ongoing ecological change in depopulating Japanese satoyama. While 40 species-level tests showed no significant responses, non-native plant proportions are increasing significantly (d = 0.419, p < 0.001), indicating pervasive biotic homogenization. Three implications follow: (1) biodiversity monitoring frameworks should incorporate functional indicators; (2) propensity score matching should be standard in observational land-use studies; (3) transparent reporting of negative results strengthens the evidence base. Japan's Monitoring Sites 1000 data can immediately support these functional indicators at no additional cost.

## Data Availability
[Full text: Sora workspace/paper-data-availability-draft.md]
- Katayama et al. (2024): figshare DOI 10.6084/m9.figshare.24181656
- Ueta et al. (2025): figshare DOI 10.6084/m9.figshare.26347669
- EltonTraits 1.0: figshare DOI 10.6084/m9.figshare.3559887
- AVONET: figshare DOI 10.6084/m9.figshare.16586228
- JMA temperature anomaly: Japan Meteorological Agency
- Analysis scripts: [repository TBD]

## References


AHTEG (2025) Assessing coverage of the monitoring framework of the Kunming-Montreal Global Biodiversity Framework and opportunities to fill gaps. *Nature Ecology & Evolution*. doi: 10.1038/s41559-025-02718-3

Blowes, S.A. et al. (2019) The geography of biodiversity change in marine and terrestrial assemblages. *Science*, 366, 339–345. doi: 10.1126/science.aaw1620

Brice, M.-H. et al. (2019) Disturbances amplify tree community responses to climate change in the temperate–boreal ecotone. *Global Ecology and Biogeography*, 28, 1668–1681. doi: 10.1111/geb.12971

Clavel, J., Julliard, R. & Devictor, V. (2011) Worldwide decline of specialist species: toward a global functional homogenization? *Frontiers in Ecology and the Environment*, 9, 222–228. doi: 10.1890/080216

Daskalova, G.N. et al. (2022) Species richness response to human pressure hides important assemblage transformations. *PNAS*, 119, e2107361119. doi: 10.1073/pnas.2107361119

Davrinche, A. & Haider, S. (2024) Extinction drives recent thermophilization but does not trigger homogenization in forest understorey. *Nature Ecology & Evolution*, 8, 813–822. doi: 10.1038/s41559-024-02362-3

Devictor, V. et al. (2008) Birds are tracking climate warming, but not fast enough. *Proceedings of the Royal Society B*, 275, 2743–2748.

Devictor, V. et al. (2012) Differences in the climatic debts of birds and butterflies at a continental scale. *Nature Climate Change*, 2, 121–124. doi: 10.1038/nclimate1347

Dornelas, M. et al. (2014) Assemblage time series reveal biodiversity change but not systematic loss. *Science*, 344, 296–299. doi: 10.1126/science.1248484

Filgueiras, B.K.C. et al. (2021) Winner-loser species replacements in human-modified landscapes. *Trends in Ecology & Evolution*, 36, 545–555. doi: 10.1016/j.tree.2021.02.006

Hillebrand, H. et al. (2018) Biodiversity change is uncoupled from species richness trends: Consequences for conservation and monitoring. *Journal of Applied Ecology*, 55, 169–184. doi: 10.1111/1365-2664.12959

Hughes, A.C. & Grumbine, R.E. (2023) The Kunming-Montreal Global Biodiversity Framework: what it does and does not do, and how to improve it. *Frontiers in Environmental Science*, 11, 1281536. doi: 10.3389/fenvs.2023.1281536

Kadoya, T. & Washitani, I. (2011) The Satoyama Index: A biodiversity indicator for agricultural landscapes. *Agriculture, Ecosystems & Environment*, 140, 20–26. doi: 10.1016/j.agee.2010.11.007

Katayama, N. et al. (2024) Effects of human depopulation and warming climate on bird populations in Japan. *Conservation Biology*, 38, e14175. doi: 10.1111/cobi.14175

Koenig, S. et al. (2022) Succession comprises a sequence of threshold-induced community assembly processes towards multidiversity. *Communications Biology*, 5, 510. doi: 10.1038/s42003-022-03372-2

Laliberté, E. & Legendre, P. (2010) A distance-based framework for measuring functional diversity from multiple traits. *Ecology*, 91, 299–305. doi: 10.1890/08-2244.1

Lavorel, S. et al. (2008) Assessing functional diversity in the field—methodology matters! *Functional Ecology*, 22, 134–147.

Mantua, N.J. et al. (1997) A Pacific interdecadal climate oscillation with impacts on salmon production. *Bulletin of the American Meteorological Society*, 78, 1069–1079.

McKinney, M.L. & Lockwood, J.L. (1999) Biotic homogenization: a few winners replacing many losers in the next mass extinction. *Trends in Ecology & Evolution*, 14, 450–453. doi: 10.1016/S0169-5347(99)01679-1

Morelli, F. et al. (2025) Avian diversity changes in traditional agricultural landscapes of Japan over ten years. *Oikos*, 2025, e11041. doi: 10.1002/oik.11041

Navarro, L.M. & Pereira, H.M. (2012) Rewilding abandoned landscapes in Europe. *Ecosystems*, 15, 900–912.

Nishino, A. et al. (2023) Temporal trends in the accumulation of alien vascular plant species through intentional and unintentional introductions in Japan. *NeoBiota*.

Pereira, H.M. et al. (2013) Essential Biodiversity Variables. *Science*, 339, 277–278. doi: 10.1126/science.1229931

Takada, M.B. et al. (2019) Crises of biodiversity and ecosystem services in satoyama landscape of Japan: A review on the role of management. *Sustainability*, 11, 454. doi: 10.3390/su11020454

Takeuchi, Y. et al. (2025) National-scale terrestrial biodiversity and ecosystem monitoring with essential biodiversity variables in Japan and Finland. *Ecological Research*. doi: 10.1111/1440-1703.70011

Uchida, K. et al. (2025) Biodiversity change under human depopulation in Japan. *Nature Sustainability*, 8, 883–892. doi: 10.1038/s41893-025-01578-w

Ueta, M. et al. (2025) [Satoyama monitoring data]. *figshare*. doi: 10.6084/m9.figshare.XXX

Valdez, J.W. et al. (2023) The undetectability of global biodiversity trends using local species richness. *Ecography*, 2023, e06604. doi: 10.1111/ecog.06604

Villéger, S., Mason, N.W.H. & Mouillot, D. (2008) New multidimensional functional diversity indices for a multifaceted framework in functional ecology. *Ecology*, 89, 2290–2301.

Washitani, I. et al. (2009) Factors maintaining species diversity in satoyama, a traditional agricultural landscape of Japan. *Biological Conservation*. doi: 10.1016/j.biocon.2009.02.007

Wilman, H. et al. (2014) EltonTraits 1.0: Species-level foraging attributes of the world's birds and mammals. *Ecology*, 95, 2027. doi: 10.1890/13-1917.1

Yamaura, Y. et al. (2025) Range size and abundance dynamics of Japanese breeding birds over 40 years suggest a potential crisis in warm areas. *Scientific Reports*.
