import requests
import pandas as pd

client_id = 'aedfcb9b-24c2-45e6-975f-8a23e8d0cd84'

# Andre værstasjoner: SN90450

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN18700',
    'elements': 'mean(air_temperature P1D),sum(precipitation_amount P1D)',
    'referencetime': '2023-03-21',
}
# Issue an HTTP GET request
r = requests.get(endpoint, parameters, auth=(client_id,''))
# Extract JSON data
json = r.json()

for entry in json["data"]:
    print(entry["sourceId"])
    print(entry["observations"])

# Check if the request worked, print out any errors
if r.status_code == 200:
    print('Data retrieved from frost.met.no!')
    data = json['data']
    df = pd.DataFrame()

    for i in range(len(data)):
        row = pd.DataFrame(data[i]['observations'])
        row['referenceTime'] = data[i]['referenceTime']
        row['sourceId'] = data[i]['sourceId']
        df = pd.concat([df, row])

    print(df.describe())

    df = df.reset_index()
    print(df)
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json['error']['message'])
    print('Reason: %s' % json['error']['reason'])