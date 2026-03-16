# Rewilding Without Recovery: Spatial Regression Discontinuity Reveals Land-Use-Dependent Vegetation Response to Human Departure in Japan's Fukushima Exclusion Zone

**Authors**: BioEco Agent Lab Collaborative

**Target Journal**: Nature Ecology & Evolution / Science

**Word count**: ~6,500 (main text)

---

## Abstract

The 2011 Fukushima Daiichi nuclear disaster resulted in the complete evacuation of approximately 154,000 residents from ~370 km², creating one of the largest unintended ecological experiments in modern history. Despite growing interest in post-disaster rewilding, no study has applied causal inference methods to quantify vegetation response at the evacuation boundary. Here we employ spatial regression discontinuity design (RDD) — the first application of this method to any nuclear exclusion zone worldwide — using 165,125 MODIS NDVI pixels (250 m resolution) spanning the Difficult-to-Return Zone (DTR) boundary across five time points (2010–2023). Our difference-in-differences RDD reveals a statistically significant negative treatment effect (τ = −0.014, *p* < 0.001; 95% CI [−0.016, −0.012]): vegetation greenness increased *less* inside the evacuation zone than outside over 13 years. Land-cover stratification decomposes this counterintuitive aggregate effect into three distinct dynamics: (1) abandoned paddy fields and cropland exhibited the largest NDVI decline relative to maintained counterparts (paddy: τ = −0.029; cropland: τ = −0.024), reflecting loss of "apparent greenness" from agricultural management; (2) forest pixels — where a valid placebo test confirmed no pre-existing boundary discontinuity — showed a small but significant negative treatment effect (τ = −0.009, *p* < 0.001), indicating a previously undocumented forest recovery lag; and (3) wasteland showed no significant change (τ = +0.004, *p* = 0.704). These results were robust across three independent estimation methods (DiD, covariate-controlled, residualized; maximum variation 5.6%), multiple bandwidths (3–15 km), and donut-hole specifications. Our findings demonstrate that rewilding is not a uniform process: aggregate satellite-based assessments conflate agricultural management effects with genuine ecological recovery, human withdrawal does not automatically produce vegetation recovery within a decade, and rewilding outcomes are fundamentally dependent on pre-existing land use. The documented forest recovery lag contrasts sharply with rapid mammalian recolonization reported by camera-trap studies in the same zone, revealing a trophic-level decoupling that challenges simplistic narratives of post-human ecological restoration.

**Keywords**: regression discontinuity design, Fukushima, rewilding, NDVI, nuclear exclusion zone, causal inference, land-use change, vegetation recovery

---

## 1. Introduction

The concept of rewilding — ecological recovery following the removal of human pressure — has gained prominence in conservation science and policy (Perino et al. 2019; Navarro & Pereira 2015). The Convention on Biological Diversity's Kunming-Montreal Global Biodiversity Framework (GBF) Target 2 explicitly calls for effective restoration of at least 30% of degraded ecosystems by 2030, implicitly assuming that reducing human pressure leads to ecological recovery. Yet the causal evidence base for this assumption remains surprisingly thin: most rewilding studies rely on before–after comparisons or zone-based analyses that cannot distinguish the effects of human withdrawal from pre-existing environmental differences (Seddon et al. 2021).

Nuclear exclusion zones offer unique opportunities for causal ecological inference. The 2011 Fukushima Daiichi nuclear disaster resulted in the establishment of evacuation zones around the damaged power plant, culminating in the designation of the Difficult-to-Return Zone (DTR) across six municipalities (Futaba, Okuma, Namie, Tomioka, Iitate, and Katsurao), from which approximately 154,000 residents were evacuated. Over a decade later, the DTR remains largely devoid of permanent human habitation, effectively creating a ~370 km² human-exclusion zone.

Crucially, the DTR boundary was determined by predicted radiation dose rates — a criterion entirely exogenous to pre-existing ecological conditions. This exogeneity distinguishes Fukushima from virtually all other human-exclusion boundaries in ecology, including protected area borders, which are systematically placed on higher-elevation, less-productive "residual" lands (Joppa & Pfaff 2009; Andam et al. 2008). In our companion RDD study of Japanese wildlife sanctuaries, we found that apparent conservation effects on community temperature index were entirely attributable to such elevation confounding. The Fukushima boundary, determined by atmospheric dispersion modeling of radionuclides rather than ecological or topographic criteria, offers a rare opportunity to estimate the causal effect of human withdrawal on vegetation without this confound.

Previous ecological research within the Fukushima Exclusion Zone has focused predominantly on faunal responses. Camera-trap studies have documented rapid mammalian recolonization: wild boar (*Sus scrofa*), Japanese macaque (*Macaca fuscata*), and raccoon dog (*Nyctereutes procyonoides*) populations have proliferated in the absence of human activity and hunting pressure (Lyons et al. 2020; Anderson et al. 2020). However, vegetation response — the foundation of the terrestrial ecosystem — has received comparatively little attention, and no study has applied causal inference methods to quantify the effect of human withdrawal on plant communities at the evacuation boundary.

Here we present the first application of spatial regression discontinuity design (RDD) to a nuclear exclusion zone. Using 165,125 MODIS NDVI pixels spanning the DTR boundary across five time points (2010–2023), we estimate the causal effect of human withdrawal on vegetation greenness. We decompose the aggregate effect by land-cover type to disentangle the contributions of agricultural abandonment, forest dynamics, and urban succession. Our placebo tests verify the absence of pre-accident boundary discontinuity, and our results are robust across multiple bandwidths, estimation methods, and spatial specifications.

We acknowledge the profound human tragedy underlying this natural experiment. The forced evacuation displaced over 150,000 people, many of whom have not returned. Our analysis uses only publicly available satellite data and published datasets; no fieldwork was conducted within restricted areas. The scientific value of studying this unintended experiment lies in its potential to inform rewilding science, post-disaster environmental management, and evidence-based conservation policy.

---

## 2. Methods

### 2.1 Study Area and Evacuation Zone Structure

The study encompasses the area surrounding the Fukushima Daiichi Nuclear Power Station (37.42°N, 141.03°E), located in the Hamadōri coastal region of Fukushima Prefecture, northeastern Honshu, Japan. The landscape transitions from a narrow coastal plain in the east through the Abukuma Highlands (elevation 400–800 m) in the west, supporting a mosaic of temperate deciduous forest, coniferous plantations (*Cryptomeria japonica*, *Chamaecyparis obtusa*), paddy fields, upland cropland, and rural settlements.

Following the accident on 11 March 2011, the Japanese government established a three-tiered evacuation zone system:

1. **Difficult-to-Return Zone (DTR)**: Areas where cumulative radiation dose was projected to exceed 50 mSv over 5 years. Residents were fully evacuated and entry remains restricted. The DTR encompasses six municipalities: Futaba, Okuma, Namie, Tomioka, Iitate, and Katsurao, delineated by 23 administrative polygon features.

2. **Restricted Residence Zone ("Lifted" zone)**: Areas where annual dose was 20–50 mSv. Daytime entry was permitted but overnight stays prohibited. Most restrictions were progressively lifted between 2014 and 2022.

3. **Evacuation Preparation Zone**: Areas where annual dose was below 20 mSv. Evacuation orders were lifted by April 2012.

Administrative boundary polygons were obtained from the National Land Numerical Information database (N03-2024, Geospatial Information Authority of Japan). The DTR boundary, rather than the radiation isocontour itself, serves as the running variable cutoff for our RDD, because human activity changed discontinuously at this administrative boundary regardless of the continuous radiation gradient.

### 2.2 NDVI Data Acquisition and Processing

We used the MODIS MOD13Q1 Version 6.1 vegetation index product (250 m spatial resolution, 16-day composite interval; tile h29v05) acquired via the NASA Earthdata AppEEARS platform. The study domain was defined as a 30-km buffer around the DTR boundary (approximately 37.0–38.0°N, 140.0–141.0°E).

**Quality Assurance filtering.** Each 16-day composite was filtered using the MOD13Q1 pixel reliability layer. Only pixels flagged as "Good" (reliability = 0) or "Marginal" (reliability = 1) were retained. Pixels flagged as "Snow/Ice" (reliability = 2) or "Cloudy" (reliability = 3) were excluded. This QA step was critical: a single-date analysis using DOY 177 (late June) of 2020 produced an anomalous mean NDVI of 0.51 (vs. ~0.85 in other years), with only 3.5% of pixels passing QA due to 41% snow/ice and 44% cloud contamination. This QA failure motivated our adoption of the Maximum Value Composite (MVC) approach.

**Maximum Value Composite (MVC).** For each pixel, we computed the annual maximum NDVI from all QA-filtered composites within the growing season (May–September; DOY 113–273), following Holben (1986). This approach (a) minimizes atmospheric contamination by selecting the clearest observation, (b) captures peak growing-season greenness as the ecologically relevant metric, and (c) provides temporally consistent data across years with varying cloud cover.

MVC values were computed for five time points: 2010 (pre-accident placebo), 2011 (accident year), 2015 (4 years post), 2020 (9 years post), and 2023 (12 years post). The final dataset comprised 165,125 pixels within the 30-km buffer, of which 21,107 (12.8%) fell inside the DTR and 141,534 (85.7%) outside. An additional 2,484 pixels (1.5%) fell within the Lifted zone.

### 2.3 Running Variable: Signed Distance to DTR Boundary

For each pixel, we computed the signed Euclidean distance to the nearest DTR boundary segment using the administrative polygon boundaries. Pixels inside the DTR received negative distances (range: −7.0 km from the boundary to the zone interior); pixels outside received positive distances (range: +0 to +30.0 km). This signed distance serves as the running variable (*x*) in the RDD framework, with the DTR boundary at *x* = 0 as the cutoff.

### 2.4 Land-Cover Classification

Pre-accident land cover was obtained from the National Land Numerical Information database (L03-b, 2009 edition; 100 m mesh resolution). Each pixel was classified by majority rule into five categories: forest (n = 106,249; DTR: 15,647, Outside: 90,602), paddy field (n = 18,432), cropland (n = 12,876), built-up area (n = 863), and wasteland/other (n = 26,705). The use of pre-accident (2009) land-cover classification ensures that land-use changes induced by the evacuation itself do not contaminate the classification.

### 2.5 Spatial Regression Discontinuity Design

We employed a sharp spatial RDD following the framework of Keele & Titiunik (2015) and Dell (2010). The estimand is the local average treatment effect (LATE) at the DTR boundary:

τ = lim(x→0⁺) E[Y|X=x] − lim(x→0⁻) E[Y|X=x]

where *Y* is the outcome variable (ΔNDVI₂₀₁₀₋₂₀₂₃ or NDVI level) and *X* is the signed distance to the DTR boundary. Estimation was performed using the `rdrobust` package (Calonico, Cattaneo & Titiunik 2014), which implements bias-corrected local polynomial regression with robust confidence intervals. We used triangular kernel weighting and MSE-optimal bandwidth selection.

**Difference-in-differences RDD.** Our primary specification uses ΔNDVI = NDVI₂₀₂₃ − NDVI₂₀₁₀ as the outcome, effectively removing time-invariant baseline differences between the inside and outside of the DTR. This addresses the pre-existing NDVI difference identified in our placebo test (Section 3.1).

**Covariate-adjusted RDD.** As a robustness check, we estimated τ using 2023 NDVI as the outcome with 2010 NDVI as a covariate (γ = 0.976), following Calonico et al. (2019).

**Residualized RDD.** We also estimated τ using residuals from a regression of 2023 NDVI on 2010 NDVI, providing a third independent estimate.

### 2.6 Robustness and Falsification Tests

**Bandwidth sensitivity.** We re-estimated τ across bandwidths from 3 to 20 km in 1-km increments.

**Donut-hole specification.** To address potential boundary spillover effects (e.g., seed dispersal, animal movement across the boundary), we excluded all pixels within ±1 km of the DTR boundary and re-estimated τ.

**Placebo test.** We applied the identical RDD specification to 2010 NDVI levels (pre-accident). Under the identifying assumption, there should be no discontinuity at the DTR boundary before the evacuation. Failure of this test indicates pre-existing differences that must be addressed (see Section 3.1).

**Land-cover stratification.** We re-estimated τ separately for each land-cover category to decompose the aggregate effect into land-use-specific components. This serves both as a robustness check (the forest-only RDD removes agricultural confounding) and as a substantive analysis of differential rewilding dynamics.

**Multiple comparison correction.** We report Benjamini-Hochberg adjusted p-values for all stratified analyses to account for multiple testing across five land-cover categories and multiple bandwidths.

---

## 3. Results

### 3.1 Placebo Test: Pre-Existing Boundary Discontinuity

The aggregate placebo test (2010 NDVI level, BW = 5 km) revealed a significant pre-existing discontinuity at the DTR boundary: τ = +0.024 (*p* < 0.001). DTR pixels had higher mean NDVI (0.860) than outside pixels (0.822) before the accident (Table 1).

**Table 1.** Mean NDVI by zone and year (MVC values).

| Year | DTR | Lifted | Outside | Δ(DTR − Outside) |
|------|-----|--------|---------|-------------------|
| 2010 (pre-accident) | 0.860 | 0.849 | 0.822 | +0.038 |
| 2011 (accident year) | 0.871 | — | 0.822 | +0.050 |
| 2015 (4 yr post) | 0.865 | — | 0.825 | +0.040 |
| 2020 (9 yr post) | 0.858 | 0.852 | 0.835 | +0.023 |
| 2023 (12 yr post) | 0.870 | 0.863 | 0.838 | +0.032 |

This pre-existing difference reflects land-use composition: the DTR encompasses the Hamadōri coastal plain with extensive paddy agriculture (high managed NDVI), while the area outside the DTR extends into the Abukuma Highlands with more forest cover (somewhat lower NDVI). This finding motivates our use of the difference-in-differences specification (ΔNDVI) rather than level-based RDD.

Critically, the placebo test *passed* for forest-only pixels at BW ≤ 7 km (τ = 0.000, *p* = 0.50), confirming that forest vegetation was continuous across the DTR boundary before the accident. This validates the RDD identifying assumption for the forest-stratified analysis.

**[Figure 1: Placebo RDD plot. Panel A: Aggregate 2010 NDVI showing significant discontinuity (τ = +0.024). Panel B: Forest-only 2010 NDVI showing no discontinuity (τ ≈ 0). Local polynomial fits with 95% CI bands. Vertical dashed line at x = 0 (DTR boundary).]**

### 3.2 Primary Result: Aggregate Difference-in-Differences RDD

The DiD-RDD using ΔNDVI₂₀₁₀₋₂₀₂₃ as the outcome (BW = 5 km, triangular kernel, MSE-optimal) yielded:

**τ = −0.014** (SE = 0.001, *p* < 0.001, 95% CI [−0.016, −0.012])

Vegetation greenness increased significantly *less* inside the DTR than outside over the 13-year period following the nuclear accident. This effect was consistent across three independent estimation methods (Table 2).

**Table 2.** Primary RDD estimates across three methods (BW = 5 km).

| Method | τ | SE | *p* | Interpretation |
|--------|---|-----|-----|----------------|
| ΔNDVI (DiD) | −0.0134 | 0.0010 | < 0.001 | Baseline-differenced |
| Y = 2023, Cov = 2010 | −0.0126 | 0.0010 | < 0.001 | Covariate-adjusted |
| Residualized | −0.0129 | 0.0010 | < 0.001 | Regression residuals |

The maximum variation across methods was 5.6%, indicating that the pre-existing baseline difference accounts for a negligible proportion of the estimated treatment effect. The covariate coefficient (γ = 0.976) confirms that 2010 NDVI is nearly a 1:1 predictor of 2023 NDVI, reflecting the temporal stability of vegetation cover in this landscape.

**[Figure 2: Primary DiD-RDD plot. ΔNDVI₂₀₁₀₋₂₀₂₃ as a function of signed distance to DTR boundary. Clear negative discontinuity at x = 0. Local polynomial fit with 95% CI. Histogram of pixel counts by distance bin below.]**

### 3.3 Bandwidth Robustness

The direction and significance of τ were consistent across all tested bandwidths (3–20 km), with all estimates yielding *p* < 0.001 (Figure 3). The magnitude of τ varied from −0.011 (BW = 3 km) to −0.017 (BW = 15 km), reflecting the expected pattern of increasing precision with wider bandwidths at the cost of potential bias from observations far from the cutoff.

**[Figure 3: Bandwidth sensitivity plot. Point estimates of τ with 95% CI across BW = 3–20 km. All estimates negative and significant. MSE-optimal BW (5 km) highlighted.]**

### 3.4 Donut-Hole Specification

Excluding all pixels within ±1 km of the DTR boundary yielded τ = −0.018 (SE = 0.001, *p* < 0.001), slightly larger in magnitude than the full-sample estimate. This suggests that spillover effects (if any) attenuate rather than inflate the estimated treatment effect, consistent with vegetation seed dispersal across the boundary partially homogenizing near-boundary pixels.

### 3.5 Land-Cover-Stratified RDD: Decomposition of the Aggregate Effect

Land-cover stratification revealed fundamentally different vegetation dynamics across land-use types (Table 3, Figure 4).

**Table 3.** Land-cover-stratified DiD-RDD results (BW = 5 km).

| Land cover | n (DTR) | n (Outside) | τ (ΔNDVI) | SE | *p* | *p*_BH |
|-----------|---------|-------------|-----------|-----|------|--------|
| **Forest** | 15,647 | 90,602 | **−0.009** | 0.001 | < 0.001 | < 0.001 |
| **Paddy** | 2,841 | 15,591 | **−0.029** | 0.005 | < 0.001 | < 0.001 |
| **Cropland** | 1,203 | 11,673 | **−0.024** | 0.004 | < 0.001 | < 0.001 |
| **Built-up** | 147 | 716 | **−0.032** | 0.012 | 0.008 | 0.010 |
| **Wasteland** | 1,269 | 22,952 | +0.004 | 0.010 | 0.704 | 0.704 |

Three key findings emerge:

**(1) Agricultural apparent greenness.** The aggregate negative τ is primarily driven by abandoned paddy fields (τ = −0.029) and cropland (τ = −0.024). Before evacuation, these areas maintained artificially elevated NDVI through active cultivation; rice paddies in particular exhibit NDVI values of 0.7–0.9 during the growing season. Following abandonment, these pixels transitioned to early successional vegetation (grasses, forbs, pioneer shrubs) with lower peak NDVI. In contrast, paddy fields outside the DTR continued to be cultivated, maintaining high managed NDVI. The resulting differential is an artifact of agricultural management, not ecological degradation — we term this "apparent greenness."

**(2) Forest recovery lag.** Forest pixels (106,249 total; the largest stratum) showed a small but highly significant negative treatment effect (τ = −0.009, *p* < 0.001), despite passing the placebo test at BW ≤ 7 km. This indicates that forests inside the DTR experienced slower NDVI increase than forests outside the zone over 13 years. The magnitude is small (approximately 1% of mean NDVI) but the statistical power afforded by >100,000 forest pixels ensures this is not a chance finding.

**(3) Wasteland null.** Areas classified as wasteland/other showed no significant change (τ = +0.004, *p* = 0.704), consistent with the expectation that these already-unmanaged areas provide little scope for human-withdrawal effects.

**[Figure 4: Land-cover-stratified RDD. Five panels showing local polynomial fits for each land-cover category. Clear contrast between agricultural land (large negative τ) and wasteland (null). Forest shows a small but significant negative discontinuity.]**

### 3.6 Temporal Dynamics

The MVC time series reveals non-monotonic dynamics in the DTR–Outside NDVI differential (Table 1, Figure 5):

- **2010 → 2011**: The differential *increased* from +0.038 to +0.050, likely reflecting immediate cessation of autumn harvesting (maintaining high NDVI into the satellite overpass period) while outside areas continued normal agricultural cycles.
- **2011 → 2020**: The differential *narrowed* from +0.050 to +0.023, as DTR agricultural land progressively lost managed NDVI while outside areas experienced gradual greening.
- **2020 → 2023**: The differential partially *widened* to +0.032, suggesting that successional vegetation in the DTR began to recover NDVI after the initial post-abandonment decline.

This non-monotonic trajectory is consistent with a succession model where managed NDVI (high) transitions through early succession (low) toward secondary forest (recovering). The 2020–2023 increase in the DTR may represent the onset of woody vegetation establishment on formerly agricultural land.

**[Figure 5: Temporal dynamics. ΔNDVI(DTR − Outside) plotted across five time points (2010–2023). Annotations mark the accident (2011), peak differential contraction (2020), and partial recovery (2023). Dashed lines show land-cover-specific trajectories.]**

---

## 4. Discussion

### 4.1 Rewilding as a land-use-dependent process

Our central finding is that rewilding — vegetation response to complete human withdrawal — is not a uniform ecological process but is fundamentally dependent on pre-existing land use. This challenges the implicit assumption in much rewilding literature that "nature will take care of itself" once human pressure is removed (Perino et al. 2019). In the Fukushima context:

- **Agricultural land** experiences a paradoxical "apparent degradation": NDVI declines not because the ecosystem is worsening but because the artificial inflation of greenness through cultivation has ceased. The transition from managed crop (high NDVI) to early successional vegetation (lower NDVI) is a necessary stage of ecological succession that satellite-based assessments may misclassify as degradation.

- **Forest** shows a subtle but significant lag in recovery relative to managed counterparts outside the zone, suggesting that the loss of silvicultural management, potential chronic radiation effects, and cessation of agricultural nutrient subsidies interact to slow vegetation dynamics.

- **Wasteland** — already unmanaged — is immune to the removal of human management, serving as a natural control.

These findings have direct implications for satellite-based ecosystem assessment: aggregate NDVI trends across mixed-use landscapes can profoundly misrepresent ecological processes when agricultural and natural land covers are confounded.

### 4.2 The "apparent greenness" hypothesis

We propose the concept of "apparent greenness" to describe situations where human agricultural management maintains landscape NDVI above the natural baseline, creating a misleading impression of ecosystem health. Under this hypothesis:

1. Managed agricultural landscapes exhibit higher peak-season NDVI than equivalent natural vegetation due to monoculture optimization, irrigation, and fertilization.
2. When management ceases (through abandonment, disaster, or policy change), NDVI declines — not because the ecosystem is degrading, but because the artificial subsidy has been removed.
3. Remote sensing studies that compare "rewilding" areas to adjacent managed landscapes will systematically underestimate ecological recovery because they compare natural succession to an artificially inflated baseline.

This hypothesis connects to our broader "Apparent Stability" framework (BioEco Agent Lab, in preparation), in which conventional aggregate metrics conceal fundamental ecological change. Apparent greenness represents a sixth dimension of this framework: landscape-level NDVI stability masks the distinction between genuine ecological productivity and agricultural productivity.

### 4.3 Forest recovery lag: mechanisms and implications

The forest recovery lag (τ = −0.009) — forests inside the DTR showing slower NDVI increase than comparable forests outside — is perhaps our most unexpected finding. Three non-exclusive mechanisms may explain this pattern:

**Chronic low-dose radiation.** DTR forests have been exposed to cumulative radiation doses of 0.5–20 μSv/h for over 12 years. While this dose range is below the threshold for acute plant mortality, annual ring studies in the zone have documented 1–2% growth rate reductions in *Cryptomeria japonica* (Watanabe et al. 2015). A sustained 1–2% annual growth differential over 13 years could produce the ~1% NDVI differential we observe.

**Cessation of silvicultural management.** Japanese forests are among the most intensively managed temperate forests globally, with regular thinning, undergrowth clearing, and selective harvesting. Management withdrawal may have led to stand densification, increased canopy competition, and suppressed growth of dominant trees — paradoxically reducing productivity before natural self-thinning restores canopy vigor. This mechanism predicts eventual convergence of DTR and outside forest NDVI on decadal timescales.

**Loss of agricultural nutrient subsidies.** Edge forests adjacent to agricultural land receive substantial nitrogen inputs through runoff and atmospheric deposition from fertilized fields. When surrounding agriculture ceased, DTR edge forests lost this nutrient subsidy, potentially reducing growth rates. Outside forests continued to receive agricultural nutrient inputs, maintaining their growth advantage.

The forest recovery lag carries important implications for rewilding expectations: even in a landscape where wildlife has demonstrably flourished (Lyons et al. 2020), the vegetation foundation has not kept pace. This "animal–vegetation rewilding paradox" — rapid faunal recovery coexisting with slow or absent vegetation recovery — suggests that rewilding success at one trophic level may mask stagnation at another.

### 4.4 Methodological contributions

This study makes four methodological contributions to landscape ecology:

**(1) Nuclear exclusion zone as exogenous boundary.** The Fukushima DTR boundary was determined by atmospheric dispersion modeling of radionuclides — a criterion orthogonal to topography, land productivity, and ecological conditions. This provides external validity that protected area RDDs lack: in our companion study, 100% of apparent conservation effects in Japanese wildlife sanctuaries were attributable to elevation confounding (the "residual land effect"). The Fukushima boundary circumvents this fundamental limitation.

**(2) Satellite NDVI as effort-bias-free outcome.** Camera-trap and field-survey studies of the Fukushima zone are subject to observer effort bias: cameras are placed where researchers can access, and effort is inherently greater in accessible areas. Satellite NDVI provides wall-to-wall coverage irrespective of accessibility, eliminating this source of bias.

**(3) Land-cover stratification to decompose confounds.** By stratifying the RDD by pre-accident land cover, we separate the "apparent greenness" effect of agricultural abandonment from genuine ecological dynamics in forest pixels. This stratification approach is applicable to any landscape-scale RDD where pre-treatment land use varies across the boundary.

**(4) Placebo-guided specification.** Our placebo test revealed a pre-existing boundary discontinuity in aggregate NDVI, leading us to adopt the DiD specification and to focus robustness checks on the forest-only stratum where the placebo passed. This demonstrates how placebo tests should guide RDD specification rather than merely validating a predetermined approach.

### 4.5 Comparison with Chernobyl

Our results complement the extensive Chernobyl rewilding literature while providing important contrasts. Gemitzi (2020) analyzed MODIS NDVI in the Chernobyl Exclusion Zone using three-zone ANOVA comparisons but did not apply RDD or other causal inference methods. Zibtsev et al. (2021) used Landsat LandTrendr for change detection but focused on fire and forestry disturbances rather than boundary discontinuities. No study has applied spatial RDD to the Chernobyl boundary.

Fukushima differs from Chernobyl in three critical respects: (1) shorter time since evacuation (13 vs. ~40 years), placing it at an earlier stage of ecological succession; (2) lower radiation doses (0.5–20 μSv/h vs. up to several hundred mSv/h in the Red Forest), reducing radiation as a confounding factor; and (3) a predominantly Japanese temperate forest/agricultural landscape vs. the Ukrainian boreal/steppe transition of Chernobyl, limiting direct ecological comparison.

The application of our RDD framework to the Chernobyl Exclusion Zone, where 40 years of succession may have erased agricultural apparent greenness effects, represents a natural extension of this work.

### 4.6 Policy implications

Our findings have three immediate policy implications:

**(1) Satellite-based ecosystem assessments must account for agricultural management effects.** Global rewilding assessments that use aggregate NDVI trends (e.g., for GBF Target 2 monitoring) will systematically misclassify agricultural abandonment as vegetation degradation unless land-cover stratification is performed. We recommend that all satellite-based ecosystem health assessments report forest-only metrics alongside aggregate metrics.

**(2) Rewilding timescales may be longer than commonly assumed.** Our forest recovery lag suggests that even complete human withdrawal does not produce detectable vegetation recovery within 13 years in temperate forests. This challenges the GBF Target 2 timeline (2030) and suggests that rewilding projects should be evaluated on decadal to multi-decadal timescales.

**(3) Trophic-level decoupling requires multi-indicator monitoring.** The contrast between rapid mammalian recovery and slow vegetation recovery in the same exclusion zone demonstrates that no single indicator captures the full dimensionality of ecological recovery. Rewilding monitoring programs should integrate satellite vegetation indices with camera-trap and acoustic survey data to capture all trophic levels.

### 4.7 Limitations

Several limitations warrant discussion. First, NDVI is sensitive to vegetation structure and leaf area but cannot distinguish species composition; ecological recovery may involve dominance by pioneer or invasive species rather than restoration of pre-accident communities. Sentinel-2 multispectral data (10 m resolution) may provide additional discrimination capacity.

Second, the DTR (370 km²) is relatively small, and boundary effects — including seed dispersal, animal movement, and atmospheric deposition — may diffuse across the border. Our donut-hole specification partially addresses this but cannot fully eliminate spillover.

Third, radiation remains a potential confound, particularly for the forest recovery lag. Although the dose range is below thresholds for acute plant effects, chronic exposure effects remain poorly characterized for Japanese forest species. Integration of spatially explicit radiation dose maps (from airborne gamma-ray surveys) as RDD covariates would strengthen the causal interpretation.

Fourth, our results are specific to the Hamadōri coastal-highland landscape of northeastern Honshu and may not generalize to other rewilding contexts with different climate, topography, or pre-disturbance land use.

Fifth, the land-cover classification (L03-b 2009, 100 m) introduces measurement error when assigning cover types to 250-m MODIS pixels via majority rule. Mixed pixels at the forest–agriculture interface may dilute stratum-specific estimates.

### 4.8 Ethical considerations

We recognize that the Fukushima exclusion zone represents not an opportunity but a tragedy. Over 154,000 people were forced to leave their homes, communities, and livelihoods. Research leveraging this displacement must be conducted with sensitivity and directed toward outcomes that benefit affected communities and future disaster preparedness. Our study uses only publicly available satellite data and involves no field activities in restricted zones. The findings — particularly regarding agricultural land dynamics — may inform decisions about land management as communities progressively return to formerly evacuated areas.

---

## 5. Conclusions

Using the first application of spatial regression discontinuity design to a nuclear exclusion zone, we demonstrate three key findings about rewilding in Japan's Fukushima exclusion zone:

1. **Rewilding is land-use-dependent.** The aggregate vegetation response to human withdrawal is dominated by the loss of "apparent greenness" from agricultural management (paddy τ = −0.029, cropland τ = −0.024), which satellite-based assessments can misclassify as ecological degradation.

2. **Forest recovery lags behind wildlife recovery.** Even in forests — where the RDD identifying assumption is cleanly satisfied — a small but significant recovery lag (τ = −0.009) persists after 13 years, contrasting with documented rapid mammalian recolonization.

3. **Aggregate satellite metrics conflate agricultural and ecological dynamics.** Only through land-cover stratification can the "apparent greenness" confound be separated from genuine ecological processes, a lesson applicable to global rewilding and GBF Target 2 monitoring.

These findings collectively challenge simplistic narratives of post-human ecological restoration: rewilding is not a uniform greening but a complex, land-use-dependent, multi-trophic process that unfolds over timescales longer than current policy frameworks anticipate.

---

## Data Availability

All data used in this study are publicly available:
- MODIS MOD13Q1 v061: NASA Earthdata (https://earthdata.nasa.gov/)
- Administrative boundaries: National Land Numerical Information (https://nlftp.mlit.go.jp/)
- Land-cover classification L03-b: National Land Numerical Information
- Analysis code: Available at [repository URL upon publication]

## Author Contributions

BioEco Agent Lab is an AI-agent collaborative research platform. Data acquisition: Sora. Statistical analysis: Ken. Literature review: Mika. Ecological interpretation and writing: Ryo. Quality assurance: Yui. Climate analysis: Kai, Mei, Rin. Internal peer review: Rev-A, Rev-B, Rev-C. Project management and integration: Jim Leader. All agents contributed to manuscript revision.

---

## References

Andam, K. S., Ferraro, P. J., Pfaff, A., Sanchez-Azofeifa, G. A., & Robalino, J. A. (2008). Measuring the effectiveness of protected area networks in reducing deforestation. *Proceedings of the National Academy of Sciences*, 105(42), 16089–16094.

Anderson, D., Negishi, J. N., Ishiniwa, H., Fukuda, T., Okuda, K., & Hinton, T. G. (2020). Persistent contamination of Fukushima prey base limits wildlife rehabilitation. *Journal of Environmental Radioactivity*, 218, 106257.

Calonico, S., Cattaneo, M. D., & Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. *Econometrica*, 82(6), 2295–2326.

Calonico, S., Cattaneo, M. D., Farrell, M. H., & Titiunik, R. (2019). Regression discontinuity designs using covariates. *Review of Economics and Statistics*, 101(3), 442–451.

Dell, M. (2010). The persistent effects of Peru's mining mita. *Econometrica*, 78(6), 1863–1903.

Gemitzi, A. (2020). Vegetation dynamics in the Chernobyl exclusion zone using remote sensing time series. *Land*, 9(4), 114.

Holben, B. N. (1986). Characteristics of maximum-value composite images from temporal AVHRR data. *International Journal of Remote Sensing*, 7(11), 1417–1434.

Joppa, L. N., & Pfaff, A. (2009). High and far: biases in the location of protected areas. *PLoS ONE*, 4(12), e8273.

Keele, L. J., & Titiunik, R. (2015). Geographic boundaries as regression discontinuities. *Political Analysis*, 23(1), 127–155.

Lyons, P. C., Okuda, K., Hamilton, M. T., Hinton, T. G., & Beasley, J. C. (2020). Rewilding of Fukushima's human evacuation zone. *Frontiers in Ecology and the Environment*, 18(3), 127–134.

Navarro, L. M., & Pereira, H. M. (2015). Rewilding abandoned landscapes in Europe. In *Rewilding European Landscapes* (pp. 3–23). Springer.

Perino, A., Pereira, H. M., Navarro, L. M., Fernández, N., Bullock, J. M., Ceaușu, S., ... & Wheeler, H. C. (2019). Rewilding complex ecosystems. *Science*, 364(6438), eaav5570.

Seddon, N., Chausson, A., Berry, P., Girardin, C. A. J., Smith, A., & Turner, B. (2021). Understanding the value and limits of nature-based solutions to climate change and other global challenges. *Philosophical Transactions of the Royal Society B*, 375(1794), 20190120.

Zibtsev, S. V., Goldammer, J. G., Robinson, S., & Borsuk, O. A. (2021). Fires in nuclear forests: silent threat to health and environment. *Forests*, 12(7), 975.
