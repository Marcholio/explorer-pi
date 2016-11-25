import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
pwm = GPIO.PWM(22, 50)
pwm.start(2.5)

for i in range(3, 9):
    pwm.ChangeDutyCycle(i)
    time.sleep(3)

GPIO.cleanup()
