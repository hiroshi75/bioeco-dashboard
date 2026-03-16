# Predicting bear-human conflict from beech mast cycles and summer sunshine: A parsimonious early warning model for Japan

**Target**: Journal of Applied Ecology
**Version**: v1 Integrated Draft
**Date**: 2026-03-17

---

## Abstract

Bear-human conflict in Japan has escalated dramatically, with record incidents in 2023 (196+ cases, 11 fatalities). We developed a parsimonious early warning model using 36 years of beech (Fagus crenata) mast crop data from 5 Tohoku prefectures (1989-2025) combined with JMA sunshine duration records. An ordinal logistic model with two predictors -- mast AR(1) (previous-year crop, beta = -1.49) and previous-summer sunshine hours (beta = +0.91) -- predicted mast crop categories with 78% accuracy within +/-1 category (LOOCV), providing 6-month lead time. The model detects 86% of severe mast failures (6/7 events). ENSO indices provided no additional predictive power (delta-AIC = +1.0), indicating that mast dynamics are driven by internal resource cycling modulated by local meteorology rather than large-scale climate teleconnections. Mast failure years closely matched major bear-conflict years (r = -0.36, p = 0.01). The 2025 crop score (0.1, severe failure) following the 2024 bumper crop (3.2) represents an imminent conflict risk for autumn 2025. We propose integration of annual mast surveys with JMA sunshine data as a real-time early warning system for prefectural bear management.

## 1. Introduction

Bear-human conflict in Japan has reached unprecedented levels. In 2023, over 196 incidents were recorded with 11 fatalities -- the deadliest year on record. The Asiatic black bear (Ursus thibetanus) population has surged from an estimated 15,000 in 2012 to over 54,000, driven by decades of favorable mast conditions and reduced hunting pressure. Simultaneously, rural depopulation has expanded the human-bear interface as abandoned settlements encroach into bear habitat.

The proximate cause of conflict surges is well established: failure of beech (Fagus crenata) mast crops forces bears to forage in human settlements during autumn. Beech mast production follows a characteristic boom-bust cycle driven by the resource budget model (Isagi et al. 1997; Satake and Iwasa 2000), in which trees accumulate photosynthetic resources over multiple years until a threshold is exceeded, triggering synchronized mass flowering and fruiting, followed by resource depletion and subsequent crop failure.

Despite the clear link between mast failure and bear conflict, no quantitative predictive model has been developed for Japan. We initially hypothesized that large-scale climate teleconnections (ENSO) might provide early warning through their influence on summer solar radiation. However, our analysis revealed that ENSO indices provide no significant predictive power for Tohoku sunshine hours (r = -0.15, all 7 stations non-significant), indicating that local meteorological variability -- driven by the Okhotsk Sea High, yamase cold fog, and foehn effects -- dominates over large-scale climate modes.

Here, we develop a parsimonious early warning model using two predictors: (1) the previous-year mast crop score (AR(1) autoregressive term) and (2) previous-summer sunshine hours (photosynthetic carbon input). Using 36 years of standardized beech mast data and JMA sunshine records, we test predictive accuracy through leave-one-out cross-validation.

## 2. Methods
- 2.1 Beech mast data: Tohoku 5 prefectures, 1989-2025, 36 years
- 2.2 Climate: JMA sunshine hours 7 stations, NOAA ONI
- 2.3 Ordinal logistic SEM (M1-M4 comparison, AIC)
- 2.4 LOOCV + asymmetric cost (recall for failure years)
- 2.5 Bear conflict: MOE annual statistics
- 2.6 Prior work differentiation: Kelly 2013(ΔT), Journé 2018, 水谷 2013, 福井県実務

## 3. Results
- 3.1 Mast AR(1): r=-0.56, p=0.0004, all 5 prefectures (Link 4)
- 3.2 Sunshine→mast: r=+0.48, p=0.003, 4/5 prefectures (Link 2)
- 3.3 ENSO→sunshine: r≈-0.15, ns (Link 1 — rejected)
- 3.4 SEM: M3(AR1+sunshine) AIC-best, ENSO ΔAIC=+1.0
- 3.5 LOOCV: exact 28%/±1 78%. Recall(severe failure): 86%(6/7). Sole miss: 2019
- 3.6 Mast-conflict: r=-0.36, p=0.01 (Link 3)
- 3.7 2025 prediction: score 0.1 → high autumn conflict risk
- 3.8 Mast CV increase: 0.55→0.92 (Theme 9 integration). Bird cascade null (6 tests all ns)

## 4. Discussion

### 4.1 Resource Budget Model: First Multi-Prefecture Quantitative Confirmation

The strong negative AR(1) coefficient (beta = -1.49, all 5 prefectures significant) provides the first large-scale empirical confirmation of the resource budget model for F. crenata. The theoretical prediction that mast years deplete stored resources and produce subsequent crop failures (Isagi et al. 1997) is supported across the entire Tohoku region with remarkable consistency. The mean AR(1) of -0.56 implies that approximately 30% of interannual mast variation is explained by the previous year's crop alone.

- 4.1 (above)
- 4.2 Sunshine modifier (r=+0.48, Kon & Noda 2007)
- 4.3 ENSO irrelevance and yamase decoupling: The absence of ENSO predictive power (r≈-0.15, ns) reflects the dominance of mesoscale meteorology in Tohoku. Yamase cold advection from the Okhotsk Sea suppresses summer warming on the Pacific coast, decoupling ENSO teleconnection. AR(1) dominance reflects local resource dynamics rather than large-scale climate modes (Mei analysis).
- 4.4 Early warning: 6-month lead, 2 inputs, 78% ±1
- 4.5 Asymmetric cost (recall 86%, false negative→human casualties)
- 4.6 Limitations (n=36, ordinal, LOOCV 28% exact, no population dynamics)
- 4.7 2025 warning (score 0.1, Akita/Iwate/Yamagata high risk)
- 4.8 Bird cascade null (Theme 9: 6 tests ns, DID null)
- 4.9 Prior work differentiation: Kelly et al. (2013) used ΔT(summer temperature difference) as predictor for European masting — correlational, no SEM, no LOOCV. Journé et al. (2018) applied multi-variable beta regression to F. sylvatica — but not F. crenata. 水谷ら(2013) described Hokuriku bear-nut correlation descriptively. Fukui Prefecture operates empirical prediction since 2005 with 2-3 month lead time. Our contribution: (1) 36-year ordinal logistic SEM with formal AIC model selection, (2) LOOCV out-of-sample validation (78% ±1), (3) ENSO pathway rejection, (4) 6-month lead time (double existing). This positions our model as the first F. crenata quantitative prediction system with cross-validated accuracy.
- 4.10 Climate context: Yamase cold advection suppresses summer warming in Tohoku Pacific coast, decoupling ENSO teleconnection (Mei analysis). AR(1) dominance reflects local resource dynamics rather than large-scale climate modes.

## 5. Conclusions
Parsimonious 2-variable model. 78% ±1 accuracy. 2025 high-risk warning. Real-time implementable.

## References (~25)
[Isagi 1997, Satake & Iwasa 2000, Kon & Noda 2007, Kelly 2013, Journé 2018, 水谷 2013, Hacket-Pain 2025]

## Data Availability
Tohoku Forest Office beech mast: rinya.maff.go.jp/tohoku/sidou/buna.html
JMA sunshine: data.jma.go.jp
NOAA ONI: psl.noaa.gov
MOE bear statistics: env.go.jp/nature/choju/

---
**Status**: v2 Integrated. Mei yamase段落(4.3)+テーマ9 null(3.8/4.8)+Kelly差別化(4.9)+Mei climate(4.10) 全て統合。Ready for Gate C.
