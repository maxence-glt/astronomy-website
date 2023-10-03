from flask import Blueprint, render_template, request
from api import weather_specs, astro_object

views = Blueprint(__name__, "views")

default_weather = weather_specs("New York City")
default_astronomy = astro_object("Sombrero Galaxy")


@views.route("/", methods = ['POST', 'GET'])
def home():
    global default_weather, default_astronomy
    if request.method == 'GET':
        return render_template('index.html', defastro=default_astronomy, defweather=default_weather)
    
    if request.method == 'POST':
        obj = request.form.get("astronomy")
        location = request.form.get("location")

        if obj == None:
            weather = weather_specs(str(location))
            if weather == False: return render_template('error.html', request=location)
            default_weather = weather

        if location == None:
            astro_list = astro_object(str(obj))
            if astro_list == False: return render_template('error.html', request=obj)
            default_astronomy = astro_list

        return render_template('index.html', defastro=default_astronomy, defweather=default_weather)
