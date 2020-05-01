from backend import db
class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'user'
    id = db.Column(db.Integer,
                   primary_key=True)
    first_name = db.Column(db.String(64),
                         index=False,
                         nullable=False,
                         unique = False)
    last_name = db.Column(db.String(64),
                         index=False,
                         nullable=False,
                         unique = False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    password_hash = db.Column(db.String(128),
                    index=False,
                    unique=False,
                    nullable=False
                    )
    created_datetime = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    modified_datetime = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
