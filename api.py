import datetime as dt
import requests
import ssl
import certifi
import geopy.geocoders
from geopy.geocoders import Nominatim

# ssl certification for geopy
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def weather_specs(location: str) -> tuple[str, str, str]:
    """Function that takes in any location on earth and (address, city, state)
    and returns a tuple with the attributes, in order, of the precipitation 
    probability, the cloud cover and the visibility of the input location at the
    current time, even optimizing for timezones"""
    geolocator = Nominatim(user_agent="my_request")
    getLoc = geolocator.geocode(location)
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=precipitation_probability,cloudcover,visibility&timezone=auto&forecast_days=3")

    # making sure the API key was input correctly
    if response.status_code != 200:
        print("API Key Invalid")
        return None
    
    curr_cloud = response.json()["hourly"]["cloudcover"][dt.datetime.now().hour]
    curr_visibility = response.json()["hourly"]["visibility"][dt.datetime.now().hour]
    curr_precipitation_prob = response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour]
    return (curr_precipitation_prob, curr_cloud, curr_visibility)

print(weather_specs("Toronto"))