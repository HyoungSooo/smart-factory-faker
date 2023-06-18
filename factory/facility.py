class Facility:
    def __init__(self, name, *sensor, time=1, error=0.02):
        self.name = name
        self.error = error
        self.sensor = sensor
        self.time = time
