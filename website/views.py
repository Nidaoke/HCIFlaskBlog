# webpages / blueprint
# store views route 
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return render_template("home.html")
    # flask knows to search for templates in folders called "templates"