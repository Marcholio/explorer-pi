import RPi.GPIO as IO
from MotorController import MotorController

move = MotorController()

move.forward(0.2)

move.reverse(0.2)

IO.cleanup()
