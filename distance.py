from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=12, trigger=18)

while True:
    print(sensor.distance)
