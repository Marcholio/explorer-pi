import RPi.GPIO as IO
from gpiozero import DistanceSensor
from MotorController import MotorController
from ServoController import ServoController
from time import sleep

ds = DistanceSensor(echo=12, trigger=18)
move = MotorController()
servos = ServoController()

safeDistance = 0.25
sideMax = 0.4
sideMin = 0.2

def check(direction):
    if (direction == 'front'):
        curMin = 1.0
        for i in range(-45, 45):
            servos.setServo('head', i)
            sleep(0.05)
            dist = ds.distance
            curMin = min(dist, curMin)
        return curMin
            
    elif (direction == 'left'):
        servos.setServo('head', 45)
    else:
        servos.setServo('head', -45)
        
    sleep(0.2)
    dist = ds.distance
    return dist
    
stop = False
angle = 0
distDir = -1
move.forward()

while (not stop):
    servos.setServo('head', angle)
    angle += distDir

    if (angle > 45):
        distDir = -1
    elif (angle < -45):
        distDir = 1
    
    sleep(0.01)
    dist = ds.distance
    stop = dist < safeDistance

move.stop()

leftSum = 0
for i in range(0,45):
    servos.setServo('head', i)
    sleep(0.02)
    leftSum += ds.distance

rightSum = 0
for i in range(-45, 0):
    servos.setServo('head', i)
    sleep(0.02)
    rightSum += ds.distance

direction = ''

print ("LEFT: %.5f, RIGHT: %.5f" % (leftSum, rightSum))

if (leftSum > rightSum):
    move.turnLeft(45)
    direction = 'left'
    i = 0
    while (i < 2):
        frontDist = check('front')
        if (frontDist < safeDistance):
            if(frontDist > 0.15):
                move.turnLeft(5)
            else:
                move.spinLeft(20)
        else:
            rightDistance = check('right')
            if (rightDistance < sideMin):
                move.turnLeft(2)
            elif (rightDistance > sideMax):
                move.turnRight(2)
        move.forward()
        i += 1
else:
    move.turnRight(45)
    direction = 'right'
    i = 0
    while (i < 2):
        frontDist = check('front')
        if (frontDist < safeDistance):
            if(frontDist > 0.15):
                move.turnRight(5)
            else:
                move.spinRight(20)
        else:
            leftDistance = check('left')
            if (leftDistance < sideMin):
                move.turnRight(2)
            elif (leftDistance > sideMax):
                move.turnLeft(2)
        move.forward()
        i += 1

servos.setServo('head', 0)
move.stop()    
sleep(1)
