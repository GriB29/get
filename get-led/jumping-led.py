import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

light_time = .2
forward = 0
try:
    while True:
        for led in leds[::1 if forward else -1]:
            GPIO.output(led, 1)
            sleep(light_time)
            GPIO.output(led, 0)
        forward = not forward
except KeyboardInterrupt:
    GPIO.output(leds, 0)
