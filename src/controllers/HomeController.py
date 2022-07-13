from crypt import methods
from flask import render_template,request,flash
from src import db
from src.models.Procedimento import Procedimento
from src.models.Agenda import Agenda
from src.models.Horario import Horario
from src.models.Cliente import Cliente

def init_app(app):
    @app.route("/")
    def index():
        return render_template("home.html"),200

    @app.route("/agendar", methods=['POST','GET'])
    def agendar():
        procedimentos = Procedimento.query.all()
        horario = Horario.query.all()
        
        if request.method == 'POST':
            agenda = Agenda(request.form['nome'],request.form['telefone'],request.form['procedimento1'],
            request.form['procedimento2'],request.form['procedimento3'],request.form['horario'])
            
            consulta = Agenda.query.filter_by(id_data_hora=agenda.horario).first()
            if consulta:
                flash("Este horário já está agendado, tente outro!")
            else:
                db.session.add(agenda)
                db.session.commit()
                flash("Agendamento realizado com sucesso!")

        return render_template("agendar.html",procedimentos=procedimentos,horario=horario)

    
    @app.route("/login",methods=["GET","POST"])
    def login():
        if request.method == 'POST':

            logar = Cliente(request.form['login'],request.form['senha'])
            login_data = Cliente.query.filter_by(login=logar.login).first()
            senha_data = Cliente.query.filter_by(senha=logar.senha).first()
            if login_data and senha_data:
                flash("Login Efetuado com sucesso!")
            else:
                flash("Nome de usuário incorreto ou inexistente!") 
        return render_template("login.html")

    @app.route('/cadastrar',methods=['GET','POST'])
    def cadastrar():
        # form = CadastrarClienteForm()
        if request.method == 'POST':
            cadastro = Cliente(request.form['nome'],request.form['login'],request.form['senha'],request.form['telefone'])
            login_data = Cliente.query.filter_by(login=cadastro.login).first()
            if login_data:
                flash("Este login já existe, tente outro!")
            else:
                db.session.add(cadastro)
                db.session.commit()
                flash("Cadastro realizado com sucesso!")
            
        return render_template("cadastrar.html")


    @app.route("/sobre")
    def sobre():
        return render_template("sobre.html")



