from ..base import BaseConfig
from flask_jwt_extended import create_access_token


class TestAuth(BaseConfig):
    def test_create_token(self):

        msg_error = {"message": "Invalid user"}
        username = "test"
        password = "111"

        if username != "admin" or password != "123":
            result = {"message": "Invalid user"}
        assert result == msg_error

        access_token = create_access_token(identity=username)
        token = {"access_token": access_token}
        assert token is not []
        assert token["access_token"] != ""
