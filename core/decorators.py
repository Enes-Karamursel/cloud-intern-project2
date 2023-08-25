from functools import wraps
from flask import Flask, redirect, url_for, g, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from application.core.db_models import Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/cloud-project'
db = SQLAlchemy(app)


@app.before_request
def check_custom_login_required():
    if request.endpoint != 'sign_in':
        if not g.user:
            return redirect(url_for('sign_in'))


def load_user():
    user_id = session.get('user_id')
    if user_id:
        g.user = Users.query.get(user_id)
    else:
        g.user = None


def custom_login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if g.user:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for('protected'))

    return login_required(wrapped_view)
