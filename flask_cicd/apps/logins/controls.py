# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os

from flask import Blueprint, render_template, flash, redirect, request, session

from flask_sqlalchemy  import SQLAlchemy, Pagination
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (login_user, 
                         login_required, logout_user, current_user)

from flask_paginate import Pagination, get_page_args


from flask_cicd.apps.logins.forms.users import LoginForm, RegisterForm

loginbp = Blueprint(
        "loginbp", 
        __name__, 
         static_folder=os.path.join(os.path.dirname(__name__), '../../static'), #apps/homes/static
         template_folder=os.path.join(os.path.dirname(__name__), '../../templates/logins')) #apps/homes/templates

users = list(range(100))

def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]

@loginbp.route("/login", methods=["GET","POST"])
def login():
    from flask_cicd.apps.logins.models.users import User
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                #return redirect(url_for('dashboard'))
                return redirect('/home')
            else:
                flash('Invalid credentials','error')
                return redirect('/login')
            
        return redirect(url_for('signup'))
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('logins.html', form=form)
    
    
    
@loginbp.route('/signup', methods=['GET', 'POST'])
def signup():
    from flask_cicd.apps.logins.models.users import User
    from run import db
    
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@loginbp.route('/users/list')
def users_list():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('users/lists.html',
                           users=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )
