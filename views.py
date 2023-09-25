from flask import Blueprint, render_template, request
from api import weather_specs, astro_object

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/", methods=['POST', 'GET'])
def button():
    if request.method == 'POST':
        return render_template("index.html")

@views.route("/astro-catalog", methods = ['POST', 'GET'])
def astro():
    if request.method == 'GET':
        return f"The URL /astro-catalog is accessed directly."
    if request.method == 'POST':
        obj = request.form.get("astronomy")
        astro_list = astro_object(str(obj))
        return render_template("catalog.html",
    	                       input_name=obj,
    	                        name=astro_list["name"],
    	                          distance=astro_list["distance"],
    	                            mag=astro_list["apparent magnitude"],
    	                              wikipedia=astro_list["wikipedia"])

@views.route('/weather', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /weather is accessed directly."
    if request.method == 'POST':
        location = request.form.get("location")
        weather = weather_specs(str(location))
        return render_template('weather.html',
                                precipitation=weather["curr_precipitation_prob"],
                                  cloud=weather["curr_cloud"],
                                    visibility=weather["curr_visibility"],
                                      location=location)
