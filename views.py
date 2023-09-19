from flask import Blueprint, render_template, request
from api import current_cloud, current_visibility

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", location="Your location", cloud=current_cloud, visibility=current_visibility)

@views.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        location = request.form.get("location")
        return render_template('index.html', cloud=current_cloud, visibility=current_visibility, location = location)
