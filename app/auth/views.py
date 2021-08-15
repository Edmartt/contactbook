import functools

from flask import render_template, request, redirect, url_for, flash, session, \
        g

from werkzeug.security import check_password_hash
from . import auth
from ..users import User


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    g.user = None if user_id is None else User.check_user_by_id(user_id)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('You must log in')
            return redirect(url_for('auth.login', next=request.url_rule))

        return view(**kwargs)
    return wrapped_view


@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Esta vista gestiona el acceso de cualquier usuario a la aplicación.
    Verifica si la solicitud es de un método POST y asigna los valores
    del formulario (username, y passsword) a dos variables
    los cuales se usan para crear un objeto
    de la clase User y usar el método log_user de dicha clase y validar
    los datos ingresados para posteriormente permitir el acceso.
    '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, password)
        user_log = user.log_user()

        if user_log is not None \
                and check_password_hash(user_log[3], password):
            session.clear()
            session['user_id'] = user_log[0]
            next = request.args.get('next')

            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)

        flash('Wrong username or password')
    return render_template('auth/login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username,password, email)

        if user.check_user_by_username(username):
            flash('User already exists')
        else:
            user.reg_user()
            flash('User registered')
            return redirect(url_for('auth.login'))

    return render_template('auth/signup.html')


@login_required
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
