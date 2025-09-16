import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
duty = .0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    sleep(.05)

    duty += 1.
    if duty >= 100.:
        duty = .0
