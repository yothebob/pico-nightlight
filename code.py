import time
import board
import neopixel
from rainbowio import colorwheel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
end_minutes = 30
now = time.monotonic()
pixel.brightness = 0.8
looping = True

def rainbow(delay):
    for color_value in range(255):
        pixel[0] = colorwheel(color_value)
        time.sleep(delay)

while looping:
    rainbow(0.1)
    if (now + (end_minutes * 60)) <  time.monotonic():
        looping = False
        
