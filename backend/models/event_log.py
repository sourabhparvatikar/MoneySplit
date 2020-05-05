from datetime import datetime
from backend import db


class EventLog(db.Model):

    __tablename__ = 'eventlog'
    id = db.Column(db.Integer,
                   primary_key=True)
    type = db.Column(db.String(64), nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
