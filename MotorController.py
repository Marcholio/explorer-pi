import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

class MotorController:
    
    # Pins for each motor
    rightPins = [25,24,23]
    leftPins = [17,27,22]
    fullRound = 4.8

    # Initialize all motor pins as output
    for p in rightPins:
        IO.setup(p, IO.OUT)
    for p in leftPins:
        IO.setup(p, IO.OUT)

    def __init__(self):
        self.stop()

    def stop(self):
        self.rightStop()
        self.leftStop()

    def forward(self, duration):
        self.rightForward()
        self.leftForward()
        sleep(duration)

    def reverse(self, duration):
        self.rightReverse()
        self.leftReverse()
        sleep(duration)

    def turnRight(self, degrees):
        self.rightStop()
        self.leftForward()
        sleep((degrees / 360.0) * self.fullRound)

    def turnLeft(self, degrees):
        self.leftStop()
        self.rightForward()
        # Right track is a bit weaker somehow so need to compensate that by running longer
        sleep((degrees / 180.0) * self.fullRound)

    def spinRight(self, degrees):
        self.rightReverse()
        self.leftForward()
        sleep((degrees / 360.0) * self.fullRound)

    def spinLeft(self, degrees):
        self.rightForward()
        self.leftReverse()
        sleep((degrees / 360.0) * self.fullRound)

    def turnRightReverse(self, degrees):
        self.rightStop()
        self.leftReverse()
        sleep((degrees / 360.0) * self.fullRound)

    def turnLeftReverse(self, degrees):
        self.leftStop()
        self.rightReverse()
        # Right track is a bit weaker somehow so need to compensate that by running longer
        sleep((degrees / 180.0) * self.fullRound)

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
