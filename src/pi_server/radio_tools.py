# coding: utf-8

import logging
import json
import requests
from flask import request


def get_radio_host():
	return 'http://%s:8000' % request.host.split(':')[0]


def get_radio_info():
	try:
		host = get_radio_host() + '/status-json.xsl'
		data = requests.get(host).content
		return json.loads(data)
	except Exception, e:
		logging.exception(e)
		return {}
