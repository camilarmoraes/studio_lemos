# Further config access https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

from flask import Flask, render_template, jsonify, make_response,session,request
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginMangager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config["SECRECT_KEY"] = 'secret-muito-secreto'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://studio:studio123@172.21.0.2/studio_lemos'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = "cosmo"
    admin = Admin(app,name="Studio Lemos",template_mode="bootstrap3")
    db.init_app(app)
    
    # login_manager.init_app(app)


    from src.models import Admin as admintrator
    admintrator.init_app(admin)
    
    from src.controllers import HomeController,AdminController, model
    HomeController.init_app(app)
    AdminController.init_app(app)
    model.init_app(app)
    return app
