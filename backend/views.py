from backend import app, db


@app.route('/')
def index():
    return "Hello, World!"
