from flask import Flask

from app.database.db import db
from app.extensions.ext import ma, jwt, migrate

from cli import create_db, create_user, run_test

from app.user.controllers.user_controller import user_api_bp
from app.auth.controllers.auth_controller import auth_api_bp
from app.home.controllers.home_controller import home_api_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "supersecreto"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.cli.add_command(create_db)
    app.cli.add_command(create_user)
    app.cli.add_command(run_test)

    app.register_blueprint(user_api_bp)
    app.register_blueprint(auth_api_bp)
    app.register_blueprint(home_api_bp)

    return app
