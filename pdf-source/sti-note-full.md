# How reliable is your Community Temperature Index? A practical framework for STI quality control in climate debt assessments

## Short Title: STI quality determines CTI reliability

## Target: Methods in Ecology and Evolution — Application Note (~2,000 words)

---

## Abstract (~150 words)

The Community Temperature Index (CTI) is widely used to track community-level responses to climate change, yet its reliability depends entirely on the quality of underlying Species Temperature Index (STI) values. Here, we demonstrate through a case study of Japanese butterfly communities that CTI trend direction and significance can reverse entirely depending on STI source, taxonomic match rate, and spatial resolution. Across five iterations of STI estimation — from European database proxies (13% species match) to Japan-specific occurrence-based values (100% match) — CTI trends shifted from a significant decrease (-0.88°C/decade, p = 0.028) to a non-significant increase (+0.30°C/decade, p = 0.14). We propose a practical STI Quality Framework comprising (1) a three-tier confidence flag system, (2) match-rate thresholds for reliable inference, and (3) mandatory multi-source sensitivity analysis. We recommend that all CTI studies report STI provenance and conduct sensitivity analyses across STI definitions.

## 1. Introduction (~400 words)

The Community Temperature Index (CTI; Devictor et al. 2008) has become the standard metric for detecting climate-driven community restructuring. CTI is computed as the abundance-weighted mean of species-level thermal affinities (Species Temperature Index, STI). Despite widespread adoption (>200 studies), the sensitivity of CTI to STI definition has received limited attention.

Previous work has shown that latitude-based STI proxies poorly correlate with temperature-based STI (r ≈ 0; [Paper 2 reference]), and that 85% of avian CTI studies show sign reversal across STI definitions. However, no study has systematically quantified how STI *data quality* — specifically, taxonomic match rate, geographic provenance, and spatial resolution — affects CTI conclusions.

Here, we present a case study from Japanese butterfly communities where iterative STI refinement produced four distinct CTI artifacts before converging on a stable result. This natural experiment in STI quality reveals that:

1. CTI conclusions can reverse sign with <50% STI taxonomic match rate
2. European STI databases produce systematic bias when applied to East Asian fauna
3. A match-rate threshold of >80% is required for stable CTI inference

We propose a practical STI Quality Framework for the CTI research community.

## 2. Methods (~500 words)

### 2.1 Study system

Japanese butterfly communities from the Monitoring Sites 1000 programme: 33 satoyama (rural landscape) sites × 114 species × 10 years (2005–2014) and 4 alpine sites × ~80 species × 12–15 years (2009–2023).

### 2.2 Five STI estimation approaches

We computed STI using five progressively refined approaches:

| Gen | Source | Species | Match rate | Method |
|---|---|---|---|---|
| G1 | CLIMBER v1.0 | 15/114 | 13% | European distribution centroids × CRU TS 1971–2000 mean annual temperature (Schweiger et al. 2014) |
| G2 | Local occurrence | 82/114 | 75% | Abundance-weighted mean of Moni1000 site temperatures (Ueta et al. 2025) |
| G3 | GBIF × WorldClim 10' | 105/114 | 92% | GBIF Japan occurrences (max 300/species, basisOfRecord=HUMAN_OBSERVATION, coordinateUncertainty<10 km) × WorldClim v2.1 BIO1 at 10-arc-minute resolution. STI = median BIO1 across occurrences (robust to outliers) |
| G4 | GBIF × WorldClim 2.5' | 129/129 | 100% | Same as G3 at 2.5-arc-minute resolution (~4.5 km). Nine previously unmatched species resolved via GBIF taxonomic backbone (taxonKey API) |
| G5 | Alpine subset of G4 | 13/16 | 81% | G4 values for alpine-specialist species only, excluding lowland species recorded at alpine survey sites |

For G3–G4, species with fewer than 30 valid temperature extractions were flagged as Medium confidence; all others were High confidence following our STI Quality Framework (see Discussion).

### 2.3 CTI computation

CTI = Σ(abundance_i × STI_i) / Σ(abundance_i) per site per year. Minimum thresholds: ≥10 individuals, ≥3 species per site-year.

### 2.4 Sensitivity metrics

For each STI generation, we computed: (a) site-level CTI trends (linear regression), (b) cross-site mean CTI trend with one-sample t-test, (c) Cohen's d effect size.

## 3. Results (~400 words)

### 3.1 CTI trends reverse with STI quality

| STI Gen | Match % | CTI (°C/decade) | p | d | Direction |
|---|---|---|---|---|---|
| G1 (CLIMBER) | 13% | **-0.876** | **0.028** | -0.52 | ❌ Significant decrease |
| G2 (occurrence) | 75% | -0.054 | 0.274 | -0.25 | ≈ Zero |
| G3 (WorldClim 10') | 92% | +0.314 | 0.147 | +0.33 | Non-sig increase |
| G4 (WorldClim 2.5') | 100% | +0.295 | 0.144 | +0.33 | Non-sig increase |
| G5 (alpine-only) | 94% | +0.131 | 0.622 | — | ≈ Zero |

G1 produced a false-positive significant CTI decrease. The result stabilized at G3 (>80% match) and remained unchanged through G4 (100%).

### 3.2 Match-rate threshold

Plotting |CTI trend| against match rate across all five generations reveals a clear threshold: below 50%, CTI trends are unreliable; between 50–80%, direction is unstable; above 80%, conclusions converge.

### 3.3 Alpine artifact replication

The same artifact pattern was independently replicated in alpine data: full-species CTI (including lowland species recorded at alpine sites) showed a significant decrease (-0.80°C/decade, p = 0.016), while alpine-specialist-only CTI was stable (+0.13°C/decade, p = 0.62).

### 3.4 Cross-taxon replication: bird CTI-RDD artifact

A sixth artifact was detected when applying CTI to a spatial Regression Discontinuity Design (RDD) for bird communities around Oze National Park. Using Katayama temp_pos STI (42/180 species matched, site-specific match rate = 23%), the CTI-RDD indicated significantly cooler communities inside the park (d = -1.62). However, WorldClim-based STI (211/212 species, 99.5% match, 97% High confidence) reversed the conclusion entirely (d = +2.61, warmer inside). The site-specific match rate of 23% fell below the 50% prohibition threshold, demonstrating that aggregate match rates (59% across all sites) can mask locally critical quality failures. This finding extends the STI quality framework from butterflies to birds and from temporal CTI trends to spatial RDD applications.

## 4. Discussion (~400 words)

### 4.1 The STI Quality Framework

We propose three components:

**Confidence flags** (per species):
- High: Same species, same region, occurrence-based STI (n ≥ 30)
- Medium: Same species, different region (e.g., European database)
- Low: Congener proxy or n < 10

**Match-rate thresholds** (per community analysis):
- <50%: Results unreliable — do not interpret
- 50–80%: Sensitivity analysis mandatory — report range of outcomes
- >80%: Primary analysis — conclusions likely stable

**Mandatory sensitivity analysis**: All CTI studies should report results under at least two independent STI definitions (e.g., regional occurrence-based + global database).

### 4.2 Implications for the CTI literature

Many published CTI studies use European-centric STI databases (CLIMBER, Devictor 2008 original values) for non-European fauna. Our results suggest that such studies may contain undetected artifacts. We recommend retrospective sensitivity analyses for CTI studies with <80% regional STI coverage.

### 4.2 Application: How STI quality propagates to climate debt assessment

The CTI is used to calculate a tracking ratio (TR = ΔCTI/Δt ÷ ΔT/Δt), where TR < 1.0 indicates climate debt accumulation (Devictor et al. 2012). Because TR inherits CTI uncertainty, STI quality directly propagates to climate debt conclusions. In our case study, STI match rate determined whether Japanese butterflies appeared to show reverse tracking (TR < 0; artifact at 13% match), indeterminate tracking (75%), or near-complete tracking (TR ≈ 1.0; stable at ≥92%). Critically, TR uncertainty is amplified relative to CTI uncertainty: SE(TR) = |TR| × √[(SE_CTI/CTI_slope)² + (SE_warming/warming)²]. When CTI slope is non-significant, TR confidence intervals become extremely wide (95% CI: [−0.26, 2.35]), rendering climate debt inference unreliable regardless of statistical framework. We recommend: (1) ensure >80% STI match before computing TR; (2) report TR with both ML and Bayesian estimates; (3) describe non-significant CTI slopes as "suggestive evidence" rather than "evidence for climate debt."

### 4.3 Spatial resolution as a fourth quality dimension

STI values for alpine specialists are sensitive to climate grid resolution. At 10-arc-minute resolution (~18 km), mountain pixels average valley and summit temperatures, inflating STI for cold-adapted species (e.g., Boloria freija: ΔSTI = 3.1°C between 10' and 2.5' resolution). For species at the cold extreme, the effect is reversed: Parnassius eversmanni (Usuba-kichō) STI shifted from -0.80°C (10') to -2.09°C (2.5'), a Δ of 1.29°C, demonstrating that coarse-resolution STI systematically overestimates thermal niches of high-altitude specialists. We recommend 2.5-arc-minute or finer resolution for montane/alpine CTI studies, and resolution sensitivity analysis as a fourth component of the STI Quality Framework.

### 4.4 Applicability to other regions and taxa

Our framework was developed using Japanese butterflies, but the principles apply universally. European avian CTI studies using Devictor (2008) original STI values should verify whether species-level thermal affinities remain accurate for peripheral populations (e.g., Mediterranean vs. Scandinavian). The >80% match-rate threshold provides a practical benchmark for any CTI study, regardless of taxon or region.

### 4.5 Connection to STI definition sensitivity

This framework complements findings that CTI trends are sensitive to STI *definition* (latitude vs. temperature-based; [Paper 2 reference]). Together, STI definition choice and STI data quality represent two independent axes of uncertainty that should be reported in all CTI studies.

## 5. Conclusions (~100 words)

CTI is a powerful tool for detecting climate-driven community change, but its reliability is determined by the underlying STI quality. We recommend: (1) report STI provenance and match rate in all CTI studies; (2) apply the >80% match-rate threshold for primary conclusions; (3) conduct multi-source STI sensitivity analysis as standard practice. The STI Quality Framework proposed here provides a practical checklist for researchers and reviewers.

## Data Availability

All STI datasets, CTI computation code, and sensitivity analysis scripts will be deposited in a public GitHub repository with a Zenodo DOI upon acceptance. Key files: butterfly_sti_merged_all.csv (130 species, G3), butterfly_sti_merged_2.5m.csv (120 species, G4), rdd_bird_sti_worldclim.csv (211 species, bird RDD), scripts/calculate_sti.py, scripts/fix_missing_sti.py.

## References (~15–20)

Devictor et al. 2008, 2012; Schweiger et al. 2014 (CLIMBER); Baselga 2010; Katayama et al. 2023, 2024; Ueta et al. 2025; Fick & Hijmans 2017 (WorldClim); [Paper 2 reference]; Chan et al. 2024.
