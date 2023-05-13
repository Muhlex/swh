from machine import Pin
from time import sleep_ms

green = Pin(25, Pin.OUT)
yellow = Pin(16, Pin.OUT)
red = Pin(21, Pin.OUT)

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

pressed = False

state = 0

def updateLights(state):
	global green, yellow, red
	green.off()
	yellow.off()
	red.off()
	if state == 0:
		red.on()
	elif state == 1:
		red.on()
		yellow.on()
	elif state == 2:
		green.on()
	else:
		yellow.on()

def onClick():
	global state
	state = (state + 1) % 4
	updateLights(state)

updateLights(state)

while True:
	if not pressed and button.value():
		onClick()
	pressed = button.value()

	sleep_ms(10)
