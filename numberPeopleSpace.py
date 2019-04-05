import requests
import json
from pprint import pprint
import urllib3


requests.packages.urllib3.disable_warnings()
url='http://api.open-notify.org/astros.json'

ticket = "ST-265-gPXbe9e2XXLvsvqJkdiB-cas"
headers={
    "Content-Type": "application/json",
    "X-Auth-Token": ticket
}

resp = requests.get(url,headers=headers,verify=False)
response_json = resp.json()
print('')
numPersonas = response_json['number']
pprint("Hay " + str(numPersonas) + ' personas en el espacio!!!')

pprint('Sus nombres son')
pprint(response_json['people'][0]['name'])
pprint(response_json['people'][1]['name'])
pprint(response_json['people'][2]['name'])
pprint(response_json['people'][3]['name'])
pprint(response_json['people'][4]['name'])
pprint(response_json['people'][5]['name'])
print('')

