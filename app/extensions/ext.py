from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

jwt = JWTManager()
ma = Marshmallow()
migrate = Migrate()
