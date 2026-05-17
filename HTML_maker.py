import os
import matplotlib
import pandas as pd
import numpy as np
import folium
from pathlib import Path
import matplotlib.colors as mcolors
from FilesBTSlocColors import FilesBTSlocColors

# import source data location, results data location a and colors in plot from FilesAndBTS.py
# BRNO
	# WALK: PalackehoVrch; Medlanky; PonavaTM; PonavaVOD; Ponava; SlovanskeNamesti; NamestiSvobodyTM; 
            #NamestiSvobodyVOD; NamestiSvobody; ReckMoravWalk; ZabovreskyO2; ZabovreskyTM; ZabovreskyVOD; ZabovreskyOperators
	# MHD: KolejniVsetinskaCelniKolejni; KolejniVsetinska; CelniKolejni; ReckMoravMHD
	# CAR: ReckMoravCAR
# CZE
	# WALK: ZamberkO2; ZamberkTM; Zamberk; PanskaDolinaO2; PanskaDolinaTM; PanskaDolina
	# CAR: ZamberkKoncinyTM; ZamberkKoncinyVOD; ZamberkKonciny; ZamberkSloupnice; SloupniceZamberk; 
           #TisnovMosty1; TisnovMosty2; TisnovMosty3; TisnovMosty
	#train: DecinBreclavO2; DecinBreclavTM; DecinBreclavVOD; DecinBreclav;	
# Transports: TransportVOD; TransportTM
# in thesis: DecinBreclav, ZabovreskyOperators;  TransportVOD, TransportTM
files, SaveFigLoc, _ ,colors, _ = FilesBTSlocColors("TransportVOD")
SaveFigLoc = SaveFigLoc + "/HTMLview"


LevelMaxRSRP = -50
LevelMinRSRP = -130

# listing of band combinations
BAND_MHz = {
#5G
"N28": "700 MHz",
"N20": "800 MHz",
"N8": "900 MHz",
"N3": "1800 MHz",
"N1": "2100 MHz",
"N38": "2600 MHz",
"N7": "2600 MHz",
"N78": "3500 MHz",
"N48": "3600 MHz",
# 4G
"L1": "2100 MHz",
"L3": "1800 MHz",
"L7": "2600 MHz",
"L8": "900 MHz",
"L20": "800 MHz",
"L38": "2600 MHz",
"L28": "700 MHz",
#2G
"EGSM": "900 MHz",
"PGSM": "900 MHz",
}  


def processOPHTML(file_path, operatorName):
    # loading the file
    data = pd.read_csv(file_path, low_memory=False)
    data["Level"] = pd.to_numeric(data["Level"], errors="coerce")
    if "SNR" in data.columns:
        data["SNR"] = pd.to_numeric(data["SNR"], errors="coerce")
    data["PINGAVG"] = pd.to_numeric(data.get("PINGAVG", np.nan), errors="coerce")
    data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
    data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
    data["Qual"] = pd.to_numeric(data["Qual"], errors="coerce")
    # Filtering redundant data
    if "EVENT" in data.columns and (data["EVENT"] == "PING TEST").any():
        data = data[data["EVENT"] == "PING TEST"]
    data = data[(data["Level"] >= LevelMinRSRP) & (data["Level"] <= LevelMaxRSRP)]
    data = data.dropna(subset=["Latitude", "Longitude"])
    data["Operator"] = operatorName
    return data

# making output directory
baseDirectory = Path(__file__).resolve().parent
resultsDirectory = baseDirectory / SaveFigLoc
resultsDirectory.mkdir(parents=True, exist_ok=True)

dataAll = pd.concat([processOPHTML(f, op) for op, f in files.items()], ignore_index=True)

for op, df_op in dataAll.groupby("Operator"):
    print(f"Právě se zpracovává operátor: {op}")
    LatitudeCentr = df_op["Latitude"].median()
    LongitudeCentr = df_op["Longitude"].median()

  
   # ---------- RSRP ----------
    m_rsrp = folium.Map(location=[LatitudeCentr, LongitudeCentr])
    m_rsrp.fit_bounds([[df_op["Latitude"].min(), df_op["Longitude"].min()], [df_op["Latitude"].max(), df_op["Longitude"].max()]])
    cmap = matplotlib.colormaps["viridis"]
    gradient = [mcolors.to_hex(cmap(i / 255)) for i in range(256)]
    gradient_str = ",".join(gradient)

    RSRPlegend = f"""
    <div style="position: fixed; bottom: 50px; left: 50px;width: 260px; background-color: white; border:2px solid grey; z-index:9999; padding: 10px; font-size:14px;">
    <b>RSRP [dBm]</b><br>
    <div style="width: 220px; height: 20px; background: linear-gradient(to right, {gradient_str});"></div>
    <div style="display:flex; justify-content:space-between;">
    <span>{LevelMinRSRP}</span><span>{(LevelMinRSRP + (LevelMaxRSRP - LevelMinRSRP) * 0.25):.0f}</span><span>{(LevelMinRSRP + (LevelMaxRSRP - LevelMinRSRP) * 0.50):.0f}</span>
    <span>{(LevelMinRSRP + (LevelMaxRSRP - LevelMinRSRP) * 0.75):.0f}</span><span>{LevelMaxRSRP}</span></div></div>
    """
    m_rsrp.get_root().html.add_child(folium.Element(RSRPlegend))
    for _, row in df_op.iterrows():
        RSRPcolor = mcolors.to_hex(matplotlib.colormaps["viridis"](mcolors.Normalize(vmin=LevelMinRSRP,vmax=LevelMaxRSRP)(row["Level"])))
        folium.CircleMarker(location=[row["Latitude"], row["Longitude"]],radius=5,color=RSRPcolor,fill=True,fill_opacity=0.8,
                            popup=folium.Popup(f"""<b>Operátor:</b> {row['Operator']}<br> <b>RSRP:</b> {row['Level']} dBm<br> <b>RSRQ:</b> {row['Qual']} dB<br> <b>SNR:</b> {row['SNR']} dB<br>""",max_width=250)).add_to(m_rsrp)
    m_rsrp.save(os.path.join(SaveFigLoc, f"{op}_RSRP.html"))
    print("RSRP done")
    
    
    
    # ---------- TECH + BAND  ----------
    df_tb = df_op[df_op["BAND"].notna()].copy()
    df_tb["TECH_BAND"] = (df_tb["NetworkTech"].astype(str) + " " + df_tb["BAND"].astype(str) + " (" + df_tb["BAND"].map(BAND_MHz).fillna("?") + ")")
    categories = sorted(df_tb["TECH_BAND"].unique())
    base_colors = ["red","blue","green","purple","orange","brown","pink","cyan"]
    combo_colors = { cat: base_colors[i % len(base_colors)] for i, cat in enumerate(categories)}

    m_tech = folium.Map(location=[LatitudeCentr, LongitudeCentr])
    m_tech.fit_bounds([[df_tb["Latitude"].min(), df_tb["Longitude"].min()], [df_tb["Latitude"].max(), df_tb["Longitude"].max()]])
    for _, row in df_tb.iterrows():
        combo = row["TECH_BAND"]
        band = row.get("BAND", "N/A")
        tech = row.get("NetworkTech", "N/A")
        band_mhz = BAND_MHz.get(band, "?")
        marker_color = combo_colors.get(combo, "black")
        folium.CircleMarker(location=[row["Latitude"], row["Longitude"]], radius=5, color=marker_color, fill=True, fill_color=marker_color, fill_opacity=0.8, 
                            popup=folium.Popup(f"""<b>Operátor:</b> {row['Operator']}<br><b>RSRP:</b> {row['Level']} dBm<br>  <b>RSRQ:</b> {row['Qual']} dB<br><b>SNR:</b> {row['SNR']} dB<br><b>Technologie:</b> {tech}<br><b>Frekvenční pásmo:</b> {band} ({band_mhz})""",max_width=250)).add_to(m_tech)
    legend_html = "<b>Technologie + pásmo</b><br>"
    for cat in categories:
        legend_html += f'<i style="color:{combo_colors[cat]};">●</i> {cat}<br>'

    m_tech.get_root().html.add_child(folium.Element(f"""<div style="position: fixed; bottom: 50px; right: 50px;width: 300px; background:white; border:2px solid grey;
        padding:10px; z-index:9999;">{legend_html}</div>"""))
    m_tech.save(os.path.join(SaveFigLoc, f"{op}_TECH_BAND.html"))
    print("Techband done")
    

    # ---------- PING ----------
    if "PINGAVG" in df_op.columns and df_op["PINGAVG"].notna().any():
        m_ping = folium.Map(location=[LatitudeCentr, LongitudeCentr])
        m_ping.fit_bounds([[df_op["Latitude"].min(), df_op["Longitude"].min()], [df_op["Latitude"].max(), df_op["Longitude"].max()]])
        
        PINGlegend = """<div style="position: fixed;bottom: 50px; left: 50px;width: 240px;background-color: white;border:2px solid grey;z-index:9999;padding: 10px;font-size:14px;">
            <b>PING [ms]</b><br><i style="color:limegreen;">●</i> ≤ 30 ms<br><i style="color:green;">●</i> 30–50 ms<br><i style="color:gold;">●</i> 50–100 ms<br>
            <i style="color:dodgerblue;">●</i> 100–250 ms<br><i style="color:red;">●</i> 250–500 ms<br><i style="color:purple;">●</i> > 500 ms<br><i style="color:black;">✖</i> invalid</div>"""
        m_ping.get_root().html.add_child(folium.Element(PINGlegend))
        
        for _, row in df_op.iterrows():

            val = row["PINGAVG"]

            if pd.isna(val):
                color = "black"
                marker = "x"
            elif val <= 30:
                color = "limegreen"
                marker = "o"
            elif val <= 50:
                color = "green"
                marker = "o"
            elif val <= 100:
                color = "gold"
                marker = "o"
            elif val <= 250:
                color = "dodgerblue"
                marker = "o"
            elif val <= 500:
                color = "red"
                marker = "o"
            else:
                color = "purple"
                marker = "o"

            if marker == "x":
                folium.Marker(location=[row["Latitude"], row["Longitude"]],icon=folium.DivIcon( html='<div style="color:black;font-size:14px;">✖</div>'), 
                              popup=folium.Popup(f"""<b>Operátor:</b> {row['Operator']}<br> <b>RSRP:</b> {row['Level']} dBm<br>  <b>PING:</b> {row['PINGAVG']} ms<br><b>SNR:</b> {row['SNR']} dB<br>""",max_width=250)).add_to(m_ping)
                
            else:
                folium.CircleMarker(location=[row["Latitude"], row["Longitude"]], radius=5, color=color, fill=True, fill_opacity=0.8, 
                popup=folium.Popup(f"""<b>Operátor:</b> {row['Operator']}<br> <b>RSRP:</b> {row['Level']} dBm<br>  <b>PING:</b> {row['PINGAVG']} ms<br><b>SNR:</b> {row['SNR']} dB<br>""",max_width=250)).add_to(m_ping)
               
        m_ping.save(os.path.join(SaveFigLoc, f"{op}_PING.html"))
        print("PING done")
    else:
        print(f" {op}: žádná PING data, tudíž PING mapa nebyla nevytvořena")
    print(f"Hotovo pro {op}")
    
print(" Všechny HTML mapy vytvořeny")