from app import ma
from app.user.models.user_model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    password = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
