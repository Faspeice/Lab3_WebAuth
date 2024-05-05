from flask import Flask, render_template, request

from app.init import app
from app.models import add_user


@app.route('/')
def index():
    return render_template("reg_page.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        email = str(request.form.get('email'))
        add_user(username=username,password=password,email=email)
    return render_template('reg_page.html', ans="Great")


