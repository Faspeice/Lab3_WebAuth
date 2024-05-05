from flask import Flask, render_template, request

from app.crud import add_user, check_login
from app.init import app


@app.route('/signup')
def rpage():
    return render_template("reg_page.html")
@app.route('/login')
def lpage():
    return render_template("log_page.html")


@app.route('/signup', methods=['post', 'get'])
def rform():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        email = str(request.form.get('email'))
        add_user(username=username,password=password,email=email)
    return render_template('reg_page.html', ans="Great")

@app.route('/login', methods=['post', 'get'])
def lform():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        password = str(request.form.get('password'))
        if check_login(name=name,password=password) == True:
            return render_template('log_page.html', ans="Great")
        return render_template('log_page.html', ans="noGreat")


