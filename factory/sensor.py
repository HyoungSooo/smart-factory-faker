import random


class Sensor:
    def __init__(self, name, max_value, min_value) -> None:
        self.name = name
        self.max_value = max_value
        self.min_value = min_value

    def _get_values(self):

        return random.uniform(
            self.min_value, self.max_value)


class BoolSensor:
    def __init__(self, name, true_rate):
        self.name = name
        self.true_rate = true_rate

    def _get_values(self):
        flag_value = random.random()

        if flag_value >= self.true_rate:
            return True

        return False
