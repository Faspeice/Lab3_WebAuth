import bcrypt
from flask import url_for, redirect, flash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.init import db
from app.models import User



def add_user(username,email,password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(username=username,email=email,password = hashed.decode('utf-8'))
    try:
        db.session.add(user)
        db.session.commit()
        return None
    except IntegrityError:
        db.session.rollback()
        return {'error': 'Такой пользователь уже существует'}

def check_login(name,password):
    stmn = select(User).where((User.username == name) | (User.email == name) & (User.password == password))
    result = db.session.execute(stmn)
    user = result.scalar_one_or_none()
    if user and  bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    return None

