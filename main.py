import RPi.GPIO as IO
from gpiozero import DistanceSensor
from MotorController import MotorController
from ServoController import ServoController
from time import sleep

ds = DistanceSensor(echo=12, trigger=18)
move = MotorController()
servos = ServoController()

safeDistance = 0.20

def checkSurroundings():
    l = check('left')
    r = check('right')
    return l, r

def check(direction):
    d = 0
    cur = 0

    if (direction == 'left'):
        d = 10
    else:
        d = -10
        
    # Turn head by 10 degree steps and measure distance at each point
    while (abs(d) < 65):
        servos.setServo('head', d)
        sleep(0.2)
        dist = ds.distance
        cur += dist

        if (direction == 'left'):
            d += 10
        else:
            d -= 10
    return cur

stop = False

while (not stop):
    move.forward()
    dist = ds.distance
    stop = dist < safeDistance
move.stop()

left, right = checkSurroundings()

servos.setServo('head', 0)

if (left < right):
    move.dodgeRight()
else:
    move.dodgeLeft()

move.stop()    
sleep(0.1)
