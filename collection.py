import requests, json, time
from web3 import web3

offset = {'assets': []}

while True:
    params = {
        'collection':'the-wanderers',
        'order_by':'pk',
        'order_direction':'asc',
        'offset': offset,
        'limit':50
    }

    r = requests.get('https://api.opensea.io/api/v1/assets', params=params)
    response_json = r.json()
    data['assets'].extend(response_json['assets'])

    if len(response_json['assets']) < 50:
        break

    offset += 50

print(json_dumps(data))