from sqlalchemy import Column, String, BigInteger
from app.database.db import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
