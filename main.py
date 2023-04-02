import requests
import json

def price_time_stamp(time_stamp):
    print("__________________________")
    print(f"Tid: {time_stamp['time_start']}")
    print(f"Pris: NOK {time_stamp['NOK_per_kWh']} eller €{time_stamp['EUR_per_kWh']}")
    print(f"Vekslingskurs: {time_stamp['EXR']} €/NOK")

response = requests.get('https://www.hvakosterstrommen.no/api/v1/prices/2023/03-10_NO5.json')

if response.status_code == 200:
    json_data = json.loads(response.content)

    data = list(json_data)

    for time_stamp in data:
        price_time_stamp(time_stamp)

response = requests.get('https://biapi.nve.no/nettleiestatistikk/swagger/v1/swagger.json')

if response.status_code == 200:
    json_data = json.loads(response.content)

    data = dict(json_data)

    print(data)