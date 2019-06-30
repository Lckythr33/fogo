# documentation: https://docs.routific.com/

# Step 1: Import http client and set routific vrp url
import urllib2
import json

URL   = "https://api.routific.com/v1/vrp"

# Step 2: Prepare visits
visits = {
    "order_1": {
      "location": {
        "name": "6800 Cambie",
        "lat": 49.227107,
        "lng": -123.1163085
      }
    },
    "order_2": {
      "location": {
        "name": "3780 Arbutus",
        "lat": 49.2474624,
        "lng": -123.1532338
      }
    },
    "order_3": {
      "location": {
        "name": "800 Robson",
        "lat": 49.2819229,
        "lng": -123.1211844
      }
    }
}

# Step 3: Prepare vehicles
fleet = {
    "vehicle_1": {
      "start_location": {
        "id": "depot",
        "name": "800 Kingsway",
        "lat": 49.2553636,
        "lng": -123.0873365
      }
    },
    "vehicle_2": {
      "start_location": {
        "id": "depot",
        "name": "800 Kingsway",
        "lat": 49.2553636,
        "lng": -123.0873365
      }
    }
}

# Step 4: Prepare data payload
data = {
    "visits": visits,
    "fleet": fleet
}

# Step 5: Put together request
# This is your demo token
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDE3YjE5ZDI5Nzg3ZjUyODc5NGEzYTgiLCJpYXQiOjE1NjE4MzM4ODV9._YYEgmP84ejG706xl3DKnVq37DNV-gBzG06C9MLejIU'

req = urllib2.Request(URL, json.dumps(data))
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', "bearer " + token)

# Step 6: Get route
res = urllib2.urlopen(req).read()

print(res)