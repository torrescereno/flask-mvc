from sqlalchemy import Column, String, BigInteger
from app.database.db import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def get_user_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    def get_user_by_email(cls, user_email):
        return cls.query.filter_by(email=user_email).first()

    def get_users(cls):
        return cls.query.all()
