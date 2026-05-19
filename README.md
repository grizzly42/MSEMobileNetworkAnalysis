# MSE Mobile Network Analysis

Framework for analysis and visualization of LTE/5G mobile network measurements collected during walk tests, tram/public transport measurements, car drive tests, and train corridor measurements across the Czech Republic.

The project focuses on:
- comparison of mobile operators,
- comparison of transport types,
- LTE/5G radio parameter analysis,
- BTS localization,
- mobility analysis,
- visualization of measured routes and radio conditions.

Repository: https://github.com/grizzly42/MSEMobileNetworkAnalysis

---

# Features

- Processing of measurement datasets from:
  - walking tests,
  - tram/public transport measurements,
  - car drive tests,
  - train measurements.
- Support for multiple operators:
  - T-Mobile,
  - Vodafone,
  - O2.
- Route visualization on maps.
- BTS position visualization.
- Heatmap generation.
- KPI evaluation:
  - RSRP,
  - RSRQ,
  - SINR,
  - PCI,
  - EARFCN/NRARFCN,
  - throughput,
  - handovers.
- Comparison of:
  - operators,
  - transport types,
  - routes,
  - mobility scenarios.
- Export of generated figures and results.

---

# Project Structure

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
