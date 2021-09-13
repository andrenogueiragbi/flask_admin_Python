from flask_admin.contrib import sqla
from app import modals
from flask import render_template, request, url_for, redirect,flash
from flask_admin import Admin
from flask_login import login_user, logout_user, login_required
from app.modals import StartDB,User,Git,Linux,Sql,Python
from app import app, login_manager,db
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import AdminIndexView

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(AdminIndexView._handle_view)


StartDB.startDB(False)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Linux,db.session))
admin.add_view(ModelView(Git,db.session))
admin.add_view(ModelView(Sql,db.session))
admin.add_view(ModelView(Python,db.session))


##LOGIN##
@app.route("/login/", methods=["GET", "POST"])
def login():

    print(request.form.get("password"), request.form.get("email"))

    if request.method == "POST":
        email = request.form.get("email")
        pwd = request.form.get("password")


        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return render_template("login.html", erro=True)

        login_user(user)
        return redirect(url_for("teste"))

    return render_template("login.html")



if __name__== '__main__':
    app.run(debug=True) 