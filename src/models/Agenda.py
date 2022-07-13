from src import db

class Agenda(db.Model):
    __tablename__ = "agenda"
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(200),nullable=False)
    telefone = db.Column(db.String(20),nullable=False)
    procedimento1 = db.Column(db.String(200),db.ForeignKey('procedimento.id'))
    procedimento2 = db.Column(db.String(200),db.ForeignKey('procedimento.id'))
    procedimento3 = db.Column(db.String(200),db.ForeignKey('procedimento.id'))
    id_data_hora = db.Column(db.Integer,db.ForeignKey('horario.id'),nullable=False)
    
    

    def __init__(self,nome,telefone,procedimento1,procedimento2,procedimento3,id_data_hora):
        self.nome = nome
        self.telefone = telefone
        self.procedimento1 = procedimento1
        self.procedimento2 = procedimento2
        self.procedimento3 = procedimento3
        self.id_data_hora = id_data_hora
