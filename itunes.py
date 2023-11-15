import requests
import json

URL = "https://itunes.apple.com/search?entity=song&limit=25&term=weezer"

atbilde = requests.get(URL)

print(atbilde)

dati = atbilde.json()

print(json.dumps(dati,indent = 2))

for a in dati['results']:
    print(a["trackName"])
