from machine import Pin, PWM
from time import sleep

bps = 8
#notes and corresponding frequency
tonesToFreq = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    ' ': 0,
}

speaker = PWM(Pin(16, Pin.OUT))
melody = ['e','d','e','g','d','c','d','f','g','f','e','d','e','a','b','a','f','g','f',' ']
rhythm = [12,  4,  4,  4,  2, 10,  6,  1,  1,  4, 12,  4,  4,  4, 12,  6,  1,  1,  2,  4 ]

try:
    while True:
        for tone, length in zip(melody, rhythm):
            print('Note:', tone)
            freq = tonesToFreq[tone]
            speaker.duty_u16(512)
            speaker.freq(freq) if freq > 8 else speaker.duty_u16(0)
            sleep(length / bps)

except:
    speaker.deinit()
