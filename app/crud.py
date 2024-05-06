from flask import url_for, redirect, flash
from sqlalchemy import  select
from sqlalchemy.exc import IntegrityError

from app.init import db
from app.models import User


def add_user(username,email,password):
    user = User(username=username,email=email,password =password)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash('Такой пользователь уже существует.')
def check_login(name,password):
    stmn = select(User).where((User.username == name) | (User.email == name) & (User.password == password))
    result = db.session.execute(stmn)
    user = result.scalar_one_or_none()
    if user and user.password == password:
        return user
    return None