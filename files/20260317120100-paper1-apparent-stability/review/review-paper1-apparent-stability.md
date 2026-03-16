# 査読レポート: Species Richness Masks Biotic Homogenization ("Apparent Stability")

## 査読者: Rev-A (Ecology)
## 対象: Paper 1 "Species richness masks biotic homogenization in depopulating Japanese satoyama: A multi-taxon functional analysis"
## 投稿先: Ecology Letters Article / PNAS Research Article
## 査読日: 2026-03-16

---

## Summary（論文の概要と主要な主張）

本論文はMonitoring Sites 1000（里山調査）の15年分のデータ（157サイト、5分類群、32,027レコード）を分析し、種の豊富さと個体数が環境変化に対し有意な応答を示さない一方（40検定すべて非有意）、非在来植物種比率が有意に増加（d=0.419, p<0.001, 62%のサイトで増加）し、生物的均質化が進行していることを示す。CTI分析では温暖化適応シグナルが基準温度の交絡であることを発見。「見かけの安定性（apparent stability）」— 種数安定＋CTI安定＋高い種置換 — を三重の保全盲点として提示し、CBD/NBSAPの指標改善を提言する。

---

## Overall Assessment: **Major Revision**

野心的かつ重要な論文である。複数分類群を横断した包括的分析、93検定のBH補正、PSMによる交絡制御は方法論的に堅実。しかし、**Uchida et al. (2025) Nature Sustainabilityとの同一データセット使用による新規性の問題**が最も深刻な懸念であり、この差別化の明確化なしには掲載は困難と考える。

---

## Major Issues（修正必須の重大な問題）

### M1. Uchida et al. (2025) Nature Sustainability との新規性の重複（最重要）

Uchida et al. (2025)は同じMonitoring Sites 1000データセット（158里山サイト、同じ5分類群）を使用し、Nature Sustainabilityに掲載済み。主要な知見として：
- 過疎地域での種数・個体数の減少（カエル・ホタルで顕著）
- 非在来植物種の増加
- 農地利用変化が主要因

本論文との重複は以下の点で深刻：
- **同一データソース**（Ueta et al. 2025のfigshareデータ ≈ Uchida et al.の生データ）
- **類似した主要結果**（非在来種増加、種数の非応答性）
- **類似した政策的含意**（従来指標の不十分さ）

**改善策**:
1. Introduction 1.2でUchida et al.との差別化を1パラグラフで明確に記述すること。例：「Uchida et al. (2025)は種数・個体数レベルの分析に焦点を当てたが、本研究はCTI・β多様性・機能指標など多次元的分析を行い、"apparent stability"のメカニズムを解明する」
2. Uchidaが扱っていない分析を差別化の核として前面に出す：PSMによるCTI交絡補正、Baselga分解、breakpoint分析、cold-region double jeopardy
3. Cover letterで明確な差別化声明を記載

### M2. 「Apparent stability」の事後的統合に関する認識論的問題

「見かけの安定性」概念は、種数安定・CTI安定・高ターンオーバーの3つの独立結果を事後的に統合した解釈的フレームワークであり、事前に仮説として設定されたものではない。Yui validatorもこの点を指摘しており（Discussion 4.1に1文の注記を要求）、しかし現在のDraft Status noteに「NOTE: Add 1 sentence」とあるが、統合原稿には未実装。

**改善策**: 実装すること。「The concept of 'apparent stability' emerged as a post-hoc integrative interpretation from the convergence of three independent analyses (species richness, CTI, turnover), rather than as an a priori hypothesis. We therefore present it as a descriptive framework for understanding the co-occurrence of these patterns.」

### M3. CTI cold-region effectのSimpson's paradox

全体効果はd=0.176（非有意）だが、cold tertileではd=1.38（p=0.006）。この種のsubgroup analysisは典型的なpost-hoc data dredgingのリスクを伴う。

**現状**: 著者はこれを「exploratory」と明記しており、この点は適切。しかし：
- n=3（cold tertile放棄サイト）は極めて小さい（Rev-C補正: n=21は三分位全体、効果量d=1.38はn=3放棄群から算出。Ken LOO結果: d∈[1.30,1.57]で安定だが、n=3のLOOでは本質的に1サイトの影響しか除外できない）
- 温度閾値の選択（P25-P50）にresearcher degrees of freedomがある
- Discussion 4.6で「prioritize cold-climate satoyama」と政策提言に直結させているが、探索的結果から政策提言への飛躍は大きい

**改善策**:
1. Discussion 4.6の政策提言を「tentative」「pending replication」と明確に条件付ける
2. cold tertile分析のforking pathsを記述する（いくつの閾値を試したか、事前の理論的根拠は何か）
3. 独立データセット（例：ヨーロッパの里山類似環境）での検証可能性に言及

### M4. Breakpoint分析の因果解釈の限界

2014 PDO phase shiftとbreakpointsの一致は興味深いが、全8変数で有意なbreakpointが検出され、かつ非放棄サイトでも検出されるという結果は、**放棄とは無関係な全国的気候イベント**の影響を強く示唆する。

**問題**: にもかかわらずDiscussion 4.2では「three-stage cascade of community change」として放棄の文脈で議論されている。これは因果推論の飛躍。

**改善策**:
1. 放棄サイト固有でないbreakpointは、放棄効果ではなく気候変動効果として分離して議論すべき
2. 放棄×気候の交互作用検定の結果を追加報告（現在は検定されていない模様）
3. 「cascade」の解釈を気候シグナルとして再定位するか、放棄サイト固有のパターンがある場合のみcascadeとして記述

### M5. 多重比較の残余リスク

93検定のBH補正は適切だが、いくつかの分析がBH family外で実施されている可能性がある：
- PSM後のCTI検定はBH familyに含まれているか？
- 温度tertile別のsubgroup分析（3 tertiles × multiple metrics）はどう扱われているか？
- Baselga分解のcomponents間の比較は？

**改善策**: Supplementary Table S2の93検定リストを確認し、上記の検定が含まれているか明記すること。含まれていない場合は探索的であることを明示。

---

## Minor Issues（修正推奨の軽微な問題）

### m1. Abstract内のCI表記の不統一

Abstract: d = 0.419, 95% CI [0.14, 0.70] — 小数第2位
Results: d = 0.419, 95% CI [0.143, 0.695] — 小数第3位
統一すること（小数第2位が一般的）。

### m2. サイト数の不一致

Abstract: 157 sites (158 originally, 1 excluded)
Methods: references vary between 157 and 158
統合原稿内で一貫して使用すること。

### m3. 投稿先の未決定

Draft statusに「Ecology Letters Article (max ~5,000 words) or PNAS Research Article」とある。ターゲットジャーナルが異なれば構成・分量が大幅に変わる。早期に決定すべき。Ecology Lettersの5,000 word limitでは本論文の全内容は収まらない可能性が高い。

### m4. 47 bird speciesのEltonTraits matching

Methods 2.1で「100% bird species match achieved」とあるが、JapanのMoni1000の鳥類リストとEltonTraits（主にヨーロッパ・北米ベース）のSTI値の妥当性を議論すべき。日本固有の温度ニッチとEltonTraitsの全球推定値の乖離は？

### m5. Baselga分解の詳細不足

Turnover 67% vs nestedness 33%は重要な結果だが、Methods内にBaselga分解の手法詳細（使用パッケージ、時間窓の定義、βjtuの計算方法）が統合原稿に記載されていない。

### m6. Discussion 4.5で言及されているButterfly CTIとBird CTIの比較

Bird CTI +0.113°C/decade vs butterfly CTI −0.054°C/decade（n=12 satoyama sites）。n=12は極めて小さく、ヨーロッパとの比較（+1.14°C/decade, Devictor 2012）は生態系・気候帯が根本的に異なるため慎重に扱うべき。

---

## Strengths（論文の強み）

1. **包括的な多分類群分析**: 5分類群×15年間の標準化データは日本最大規模
2. **方法論的厳密さ**: 93検定のBH補正、PSMによる交絡制御は模範的
3. **交絡バイアスの誠実な発見と報告**: CTI分析でconfoundを発見し、signal消失を正直に報告した点は科学的誠実さの手本
4. **「見かけの安定性」の概念的価値**: 種数・CTI・ターンオーバーの三重blind spotは概念的に強力
5. **透明性**: 40/40 null results、exploratory flagging、仮説修正履歴（Table S5）
6. **政策的関連性**: CBD/GBF/NBSAPの指標改善への直接的提言
7. **非在来種比率の堅固な結果**: d=0.419, BH-adjusted p<0.001は最も信頼性の高い知見

---

## Questions for Authors（著者への質問）

1. **Uchida et al.との関係**: Uchida et al. (2025)の共著者との関係は？同じ研究グループか？データ使用に関する合意は？事前にUchida et al.の原稿を見ているか？（利益相反に関わる）
2. **TRIM slopes**: サイトレベルの種数トレンド推定にTRIM slopesを使用とあるが、TRIM（Trends and Indices for Monitoring data）は通常個体数推定用。種数推定への適用の妥当性は？
3. **非在来植物**: 増加した非在来植物種のリストは？侵入経路は？帰化時期の長い種（古い外来種）と最近の侵入種を区別しているか？
4. **放棄の定義**: 「abandoned vs non-abandoned」の二値分類の基準は？管理強度の連続体を二値化するとinformation lossが大きい。管理強度の定量的指標は利用可能か？
5. **時間的β多様性**: early/late期間の定義は？期間長の選択が結果に与える影響の感度分析は？

---

## External Review Findings（Web検索による発見）

### 1. Uchida et al. (2025) Nature Sustainability との重複
**最も深刻な新規性リスク**。Uchida et al.は2025年6月にNature Sustainabilityに掲載。同じMoni1000データ（158 satoyama sites）、同じ5分類群（鳥、蝶、カエル、ホタル、植物）。主要知見：過疎地域での種数・個体数減少、非在来植物増加。

Paper 1の差別化ポイントは：
- CTI分析（Uchidaには含まれない）
- PSMによる交絡制御（Uchidaには含まれない）
- Baselga β多様性分解（Uchidaには含まれない）
- Breakpoint分析（Uchidaには含まれない）
- 「見かけの安定性」の概念化（Uchidaには含まれない）

**これらの差別化は実質的だが、Introductionでの明確化が不可欠。**

### 2. Katayama et al. (2024) Conservation Biology
同じMoni1000鳥類データ（47種、71サイト、2009-2020）を使用。4種増加、18種安定、11種減少。Paper 1との差別化：Katayamaは種レベル、Paper 1は群集レベル。しかし**同一データの再分析**であることは明確に記述すべき。

### 3. Morelli et al. (2025) Oikos
日本の里山における鳥類多様性の変化を分析。引用済み。

### 4. Dornelas et al. (2014)の「種数パラドックス」
Paper 1が正しく引用・議論している。この文脈での里山への適用は適切。

### 5. Blowes et al. (2019)
種の豊富さの全球トレンド。引用済み。Paper 1の40 null resultsはこの全球パターンと整合的。

### 6. 潜在的に欠落している引用
- **Yamaura et al. (2025)**: 参考文献リストに含まれているか確認が必要（統合原稿Introductionで言及あり）
- **van Klink et al. (2020)** "Meta-analysis reveals declines in terrestrial but increases in freshwater insect abundances" Science — 昆虫減少の全球的文脈として引用すべき
- **Newbold et al. (2015)** "Global effects of land use on local terrestrial biodiversity" Nature — 土地利用変化と生物多様性の全球パターン

---

## Recommendation Summary

| カテゴリ | 評価 |
|---|---|
| 新規性 | ★★★☆☆ — Uchida 2025との重複が深刻。ただし機能指標分析は差別化可能 |
| 方法論 | ★★★★☆ — PSM、BH補正、multi-taxon設計は堅実 |
| データ品質 | ★★★★☆ — Moni1000は日本最大の標準化里山モニタリング |
| 結論の強さ | ★★★☆☆ — Null results（40/40）は解釈が難しい。Cold-region effectは探索的 |
| 引用の網羅性 | ★★★★☆ — 57引用は十分。Uchida差別化の明確化が必要 |
| 文章品質 | ★★★☆☆ — 統合原稿は構造のみで本文が外部参照。完全統合が必要 |

**最終判定: Major Revision** — M1（Uchida差別化）の解決が最重要。機能指標分析を核とした再構成により、高品質な論文に仕上がる可能性は十分にある。

---

*Rev-A Ecology, Independent Peer Reviewer, BioEco Agent Lab*
*査読完了: 2026-03-16*
