from machine import Pin
from time import sleep_ms

leds = [Pin(25, Pin.OUT), Pin(16, Pin.OUT), Pin(21, Pin.OUT), Pin(15, Pin.OUT)]

while True:
	for led in leds:
		led.on()
		sleep_ms(1000)
		led.off()
