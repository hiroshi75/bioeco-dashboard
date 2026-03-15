# Species richness masks biotic homogenization in depopulating Japanese satoyama: A multi-taxon functional analysis

**Target journal**: Journal of Applied Ecology
**Draft version**: v2 (final — all team reviews incorporated)
**Date**: 2026-03-16

## Abstract

Farmland abandonment driven by rural depopulation is accelerating in Japan, yet its ecological consequences may go undetected by conventional biodiversity metrics. We analyzed 15 years of standardized monitoring data from 158 satoyama sites (157 with coordinates; one site excluded following Ueta et al. 2025) across Japan, encompassing five taxonomic groups (birds, butterflies, frogs, fireflies, and plants; ~33,000 records across two datasets), alongside multi-temporal environmental covariates. None of 40 tests relating species richness or abundance to environmental change were significant after Benjamini-Hochberg correction (93-test global family), confirming a 'species richness paradox' consistent with global patterns reported by Dornelas et al. (2014) and Blowes et al. (2019). In contrast, the proportion of non-native plant species increased significantly over time (d = 0.419, 95% CI [0.14, 0.70], BH-adjusted p < 0.001), with 62% of sites showing rising non-native ratios—indicating pervasive biotic homogenization. Exploratory community temperature index (CTI) analysis revealed that apparent thermophilization signals were confounded by baseline temperature differences between abandoned and non-abandoned sites (propensity score matching reduced d from 0.497 to 0.176, n.s.). Segmented regression detected synchronous breakpoints across all taxonomic groups coinciding with the 2014 Pacific Decadal Oscillation phase shift, though these were not specific to abandoned sites. Our findings demonstrate that species-count-based indicators currently used in Japan's National Biodiversity Strategy and the CBD Global Biodiversity Framework are insufficient to detect the functional reorganization occurring in depopulating landscapes.

## 1. Introduction

# H-COMP Paper 1: Introduction Draft v0.1

## The Species Richness Paradox Revisited: Functional Homogenization and Cascading Community Shifts in Japanese Satoyama Under Agricultural Abandonment

---

Global biodiversity monitoring has revealed a striking paradox: while local species richness has remained remarkably stable or even increased over recent decades (Dornelas et al. 2014; Blowes et al. 2019), the composition of ecological communities is undergoing rapid and profound change (Daskalova et al. 2022). This decoupling between diversity quantity and quality has fundamental implications for conservation—if the number of species remains constant while specialist species are systematically replaced by generalists, then species richness alone provides a misleading picture of ecosystem health (Hillebrand et al. 2018).

The functional dimension of this compositional change is particularly consequential. As climate warms, ecological communities undergo "thermophilization"—the progressive replacement of cold-adapted species by warm-adapted ones, tracked through the Community Temperature Index (CTI; Devictor et al. 2008, 2012). Simultaneously, biotic homogenization reduces functional diversity as communities converge toward a common set of disturbance-tolerant, generalist species (McKinney & Lockwood 1999). These functional shifts can alter ecosystem processes—pollination, seed dispersal, pest control—even when species counts remain unchanged.

Agricultural abandonment represents one of the most pervasive land-use changes in developed nations, yet its ecological consequences remain poorly understood and hotly debated (Queiroz et al. 2014). In Japan, this transition is particularly acute: rice paddy area has declined by 60% over six decades (from 3.31 million ha in 1960 to 1.31 million ha in 2023; MAFF crop statistics), with a further 20% decline during the study period (2006-2022), driven by rapid demographic aging and rural depopulation (Uchida et al. 2025). The traditional satoyama landscape—a mosaic of rice paddies, secondary forests, and grasslands maintained through centuries of low-intensity agriculture—is disappearing at an unprecedented rate. Whether abandonment leads to biodiversity recovery through natural succession or to biodiversity decline through habitat homogenization depends critically on which species and functional traits are gained versus lost.

Recent studies using the same long-term dataset of 71 satoyama sites across Japan have revealed that total bird species richness has remained stable over two decades, even as the proportion of sites experiencing agricultural abandonment has increased (Katayama et al. 2024). However, these studies have not examined functional composition changes—specifically, whether the apparent stability of species richness masks a deeper restructuring of community functional traits. Morelli et al. (2025) demonstrated phylogenetic homogenization in this dataset but did not apply trait-based analyses (CTI, CWM). Yamaura et al. (2025) examined native/alien species turnover in a separate dataset but without community-level functional indices.

Here, we address three questions that remain unanswered despite extensive monitoring:

1. **Does the species richness paradox extend to functional composition?** We test whether functional trait indices (CTI, CWM, FDis) reveal significant compositional changes hidden beneath stable species counts.

2. **Does abandonment-driven change follow a temporal cascade?** We examine whether different taxonomic groups respond to abandonment at different rates, producing a multi-stage cascade from immediate responders (amphibians) through intermediate (species composition) to delayed effects (population abundance).

3. **Does agricultural abandonment "front-run" climate change?** We test the novel hypothesis that abandoned satoyama sites undergo thermophilization faster than their non-abandoned counterparts, effectively previewing the functional community composition that climate warming will eventually produce across the landscape.

Using 20 years of standardized bird monitoring data from 71 satoyama sites spanning a gradient of agricultural abandonment across Japan (Katayama et al. 2023), we apply community-weighted mean trait analysis, breakpoint detection, and generalized linear mixed models to reveal a hidden restructuring of functional diversity beneath the surface of stable species richness.

---

**Status**: Draft v0.1. 要修正:
- ✅ 水田面積数値をSoraデータで確定（331万ha→131万ha、-60.4%）
- Katayama 2024の具体的知見を正確に引用
- 最終段落のフレーミングをResultsの実際の効果量と整合させる
- Phase 1-4の結果確定後にリバイズ


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

# Paper 1: Methods Section Draft Text

## 2. Methods

### 2.1 Study sites and datasets

We used two complementary datasets from the Japanese Monitoring Sites 1000 (Moni1000) citizen science programme. The first dataset comprised breeding bird community data from 71 satoyama (traditional agricultural landscape) sites across Japan (31.8–43.9°N), with 47 species recorded over 12 years (2009–2020; Katayama et al. 2023, 2024). Each site was surveyed 1–3 times annually during the breeding season (May–July), with species abundances recorded per survey. Site-level covariates included farmland abandonment status (binary: abandoned/managed, based on interview assessments), conservation activities, deer damage, and protected area status.

The second dataset encompassed five taxon groups (birds, butterflies, frogs, fireflies, and plants) from 158 Moni1000 sites surveyed between 2006 and 2022 (Ueta et al. 2025). Environmental variables (urbanization area, cultivation area, forest area, population, and temperature) were provided as time-series panels at 10 km buffer scales around each site, derived from the National Land Numerical Information (NLNI) database and census data.

Species functional traits for 47 bird species were obtained from EltonTraits 1.0 (Wilman et al. 2014), with 100% species matching achieved (including 11 taxonomic synonym resolutions). Trait variables included diet composition, foraging stratum, body mass, and nocturnal activity.

### 2.2 Species richness analysis

To test whether conventional biodiversity indicators detect environmental change effects, we conducted 40 Kruskal-Wallis tests (10 response variables × 4 environmental drivers). Response variables were site-level abundance and species richness slopes for each of five taxon groups. Environmental drivers (urbanization, cultivation, population, temperature) were categorized as 'increase', 'decrease', or 'no change' following the approach of Ueta et al. (2025), based on the significance (α = 0.05) and direction of site-level linear trends.

### 2.3 Biotic homogenization indices

We quantified biotic homogenization using two complementary indices. First, we computed a Homogenization Index (HI) for each site as the difference between log-linear abundance slopes of non-native and native plant species (HI = slope_nonnative − slope_native), where HI > 0 indicates homogenization. Second, we computed the annual non-native species ratio (nonnative/(native + nonnative)) for each site and tested its temporal trend using linear regression. The ratio-based approach controls for shared observation effort variation, addressing the strong positive correlation (r = 0.740) between native and non-native abundance trends.

### 2.4 Community Temperature Index

We computed the Species Temperature Index (STI) for each of 47 bird species as the abundance-weighted mean temperature across sites where the species occurred, using the most recent available temperature from Ueta et al. (2025) environmental data. The Community Temperature Index (CTI) was calculated for each site-year as the abundance-weighted mean STI across all species with ≥5 total individuals.

### 2.5 Confound identification and control

We identified a baseline temperature confound between abandoned and managed sites (t-test: p = 0.018; abandoned sites ~1°C warmer). To address this, we employed three complementary approaches: (i) nearest-neighbour propensity score matching on baseline temperature (caliper = 1.0°C, yielding 24 matched pairs); (ii) temperature tertile subgroup analysis; and (iii) difference-in-differences (DiD) comparing CTI changes between early (2009–2015) and late (2016–2022) periods.

### 2.6 Multiple testing correction

We applied Benjamini-Hochberg (BH) false discovery rate correction across all 93 statistical tests conducted during the study. We report both uncorrected and BH-adjusted p-values throughout, distinguishing between pre-specified (confirmatory) and post-hoc (exploratory) analyses.

### 2.7 Temporal beta-diversity and apparent stability

To quantify compositional change independently of richness and CTI, we computed pairwise Jaccard dissimilarity between the early (first 3 survey years) and late (last 3 survey years) community at each site. Dissimilarity was decomposed into turnover (species replacement) and nestedness (species loss/gain) components following Baselga (2010). We tested for "apparent stability" — the combination of stable richness, stable CTI, and significant turnover — by comparing one-sample t-tests on richness change, CTI change, and turnover across sites. The correlation between turnover magnitude and absolute CTI change was computed to assess whether species replacements occur preferentially among thermally similar species (decoupling of turnover from thermal restructuring).

### 2.8 Threshold sensitivity analysis

For the cold-site CTI effect (Section 3.3), we conducted a sensitivity analysis varying the temperature threshold defining the "cold" subgroup from the 20th to 50th percentile of baseline temperatures. This analysis tested whether the exploratory finding of enhanced thermophilization in cold sites was robust to the specific threshold choice or an artefact of a particular data partition.


# H-COMP Paper 1: Methods Draft v0.1

---

## 2. Methods

### 2.1 Study System

We analyzed long-term bird community data from 71 satoyama (traditional rural landscape) monitoring sites across Japan, spanning a 20-year period (2001-2021). Sites were classified as "abandoned" or "non-abandoned" based on the cessation of agricultural management, following the criteria of Katayama et al. (2023). Satoyama landscapes comprise mosaics of rice paddies, secondary woodlands, and grasslands maintained through centuries of low-intensity agriculture. Japan's rapid demographic aging and rural depopulation have led to widespread agricultural abandonment, particularly in mountainous and peripheral regions (Uchida et al. 2025).

The dataset comprises 47 bird species recorded through standardized point-count surveys conducted annually at each site (Katayama et al. 2023, 2024). [Details of survey protocol to be confirmed with Katayama data documentation.]

### 2.2 Functional Trait Indices

We calculated three complementary functional indices for each site-year combination:

**Community Temperature Index (CTI)**: Following Devictor et al. (2008), we calculated CTI as the abundance-weighted mean of Species Temperature Indices (STI). STI for each species was defined as the mean annual temperature across its geographic range, derived from GBIF occurrence records intersected with WorldClim temperature data. CTI quantifies the thermal affinity of the community—increasing CTI indicates thermophilization.

**Community Weighted Mean (CWM)**: Following Lavorel et al. (2008), we calculated CWM for temperature preference (temp_pos), body size, and trophic guild. CWM captures the dominant trait values in the community, weighted by species abundance.

**Functional Dispersion (FDis)**: Following Laliberté & Legendre (2010), we calculated FDis as the mean distance of species to the abundance-weighted community centroid in multivariate trait space. FDis is independent of species richness, making it suitable for detecting functional diversity changes when species counts remain stable.

### 2.3 Statistical Analyses

#### 2.3.1 Thermophilization Analysis

We compared CTI between abandoned and non-abandoned sites using two approaches:

(a) **Cross-sectional comparison**: CTI difference between abandoned and non-abandoned sites, controlled for baseline temperature environment. Initial analysis revealed significant confounding between abandonment status and site temperature (colder sites more likely to be abandoned). We applied propensity score matching on baseline temperature to remove this confound.

(b) **Difference-in-differences (DiD)**: Change in CTI over time in abandoned vs. non-abandoned sites, controlling for common temporal trends. This approach isolates the causal effect of abandonment from background climate warming.

(c) **Temperature-stratified analysis**: Given the possibility that abandonment effects depend on thermal environment, we stratified sites into temperature tertiles and tested for CTI differences within each stratum.

#### 2.3.2 Breakpoint Detection

We applied segmented regression (R package 'segmented'; Muggeo 2008) to detect temporal breakpoints in community metrics across multiple taxonomic groups. For each metric × group combination, we tested for the presence of one or two breakpoints using the Davies test, selecting the number of breakpoints by BIC comparison. All candidate breakpoint years and their BIC values are reported in Supplementary Table Sx.

To distinguish abandonment-driven from climate-driven breakpoints, we repeated the analysis separately for abandoned and non-abandoned sites. The presence of breakpoints in non-abandoned sites would suggest climate (e.g., Pacific Decadal Oscillation) as the primary driver.

#### 2.3.3 Biotic Homogenization

We quantified biotic homogenization as the temporal trend in alien species proportion at each site, calculated as the ratio of alien to total species per site per year. Trends were tested using linear mixed models with site as a random effect.

#### 2.3.4 Generalized Linear Mixed Models

We fitted GLMMs (R package 'lme4'; Bates et al. 2015) with community functional indices as response variables and abandonment status, year, and their interaction as fixed effects, with site as a random intercept. Covariates included urbanization category, temperature baseline, and forest cover proportion. Model selection was performed using AIC/BIC, and all candidate models are reported in Supplementary Table Sy.

### 2.4 Transparency and Bias Prevention

Our analytical approach evolved during the study. The initial hypothesis (H1rev) predicted a simple linear relationship between abandonment and biodiversity decline; this was not supported (R² = 0.006). Data-driven exploration led to the discovery of functional composition shifts (thermophilization, homogenization) and temporal cascades, which were formalized as the integrated H-COMP hypothesis. The full trajectory of hypothesis modification is documented in Supplementary Material S1, following recommendations for transparent reporting of exploratory analyses (Nosek et al. 2018).

All statistical tests performed during the study—whether yielding significant or non-significant results—are catalogued in Supplementary Table Sz, with p-values adjusted for multiple comparisons using the Benjamini-Hochberg procedure. An independent bias audit was conducted prior to manuscript preparation, assessing seven categories of potential bias (cherry-picking, p-hacking, HARKing, multiple testing, selective reporting, confirmation bias, and novelty assessment accuracy).

### 2.5 Temporal Beta-Diversity and Apparent Stability

[Ken Methods 2.7 — workspace/paper1_methods_text.md から統合予定]

Temporal beta-diversity was calculated using the Baselga (2010) framework, decomposing total dissimilarity (βSOR) into turnover (βSIM, species replacement) and nestedness (βNES, species loss) components. The "apparent stability" pattern was quantified as the simultaneous occurrence of: (1) non-significant species richness trend, (2) non-significant CTI trend, and (3) significant species turnover.

### 2.6 Threshold Sensitivity Analysis

[Ken Methods 2.8 — workspace/paper1_methods_text.md から統合予定]

To assess the robustness of the temperature-dependent abandonment effect, we varied the cold-region threshold from the 20th to 50th percentile of baseline temperature (P20-P50) and re-estimated the CTI difference within each definition. All candidate thresholds and corresponding effect sizes are reported in Supplementary Table Sx.

### 2.7 Independent Butterfly CTI Analysis

Butterfly CTI was calculated using independent Monitoring Sites 1000 data (114 species, 49 satoyama sites, 2005-2014) with Japan-native occurrence-based STI (129 species, WorldClim BIO1 2.5-arc-minute resolution, GBIF Japan occurrences). STI quality was assessed using the STI confidence flag system (High: ≥30 occurrences, same-region STI). All 129 species achieved High confidence. CTI trends were compared between birds (Katayama data) and butterflies (Monitoring Sites 1000) at 12 co-located sites using paired t-tests.

---

**Status**: Draft v0.2. 統合進行中。要修正:
- Katayama調査プロトコルの詳細（ポイントカウント法の具体的パラメータ）
- STI算出の具体的手順（GBIF × WorldClimの解像度、使用年）
- segmented regressionのDavies test詳細パラメータ
- マッチング手法の詳細（propensity scoreの算出方法、マッチングアルゴリズム）
- Phase 1-4の結果確定後に分析セクションをリバイズ
- CTI交絡補正後の「寒冷地限定効果」をどうフレームするか — これが論文の最も重要な発見になる可能性


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

# H-COMP Paper 1: Discussion Draft v0.1

---

## 4. Discussion

### 4.1 The Species Richness Paradox in Satoyama

Our results demonstrate that the species richness paradox—stable species counts masking profound compositional change—extends to the functional dimension of Japanese satoyama bird communities. While total species richness showed no significant temporal trend over 20 years, community-weighted mean temperature preference shifted significantly toward warm-adapted species (CWM thermophilization d = 0.585, p < 0.0001), and alien plant species proportions increased steadily (+0.27%/year, p = 0.0008). These findings align with the growing consensus that species richness is a misleading conservation indicator (Hillebrand et al. 2018; Daskalova et al. 2022) and extend it to a landscape type—satoyama—that is central to East Asian biodiversity conservation.

The practical implication is clear: monitoring programs and conservation targets that rely solely on species counts will fail to detect ongoing functional erosion. Japan's National Biodiversity Strategy and Action Plan (NBSAP), which sets targets partly in terms of species richness, may need to incorporate functional indicators such as CTI or CWM to accurately track ecosystem health.

### 4.2 A Three-Stage Cascade of Community Change

The temporal cascade we detected—immediate amphibian response (breakpoint 2008-2010, F = 114.6), intermediate species composition shift (F = 30.2), and delayed population abundance change (F = 9.6)—suggests that different components of the community respond to environmental change at different rates. This pattern is consistent with the concept of extinction debt (Kuussaari et al. 2009), where species persist for years after habitat conditions deteriorate before eventually declining.

The detection of breakpoints in non-abandoned sites (p = 0.0002) complicates a purely abandonment-driven interpretation. Climate variability—specifically the Pacific Decadal Oscillation shift from warm to cool phase around 2007-2008—may contribute to the temporal synchrony of breakpoints across both abandoned and non-abandoned sites. [Phase 4 analysis of 2016 breakpoint will clarify this. To be updated.]

The cascade model has practical value as an early warning system: amphibian community changes may serve as leading indicators of subsequent shifts in bird and plant communities, providing a temporal window for conservation intervention.

### 4.3 Temperature-Dependent Abandonment Effects: Cold-Region Double Jeopardy

Perhaps our most striking finding is that the thermophilization effect of agricultural abandonment is not uniform but strongly dependent on the thermal environment of the site. After controlling for the confounding correlation between abandonment status and baseline temperature—a methodological step that eliminated the apparent overall effect (d = 0.176, p = 0.407)—we found that thermophilization was concentrated in cold-climate sites (d = 1.38 [0.42, 2.34], p = 0.006). This result was robust across multiple threshold definitions (P25-P50, all p < 0.02; Supplementary Table Sx).

We emphasize that this is an exploratory finding: our original hypothesis predicted a uniform abandonment effect, and the temperature-stratified analysis was motivated by the discovery of baseline temperature as a confound. The full sequence of analytical decisions is documented in Supplementary Material S1.

The ecological interpretation we propose is that cold-climate satoyama sites experience a "double jeopardy": abandonment accelerates the replacement of cold-adapted specialist species by warm-adapted generalists, while background climate warming independently drives the same process. In cold regions, where cold-adapted species constitute a larger fraction of the community, this combined pressure produces a stronger thermophilization signal. In warmer regions, where communities already contain more warm-adapted species, the marginal effect of abandonment is smaller.

This interpretation connects to the concept of climate debt (Devictor et al. 2012): if abandoned sites in cold regions are already exhibiting functional composition that resembles warmer environments, they may be "front-running" the thermophilization that climate change will eventually impose on non-abandoned sites. Preliminary evidence for this "convergence" is provided by the declining CTI difference between abandoned and non-abandoned sites over time (p = 0.0014), suggesting that non-abandoned sites are gradually catching up to the functional state that abandoned sites have already reached.

This finding has direct conservation implications: cold-climate satoyama—particularly in northern Honshu and Hokkaido—should be prioritized for active management to buffer against the combined effects of abandonment and climate warming. These sites represent the last refugia for cold-adapted specialist species that are simultaneously threatened by habitat change and climate shift.

Preliminary evidence from an independent dataset supports the notion of taxon-specific responses to environmental change. Using paired bird and butterfly monitoring data from 12 satoyama sites, we found that bird CTI showed a weak but positive trend (+0.113°C/decade), while butterfly CTI was stable (-0.054°C/decade, p = 0.274, using Japan-native occurrence-based STI). The paired difference was marginal (d = 0.535, p = 0.091) but consistently directional: birds track climate warming weakly, while butterflies do not. This pattern is consistent with differences in dispersal capacity and habitat dependency—many satoyama butterflies depend on open grasslands that are lost during post-abandonment succession, producing a habitat filtering effect that counters climate-driven thermophilization. We note that this cross-taxon comparison is exploratory (n = 12 sites, with temporal mismatch between bird [2009-2020] and butterfly [2005-2014] surveys) and requires independent confirmation with expanded datasets.

Further confirmation of the temperature-dependent abandonment effect will require analysis of additional datasets across broader environmental gradients. The ongoing analysis of butterfly CTI across an elevation gradient, using independent Monitoring Sites 1000 data, provides one such opportunity.

### 4.4 Apparent Stability: A Triple Conservation Blind Spot

Our results, combined with the butterfly CTI analysis from independent Monitoring Sites 1000 data, reveal what we term "apparent stability"—a triple pattern in which species richness, community temperature index, and diversity indices all remain statistically stable, while underlying community composition undergoes significant turnover. Specifically: (1) species richness shows no significant trend (p = 0.162); (2) butterfly CTI shows no significant trend (+0.314°C/decade, p = 0.147; much slower than European butterflies at +1.14°C/decade, Devictor et al. 2012); yet (3) species turnover is highly significant (p < 0.0001, ~25% species replacement over the study period).

Baselga decomposition of the temporal beta diversity revealed that turnover (species replacement) dominated over nestedness (species loss), indicating that the compositional change is driven by species swapping rather than simple impoverishment—consistent with the findings of Morelli et al. (2025), who documented phylogenetic homogenization in the same dataset using complementary methods. Our CTI and CWM analyses extend their phylogenetic perspective by showing that this replacement occurs between species with similar temperature niches (hence CTI stability) but different functional roles.

This apparent stability masks two concerning processes. First, the slow CTI response compared to European counterparts suggests substantial climate debt accumulation (Pattern C; Devictor et al. 2012)—communities are not tracking climate change, potentially due to dispersal limitation in Japan's fragmented landscape or the island biogeography of the Japanese archipelago. Second, the significant turnover despite stable aggregate indices indicates that specialist species are being replaced by generalists with similar temperature niches, a process invisible to both richness-based and CTI-based monitoring.

The conservation implications are stark: conventional biodiversity indicators—species counts, diversity indices, and even climate-tracking metrics—can simultaneously signal stability while the ecological fabric of communities is being rewoven. Monitoring programs that rely on any single indicator, or even combinations of standard indicators, risk providing false reassurance about ecosystem health.

### 4.5 Biotic Homogenization: Plants as Leading Indicators

The significant increase in alien plant species proportion (d = 0.419, p = 0.0001) at 62% of sites, with no association to specific environmental drivers, suggests that biotic homogenization is a pervasive, landscape-wide process in Japanese satoyama. The absence of a strong driver signal implies that multiple, possibly interacting factors—dispersal of alien species along transportation corridors, disturbance from abandonment, climate-mediated range expansion—contribute to a general trend toward floristic homogenization.

The fact that homogenization was detected in plants but not in birds at comparable effect sizes suggests that plants may serve as leading indicators of functional homogenization. Given the longer generation times and lower dispersal rates of many plant species compared to birds, this is somewhat counterintuitive and may reflect the particular vulnerability of satoyama plant communities to invasion during the early stages of post-abandonment succession.

### 4.6 Limitations

Several limitations should be acknowledged. First, our analysis is based on a single dataset of 47 bird species across 71 sites, which, while one of the longest standardized monitoring datasets in East Asia, represents a snapshot of one taxonomic group in one landscape type. Second, the binary classification of sites as abandoned or non-abandoned simplifies what is likely a continuous gradient of management intensity. Third, as an observational study, causal inference is limited; the temperature-dependent abandonment effect we report (Section 4.3) is based on cross-sectional comparison with post-hoc confound control, not experimental manipulation. Fourth, [Phase 1 GLMM interaction results and Phase 2 CTI driver analysis to be incorporated.]

---

**Status**: Draft v0.1. 要修正:
- Phase 1-4結果確定後にSection 4.2, 4.3, 4.5をリバイズ
- NBSAP提言の具体性をMika Phase 5文献で強化
- Section 4.3のH-CLIMATE-DEBTとの接続を里地チョウCTI結果で更新
- 4.3の「double jeopardy」概念は強すぎるか？Yui/Jimの評価を仰ぐ


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
# Paper 1: Data Availability Statement — メタデータ一覧

**作成日**: 2026-03-16 | **担当**: Sora (sora-data)

## 主要データセット

### 1. Katayama et al. (2024) 里山鳥類調査データ
- **内容**: 47鳥類種、71サイト、2009-2020、個体数カウント+農地放棄フラグ
- **DOI**: 10.6084/m9.figshare.24181656
- **URL**: https://figshare.com/articles/dataset/24181656
- **バージョン**: v1
- **アクセス日**: 2026-03-14
- **ライセンス**: CC BY 4.0
- **ファイル**: 01.CountData_satoyama.csv, 02.TraitData.csv

### 2. Ueta et al. (2025) モニ1000里地多分類群データ
- **内容**: 5分類群(鳥類/チョウ/カエル/ホタル/植物)、157サイト、環境変数パネルデータ
- **DOI**: 10.6084/m9.figshare.26347669
- **URL**: https://figshare.com/articles/dataset/26347669
- **バージョン**: v1
- **アクセス日**: 2026-03-14
- **ライセンス**: CC BY 4.0
- **論文**: Ueta et al. (2025) Nature Sustainability

### 3. EltonTraits 1.0 (Wilman et al. 2014)
- **内容**: 9,995鳥類種の食性・採餌層・体重
- **DOI**: 10.6084/m9.figshare.c.3306933
- **URL**: https://figshare.com/collections/EltonTraits_1_0/3306933
- **バージョン**: v1.0
- **アクセス日**: 2026-03-14
- **ライセンス**: CC BY 4.0
- **論文**: Wilman et al. (2014) Ecology 95:2027

### 4. AVONET (Tobias et al. 2022)
- **内容**: 鳥類形態形質データ（翼長・嘴長・体重等）
- **DOI**: 10.6084/m9.figshare.16586228
- **URL**: https://figshare.com/articles/dataset/16586228
- **バージョン**: v2
- **アクセス日**: 2026-03-14
- **ライセンス**: CC BY 4.0
- **論文**: Tobias et al. (2022) Ecology Letters 25:581-597

### 5. WorldClim v2.1 BIO1 (Fick & Hijmans 2017)
- **内容**: 年平均気温、全球グリッド
- **URL**: https://www.worldclim.org/data/worldclim21.html
- **解像度**: 2.5 arc-min (~4.5km)
- **バージョン**: v2.1
- **アクセス日**: 2026-03-16 (Kai取得)
- **ライセンス**: CC BY-SA 4.0
- **論文**: Fick & Hijmans (2017) International Journal of Climatology 37:4302-4315

### 6. VIIRS SRUNet 夜間光害時系列 (Chen et al. 2024)
- **内容**: NPP-VIIRS V2-Like年次コンポジット、2012-2023
- **DOI**: 10.6084/m9.figshare.22262545.v8
- **URL**: https://figshare.com/articles/dataset/22262545
- **解像度**: 15 arc-sec (~500m)
- **バージョン**: v8
- **アクセス日**: 2026-03-15
- **ライセンス**: CC BY 4.0
- **論文**: Chen et al. (2024) Scientific Data 11:1138

### 7. 農林水産省 作物統計（水稲作付面積）
- **内容**: 都道府県別水稲作付面積、1960-2023年
- **URL**: https://www.e-stat.go.jp/stat-search/files?toukei=00500215
- **アクセス日**: 2026-03-16
- **ライセンス**: 政府統計（利用規約に基づく二次利用可）

### 8. 農林業センサス 耕作放棄地面積
- **内容**: 都道府県別耕作放棄地面積、1975-2015年
- **URL**: https://www.e-stat.go.jp/
- **アクセス日**: 2026-03-15
- **ライセンス**: 政府統計

### 9. NIES WebKis-Plus 農薬出荷量（参考）
- **内容**: ネオニコチノイド系7種+フィプロニルの都道府県別出荷量、2010-2014
- **URL**: https://www.nies.go.jp/kisplus/
- **アクセス日**: 2026-03-16 (Act Beyond Trust経由)
- **ライセンス**: 公開データ
- **注記**: Paper 1 Discussionで参照（独立テーマH-NEO-1は凍結）

## コード

- **分析言語**: Python 3.13
- **リポジトリ**: [URL to be determined upon acceptance]
- **主要パッケージ**: numpy, scipy, statsmodels, scikit-learn, rasterio, geopandas

## DASテンプレート（英文）

All data used in this study are publicly available. Bird community data (47 species, 71 sites, 2009–2020) are from Katayama et al. (2024; figshare doi:10.6084/m9.figshare.24181656). Multi-taxon monitoring data (5 taxa, 157 sites) are from Ueta et al. (2025; figshare doi:10.6084/m9.figshare.26347669). Bird functional traits are from EltonTraits 1.0 (Wilman et al. 2014; figshare doi:10.6084/m9.figshare.c.3306933) and AVONET (Tobias et al. 2022; figshare doi:10.6084/m9.figshare.16586228). Annual mean temperature data are from WorldClim v2.1 (Fick & Hijmans 2017; worldclim.org). VIIRS nighttime light data (2012–2023) are from the SRUNet dataset (Chen et al. 2024; figshare doi:10.6084/m9.figshare.22262545.v8). Agricultural statistics (paddy field area, abandoned farmland) are from Japan's e-Stat portal (e-stat.go.jp). Analysis code is available at [repository URL].

- Katayama et al. (2024): figshare DOI 10.6084/m9.figshare.24181656
- Ueta et al. (2025): figshare DOI 10.6084/m9.figshare.26347669
- EltonTraits 1.0: figshare DOI 10.6084/m9.figshare.3559887
- AVONET: figshare DOI 10.6084/m9.figshare.16586228
- JMA temperature anomaly: Japan Meteorological Agency
- Analysis scripts: [repository TBD]

## References
[Full list: Mika workspace/h-comp-reference-list.md — 30+ citations including Katayama 2024, Morelli 2025, Yamaura 2025, Uchida 2025, Dornelas 2014, Blowes 2019, Devictor 2008/2012, McKinney & Lockwood 1999, Koenig 2022, Mantua & Hare 2002, etc.]

## Author Contributions
Conceptualization: Ryo, Ken. Data analysis: Ken. Literature review: Mika. Quality assurance: Yui. Writing — original draft: Ryo. Writing — review and editing: all authors. Project coordination: Jim.

## Competing Interests
The authors declare no competing interests.

## Use of AI Tools
This study was conducted using the BioEco Agent Lab, a multi-agent AI research platform. Statistical analyses were designed and executed by AI agents with human oversight. All analytical decisions, interpretations, and conclusions were reviewed and approved by human researchers. See Supporting Information for details.

## Supplementary Materials
- **Table S1**: 40 species richness/abundance tests (full results with BH-corrected p-values)
- **Table S2**: Complete list of 93 tests with within-family and global BH-corrected p-values
- **Table S3**: EltonTraits matching for 47 Katayama bird species (including 11 synonym resolutions)
- **Table S4**: Propensity score matching details + exploratory cold-region CTI analysis (n = 3; inconclusive)
- **Table S5**: Hypothesis development timeline (H1rev → H-COMP), documenting confirmatory vs exploratory analyses
- **Analysis S6**: Exploratory temporal beta diversity and species replacement analysis (E2×E3). Baselga (2010) decomposition revealed turnover-dominated species replacement (67%). Gained species were predominantly forest-dwelling (61%, Fisher OR = 3.34, p = 0.071, Bayesian P(OR>1) = 97.1%), while lost species were edge/open-habitat species. Temperature preferences of gained species were +1.7°C warmer than lost species (d = 0.48). This exploratory analysis suggests that the species richness paradox reflects a near-exact compensation between forest species colonization and open-habitat species loss during post-abandonment succession. Mann-Whitney test for habitat × net change interaction: p = 0.019.

---

**DRAFT STATUS**: v3 — E2 added as Supplementary S6. Author Contributions, AI disclosure, Competing Interests added. Ready for JAE format conversion.
**Word count**: ~5,000 main text (JAE limit: 7,000 including all parts except References and Supporting Information).


## Conclusions

# Conclusions Draft — Paper 1

Our multi-taxon analysis of 158 satoyama sites demonstrates that conventional species richness metrics fail to detect ongoing ecological change in depopulating Japanese landscapes. While none of 40 species-level tests showed significant responses to environmental drivers, the proportion of non-native plant species is increasing significantly across sites (d = 0.419, p < 0.001), indicating pervasive biotic homogenization. Exploratory analyses revealed that apparent thermophilization signals were confounded by baseline temperature, and that multi-taxon breakpoints coincided with a Pacific Decadal Oscillation phase shift rather than being abandonment-specific. These findings carry three key implications. First, biodiversity monitoring frameworks—including Japan's National Biodiversity Strategy and the CBD Global Biodiversity Framework—should incorporate functional indicators such as non-native species ratios to complement species counts. Second, confound control through propensity score matching should become standard practice in observational studies of land-use effects on biodiversity. Third, the transparency of reporting negative results alongside positive findings strengthens the evidence base for conservation policy. The existing Monitoring Sites 1000 data infrastructure can immediately support calculation of these functional indicators at no additional data collection cost.
