from sqlalchemy import Column, String, BigInteger, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<User> {self.email}"

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_user_by_id(user_id: int):
        return User.query.filter_by(id=user_id).first()

    @staticmethod
    def get_user_by_email(user_email):
        return User.query.filter_by(email=user_email).first()

    @staticmethod
    def get_users():
        return User.query.all()
