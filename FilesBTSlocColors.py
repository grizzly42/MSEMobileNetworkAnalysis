# BRNO
	# WALK: PalackehoVrch; Medlanky; PonavaTM; PonavaVOD; Ponava; SlovanskeNamesti; NamestiSvobodyTM; 
            #NamestiSvobodyVOD; NamestiSvobody; ReckMoravWalk; ZabovreskyO2; ZabovreskyTM; ZabovreskyVOD; ZabovreskyOperators
	# MHD: KolejniVsetinskaCelniKolejni; KolejniVsetinska; CelniKolejni; ReckMoravMHD
	# CAR: ReckMoravCAR
# CZE
	# WALK: ZamberkO2; ZamberkTM; Zamberk; PanskaDolinaO2; PanskaDolinaTM; PanskaDolina
	# CAR: ZamberkKoncinyTM; ZamberkKoncinyVOD; ZamberkKonciny; ZamberkSloupnice; SloupniceZamberk; 
           #TisnovMosty1; TisnovMosty2; TisnovMosty3; TisnovMosty
	#train: DecinBreclavO2; DecinBreclavTM; DecinBreclavVOD; DecinBreclav; UstiNadOrliciLetohrad; UstiNadOrliciLetohradVOD; UstiNadOrliciLetohradTM	
# Transports: TransportVOD; TransportTM
# in thesis: DecinBreclav, ZabovreskyOperators;  TransportVOD, TransportTM
def FilesBTSlocColors(dataset):
    
    #-------------------------------------------------------------------------------------
    # BRNO WALK TESTS
    #-------------------------------------------------------------------------------------
    if dataset == "PalackehoVrch":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_Palackeho_Vrch_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/PalackehoVrch"

        RealBTSLocation = [
            {"node": 606101, "lat": 49.228383, "lon": 16.581408},
            {"node": 606281, "lat": 49.2250667, "lon": 16.5763833},
            {"node": 606491, "lat": 49.2320722, "lon": 16.5717556}]
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None

    #-------------------------------------------------------------------------------------
    elif dataset == "Medlanky":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_Medlanky_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Medlanky"

        RealBTSLocation = [
            {"node": 606011, "lat": 49.2333472, "lon": 16.5898306},
            {"node": 606091, "lat": 49.2415222, "lon": 16.5789167},
            {"node": 606101, "lat": 49.2283833, "lon": 16.5814083},
            {"node": 606191, "lat": 49.2361861, "lon": 16.5824139},
            {"node": 606281, "lat": 49.2250667, "lon": 16.5763833},
            {"node": 606491, "lat": 49.2320722, "lon": 16.5717556}]
        
        Colors = {'T-Mobile': 'magenta'}

        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "PonavaTM":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_Ponava_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Ponava/T-Mobile"
            
        RealBTSLocation = [
            {"node": 605241, "lat": 49.2098722, "lon": 16.6033583},
            {"node": 605281, "lat": 49.2098722, "lon": 16.6033583},
            {"node": 605991, "lat": 49.2114389, "lon": 16.6165500},
            {"node": 606081, "lat": 49.2118278, "lon": 16.5987028},
            {"node": 606131, "lat": 49.2044528, "lon": 16.5935667},
            {"node": 606141, "lat": 49.2068361, "lon": 16.5964861},
            {"node": 606201, "lat": 49.2140194, "lon": 16.5925194},
            {"node": 606261, "lat": 49.2034167, "lon": 16.5985528},
            {"node": 607011, "lat": 49.2101472, "lon": 16.5896167}]
        
        Colors = {'T-Mobile': 'magenta'}
    
        SplitPoint = 0.65
    #-------------------------------------------------------------------------------------   
    elif dataset == "PonavaVOD":
        InputFiles = {"Vodafone": "datasets/Brno/WalkTests/walk_Ponava_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Ponava/Vodafone"
            
        RealBTSLocation = None
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = 0.65
    #-------------------------------------------------------------------------------------   
    elif dataset == "Ponava":
        InputFiles = {"Vodafone": "datasets/Brno/WalkTests/walk_Ponava_VOD.csv",
                      "T-Mobile": "datasets/Brno/WalkTests/walk_Ponava_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Ponava"
            
        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta', 'Vodafone': 'red'}
    
        SplitPoint = 0.65
    #-------------------------------------------------------------------------------------   
    elif dataset == "SlovanskeNamesti":
        InputFiles = {
            "T-Mobile": "datasets/Brno/WalkTests/walk_Technologicke_muzeum-Slovanke_namesti_TM.csv"
        }
        ResultsFilesLocation = "results/Brno/WalkTests/SlovanskeNamesti/T-Mobile"

        RealBTSLocation =  [
            {"node": 605061, "lat": 49.2256694, "lon": 16.5915722},
            {"node": 605071, "lat": 49.2226083, "lon": 16.5913278},
            {"node": 605371, "lat": 49.2282028, "lon": 16.5926306},
            {"node": 606011, "lat": 49.2333472, "lon": 16.5898306},
            {"node": 606101, "lat": 49.2283833, "lon": 16.5814083},
            {"node": 606411, "lat": 49.2242389, "lon": 16.5857167}]
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------   
    elif dataset == "NamestiSvobodyTM":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_nam_Svobody_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/NamestiSvobody/T-Mobile"

        RealBTSLocation = [
            {"node": 2471,   "lat": 49.1969806, "lon": 16.6097250},
            {"node": 600011, "lat": 49.1919111, "lon": 16.6102583},
            {"node": 600061, "lat": 49.1947861, "lon": 16.6078750},
            {"node": 600111, "lat": 49.1939639, "lon": 16.6124750},
            #{"node": 600121, "lat": 49.1959806, "lon": 16.6063444},
            {"node": 600151, "lat": 49.1935278, "lon": 16.6076111},
            {"node": 600201, "lat": 49.1961667, "lon": 16.6095667},
            {"node": 600391, "lat": 49.1979389, "lon": 16.6059917}]
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = 0.73
        
    #-------------------------------------------------------------------------------------     
    elif dataset == "NamestiSvobodyVOD":
        InputFiles = {"Vodafone": "datasets/Brno/WalkTests/walk_nam_Svobody_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/NamestiSvobody/Vodafone"

        RealBTSLocation = None
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = 0.73
        
    #-------------------------------------------------------------------------------------     
    elif dataset == "NamestiSvobody":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_nam_Svobody_TM.csv",
                      "Vodafone": "datasets/Brno/WalkTests/walk_nam_Svobody_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/NamestiSvobody"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta', 'Vodafone': 'red'}
        
        SplitPoint = 0.73
        
    #-------------------------------------------------------------------------------------     
    elif dataset == "ReckMoravWalk":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_reckovice-moravske_namesti_TM.csv",
                      "Vodafone": "datasets/Brno/WalkTests/walk_reckovice-moravske_namesti_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Reckovice-MoravskeNamesti"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta', 'Vodafone': 'red'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------     
    elif dataset == "ZabovreskyO2":
        InputFiles = {"O2": "datasets/Brno/WalkTests/walk_Zabovresky_O2.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Zabovresky/O2"

        RealBTSLocation = None
        
        Colors = {'O2': 'blue'}
        
        SplitPoint = 0.76
    
    #------------------------------------------------------------------------------------- 
    elif dataset == "ZabovreskyTM":
        InputFiles = {"T-Mobile": "datasets/Brno/WalkTests/walk_Zabovresky_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Zabovresky/T-Mobile"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = 0.76
        
    #------------------------------------------------------------------------------------- 
    elif dataset == "ZabovreskyVOD":
        InputFiles = {"Vodafone": "datasets/Brno/WalkTests/walk_Zabovresky_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/WalkTests/Zabovresky/Vodafone"

        RealBTSLocation = None
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = 0.76
        
    #------------------------------------------------------------------------------------- 
    elif dataset == "ZabovreskyOperators":
        InputFiles = {"O2": "datasets/Brno/WalkTests/walk_Zabovresky_O2.csv",
                      "T-Mobile": "datasets/Brno/WalkTests/walk_Zabovresky_TM.csv",
                      "Vodafone": "datasets/Brno/WalkTests/walk_Zabovresky_VOD.csv"}
        
        ResultsFilesLocation = "results/ComparisonOperators/Zabovresky"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta','O2': 'blue','Vodafone': 'red'}
        
        SplitPoint = 0.76
        
        
    #-------------------------------------------------------------------------------------
    # BRNO MHD DRIVE TESTS
    #-------------------------------------------------------------------------------------
    elif dataset == "KolejniVsetinskaCelniKolejni":
        InputFiles = {"T-Mobile": "datasets/Brno/MHD/tram_kolejni-vsetinska-celni-kolejni_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/MHD/Kolejni-Vsetinska-Celni-Kolejni"

        RealBTSLocation = [
        {"node": 7641,   "lat": 49.1869778, "lon": 16.6138639},
        {"node": 600391, "lat": 49.1979389, "lon": 16.6059917},
        {"node": 601201, "lat": 49.1760306, "lon": 16.6024056},
        {"node": 601241, "lat": 49.1806333, "lon": 16.6057167},
        {"node": 601271, "lat": 49.1803778, "lon": 16.5943056},
        {"node": 601351, "lat": 49.1854639, "lon": 16.5973944},
        {"node": 601391, "lat": 49.1814389, "lon": 16.5993417},
        {"node": 605071, "lat": 49.2226083, "lon": 16.5913278},
        {"node": 605371, "lat": 49.2282028, "lon": 16.5926306},
        {"node": 606041, "lat": 49.2174972, "lon": 16.5929278},
        {"node": 606101, "lat": 49.2283833, "lon": 16.5814083},
        {"node": 606131, "lat": 49.2044528, "lon": 16.5935667},
        {"node": 606141, "lat": 49.2068361, "lon": 16.5964861},
        {"node": 606201, "lat": 49.2140194, "lon": 16.5925194},
        {"node": 606261, "lat": 49.2034167, "lon": 16.5985528},
        {"node": 606281, "lat": 49.2250667, "lon": 16.5763833},
        {"node": 606301, "lat": 49.2201167, "lon": 16.5857667},
        {"node": 606491, "lat": 49.2320722, "lon": 16.5717556},
        {"node": 608021, "lat": 49.1890611, "lon": 16.6030750},
        {"node": 608191, "lat": 49.1897778, "lon": 16.5920306}
        ]
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "KolejniVsetinska":
        InputFiles = {"T-Mobile": "datasets/Brno/MHD/tram_kolejni-vsetinska_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/MHD/Kolejni-Vsetinska"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "CelniKolejni":
        InputFiles = {"T-Mobile": "datasets/Brno/MHD/tram_celni-kolejni_TM.csv"}
        
        ResultsFilesLocation = "results/Brno/MHD/Celni-Kolejni"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "ReckMoravMHD":
        InputFiles = {"T-Mobile": "datasets/Brno/MHD/tram_reckovice-moravske_namesti_TM.csv",
                      "Vodafone": "datasets/Brno/MHD/tram_reckovice-moravske_namesti_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/MHD/Reckovice-MoravskeNamesti"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta','Vodafone': 'red'}
        
        SplitPoint = None
        
        
    #-------------------------------------------------------------------------------------
    # BRNO CAR DRIVE TESTS
    #------------------------------------------------------------------------------------- 
    elif dataset == "ReckMoravCAR":
        InputFiles = {"T-Mobile": "datasets/Brno/CAR/car_reckovice-moravske_namesti_TM.csv",
                      "Vodafone": "datasets/Brno/CAR/car_reckovice-moravske_namesti_VOD.csv"}
        
        ResultsFilesLocation = "results/Brno/CAR/Reckovice-MoravskeNamesti"

        RealBTSLocation = None
        
        Colors = {'T-Mobile': 'magenta','Vodafone': 'red'}
        
        SplitPoint = None
        
        
        
    
    #-------------------------------------------------------------------------------------
    # CZE WALK TESTS
    #------------------------------------------------------------------------------------- 
    elif dataset == "ZamberkO2":
        InputFiles = {"O2": "datasets/CzechRepublic/walk_Zamberk_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Zamberk/O2"

        RealBTSLocation = [
            {"node": 923802,   "lat": 50.0875000, "lon": 16.4569944},
            {"node": 925591,   "lat": 50.0776333, "lon": 16.4665222},]  
        
        Colors = {'O2': 'blue'}
        
        SplitPoint = None
        
    #------------------------------------------------------------------------------------- 
    elif dataset == "ZamberkTM":
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/walk_Zamberk_TM.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Zamberk/T-Mobile"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
     #------------------------------------------------------------------------------------- 
    elif dataset == "Zamberk":
        InputFiles = {
         "T-Mobile": "datasets/CzechRepublic/walk_Zamberk_TM.csv",
         "O2": "datasets/CzechRepublic/walk_Zamberk_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Zamberk"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta', 'O2': 'blue'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "PanskaDolinaO2":
        
        InputFiles = {"O2": "datasets/CzechRepublic/walk_Panska_dolina_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/PanskaDolina/O2"

        RealBTSLocation = [
            {"node": 921521,   "lat": 50.0753778, "lon": 16.5185000},
            {"node": 922931,   "lat": 50.1186472, "lon": 16.5823417},
            {"node": 923011,   "lat": 50.1141444, "lon": 16.4914444},
            {"node": 923801,   "lat": 50.0875000, "lon": 16.4569944},
            
        ]  
        Colors = {'O2': 'blue'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "PanskaDolinaTM":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/walk_Panska_dolina_TM.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/PanskaDolina/T-Mobile"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "PanskaDolina":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/walk_Panska_dolina_TM.csv",
                      "O2": "datasets/CzechRepublic/walk_Panska_dolina_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/PanskaDolina"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta', 'O2': 'blue'}
        
        SplitPoint = None
        
        
    #-------------------------------------------------------------------------------------
    elif dataset == "albertinumO2":
        
        InputFiles = {"O2": "datasets/CzechRepublic/walk_Albertinum_Panska_Dolina_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Albertinum-Panska Dolina/O2"
        RealBTSLocation = [
            {"node": 923802,   "lat": 50.0875000, "lon": 16.4569944},
            {"node": 925591,   "lat": 50.0776333, "lon": 16.4665222},] 
         
        Colors = {'O2': 'blue'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "albertinumTM":
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/walk_Albertinum_Panska_Dolina_TM.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Albertinum-Panska Dolina/T-Mobile"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "albertinum":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/walk_Albertinum_Panska_Dolina_TM.csv",
                      "O2": "datasets/CzechRepublic/walk_Albertinum_Panska_Dolina_O2.csv"}
        
        ResultsFilesLocation = "results/CR/WalkTests/Albertinum-Panska Dolina"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta', 'O2': 'blue'}
        
        SplitPoint = None
        
        
    #-------------------------------------------------------------------------------------
    # CZE CAR DRIVE TESTS
    #-------------------------------------------------------------------------------------
    
    elif dataset == "ZamberkKoncinyTM":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/car_Zamberk_Konciny_TM.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/ZamberkKonciny/T-Mobile"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    
    elif dataset == "ZamberkKoncinyVOD":
        
        InputFiles = {"Vodafone": "datasets/CzechRepublic/car_Zamberk_Konciny_VOD.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/ZamberkKonciny/Vodafone"

        RealBTSLocation = None  
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    
    elif dataset == "ZamberkKonciny":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/car_Zamberk_Konciny_TM.csv",
                      "Vodafone": "datasets/CzechRepublic/car_Zamberk_Konciny_VOD.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/ZamberkKonciny"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta','Vodafone': 'red'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "ZamberkSloupnice":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/car_Zamberk_Sloupnice_TM.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/ZamberkSloupnice"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "SloupniceZamberk":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/car_Sloupnice_Zamberk_TM.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/SloupniceZamberk"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "TisnovMosty1":
        
        InputFiles = {"T-Mobile1": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_1.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/Tisnov-Mosty_u_Jablunkova/T-Mobile1"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile1': 'magenta'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "TisnovMosty2":
        
        InputFiles = {"T-Mobile2": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_2.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/Tisnov-Mosty_u_Jablunkova/T-Mobile2"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile2': 'magenta'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "TisnovMosty3":
        
        InputFiles = {"T-Mobile3": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_3.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/Tisnov-Mosty_u_Jablunkova/T-Mobile3"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile3': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------    
    elif dataset == "TisnovMosty":
        
        InputFiles = {"T-Mobile1": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_1.csv",
                      "T-Mobile2": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_2.csv",
                      "T-Mobile3": "datasets/CzechRepublic/car_Tisnov_Mosty_u_Jablunkova_TM_3.csv"}
        
        ResultsFilesLocation = "results/CR/CAR/Tisnov-Mosty_u_Jablunkova"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile1': 'green', 'T-Mobile2': 'orange', 'T-Mobile3': 'purple'}
        
        SplitPoint = None

        
    #-------------------------------------------------------------------------------------
    # CZE TRAIN DRIVE TESTS
    #-------------------------------------------------------------------------------------
    elif dataset == "DecinBreclavO2":
        
        InputFiles = {"O2": "datasets/CzechRepublic/train_koridor_Decin_Breclav_O2.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/DecinBreclav/O2"

        RealBTSLocation = None  
        
        Colors = {'O2': 'blue'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "DecinBreclavTM":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/train_koridor_Decin_Breclav_TM.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/DecinBreclav/T-Mobile"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "DecinBreclavVOD":
        
        InputFiles = {"Vodafone": "datasets/CzechRepublic/train_koridor_Decin_Breclav_VOD.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/DecinBreclav/Vodafone"

        RealBTSLocation = None  
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "DecinBreclav":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/train_koridor_Decin_Breclav_TM.csv",
                      "O2": "datasets/CzechRepublic/train_koridor_Decin_Breclav_O2.csv",
                      "Vodafone": "datasets/CzechRepublic/train_koridor_Decin_Breclav_VOD.csv"}
        
        ResultsFilesLocation = "results/ComparisonOperators/DecinBreclav"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta','O2': 'blue','Vodafone': 'red'}
        
        SplitPoint = None
        
     #-------------------------------------------------------------------------------------
    elif dataset == "UstiNadOrliciLetohrad":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/train_UstiNadOrlici_Letohrad_TM.csv",
                      "Vodafone": "datasets/CzechRepublic/train_UstiNadOrlici_Letohrad_VOD.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/UstiNadOrlici_Letohrad"

        RealBTSLocation = None 
        
        Colors = {'T-Mobile': 'magenta','Vodafone': 'red'}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "UstiNadOrliciLetohradTM":
        
        InputFiles = {"T-Mobile": "datasets/CzechRepublic/train_UstiNadOrlici_Letohrad_TM.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/UstiNadOrlici_Letohrad/T-Mobile"

        RealBTSLocation = None  
        
        Colors = {'T-Mobile': 'magenta'}
        
        SplitPoint = None
    
    #-------------------------------------------------------------------------------------
    elif dataset == "UstiNadOrliciLetohradVOD":
        
        InputFiles = {"Vodafone": "datasets/CzechRepublic/train_UstiNadOrlici_Letohrad_VOD.csv"}
        
        ResultsFilesLocation = "results/CR/TRAIN/UstiNadOrlici_Letohrad/Vodafone"

        RealBTSLocation = None  
        
        Colors = {'Vodafone': 'red'}
        
        SplitPoint = None
        
        
    #-------------------------------------------------------------------------------------
    # comparison of transport types
    #-------------------------------------------------------------------------------------
    elif dataset == "TransportVOD":
        InputFiles = {
            "automobil": "datasets/Brno/CAR/car_reckovice-moravske_namesti_VOD.csv",
            "tramvaj": "datasets/Brno/MHD/tram_reckovice-moravske_namesti_VOD.csv",
            "chůze": "datasets/Brno/WalkTests/walk_reckovice-moravske_namesti_VOD.csv",
        }
        ResultsFilesLocation = "results/ComparisonOfTransport/Vodafone"
        
        RealBTSLocation = None
        
        Colors = {"automobil": "green", "tramvaj": "orange", "chůze": "purple"}
        
        SplitPoint = None
        
    #-------------------------------------------------------------------------------------
    elif dataset == "TransportTM":
        InputFiles = {
            "automobil": "datasets/Brno/CAR/car_reckovice-moravske_namesti_TM.csv",
            "tramvaj": "datasets/Brno/MHD/tram_reckovice-moravske_namesti_TM.csv",
            "chůze": "datasets/Brno/WalkTests/walk_reckovice-moravske_namesti_TM.csv",
        }
        ResultsFilesLocation = "results/ComparisonOfTransport/T-Mobile"
        
        RealBTSLocation = None
        
        Colors = {"automobil": "green", "tramvaj": "orange", "chůze": "purple"}
        
        SplitPoint = None
   
       
    else:
        raise ValueError("Neznámý dataset")

    return InputFiles, ResultsFilesLocation, RealBTSLocation, Colors, SplitPoint


