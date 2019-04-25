# coding: utf-8
import json
import logging
from socket import socket, AF_INET, SOCK_DGRAM

UdpPort = 54545
Data = {
	"protocol": 1,
	"name": "Raspberry",
	"type": "Raspberry"
}
Text = json.dumps(Data)


def main():
	try:
		logging.root.addHandler(logging.StreamHandler())
		logging.root.setLevel(logging.INFO)
		server = socket(AF_INET, SOCK_DGRAM)
		server.bind(('0.0.0.0', UdpPort))
		while True:
			try:
				message, address = server.recvfrom(1024)
				logging.info('message "{}" from "{}"'.format(message, address))
				if message != '?':
					continue
				server.sendto(Text, address)
			except Exception, e:
				logging.exception(e)
	except Exception, e:
		logging.exception(e)


if __name__ == '__main__':
	main()
