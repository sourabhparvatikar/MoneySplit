from flask_restful import Resource
from flask import request
from backend import db
from backend.models import User
from backend import api
from backend.modules.expenses import add_to_transactions


class HelloWorld(Resource):

    def post(self):
        # data = request.json
        # import pdb;pdb.set_trace()
        # u = User(first_name="Guru", last_name="pad", email="dsafsadf", password_hash="sdf")
        # db.session.add(u)
        # db.session.commit()
        data = {"sender":1, "receiver":2, "amount":20, "done":"N", "group":1, "valid":"Y"}
        add_to_transactions(data)
        return "Hello, World!"

api.add_resource(HelloWorld, '/')