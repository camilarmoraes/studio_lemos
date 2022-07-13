from flask import render_template,request,url_for,redirect,flash
from src import db
from src.models.Cliente import *
from src import *
from flask import Flask, render_template,request,url_for,redirect,flash,abort
from flask_login import LoginManager,login_required,login_user,logout_user,current_user
from flask_sqlalchemy import Model, SQLAlchemy

def init_app(app):
    pass