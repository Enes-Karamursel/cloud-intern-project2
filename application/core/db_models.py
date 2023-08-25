#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2023 Sarp Cyber Security - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential


from application import db

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer(), primary_key=True)
    test = db.Column(db.String())

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

