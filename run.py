
from flask import Flask, render_template, request, flash, redirect, session

from flask_cicd.apps.homes.controls import homebp
from flask_cicd.apps.logins.controls import loginbp


# Set App
app = Flask(__name__)

app.secret_key = "$HERBEWscKKwwqy#@!"

app.register_blueprint(homebp, url_prefix="/home")
app.register_blueprint(loginbp, url_prefix="/login")

@app.route("/")
def main():
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)