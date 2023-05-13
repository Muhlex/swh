from machine import Pin, PWM, ADC
from time import sleep_ms

class Position():
	MIN = 1000000
	MID = 1500000
	MAX = 2000000

def mapRange(value, inMin, inMax, outMin, outMax):
	return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

input = ADC(Pin(26))
servo = PWM(Pin(16))
servo.freq(100)
servo.duty_ns(Position.MID)

try:
	while True:
		value = input.read_u16()
		pos = mapRange(value, 0, 2 ** 16 - 1, Position.MIN, Position.MAX)
		servo.duty_ns(int(pos))
		sleep_ms(50)

except:
	servo.deinit()
