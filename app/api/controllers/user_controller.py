from typing import Dict, Tuple

from app.api.models.user_model import User
from app.api.schemas.user_schema import user_schema
from app.database.db import save_changes


class UserController:
    @staticmethod
    def save_new_user(data: object) -> Tuple[Dict[str, str], int]:
        id = data["id"]
        username = data["name"]
        name = data["name"]
        email = data["email"]
        password = data["password"]

        user = User.get_user_by_id(user_id=id)
        if user is None:
            new_user = User(id=id, username=username, name=name, email=email)
            new_user.set_password(password)

            save_changes(new_user)
            result = user_schema.dump(User.query.get(new_user.id))
            return {"message": "Created new user", "user": result}, 200

        result = {
            "message": "User already exists",
        }

        return result, 409

    @staticmethod
    def get_a_user(email: str) -> User:
        return User.get_user_by_email(user_email=email)

    @staticmethod
    def get_all_users() -> Tuple[User]:
        return User.get_users()
