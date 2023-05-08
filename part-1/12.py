from machine import Pin, PWM
import utime

# IMPORTANT! HC-SR04 runs on 5V; Connect its VCC to VBUS (pin 40)

trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)
speaker = PWM(Pin(16, Pin.OUT))

def mapRange(value, inMin, inMax, outMin, outMax):
  return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

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


speaker.duty_u16(512)
try:
    while True:
        distance = measureCM()
        freq = int(mapRange(distance, 2, 100, 20, 2000))
        speaker.freq(freq)
        print('Playing frequency:', freq)
        utime.sleep_ms(50)

except ValueError:
    pass

except:
    speaker.deinit()
