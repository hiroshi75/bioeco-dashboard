# H-MHW-SANRIKU: GRL Note 論文アウトライン

**作成日**: 2026-03-17 | **リード**: Mei (mei-climate-lead)
**ターゲット**: Geophysical Research Letters (Research Letter)
**制約**: 12ページ（メイン）、4図、Supporting Information可

## タイトル案

**"Unprecedented Persistent Marine Heatwave off Sanriku, Japan (2022–2024): Kuroshio Extension Meander Dominates Over Climate Mode Forcing"**

## 著者

Mei (気候分析), Rin (回帰/モデリング), Kai (データ/MHW検出), Ryo (生態学的文脈), Jim (統括)
+ BioEco Agent Lab

## Abstract (150語以内)

三陸沖で2022-2024に3年間のEXTREME級MHWが発生。30年Hobday基準で2024年の84.7%が90thパーセンタイル超過、最大SST anomaly +11.2°C。SST変動の気候モード分解（GLS-AR1）により、PDO/ENSO/トレンドが40%を説明し、残り60%は黒潮続流(KE)蛇行が支配的であることを示す。注目すべきは(1)β_PDO=-0.97（PDO負→SST上昇）でKOE遷移域の非標準的PDO応答、(2)冬季anomalyが夏季より極端(z=3.99)で深層暖水浸透を示唆、(3)PDO<-1×El Niñoの組み合わせは72年ぶり。2025年初頭にPDO微回復に同期してMHW緩和。PDO位相がMHWの開始・持続・終息を制御する可能性を示唆。

## 1. Introduction (2段落)

### 1.1 MHWの全球的重要性
- 海洋熱波(MHW)の頻度・強度・持続期間が増大（Hobday 2016, Oliver 2018）
- 生態系影響：サンゴ白化、漁業崩壊、海藻林消失
- 北西太平洋は全球的MHWホットスポットの一つ

### 1.2 2022-2024三陸沖MHW
- Sugimoto et al. (2025): KE初の40°N到達、SST+4.9°C、17ヶ月持続
- **本研究の新規性**: (1)Hobday法による正式MHW分類、(2)PDO/ENSO成分分解、(3)KE寄与の定量化、(4)3年間の持続性の確認

## 2. Data and Methods (3段落)

### 2.1 データ
- NOAA OISST v2.1 (0.25°日次, 1982-2025)
- NOAA PDO/ONI/AMO月次インデックス
- Hobday et al. (2016) MHW定義、30年基準期間(1982-2011)

### 2.2 MHW検出
- 30年日次気候値(11日平滑) → 90thパーセンタイル閾値
- ≥5日連続超過 = MHW
- カテゴリ: Moderate/Strong/Severe/Extreme (Hobday 2018)

### 2.3 気候モード分解
- GLS-AR1回帰: SST = β₀ + β₁PDO + β₂ONI + β₃ONI(t-1) + β₄trend + 季節ダミー + ε(AR1)
- KE_index = 残差（PDO/ENSO/トレンドで説明できないSST変動）
- 三陸コア域(40°N, 144°E)の四半期SST (1982-2025, n=175)

## 3. Results (4段落 + 4図)

### 3.1 MHW特性 [Fig 1]
- 2022-2024: 3年間のpersistent extreme MHW
- 2023: 79.4% EXTREME, 2024: 84.7% EXTREME（2024が悪化）
- Max anomaly +11.2°C (2024), mean anomaly +4.8°C (2024)
- 2025年初頭に回復（Feb 27.1%）
- **Fig 1**: SST時系列 + 90th閾値 + MHW期間塗りつぶし

### 3.2 気候モード分解 [Fig 2]
- R²=0.90（季節+気候モード）
- β_PDO = -0.969 (p<0.001): **PDO負→SST上昇（逆符号）**
- β_ONI = +0.442 (p=0.010), β_ONI_lag = +0.382 (p=0.017)
- β_trend = +0.016 (p=0.145, ns)
- **Fig 2**: 観測SST vs 予測SST + 残差(KE_index)

### 3.3 KE蛇行の支配的寄与 [Fig 3]
- 2023 Jul: 気候モード40%説明、KE蛇行60%
- 冬季(2024 Jan) z=3.99 > 夏季(2023 Jul) z=2.68
- **Fig 3**: 成分分解棒グラフ（PDO/ONI/trend/KE成分）

### 3.4 気候レジームの稀少性 [Fig 4]
- PDO<-1.0 × ONI>0.5 = 1950年以降2年のみ(1972, 2023)
- 2024年PDO = -2.594（172年記録最負）
- PDO微回復(-2.59→-1.99)に同期してMHW緩和
- **Fig 4**: PDO-ONI散布図（4象限、2023-2024ハイライト）

## 4. Discussion (3段落)

### 4.1 β_PDO逆符号のメカニズム
- KOE遷移域の特殊性: PDO負→亜寒帯ジャイア強化→KE不安定化→暖水渦
- Qiu & Chen (2005)のKE安定性理論と整合
- 標準的PDO応答（中央冷却/沿岸温暖化）ではなくKE力学が支配

### 4.2 3年間の持続メカニズム
- 暖水渦の深層浸透(50-400m, +10°C) → 正のフィードバック
- PDO負位相の深化(2024年172年最負) → KE北偏促進
- 冬季z=3.99: 大気-海洋結合(+300 W/m²)が暖水維持
- 2025年回復: PDO微回復に同期 → PDOがMHWライフサイクルを制御

### 4.3 含意と今後
- 従来のPDO-SST予測が三陸域で不適切
- PDO負位相が持続する限りMHW再発リスク
- 生態系影響(コンブ壊滅、暖水魚北上)は累積的 → 回復に時間

## 5. Conclusions (1段落)

三陸沖の2022-2024 persistent extreme MHWは、PDO負位相によるKE不安定化（β_PDO=-0.97）とKE蛇行の正フィードバックにより3年間維持された。気候モードが説明できるのは40%に留まり、60%はKE蛇行による。PDO<-1×El Niñoの72年ぶりの気候レジームで発生し、PDO微回復に同期して終息。PDO位相がMHWの全ライフサイクルを制御する新しい知見を提供。

## Supporting Information

- S1: 全四半期のSST時系列 + MHW判定表
- S2: GLS-AR1回帰の診断統計
- S3: ベースライン収束テーブル(10yr→30yr)
- S4: 局別MHW検出結果（複数地点）

## 参考文献（主要15本）

1. Sugimoto et al. (2025) J Oceanography — KE北偏と三陸MHW
2. Hobday et al. (2016) Prog Oceanogr — MHW定義
3. Hobday et al. (2018) Oceanography — MHWカテゴリ
4. Oliver et al. (2018) Nature Comms — 全球MHW増加トレンド
5. Qiu & Chen (2005) J Phys Oceanogr — KE安定性とPDO
6. Loarie et al. (2009) Nature — 気候速度
7. Chust et al. (2024) Nature Comms — 欧州海域tropicalization

## データ可用性

- NOAA OISST v2.1: ERDDAP
- NOAA PDO/ONI/AMO: 公開CSV
- 分析コード: GitHub → Zenodo DOI（受理後）
