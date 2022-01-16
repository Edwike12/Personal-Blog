from flask import Flask
#from app import SQLALchemy
from os import path
from flask_login import LoginManager

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"

    @app.route("/")
    def home():
        return "<h1>HELLO WORLD</h1>"

    from .views import views

    app.register_blueprint(views, url_prefix="/")        

    return app