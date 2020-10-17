import requests
import json

lat = '41.2042616'
lng = '-73.72707609999999'

r = requests.get(
    'https://reverse.geocoder.ls.hereapi.com/6.2/reversegeocode.json?prox=' + lat + '%2C' + lng + '%2C250&mode='
                        'retrieveAddresses&maxresults=1&gen=9&apiKey=[your API Key]')
    

print(r.status_code)

# print(json.dumps(r.json(),indent=2),)

print(r.json()['Response']['View'][0]['Result'][0]['Location']['Address']['Label'])

# p = re.compile(r'Address":{"Label":"[\w  , ]+')
# print(re.search(p, r.text).group(0)[19:])
