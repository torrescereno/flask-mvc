from flask import Flask, jsonify, request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from .db import db

jwt = JWTManager()


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "supersecreto"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    jwt.init_app(app)
    db.init_app(app)

    @app.route("/", methods=["GET"])
    @jwt_required()
    def home():
        current_user = get_jwt_identity()
        return jsonify(loggin_in_as=current_user), 200

    @app.route("/login", methods=["POST"])
    def login():
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "admin" or password != "123":
            return jsonify(msg="Usuario no es valido"), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return app
