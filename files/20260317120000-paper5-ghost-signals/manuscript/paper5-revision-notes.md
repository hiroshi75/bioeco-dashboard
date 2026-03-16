# Paper 5 改訂ノート — Ellwood差別化 + GLS補正

**作成日**: 2026-03-16 | **ステータス**: 改訂中

## Introduction改訂ポイント

### Ellwood et al. (2012) の引用と差別化

追加する段落（Introduction末尾、研究目的の直前に挿入）:

> The possibility that phenological delays in Japanese insects reflect population declines rather than climate maladaptation was first raised by Ellwood et al. (2012), who analyzed ~40 years of JMA phenological records for 14 insect species. They noted that "declining populations may show delayed first appearance dates simply because fewer individuals are present to be detected early in the season," but did not formally test this hypothesis against alternative explanations. Here, we extend their analysis in four key ways: (1) a substantially longer time series (67 years vs. ~40 years) encompassing 33 species across both animals and plants; (2) systematic testing and exclusion of six alternative hypotheses (agricultural abandonment, urbanization, precipitation changes, warming-driven advancement, observer bias, and habitat-specific effects); (3) independent validation using population abundance data from Ueta et al. (2025); and (4) identification of taxon-specific vulnerability patterns (paddy-dependent species declining 2× faster) and a latitudinal gradient (Hokkaido most severely affected).

### Methods改訂

- OLS → "Generalized Least Squares with first-order autoregressive errors (GLS-AR1), estimated via the Cochrane-Orcutt procedure"
- "To assess the impact of temporal autocorrelation, we report both OLS and GLS results (Supplementary Table S1). For species where the Durbin-Watson test indicated significant autocorrelation (DW < 1.5 or > 2.5), GLS estimates were used as the primary result."

### Results改訂

- "Of 33 species, 9 showed significant phenological trends after GLS correction (compared to 10 under OLS). Three species lost significance after autocorrelation correction (species 002, 054, 114), while two gained significance (species 009, 011). Core results—including the strong delay in Japanese tree frog first-calling (+5.3 days/decade, GLS p < 0.0001)—were robust to autocorrelation correction."
- Fisher meta-analysis p値: GLS版で再計算待ち。p>0.05の場合は「動物-植物差はstatistically non-significantだが方向性は一貫」に修正

### Discussion改訂

- "Our findings provide the first large-scale, multi-taxon confirmation of the hypothesis raised by Ellwood et al. (2012) that phenological delays in Japanese insects and amphibians reflect population declines rather than climate maladaptation."
- 追加代替仮説: "We were unable to test for effects of artificial light at night, pesticide use, or invasive species due to lack of site-level data for these variables. These remain important avenues for future research."

### Fisher GLS版結果（Ken完了）
- 全種: chi2=231.2, p<0.0001 → **結論不変**
- 動物: chi2=124.1, p<0.0001
- 植物: chi2=107.1, p<0.0001
- 「動物-植物方向対比」のp=0.37はGLS版でも要再計算だが、方向自体は不変
- species 043: GLS収束失敗→外れ値フラグ付けで対処

### 改訂残タスク
- [x] GLS/ARMA補正（Ken完了）
- [x] Fisher meta-analysis GLS版（Ken完了、結論不変）
- [ ] species 043個別確認（Ken）
- [ ] Ellwood差別化（Mika進行中）
- [ ] Intro/Discussion改訂（Ryo — 本ファイルの改訂ポイントに基づき着手）
- [ ] ゲートC再評価（Yui）

## 差別化テーブル（Mika作成待ち、暫定版）

| 項目 | Ellwood 2012 | 本論文 |
|---|---|---|
| データ期間 | ~40年 | 67年（1953-2020） |
| 種数 | 14昆虫 | 33種（昆虫+両生類+植物） |
| 仮説検証 | 仮説提起のみ | 6代替仮説を体系的に排除 |
| 個体数検証 | なし | Ueta 2025データで独立検証 |
| 統計手法 | OLS | GLS-AR1（自己相関補正） |
| 空間パターン | なし | 緯度勾配（r=0.49, 北海道最深刻） |
| 種別パターン | なし | 水田依存種の選択的2倍速減少 |
