from datetime import datetime
from sqlalchemy import ForeignKey

from backend import db


class Events(db.Model):
    """Creating model for events table"""
    __tablename__ = "events"

    id = db.Column(db.Integer,
                   primary_key=True)

    user_id = db.Column(db.Integer,
                        ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False)

    reason = db.Column(db.String(64), nullable=False)

    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
