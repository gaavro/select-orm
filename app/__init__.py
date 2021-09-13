from flask import Flask
from app.configs import database,commands,migrate
from app import views
from os import getenv


def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    database.init_app(app)
    migrate.init_app(app)
    commands.init_app(app)
    views.init_app(app)
    return app

