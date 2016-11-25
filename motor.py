import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

MotorRight1 = 25
MotorRight2 = 24
MotorRight3 = 23

GPIO.setup(MotorRight1, GPIO.OUT)
GPIO.setup(MotorRight2, GPIO.OUT)
GPIO.setup(MotorRight3, GPIO.OUT)

MotorLeft1 = 17
MotorLeft2 = 27
MotorLeft3 = 22

GPIO.setup(MotorLeft1, GPIO.OUT)
GPIO.setup(MotorLeft2, GPIO.OUT)
GPIO.setup(MotorLeft3, GPIO.OUT)

print "Forward"
GPIO.output(MotorRight1, GPIO.LOW)
GPIO.output(MotorRight2, GPIO.HIGH)
GPIO.output(MotorRight3, GPIO.HIGH)

GPIO.output(MotorLeft1, GPIO.LOW)
GPIO.output(MotorLeft2, GPIO.HIGH)
GPIO.output(MotorLeft3, GPIO.HIGH)
sleep(1)

print "Backwards"
GPIO.output(MotorRight1, GPIO.HIGH)
GPIO.output(MotorRight2, GPIO.HIGH)
GPIO.output(MotorRight3, GPIO.LOW)

GPIO.output(MotorLeft1, GPIO.HIGH)
GPIO.output(MotorLeft2, GPIO.HIGH)
GPIO.output(MotorLeft3, GPIO.LOW)
sleep(1)

GPIO.cleanup()
