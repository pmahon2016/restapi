import requests
import json 
my_location = 'Dublin, Ireland'

api_key = API_KEY

payload = {'key': api_key, 'address':my_location} 
           

url = 'https://maps.googleapis.com/maps/api/geocode/' 'json?'

r = requests.get(url, params=payload)
