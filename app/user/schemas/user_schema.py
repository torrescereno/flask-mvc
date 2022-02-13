from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    password = fields.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
