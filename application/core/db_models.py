#!/usr/bin/python3
from application import db, login_manager
from flask_login import UserMixin


class DomainInfo(db.Model):
    __tablename__ = 'domain_info'
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String)
    status_code = db.Column(db.Integer)
    title = db.Column(db.String)
    content = db.Column(db.String)
    is_it_key = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean, default=True)
    extra_info = db.Column(db.JSON)


class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True)
    password = db.Column(db.String)


@login_manager.user_loader
def load_user(user_id):
    print(123)
    return Users.query.get(int(user_id))


