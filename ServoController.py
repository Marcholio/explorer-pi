import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)
IO.setmode(IO.BCM)

PWM_MIN = 2.5
PWM_MID = 6.25
PWM_MAX = 10
PWM_DIVIDER = 180 / (PWM_MAX - PWM_MIN)

class ServoController:
    pwms = {}

    # Initialize all servos and set them to middle
    def __init__(self, pins):
        for pin in pins:
            IO.setup(pin, IO.OUT)
            self.pwms[pin] = IO.PWM(pin, 50)
            self.pwms[pin].start(PWM_MID)

    # Degrees are between -90 and 90 degrees
    def setServo(self, pin, degrees):
        cycle = min(max(degrees / PWM_DIVIDER + PWM_MID, PWM_MIN), PWM_MAX)
        self.pwms[pin].ChangeDutyCycle(cycle)

    def reset(self):
        for pin in self.pwms.keys():
            self.setServo(pin, 0)
        sleep(0.2)
        for pin in self.pwms.keys():
            self.pwms[pin].stop()
        sleep(1)
        IO.cleanup()
