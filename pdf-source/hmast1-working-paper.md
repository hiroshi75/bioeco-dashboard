# Predicting bear-human conflict from beech mast cycles and summer sunshine: A parsimonious early warning model for Japan

**Target**: Journal of Applied Ecology
**Version**: v1 Integrated Draft
**Date**: 2026-03-17

---

## Abstract
[From h-mast1-paper-outline.md — ~250 words. AR(1)=-1.49, sunshine=+0.91, LOOCV ±1=78%, recall 86%, 6-month lead time. 2025 severe failure warning.]

## 1. Introduction
[From h-mast1-paper-intro-draft.md — ~370 words. Bear crisis, resource budget model, ENSO hypothesis tested and rejected, parsimonious 2-variable model.]

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
[From h-mast1-paper-discussion-draft.md — ~780 words]
- 4.1 Resource budget model confirmed (β_AR1=-1.49)
- 4.2 Sunshine modifier (r=+0.48, Kon & Noda 2007)
- 4.3 ENSO irrelevance (PJ pattern spatial heterogeneity)
- 4.4 Early warning: 6-month lead, 2 inputs, 78% ±1
- 4.5 Asymmetric cost (recall 86%, false negative→human casualties)
- 4.6 Limitations (n=36, ordinal, LOOCV 28% exact, no population dynamics)
- 4.7 2025 warning (score 0.1, Akita/Iwate/Yamagata high risk)
- 4.8 Bird cascade null (Theme 9: 6 tests ns, DID null)
- 4.9 Kelly/Journé/水谷 differentiation (36yr SEM, LOOCV, ENSO rejection)

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
**Status**: v1 Integrated. Kelly差別化(Mika)+Rin SEM Methods記述を最終統合後にGate C。
