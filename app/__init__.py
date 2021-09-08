from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
import pymysql
pymysql.install_as_MySQLdb()




app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)
db = SQLAlchemy(app)

