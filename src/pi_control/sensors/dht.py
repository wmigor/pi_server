# coding: utf-8

try:
	import Adafruit_DHT
except ImportError:
	import random


	class Adafruit_DHT(object):
		DHT11 = '11'
		DHT22 = '22'
		AM2302 = '2302'

		@staticmethod
		def read_retry(type_, pin):
			return random.random(), random.random()


class DthSensor(object):
	DTH11 = Adafruit_DHT.DHT11
	DTH22 = Adafruit_DHT.DHT22
	AM2302 = Adafruit_DHT.AM2302

	def __init__(self, type_, pin):
		if type_ not in (self.DTH11, self.DTH22, self.AM2302):
			raise TypeError('Unsupported type {}'.format(type_))
		self.pin = pin
		self.type = type_

	def read(self):
		humidity, temperature = Adafruit_DHT.read_retry(self.type, self.pin)
		return dict(humidity=humidity, temperature=temperature)
