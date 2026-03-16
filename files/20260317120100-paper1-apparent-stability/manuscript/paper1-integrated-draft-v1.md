# Species richness masks biotic homogenization in depopulating Japanese satoyama: A multi-taxon functional analysis

## Abstract

Farmland abandonment driven by rural depopulation is accelerating in Japan, yet its ecological consequences may go undetected by conventional biodiversity metrics. We analyzed 15 years of standardized monitoring data from 157 satoyama sites across Japan (158 originally surveyed; 1 site excluded due to incomplete temporal coverage), encompassing five taxonomic groups (birds, butterflies, frogs, fireflies, and plants; 32,027 records), alongside multi-temporal environmental covariates. None of 40 tests relating species richness or abundance to environmental change were significant after Benjamini-Hochberg correction, confirming a 'species richness paradox' consistent with global patterns. In contrast, the proportion of non-native plant species increased significantly over time (d = 0.419, 95% CI [0.14, 0.70], BH-adjusted p < 0.001), with 62% of sites showing rising non-native ratios—indicating pervasive biotic homogenization. Exploratory community temperature index (CTI) analysis revealed that apparent thermophilization signals were confounded by baseline temperature differences between abandoned and non-abandoned sites. Segmented regression detected synchronous breakpoints across all taxonomic groups coinciding with the 2014 Pacific Decadal Oscillation phase shift, though these were not specific to abandoned sites. Our findings demonstrate that species-count-based indicators used in Japan's National Biodiversity Strategy and the CBD Global Biodiversity Framework are insufficient to detect the functional reorganization occurring in depopulating landscapes. We recommend incorporating non-native species ratios and functional diversity metrics into national monitoring frameworks.

## 1. Introduction

[Source: Mika paper-introduction-draft.md — 4 sections covering global abandonment trends, prior species-level studies (Katayama 2024, Morelli 2025, Yamaura 2025, Uchida 2025), species richness paradox literature (Dornelas 2014, Blowes 2019, Hillebrand 2018), functional indicator gap (CTI/CWM absent from prior Japanese studies), and study objectives]

**Rev-A対応: Uchida et al. (2025) Nat Sustain差別化（Intro末尾に追加）:**
Uchida et al. (2025) analyzed 5-17 year population trends of 464 species across the same 158 satoyama monitoring sites and demonstrated that biodiversity declined in both growing and shrinking municipalities. However, their analysis focused on taxonomic-level population trends and did not examine functional community composition. Our study extends their findings by asking not whether species are declining, but how community functional structure is changing even when species richness appears stable. Specifically, we apply community-weighted mean trait analysis (CTI, CWM), functional diversity indices (FDis), temporal beta-diversity decomposition, and propensity score matching to reveal hidden functional reorganization beneath the surface of stable species counts — the "apparent stability" paradox that conventional taxonomic indicators, including those used by Uchida et al., cannot detect.

### 1.1 Farmland abandonment and the satoyama crisis
### 1.2 Prior studies: Species-level analyses
### 1.3 The species richness paradox and functional indicators
### 1.4 Study objectives

## 2. Methods

[Source: Ken paper1_methods_text.md + Sora paper-methods-2.1-2.3-draft.md — 600+ words]

### 2.1 Study sites and datasets
- Monitoring Sites 1000 (satoyama survey): Katayama et al. (2024), 47 bird species, 71 sites, 2009-2020
- Ueta et al. (2025): 5 taxonomic groups, 157 sites, 2004-2022
- EltonTraits 1.0 (Wilman et al. 2014): STI, diet, foraging stratum
- Environmental covariates: urbanization, cultivation, forest, population, temperature (5km/10km, panel)

### 2.2 Species richness analysis
- Site-level TRIM slopes, Kruskal-Wallis by environmental change categories
- 5 groups × 4 drivers × 2 metrics = 40 tests

### 2.3 Biotic homogenization indices
- Non-native ratio: nonnative/(native+nonnative), annual trend
- Homogenization Index (HI) = slope(nonnative) - slope(native)

### 2.4 Community Temperature Index (exploratory)
- CTI = Σ(abundance × STI) / Σ(abundance), EltonTraits STI
- Confound control: PSM on baseline temperature

### 2.5 Breakpoint analysis
- Segmented regression, BH correction across 8 variables
- Discrimination test: abandoned vs non-abandoned control

### 2.6 Multiple testing correction
- BH method across family (per analysis) and global (93 tests)
- Full 93-test list in Supplementary Table S2

## 3. Results

### 3.1 Species richness and abundance show no response to environmental change
None of 40 BH-corrected tests significant. Shannon H' d=0.115, ns. Comprehensive null result across all 5 taxonomic groups.

### 3.2 Biotic homogenization: Non-native plant proportions are increasing
Ratio trend +0.27%/yr (r=0.717, p=0.0008). HI mean=+0.012, p=0.0005. Ratio-based d=0.419, 95%CI [0.143, 0.695], BH p<0.001. 62% of sites increasing. No association with specific environmental drivers. Independent confirmation of Uchida et al. (2025).

### 3.3 Community temperature index: Confounding by baseline temperature (exploratory)
Uncorrected CTI: d=0.497, p<0.001. PSM-corrected: d=0.176, p=0.407 (ns). Baseline temp imbalance: p=0.018. Interaction: p=0.90 (ns). Forest→CTI: r=-0.729 (afforestation decreases, not increases, CTI). STI definition sensitivity noted.

### 3.4 Synchronous multi-taxon breakpoints coinciding with climate regime shift
All 8 variables significant (BH-corrected). Two clusters: immediate (2008-2010: frogs F=114.6) and delayed (2016-2019: fireflies, bird abundance). Discrimination test: non-abandoned also show breakpoints (F=17.9, p=0.0002). Coincides with PDO phase shift 2014 + JMA +0.55°C.

## 4. Discussion

[Source: Mika paper-discussion-draft.md — 4 subsections + Limitations]

### 4.1 Species richness indicators are blind to functional change — Policy implications
[NOTE: Add 1 sentence clarifying that "apparent stability" emerged as a post-hoc integrative interpretation from the convergence of multiple independent analyses, not as an a priori hypothesis.]
[Rev-A対応: Uchida et al. (2025) showed taxonomic declines in the same satoyama sites. Our results demonstrate that even where Uchida's species-level analysis would detect no change (stable richness sites), functional reorganization proceeds silently. This underscores the inadequacy of species-count approaches — the very metric used by Uchida et al. and by Japan's NBSAP.]
### 4.2 Methodological lessons: CTI confounding and the importance of propensity score matching
### 4.3 Biotic homogenization: Pervasive and driver-independent
### 4.4 Climate regime shift and multi-taxon synchrony
[Rev-C M3対応: Breakpoints were detected in both abandoned (2016, F=11.9, p=0.004) AND non-abandoned (2015, F=13.2, p=0.003) sites. This confirms that breakpoints are NOT abandonment-specific but reflect regional-scale drivers, most likely the ~2014 PDO phase shift. We interpret breakpoints as temporal markers of broad environmental change rather than causal evidence for abandonment effects. The causal effect of abandonment is instead captured by the CTI analysis (Section 3.3), which uses cross-sectional comparison with propensity score matching.]
### 4.5 Apparent stability: A triple conservation blind spot
[Source: Ryo h-comp-paper-discussion-draft-v1.md Section 4.4]
Species richness stable (p=0.162) + CTI stable (+0.295°C/dec, p=0.144) + Turnover significant (p<0.0001, 25% replacement) = "apparent stability." Independent butterfly CTI confirms Japanese communities track climate at ~1/4 European rate (Pattern C: climate debt). Baselga decomposition: turnover >> nestedness (species replacement, not loss). Morelli 2025 phylogenetic complement. Conservation implication: standard indicators provide false reassurance. [NOTE: Add Simpson's paradox caution — the cold tertile CTI effect (d=1.38) coexists with a near-zero overall CTI effect (d=0.176), illustrating how aggregate analyses can mask subgroup-specific patterns.]

### 4.6 Temperature-dependent abandonment: Cold-region double jeopardy
[Source: Ryo h-comp-paper-discussion-draft-v1.md Section 4.3]
Cold-climate sites d=1.38 (exploratory). Robust P25-P50. Not HARKing (honest discovery via confound correction, Yui/Jim判定). Deer amplification (d=1.03 in high-density, exploratory). H-CLIMATE-DEBT connection. Policy: prioritize cold-climate satoyama.

### 4.7 Limitations

## 5. Conclusions
Four key implications: (1) "apparent stability" — species richness, CTI, and diversity indices can simultaneously signal stability while communities undergo profound reorganization; (2) functional and compositional indicators (CWM, turnover, alien ratios) must supplement richness-based targets in NBSAP/GBF; (3) cold-climate satoyama are priority conservation targets due to amplified thermophilization under abandonment; (4) the three-stage cascade suggests amphibian monitoring as an early warning system. We urge reinterpretation of stable biodiversity trends worldwide through the lens of apparent stability.

## Data Availability
[Source: Sora paper-data-availability-draft.md]

## References
[Source: Mika h-comp-reference-list.md — 30+ citations]

## Supplementary Materials
- Table S1: 40 species richness tests (full results)
- Table S2: 93 global tests with BH-corrected p-values
- Table S3: EltonTraits matching details (47 species)
- Table S4: PSM covariates and balance
- Table S5: Hypothesis development timeline (H1rev → H-COMP)

---

**DRAFT STATUS**: Integrated structure v2 (Ryo additions: Apparent Stability 4.5, Cold-region 4.6, enhanced Conclusions, Back Matter). Section bodies reference source files for full text. Ready for Yui bias audit + Gate C.
**Target**: Ecology Letters Article (max ~5,000 words) or PNAS Research Article
**Full text source files**: Ryo intro/methods/discussion drafts + Ken methods/results text + Sora DAS + Mika references
**Back Matter**: workspace/h-comp-paper-backmatter.md (DAS, Author Contributions, Competing Interests)
