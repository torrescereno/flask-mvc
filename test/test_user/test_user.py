import uuid

from ..base import BaseConfig
from app.user.models.user_model import User
from app.user.services.user_services import UserService
from app.user.schemas.user_schema import users_schema, user_schema
from app import db


class TestUserModel(BaseConfig):
    def test_create_user(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        get_user = User.query.get(user.id)
        assert get_user.id == 0


class TestUserServices(BaseConfig):
    def test_get_all_users(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        users = UserService.get_all_users()
        assert users is not None
        result = users_schema.dump(users)
        assert result is not []

    def test_get_user(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        user = UserService.get_a_user(email=user.email)
        assert user is not None
        result = user_schema.dump(user)
        assert result is not []

    def test_save_new_user(self):

        id = uuid.uuid4()
        id = str(id.int)
        id = int(id[:4])

        data = {
            "id": id,
            "name": "test",
            "email": "test@test.com",
            "password": "123",
        }

        result = UserService.save_new_user(data)
        assert result[0] is not []
        assert result[1] == 200

        # new_user = User(
        #     id=data["id"],
        #     name=data["name"],
        #     email=data["email"],
        #     password=data["password"],
        # )
