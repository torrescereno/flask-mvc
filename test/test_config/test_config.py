from ..base import BaseConfig


class TestConfig(BaseConfig):
    def test_testing_config(self):
        assert self.app.config["DEBUG"] is True
        assert self.app.config["TESTING"] is True
        assert self.app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] is False
        assert self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] is False
