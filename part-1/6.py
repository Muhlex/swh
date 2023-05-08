from machine import Pin, ADC, PWM
from time import sleep_ms

input = ADC(Pin(28))
output = PWM(Pin(16))
output.freq(1000)

MAX = 2 ** 16 - 1

while True:
    value = input.read_u16()
    print('Analog input value:', value)
    output.duty_u16(int(value ** 2 / MAX)) # adjust for linear brightness perception
    sleep_ms(50)
