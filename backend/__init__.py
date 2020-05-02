from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend import config # noqa


app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from backend import views, models # noqa
