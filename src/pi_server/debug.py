# coding: utf-8

import sys
from main import app


if __name__ == '__main__':
	debug = len(sys.argv) > 1 and sys.argv[1] == 'debug'
	app.run(host='0.0.0.0', debug=debug)
