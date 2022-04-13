# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
from flask import Blueprint, render_template, redirect, session


homebp = Blueprint(
    "homebp",
    __name__, 
    static_folder=os.path.join(os.path.dirname(__name__), '../../static'), #apps/homes/static
    template_folder=os.path.join(os.path.dirname(__name__), '../../templates/homes')) #apps/homes/templates



@homebp.route("/home")
def home():
    if "uname" in session:
        uname = session["uname"]
        phno  =  session["phno"]
        emai  =  session["emai"]
        return render_template('homes.html',uname=uname,phno=phno,emai=emai)
    else:
        return redirect('/login')

@homebp.route("/logout")
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/login')