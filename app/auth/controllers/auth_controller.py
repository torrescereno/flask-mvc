from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from flask_jwt_extended import create_access_token

auth_api_bp = Blueprint("auth_api_bp", __name__)


api = Api(auth_api_bp)


class ApiAuth(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "admin" or password != "123":
            return jsonify(message="Invalid user"), 401
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)


api.add_resource(ApiAuth, "/login", endpoint="login")
