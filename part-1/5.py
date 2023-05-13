from machine import Pin, PWM
from time import sleep_ms

pwmLED = PWM(Pin(16))

while True:
	pwmLED.freq(1000)

	for brightness in range(16 * 4):
		pwmLED.duty_u16(int(2 ** (brightness / 4)))
		sleep_ms(50)

	for freq in range(32, 0, -8):
		pwmLED.freq(freq)
		sleep_ms(1000)
