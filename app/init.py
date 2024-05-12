import os

from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)
