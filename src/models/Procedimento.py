from src import db

class Procedimento(db.Model):
    __tablename__ = "procedimento"
    id = db.Column(db.Integer,primary_key=True)
    procedimento = db.Column(db.String(200),nullable=False)
    #agenda= db.relationship('Agenda',backref='procedimento',lazy=True)
    

    def __init__(self,procedimento):
        self.procedimento = procedimento

    def __repr__(self):
        return '<Procedimento %r>' % self.procedimento