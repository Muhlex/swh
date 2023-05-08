from machine import ADC
from time import sleep_ms

#We are using ADC2 which is referenced as GP28
analog_input = ADC(28)

while True:
    value = analog_input.read_u16()
    print("ADC value:",value)
    print(value)

    sleep_ms(100)
