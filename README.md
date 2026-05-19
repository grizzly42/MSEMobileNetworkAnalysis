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

# Installation

Clone repository:

```bash
git clone https://github.com/grizzly42/MSEMobileNetworkAnalysis.git
cd MSEMobileNetworkAnalysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Required Python Packages

Example dependencies:

```bash
pip install pandas numpy matplotlib scipy folium geopandas contextily
```

Depending on your scripts, additional libraries may be required.

---

# Usage

Run the main analysis script:

```bash
python main.py
```

Example dataset selection:

```python
dataset = "DecinBreclav"
```

Example available datasets:

```python
"PalackehoVrch"
"Ponava"
"NamestiSvobody"
"ZabovreskyOperators"
"DecinBreclav"
"TransportTM"
"TransportVOD"
```

---

# Example Analyses

## Operator Comparison

Compare:
- coverage,
- signal quality,
- throughput,
- handovers,

between:
- T-Mobile,
- Vodafone,
- O2.

---

## Transport Type Comparison

Compare radio conditions for:
- walking,
- tram/public transport,
- car transport.

---

## BTS Localization

Visualization of:
- real BTS locations,
- estimated BTS positions,
- serving cells,
- handover regions.

---

# Output Examples

Generated outputs may include:
- route maps,
- heatmaps,
- KPI graphs,
- BTS overlays,
- comparison plots,
- statistical summaries.

---

# Thesis Usage

This repository was developed as part of a university thesis focused on mobile network measurement and analysis in mobility scenarios.

Used measurement scenarios include:
- Děčín → Břeclav railway corridor,
- Žabovřesky operator comparison,
- transport type comparison.

---

# Future Improvements

- 5G NSA/SA improvements,
- automatic BTS clustering,
- machine learning for BTS localization,
- interactive dashboards,
- automated report generation,
- real-time measurement support.

---

# Author

Jakub Pachel

---

# License

Add your preferred license here, for example:

```text
MIT License
```

or

```text
GNU GPL v3
```

---

# Citation

If you use this repository in academic work, please cite the related thesis/project.

---

GitHub repository:

https://github.com/grizzly42/MSEMobileNetworkAnalysis
