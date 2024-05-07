from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify

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
    if 'user_id' not in session:

        return redirect(url_for('lform'))

    return render_template('base.html')


@app.route('/logout', methods=['post'])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('lform'))
@app.route('/signup', methods=['post', 'get'])
def rform():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        email = str(request.form.get('email'))
        if username and password and email:
            result = add_user(username=username,password=password,email=email)
            if result is None:
                return jsonify({})
            else:
                return jsonify(result)
        else:
            return jsonify({'error': 'Необходимо заполнить все поля'})

@app.route('/login', methods=['post'])
def lform():
    if request.method == 'POST':
        name = str(request.form.get('name'))
        password = str(request.form.get('password'))
        if name and password:
            user = check_login(name=name,password=password)
            if not user:
                return jsonify({'error': 'Неверный логин или пароль.'})
            else:
                session['user_id'] = user.id
                return jsonify({})
        else:
            return jsonify({'error': 'Необходимо заполнить все поля'})


