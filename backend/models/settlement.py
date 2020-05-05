from datetime import datetime

from sqlalchemy import ForeignKey

from backend import db


def default_for_modified_datetime(context):
    return context.get_current_parameters()['created_datetime']


class Settlement(db.Model):
    """Creating model for settlement table"""
    __tablename__ = "settlement"

    id = db.Column(db.Integer,
                   primary_key=True)

    ower = db.Column(db.Integer,
                     ForeignKey('user.id', ondelete='CASCADE'),
                     nullable=False)

    payer = db.Column(db.Integer,
                      ForeignKey('user.id', ondelete='CASCADE'),
                      nullable=False)

    amount = db.Column(db.Float, nullable=False)
    is_settled = db.Column(db.Enum("Y", "N"), server_default="N",
                           nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())
    modified_datetime = db.Column(db.DateTime, nullable=False,
                                  default=default_for_modified_datetime)

    def save(self):
        db.session.add(self)
        db.session.commit()
