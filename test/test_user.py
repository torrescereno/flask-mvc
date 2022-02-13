from .base import BaseConfig
from app.user.models.user_model import User
from app.user.services.user_services import get_all_users, get_a_user
from app.user.schemas.user_schema import users_schema, user_schema
from app import db


class TestUserModel(BaseConfig):
    def test_create_user(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        get_user = User.query.get(user.id)
        assert get_user.id == 0

    def test_get_all_users(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        users = get_all_users()
        assert users is not None
        result = users_schema.dump(users)
        assert result is not []

    def test_get_user(self):
        user = User(id=0, name="test", email="test@test.com", password="123")
        db.session.add(user)
        user = get_a_user(email=user.email)
        assert user is not None
        result = user_schema.dump(user)
        assert result is not []
