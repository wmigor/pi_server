# coding: utf-8

from redis import Redis
from flask import render_template, redirect, url_for, request
from flask.views import MethodView
from flask_login import current_user, login_user, logout_user
from pi_server import radio_tools
from pi_server.services import Services
from pi_control.abstract_pi_device import PinValue

pi = None


def init_device():
	global pi
	if pi is not None:
		return
	try:
		from pi_control.pi_device import PiDevice
	except Exception, e:
		print e
		from pi_control.pi_imitator import PiImitator as PiDevice

	pi = PiDevice()
	pi.set_mode_board()
	pi.setup_output(11, value=PinValue.High)
	pi.setup_output(13, value=PinValue.High)
	pi.setup_output(15, value=PinValue.High)
	pi.setup_output(16, value=PinValue.High)


def index():
	user = current_user
	radio_info = radio_tools.get_radio_info()
	radio_stations = radio_info.get('icestats', {}).get('source', [])
	if isinstance(radio_stations, dict):
		radio_stations = [radio_stations]
	context = dict(user=user, radio_host=radio_tools.get_radio_host(), radio_stations=radio_stations)
	return render_template('index.html', **context)


class Login(MethodView):

	@staticmethod
	def get():
		return render_template('login.html')

	@staticmethod
	def post():
		name = request.form.get('name')
		password = request.form.get('password')
		user = Services.user.get_by_name(name)
		if not user or not Services.user.is_valid_password(user, password):
			return redirect(url_for('login'))
		login_user(user)
		return redirect(url_for('index'))


class Relay(MethodView):

	@staticmethod
	def get():
		context = {
			'user': current_user,
			'pins': []}
		for number in [11, 13, 15, 16]:
			pin = {
				'number': number,
				'value': pi.get_output(number)}
			context['pins'].append(pin)
		return render_template('relay.html', **context)

	@staticmethod
	def post():
		value = int(request.form.get('value'))
		number = int(request.form.get('number'))
		if value == PinValue.High:
			pi.set_output_high(number)
		else:
			pi.set_output_low(number)
		return str(value)


def logout():
	logout_user()
	return redirect(url_for('index'))


class Register(MethodView):

	@staticmethod
	def get():
		if current_user.is_anonymous:
			return redirect(url_for('index'))
		return render_template('register.html')

	@staticmethod
	def post():
		if current_user.is_anonymous:
			return redirect(url_for('index'))
		name = request.form.get('name')
		password = request.form.get('password')
		user = Services.user.get_by_name(name)
		if user:
			return redirect(url_for('register'))
		Services.user.register(name, password)
		return redirect(url_for('index'))


def sensors():
	redis = Redis()
	temperature = redis.get('AM2303:temperature')
	humidity = redis.get('AM2303:humidity')
	context = {
		'sensors': [
			{
				'name': u'Температура',
				'value': round(float(temperature), 2) if temperature else u'?',
				'measure': u'°',
				'chart_url': url_for('temperature_chart')
			},
			{
				'name': u'Влажность',
				'value': round(float(humidity), 2) if humidity else u'?',
				'measure': '%',
				'chart_url': url_for('humidity_chart')
			}
		],
		'user': current_user
	}
	return render_template('sensors.html', **context)


def temperature_chart():
	context = {
		'name': u'Температура',
		'user': current_user,
		'items': Services().temperature.get_last()
	}
	return render_template('statistic.html', **context)


def humidity_chart():
	context = {
		'name': u'Влажность',
		'user': current_user,
		'items': Services().humidity.get_last()
	}
	return render_template('statistic.html', **context)
