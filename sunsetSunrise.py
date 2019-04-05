import requests
import json
from pprint import pprint
import urllib3


requests.packages.urllib3.disable_warnings()
url='https://api.sunrise-sunset.org/json?lat=50.85045&lng=-4.34878'

ticket = "ST-265-gPXbe9e2XXLvsvqJkdiB-cas"
headers={
    "Content-Type": "application/json",
    "X-Auth-Token": ticket
}

resp = requests.get(url,headers=headers,verify=False)

print("Ticket request status:", resp.status_code)
response_json = resp.json()
pprint(response_json['status'])
pprint("Iformacion sobre la ciudad de Bruselas")
print("\nSalida de sol: " + response_json['results']['sunrise'])
print("Puesta de sol: " + response_json['results']['sunset'])
print("Sol mediodia: " + response_json['results']['solar_noon'])
print("Duracion dia: " + response_json['results']['day_length'])
print("\nInicio crepusculo civil: " + response_json['results']['civil_twilight_begin'])
print("Final crepusculo civil: " + response_json['results']['civil_twilight_end'])
print("\nInicio crepusculo nautico: " + response_json['results']['nautical_twilight_begin'])
print("Final crepusculo nautico: " + response_json['results']['nautical_twilight_end'])
print("\nInicio crepusculo astronomico: " + response_json['results']['astronomical_twilight_begin'])
print("Final crepusculo astronomico: " + response_json['results']['astronomical_twilight_end'])
