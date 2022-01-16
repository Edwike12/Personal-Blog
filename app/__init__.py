from flask import Flask
#from app import SQLALchemy
from os import path
from flask_login import LoginManager

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"



    return app