# 査読レポート: Ghost Signals in Phenological Records

## 査読者: Rev-A (Ecology)
## 対象: Paper 5 "Ghost signals in phenological records: Delayed first-detection dates reveal widespread population declines of Japanese insects and amphibians"
## 投稿先: Ecology Letters (Article)
## 査読日: 2026-03-16

---

## Summary（論文の概要と主要な主張）

本論文はJMA（気象庁）の67年間（1953–2020）にわたる生物季節観測データを用い、動物の初検出日（FDD）の遅延が気候変動への応答ではなく、個体群減少による「検出バイアス」（ghost signals）であることを主張する。10種の動物フェノロジーのうち3種が有意な遅延を示し、前進は0種。6つの対立仮説を排除し、Ueta et al. (2025)の独立モニタリングデータで検証している。著者らは、フェノロジーモニタリングが個体群崩壊の早期警報システムとなり得ることを提案する。

---

## Overall Assessment: **Major Revision**

本論文は重要かつ創造的な仮説を提示しており、Ellwood et al. (2012)の先行研究を有意義に拡張している。しかし、統計的手法の一貫性の欠如、独立検証の弱さ、重要な先行研究の欠落など、Major Revisionレベルの修正が必要である。骨格は堅固であり、適切な改訂により高インパクト誌への掲載に値すると考える。

---

## Major Issues（修正必須の重大な問題）

### M1. 統計手法の不一致（Methods vs. Results の齟齬）

統合原稿のMethods (Section 2.3)ではGLS-AR1（Cochrane-Orcutt法）を使用と明記しているが、詳細なMethodsテキスト（paper5_methods_text.md, Section 2.3）ではOLS回帰のみが記述されている。GLS-AR1への言及は統合原稿にのみ存在する。

- **問題**: どちらが実際に実行された解析なのかが不明確
- **影響**: 主要結果（+5.3 days/decade, p < 0.0001）の信頼性に直結
- **改善策**: Methods全体を統一し、OLSとGLS-AR1の両方の結果を本文中で比較報告すること。Table S1にはOLS/GLS両方のデータが含まれているとされるため、本文のMethodsもこれと整合させること

### M2. 独立検証の統計的脆弱性

「独立検証」として提示されているfrog egg massデータは、統計的に十分な裏付けを提供していない：

- *Rana japonica*: −58% decade⁻¹だが p = 0.094（有意でない）
- *R. ornativentris*: −25% decade⁻¹だが p = 0.24（有意でない）
- さらに、JMAフェノロジーデータの対象種は*Dryophytes japonicus*（アマガエル科）であり、検証データは*Rana japonica*（アカガエル科）— 科レベルで異なる

**問題**: 有意でない結果を「独立検証」と呼ぶのは誤解を招く。特にAbstractで「Independent monitoring data confirm widespread declines」と断定的に記述しているが、カエルのデータは統計的に confirm していない。

**改善策**:
1. Abstractの表現を「Independent monitoring data show patterns consistent with...」に弱める
2. ホタルの結果（p = 0.002）は堅固なので、これを主要な独立検証として前面に出す
3. カエルデータは「suggestive but not statistically significant」と明記
4. 種の不一致を制限事項だけでなくResults内でも明示的に議論する

### M3. サンプルサイズの制約と動物-植物比較

動物10現象・植物23現象のFisher's exact test（p = 0.37）は有意でなく、「動物のみが遅延し植物は混合パターン」という中心的主張の統計的根拠は弱い。

- **問題**: 論文の核心的論理構造が統計的に未確認のパターンに依存している
- **改善策**:
  1. 二項検定の結果（0/10 advanced, p = 0.001）をより前面に出す — これは強い証拠
  2. 動物-植物比較を「suggestive pattern」として記述し、Fisher検定の限界を正直に認める
  3. 効果量とconfidence intervalを報告する

### M4. 重要な先行研究の欠落

以下の重要論文が引用されていない：

1. **Roth, Strebel & Amrhein (2014)** "Estimating unbiased phenological trends by adapting site-occupancy models" *Ecology*, 95, 2144-2154 — FADのdetection biasに対する統計的解決策を提案。本論文の核心テーマと直接関連するにもかかわらず未引用。**占有モデルによるバイアス補正を適用していない理由を議論すべき**

2. **Hanmer, Boersch-Supan & Robinson (2022)** "Differential changes in life cycle-event phenology provide a window into regional population declines" *Biology Letters*, 18, 20220186 — フェノロジー変化から個体群減少を推測する研究。本論文の主張と直接的に関連

3. **Dunn & Møller (2014)** "Changes in breeding phenology and population size of birds" *Journal of Animal Ecology*, 83, 729-739 — フェノロジーと個体数の関係を大規模に分析。反証的知見（繁殖フェノロジーの変化は個体数変化と相関しない）を含む

4. **Primack et al. (2023)** "Ten best practices for effective phenological research" *International Journal of Biometeorology*, 67, 1509-1522 — フェノロジー研究のベストプラクティス。参照リストにはPrimack 2023への言及がない

### M5. 「Ghost signals」用語の定義不足

"Ghost signals"は本論文のオリジナル用語と思われるが（Web検索で先行使用は確認できず）、明確な定義が与えられていない。

**改善策**: Introduction内で正式に定義する。例：「We define 'ghost signals' as apparent phenological trends in first-detection dates that arise from changes in detection probability due to population size fluctuations, rather than from actual shifts in the timing of biological events.」

---

## Minor Issues（修正推奨の軽微な問題）

### m1. 相関係数の不一致

統合原稿のSection 3.5では緯度勾配にSpearman順位相関（ρ = 0.49）を使用しているが、Methods（paper5_methods_text.md, Section 2.6）ではPearson相関（r）と記述。統一が必要。

### m2. 都市の定義の不一致

Methods (paper5_methods_text.md)では都市を「population > 1 million（6都市）」と定義しているが、統合原稿では「population > 300,000（12 cities met this criterion, of which 6 had sufficient phenological data）」と記述。正確な基準を統一すること。

### m3. Abstractの数値精度

Abstract内の「+0.052°C yr⁻¹」の温暖化率の出典が不明確。JMA全国平均か、対象ステーション平均か、気象庁の全球データか。データソースを明記すること。

### m4. Figure 2のaggregate vs. station-level slope

Fig. 2キャプションで年次集約回帰（+3.1 days/decade）とstation-level mean（+5.3 days/decade）の乖離が指摘されている。この1.7倍の差異の原因（reporting stationの構成変化）をResults本文内でも議論すべき。読者がどちらの推定値を信頼すべきか判断できるよう、両推定値の長所・短所を記述すること。

### m5. 因果推論の限界の明示

本論文は観察研究であり、6つの対立仮説の排除は相関的証拠に基づく。「population decline as the most parsimonious explanation」は妥当だが、真の因果メカニズム（detectability ∝ population size）を直接検証していない。シミュレーションによる検出バイアスの定量的評価（例：population sizeとFDDの理論的関係のMonte Carloシミュレーション）が加われば格段に説得力が増す。

### m6. Ecology Letters word limitの超過リスク

Draft status noteで~5,000 wordsとされ、Ecology Lettersの制限（5,000 words）ギリギリである。Supplementary MaterialへのMethodsの一部移動を検討すべき。

### m7. Uchida et al. (2025) vs. Ueta et al. (2025)の混乱

参考文献リストに「Uchida et al. (2025) Nature Sustainability」と「Ueta et al. (2025) figshare」の両方が存在する。本文中では一貫して「Ueta et al. (2025)」を使用しているが、実際のNature Sustainability論文の筆頭著者はUchidaである可能性がある（Web検索では著者名に不一致あり）。正確な引用を確認すること。

---

## Strengths（論文の強み）

1. **創造的な仮説**: フェノロジー遅延を検出バイアスとして再解釈するアプローチは独創的で、広範な影響を持つ
2. **系統的な対立仮説排除**: 6つの代替説を個別に検証するアプローチは模範的。各仮説に独立した検定を適用している点が良い
3. **67年間の長期データセット**: Ellwood et al. (2012)の~40年を大幅に拡張
4. **動物・植物の対比**: 検出バイアスが動物にのみ影響するはずという予測と整合するパターン
5. **政策的含意**: JMAの動物フェノロジー観測廃止（2021年）への批判的示唆
6. **透明性**: 非有意結果（Fisher p = 0.37、farmland r = 0.05、frog p = 0.094）を誠実に報告
7. **二項検定の追加**: 0/10の前進ゼロパターンに対する検定（p = 0.001）は強い補完的証拠

---

## Questions for Authors（著者への質問）

1. **GLS-AR1の詳細**: Cochrane-Orcutt反復推定の収束基準は？反復回数の上限は？Prais-Winsten推定との比較は検討したか？
2. **Table S1の13ステーション**: AR(1) > 0.95で第一階差回帰にフォールバックしたとあるが、これらのケースを除外した感度分析の結果は？
3. **ホタルの種名**: 参考文献リストでは*Luciola lateralis*（ヘイケボタル）だが、現在の分類では*Aquatica lateralis*が正式名。統合原稿のAbstractでは*Aquatica*を使用しているが、Results本文では未確認。統一すること
4. **Ecography 2021 Wood frog study**: Discussion 4.1で言及されているが、参考文献リストに含まれていない。フルサイテーションを追加すべき
5. **latitudinal gradient**: 41°N以北のn=4は極めて小さい。Hokkaido結果を「most severe」と記述する根拠として十分か？感度分析（Hokkaido除外）の結果は？

---

## External Review Findings（Web検索による発見）

### 1. Ellwood et al. (2012)との差別化
差別化は概ね適切。4つの改善点（長期データ、多分類群、対立仮説排除、独立検証）は明確に述べられている。ただし、Ellwoodが「提案のみ」で「検証していない」との表現はやや過小評価的。Ellwoodの論文もデータ分析を含んでおり、仮説を裏付ける証拠を提示している。

### 2. JMAデータを使った関連論文
- **Lee et al. (2021)**: "Declining phenology observations by the Japan Meteorological Agency" — JMAの観測廃止に関する通信。本論文の文脈で重要だが未引用
- **Hu et al. (2023)**: Science Advances — 東アジアの昆虫移動バイオマスの減少。引用済み

### 3. 見落とされている重要先行研究
- **Roth, Strebel & Amrhein (2014)**: サイト占有モデルによるバイアスなしフェノロジー推定 — **最も重要な欠落**
- **Sparks & Tryjanowski (2001)**: 引用済みだが、Tryjanowski et al.の後続研究も参照すべき
- **Hanmer et al. (2022) Biology Letters**: フェノロジー差異から個体群減少を推測

### 4. GLS-AR1の妥当性
GLS-AR1は時系列フェノロジーデータの自己相関補正として適切。ただし、Primack et al. (2023)のベストプラクティスや、GAM（一般化加法モデル）による非線形トレンド推定の検討がなされていない。67年の時系列で線形トレンドのみを仮定するのはやや強い前提であり、break-point分析やGAMフィッティングが望ましい。

### 5. "Ghost signals"の用語
Web検索では生態学・フェノロジー文献での先行使用は確認されなかった。地球物理学・信号処理では使われるが、文脈は異なる。本論文のオリジナル用語として使用可能だが、明確な定義が必要（→ M5参照）。

### 6. Ueta et al. (2025)の実態
Web検索で確認したところ、**Uchida et al. (2025) "Biodiversity change under human depopulation in Japan" Nature Sustainability, 8, 883-892** が実際の論文であり、Monitoring Sites 1000のデータを使用。Ueta et al. (2025)はfigshareの生データ。本文中の引用が混乱している可能性がある（→ m7参照）。

---

## Recommendation Summary

| カテゴリ | 評価 |
|---|---|
| 新規性 | ★★★★☆ — Ellwood 2012の有意義な拡張。ghost signalsコンセプトは独創的 |
| 方法論 | ★★★☆☆ — GLS-AR1は適切だが文書内不一致あり。占有モデル未検討 |
| データ品質 | ★★★★☆ — 67年JMAデータは世界的にもユニーク |
| 結論の強さ | ★★★☆☆ — 独立検証が統計的に弱い。因果推論の限界あり |
| 引用の網羅性 | ★★☆☆☆ — Roth 2014、Hanmer 2022、Primack 2023等の重要論文が欠落 |
| 文章品質 | ★★★★☆ — 明瞭で論理的。Ecology Lettersの基準を満たす |

**最終判定: Major Revision** — 上記の問題を解決すれば、Ecology Lettersへの掲載に値する。

---

*Rev-A Ecology, Independent Peer Reviewer, BioEco Agent Lab*
*査読完了: 2026-03-16*
