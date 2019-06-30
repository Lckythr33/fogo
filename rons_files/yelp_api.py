#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

# Import the modules
import requests
import json

# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = 'CTVhIYW7svOGojHn5JrEnlJt7AuZpAKVx3X5oGUTsJnDyFS2dXtECo9AArFMOOb8DRA6KIxDGCoXM7jI2qE_bxQdVdZh5lROIWYdfKafzGBb5hMSdo_HKfuh7ZHtXHYx'
# ENDPOINT_reviews = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
ENDPOINT_business = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
PARAMETERS = {'term': 'food bank',
             'limit': 5,
             'offset': 50,
             'radius': 10000,
             'location': 'Cypress, CA 90630'}

# BUSINESS MATCH PARAMETERS - EXAMPLE
#PARAMETERS = {'name': 'Peets Coffee & Tea',
#              'address1': '7845 Highland Village Pl',
#              'city': 'San Diego',
#              'state': 'CA',
#              'country': 'US'}

# Make a request to the Yelp API
response = requests.get(url = ENDPOINT_business,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String
business_data = response.json()

# print the response
print(json.dumps(business_data, indent = 3))