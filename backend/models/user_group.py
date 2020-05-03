from datetime import datetime
from sqlalchemy import ForeignKey

from backend import db


def default_for_modified_datetime(context):
    return context.get_current_parameters()['created_datetime']


class UserGroup(db.Model):
    """Data model for user_group table."""
    __tablename__ = 'user_group'
    id = db.Column(db.Integer,
                   primary_key=True)
    user_id = db.Column(db.Integer,
                        ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=False)

    group_id = db.Column(db.Integer,
                         ForeignKey('friend_groups.id', ondelete='CASCADE'),
                         nullable=False)

    access = db.Column(db.Enum("moderator", "participant"), nullable=False)

    created_datetime = db.Column(db.DateTime, nullable=False,
                                 default=datetime.now())
    modified_datetime = db.Column(db.DateTime, nullable=False,
                                  default=default_for_modified_datetime)

    def save(self):
        db.session.add(self)
        db.session.commit()
