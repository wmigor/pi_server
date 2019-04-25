# coding: utf-8

import unittest

try:
	from RPi import GPIO
	from pi_control.pi_device import PiDevice
	from pi_control.abstract_pi_device import PinMode, PinValue, DeviceMode, Pull
	is_raspberry = True
except RuntimeError:
	is_raspberry = False


if is_raspberry:
	class TestPiDevice(unittest.TestCase):
		pi = PiDevice()

		def test_get_numbers(self):
			self.assertEqual(range(1, 41), PiDevice().get_numbers())

		def test_to_pi_device_mode(self):
			self.assertEqual(GPIO.BOARD, PiDevice.to_pi_device_mode(DeviceMode.Board))
			self.assertEqual(GPIO.BCM, PiDevice.to_pi_device_mode(DeviceMode.Bcm))
			with self.assertRaises(ValueError):
				PiDevice.to_pi_device_mode('NO EXISTS')

		def test_to_pi_pin_mode(self):
			self.assertEqual(GPIO.OUT, PiDevice.to_pi_pin_mode(PinMode.Output))
			self.assertEqual(GPIO.IN, PiDevice.to_pi_pin_mode(PinMode.Input))
			with self.assertRaises(ValueError):
				PiDevice.to_pi_pin_mode('NO EXISTS')

		def test_to_pi_pin_value(self):
			self.assertEqual(GPIO.LOW, PiDevice.to_pi_pin_value(PinValue.Low))
			self.assertEqual(GPIO.HIGH, PiDevice.to_pi_pin_value(PinValue.High))
			with self.assertRaises(ValueError):
				PiDevice.to_pi_pin_value('NO EXISTS')

		def test_to_pi_pull(self):
			self.assertEqual(GPIO.PUD_OFF, PiDevice.to_pi_pull(Pull.Off))
			self.assertEqual(GPIO.PUD_UP, PiDevice.to_pi_pull(Pull.Up))
			self.assertEqual(GPIO.PUD_DOWN, PiDevice.to_pi_pull(Pull.Down))
			with self.assertRaises(ValueError):
				PiDevice.to_pi_pull('NO EXISTS')

		def test_to_pin_value(self):
			self.assertEqual(PinValue.High, PiDevice.to_pin_value(1))
			self.assertEqual(PinValue.High, PiDevice.to_pin_value(True))
			self.assertEqual(PinValue.High, PiDevice.to_pin_value(GPIO.HIGH))
			self.assertEqual(PinValue.Low, PiDevice.to_pin_value(0))
			self.assertEqual(PinValue.Low, PiDevice.to_pin_value(False))
			self.assertEqual(PinValue.Low, PiDevice.to_pin_value(GPIO.LOW))
			with self.assertRaises(ValueError):
				PiDevice.to_pin_value('NO EXISTS')

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
			self.pi = PiDevice()
			self.pi.set_mode_board()

		def tearDown(self):
			self.pi.cleanup()


if __name__ == '__main__':
	unittest.main()
