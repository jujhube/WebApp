from flask_sqlalchemy import SQLAlchemy
from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    creator = db.Column(db.Text)
    mutable = db.Column(db.Text)
    date = db.Column(db.Text)