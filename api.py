import datetime as dt
import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=42.8865&longitude=-78.8784&hourly=precipitation_probability,cloudcover,visibility&timezone=auto&forecast_days=3")

if response.status_code != 200:
    print("API Key Invalid")


current_cloud = response.json()["hourly"]["cloudcover"][23]
current_visibility = response.json()["hourly"]["visibility"][23]

print("The current total cloud cover is " + str(current_cloud) + "%")
print("The current visibility is " + str(current_visibility) + "meters")