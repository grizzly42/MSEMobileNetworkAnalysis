# imports needed for code 
import numpy as np
import pandas as pd
import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
from pathlib import Path
from pyproj import Transformer
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import griddata
from pykrige.ok import OrdinaryKriging
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error, r2_score
from FilesBTSlocColors import FilesBTSlocColors

# If you want to set the input data and save location manually uncomment this:
""" # Define input datasets location
files = {"Vodafone": "BRNO_data/WALK/VOD_Ponava.csv"}
# Define location to save results
SaveFigLoc = "BRNO_vysledky/VOD_Ponava_res" 
SplitPoint = 0.65
Colors = {'Vodafone': 'red'}
"""

# Suitable datasets for prediction:PonavaTM; PonavaVOD; Ponava; NamestiSvobodyTM; NamestiSvobodyVOD; NamestiSvobody; 
#                                  ZabovreskyO2; ZabovreskyTM; ZabovreskyVOD; ZabovreskyOperators
files, SaveFigLoc, _ ,colors, SplitPoint= FilesBTSlocColors("PonavaTM")
SaveFigLoc = SaveFigLoc + "/PredictRSRPmap"


# define limits values of RSRP value
LevelMaxRSRP = -50
LevelMinRSRP = -130

# if 0 title is hide / if 1 title is shown
FlagShowFiguresTitle  = 0
# define dimesion of figure windows
SizeOfFigures = (16, 10)
# Setting fugure text style to LaTex font and font size
unitFontSize = 20
plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "axes.titlepad": 24, "axes.labelsize": unitFontSize, "axes.titlesize": unitFontSize, 
                     "xtick.labelsize": unitFontSize, "ytick.labelsize": unitFontSize, "legend.fontsize": unitFontSize, "figure.titlesize": unitFontSize})

baseDirectory = Path(__file__).resolve().parent
resultsDirectory = baseDirectory / SaveFigLoc
resultsDirectory.mkdir(parents=True, exist_ok=True)

# function to pre porcess data
def processOPML(filePath, nameOP):
    Data = pd.read_csv(filePath, low_memory=False)
    # numeric conversion
    for col in ["Level", "SNR", "Qual", "Speed"]:
        Data[col] = pd.to_numeric(Data[col], errors="coerce")
    for i in range(1, 7):
        Data[f"NRxLev{i}"] = pd.to_numeric(Data[f"NRxLev{i}"], errors="coerce")
    # remove invalid values
    Data = Data[(Data["Level"] >= LevelMinRSRP) &(Data["Level"] <= LevelMaxRSRP)]
    Data = Data.dropna(subset=["Longitude", "Latitude", "Level", "SNR", "Qual", "Speed"])
    # feature engineering
    centerLat = Data["Latitude"].mean()
    centerLon = Data["Longitude"].mean()
    Data["distCentr"] = np.sqrt((Data["Latitude"] - centerLat)**2 +(Data["Longitude"] - centerLon)**2) * 111000
    Data["SNRxQual"] = Data["SNR"] * Data["Qual"]
    Data["logDist"] = np.log1p(Data["distCentr"])

    # neighbouring cells
    neighCell = [f"NRxLev{i}" for i in range(1, 7)]
    Data["neigthMean"] = Data[neighCell].mean(axis=1)
    Data["neigthMax"]  = Data[neighCell].max(axis=1)
    Data["neigthStd"]  = Data[neighCell].std(axis=1)
    for col in neighCell:
        Data[col] = Data[col].fillna(Data["neigthMean"])
    Data["neigthMean"] = Data["neigthMean"].fillna(Data["Level"])
    Data["neigthStd"] = Data["neigthStd"].fillna(0)
    # operator
    Data["Operator"] = nameOP
    # train/test split
    IdxSplit = int(len(Data) * SplitPoint)
    TrainVals = Data.iloc[:IdxSplit].copy()
    TestVals  = Data.iloc[IdxSplit:].copy()
    

    return TrainVals, TestVals, Data.copy()

processed = [processOPML(file, op) for op, file in files.items()]

# Transformer for converting map coordinates from Web Mercator  to WGS84
trans = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
# Formatter for longitude axis convert from meters  to degrees
def formatAxisLon(x, pos):
    lon, lat = trans.transform(x, 0)
    return f"{lon:.2f}°"
# Formatter for latitude axis convert from meters  to degrees
def formatAxisLat(y, pos):
    lon, lat = trans.transform(0, y)
    return f"{lat:.2f}°"



def PlotFunc(GeoDataTrain, GeoData_test, yPredict, title, filename):
    fig, ax = plt.subplots(figsize=SizeOfFigures)
    colorMap = plt.cm.viridis   
    GeoDataTrain.plot(ax=ax, column="Level", cmap=colorMap, markersize=50, vmin=LevelMinRSRP, vmax=LevelMaxRSRP)
    GeoDataPredict = GeoData_test.copy()
    GeoDataPredict["Pred"] = yPredict
    GeoDataPredict.plot(ax=ax, column="Pred", cmap=colorMap, markersize=70, marker="^", vmin=LevelMinRSRP, vmax=LevelMaxRSRP)
    sm = plt.cm.ScalarMappable(cmap=colorMap)
    sm.set_clim(LevelMinRSRP, LevelMaxRSRP)
    colorBar = plt.colorbar(sm,ax=ax,label="RSRP [dBm]",fraction=0.035,pad=0.02)
    colorBar.ax.tick_params()
    colorBar.set_label("RSRP [dBm]")
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.6)
    ax.xaxis.set_major_formatter(FuncFormatter(formatAxisLon))
    ax.yaxis.set_major_formatter(FuncFormatter(formatAxisLat))
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    ax.tick_params(axis='both')
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
    ax.legend(["Měřené", "Predikované"])
    if FlagShowFiguresTitle:
        ax.set_title(title)
    plt.tight_layout()
    plt.savefig(f"{SaveFigLoc}/{filename}.pdf", bbox_inches="tight", dpi=600, pad_inches=0.05)
    plt.close()
    
    
def ModelMetrics(measVals, predVals, ModelName):
    measVals = np.asarray(measVals)
    predVals = np.asarray(predVals)
    if np.ma.isMaskedArray(predVals):
        predVals = predVals.filled(np.nan)
    # delete NaN vals
    mask = ~np.isnan(predVals)
    measVals = measVals[mask]
    predVals = predVals[mask]
    # evaluate models
    mae = mean_absolute_error(measVals, predVals)
    rmse = np.sqrt(mean_squared_error(measVals, predVals))
    r2 = r2_score(measVals, predVals)
    # print evaluation
    print(f"{ModelName}:")
    print(f"  Střední absolutní chyba (MAE) = {mae:.3f} dBm")
    print(f"  Střední kvadratická chyba (RMSE) = {rmse:.3f} dBm")
    print(f"  Koeficient determinace  (R²)  = {r2:.3f}")
    print()
    print("-------------------------------------------")
    print()


for (op, _), (Data_train, Data_test, Data_all) in zip(files.items(), processed):
    # print name actual processed operátor 
    print(f"\nPro data operátora {op}")

    # GEO
    GeoDataTrain = gpd.GeoDataFrame(Data_train, geometry=gpd.points_from_xy(Data_train["Longitude"], Data_train["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)
    GeoDataTest = gpd.GeoDataFrame(Data_test, geometry=gpd.points_from_xy(Data_test["Longitude"], Data_test["Latitude"]), crs="EPSG:4326" ).to_crs(epsg=3857)
    GeoDataAll = gpd.GeoDataFrame(Data_all, geometry=gpd.points_from_xy(Data_all["Longitude"], Data_all["Latitude"]), crs="EPSG:4326").to_crs(epsg=3857)


    # ML DATA input data
    InputVals = ["Longitude", "Latitude", "SNR", "Qual", "Speed","distCentr", "logDist", "SNRxQual","NRxLev1", "NRxLev2", "NRxLev3", "neigthMean" ,"NRxLev4", "NRxLev5", "NRxLev6", "neigthMax", "neigthStd"]
    
    InpTrain = Data_train[InputVals]
    RsrpTrain = Data_train["Level"]
    InpTest = Data_test[InputVals]
    RsrpTest = Data_test["Level"]

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Nearest Neighbour interpolation
    NearNeigPred = griddata((InpTrain["Longitude"], InpTrain["Latitude"]), RsrpTrain, (InpTest["Longitude"], InpTest["Latitude"]), method="nearest")
    ModelMetrics(RsrpTest, NearNeigPred, "Metoda nejbližšího souseda")
    PlotFunc(GeoDataTrain, GeoDataTest, NearNeigPred, "Metoda nejbližšího souseda", f"{op}_Nearest_Neighbour")

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Linear interpolation
    LinInterPred = griddata((InpTrain["Longitude"], InpTrain["Latitude"]), RsrpTrain, (InpTest["Longitude"], InpTest["Latitude"]), method="linear")
    ModelMetrics(RsrpTest, LinInterPred, "Lineární interpolace ")
    PlotFunc(GeoDataTrain, GeoDataTest, LinInterPred, "Lineární interpolace ", f"{op}_Linear_Interp")

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Cubic interpolation
    CubInterPred = griddata((InpTrain["Longitude"], InpTrain["Latitude"]), RsrpTrain, (InpTest["Longitude"], InpTest["Latitude"]), method="cubic")
    PlotFunc(GeoDataTrain, GeoDataTest, CubInterPred, "Kubická interpolace ", f"{op}_Cubic_Interp")
    ModelMetrics(RsrpTest, CubInterPred, "Kubická interpolace ")

    #----------------------------------------------------------------------------------------------------------------------------------------------
    TrainKrig = pd.DataFrame({"Longitude": InpTrain["Longitude"],"Latitude": InpTrain["Latitude"],"RSRP": RsrpTrain})
    # delete datas measured at same spot kriging need it 
    TrainKrig = TrainKrig.groupby(["Longitude", "Latitude"],as_index=False)["RSRP"].mean()
    # KRIGING (4 types of variograms)
    for vmodel in ["spherical", "gaussian", "exponential", "linear"]:
        OK = OrdinaryKriging(TrainKrig["Longitude"].values,TrainKrig["Latitude"].values,TrainKrig["RSRP"].values,variogram_model=vmodel,verbose=False)
        KrigPred, _ = OK.execute("points", InpTest["Longitude"].values, InpTest["Latitude"].values)
        ModelMetrics(RsrpTest, KrigPred, f"Krigování  (variogram: {vmodel})")
        PlotFunc(GeoDataTrain, GeoDataTest, KrigPred, "Krigování ", f"{op}_Kriging_{vmodel}")

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Linear Regression 
    LinReg = Pipeline([("scaler", StandardScaler()),("reg", LinearRegression())])
    LinReg.fit(InpTrain, RsrpTrain)
    LinRegPred = LinReg.predict(InpTest)
    ModelMetrics(RsrpTest, LinRegPred, "Lineární regrese ")
    PlotFunc(GeoDataTrain, GeoDataTest, LinRegPred, "Lineární regrese ", f"{op}_Linear_Regression")
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Ridge Regression
    RidReg = Pipeline([("scaler", StandardScaler()),("reg", Ridge(alpha=10.0))])
    RidReg.fit(InpTrain, RsrpTrain)
    RidRegPred = RidReg.predict(InpTest)
    ModelMetrics(RsrpTest, RidRegPred, "Hřebenová regrese")
    PlotFunc(GeoDataTrain, GeoDataTest, RidRegPred, "Hřebenová regrese", f"{op}_Ridge_Regression")
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Random Forest
    RandFor = RandomForestRegressor(n_estimators=500, max_depth=15, min_samples_leaf=3, max_features="sqrt", random_state=42, n_jobs=-1)
    RandFor.fit(InpTrain, RsrpTrain)
    RandForPred = RandFor.predict(InpTest)
    ModelMetrics(RsrpTest, RandForPred, "Random Forest")
    PlotFunc(GeoDataTrain, GeoDataTest, RandForPred, "Random  Forest", f"{op}_Random_Forest")
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # RXGBoost
    X_tr, X_val, y_tr, y_val = train_test_split(InpTrain, RsrpTrain, test_size=0.2, random_state=42)
    xgb = XGBRegressor(n_estimators=1000,max_depth=5,learning_rate=0.05,subsample=0.8,colsample_bytree=0.8,early_stopping_rounds=30,min_child_weight=3,random_state=42)
    xgb.fit(X_tr, y_tr, eval_set=[(X_val, y_val)], verbose=False)
    xgbPred = xgb.predict(InpTest)
    ModelMetrics(RsrpTest, xgbPred, "XGBoost")
    PlotFunc(GeoDataTrain, GeoDataTest, xgbPred, "XGBoost", f"{op}_XGB")
    
    
    
    # plot measured RSRP points on map
    fig, ax = plt.subplots(figsize=SizeOfFigures)
    colorMap = plt.cm.viridis
    GeoDataAll.plot(ax=ax, column="Level", cmap=colorMap, markersize=50, vmin=LevelMinRSRP, vmax=LevelMaxRSRP)
    sm = plt.cm.ScalarMappable(cmap=colorMap)
    sm.set_clim(LevelMinRSRP, LevelMaxRSRP)
    colorBar = plt.colorbar(sm,ax=ax,label="RSRP [dBm]",fraction=0.035,pad=0.02)

    colorBar.ax.tick_params()
    colorBar.set_label("RSRP [dBm]")
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.6)
    ax.xaxis.set_major_formatter(FuncFormatter(formatAxisLon))
    ax.yaxis.set_major_formatter(FuncFormatter(formatAxisLat))
    ax.set_xlabel("Zeměpisná délka [°]")
    ax.set_ylabel("Zeměpisná šířka [°]")
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
    ax.tick_params(axis='both')
    ax.legend(["Měřené", "Predikované"])
    if FlagShowFiguresTitle:
        ax.set_title("Změřená RSRP data v závislosti na pozici")
    plt.tight_layout()
    plt.savefig(f"{SaveFigLoc}/{op}_RSRP_MEAS.pdf", bbox_inches="tight", dpi=600, pad_inches=0.05)
    plt.close()
    
    
print("PDF soubory jsou vytvořeny")  

    
    
    

