from sqlalchemy import  select

from app.init import db
from app.models import User


def add_user(username,email,password):
    user = User(username=username,email=email,password =password)
    db.session.add(user)
    db.session.commit()
def check_login(name,password):
    stmn = select(User).where((User.username == name) | (User.email == name))
    result = db.session.execute(stmn)
    user = result.scalar_one_or_none()
    if user:
        if password == user.password:
            return True
    return False