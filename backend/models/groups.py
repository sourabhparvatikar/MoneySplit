from datetime import datetime
from backend import db


def default_for_modified_datetime(context):
    return context.get_current_parameters()['created_datetime']


class Groups(db.Model):

    __tablename__ = 'friend_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())
    modified_datetime = db.Column(db.DateTime, nullable=False,
                                  default=default_for_modified_datetime)
    deleted = db.Column(db.Enum("Y", "N"), server_default="N")

    def save(self):
        db.session.add(self)
        db.session.commit()
