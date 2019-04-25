# coding: utf-8

import logging
import time
from redis import Redis
from pi_control.sensors.dht import DthSensor


def main():
	try:
		logging.root.addHandler(logging.StreamHandler())
		logging.root.setLevel(logging.INFO)
		sensor_type = DthSensor.AM2302
		pin = 24
		delay = 10
		sensor = DthSensor(sensor_type, pin)
		redis = Redis()
		expire = delay * 2
		while True:
			try:
				data = sensor.read()
				redis.set('AM2303:temperature', data['temperature'], ex=expire)
				redis.set('AM2303:humidity', data['humidity'], ex=expire)
				logging.info('temperature: {}'.format(data['temperature']))
				logging.info('humidity: {}'.format(data['humidity']))
				time.sleep(delay)
			except Exception, e:
				logging.exception(e)
	except Exception, e:
		logging.exception(e)


if __name__ == '__main__':
	main()
