# coding: utf-8

from pi_control.abstract_pi_device import AbstractPiDevice, PinMode, PinValue, DeviceMode, Pull


class PiImitator(AbstractPiDevice):

	def __init__(self, numbers=None):
		AbstractPiDevice.__init__(self)
		self._pins = {}
		self._mode = DeviceMode.Board
		for i in numbers or xrange(1, 41):
			self._pins[i] = Pin()

	def set_mode(self, device_mode):
		self._mode = device_mode

	def get_input(self, number):
		return self._pins[number].value

	def set_output(self, number, value):
		self._pins[number].value = value

	def get_output(self, number):
		return self._pins[number].value

	def get_numbers(self):
		return sorted(self._pins.keys())

	def setup(self, number, mode, pull=Pull.Off, value=None):
		self._pins[number].mode = mode
		self._pins[number].pull = pull
		self._pins[number].value = value

	def cleanup(self):
		numbers = self.get_numbers()
		self._pins.clear()
		for number in numbers:
			self._pins[number] = Pin()


class Pin(object):

	def __init__(self):
		self.value = PinValue.Low
		self.mode = PinMode.Output
		self.pull = Pull.Off
