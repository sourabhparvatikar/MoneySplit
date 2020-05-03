from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from backend import config # noqa
# from backend.api_resources import add_resource


app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
api = Api(app)

migrate = Migrate(app, db)


from backend import views, models # noqa
# add_resource(api)
