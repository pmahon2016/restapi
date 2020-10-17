import requests

payload = {'q': 'Mount Kisco, USA', 'units': 'imperial'}

headers = {'x-rapidapi-key': 'YOUR API Key'}

url = 'https://community-open-weather-map.p.rapidapi.com/weather?'

r = requests.get(url, params=payload, headers = headers)

print(r.json()['main']['temp'])
