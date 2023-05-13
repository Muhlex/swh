from machine import Pin
import utime

# IMPORTANT! HC-SR04 runs on 5V; Connect its VCC to VBUS (pin 40)

trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

def measureCM():
	trigger.low()
	utime.sleep_us(2)
	trigger.high()
	utime.sleep_us(5)
	trigger.low()
	signalon = 0
	signaloff = 0
	while echo.value() == 0:
		signaloff = utime.ticks_us()
	while echo.value() == 1:
		signalon = utime.ticks_us()
	timepassed = signalon - signaloff
	distance = timepassed * 0.01715
	return distance


while True:
	distance = measureCM()
	print("The distance from object is", f"{distance:4.2f}", "cm")
	utime.sleep_ms(50)
