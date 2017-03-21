import RPi.GPIO as IO
from MotorController import MotorController
from time import sleep

move = MotorController()

move.turnLeftReverse(90)

move.forward(0.5)

move.turnRight(90)

IO.cleanup()
