from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from backend import db


class UserGroup(db.Model):
    """Data model for user_group table."""
    __tablename__ = 'user_group'
    id = db.Column(db.Integer,
                   primary_key=True)
    user_id = db.Column(db.Integer,
                        ForeignKey('user.id', ondelete='CASCADE'), nullable=False, )

    group_id = db.Column(db.Integer, ForeignKey('friend_groups.id', ondelete='CASCADE'), nullable=False)

    access = db.Column(db.Enum("moderator", "participant"), nullable=False)

    created_datetime = db.Column(db.DateTime,
                                 index=False,
                                 unique=False,
                                 nullable=False)

    modified_datetime = db.Column(db.DateTime,
                                  index=False,
                                  unique=False,
                                  nullable=False)
