from src import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(200),nullable=False)
    login = db.Column(db.String(100),nullable=False,unique=True)
    senha = db.Column(db.String(50),nullable=False)
    telefone = db.Column(db.String(20),nullable=False)
    
    def __init__(self,nome,login,senha,telefone):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.telefone = telefone

    def __repr__(self):
        return '<User %r>' % self.nome
