from machine import Pin
from time import sleep_us

speaker = Pin(16, Pin.OUT)

def hertzToHalfUS(hertz: int):
    return int(1 / hertz * 1000000 / 2)

for hertz in range(20, 12000, 80):
    print(hertz)
    for i in range(int(hertz / 8)):
        sleepTime = hertzToHalfUS(hertz)
        speaker.on()
        sleep_us(sleepTime)

        speaker.off()
        sleep_us(sleepTime)
