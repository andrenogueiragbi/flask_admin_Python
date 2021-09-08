from app import modals
from flask import Flask
from flask_admin import Admin
from app.modals import StartDB,User,Git,Linux,Sql,Python
from app import app, login_manager,db
from flask_admin.contrib.sqla import ModelView


admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Linux,db.session))
admin.add_view(ModelView(Git,db.session))
admin.add_view(ModelView(Sql,db.session))
admin.add_view(ModelView(Python,db.session))


StartDB.startDB(True)

if __name__== '__main__':
    app.run(debug=True) 