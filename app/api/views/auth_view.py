from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from flask_restful import Api, Resource

from app.api.models.user_model import User

auth_api_bp = Blueprint("auth_api_bp", __name__)

api = Api(auth_api_bp)


class ApiAuth(Resource):
    @staticmethod
    def post():
        username = request.json.get("username", None)

        user = User.get_user_by_username(username=username)

        if not user:
            return {"message": "Invalid user"}, 402

        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200


api.add_resource(ApiAuth, "/login", endpoint="login")
