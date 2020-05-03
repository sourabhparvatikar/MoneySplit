from backend import db
from backend.models import Transactions


def add_to_transactions(data):
    # import pdb;pdb.set_trace()
    trans = Transactions(**data)
    db.session.add(trans)
    db.session.commit()


def update_row_in_transactions(data):
    row = db.session.query(Transactions).get(id)
    row.valid = "N"
