from flask import Blueprint, render_template, request
from api import weather_specs, astro_object

views = Blueprint(__name__, "views")

default = weather_specs("New York City")

@views.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html',
                                location=default["address"],
                                visibility1=default["visibility1"],
                                visibility2=default["visibility2"],
                                visibility3=default["visibility3"],
                                visibility4=default["visibility4"],
                                visibility5=default["visibility5"],
                                    cloud1=default["cloud1"],
                                    cloud2=default["cloud2"],
                                    cloud3=default["cloud3"],
                                    cloud4=default["cloud4"],
                                    cloud5=default["cloud5"],
                                        prec1=default["prec1"],
                                        prec2=default["prec2"],
                                        prec3=default["prec3"],
                                        prec4=default["prec4"],
                                        prec5=default["prec5"],
                                            humid1=default["humid1"],
                                            humid2=default["humid2"],
                                            humid3=default["humid3"],
                                            humid4=default["humid4"],
                                            humid5=default["humid5"],
                                                wind1=default["wind1"],
                                                wind2=default["wind2"],
                                                wind3=default["wind3"],
                                                wind4=default["wind4"],
                                                wind5=default["wind5"],
                                                    sunrise=default["sunrise"],
                                                    sunset=default["sunset"])
    if request.method == 'POST':
        location = request.form.get("location")
        weather = weather_specs(str(location))
        if weather == False:  
            return render_template('error.html')
        return render_template('index.html',
                                location=weather["address"],
                                visibility1=weather["visibility1"],
                                visibility2=weather["visibility2"],
                                visibility3=weather["visibility3"],
                                visibility4=weather["visibility4"],
                                visibility5=weather["visibility5"],
                                    cloud1=weather["cloud1"],
                                    cloud2=weather["cloud2"],
                                    cloud3=weather["cloud3"],
                                    cloud4=weather["cloud4"],
                                    cloud5=weather["cloud5"],
                                        prec1=weather["prec1"],
                                        prec2=weather["prec2"],
                                        prec3=weather["prec3"],
                                        prec4=weather["prec4"],
                                        prec5=weather["prec5"],
                                            humid1=weather["humid1"],
                                            humid2=weather["humid2"],
                                            humid3=weather["humid3"],
                                            humid4=weather["humid4"],
                                            humid5=weather["humid5"],
                                                wind1=weather["wind1"],
                                                wind2=weather["wind2"],
                                                wind3=weather["wind3"],
                                                wind4=weather["wind4"],
                                                wind5=weather["wind5"],
                                                    sunrise=weather["sunrise"],
                                                    sunset=weather["sunset"])



@views.route("/astro-catalog", methods = ['POST', 'GET'])
def astro():
    if request.method == 'GET':
        return f"The URL /astro-catalog is accessed directly."
    if request.method == 'POST':
        obj = request.form.get("astronomy")
        astro_list = astro_object(str(obj))
        return render_template("catalog.html",
    	                        input_name=obj.capitalize(),
    	                            name=astro_list["name"],
    	                                distance=astro_list["distance"],
    	                                    mag=astro_list["apparent magnitude"],
    	                                        wikipedia=astro_list["wikipedia"])

