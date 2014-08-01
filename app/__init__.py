from flask import Flask, redirect, url_for, session, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()

lm.init_app(app)
db = SQLAlchemy(app)

lm.login_view = 'login'

from app import views, models