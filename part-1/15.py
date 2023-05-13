from machine import Pin, ADC
from time import sleep_ms
import Stepper

class Rotary:
	value = -1
	frac = -1
	MAX_VALUE = 2 ** 16 - 1

	def __init__(self, pinID: int | str):
		self.adc = ADC(Pin(pinID))

	def update(self):
		self.value = self.adc.read_u16()
		self.frac = self.value / self.MAX_VALUE

class Motor:
	def __init__(self, pinID1: int | str, pinID2: int | str, pinID3: int | str, pinID4: int | str):
		self.pins = [Pin(pinID1, Pin.OUT), Pin(pinID2, Pin.OUT), Pin(pinID3, Pin.OUT) , Pin(pinID4, Pin.OUT)]

	def step(self, delay: int, steps: int):
		stepper = Stepper.create(self.pins[0], self.pins[1], self.pins[2], self.pins[3], delay)
		stepper.step(abs(steps), -1 if steps < 0 else 1)

	def stepDegrees(self, delay: int, degrees: int):
		self.step(delay, int(degrees * 509 / 360))

rotary = Rotary(26)
motor = Motor(5, 4, 3, 2)

try:
	while True:
		rotary.update()
		speedRaw = (rotary.frac - 0.5) * 2;
		speedRawAbs = abs(speedRaw)
		speed = speedRawAbs if speedRawAbs > 0.2 else 0
		if speed == 0:
			sleep_ms(100)
			continue

		CENTER_DELAY = 12
		delay = int((1 - speed) * CENTER_DELAY + 1)
		steps = 1 if speedRaw > 0 else -1
		print('delay:', delay, '| steps:', steps)
		motor.step(delay, steps)
except KeyboardInterrupt:
	print('Exited.')
