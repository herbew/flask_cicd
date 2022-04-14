
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask_login import UserMixin

from run import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #addresses = db.relationship('Address', backref='person', lazy=True)
    addresses = db.relationship('Address', lazy='select',
        backref=db.backref('person', lazy='joined'))

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)