
from flask import Flask, render_template, request, flash, redirect, session
from flask_sqlalchemy  import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from flask_script import Manager, Command, Shell

def shell_context():
    import os, sys
    return dict(app=app, os=os, sys=sys)

manager.add_command("shell", Shell(make_context=shell_context))
                         
from flask_cicd.apps.homes.controls import homebp
from flask_cicd.apps.logins.controls import loginbp


# Set App
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db_flask_cicd.db'
app.config['SECRET_KEY'] = "$HERBEWscKKwwqy#@!"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

app.register_blueprint(homebp, url_prefix="/home")
app.register_blueprint(loginbp, url_prefix="/login")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from flask_cicd.apps.logins.models.users import User
    return User.query.get(int(user_id))

@app.route("/")
def main():
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)