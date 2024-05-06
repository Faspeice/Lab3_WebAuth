from flask import Flask, render_template, request, redirect, url_for, flash

from app.crud import add_user, check_login
from app.init import app


@app.route('/signup')
def rpage():
    return render_template("reg_page.html")
@app.route('/login')
def lpage():
    return render_template("log_page.html")
@app.route('/base')
def base():
    return render_template("base.html")


@app.route('/signup', methods=['post', 'get'])
def rform():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        email = str(request.form.get('email'))
        if username and password and email:
            add_user(username=username,password=password,email=email)
            return redirect(url_for('lform'))
        return render_template('reg_page.html')

@app.route('/login', methods=['post'])
def lform():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        password = str(request.form.get('password'))
        if check_login(name=name,password=password) == False:
            flash('Неверный логин или пароль.')
            return render_template('log_page.html')
        return redirect(url_for('base'))


