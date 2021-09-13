from app import db, login_manager, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(86), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = generate_password_hash(password)
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd) 


class Linux(db.Model):

    __tablename__ = 'linux'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    funcao = db.Column(db.String(100), nullable=False)
    comando = db.Column(db.String, nullable=False)
    origem = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, funcao, comando,origem):
        self.nome = nome
        self.funcao = funcao
        self.comando = comando
        self.origem = origem

class Sql(db.Model):

    __tablename__ = 'sql'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    funcao = db.Column(db.String(100), nullable=False)
    comando = db.Column(db.String, nullable=False)
    origem = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, funcao, comando,origem):
        self.nome = nome
        self.funcao = funcao
        self.comando = comando
        self.origem = origem

class Python(db.Model):

    __tablename__ = 'python'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    funcao = db.Column(db.String(100), nullable=False)
    comando = db.Column(db.String, nullable=False)
    origem = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, funcao, comando,origem):
        self.nome = nome
        self.funcao = funcao
        self.comando = comando
        self.origem = origem

class Git(db.Model):

    __tablename__ = 'git'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    funcao = db.Column(db.String(100), nullable=False)
    comando = db.Column(db.String, nullable=False)
    origem = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, funcao, comando,origem):
        self.nome = nome
        self.funcao = funcao
        self.comando = comando
        self.origem = origem



class StartDB():
    def startDB(a):
        if a:
            db.create_all()
            user = User('debug','debug@debug','123')
            db.session.add(user)
            db.session.commit()





    



    
