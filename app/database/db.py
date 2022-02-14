from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def save_changes(data: object) -> None:
    db.session.add(data)
    db.session.commit()
