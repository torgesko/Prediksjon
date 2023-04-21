import matplotlib.pyplot as plt
import requests
import time

soner = ["NO1", "NO2", "NO3", "NO4", "NO5"]

maaneder = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def show_sone(sone):
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
                        json = response.json()                        
                        prices = []

                        for element in json:
                            prices.append(element["NOK_per_kWh"])

                        deltas = [x for x in range(len(prices))]

                        plt.plot(deltas, prices)
                        plt.title(f"{sone} - {faktisk_maaned}/{faktisk_dag}/{faktisk_aar}")
                        plt.xlabel("Time")
                        plt.ylabel("Price (NOK/kWh)")
                        plt.pause(0.05)
                        plt.clf()

                        time.sleep(10)
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
                        json = response.json()
                        prices = []

                        for element in json:
                            prices.append(element["NOK_per_kWh"])

                        deltas = [x for x in range(len(prices))]

                        plt.plot(deltas, prices)
                        plt.title(f"{sone} - {faktisk_maaned}/{faktisk_dag}/{faktisk_aar}")
                        plt.xlabel("Time")
                        plt.ylabel("Price (NOK/kWh)")
                        plt.pause(0.05)
                        plt.clf()
                        
                        time.sleep(10)
                    else:
                        stop = True
                        break
        if stop:
            break

def hovedprogram():
    for sone in soner:
        show_sone(sone)
    plt.show()

hovedprogram()