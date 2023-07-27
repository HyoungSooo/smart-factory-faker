class Facility:
    def __init__(self, name, *sensor, time=1, error=0.02):
        self.name = name
        self.error = error
        self.sensor = sensor
        self.time = time
        self.stack = []

        self._check_time()

    def _check_time(self):
        '''
        Check the time whether it is float

        Return:
          Bool
        '''

        if type(self.time) == int:
            return True
        raise TypeError('time must be an int')
