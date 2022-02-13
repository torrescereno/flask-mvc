import uuid
import click

from flask.cli import with_appcontext
from app import db

from app.user.models.user_model import User
from app.database.db import save_chages


@click.command(name="db")
@with_appcontext
def create_db():
    """Create database"""
    db.create_all()


@click.command(name="admin")
@click.argument("name")
@click.argument("email")
@click.argument("password")
@with_appcontext
def create_user(name: str, email: str, password: str):
    """Create user"""
    id = uuid.uuid4()
    id = str(id.int)
    id = int(id[:4])
    user = User(id=id, name=name, email=email, password=password)
    save_chages(user)


@click.command(name="test")
@with_appcontext
def run_test():
    """Run test"""
    import pytest

    rv = pytest.main(["-v"])
    exit(rv)
