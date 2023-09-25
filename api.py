import datetime as dt
import requests
import ssl
import certifi
import geopy.geocoders
from geopy.geocoders import Nominatim
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord





# ssl certification for geopy and VOT mods for SIMBAD
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
Simbad.add_votable_fields('flux(V)', 'distance')


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
    
    weather_list = {
        "address": str(getLoc.address) + "(" + str(round((getLoc.longitude), 3)) + ", " + str(round((getLoc.latitude), 3)) + ")",
        "curr_cloud": str(response.json()["hourly"]["cloudcover"][dt.datetime.now().hour]) + "%",
        "curr_visibility": str(response.json()["hourly"]["visibility"][dt.datetime.now().hour]) + " meters",
        "curr_precipitation_prob": str(response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour]) + "%"
    }
    return weather_list

def astro_object(obj: str) -> dict:
    result_table = Simbad.query_object(str(obj))
    if result_table is None: return "The inputed object was not recognized by the SIMBAD Astronomical Database"

    obj_list = {
        "name": result_table[0][0],
        "distance": str(result_table[0][-8]) + result_table[0][-6],
        "apparent magnitude": result_table[0][-9],
        "wikipedia": f"wikipedia.org/wiki/{obj.replace(' ', '_')}"
    }
    return obj_list

print(weather_specs("mount marcy"))