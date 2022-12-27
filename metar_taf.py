import requests
import pandas as pd

df = pd.read_csv('airport-codes_csv.csv')

print("For Metar type m \nFor Taf type t")
meteo_info = input()
valid_selections = ['m', 'M', 't', 'T']
while meteo_info not in valid_selections:
    print('Incorrect selection!\n For Metar type m \n For Taf type t')
    meteo_info = input()
if meteo_info == 'm' or meteo_info == 'M':
    meteo_info = 'metar'
elif meteo_info == 't' or meteo_info == 'T':
    meteo_info = 'taf'

print('Enter aiport ICAO code:\n')
airport = ''
valid_airport = False
while not valid_airport:
    airport = input()
    airport = airport.upper()
    if airport in df.to_string():
        valid_airport = True
    else:
        print('Type a valid ICAO code!\n')

hdr = {"X-API-Key": "8959bdce0ef44283aff7f7032d"}
url = "https://api.checkwx.com/" + f"/{meteo_info}" + f"/{airport}"
response = requests.get(url, headers=hdr)
if response.reason != 'OK':
    print('A connection error occurred!\nTry a different airport')
    exit()
# print(response.request.headers)
meteo_data = response.json()
print(meteo_data['data'][0])

# print(response.status_code)
