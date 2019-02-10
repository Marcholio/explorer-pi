import RPi.GPIO as IO
from ServoController import ServoController
from time import sleep

servos = ServoController()

servos.setServo('test', 0)
sleep(1)
