import board
import digitalio
import time

now = time.monotonic()
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
end_minutes = 30

looping = True

while looping:
    led.value = True
    # then = datetime.datetime.now()
    if (now + (end_minutes * 60)) <  time.monotonic():
        looping = False
        
