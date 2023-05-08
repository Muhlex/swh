from machine import Pin, ADC, PWM
from time import sleep_ms

MAX_UINT16 = 2 ** 16 - 1

class Button:
    def __init__(self, pinID: int | str, onClick):
        self.pressed = False
        self.pin = Pin(pinID, Pin.IN, Pin.PULL_DOWN)
        self.onClick = onClick

    def update(self):
        value = self.pin.value()
        if not self.pressed and value:
            self.onClick()
        self.pressed = value

input = ADC(Pin(28))
output = PWM(Pin(16))
output.freq(1000)

reversed = False

def onClick():
    global reversed
    reversed = not reversed
button = Button(0, onClick)

while True:
    button.update()

    value = input.read_u16()
    print('Analog input value:', value, "| Reversed:", reversed)
    valueAdjusted = value if not reversed else MAX_UINT16 - value
    brightness = int(valueAdjusted ** 2 / MAX_UINT16) # adjust for linear brightness perception
    output.duty_u16(brightness)
    sleep_ms(50)
