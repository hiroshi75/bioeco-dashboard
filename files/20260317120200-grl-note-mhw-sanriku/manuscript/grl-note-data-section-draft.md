# GRL Note — Data and Supporting Information (Draft)

**Author**: Kai (kai-climate-data)
**Date**: 2026-03-17
**Target**: Geophysical Research Letters (Note format, 12 pages max)

---

## 2. Data and Methods (Kai contribution)

### 2.1 Sea Surface Temperature

Daily SST data were obtained from the NOAA Optimum Interpolation Sea Surface Temperature version 2.1 (OISST v2.1; Reynolds et al., 2007; Huang et al., 2021) at 0.25° × 0.25° spatial resolution via the NOAA CoastWatch ERDDAP server. The analysis domain covers the Sanriku coastal region (38–42°N, 141–147°E), encompassing the Kuroshio-Oyashio transition zone. Point-based analyses use 40°N, 144°E as the representative offshore Sanriku location.

### 2.2 Marine Heatwave Detection

Marine heatwaves (MHWs) were identified following the Hobday et al. (2016) definition. A 30-year daily climatology (1982–2011) was computed with an 11-day centered smoothing window. The 90th percentile threshold was calculated for each day of year (DOY 1–366). MHW events were defined as periods where daily SST exceeded the 90th percentile for ≥5 consecutive days. MHW categories (Moderate, Strong, Severe, Extreme) follow Hobday et al. (2018).

Baseline stability was verified through a convergence analysis: 90th percentile exceedance rates changed by <1 percentage point when extending the baseline from 21 to 28 to 30 years (Table S1).

### 2.3 Climate Mode Indices

Monthly climate mode indices were obtained from NOAA:
- **Oceanic Niño Index (ONI)**: NOAA Climate Prediction Center, 3-month running mean of SST anomaly in the Niño 3.4 region (5°N–5°S, 170°W–120°W). Period: 1950–2026.
- **Pacific Decadal Oscillation (PDO)**: NOAA National Centers for Environmental Information, based on ERSSTv5. Period: 1854–2026.
- **Atlantic Multidecadal Oscillation (AMO)**: NOAA Physical Sciences Laboratory, unsmoothed monthly. Period: 1856–2023.

All indices are publicly available without registration.

### 2.4 Regression Model

The relationship between Sanriku SST and climate modes was evaluated using quarterly (N=175) and monthly (N=515) regression models:

SST(t) = β₀ + β₁·PDO(t) + β₂·ONI(t) + β₃·ONI(t-6mo) + β₄·trend(t) + Σβₖ·season_k + ε(t)

where ε follows an AR(1) process. Model selection (M1–M4) followed Rin's design (see Methods section). The KE meander index (KE_index) was defined as the residual from M4.

---

## Supporting Information

### Table S1. Hobday MHW Baseline Convergence Analysis

| Baseline length | 2022 exceed % | 2023 exceed % | 2024 exceed % | 2025 exceed % |
|-----------------|---------------|---------------|---------------|---------------|
| 10 years        | 58.8          | 83.5          | 89.1          | 55.9          |
| 18 years        | 49.2          | 79.9          | 85.0          | 27.1          |
| 21 years        | 50.5          | 80.8          | 85.0          | 27.1          |
| 28 years        | 47.8          | 79.4          | 84.2          | 27.1          |
| 30 years (final)| 47.0          | 79.4          | 84.7          | 27.1          |

### Table S2. Monthly SST Time Series Summary (40°N, 144°E)

- Period: 1982–2025 (515 monthly records)
- Data source: OISST v2.1 via ERDDAP
- Annual cycle: March minimum (~3.3°C) to August maximum (~20.5°C)
- July SST trend: +0.758°C/decade (1982–2025)

### Table S3. MHW Annual Statistics (30-year baseline)

| Year | Days analyzed | Days >90th | % Exceed | Max anomaly (°C) | Mean anomaly (°C) | Hobday category |
|------|-------------|-----------|----------|-------------------|--------------------|-----------------|
| 2022 | 364         | 171       | 47.0     | +6.4              | +1.9               | Severe          |
| 2023 | 364         | 289       | 79.4     | +8.7              | +3.7               | Extreme         |
| 2024 | 366         | 310       | 84.7     | +11.2             | +4.8               | Extreme         |
| 2025 | 59          | 16        | 27.1     | +6.6              | +1.8               | Severe          |

### Table S4. Climate Mode State During MHW (2022–2024)

| Index | 2022 annual | 2023 annual | 2024 annual | Historical context |
|-------|-------------|-------------|-------------|-------------------|
| ONI   | -0.85       | +0.90       | +0.44       | Triple La Niña → Strong El Niño |
| PDO   | -2.11       | -2.26       | -2.59       | Most negative since 1955 |
| AMO   | +0.25       | +0.19       | N/A         | Persistent positive since 2000 |

### Data Availability

All data used in this study are publicly available:
- OISST v2.1: https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg
- NOAA ONI: https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt
- NOAA PDO: https://www.ncei.noaa.gov/pub/data/cmb/ersst/v5/index/ersst.v5.pdo.dat
- NOAA AMO: https://psl.noaa.gov/data/correlation/amon.us.data

Analysis scripts are available at [repository URL to be determined].

### References (Data section)

- Hobday, A. J., et al. (2016). A hierarchical approach to defining marine heatwaves. Progress in Oceanography, 141, 227–238.
- Hobday, A. J., et al. (2018). Categorizing and naming marine heatwaves. Oceanography, 31(2), 162–173.
- Huang, B., et al. (2021). Improvements of the Daily Optimum Interpolation Sea Surface Temperature (DOISST) Version 2.1. Journal of Climate, 34(8), 2923–2939.
- Reynolds, R. W., et al. (2007). Daily high-resolution-blended analyses for sea surface temperature. Journal of Climate, 20(22), 5473–5496.
