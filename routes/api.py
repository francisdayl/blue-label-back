from flask import Blueprint, jsonify, request, Response
from sqlalchemy.sql import text
from marshmallow import ValidationError
from schemas.userOption import user_option_schema
from app import db

api_pb = Blueprint("api", __name__)
optionsSelect = ["Agent", "Main Corp", "Accounting"]


@api_pb.route("/get-options", methods=["GET"])
def get_options():
    # Modifica el codigo para que devuelva las opciones declaradas arriba en optionsSelect
    return jsonify({"status": 200, "body": optionsSelect})


@api_pb.route("/save", methods=["POST"])
def save():
    # Realiza aqui tu codigo para guardar la informacion en el txt,de la forma que creas mas conveniente
    print("Guardando...")
    try:
        user_option_data = user_option_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"message": "Validation error", "errors": err.messages}), 400
    try:
        with db.engine.begin() as connection:
            connection.execute(
                text(
                    """INSERT INTO user_options (name, email, selected_option) VALUES (:name, :email, :option)"""
                ),
                user_option_data,
            )
            connection.commit()

    except Exception as e:
        return jsonify({"message": "Database error", "errors": str(e)}), 500
    return jsonify({"status": 201, "message": "User option saved successfully"})


@api_pb.route("/")
def index():
    return "All Good"
