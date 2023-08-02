class Facility:
    def __init__(self, name, *sensor, time=1):
        self.name = name
        self.sensor = sensor
        self.time = time
        self.stack = []
        self.current_time = 0
        self.total_running_time = 0

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

    def _update_current_time(self, time):
        self.current_time = time + self.time

    def _check_is_running(self, time):
        if time >= self.current_time:
            self._update_current_time(time)
            return True

        return False
