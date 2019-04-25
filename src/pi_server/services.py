# coding: utf-8

import os
import hashlib

from datetime import datetime, timedelta
from pi_server import models


class Service(object):
	model = None

	def get(self, id_):
		return self.model.select().where(self.model.id == id_).get()

	def get_all(self):
		return list(self.model.select())


class UserService(Service):
	model = models.User

	def get_by_name(self, name):
		user = self.model.select().where(self.model.name == name).first()
		return user

	def register(self, name, password):
		user = models.User()
		user.name = name
		user.salt = self.generate_salt()
		user.password = hashlib.md5(password).hexdigest()
		user.save()

	@staticmethod
	def generate_salt():
		return hashlib.md5(os.urandom(100)).hexdigest()

	@staticmethod
	def is_valid_password(user, password):
		user_hash = hashlib.md5(user.salt + user.password).hexdigest()
		password_hash = hashlib.md5(user.salt + hashlib.md5(password).hexdigest()).hexdigest()
		return user_hash == password_hash


class TemperatureService(Service):
	model = models.Temperature

	def get_all_sorted(self):
		return self.model.select().order_by(self.model.date_time)

	def get_last(self, hours=24):
		last_days = datetime.now() - timedelta(hours=hours)
		return self.model.select().where(self.model.date_time > last_days).order_by(self.model.date_time)


class HumidityService(Service):
	model = models.Humidity

	def get_all_sorted(self):
		return self.model.select().order_by(self.model.date_time)

	def get_last(self, hours=24):
		last_days = datetime.now() - timedelta(hours=hours)
		return self.model.select().where(self.model.date_time > last_days).order_by(self.model.date_time)


class Services(object):
	user = UserService()
	temperature = TemperatureService()
	humidity = HumidityService()
