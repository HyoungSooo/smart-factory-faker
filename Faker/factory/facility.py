from collections import defaultdict
from datetime import datetime, timedelta
import pandas as pd


class Facility:
    def __init__(self, name, *sensor, time=1):
        self.name = name
        self.sensor = sensor
        self.time = time
        self.stack = []
        self.current_time = 0
        self.total_running_time = 0
        self.__history = {'expire': {}, 'wait': {}}
        self.max_wait_stack = 0

        self._check_time()

    @property
    def history(self):
        history_log = {}
        history_frame = []
        for keyword in self.__history:
            for date, value in self.__history[keyword].items():
                if date not in history_log:
                    history_log[date] = [0, 0]
                if keyword == 'expire':
                    history_log[date][0] += value
                else:
                    history_log[date][1] += value

        for date, log in history_log.items():
            history_frame.append([date]+log)

        df = pd.DataFrame(history_frame, columns=[
                          '@timestamp', 'expired', 'wait'])

        return df

    def _check_time(self):
        '''
        Check the time whether it is float

        Return:
          Bool
        '''

        if type(self.time) == int:
            return True
        raise TypeError('time must be an int')

    def _update_current_time(self, time, now):
        self.current_time = time + self.time
        self.__set_history(time, now, 'expire')

    def _check_is_running(self, time, now):
        if time > self.current_time:
            self._update_current_time(time, now)
            return True
        else:
            self.__set_history(time, now, 'wait')
            return False

    def __set_history(self, time, now, keyword):
        date = datetime.strftime(
            now + timedelta(seconds=time), '%Y-%m-%d %H:%M:%S')

        if date not in self.__history[keyword]:
            self.__history[keyword][date] = 0

        self.__history[keyword][date] += 1
