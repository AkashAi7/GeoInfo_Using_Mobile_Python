import phonenumbers

from myphone import num
import folium 

num='+917390818458'
# Extracting the country name 
from phonenumbers import geocoder
pepnumber=phonenumbers.parse(num)
location=geocoder.description_for_number(pepnumber, "en")
print('location',location)

# Service Provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(num, "RO")
print(carrier.name_for_number(service_provider, "en"))


# latitue and longitude
from opencage.geocoder import OpenCageGeocode

key='2006547941b74ddcbe50ea04155647a0'
geocoder=OpenCageGeocode(key)

query=str(location)

RESULTS=geocoder.geocode(query)


# print(RESULTS)

lat=RESULTS[0]['geometry']['lat']

long=RESULTS[0]['geometry']['lng']


print(lat , long )

# my_map = folium.Map(location=[lat,long], zoom_start=12)

# folium.marker([lat,long], popup=location).add_to(my_map)

# # save map in html file
# my_map.save('map.html')



# Lat long to State Conversion 

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
state = geolocator.reverse(str(lat)+","+str(long))

print('State:',state.raw['address']['state'])



