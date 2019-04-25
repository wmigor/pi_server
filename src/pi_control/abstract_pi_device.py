# coding: utf-8

from abc import abstractmethod, ABCMeta


class DeviceMode(object):
	Board = 1
	Bcm = 2


class PinMode(object):
	Input = 1
	Output = 2


class PinValue(object):
	Low = 0
	High = 1


class Pull(object):
	Off = 0
	Up = 1
	Down = 2


class AbstractPiDevice(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_numbers(self):
		pass

	@abstractmethod
	def set_mode(self, device_mode):
		pass

	@abstractmethod
	def setup(self, number, mode, pull=Pull.Off, value=None):
		pass

	@abstractmethod
	def get_input(self, number):
		pass

	@abstractmethod
	def set_output(self, number, value):
		pass

	@abstractmethod
	def get_output(self, number):
		pass

	@abstractmethod
	def cleanup(self):
		pass

	def setup_output(self, number, pull=Pull.Off, value=None):
		self.setup(number, PinMode.Output, pull, value)

	def setup_input(self, number, pull=Pull.Off, value=None):
		self.setup(number, PinMode.Input, pull, value)

	def set_mode_board(self):
		self.set_mode(DeviceMode.Board)

	def set_mode_bcm(self):
		self.set_mode(DeviceMode.Board)

	def set_output_high(self, number):
		self.set_output(number, PinValue.High)

	def set_output_low(self, number):
		self.set_output(number, PinValue.Low)
