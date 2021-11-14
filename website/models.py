'''
models.py
Creates the database models in SQLAlchemy
'''
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Post(db.Model): # Every entry a user posts is a Post table
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(32768))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin): # Every successful registered user is saved as a User in the User table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    posts = db.relationship('Post')