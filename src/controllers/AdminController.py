from flask import render_template,request,flash,redirect,url_for
from src import db
from src.models.Horario import Horario
from src.models.Procedimento import Procedimento
from src.models.Agenda import Agenda
from src.models.Cliente import Cliente

def init_app(app):

    @app.route("/admin/criar_horario",methods=["GET","POST"])
    def criar_horario():
        if request.method == 'POST':
            horario = Horario(request.form['data'],request.form['hora'])
            dado_data = Horario.query.filter_by(data=horario.data).first()
            dado_hora = Horario.query.filter_by(hora=horario.hora).first()

            if dado_data and dado_hora:
                flash("Esta data e hora de atendimento já existe!")
            else:
                db.session.add(horario)
                db.session.commit()
                flash("Horário de agendamento cadastrado com sucesso!")
        return render_template("/admin/criar_horario.html")



    @app.route("/admin/criar_procedimento",methods=['POST','GET'])
    def criar_procedimento():
        error = None
        if request.method == "POST":
            proced = Procedimento(request.form['procedimento'])
            dado = Procedimento.query.filter_by(procedimento=proced.procedimento).first()
            if dado:
                flash('Este procedimento já existe')
            else:
                db.session.add(proced)
                db.session.commit()
                flash('Procedimento criado com Sucesso!')
        return render_template("/admin/criar_procedimento.html",error=error)


    # Questao de Deletar registros

    @app.route('/admin/delete_procedimento/<int:id>')
    def delete_procedimento(id):
        del_procedimento = Procedimento.query.get(id)
        db.session.delete(del_procedimento)
        db.session.commit()
        return redirect(url_for('listar_procedimento'))

    @app.route('/admin/delete_agenda/<int:id>')
    def delete_agenda(id):
        del_agenda = Agenda.query.get(id)
        db.session.delete(del_agenda)
        db.session.commit()
        return redirect(url_for('listar_agenda'))

    @app.route('/admin/delete_horario/<int:id>')
    def delete_horario(id):
        del_horario = Horario.query.get(id)
        db.session.delete(del_horario)
        db.session.commit()
        return redirect(url_for('listar_horario'))

    @app.route('/admin/delete_cliente/<int:id>')
    def delete_cliente(id):
        del_cliente = Cliente.query.get(id)
        db.session.delete(del_cliente)
        db.session.commit()
        return redirect(url_for('listar_cliente'))


    #Para editar os registros

    @app.route("/admin/edit_agenda/<int:id>",methods=['GET','POST'])
    def reagendar(id):
        agenda = Agenda.query.get(id)
        procedimentos = Procedimento.query.all()
        horario = Horario.query.all()

        if request.method == 'POST':
            agenda.nome = request.form['nome']
            agenda.telefone = request.form['telefone']
            agenda.procedimento1 = request.form['procedimento1']
            agenda.procedimento2 = request.form['procedimento2']
            agenda.procedimento3 = request.form['procedimento3']
            agenda.id_data_hora = request.form['horario']
            
            db.session.commit()

        return render_template("/admin/edit_agenda.html",agenda=agenda,procedimentos=procedimentos,horario=horario)

    @app.route("/admin/edit_cliente/<int:id>",methods=['GET','POST'])
    def edit_cliente(id):
        cliente = Cliente.query.get(id)

        if request.method == 'POST':
            cliente.nome = request.form['nome']
            cliente.login = request.form['login']
            cliente.telefone = request.form['telefone']
            db.session.commit()

        return render_template("/admin/edit_cliente.html",cliente=cliente)

    # @app.route("/admin/edit_horario/<int:id>",methods=['GET','POST'])
    # def edit_horario(id):
    #     horario = Horario.query.get(id)
    #     return render_template("")

    @app.route("/admin/edit_procedimento/<int:id>",methods=['GET','POST'])
    def edit_procedimento(id):
        procedimento = Procedimento.query.get(id)
        if request.method == 'POST':
            procedimento.procedimento = request.form['procedimento']

            db.session.commit()
        return render_template("/admin/edit_procedimento.html",procedimento=procedimento)
