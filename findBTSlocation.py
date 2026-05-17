# Required imports are insert here
import numpy as np
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path
from pyproj import Transformer
from matplotlib.ticker import FuncFormatter
from FilesBTSlocColors import FilesBTSlocColors

# Suitable datasets for BTS location prediction: PalackehoVrch; Medlanky; PonavaTM; SlovanskeNamesti
           # NamestiSvobodyTM;  KolejniVsetinskaCelniKolejni; ZamberkO2;  PanskaDolinaO2; 
files, SaveFigLoc, real_bts_loc, _ , _ = FilesBTSlocColors("PanskaDolinaO2")
SaveFigLoc = SaveFigLoc + "/findBTSlocation"

# Here select size of figures 
FigSizeSet = (16,10)
# Setting fugure text style to LaTex font and font size
unitFontSize = 20
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "axes.titlepad": 24, "axes.labelsize": unitFontSize, "axes.titlesize": unitFontSize, 
                     "xtick.labelsize": unitFontSize, "ytick.labelsize": unitFontSize, "legend.fontsize": unitFontSize, "figure.titlesize": unitFontSize})
colorsetStyle = "tab20b_r"
# Conversion constant from Timing Advance to meters  https://www.researchgate.net/publication/357642120_Localizing_Basestations_From_End-User_Timing_Advance_Measurements
distTA = 78.125
# Earth radius used for Haversine distance calculation (in meters)
R = 6371000

# Function for preprocessing raw CSV data for each operator
def processOPTA(filePath, nameOP):
    # Load file
    Data = pd.read_csv(filePath, low_memory=False) 
    # Convert TA paramter to number
    Data["TA"] = pd.to_numeric(Data["TA"], errors="coerce")  
    # Convert Node ID paramter to number
    Data["Node"] = pd.to_numeric(Data["Node"], errors="coerce")  
    # Remove rows with missing key values
    Data = Data.dropna(subset=["Longitude","Latitude","TA","Node"])  
    # Delete invalid TA values
    Data = Data[Data["TA"] >= 0]  
    # Add operator label
    Data["Operator"] = nameOP  
    Data["NodeByOP"] = Data["Operator"] + "_" + Data["Node"].astype(int).astype(str)
    return Data


# making output directory
baseDirectory = Path(__file__).resolve().parent
resultsDirectory = baseDirectory / SaveFigLoc
resultsDirectory.mkdir(parents=True, exist_ok=True)

# Load and merge all operator datasets into one DataFrame
processed = [processOPTA(file, op) for op, file in files.items()]
processedAll = pd.concat(processed, ignore_index=True)


# Transformer for converting map coordinates (Web Mercator → WGS84)
transformer = Transformer.from_crs(3857, 4326, always_xy=True)
# Formatter for longitude axis (convert meters → degrees)
def foramtLon(x, pos):
    lon, lat = transformer.transform(x, 0)
    return f"{lon:.4f}°"
# Formatter for latitude axis (convert meters → degrees)
def foramtLat(y, pos):
    lon, lat = transformer.transform(0, y)
    return f"{lat:.4f}°"


# main loop
for op, dataOP in processedAll.groupby("Operator"):
    print(op)
    fig, ax = plt.subplots(figsize=FigSizeSet)
    # Convert measurement points into GeoDataFrame and project to Web Mercator
    GeoData = gpd.GeoDataFrame(dataOP,geometry=gpd.points_from_xy(dataOP["Longitude"],dataOP["Latitude"]),crs="EPSG:4326").to_crs(epsg=3857)

    ## Filtering of BTS stations to which mobile connected 2x or fewer during measurement
    counts = GeoData.groupby("NodeByOP")["TA"].nunique()
    GeoData["valid"] = GeoData["NodeByOP"].map(counts) >= 2
    # Split dataset into valid and invalid nodes for display
    GeoDataValid = GeoData[GeoData["valid"]].copy()
    GeoDataInvalid = GeoData[~GeoData["valid"]].copy()

    # Prepare colors for valid nodes
    node_categories = sorted(GeoDataValid["NodeByOP"].unique())
    GeoDataValid["node_id"] = GeoDataValid["NodeByOP"].astype("category").cat.codes
    cmap_nodes = plt.get_cmap(colorsetStyle).resampled(len(node_categories))

    # Plot valid nodes with categorical colors (circles)
    GeoDataValid.plot( ax=ax, column="node_id",cmap=cmap_nodes,markersize=25,alpha=1,)
    # Plot invalid nodes as black x
    if not GeoDataInvalid.empty:
        GeoDataInvalid.plot(ax=ax,color="black",markersize=25,marker="x")
    handles = [mpatches.Patch(color=cmap_nodes(i),label=f"Node {node.split('_')[1]}")for i, node in enumerate(node_categories)]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.02, 1), frameon=True)
    heatScale = None
    
    
    ## estimation of BTS location
    for node, DataNode in dataOP.groupby("NodeByOP"):
        # Skip nodes with low information data (finding location with less than 3 points is nonsence)
        if len(DataNode) < 2:
            continue
        # Create radius from measured points
        DataNode["radius"] = DataNode["TA"] * distTA

        # Extract coordinates 
        points_lat = DataNode["Latitude"].values
        points_lon = DataNode["Longitude"].values
        radiusTA = DataNode["radius"].values
        countOfTA = pd.Series(radiusTA).value_counts()
        weigth = np.array([1 / countOfTA[r] if r in countOfTA else 1.0 for r in radiusTA])
        weigth /= weigth.sum()
       
        # Define grid boundaries based on measurement spread
        max_radius_m = DataNode["radius"].max()
        margin_deg = max_radius_m / 111000
        # how many grids are used
        resolution = 400
        # Create grid in geographic coordinates
        lonGrid = np.linspace(DataNode["Longitude"].min() - margin_deg,DataNode["Longitude"].max() + margin_deg, resolution)
        latGrid = np.linspace(DataNode["Latitude"].min() - margin_deg,DataNode["Latitude"].max() + margin_deg, resolution)

        LonGrid, LatGrid = np.meshgrid(lonGrid, latGrid)
        intersection_map = np.ones_like(LonGrid, dtype=float)

        # Evaluate likelihood contribution for each measurement
        for i, (plat, plon, r) in enumerate(zip(points_lat, points_lon, radiusTA)):
            dlat = np.radians(LatGrid - plat)
            dlon = np.radians(LonGrid - plon)

            # Haversine formula for distance
            a = (np.sin(dlat / 2) ** 2+ np.cos(np.radians(plat))* np.cos(np.radians(LatGrid))* np.sin(dlon / 2) ** 2)
            dist = 2 * R * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

            TACircleSpread = distTA / 2  
            sigma_ring = np.sqrt((0.15 * r)**2 + TACircleSpread**2 + 30**2)
            # Gaussian likelihood of being on the TA circle
            likelihood = np.exp(-((dist - r) ** 2) / (2 * sigma_ring ** 2))
            intersection_map *= likelihood ** weigth[i]

        # Stabilize values 
        intersection_map = np.log1p(intersection_map)
        intersection_map /= intersection_map.max()

        # Show only most relavant heatmap parts
        threshold = np.percentile(intersection_map, 99.5)
        mask = intersection_map >= threshold

        heat_df = pd.DataFrame({"Longitude": LonGrid[mask], "Latitude": LatGrid[mask], "score": intersection_map[mask]})
        gdf_heat = gpd.GeoDataFrame(heat_df,geometry=gpd.points_from_xy(heat_df["Longitude"],heat_df["Latitude"]),crs="EPSG:4326").to_crs(epsg=3857)
        heatScale = ax.scatter(gdf_heat.geometry.x, gdf_heat.geometry.y,s=22,alpha=0.15,c=gdf_heat["score"],cmap="inferno")

    # Plot real BTS positions for comparison if BTS position is unknown paint it black
    for bts in real_bts_loc:
        lat_real = bts["lat"]
        lon_real = bts["lon"]
        node_real = f"{op}_{bts['node']}"
        if node_real in node_categories:
            color_idx = node_categories.index(node_real)
            node_color = cmap_nodes(color_idx)
        else:
            node_color = "black"   
        gdf_real = gpd.GeoDataFrame( geometry=gpd.points_from_xy([lon_real],[lat_real]),crs="EPSG:4326").to_crs(epsg=3857)
        gdf_real.plot(ax=ax,marker="o",color=node_color,edgecolor="black",markersize=120)
        
    # Add basemap
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.6)
     # Show Longitude and Latitude in degrees
    ax.xaxis.set_major_formatter(FuncFormatter(foramtLon))
    ax.yaxis.set_major_formatter(FuncFormatter(foramtLat))
    ax.tick_params(axis='both')
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    # Add colorbar for heatmap (likelihood scale)
    if heatScale is not None:
       cbar = plt.colorbar(heatScale,ax=ax,orientation="horizontal",pad=0.15,fraction=0.05)
       #cbar = plt.colorbar(heatScale,ax=ax,orientation="vertical",location="left",pad=0.15,fraction=0.05)
    cbar.set_label("Pravděpodobnost polohy BTS")
    cbar.ax.tick_params()
    plt.tight_layout()
    # Save figure as PDF picture
    plt.savefig( f"{SaveFigLoc}/BTS_Heatmap_{op}.pdf", dpi=600, bbox_inches="tight")
    
# print node categories to find real bts location in CZE on web: https://gsmweb.cz/
print(node_categories)
# Display all plots
plt.show()
