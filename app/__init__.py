from flask import Flask

from app.database.db import db
from app.extensions.ext import ma, jwt, migrate

from cli import create_db, create_user, run_test, run_converage

from config.config import DevelopmentConfig

from app.user.controllers.user_controller import user_api_bp
from app.auth.controllers.auth_controller import auth_api_bp
from app.home.controllers.home_controller import home_api_bp


def create_app(config=DevelopmentConfig) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)

    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.cli.add_command(create_db)
    app.cli.add_command(create_user)
    app.cli.add_command(run_test)
    app.cli.add_command(run_converage)

    app.register_blueprint(user_api_bp)
    app.register_blueprint(auth_api_bp)
    app.register_blueprint(home_api_bp)

    return app
