# coding: utf-8

import unittest

from pi_control.pi_imitator import PinMode, PinValue
from pi_control.pi_imitator import PiImitator


class TestPiImitator(unittest.TestCase):
	pi = PiImitator()

	def test_get_numbers(self):
		self.assertEqual(range(1, 41), PiImitator().get_numbers())

	def test_value(self):
		pi = PiImitator()
		pi.set_output(1, PinValue.High)
		self.assertEqual(PinValue.High, pi.get_output(1))
		pi.set_output(1, PinValue.Low)
		self.assertEqual(PinValue.Low, pi.get_output(1))

	def test_setup(self):
		pi = PiImitator()
		pi.setup(1, PinMode.Input)

	def test_setup_output_high(self):
		self.pi.setup_output(11, value=PinValue.High)
		self.assertEqual(PinValue.High, self.pi.get_output(11))

	def test_setup_output_low(self):
		self.pi.setup_output(11, value=PinValue.Low)
		self.assertEqual(PinValue.Low, self.pi.get_output(11))

	def test_setup_output(self):
		self.pi.setup_output(11)
		self.assertEqual(None, self.pi.get_output(11))

	def test_set_output_low(self):
		self.pi.setup_output(11)
		self.pi.set_output_low(11)
		self.assertEqual(PinValue.Low, self.pi.get_output(11))

	def test_set_output_high(self):
		self.pi.setup_output(11)
		self.pi.set_output_high(11)
		self.assertEqual(PinValue.High, self.pi.get_output(11))

	def setUp(self):
		self.pi = PiImitator()
		self.pi.set_mode_board()

	def tearDown(self):
		self.pi.cleanup()


if __name__ == '__main__':
	unittest.main()
