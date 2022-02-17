import uuid
import click

from flask.cli import with_appcontext
from app import db

from app.api.models.user_model import User
from app.database.db import save_changes


@click.command(name="db")
@with_appcontext
def create_db():
    """Create database"""
    db.create_all()


@click.command(name="admin")
@click.argument("username")
@click.argument("name")
@click.argument("email")
@click.argument("password")
@with_appcontext
def create_user(username: str, name: str, email: str, password: str):
    """Create user"""
    id = uuid.uuid4()
    id = str(id.int)
    id = int(id[:4])
    user = User(id=id, username=username, name=name, email=email)
    user.set_password(password)
    save_changes(user)


@click.command(name="test")
@with_appcontext
def run_test():
    """Run test"""
    import pytest

    rv = pytest.main(["-v"])
    exit(rv)


@click.command(name="coverage")
@with_appcontext
def run_converage():
    """Run coverage"""
    import coverage
    import pytest

    cov = coverage.Coverage()
    cov.start()

    rv = pytest.main(["-v"])

    cov.stop()
    cov.save()

    print("Coverage summary")

    cov.report()
    cov.html_report()
    cov.erase()

    exit(rv)
