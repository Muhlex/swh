from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
import Stepper

class Button:
	ticksDown = -1

	def __init__(self, onClick, pinID: int | str, pull = Pin.PULL_DOWN):
		self.invert = (pull == Pin.PULL_UP)
		self.pin = Pin(pinID, Pin.IN, pull)
		self.onClick = onClick

	def update(self):
		pressed = bool(self.pin.value()) ^ self.invert
		if pressed and self.ticksDown == -1:
			self.ticksDown = ticks_ms()
			return
		if not pressed and self.ticksDown > -1:
			onClick(ticks_diff(ticks_ms(), self.ticksDown))
			self.ticksDown = -1

class Motor:
	def __init__(self, pinID1: int | str, pinID2: int | str, pinID3: int | str, pinID4: int | str):
		self.pins = [Pin(pinID1, Pin.OUT), Pin(pinID2, Pin.OUT), Pin(pinID3, Pin.OUT) , Pin(pinID4, Pin.OUT)]

	def step(self, delay: int, steps: int):
		stepper = Stepper.create(self.pins[0], self.pins[1], self.pins[2], self.pins[3], delay)
		stepper.step(abs(steps), -1 if steps < 0 else 1)

	def stepDegrees(self, delay: int, degrees: int):
		self.step(delay, int(degrees * 509 / 360))

led = Pin(25, Pin.OUT)

def onClick(timeMS):
	if timeMS > 800:
		led.on()
		motor.stepDegrees(1, 180)
		led.off()
	else:
		motor.stepDegrees(1, 45)

button = Button(onClick, 16, Pin.PULL_UP)
motor = Motor(5, 4, 3, 2)

try:
	while True:
		button.update()
		sleep_ms(20)
except KeyboardInterrupt:
	print('Exited.')
finally:
	led.off()
