from flask import Blueprint, render_template, flash, redirect, request, session

from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, UserMixin, login_user, 
                         login_required, logout_user, current_user)

from flask_cicd.apps.logins.models.users import User
from flask_cicd.apps.logins.forms.users import LoginForm, RegisterForm

from run import app 

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

loginbp = Blueprint(
        "loginbp", 
        __name__, 
        static_folder="static", 
        template_folder="templates"
        )

@loginbp.route("/", methods=["GET","POST"])
def login():
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

    return render_template('login.html', form=form)
    
    
    
@loginbp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)
