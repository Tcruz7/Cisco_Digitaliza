import requests
import json
from pprint import pprint
from tabulate import *
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
personas = response_json['people']
pprint('Sus nombres son')
i=0
while i < len(personas):
    pprint(response_json['people'][i]['name'])
    i=i+1

print('')
