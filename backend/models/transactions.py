from sqlalchemy import ForeignKey

from backend import db

class Transactions(db.Model):
    """Creating model for transactions table"""

    __tablename__ = 'transactions'

    id = db.Column(db.Integer,
                   primary_key=True)

    sender = db.Column(db.Integer,
                       ForeignKey('user.id', ondelete='CASCADE'),
                       nullable=False)

    receiver = db.Column(db.Integer,
                         ForeignKey('user.id', ondelete='CASCADE'),
                         nullable=False)

    amount = db.column(db.Float, nullable=False)

    done = db.column(db.Enum("Y", "N"))

    created_datetime = db.Column(db.DateTime,
                                 index=False,
                                 unique=False,
                                 nullable=False)

    modified_datetime = db.Column(db.DateTime,
                                  index=False,
                                  unique=False,
                                  nullable=False)
