# from src import db

# class Admin(db.Model):
#     __tablename__ = "admin"
#     id = db.Column(db.Integer,primary_key=True)
#     login = db.Column(db.String(40),nullable=False)
#     senha = db.Column(db.String(20),nullable=False)

#     def __init__(self,login,senha):
#         self.login = login
#         self.senha = senha

from src.models.Cliente import Cliente
from src.models.Procedimento import Procedimento
from src.models.Agenda import Agenda
from src.models.Horario import Horario

from flask_admin.contrib.sqla import ModelView
#from flask.ext.admin import BaseView,expose
from src import db

class ClienteView(ModelView):
    list_template = 'listar_cliente.html'
    create_template = 'cadastrar.html'
    

class ProcedimentoView(ModelView):
    list_template = 'listar_procedimento.html'
    create_template= 'criar_procedimento.html'

class AgendaView(ModelView):
    list_template = 'listar_agenda.html'
    create_template = 'agendar.html'
    edit_template = 'reagendar.html'

class HorarioView(ModelView):
    list_template = 'listar_horario.html'
    create_template = 'criar_horario.html'



def init_app(admin):
    admin.add_view(ClienteView(Cliente,db.session))
    admin.add_view(ProcedimentoView(Procedimento,db.session))
    admin.add_view(AgendaView(Agenda,db.session))
    admin.add_view(HorarioView(Horario,db.session))

