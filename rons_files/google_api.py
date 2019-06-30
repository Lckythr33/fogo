# documentation : https://developers.google.com/places/web-service/search

import googlemaps
import pprint
import time

API_KEY = 'AIzaSyBYKjjTJ__PNE2MIeJSOaZHIGuWQh-UHmY'

gmaps = googlemaps.Client(key = API_KEY)

places_result  = gmaps.places_nearby(location='-33.8670522,151.1957362', keyword = 'food bank', radius = 8000)

pprint.pprint(places_result)