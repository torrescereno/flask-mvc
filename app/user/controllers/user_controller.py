from flask import Blueprint, request
from flask_restful import Api, Resource

from app.user.schemas.user_schema import user_schema, users_schema
from app.user.services.user_services import save_new_user, get_all_users

user_api_bp = Blueprint("user_api_bp", __name__)

api = Api(user_api_bp)


class ApiUser(Resource):
    def get(self):
        users = get_all_users()
        result = users_schema.dump(users)
        return {"users": result}

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provider"}, 400

        try:
            data = user_schema.load(json_data)
        except Exception as err:
            return err.messages, 422

        result = save_new_user(data)
        return result


api.add_resource(ApiUser, "/users", endpoint="users")
