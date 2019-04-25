# coding: utf-8

from RPi import GPIO

from pi_control.abstract_pi_device import AbstractPiDevice, PinMode, PinValue, DeviceMode, Pull


class PiDevice(AbstractPiDevice):

	def __init__(self, ):
		self._pin_outputs = {}

	def set_mode(self, device_mode):
		pi_device_mode = self.to_pi_device_mode(device_mode)
		GPIO.setmode(pi_device_mode)

	def setup(self, number, mode, pull=Pull.Off, value=None):
		pi_mode = self.to_pi_pin_mode(mode)
		pi_pull = self.to_pi_pull(pull)
		if number in self._pin_outputs:
			del self._pin_outputs[number]
		if value is None:
			GPIO.setup(number, pi_mode, pi_pull)
		else:
			pi_value = self.to_pi_pin_value(value)
			GPIO.setup(number, pi_mode, pi_pull, pi_value)
			if mode == PinMode.Output:
				self._pin_outputs[number] = value

	def get_input(self, number):
		value = GPIO.input(number)
		if value == GPIO.LOW:
			return PinValue.Low
		return PinValue.High

	def set_output(self, number, value):
		pi_value = self.to_pi_pin_value(value)
		GPIO.output(number, pi_value)
		self._pin_outputs[number] = value

	def get_output(self, number):
		return self._pin_outputs.get(number)

	def get_numbers(self):
		return range(1, 41)

	def cleanup(self):
		GPIO.cleanup()
		self._pin_outputs.clear()

	@staticmethod
	def to_pi_device_mode(device_mode):
		if device_mode == DeviceMode.Board:
			return GPIO.BOARD
		if device_mode == DeviceMode.Bcm:
			return GPIO.BCM
		raise ValueError('Device mode %s' % device_mode)

	@staticmethod
	def to_pi_pin_mode(pin_mode):
		if pin_mode == PinMode.Output:
			return GPIO.OUT
		if pin_mode == PinMode.Input:
			return GPIO.IN
		raise ValueError('Pin mode %s' % pin_mode)

	@staticmethod
	def to_pi_pin_value(pin_value):
		if pin_value == PinValue.High:
			return GPIO.HIGH
		if pin_value == PinValue.Low:
			return GPIO.LOW
		raise ValueError('Pin value %s' % pin_value)

	@staticmethod
	def to_pi_pull(pull):
		if pull == Pull.Off:
			return GPIO.PUD_OFF
		if pull == Pull.Up:
			return GPIO.PUD_UP
		if pull == Pull.Down:
			return GPIO.PUD_DOWN
		raise ValueError('Pull %s' % pull)

	@staticmethod
	def to_pin_value(pi_pin_value):
		if pi_pin_value in (1, True, GPIO.HIGH):
			return PinValue.High
		if pi_pin_value in (0, False, GPIO.LOW):
			return PinValue.Low
		raise ValueError('Pin value %s' % pi_pin_value)
