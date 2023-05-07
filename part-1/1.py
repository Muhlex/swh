from machine import Pin
from time import sleep_ms

leds = [Pin(25, Pin.OUT), Pin(16, Pin.OUT), Pin(21, Pin.OUT)]

iteration = 0
while True:
    sleep_ms(200)
    for i, led in enumerate(leds):
        if iteration % ((i+1) * 2) < i+1:
            led.on()
        else:
            led.off()
    iteration += 1