from flask import Blueprint, render_template, flash, redirect, request, session

loginbp = Blueprint(
        "loginbp", 
        __name__, 
        static_folder="static", 
        template_folder="templates"
        )

@loginbp.route("/", methods=["GET","POST"])
def login():

    if "uname" in session:
        return redirect('/home')

    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        passw = request.form['pass']
        uname =  request.form['uname']
        datav = mongo.db.personal_data.find_one({"uname":uname})
        if datav:
            passwv = datav['pass']
            session["uname"] = datav['uname']
            session["phno"]  = datav['phno']
            session["emai"]  = datav['email']
            if(passwv==passw and session["uname"]==uname):
                return redirect('/home')

            else:
                flash('Invalid credentials','error')
                return redirect('/login')
        else:
            flash('Invalid credentials','error')
            return redirect('/login')