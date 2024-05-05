
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from app import app
from app.init import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


def add_user(username,email,password):
    user = User(username=username,email=email,password =password)
    db.session.add(user)
    db.session.commit()