from sklearn.linear_model import LinearRegression
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

client_id = 'aedfcb9b-24c2-45e6-975f-8a23e8d0cd84'

endpoint = 'https://frost.met.no/observations/v0.jsonld'

soner = {
    "NO1" : "SN18315,SN17090,SN1070,SN3280,SN2830,SN4950,SN11463,SN12030,SN4590,SN5680,SN6580,SN13420,SN7420,SN8800,SN22840", 
    "NO2" : "SN45770,SN42940,SN41550,SN37310,SN32850,SN34580,SN36560,SN38380,SN41175,SN43010,SN44520,SN40510,SN35340,SN39220", 
    "NO3" : "SN71000,SN1280,SN66175,SN68420,SN64870,SN61070,SN9580,SN66810,SN16845,SN69661,SN71320,SN62160,SN71550,SN10300,SN69035", 
    "NO4" : "SN96220,SN94050,SN88023,SN91010,SN83710,SN80615,SN78250,SN93301,SN78910,SN77280,SN81340,SN85560,SN85080,SN88660,SN89940", 
    "NO5" : "SN54110,SN55300,SN55670,SN55820,SN52930,SN53070,SN51940,SN57030,SN56400,SN52555,SN52475,SN51210,SN53160,SN56850,SN53990"
}

maaneder = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def hent_priser(prisomraade):
    priser = []

    stop = False

    for aar in range(2021, 2024):
        faktisk_aar = str(aar)
    
        if aar == 2021:
            for maaned in range(11, len(maaneder)): # Faktisk maaned - 1 = start
                faktisk_maaned = str(maaned + 1).zfill(2)
                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)
                    response = requests.get(f"https://www.hvakosterstrommen.no/api/v1/prices/{faktisk_aar}/{faktisk_maaned}-{faktisk_dag}_{prisomraade}.json")

                    if response.status_code == 200:
                        gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].mean()
                        print(gj_pris)
                        priser.append(gj_pris)
                    else:
                        stop = True
                        break
                if stop:
                    break
        else:
            for maaned in range(0, len(maaneder)):
                faktisk_maaned = str(maaned + 1).zfill(2)
                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)
                    response = requests.get(f"https://www.hvakosterstrommen.no/api/v1/prices/{faktisk_aar}/{faktisk_maaned}-{faktisk_dag}_{prisomraade}.json")

                    if response.status_code == 200:
                        gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].mean()
                        print(gj_pris)
                        priser.append(gj_pris)
                    else:
                        stop = True
                        break
        if stop:
            break

    return priser

def hent_nedbor(sone):
    nedbor = []

    parameters = {
        'sources': soner[sone],
        'elements': 'sum(precipitation_amount P1D)'
    }

    stop = False

    for aar in range(2021, 2024):
        faktisk_aar = str(aar)
    
        if aar == 2021:
            for maaned in range(11 , len(maaneder)): # Faktisk maaned - 1 = start
                faktisk_maaned = str(maaned + 1).zfill(2)

                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)

                    faktisk_dato = f"{faktisk_aar}-{faktisk_maaned}-{faktisk_dag}"

                    parameters["referencetime"] = f"{faktisk_dato}"

                    response = requests.get(endpoint, parameters, auth=(client_id,''))

                    if response.status_code == 200:
                        data = response.json()["data"]

                        dataframe = pd.DataFrame()
                    
                        for entry in data:
                            df = pd.DataFrame(entry["observations"])
                            dataframe = pd.concat([dataframe, df])

                        mean_nedbor = dataframe["value"].mean()
                        print(f"{faktisk_dato} : {mean_nedbor}")
                        nedbor.append(mean_nedbor)

                    else:
                        stop = True
                        break
                if stop:
                    break
        else:
            for maaned in range(0, len(maaneder)):
                faktisk_maaned = str(maaned + 1).zfill(2)

                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)

                    faktisk_dato = f"{faktisk_aar}-{faktisk_maaned}-{faktisk_dag}"

                    parameters["referencetime"] = f"{faktisk_dato}"

                    response = requests.get(endpoint, parameters, auth=(client_id,''))

                    if response.status_code == 200:
                        data = response.json()["data"]

                        dataframe = pd.DataFrame()

                        for entry in data:
                            df = pd.DataFrame(entry["observations"])
                            dataframe = pd.concat([dataframe, df])

                        mean_nedbor = dataframe["value"].mean()
                        print(f"{faktisk_dato} : {mean_nedbor}")
                        nedbor.append(mean_nedbor)
                    else:
                        stop = True
                        break
        if stop:
            break

    return nedbor

def hent_temps(sone):
    temps = []

    parameters = {
        'sources': soner[sone],
        'elements': 'mean(air_temperature P1D)'
    }

    stop = False

    for aar in range(2021, 2024):
        faktisk_aar = str(aar)
    
        if aar == 2021:
            for maaned in range(11, len(maaneder)): # Faktisk maaned - 1 = start
                faktisk_maaned = str(maaned + 1).zfill(2)

                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)

                    faktisk_dato = f"{faktisk_aar}-{faktisk_maaned}-{faktisk_dag}"

                    parameters["referencetime"] = f"{faktisk_dato}"

                    response = requests.get(endpoint, parameters, auth=(client_id,''))

                    if response.status_code == 200:
                        data = response.json()["data"]

                        dataframe = pd.DataFrame()

                        for entry in data:
                            df = pd.DataFrame(entry["observations"])
                            dataframe = pd.concat([dataframe, df])

                        mean_temp = dataframe["value"].mean()
                        print(f"{faktisk_dato} : {mean_temp}")
                        temps.append(mean_temp)

                    else:
                        stop = True
                        break
                if stop:
                    break
        else:
            for maaned in range(0, len(maaneder)):
                faktisk_maaned = str(maaned + 1).zfill(2)

                for dag in range(1, maaneder[maaned] + 1):
                    faktisk_dag = str(dag).zfill(2)

                    faktisk_dato = f"{faktisk_aar}-{faktisk_maaned}-{faktisk_dag}"

                    parameters["referencetime"] = f"{faktisk_dato}"

                    response = requests.get(endpoint, parameters, auth=(client_id,''))

                    if response.status_code == 200:
                        data = response.json()["data"]

                        dataframe = pd.DataFrame()

                        for entry in data:
                            df = pd.DataFrame(entry["observations"])
                            dataframe = pd.concat([dataframe, df])

                        mean_temp = dataframe["value"].mean()
                        print(f"{faktisk_dato} : {mean_temp}")
                        temps.append(mean_temp)
                    else:
                        stop = True
                        break
        if stop:
            break

    return temps

def create_model(sone):
    priser = hent_priser(sone)
    nedbor = hent_nedbor(sone)
    temps = hent_temps(sone)

    X = np.column_stack((nedbor, temps))
    Y = np.array(priser)

    model = LinearRegression()
    model.fit(X, Y)

    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)

def hovedprogram():
    create_model("NO5")

hovedprogram()