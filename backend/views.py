from backend import app, api
from flask_restful import Resource

class HelloWorld(Resource):

    def get(self):
        return "Hello, World!"

