from sqlalchemy import Column, String, BigInteger
from app.database.db import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    def get_user_by_email(user_email):
        return User.query.filter_by(email=user_email).first()

    def get_users():
        return User.query.all()
