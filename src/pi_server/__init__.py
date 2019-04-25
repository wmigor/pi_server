# coding: utf-8

from flask import Flask
from flask_peewee.db import Database
from flask_peewee.rest import RestAPI
from flask_login import LoginManager


app = Flask('pi_server')
app.secret_key = open('secret_key.txt').read()
app.config['DATABASE'] = {
	'name': 'data.db',
	'engine': 'peewee.SqliteDatabase'
}
db = Database(app)
api = RestAPI(app)
login_manager = LoginManager(app)
