import pymysql
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("DB_USERNAME", "")
password = os.environ.get("DB_PASSWORD", "")
userpass = "mysql+pymysql://" + username + ":" + password + "@"
server = os.environ.get("DB_HOST", "")
dbname = os.environ.get("DB_NAME", "")

db = SQLAlchemy()
ma = Marshmallow()

API_DEFINITION = "/static/api_definition.yml"
SWAGGER_URL = "/api/docs"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_DEFINITION,
    config={"app_name": "API"},
)


def create_app(testing=False):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = userpass + server + "/" + dbname
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    from routes.api import api_pb

    app.register_blueprint(api_pb, url_prefix="/api")
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
    CORS(app)

    return app
