# MSE Mobile Network Analysis

Interactive analysis and visualization of 4G/5G mobile network measurements collected in real environments across the Czech Republic.

This repository was created as part of the master's thesis:

> **A Comprehensive Analysis of Mobile Signals in 4G/5G Networks**  
> Brno University of Technology — Faculty of Electrical Engineering and Communication  
> Author: Jakub Pachel :contentReference[oaicite:0]{index=0}

The project focuses on:
- mobile network coverage analysis,
- signal quality evaluation,
- operator comparison,
- mobility analysis,
- geographical visualization of measurements,
- BTS localization,
- interpolation and machine learning prediction methods.

Measurements were performed using smartphones and the G-NetTrack application during:
- train measurements,
- car drive tests,
- tram/public transport measurements,
- walk tests.

Measured and analyzed parameters include:
- RSRP,
- RSRQ,
- SNR,
- PING,
- LTE/5G technologies,
- frequency bands,
- Timing Advance (TA).

---

# Repository Content

## Python Code

The repository contains Python scripts for:
- measurement data processing, statistical analysis, plotting and visualization
- interactive HTML maps,
- interpolation methods and machine learning prediction models,
- BTS position estimation.


Implemented methods include:
- nearest neighbor interpolation,
- bilinear and cubic interpolation,
- kriging,
- linear regression,
- ridge regression,
- random forest,
- XGBoost.

---
# Thesis Overview

The thesis focuses on practical analysis of real mobile network measurements in 4G and 5G networks using commonly available devices.

The work combines:
- RF signal analysis,
- statistical processing,
- geographical visualization,
- interpolation methods,
- machine learning approaches.

The project also investigates:
- BTS localization using Timing Advance,
- prediction of spatial RSRP distribution,
- comparison of operators and mobility scenarios.

---

# Author

Jakub Pachel

Brno University of Technology  
Faculty of Electrical Engineering and Communication  
Department of Radio Electronics



```text
MSEMobileNetworkAnalysis/
│
├── datasets/
│   ├── Brno/
│   │   ├── WalkTests/
│   │   ├── MHD/
│   │   └── CAR/
│   │
│   └── CzechRepublic/
│       ├── TRAIN/
│       ├── CAR/
│       └── WalkTests/
│
├── results/
│
├── src/
│
├── main.py
└── README.md
```

---

# Supported Measurement Scenarios

## Brno

### Walk Tests
- Palackého vrch
- Medlánky
- Ponava
- Slovanské náměstí
- Náměstí Svobody
- Řečkovice → Moravské náměstí
- Žabovřesky

### Public Transport (MHD)
- Kolejní → Vsetínská → Celní → Kolejní
- Řečkovice → Moravské náměstí

### Car Drive Tests
- Řečkovice → Moravské náměstí

---

## Czech Republic

### Walk Tests
- Žamberk
- Panská dolina

### Car Drive Tests
- Žamberk → Končiny
- Žamberk → Sloupnice
- Sloupnice → Žamberk
- Tišnov → Mosty u Jablunkova

### Train Measurements
- Děčín → Břeclav corridor
- Ústí nad Orlicí → Letohrad

---


# Interactive Maps
Interactive maps are available through GitHub Pages.

## Brno — CAR

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/CAR/Reckovice-MoravskeNamesti/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/CAR/Reckovice-MoravskeNamesti/HTMLview/T-Mobile_TECH_BAND.html)

### Vodafone

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/CAR/Reckovice-MoravskeNamesti/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/CAR/Reckovice-MoravskeNamesti/HTMLview/Vodafone_TECH_BAND.html)

---

# Brno — MHD

## Celni-Kolejni

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Celni-Kolejni/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Celni-Kolejni/HTMLview/T-Mobile_TECH_BAND.html)

---

## Kolejni-Vsetinska

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Kolejni-Vsetinska/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Kolejni-Vsetinska/HTMLview/T-Mobile_TECH_BAND.html)

---

## Reckovice-MoravskeNamesti

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Reckovice-MoravskeNamesti/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Reckovice-MoravskeNamesti/HTMLview/T-Mobile_TECH_BAND.html)

### Vodafone

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Reckovice-MoravskeNamesti/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/MHD/Reckovice-MoravskeNamesti/HTMLview/Vodafone_TECH_BAND.html)

---

# Brno — Walk Tests

## Medlanky

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Medlanky/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Medlanky/HTMLview/T-Mobile_TECH_BAND.html)

---

## NamestiSvobody

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/NamestiSvobody/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/NamestiSvobody/HTMLview/T-Mobile_TECH_BAND.html)

### Vodafone

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/NamestiSvobody/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/NamestiSvobody/HTMLview/Vodafone_TECH_BAND.html)

---

## PalackehoVrch

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/PalackehoVrch/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/PalackehoVrch/HTMLview/T-Mobile_TECH_BAND.html)

---

## Ponava

### T-Mobile

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Ponava/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Ponava/HTMLview/T-Mobile_TECH_BAND.html)

### Vodafone

- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Ponava/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/Brno/WalkTests/Ponava/HTMLview/Vodafone_TECH_BAND.html)

---

# Comparison Operators

## O2

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/O2_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/O2_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/O2_TECH_BAND.html)

## T-Mobile

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/T-Mobile_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/T-Mobile_TECH_BAND.html)

## Vodafone

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/Vodafone_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/ComparisonOperators/DecinBreclav/HTMLview/Vodafone_TECH_BAND.html)

---

# CR — TRAIN

## O2

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/O2/HTMLview/O2_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/O2/HTMLview/O2_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/O2/HTMLview/O2_TECH_BAND.html)

## T-Mobile

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/T-Mobile/HTMLview/T-Mobile_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/T-Mobile/HTMLview/T-Mobile_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/T-Mobile/HTMLview/T-Mobile_TECH_BAND.html)

## Vodafone

- [PING](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/Vodafone/HTMLview/Vodafone_PING.html)
- [RSRP](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/Vodafone/HTMLview/Vodafone_RSRP.html)
- [TECH BAND](https://grizzly42.github.io/MSEMobileNetworkAnalysis/CR/TRAIN/DecinBreclav/Vodafone/HTMLview/Vodafone_TECH_BAND.html)
