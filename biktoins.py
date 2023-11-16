import requests
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

atbilde = requests.get(URL)


dati = atbilde.json()

#print(json.dumps(dati,indent=2))

print(dati["bpi"]["USD"]["rate_float"])
a = float(input("ievadi bitkoinu skaitu: "))
b = a * dati["bpi"]["USD"]["rate_float"]
print("cena ir: ",b)
    