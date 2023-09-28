from flask import Blueprint, render_template, request
from api import weather_specs, astro_object

views = Blueprint(__name__, "views")

default_weather = weather_specs("New York City")
default_astronomy = astro_object("Betelgeuse")


@views.route("/", methods = ['POST', 'GET'])
def home():
    global default_weather, default_astronomy
    if request.method == 'GET':
        return render_template('index.html',
                                location=default_weather["address"],
                                visibility1=default_weather["visibility1"],
                                visibility2=default_weather["visibility2"],
                                visibility3=default_weather["visibility3"],
                                visibility4=default_weather["visibility4"],
                                visibility5=default_weather["visibility5"],
                                    cloud1=default_weather["cloud1"],
                                    cloud2=default_weather["cloud2"],
                                    cloud3=default_weather["cloud3"],
                                    cloud4=default_weather["cloud4"],
                                    cloud5=default_weather["cloud5"],
                                        prec1=default_weather["prec1"],
                                        prec2=default_weather["prec2"],
                                        prec3=default_weather["prec3"],
                                        prec4=default_weather["prec4"],
                                        prec5=default_weather["prec5"],
                                            humid1=default_weather["humid1"],
                                            humid2=default_weather["humid2"],
                                            humid3=default_weather["humid3"],
                                            humid4=default_weather["humid4"],
                                            humid5=default_weather["humid5"],
                                                wind1=default_weather["wind1"],
                                                wind2=default_weather["wind2"],
                                                wind3=default_weather["wind3"],
                                                wind4=default_weather["wind4"],
                                                wind5=default_weather["wind5"],
                                                    sunrise=default_weather["sunrise"],
                                                    sunset=default_weather["sunset"],
                                                        id=default_astronomy["id"],
                                                        name=default_astronomy["name"],
                                                        distance=default_astronomy["distance"],
                                                        app_mag=default_astronomy["apparent magnitude"],
                                                        spectp=default_astronomy["spectral type"],
                                                        wiki=default_astronomy["wikipedia"],
                                                        wiki_sum=default_astronomy["wiki summary"])
    
    if request.method == 'POST':
        obj = request.form.get("astronomy")
        location = request.form.get("location")

        if obj == None:
            weather = weather_specs(str(location))
            if weather == False: return render_template('error.html')
            default_weather = weather

        if location == None:
            astro_list = astro_object(str(obj))
            if astro_list == False: return render_template('error.html')
            default_astronomy = astro_list




        
        return render_template('index.html',
                                location=default_weather["address"],
                                visibility1=default_weather["visibility1"],
                                visibility2=default_weather["visibility2"],
                                visibility3=default_weather["visibility3"],
                                visibility4=default_weather["visibility4"],
                                visibility5=default_weather["visibility5"],
                                    cloud1=default_weather["cloud1"],
                                    cloud2=default_weather["cloud2"],
                                    cloud3=default_weather["cloud3"],
                                    cloud4=default_weather["cloud4"],
                                    cloud5=default_weather["cloud5"],
                                        prec1=default_weather["prec1"],
                                        prec2=default_weather["prec2"],
                                        prec3=default_weather["prec3"],
                                        prec4=default_weather["prec4"],
                                        prec5=default_weather["prec5"],
                                            humid1=default_weather["humid1"],
                                            humid2=default_weather["humid2"],
                                            humid3=default_weather["humid3"],
                                            humid4=default_weather["humid4"],
                                            humid5=default_weather["humid5"],
                                                wind1=default_weather["wind1"],
                                                wind2=default_weather["wind2"],
                                                wind3=default_weather["wind3"],
                                                wind4=default_weather["wind4"],
                                                wind5=default_weather["wind5"],
                                                    sunrise=default_weather["sunrise"],
                                                    sunset=default_weather["sunset"],
                                                        id=default_astronomy["id"],
                                                        name=default_astronomy["name"],
                                                        distance=default_astronomy["distance"],
                                                        app_mag=default_astronomy["apparent magnitude"],
                                                        spectp=default_astronomy["spectral type"],
                                                        wiki=default_astronomy["wikipedia"],
                                                        wiki_sum=default_astronomy["wiki summary"])








# return render_template('index.html',
#                                 location=weather["address"],
#                                 visibility1=weather["visibility1"],
#                                 visibility2=weather["visibility2"],
#                                 visibility3=weather["visibility3"],
#                                 visibility4=weather["visibility4"],
#                                 visibility5=weather["visibility5"],
#                                     cloud1=weather["cloud1"],
#                                     cloud2=weather["cloud2"],
#                                     cloud3=weather["cloud3"],
#                                     cloud4=weather["cloud4"],
#                                     cloud5=weather["cloud5"],
#                                         prec1=weather["prec1"],
#                                         prec2=weather["prec2"],
#                                         prec3=weather["prec3"],
#                                         prec4=weather["prec4"],
#                                         prec5=weather["prec5"],
#                                             humid1=weather["humid1"],
#                                             humid2=weather["humid2"],
#                                             humid3=weather["humid3"],
#                                             humid4=weather["humid4"],
#                                             humid5=weather["humid5"],
#                                                 wind1=weather["wind1"],
#                                                 wind2=weather["wind2"],
#                                                 wind3=weather["wind3"],
#                                                 wind4=weather["wind4"],
#                                                 wind5=weather["wind5"],
#                                                     sunrise=weather["sunrise"],
#                                                     sunset=weather["sunset"],
#                                                         id=astro_list["id"],
#                                                         name=astro_list["name"],
#                                                         distance=astro_list["distance"],
#                                                         app_mag=astro_list["apparent magnitude"],
#                                                         spectp=astro_list["spectral type"],
#                                                         wiki=astro_list["wikipedia"],
#                                                         wiki_sum=astro_list["wiki summary"])