class Config(object):

    TESTING = False
    SECRET_KEY = "supersecreto"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"


class ProductionConfig(Config):
    pass
