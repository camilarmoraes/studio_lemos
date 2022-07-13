from src import db
from flask import render_template
from src.models.Cliente import Cliente
from src.models.Procedimento import Procedimento
from src.models.Horario import Horario
from src.models.Agenda import Agenda

def init_app(app):
    @app.route("/admin/listar_procedimento")
    def listar_procedimento():
        procedimento = Procedimento.query.all()
        return render_template('/admin/listar_procedimento.html',procedimento=procedimento)

    @app.route("/admin/listar_cliente")
    def listar_cliente():
        cliente = Cliente.query.all()
        return render_template('/admin/listar_cliente.html',cliente=cliente)
    
    @app.route("/admin/listar_horario")
    def listar_horario():
        horario = Horario.query.all()
        return render_template('/admin/listar_horario.html',horario=horario)

    @app.route("/admin/listar_agenda")
    def listar_agenda():
        agenda = Agenda.query.all()
        horario = Horario.query.all()
        procedimento = Procedimento.query.all()
        return render_template('/admin/listar_agenda.html',agenda=agenda,horario=horario,
        procedimento=procedimento)

