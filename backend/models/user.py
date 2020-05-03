from datetime import datetime
from backend import db


def default_for_modified_datetime(context):
    return context.get_current_parameters()['created_datetime']


class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())
    modified_datetime = db.Column(db.DateTime, nullable=False,
                                  default=default_for_modified_datetime)

    def save(self):
        db.session.add(self)
        db.session.commit()
