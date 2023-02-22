#!/usr/bin/env python3
import requests
import pandas as pd

df = pd.read_csv('airport-codes_csv.csv')


def get_meteo(info):
    hdr = {"X-API-Key": "05dba8efa41343e290b94e2cea"}
    url = "https://api.checkwx.com/" + f"{info}" + f"/{airport}/"
    response = requests.request("GET", url, headers=hdr)
    if response.reason != 'OK':
        print(response.reason)
        print(url)
        print('A connection error occurred!\nTry a different airport')
        exit()
    else:
        return response.json()


def print_meteo(info):
    met_data = get_meteo(info)
    print(f"{info.upper()} for {airport}:")
    print(met_data['data'][0])


print("Airpot METAR/TAF INFO")
print('Enter ICAO code to view latest info:')
airport = ''
valid_airport = False
while not valid_airport:
    airport = input()
    airport = airport.upper()
    if airport in df.to_string():
        valid_airport = True
    else:
        print('Type a valid ICAO code!')

print_meteo('metar')
print_meteo('taf')
