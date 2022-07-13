from src import db

class Horario(db.Model):
    __tablename__ = "horario"
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.Date,nullable=False)
    hora = db.Column(db.DateTime,nullable=False)
    agenda= db.relationship('Agenda',backref='horario',lazy=True)

    def __init__(self,data,hora):
        self.data = data
        self.hora = hora
