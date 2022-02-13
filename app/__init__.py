from flask import Flask, jsonify

from flask_jwt_extended import jwt_required

from app.database.db import db
from app.extensions.ext import ma, jwt, migrate


from app.user.controllers.user_controller import user_api_bp
from app.auth.controllers.auth_controller import auth_api_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "supersecreto"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    @app.route("/", methods=["GET"])
    @jwt_required()
    def home():
        # current_user = get_jwt_identity()
        # return jsonify(loggin_in_as=current_user), 200
        return jsonify(message="Welcome"), 200

    app.register_blueprint(user_api_bp)
    app.register_blueprint(auth_api_bp)

    return app
