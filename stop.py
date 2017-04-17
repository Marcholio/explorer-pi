import RPi.GPIO as IO
from MotorController import MotorController
from ServoController import ServoController
from time import sleep

move = MotorController()
servos = ServoController()

move.stop()
servos.setServo('head', 0)
sleep(1)
