# coding: utf-8

import time

from pi_control.pi_device import PiDevice, PinValue


def main():
	delay = 0.5
	pi = PiDevice()
	try:
		pi.set_mode_board()
		pins = [11, 13, 15, 16]
		for pin in pins:
			pi.setup_output(pin, value=PinValue.High)
		for pin in pins:
			time.sleep(delay)
			pi.set_output_low(pin)
			time.sleep(delay)
			pi.set_output_high(pin)
		for i in xrange(4):
			time.sleep(delay)
			for pin in pins:
				pi.set_output_low(pin)
			time.sleep(delay)
			for pin in pins:
				pi.set_output_high(pin)
	finally:
		pi.cleanup()


if __name__ == '__main__':
	main()
