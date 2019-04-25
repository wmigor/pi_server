# coding: utf-8

from pi_server import models


def setup(api):
	api.register(models.Temperature)
	api.register(models.Humidity)
	api.setup()
