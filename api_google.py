import requests

my_location = '300 west 42nd Street, New York, NY'    # address
with open('api_key_file', 'r') as kf:
    api_key = kf.read()                               # key

payload = {'key': api_key, 'address': my_location}

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

r = requests.get(url, params=payload)

lat = r.json()['results'][0]['geometry']['location']['lat']
lng = r.json()['results'][0]['geometry']['location']['lng']

print("{} \t {}".format(lat, lng))

# --------------------------------

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?parameters'

payload1 = {'key': api_key, 'location': str(lat) + "," + str(lng), 'radius': 9500, 'type': 'restaurant'}

r = requests.get(url, params=payload1)

# print(json.dumps(r.json()['results'][2]['name'],indent=2))

for i in r.json()['results']:
    print(i['name'])
