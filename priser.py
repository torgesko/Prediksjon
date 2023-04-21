def hent_priser(sone):
    with open(f"data/priser/max/{sone}.txt", "w") as file:
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
                            gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].max()
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
                            gj_pris = pd.DataFrame(response.json())["NOK_per_kWh"].max()
                            file.write(f"{gj_pris}\n")
                        else:
                            stop = True
                            break
            if stop:
                break