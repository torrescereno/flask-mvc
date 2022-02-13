from typing import Dict, Tuple
from app.user.models.user_model import User
from app.user.schemas.user_schema import user_schema
from app.database.db import save_chages


def save_new_user(data: object) -> Tuple[Dict[str, str], int]:

    user = User.query.filter_by(id=data["id"]).first()
    if user is None:
        new_user = User(
            id=data["id"], name=data["name"], email=data["email"], password=data["password"]
        )
        save_chages(new_user)
        result = user_schema.dump(User.query.get(new_user.id))
        return {"message": "Created new user", "user": result}, 200

    result = {
        "message": "User already exists",
    }
    return result, 409


def get_a_user(email: str) -> User:
    return User.query.filter_by(email=email).first()


def get_all_users() -> Tuple[User]:
    return User.query.all()
