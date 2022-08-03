# authentication page 

# webpages / blueprint
# where you store login page route
# render template gives access to fancy html templates
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "login page"

@auth.route("/sign-up")
def sign_up():
    return "sign-up"

@auth.route("/log-out")
def log_out():
    return "log-out"