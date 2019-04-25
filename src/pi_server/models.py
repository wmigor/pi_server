# coding: utf-8

import datetime
from flask_login import UserMixin
from pi_server import db
from peewee import PrimaryKeyField, CharField, FloatField, DateTimeField


class User(db.Model, UserMixin):
	id = PrimaryKeyField()
	name = CharField(unique=True)
	salt = CharField()
	password = CharField()

	def __str__(self):
		return self.name


class Temperature(db.Model):
	date_time = DateTimeField(default=datetime.datetime.now)
	value = FloatField()


class Humidity(db.Model):
	date_time = DateTimeField(default=datetime.datetime.now)
	value = FloatField()
