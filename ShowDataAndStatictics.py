# Required imports are insert here
import numpy as np
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from matplotlib.ticker import FuncFormatter, MultipleLocator
from pathlib import Path
from pyproj import Transformer
from mpl_toolkits.axes_grid1 import make_axes_locatable
from FilesBTSlocColors import FilesBTSlocColors

# import source data location, results data location a and colors in plot from FilesAndBTS.py
# BRNO
	# WALK: PalackehoVrch; Medlanky; PonavaTM; PonavaVOD; Ponava; SlovanskeNamesti; NamestiSvobodyTM 
            #NamestiSvobodyVOD; NamestiSvobody; ReckMoravWalk; ZabovreskyO2; ZabovreskyTM; ZabovreskyVOD; ZabovreskyOperators      
	# MHD: KolejniVsetinskaCelniKolejni; KolejniVsetinska; CelniKolejni; ReckMoravMHD
	# CAR: ReckMoravCAR
# CZE
	# WALK: ZamberkO2; ZamberkTM; Zamberk; PanskaDolinaO2; PanskaDolinaTM; PanskaDolina
	# CAR: ZamberkKoncinyTM; ZamberkKoncinyVOD; ZamberkKonciny; ZamberkSloupnice; SloupniceZamberk; 
           #TisnovMosty1; TisnovMosty2; TisnovMosty3; TisnovMosty       
	#train: DecinBreclavO2; DecinBreclavTM; DecinBreclavVOD; DecinBreclav; UstiNadOrliciLetohrad; UstiNadOrliciLetohradVOD; UstiNadOrliciLetohradTM	
# Transports: TransportVOD; TransportVOD
# in thesis: DecinBreclav, ZabovreskyOperators;  TransportVOD, TransportTM

files, SaveFigLoc, _ ,colors, _ = FilesBTSlocColors("UstiNadOrliciLetohradTM")
SaveFigLoc = SaveFigLoc + "/ViewAndStat"

# If you dont wanna use file FilesAndBTS.py you can define your paths here (uncomment and type your paths):
""" 
files = {
    "T-Mobile": "BRNO_data/WALK/TM_Zabovresky.csv",
    "O2": "BRNO_data/WALK/O2_Zabovresky.csv",
    "Vodafone": "BRNO_data/WALK/VOD_Zabovresky.csv"
} 

# Here define lacation whrere you want to save figures as PDF
#SaveFigLoc = "BRNO_vysledky/Zabovresky"

# Color settings for operators
#colors = {'T-Mobile': 'magenta','O2': 'blue','Vodafone': 'red'}
"""

# if 0 title is hide / if 1 title is shown
FlagShowFiguresTitle  = 0
# if 0 cbar is on right side / if 1 cbar is on bottom
cbarBot = 1

# DPI of PDF
DPIset = 600
# Limit RSRP values
LevelMaxRSRP = -50
LevelMinRSRP = -130

# Setting the number of bins in histogram
SNRbins = 20
RSRPbins = 20

# setting the size of the figures
FigSizeSet = (18,10)

# Setting fugure text style to LaTex font and font size
unitFontSize = 24
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "axes.titlepad": 24, "axes.labelsize": unitFontSize, "axes.titlesize": unitFontSize, 
                     "xtick.labelsize": unitFontSize, "ytick.labelsize": unitFontSize, "legend.fontsize": unitFontSize, "figure.titlesize": unitFontSize})


## function that does data preprocessing
def processOP(file_path, operatorName):
    # loading the file
    data = pd.read_csv(file_path, low_memory=False)
    if operatorName == "auto":
        data = data.iloc[::-1].reset_index(drop=True)
    
    # Splitting the first column into date and time
    splitColumns = data[data.columns[0]].astype(str).str.split('_', n=1, expand=True)
    splitColumns.columns = ['date', 'time']
    splitColumns['date'] = splitColumns['date'].str.replace('.', '-', regex=False)
    splitColumns['time'] = splitColumns['time'].str.replace('.', ':', n=2, regex=False)
    data = pd.concat([splitColumns, data.drop(columns=[data.columns[0]])], axis=1)
    
    # conversion to numbers
    data["Level"] = pd.to_numeric(data["Level"], errors="coerce")
    if "SNR" in data.columns:
        data["SNR"] = pd.to_numeric(data["SNR"], errors="coerce")
        
    # Filtering redundant data
    if "EVENT" in data.columns and (data["EVENT"] == "PING TEST").any():
        data = data[data["EVENT"] == "PING TEST"]
    # Filtering irrelevant RSRP data
    data = data[(data["Level"] >= LevelMinRSRP) & (data["Level"] <= LevelMaxRSRP)]
    
    # Datetime
    data['datetime'] = pd.to_datetime(data['date'] + ' ' + data['time'], errors='coerce')
    data = data.dropna(subset=['datetime'])
    data = data.sort_values('datetime')
        
    # distance calculation using harvesin's formula
    lat_rad = np.radians(data["Latitude"].values)
    lon_rad = np.radians(data["Longitude"].values)
    R = 6371000
    dlat = np.diff(lat_rad)
    dlon = np.diff(lon_rad)
    a = np.sin(dlat/2)**2 + np.cos(lat_rad[:-1]) * np.cos(lat_rad[1:]) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    dist = np.insert(R * c, 0, 0)
    # distance conversion to kilometers
    data['Distance_km'] = pd.Series(dist).cumsum() / 1000
    data['Operator'] = operatorName
    print(operatorName)
    data["Speed"] = pd.to_numeric(data["Speed"], errors="coerce")
    # print average speed
    print(f"Průměrná rychlost: {data['Speed'].mean():.2f} km/h")
    return data

# making output directory
baseDirectory = Path(__file__).resolve().parent
resultsDirectory = baseDirectory / SaveFigLoc
resultsDirectory.mkdir(parents=True, exist_ok=True)


# Process each file store the resulting DataFrames
dataframes = [processOP(file, op) for op, file in files.items()] 
dataAll = pd.concat(dataframes, ignore_index=True)
# List of all operators 
operators = list(files.keys())

singleOperator = len(operators) == 1
subplotCount = len(operators) if singleOperator else len(operators) + 1

#-------------------------------------------------------------------------------------------------------------------- 
##  Display of RSRP parameter development over time
# search for unique measurement dates (needed when measurements were taken over several days)
all_days = sorted(dataAll['datetime'].dt.date.unique())
for day in all_days: 
    # for each date a subplot of 3 operators and a comparative is drawn
    fig, axes = plt.subplots(subplotCount, 1, figsize=FigSizeSet, sharex=True, sharey=True)
    
    if subplotCount == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
        
    # subplots of 3 operators 
    for i, op in enumerate(operators):
        dataOP = dataAll[dataAll["Operator"] == op]
        dataDay = dataOP[dataOP['datetime'].dt.date == day]
        axes[i].plot(dataDay['datetime'], dataDay['Level'], color=colors[op], linewidth=1)
        axes[i].set_ylabel("RSRP [dBm]")
        axes[i].grid(True)
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))  
    # comparative subplot
    if not singleOperator:
        axesAll = axes[-1]
        for op in operators:
            dataOP = dataAll[dataAll["Operator"] == op]
            dataDay = dataOP[dataOP['datetime'].dt.date == day]
            axesAll.plot(dataDay['datetime'], dataDay['Level'], label=op, color=colors[op], linewidth=1)    
        axesAll.set_xlabel("Čas [hh:mm:ss]")
        axesAll.set_ylabel("RSRP [dBm]")
        axesAll.legend(loc='lower right')
        axesAll.grid(True)  
    else:
        axes[0].set_xlabel("Čas [hh:mm:ss]") 
    if FlagShowFiguresTitle:
        axes[0].set_title(f"RSRP v závislosti na čase - {day}") 
    fig.tight_layout() 
    # save figure in pdf format
    plt.savefig(f"{SaveFigLoc}/RSRPtime_{day}.pdf", bbox_inches="tight")
    
#-------------------------------------------------------------------------------------------------------------------- 
##  Display of RSRP parameter development over distance
fig, axes = plt.subplots(subplotCount, 1, figsize=FigSizeSet, sharex=True, sharey=True)
if subplotCount == 1:
    axes = [axes]
else:
    axes = axes.flatten()
# subplots of operators
for i, op in enumerate(operators):
    dataOP = dataAll[dataAll["Operator"] == op]
    axes[i].plot(dataOP['Distance_km'], dataOP['Level'], color=colors[op])
    axes[i].set_ylabel("RSRP [dBm]")
    axes[i].grid(True)
# comparative subplot
if not singleOperator:
    axesAll = axes[-1]
    for op in operators:
        dataOP = dataAll[dataAll["Operator"] == op]
        axesAll.plot(dataOP['Distance_km'], dataOP['Level'], label=op, color=colors[op])
    axesAll.set_xlabel("vzdálenost [km]")
    axesAll.set_ylabel("RSRP [dBm]")
    axesAll.legend()
    axesAll.grid(True)
    axesAll.locator_params(axis='x', nbins=8)
else:
    axes[0].set_xlabel("vzdálenost [km]") 
if FlagShowFiguresTitle:
    axes[0].set_title("RSRP v závislosti na vzdálenosti")
fig.tight_layout()
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/RSRPdistance.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
##  Display HISTOGRAMS of parameter RSRP
fig, axes = plt.subplots(subplotCount, 1, figsize=FigSizeSet, sharex=True)
if subplotCount == 1:
    axes = [axes]
else:
    axes = axes.flatten()
# subplots of 3 operators
for i, op in enumerate(operators):
    dataOP = dataAll[dataAll["Operator"] == op]
    axes[i].hist(dataOP["Level"].dropna(), bins=RSRPbins, color=colors[op])
    axes[i].set_ylabel("Četnost")
    axes[i].grid(True) 
# comparative subplot
if not singleOperator:
    axesAll = axes[-1]
    for op in operators:
        axesAll.hist(dataAll[dataAll["Operator"] == op]["Level"].dropna(), bins=RSRPbins, histtype='step', linewidth=1.5, color=colors[op], label=op)  
    axesAll.set_xlabel("RSRP [dBm]")
    axesAll.set_ylabel("Četnost")
    axesAll.legend()
    axesAll.grid(True)
else:
    axes[0].set_xlabel("RSRP [dBm]") 
if FlagShowFiguresTitle:
    axes[0].set_title("Histogram parametru RSRP")
fig.tight_layout()
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/HistRSRP.pdf", bbox_inches="tight")



#--------------------------------------------------------------------------------------------------------------------
##  Display BOXPLOTS of parameter RSRP
fig, ax = plt.subplots(figsize=FigSizeSet)
data_box = [dataAll[dataAll["Operator"] == op]["Level"].dropna() for op in operators]
bp = ax.boxplot(data_box, tick_labels=operators, patch_artist=True)
for patch, op in zip(bp['boxes'], operators):
    patch.set_facecolor('none')
    patch.set_edgecolor(colors[op])
    patch.set_linewidth(1.8)
if FlagShowFiguresTitle:
    ax.set_title("Boxplot parametru RSRP")    
ax.set_ylabel("RSRP [dBm]")
ax.grid(True)
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/BoxRSRP.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
## Display HISTOGRAMS of parameter SNR
fig, axes = plt.subplots(subplotCount, 1, figsize=FigSizeSet, sharex=True)
if subplotCount == 1:
    axes = [axes]
else:
    axes = axes.flatten()   
# subplots of operators
for i, op in enumerate(operators):
    dataOP = dataAll[dataAll["Operator"] == op]
    axes[i].hist(dataOP["SNR"].dropna(),bins=SNRbins,color=colors[op])
    axes[i].set_ylabel("Četnost")
    axes[i].grid(True) 
# comparative subplot
if not singleOperator:
    axesAll = axes[-1] 
    for op in operators:
        dataOP = dataAll[dataAll["Operator"] == op]
        axesAll.hist(dataOP["SNR"].dropna(),bins=SNRbins,histtype='step',linewidth=1.5,color=colors[op],label=op)     
    axesAll.set_xlabel("SNR [dB]")
    axesAll.set_ylabel("Četnost")
    axesAll.legend()
    axesAll.grid(True)
else:
    axes[0].set_xlabel("SNR [dB]")
if FlagShowFiguresTitle:
    axes[0].set_title("Histogram parametru SNR")  
fig.tight_layout()
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/HistSNR.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
## Display BOXPLOTS of parameter SNR
fig, ax = plt.subplots(figsize=FigSizeSet)
data_box_snr = [dataAll[dataAll["Operator"] == op]["SNR"].dropna()for op in operators]
bp = ax.boxplot(data_box_snr,tick_labels=operators, patch_artist=True)
for patch, op in zip(bp['boxes'], operators):
    patch.set_facecolor('none')
    patch.set_edgecolor(colors[op])
    patch.set_linewidth(1.8)
if FlagShowFiguresTitle:
    ax.set_title("Boxplot parametru SNR")
ax.set_ylabel("SNR [dB]")
ax.grid(True)
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/BoxSNR.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
## ECDF of RSRP
fig, ax = plt.subplots(figsize=FigSizeSet)
for op in operators:
    dataOP = dataAll[dataAll["Operator"] == op]
    rsrp = dataOP["Level"].dropna()
    # calculation of ECDF of RSRP
    x = np.sort(rsrp.values)
    y = np.arange(1, len(x)+1) / len(x)
    ax.plot(x, y, label=op, color=colors[op], linewidth=2)
if FlagShowFiguresTitle:
    ax.set_title("Empirická distribuční funkce parametru RSRP")  
ax.set_xlabel("RSRP [dBm]")
ax.set_ylabel("Empirická distribuční funkce")
ax.grid(True)
ax.legend()
fig.tight_layout()
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/ECDF_RSRP.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
## ECDF of SNR
fig, ax = plt.subplots(figsize=FigSizeSet)
for op in operators:
    dataOP = dataAll[dataAll["Operator"] == op]
    snr = dataOP["SNR"].dropna()
     # calculation of ECDF of SNR
    x = np.sort(snr.values)
    y = np.arange(1, len(x)+1) / len(x)
    ax.plot(x, y, label=op, color=colors[op], linewidth=2)
if FlagShowFiguresTitle:
    ax.set_title("Empirická distribuční funkce parametru SNR")  
ax.set_xlabel("SNR [dB]")
ax.set_ylabel("Empirická distribuční funkce")
ax.grid(True)
ax.legend()
fig.tight_layout()
# save figure in pdf format
plt.savefig(f"{SaveFigLoc}/ECDF_SNR.pdf", bbox_inches="tight")


#--------------------------------------------------------------------------------------------------------------------
## GPS unit conversion from meters to degrees (for asis of map figures)
transformer = Transformer.from_crs(3857, 4326, always_xy=True)
def foramtLon(x, pos):
    lon, lat = transformer.transform(x, 0)
    return f"{lon:.3f}°"
def foramtLat(y, pos):
    lon, lat = transformer.transform(0, y)
    return f"{lat:.3f}°"


#--------------------------------------------------------------------------------------------------------------------
## RSRP depending on location supported by map
for op, dataOP in dataAll.groupby("Operator"):
    fig, ax = plt.subplots(figsize=FigSizeSet)
    # get our gps location and transfer Longitude and Latitude to Web Mercator (meters) --> basemap require this
    gdf = gpd.GeoDataFrame(dataOP, geometry=gpd.points_from_xy(dataOP["Longitude"], dataOP["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)
    # plot RSRP on location
    
    
    plot = gdf.plot(ax=ax,column="Level",cmap="viridis",markersize=50,legend=False,vmin=-130,vmax=-50)
    # add base map undr trace
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    divider = make_axes_locatable(ax)
    if cbarBot:
        cax = divider.append_axes("bottom", size="5%", pad=0.8)
        cbar = fig.colorbar(plot.collections[0],cax=cax,orientation="horizontal")
        
    else:
        cax = divider.append_axes("right", size="5%", pad=0.8)
        cbar = fig.colorbar(plot.collections[0],cax=cax,orientation="vertical")
    cbar.set_label("RSRP [dBm]", fontsize=20)
    cbar.ax.tick_params(labelsize=18)
    
    ax.set_aspect('equal')
    # Show Longitude and Latitude in degrees
    ax.xaxis.set_major_formatter(FuncFormatter(foramtLon))
    ax.yaxis.set_major_formatter(FuncFormatter(foramtLat))
    #ax.tick_params(axis='y', labelrotation=45)
    if FlagShowFiguresTitle:
        ax.set_title(f"RSRP v závislosti na pozici – {op}")
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    # save figure in pdf format
    plt.savefig(f"{SaveFigLoc}/RSRPmap_{op}.pdf", format="pdf", dpi=DPIset,bbox_inches="tight")
    
    
#--------------------------------------------------------------------------------------------------------------------
## SNR depending on location supported by map
for op, dataOP in dataAll.groupby("Operator"):
    fig, ax = plt.subplots(figsize=FigSizeSet)
    # get our gps location and transfer Longitude and Latitude to Web Mercator (meters) - basemap require this
    gdf = gpd.GeoDataFrame(dataOP, geometry=gpd.points_from_xy(dataOP["Longitude"], dataOP["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)
    # plot SNR on location
    gdf.plot(ax=ax, column="SNR", cmap="viridis", markersize=50, legend=True, vmin=dataAll["SNR"].min(), vmax=dataAll["SNR"].max(), legend_kwds={"label": "SNR [dB]"} )
    # add based map under trace
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    ax.set_aspect('equal')
    # Show Longitude and Latitude in degrees
    ax.xaxis.set_major_formatter(FuncFormatter(foramtLon))
    ax.yaxis.set_major_formatter(FuncFormatter(foramtLat))
    if FlagShowFiguresTitle:
        ax.set_title(f"SNR v závislosti na pozici – {op}")
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    # save figure in pdf format
    plt.savefig(f"{SaveFigLoc}/polohaSNR_{op}.pdf", format="pdf", dpi=DPIset, bbox_inches="tight") 
    
    
#--------------------------------------------------------------------------------------------------------------------  
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
bands2G = {"EGSM", "PGSM"}                   
bands4G = {"L1","L3","L7","L8","L20","L28","L38"}  
bands5G  = {"N1","N3","N7","N8","N28","N38","N78"}  


#-------------------------------------------------------------------------------------------------------------------- 
## Technology and band depending on location with map under
for op, dataOP in dataAll.groupby("Operator"):
    fig, ax = plt.subplots(figsize=FigSizeSet)
    dataOP = dataOP[dataOP["BAND"].notna()].copy()
    dataOP = dataOP[((dataOP["NetworkTech"] == "2G") & (dataOP["BAND"].isin(bands2G))) | ((dataOP["NetworkTech"] == "4G") & (dataOP["BAND"].isin(bands4G))) | ((dataOP["NetworkTech"] == "5G") & (dataOP["BAND"].isin(bands5G)))]
    # create technology band labels to legend
    dataOP["TECH_BAND"] = (dataOP["NetworkTech"].astype(str) + " " + dataOP["BAND"].astype(str) + " (" + dataOP["BAND"].map(BAND_MHz).fillna("?") + ")")
    # get our gps location and transfer Longitude and Latitude to Web Mercator (meters) - basemap require this
    gdf = gpd.GeoDataFrame(dataOP, geometry=gpd.points_from_xy(dataOP["Longitude"], dataOP["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)
    # Create sorted category labels - give theme ID and do colormap  
    categories = sorted(gdf["TECH_BAND"].unique())
    gdf["cat_id"] = gdf["TECH_BAND"].astype("category").cat.codes
    cmap = plt.get_cmap("tab20").resampled(len(categories))
    # plot Technology and band on location
    gdf.plot(ax=ax, column="cat_id", cmap=cmap, markersize=25, categorical=True, legend=False)
     # add map under trace
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    ax.set_aspect("equal")
    # Show Longitude and Latitude in degrees
    ax.xaxis.set_major_formatter(FuncFormatter(foramtLon))
    ax.locator_params(axis='x', nbins=4)
    ax.yaxis.set_major_formatter(FuncFormatter(foramtLat))
    ax.tick_params(axis='y', labelrotation=45)
    if FlagShowFiguresTitle:
        ax.set_title(f"Tachnologie a band v závislosti na pozici – {op}")
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    # Create legend handles
    handles = [mpatches.Patch(color=cmap(i), label=cat) for i, cat in enumerate(categories)]
    # set legend
    #ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.02, 1), frameon=True)
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=True, fontsize=18)   
    # save figure in pdf format
    plt.savefig(f"{SaveFigLoc}/TechBand_{op}.pdf",format="pdf", dpi=DPIset,bbox_inches="tight")
 

#--------------------------------------------------------------------------------------------------------------------
## function of dividing ping into categories
def pingCat(value):
    if value <= 30:
        return "≤ 30 ms"
    elif value <= 50:
        return "30–50 ms"
    elif value <= 100:
        return "50–100 ms"
    elif value <= 250:
        return "100–250 ms"
    elif value <= 500:
        return "250–500 ms"
    else:
        return "> 500 ms"
    
#--------------------------------------------------------------------------------------------------------------------
# Ping classification into categories
if "PINGAVG" in dataOP.columns and dataOP["PINGAVG"].notna().any():
    dataAll["PING_CAT"] = dataAll["PINGAVG"].apply(pingCat)
    # set legend from low PING to high PING
    ordered_categories = ["≤ 30 ms", "30–50 ms", "50–100 ms", "100–250 ms", "250–500 ms", "> 500 ms"]
    dataAll["PING_CAT"] = pd.Categorical(dataAll["PING_CAT"],categories=ordered_categories, ordered=True)
    # set colors to individual categories
    cmap = plt.get_cmap("tab20").resampled(len(ordered_categories))
    ## PING parameter depending on location 
    for op in operators:
        # Filter data and assign ID to ping categories
        dataOP = dataAll[dataAll["Operator"] == op].copy()
        dataOP["ping_id"] = dataOP["PING_CAT"].cat.codes
        fig, ax = plt.subplots(figsize=FigSizeSet)
        # get our gps location and transfer Longitude and Latitude to Web Mercator (meters) - basemap require this
        gdf = gpd.GeoDataFrame(dataOP, geometry=gpd.points_from_xy(dataOP["Longitude"], dataOP["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)
        # plot PING on location
        gdf.plot(ax=ax, column="ping_id", cmap=cmap, categorical=True, markersize=50, legend=False )
        # add map under trace
        ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
        # Set equal scaling for both x and y axes
        ax.set_aspect("equal")
        # Show Longitude and Latitude in degrees
        ax.xaxis.set_major_formatter(FuncFormatter(foramtLon))
        ax.yaxis.set_major_formatter(FuncFormatter(foramtLat))
        if FlagShowFiguresTitle:
            ax.set_title(f"PING v závislosti na pozici – {op}")
        ax.set_xlabel("Zeměpisná délka [°]")
        ax.set_ylabel("Zeměpisná šířka [°]")
        # Create legend handles
        handles = [mpatches.Patch(color=cmap(i), label=cat)
            for i, cat in enumerate(ordered_categories)]
        # set legend
        ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.02, 1), frameon=True)
        # save figure in pdf format
        plt.savefig(f"{SaveFigLoc}/PING_{op}.pdf",format="pdf", dpi=DPIset,bbox_inches="tight")
else:
    print(f" {op}: žádná PING data, tudíž PING mapa nebyla nevytvořena")
    
#plt.show()

print("PDF soubory vytvořeny")
