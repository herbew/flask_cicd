# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from flask import Blueprint, render_template, redirect, session
from flask_login import logout_user, current_user


homebp = Blueprint(
    "homebp",
    __name__, 
    static_folder=os.path.join(os.path.dirname(__name__), '../../static'), #apps/homes/static
    template_folder=os.path.join(os.path.dirname(__name__), '../../templates/homes')) #apps/homes/templates



@homebp.route("/home")
def home():
    return render_template('homes.html', name=current_user.username)

    

@homebp.route("/logout")
def logout():
    logout_user()
    return redirect('/login')