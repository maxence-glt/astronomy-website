import datetime as dt
import requests
import ssl
import certifi
import geopy.geocoders
import sys
import json

from geopy.geocoders import Nominatim

from astroquery.simbad import Simbad

import pprint
pp = pprint.PrettyPrinter(indent=4)

from urllib.parse import quote as urlencode

# Helper functions
def mast_query(request):
    request_url='https://mast.stsci.edu/api/v0/invoke'    
    version = ".".join(map(str, sys.version_info[:3]))
    headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
            "User-agent":"python-requests/"+version}
    req_string = json.dumps(request)
    req_string = urlencode(req_string)
    
    resp = requests.post(request_url, data="request="+req_string, headers=headers)
    
    head = resp.headers
    content = resp.content.decode('utf-8')
    return head, content
def set_filters(parameters):
    return [{"paramName":p, "values":v} for p,v in parameters.items()]
def set_min_max(min, max):
    return [{'min': min, 'max': max}]
def degToCompass(num) -> str:
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]
def time_format(time: str) -> str:
    hour = int(time[:2])
    if hour < 10:
        return time[1:] + " AM"
    if hour <= 12:
        return time + " AM"
    else:
        hour = hour - 12
        return str(hour) + time[2:] + " PM"



# ssl certification for geopy and VOT mods for SIMBAD
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
Simbad.add_votable_fields('distance', 'flux(V)', 'id(NAME)', 'sptype')




def weather_specs(location: str) -> dict:
    """Function that takes in any location on earth and (address, city, state)
    and returns a tuple with the attributes, in order, of the precipitation 
    probability, the cloud cover and the visibility of the input location at the
    current time, even optimizing for timezones"""
    geolocator = Nominatim(user_agent="my_request")
    getLoc = geolocator.geocode(location)
    if getLoc is None: return False

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={getLoc.latitude}&longitude={getLoc.longitude}&hourly=relativehumidity_2m,precipitation_probability,cloudcover,visibility,windspeed_10m,winddirection_10m&daily=sunrise,sunset&timezone=auto&forecast_days=3")
    # making sure the API key was input correctly
    if response.status_code != 200:
        print("API Key Invalid")
        return None

    weather_list = {
        "address": f'{getLoc.address} ({(round((getLoc.latitude), 3))}, {(round((getLoc.longitude), 3))})',
        "cloud1": f'{response.json()["hourly"]["cloudcover"][dt.datetime.now().hour]}%',
        "cloud2": f'{response.json()["hourly"]["cloudcover"][dt.datetime.now().hour + 1]}%',
        "cloud3": f'{response.json()["hourly"]["cloudcover"][dt.datetime.now().hour + 2]}%',
        "cloud4": f'{response.json()["hourly"]["cloudcover"][dt.datetime.now().hour + 3]}%',
        "cloud5": f'{response.json()["hourly"]["cloudcover"][dt.datetime.now().hour + 4]}%',
        "visibility1": f'{response.json()["hourly"]["visibility"][dt.datetime.now().hour]} meters',
        "visibility2": f'{response.json()["hourly"]["visibility"][dt.datetime.now().hour + 1]} meters',
        "visibility3": f'{response.json()["hourly"]["visibility"][dt.datetime.now().hour + 2]} meters',
        "visibility4": f'{response.json()["hourly"]["visibility"][dt.datetime.now().hour + 3]} meters',
        "visibility5": f'{response.json()["hourly"]["visibility"][dt.datetime.now().hour + 4]} meters',
        "prec1": f'{response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour]}',
        "prec2": f'{response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour + 1]}%',
        "prec3": f'{response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour + 2]}%',
        "prec4": f'{response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour + 3]}%',
        "prec5": f'{response.json()["hourly"]["precipitation_probability"][dt.datetime.now().hour + 4]}%',
        "humid1": f'{response.json()["hourly"]["relativehumidity_2m"][dt.datetime.now().hour]}%',
        "humid2": f'{response.json()["hourly"]["relativehumidity_2m"][dt.datetime.now().hour + 1]}%',
        "humid3": f'{response.json()["hourly"]["relativehumidity_2m"][dt.datetime.now().hour + 2]}%',
        "humid4": f'{response.json()["hourly"]["relativehumidity_2m"][dt.datetime.now().hour + 3]}%',
        "humid5": f'{response.json()["hourly"]["relativehumidity_2m"][dt.datetime.now().hour + 4]}%',
        "wind1": f'{response.json()["hourly"]["windspeed_10m"][dt.datetime.now().hour]}km/h, {response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour]}˚ ({degToCompass(response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour])})',
        "wind2": f'{response.json()["hourly"]["windspeed_10m"][dt.datetime.now().hour + 1]}km/h, {response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 1]}˚ ({degToCompass(response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 1])})',
        "wind3": f'{response.json()["hourly"]["windspeed_10m"][dt.datetime.now().hour + 2]}km/h, {response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 2]}˚ ({degToCompass(response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 2])})',
        "wind4": f'{response.json()["hourly"]["windspeed_10m"][dt.datetime.now().hour + 3]}km/h, {response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 3]}˚ ({degToCompass(response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 3])})',
        "wind5": f'{response.json()["hourly"]["windspeed_10m"][dt.datetime.now().hour + 4]}km/h, {response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 4]}˚ ({degToCompass(response.json()["hourly"]["winddirection_10m"][dt.datetime.now().hour + 4])})',
        "sunrise": time_format(response.json()["daily"]["sunrise"][0][-5:]),
        "sunset": time_format(str(response.json()["daily"]["sunset"][0][-5:]))
    }
    return weather_list

def astro_object(obj: str) -> dict:
    result_table = Simbad.query_object(str(obj))

    if result_table is None: return False

    resolver_request = {'service':'Mast.Name.Lookup',
                        'params':{'input':obj,
                                'format':'json'},
                        }
    headers, resolved_object_string = mast_query(resolver_request)
    resolved_object = json.loads(resolved_object_string)

    obj_ra, obj_dec = resolved_object['resolvedCoordinate'][0]['ra'], resolved_object['resolvedCoordinate'][0]['decl']

    picture = f"http://gsss.stsci.edu/webservices/dssjpg/dss.svc/GetImage?POS={obj_ra},{obj_dec}&SIZE=0"



    wiki_extract = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={obj}").json()["query"]["pages"]


    if '-1' in wiki_extract:
        wiki_output = "No wikipedia extract found! Try searching the object's wikipedia page through a web browser"
    
    if '-1' not in wiki_extract:
        wiki_output = wiki_extract[next(iter(wiki_extract))]["extract"]

    obj_list = {
        "id": result_table["MAIN_ID"][0],
        "name": result_table["ID_NAME"][0][5:],
        "distance": str(result_table["Distance_distance"][0]) + result_table["Distance_unit"][0],
        "apparent magnitude": result_table["FLUX_V"][0],
        "spectral type": result_table["SP_TYPE"][0],
        "wikipedia": f"wikipedia.org/wiki/{obj.replace(' ', '_')}",
        "wiki summary": wiki_output,
        "picture": picture
    }
    return obj_list
