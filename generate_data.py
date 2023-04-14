import pandas as pd
import numpy as np
import requests

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

def hent_priser(sone):
    with open(f"data/priser/min/{sone}.txt", "w") as file:
        stop = False

        for aar in range(2021, 2024):
            faktisk_aar = str(aar)

            if aar == 2021:
                for maaned in range(11, len(maaneder)): # Faktisk maaned - 1 = start
                    faktisk_maaned = str(maaned + 1).zfill(2)
                
                    for dag in range(1, maaneder[maaned] + 1):
                        faktisk_dag = str(dag).zfill(2)
                        response = requests.get(f"https://www.hvakosterstrommen.no/api/v1/prices/{faktisk_aar}/{faktisk_maaned}-{faktisk_dag}_{sone}.json")
                        if response.status_code == 200:
                            gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].min()
                            file.write(f"{gj_pris}\n")
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
                        response = requests.get(f"https://www.hvakosterstrommen.no/api/v1/prices/{faktisk_aar}/{faktisk_maaned}-{faktisk_dag}_{sone}.json")

                        if response.status_code == 200:
                            gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].min()
                            file.write(f"{gj_pris}\n")
                        else:
                            stop = True
                            break
            if stop:
                break

def hent_nedbor(sone):
    with open(f"data/nedbor/{sone}.txt", "w") as file:
        parameters = {
            'sources': soner[sone],
            'elements': 'sum(precipitation_amount P1D)'
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

                        parameters["referencetime"] = faktisk_dato

                        response = requests.get(endpoint, parameters, auth=(client_id,''))

                        if response.status_code == 200:
                            data = response.json()["data"]

                            dataframe = pd.DataFrame()

                            for entry in data:
                                df = pd.DataFrame(entry["observations"])
                                dataframe = pd.concat([dataframe, df])
                            
                            mean_nedbor = dataframe["value"].mean()
                            file.write(f"{mean_nedbor}\n");
                            
                            print(faktisk_dato)

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

                            print(faktisk_dato)
                            mean_nedbor = dataframe["value"].mean()
                            file.write(f"{mean_nedbor}\n");
                        else:
                            stop = True
                            break
            if stop:
                break
def hent_temperatur(sone):
    with open(f"data/temperatur/{sone}.txt", "w") as file:
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
                            file.write(f"{mean_temp}\n")

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
                            file.write(f"{mean_temp}\n")
                        else:
                            stop = True
                            break
            if stop:
                break

# This is going to be an interface
def hovedprogram():
    for sone in soner:
        #hent_priser(sone)
        hent_temperatur(sone)
        #hent_nedbor(sone)

hovedprogram()