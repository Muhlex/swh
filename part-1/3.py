from machine import Pin
from time import sleep_ms

leds = [Pin(25, Pin.OUT), Pin(16, Pin.OUT), Pin(21, Pin.OUT)]
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
	pressed = button.value()
	for led in leds:
		if pressed:
			led.on()
		else:
			led.off()

	sleep_ms(50)
