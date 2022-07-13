import pytest
from src import create_app,db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" #banco de dados em memoria
    app.config["WTF_CSRF_ENABLED"] = False
    context = app.app_context()
    context.push()

    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()

    context.pop()

def test_se_a_pagina_de_usuarios_restorna_status_codes_200(client):
    response = client.get("/")
    assert response.status_code == 200 #Pagina esta online

def test_se_link_agendar_existe(client):
    response = client.get("/")
    assert "Agendar" in response.get_data(as_text=True)

def test_se_link_cadastrar_existe(client):
    response = client.get("/")
    assert "Cadastrar" in response.get_data(as_text=True)

def test_se_link_login_existe(client):
    response = client.get("/")
    assert "Login" in response.get_data(as_text=True)

def test_se_link_sobre_existe(client):
    response = client.get("/")
    assert "Sobre" in response.get_data(as_text=True)
    
def test_cadastrando_cliente(client):
    data = {
        "nome": "Camila",
        "login": "camilinha",
        "telefone": "99999999",
        "senha": "123"
    }
    response = client.post("/cadastrar",data=data, follow_redirects=True)
    assert "Camila" in response.get_data(as_text=True)


def test_agendar_procedimento(client):
    data = {
        "nome": "Joao",
        "telefone": "7568291273",
        "procedimento1":3,
        "procedimento2":1,
        "procedimento3":2,
        "horario":1
    }
    response = client.post("/agendar",data=data,follow_redirects=True)
    assert "Joao" in response.get_data(as_text=True)