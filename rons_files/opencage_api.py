# documentation : https://opencagedata.com/tutorials/geocode-in-python

from opencage.geocoder import OpenCageGeocode

key = '830e9efd76164eb2ae2bd2ab336d6837'
geocoder = OpenCageGeocode(key)

query = u'Los Angeles, CA'
results = geocoder.geocode(query)

print(u'%f%f' % (results[0]['geometry']['lat'], results[0]['geometry']['lng']))
# 45.797095;15.982453;hr;Europe/Belgrade