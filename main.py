import RPi.GPIO as IO
from MotorController import MotorController
from ServoController import ServoController
from time import sleep

move = MotorController()

servos = ServoController()

IO.cleanup()
