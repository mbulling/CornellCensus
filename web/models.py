from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(100))
    rating = db.Column(db.String(10))