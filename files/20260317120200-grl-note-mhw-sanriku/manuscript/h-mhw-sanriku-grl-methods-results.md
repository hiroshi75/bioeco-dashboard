# H-MHW-SANRIKU GRL Note: Methods & Results Draft

**担当**: Rin (rin-climate-model) | **Draft**: 2026-03-17

---

## 2. Data and Methods

### 2.1 Sea Surface Temperature

Monthly SST data were obtained from NOAA Optimum Interpolation SST v2.1 (OISST; Reynolds et al. 2007) for the Sanriku offshore region (40°N, 144°E) over 1982–2025. Both point values and spatial averages over the core domain (38–42°N, 141–147°E) were analyzed.

### 2.2 Climate Mode Indices

Monthly indices of the Pacific Decadal Oscillation (PDO; Mantua et al. 1997), Oceanic Niño Index (ONI; CPC/NOAA), and Atlantic Multidecadal Oscillation (AMO; Enfield et al. 2001) were obtained from NOAA. ONI values lagged by one year (ONI_lag1yr) were included to capture the delayed Rossby wave propagation effect on Kuroshio Extension (KE) dynamics.

### 2.3 Marine Heatwave Detection

MHW events were identified following Hobday et al. (2016). Daily SST climatology and the 90th percentile threshold were calculated from a 30-year baseline (1982–2011) with an 11-day smoothing window. MHW days were defined as periods when daily SST exceeded the 90th percentile for ≥5 consecutive days. MHW categories (Moderate, Strong, Severe, Extreme) follow Hobday et al. (2018).

### 2.4 SST Component Decomposition

To quantify the contribution of large-scale climate modes versus local KE dynamics, quarterly SST was modeled as:

SST(t) = α + β₁·PDO(t) + β₂·ONI(t) + β₃·ONI(t-1yr) + β₄·trend + Σβₖ·season_k + ε(t)

where season_k are quarterly dummy variables (reference: January). The model was estimated using generalized least squares with AR(1) errors (Cochrane-Orcutt procedure) to account for temporal autocorrelation. The residual ε(t) serves as a proxy for the KE meander contribution (KE_index).

The proportion of observed SST anomaly explained by climate modes was calculated for the 2023 July peak as:

Explained = [Predicted(2023 Jul) - Climatology(Jul)] / [Observed(2023 Jul) - Climatology(Jul)]

---

## 3. Results

### 3.1 Marine Heatwave Characterization

The Sanriku offshore region experienced a persistent extreme MHW from 2022 to 2024 (Table 1). In 2023, 79.4% of days exceeded the 90th percentile threshold, qualifying as Hobday Extreme category. Remarkably, 2024 exhibited an even higher exceedance rate of 84.7%, with a maximum SST anomaly of +11.2°C — the largest in the 44-year satellite record. The MHW showed recovery in early 2025, with February SST (7.0°C) approaching the climatological baseline (~5°C).

**Table 1.** MHW summary statistics (30-year baseline, 40°N, 144°E).

| Year | Exceedance (%) | Max anomaly (°C) | Mean anomaly (°C) | Category |
|---|---|---|---|---|
| 2022 | 47.0 | +6.4 | +1.9 | Severe |
| 2023 | 79.4 | +8.7 | +3.7 | Extreme |
| 2024 | 84.7 | +11.2 | +4.8 | Extreme |
| 2025 | 27.1 | +6.6 | +1.8 | Recovery |

### 3.2 SST Component Decomposition

The GLS-AR1 model explained 90% of quarterly SST variance (R² = 0.898, AR(1) ρ = −0.294; Table 2). Seasonal effects dominated, but climate mode coefficients revealed a striking non-standard response:

**Table 2.** GLS-AR1 regression coefficients (n = 175 quarterly records, 1982–2025).

| Variable | β | SE | p |
|---|---|---|---|
| PDO | −0.969 | 0.137 | <0.001 |
| ONI | +0.442 | 0.171 | 0.010 |
| ONI (1-yr lag) | +0.382 | 0.158 | 0.017 |
| Linear trend | +0.016 | 0.011 | 0.145 |

The PDO coefficient was significantly negative (β = −0.969, p < 0.001), indicating that negative PDO phases are associated with SST warming in the Sanriku region — opposite to the canonical PDO response in the broader North Pacific. This reflects the Kuroshio-Oyashio transition zone dynamics, where negative PDO strengthens the subarctic gyre and promotes KE northward meandering, advecting warm subtropical water to the Sanriku coast.

Both contemporaneous ONI (β = +0.442, p = 0.010) and 1-year lagged ONI (β = +0.382, p = 0.017) were significant, consistent with the Rossby wave propagation mechanism linking ENSO to KE instability with a 6–24 month delay.

### 3.3 Kuroshio Extension Dominance

For the July 2023 peak (observed SST = 25.0°C), the decomposition yielded:

- Climatological July mean (1982–2019): 17.8°C
- Total anomaly: +7.2°C
- Climate modes + trend explained: +2.9°C (40%)
- **Residual (KE meander proxy): +4.4°C (60%)**

The most extreme residual occurred in January 2024 (+6.58°C, z = 3.99), when winter SST reached 17.1°C — a value typically observed in October. This winter anomaly exceeding the summer anomaly suggests deep penetration of warm water masses (50–400 m; Sugimoto et al. 2025) that resists winter surface cooling.

The KE_index (residual time series) showed sustained positive values throughout 2022–2024, with a maximum in January 2024, followed by a return toward zero in 2025 — consistent with the SST recovery observed in the Hobday analysis (Section 3.1).

---

*[Draft ready for Mei Introduction/Discussion integration]*
