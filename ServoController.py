import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode(IO.BCM)

class ServoController:
    # PWM pin for each servo
    servos = {
        'head': 4
    }

    pwms = {}

    # Initialize all servos and set them to middle
    def __init__(self):
        for name, pin in self.servos.items():
            IO.setup(pin, IO.OUT)
            self.pwms[name] = IO.PWM(self.servos[name], 50)
            self.pwms[name].start(6.25)

    # Degrees are between -90 and 90 degrees
    def setServo(self, name, degrees):
        cycle = min(max(degrees / 24.0 + 6.25, 2.5), 10.0)
        self.pwms[name].ChangeDutyCycle(cycle)
