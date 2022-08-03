# webpages / blueprint
# store views route

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)
    # flask knows to search for templates in folders called "templates"
