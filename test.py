import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
while 1:
    print "LED on"
    GPIO.output(26, GPIO.HIGH)
    time.sleep(6)
    print "LED off"
    GPIO.output(26, GPIO.LOW)
    time.sleep(10)
