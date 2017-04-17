import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

class MotorController:
    
    # Pins for each motor
    rightPins = [25,24,23]
    leftPins = [17,27,22]
    fullRound = 4.8
    lastTime = 0
    
    # Initialize all motor pins as output
    for p in rightPins:
        IO.setup(p, IO.OUT)
    for p in leftPins:
        IO.setup(p, IO.OUT)

    def __init__(self):
        self.stop()

    def dodgeRight(self):
        self.turnRight(45)
        self.forward()
        time.sleep(2)
        self.turnLeft(45)

    def dodgeLeft(self):
        self.turnLeft(45)
        self.forward()
        sleep(2)
        self.turnRight(45)

    def stop(self):
        self.rightStop()
        self.leftStop()

    def forward(self):
        if( round(time.time()) != self.lastTime):
            self.lastTime = round(time.time())
            self.turnLeft(5)
        self.rightForward()
        self.leftForward()

    def reverse(self):
        self.rightReverse()
        self.leftReverse()
        
    def turnRight(self, degrees):
        self.rightStop()
        self.leftForward()
        time.sleep((degrees / 360.0) * self.fullRound)

    def turnLeft(self, degrees):
        self.leftStop()
        self.rightForward()
        # Right track is a bit weaker somehow so need to compensate that by running longer
        time.sleep((degrees / 180.0) * self.fullRound)

    def spinRight(self, degrees):
        self.rightReverse()
        self.leftForward()
        time.sleep((degrees / 360.0) * self.fullRound)

    def spinLeft(self, degrees):
        self.rightForward()
        self.leftReverse()
        time.sleep((degrees / 360.0) * self.fullRound)

    def turnRightReverse(self, degrees):
        self.rightStop()
        self.leftReverse()
        sleep((degrees / 360.0) * self.fullRound)

    def turnLeftReverse(self, degrees):
        self.leftStop()
        self.rightReverse()
        # Right track is a bit weaker somehow so need to compensate that by running longer
        time.sleep((degrees / 180.0) * self.fullRound)

    def rightForward(self):
        self.setPin(self.rightPins[0], False)
        self.setPin(self.rightPins[1], True)
        self.setPin(self.rightPins[2], True)

    def rightStop(self):
        for i in range(0,3):
            self.setPin(self.rightPins[i], False)

    def rightReverse(self):
        self.setPin(self.rightPins[0], True)
        self.setPin(self.rightPins[1], True)
        self.setPin(self.rightPins[2], False)

    def leftForward(self):
        self.setPin(self.leftPins[0], False)
        self.setPin(self.leftPins[1], True)
        self.setPin(self.leftPins[2], True)

    def leftStop(self):
        for i in range(0,3):
            self.setPin(self.leftPins[i], False)

    def leftReverse(self):
        self.setPin(self.leftPins[0], True)
        self.setPin(self.leftPins[1], True)
        self.setPin(self.leftPins[2], False)
        
    # Wrapper for IO.output function
    def setPin(self, pin, value):
        if (value):
            IO.output(pin, IO.HIGH)
        else:
            IO.output(pin, IO.LOW)
