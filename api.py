import datetime as dt
import requests
import ssl
import certifi
import geopy.geocoders
from geopy.geocoders import Nominatim

# ssl certification for geopy
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


geolocator = Nominatim(user_agent="my_request")
getLoc = geolocator.geocode("Plattsburgh")

print(getLoc.latitude, getLoc.longitude)

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=precipitation_probability,cloudcover,visibility&timezone=auto&forecast_days=3")

print(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=precipitation_probability,cloudcover,visibility&timezone=auto&forecast_days=3")
print(dt.datetime.now().hour)

if response.status_code != 200:
    print("API Key Invalid")


current_cloud = response.json()["hourly"]["cloudcover"][dt.datetime.now().hour]
current_visibility = response.json()["hourly"]["visibility"][dt.datetime.now().hour]

print("The current total cloud cover is " + str(current_cloud) + "%")
print("The current visibility is " + str(current_visibility) + "meters")