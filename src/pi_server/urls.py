# coding: utf-8

from pi_server import views


def setup(app):
	app.add_url_rule('/', None, views.index)
	app.add_url_rule('/login', None, views.Login.as_view('login'))
	app.add_url_rule('/logout', None, views.logout)
	app.add_url_rule('/register', None, views.Register.as_view('register'))
	app.add_url_rule('/relay', None, views.Relay.as_view('relay'))
	app.add_url_rule('/sensors', None, views.sensors)
	app.add_url_rule('/temperature_chart', None, views.temperature_chart)
	app.add_url_rule('/humidity_chart', None, views.humidity_chart)
