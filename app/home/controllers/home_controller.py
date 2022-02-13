from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, Resource

home_api_bp = Blueprint("home_api_bp", __name__)

api = Api(home_api_bp)


class ApiHome(Resource):
    @jwt_required()
    def get():
        current_user = get_jwt_identity()
        return jsonify(loggin_in_as=current_user), 200


api.add_resource(ApiHome, "/", endpoint="home")
