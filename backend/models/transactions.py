from datetime import datetime

from sqlalchemy import ForeignKey

from backend import db


def default_for_modified_datetime(context):
    return context.get_current_parameters()['created_datetime']


class Transactions(db.Model):
    """Creating model for transactions table"""

    __tablename__ = 'transactions'

    id = db.Column(db.Integer,
                   primary_key=True)
    payer = db.Column(db.Integer,
                      ForeignKey('user.id', ondelete='CASCADE'),
                      nullable=False)

    ower = db.Column(db.Integer,
                     ForeignKey('user.id', ondelete='CASCADE'),
                     nullable=False)

    amount = db.Column(db.Float, nullable=False)

    reason = db.Column(db.String(64), nullable=False)
    event = db.Column(db.Integer,
                      ForeignKey('eventlog.id', ondelete='CASCADE'),
                      nullable=False)
    group = db.Column(db.Integer,
                      ForeignKey('friend_groups.id', ondelete='CASCADE'),
                      nullable=False)
    valid = db.Column(db.Enum("Y", "N"), server_default="Y", nullable=False)
    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())
    modified_datetime = db.Column(db.DateTime, nullable=False,
                                  default=default_for_modified_datetime)

    def save(self):
        db.session.add(self)
        db.session.commit()
