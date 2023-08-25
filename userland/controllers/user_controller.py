from flask import request, jsonify, render_template, redirect, url_for
from flask_cors import cross_origin
from flask_login import logout_user, login_user, current_user, login_required
from werkzeug.security import check_password_hash
from application.core.app_models import BaseResponse
from application.userland.controller import mod_userland
from application.core.utils.user_utils import UserUtils
from application.core.db_models import Users


@mod_userland.route('/', methods=['GET', 'POST'])
def cloud():
    return redirect('/signup')


@mod_userland.route('/sign_up', methods=['POST'])
@cross_origin()
def sign_up():
    email = request.form.get('email')
    password = request.form.get('password')
    response = UserUtils.sign_up_user(email, password)
    return jsonify(response.__dict__)


@mod_userland.route('/sign_in', methods=['POST'])
@cross_origin()
def sign_in():
    response = BaseResponse()
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')
    user = Users.query.filter(Users.email == email).first()
    if not user or not check_password_hash(user.password, password):
        return response.fail()

    login_user(user, remember=remember)
    return jsonify(response.__dict__)


@mod_userland.route('/protected')
def protected():
    isLoggedIn = False
    return render_template('protected.html', isLoggedIn=isLoggedIn)


@mod_userland.route('/logout', methods=['POST'])
@login_required
def logout():
    response = BaseResponse()
    logout_user()
    return response
