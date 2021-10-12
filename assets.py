import requests
import json

params = {
    ' collection': 'the-wanderers'
}

r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

print(r.json.dumps(r.json()))
