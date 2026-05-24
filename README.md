# MSE Mobile Network Analysis

Interactive analysis and visualization of 4G/5G mobile network measurements collected in real environments across the Czech Republic.

This repository was created as part of the master's thesis:

- **A Comprehensive Analysis of Mobile Signals in 4G/5G Networks**  
- Brno University of Technology — Faculty of Electrical Engineering and Communication  
- Author: Jakub Pachel

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
- tram drive tests,
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

# Interactive Maps

Interactive maps are available through GitHub Pages:

[Open Interactive Maps](https://grizzly42.github.io/MSEMobileNetworkAnalysis/)

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


# The directory contains:

```text
MSEMobileNetworkAnalysis/
│
├── datasets/
│   │
│   ├── Brno/
│   │   │
│   │   ├── CAR/
│   │   │   │
│   │   │   ├── car_reckovice-moravske_namesti_TM.csv
│   │   │   └── car_reckovice-moravske_namesti_VOD.csv
│   │   │
│   │   ├── MHD/
│   │   │   │
│   │   │   ├── tram_celni-kolejni_TM.csv
│   │   │   ├── tram_kolejni-vsetinska_TM.csv
│   │   │   ├── tram_kolejni-vsetinska-celni-kolejni_TM.csv
│   │   │   ├── tram_reckovice-moravske_namesti_TM.csv
│   │   │   └── tram_reckovice-moravske_namesti_VOD.csv
│   │   │
│   │   └── WalkTests/
│   │       │
│   │       ├── walk_Medlanky_TM.csv
│   │       ├── walk_nam_Svobody_TM.csv
│   │       ├── walk_nam_Svobody_VOD.csv
│   │       ├── walk_Palackeho_Vrch_TM.csv
│   │       ├── walk_Ponava_TM.csv
│   │       ├── walk_Ponava_VOD.csv
│   │       ├── walk_reckovice-moravske_namesti_TM.csv
│   │       ├── walk_reckovice-moravske_namesti_VOD.csv
│   │       ├── walk_Technologicke_muzeum-Slovanke_namesti_TM.csv
│   │       ├── walk_Zabovresky_O2.csv
│   │       ├── walk_Zabovresky_TM.csv
│   │       └── walk_Zabovresky_VOD.csv
│   │
│   └── CzechRepublic/
│       │
│       ├── TRAIN/
│       │   │
│       │   ├── train_koridor_Decin_Breclav_O2.csv
│       │   ├── train_koridor_Decin_Breclav_TM.csv
│       │   ├── train_koridor_Decin_Breclav_VOD.csv
│       │   ├── train_UstiNadOrlici_Letohrad_TM.csv
│       │   └── train_UstiNadOrlici_Letohrad_VOD.csv
│       │
│       ├── CAR/
│       │   │
│       │   ├── car_Sloupnice_Zamberk_TM.csv
│       │   ├── car_Tisnov_Mosty_u_Jablunkova_TM_1.csv
│       │   ├── car_Tisnov_Mosty_u_Jablunkova_TM_2.csv
│       │   ├── car_Tisnov_Mosty_u_Jablunkova_TM_3.csv
│       │   ├── car_Zamberk_Konciny_TM.csv
│       │   ├── car_Zamberk_Konciny_VOD.csv
│       │   └── car_Zamberk_Sloupnice_TM.csv
│       │
│       └── WalkTests/
│           │
│           ├── walk_Panska_dolina_O2.csv
│           ├── walk_Panska_dolina_TM.csv
│           ├── walk_Zamberk_O2.csv
│           └── walk_Zamberk_TM.csv
│
├── results/
│   │
│   ├── Brno/
│   │   ├── CAR/
│   │   ├── MHD/
│   │   └── WalkTests/
│   │
│   ├── CR/
│   │   ├── CAR/
│   │   ├── TRAIN/
│   │   └── WalkTests/
│   │
│   ├── ComparisonOperators/
│   │   ├── DecinBreclav/
│   │   └── Zabovresky/
│   │
│   └── ComparisonOfTransport/
│       ├── T-Mobile/
│       └── Vodafone/
│
├── FilesBTSlocColors.py
│
├── HTML_maker.py
│
├── RSRPpredictionMLandInterpolation.py
│
├── ShowDataAndStatictis.py
│
├── findBTSlocation.py
│
└── README.md
    │
    └── Main project documentation and interactive map navigation.
```



