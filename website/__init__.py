from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#__init__.py makes this file a package

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"

    # import routes from views file 
    # routes are stored in the views variable  
    # the dot is needed to show there is a relative import from inside the python package 
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    # @app.route adds a new webpage 
    # "/" is the address of the website that is being visited
    # inside the function is the logic of the webpage 
    # return is what is displayed
    @app.route("/")
    def home():
        return "<h1>Hello<h1>"

    # add "/profile" at the end of the existing address in the search bar to change pages 
    @app.route("/profile")
    def profile():
        return "<h1>Profile<h1>"

    return app