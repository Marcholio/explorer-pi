import RPi.GPIO as IO
from gpiozero import DistanceSensor
from MotorController import MotorController
from ServoController import ServoController
from time import sleep

ds = DistanceSensor(echo=12, trigger=18)
move = MotorController()
servos = ServoController()

safeDistance = 0.25
leftMax = 0.4
leftMin = 0.25

def check(direction):
    if (direction == 'front'):
        servos.setServo('head', 0)
    elif (direction == 'left'):
        servos.setServo('head', 45)
    else:
        servos.setServo('head', -45)
        
    sleep(0.2)
    dist = ds.distance
    print(direction + '%.2f' %(dist))
    return dist

stop = False

while (not stop):
    move.forward()
    dist = ds.distance
    stop = dist < safeDistance
move.stop()

move.turnRight(90)

i = 0

while (i < 1):
    frontDist = check('front')
    if (frontDist < safeDistance):
        if(frontDist > 0.15):
            move.turnRight(10)
        else:
            move.spinRight(20)
    else:
        leftDistance = check('left')
        if (leftDistance < leftMin):
            move.turnRight(2)
        elif (leftDistance > leftMax):
            move.turnLeft(2)
        else:
            move.forward()
    i += 1

servos.setServo('head', 0)
move.stop()    
sleep(1)
