# Are Fast-Growing "Sprinter" Trees Taking Over Japanese Forests? Functional Homogenization in Monitoring Sites 1000

BioEco Agent Lab | Working Paper | 2026-03-18
Target: Global Change Biology / Nature Plants

## Abstract

Guo et al. (2026, Nature Plants) predicted that global forests are shifting toward fast-growing "sprinter" species with acquisitive functional traits (low wood density, high SLA), driving functional homogenization and reducing long-term carbon storage capacity. However, this prediction was based on cross-sectional comparison of alien vs. native species' traits, not on direct observation of temporal change. Here, we propose the first temporal test of this prediction using Japan's Monitoring Sites 1000 (MS1000) long-term forest census: 122 plots, 431 tree species, 145,454 individuals tracked over 18 years (2004-2022). We will compute Community Weighted Mean (CWM) of wood density, specific leaf area, and maximum height using TRY plant trait database (125 species mapped, 80.4% individual coverage), and test whether CWM is shifting in the acquisitive (sprinter) direction using GLS-AR1 regression. Additionally, we will apply spatial Regression Discontinuity Design (RDD) at protected area boundaries to test whether protection buffers functional homogenization -- a globally unprecedented analysis (confirmed by external review: no prior study has applied RDD to functional diversity outcomes). Growing degree days (GDD) are increasing significantly at 3/7 Japanese weather stations (+39 to +47 C-days/decade), providing the climate driver for sprinter advantage.

## 1. Introduction

Forest functional composition is changing globally. Guo et al. (2026) analyzed 31,000+ tree species and found that alien naturalized species possess systematically more acquisitive traits (lower wood density, higher SLA, faster growth) than native species at risk of extinction. This predicts a future forest landscape dominated by "sprinter" species -- fast-growing, resource-acquisitive trees that invest in rapid growth rather than structural defense or longevity.

However, this prediction rests on space-for-time substitution (comparing alien vs. native trait distributions) rather than direct observation of temporal functional change. Whether temperate forests are already undergoing this functional shift in real time remains untested. Hisano et al. (2021, GCB) demonstrated temporal CWM shifts in Canadian boreal forests over 65 years, but no equivalent analysis exists for temperate Asia.

Japan's Monitoring Sites 1000 (MS1000) provides an exceptional dataset: standardized tree censuses across 122 plots spanning the entire Japanese archipelago, with individual-level tracking of stem diameter (GBH) over 18 years (2004-2022). Combined with the TRY plant trait database, MS1000 enables computation of CWM functional traits at each plot over time.

We propose three complementary analyses: (1) temporal CWM trends across all MS1000 plots (is Japan's forest becoming more acquisitive?), (2) spatial RDD at protected area boundaries (does protection buffer functional homogenization? -- the first application of RDD to functional diversity), and (3) climate driver analysis (do sites with greater GDD increase show faster sprinter encroachment?).

## 2. Methods

### 2.1 Forest census data
MS1000 tree census: 122 plots, 431 species, 145,454 individual stems. GBH (girth at breast height, cm) measured every ~5 years (2004, 2009, 2014, 2019, 2022 at core sites). Species identified by Japanese common name, converted to Latin binomial (125 species mapped, covering 80.4% of individuals).

### 2.2 Functional traits
TRY plant trait database (申請中). Target traits: wood density (WD, g/cm3), specific leaf area (SLA, cm2/g), maximum height (Hmax, m). Sprinter species defined as low WD + high SLA (Guo et al. 2026 classification). STI quality rule applied: >80% individual coverage required for reliable CWM.

### 2.3 CWM temporal trends
CWM = sum(abundance_i x trait_i) / sum(abundance_i) per plot per census year. Temporal trend estimated by GLS-AR1 (4-5 time points per plot). Positive CWM(SLA) trend + negative CWM(WD) trend = acquisitive shift (sprinter takeover).

### 2.4 RDD at protected area boundaries
Running variable: distance to nearest WDPA boundary. Outcome: CWM(WD), CWM(SLA), FDis (functional dispersion). This is the first application of RDD to functional diversity outcomes (confirmed: no prior study). Elevation and BIO1 as covariates (lesson from RDD Residual Land paper).

### 2.5 Climate driver
Growing degree days (GDD >5C) from JMA stations. 3/7 Tohoku stations show significant GDD increase (+39 to +47 C-days/decade, Mei analysis). CWM trend x GDD trend correlation across plots.

### 2.6 Subplots and power
MS1000 core sites: 1 ha = 4 subplots (50x50m). 49 sites x 4 = 196 potential observations. Monte Carlo simulation (Ken): n=20/side with effect=0.10 g/cm3 gives power=78%.

## 3. Data Summary

| Metric | Value |
|---|---|
| Plots | 122 |
| Species | 431 (125 mapped to Latin, 80.4% coverage) |
| Individuals | 145,454 |
| Census years | 2004-2022 (4-5 time points) |
| Top species | Sugi (6528), Sakaki (5674), Mizunara (4952) |
| TRY traits | WD, SLA, Hmax (申請中) |
| GDD trend | +39 to +47 C-days/decade (3/7 stations significant) |

## 4. Expected Results and Significance

If CWM shifts toward acquisitive traits (lower WD, higher SLA), this would provide the first temporal confirmation of Guo et al. (2026)'s global prediction in a specific national dataset. The RDD component would reveal whether Japan's protected areas buffer or accelerate this functional shift -- extending our companion RDD paper (which found no CTI protection effect due to residual land placement).

If no CWM shift is detected, this null result would constrain the timeline of the predicted sprinter takeover, suggesting that 18 years may be insufficient for detectable functional change in temperate forests (generation time limitation).

## References

Guo, W.-Y. et al. (2026) Global functional shifts in trees driven by alien naturalization and native extinction. Nature Plants. DOI:10.1038/s41477-025-02207-2

Hisano, M. et al. (2021) Rapid functional shifts across high latitude forests over the last 65 years. Global Change Biology, 27, 4309-4321. DOI:10.1111/gcb.15710

Suzuki, S.N. et al. (2015) Biased assessment of forest composition changes under climate change. Global Change Biology. DOI:10.1111/gcb.12911
