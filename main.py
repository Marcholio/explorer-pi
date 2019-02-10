import RPi.GPIO as IO
from ServoController import ServoController
from time import sleep

RF_SHOULDER = 18
RF_ELBOW = 23
LB_SHOULDER = 6
LB_ELBOW = 13

pins = [RF_SHOULDER, RF_ELBOW, LB_SHOULDER, LB_ELBOW]

SHOULDER_MIN = -60
SHOULDER_MID = 0
SHOULDER_MAX = 60

ELBOW_MIN = -10
ELBOW_MID = 0
ELBOW_MAX = 10

SPEED = 1

right_legs = [[RF_SHOULDER, RF_ELBOW]]
left_legs = [[LB_SHOULDER, LB_ELBOW]]
right_leg_positions = [0]
left_leg_positions = [2]

servos = ServoController(pins)

def forward():
    right_shoulder_sequence = [SHOULDER_MAX, SHOULDER_MID, SHOULDER_MIN, SHOULDER_MID]
    left_shoulder_sequence = [SHOULDER_MIN, SHOULDER_MID, SHOULDER_MAX, SHOULDER_MID]
    elbow_sequence = [ELBOW_MAX, ELBOW_MIN, ELBOW_MAX, ELBOW_MID]

    for i in range(len(right_legs)):
        right_leg_positions[i] += 1
        right_leg_positions[i] = right_leg_positions[i] % len(right_shoulder_sequence)

        servos.setServo(right_legs[i][0], right_shoulder_sequence[right_leg_positions[i]])
        servos.setServo(right_legs[i][1], elbow_sequence[right_leg_positions[i]])

    for i in range(len(left_legs)):
        left_leg_positions[i] += 1
        left_leg_positions[i] = left_leg_positions[i] % len(left_shoulder_sequence)

        servos.setServo(left_legs[i][0], left_shoulder_sequence[left_leg_positions[i]])
        servos.setServo(left_legs[i][1], elbow_sequence[left_leg_positions[i]])
        
    sleep(1.0/SPEED)
    

for i in range(8):
    forward()
    
servos.reset()
