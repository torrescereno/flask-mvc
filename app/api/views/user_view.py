from flask import Blueprint, request
from flask_restful import Api, Resource

from app.api.controllers.user_controller import UserController
from app.api.schemas.user_schema import user_schema, users_schema

user_api_bp = Blueprint("user_api_bp", __name__)

api = Api(user_api_bp)


class ApiUser(Resource):
    @staticmethod
    def get():
        users = UserController.get_all_users()
        result = users_schema.dump(users)

        return {"users": result}

    @staticmethod
    def post():
        json_data = request.get_json()

        if not json_data:
            return {"message": "No input data provider"}, 400

        try:
            data = user_schema.load(json_data)
        except Exception as err:
            return err.messages, 422

        result = UserController.save_new_user(data)
        return result


api.add_resource(ApiUser, "/users", endpoint="users")
