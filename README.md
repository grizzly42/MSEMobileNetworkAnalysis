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


