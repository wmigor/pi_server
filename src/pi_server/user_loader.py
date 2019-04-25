# coding: utf-8

from pi_server import login_manager
from pi_server.services import Services


@login_manager.user_loader
def user_loader(user_id):
	return Services.user.get(int(user_id))
