import RPi.GPIO as GPIO
from time import sleep


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
up, down = 9, 10
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.output(leds, 0)

num = 0
sleep_time = .2
try:
    while True:
        if GPIO.input(up) and GPIO.input(down):
            num = 2 ** len(leds) - 1
            print(f"current number: DEC={num}, BIN={''.join(map(str, dec2bin(num)))}")
            sleep(sleep_time)
        if GPIO.input(up):
            if num < 2 ** len(leds) - 1:
                num += 1
            else:
                num = 0
            print(f"current number: DEC={num}, BIN={''.join(map(str, dec2bin(num)))}")
            sleep(sleep_time)
        if GPIO.input(down) and num > 0:
            num -= 1
            print(f"current number: DEC={num}, BIN={''.join(map(str, dec2bin(num)))}")
            sleep(sleep_time)
        bin_num = dec2bin(num)
        for i in range(len(leds)):
            GPIO.output(leds[i], bin_num[i])

except KeyboardInterrupt:
    GPIO.output(leds, 0)
