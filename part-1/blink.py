from machine import Pin
from time import sleep_ms

led = Pin(25, Pin.OUT);

while True:
	led.on()
	sleep_ms(200)
	led.off()
	sleep_ms(50)
