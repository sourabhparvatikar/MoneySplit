from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:MoneySplit123@localhost/moneysplit'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from backend import views, models
    
# if __name__ == "__main__":
#     db.init_app(app)
#     app.run(debug=True)
