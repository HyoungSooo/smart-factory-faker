from collections import deque
from datetime import datetime, timedelta
import pandas as pd
import string
import random


class Route:
    def __init__(self, start_node, route) -> None:
        self.start_node = start_node
        self.route = route
        self.logs = []
        self.token_id_len = 10
        self.senser_hash = {}
        self.senser_pointer = 0

    def run(self, iter):

        stack = deque([])

        for i in range(iter):
            time = datetime.now() + timedelta(seconds=i)
            token_id = self.unique_id(self.token_id_len)
            self.set_logs(token_id, self.start_node, time=time)
            stack.append((token_id, self.route[self.start_node.name], time))

        while stack:
            token_id, gate, time = stack.popleft()

            node = gate.get_next_node()

            node, time = self.set_logs(token_id, node, time)

            if self.route[node.name] == None:
                continue

            stack.append((token_id, self.route[node.name], time))

    def to_dataframe(self, iter):
        self.run(iter)
        for i in self.logs:
            self.pad_list(i, 3 + self.senser_pointer)
        sensor_columns = [i[0] for i in sorted(
            self.senser_hash.items(), key=lambda x: x[1])]

        return pd.DataFrame(self.logs, columns=['token_id', 'facility', '@timestamp'] + sensor_columns)

    def set_logs(self, token_id, node, time):
        sensor_log = self._generate_sensor_log(node.sensor)
        log_entry = [token_id, node.name, time +
                     timedelta(node.time)] + sensor_log
        self.logs.append(log_entry)
        return node, time + timedelta(node.time)

    def _generate_sensor_log(self, sensors):
        sensor_log = [None] * self.senser_pointer
        for sensor in sensors:
            if sensor.name in self.senser_hash:
                try:
                    sensor_log[self.senser_hash[sensor.name]] = random.uniform(
                        sensor.min_value, sensor.max_value)
                except IndexError:
                    diff = self.senser_hash[sensor.name] - len(sensor_log)
                    sensor_log += [None] * diff + \
                        [random.uniform(sensor.min_value, sensor.max_value)]
            else:
                self.senser_hash[sensor.name] = self.senser_pointer
                diff = self.senser_hash[sensor.name] - len(sensor_log)
                sensor_log += [None] * diff + \
                    [random.uniform(sensor.min_value, sensor.max_value)]
                self.senser_pointer += 1
        return sensor_log

    def unique_id(self, size):
        chars = list(set(string.ascii_uppercase +
                     string.digits).difference('LIO01'))
        return ''.join(random.choices(chars, k=size))

    def pad_list(self, list_to_pad, desired_length):
        """
        Pads a list with the given padding value to the desired length.

        Args:
          list_to_pad: The list to pad.
          padding_value: The value to pad the list with.
          desired_length: The desired length of the padded list.

        Returns:
          The padded list.
        """

        padded_list = list_to_pad
        while len(padded_list) < desired_length:
            padded_list.append(None)

        return padded_list
