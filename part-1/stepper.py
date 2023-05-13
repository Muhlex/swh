import Stepper
from machine import Pin

In1 = Pin(5, Pin.OUT)
In2 = Pin(4, Pin.OUT)
In3 = Pin(3, Pin.OUT)
In4 = Pin(2, Pin.OUT)

while True:
	s1 = Stepper.create(In1, In2, In3, In4, delay = 3)
	s1.step(509, -1)

	s1 = Stepper.create(In1, In2, In3, In4, delay = 1)
	s1.step(509)
