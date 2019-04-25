# coding: utf-8

from pi_server import app, api, user_loader, urls, resources


id([user_loader])
urls.setup(app)
resources.setup(api)
