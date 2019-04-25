# coding: utf-8

import logging
import time
import datetime
from redis import Redis
from peewee import SqliteDatabase, Model, DateTimeField, FloatField


db = SqliteDatabase('/home/pi/work/pi_server/src/pi_server/data.db')


class BaseModel(Model):

	class Meta:
		database = db


class Temperature(BaseModel):
	date_time = DateTimeField(default=datetime.datetime.now)
	value = FloatField()


class Humidity(BaseModel):
	date_time = DateTimeField(default=datetime.datetime.now)
	value = FloatField()


def main():
	try:
		logging.root.addHandler(logging.StreamHandler())
		logging.root.setLevel(logging.INFO)
		delay = 5 * 60
		Temperature.create_table(True)
		Humidity.create_table(True)
		redis = Redis()
		while True:
			try:
				temperature = redis.get('AM2303:temperature')
				humidity = redis.get('AM2303:humidity')
				with db.transaction():
					if temperature is not None:
						Temperature.create(value=temperature)
						logging.info('temperature: {}'.format(temperature))
					if humidity is not None:
						Humidity.create(value=humidity)
						logging.info('humidity: {}'.format(humidity))
				time.sleep(delay)
			except Exception, e:
				logging.exception(e)
	except Exception, e:
		logging.exception(e)


if __name__ == '__main__':
	main()
