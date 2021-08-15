from flask import jsonify, redirect, url_for, render_template
from app.auth.views import login_required
from . import main


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/gente')
@login_required
def show_gente():
    nombres = ["Maria", "Jose"]
    return jsonify(nombres)
