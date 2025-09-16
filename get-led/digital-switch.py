import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

button = 13
led = 26
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

state = True
while True:
    if GPIO.input(button):
        GPIO.output(led, state)
        state = not state
        sleep(.2)
