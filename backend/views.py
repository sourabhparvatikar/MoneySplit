from backend import app, db
from backend.models import User
from datetime import datetime

@app.route('/')
def index():
    return "Hello, World!"