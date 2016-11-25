import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BCM)

class MotorController:
    
    # Pins for each motor
    rightPins = [25,24,23]
    leftPins = [17,27,22]

    # Initialize all motor pins as output
    for p in rightPins:
        IO.setup(p, IO.OUT)
    for p in leftPins:
        IO.setup(p, IO.OUT)

    def __init__(self):
        self.stop()

    def stop(self):
        # Set all pins to False
        for i in range(0,3):
            self.setPin(self.rightPins[i], False)
            self.setPin(self.leftPins[i], False)

    def forward(self, duration):
        self.setPin(self.rightPins[0], False)
        self.setPin(self.rightPins[1], True)
        self.setPin(self.rightPins[2], True)

        self.setPin(self.leftPins[0], False)
        self.setPin(self.leftPins[1], True)
        self.setPin(self.leftPins[2], True)
        sleep(duration)

    def reverse(self, duration):
        self.setPin(self.rightPins[0], True)
        self.setPin(self.rightPins[1], True)
        self.setPin(self.rightPins[2], False)

        self.setPin(self.leftPins[0], True)
        self.setPin(self.leftPins[1], True)
        self.setPin(self.leftPins[2], False)
        sleep(duration)
        
    # Wrapper for IO.output function
    def setPin(self, pin, value):
        if (value):
            IO.output(pin, IO.HIGH)
        else:
            IO.output(pin, IO.LOW)
