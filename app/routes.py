from flask import Blueprint, session, abort, request, url_for, redirect, render_template

routes_app = Blueprint('routes', __name__)

@routes_app.route('/')
@routes_app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)