from collections import deque
from datetime import datetime, timedelta
import pandas as pd
import string
import random
from collections import defaultdict


class Route:
    def __init__(self, start_node, route) -> None:
        self.start_node = start_node
        self.route = route
        self.logs = []
        self._by_fa = defaultdict(list)
        self._fa_sensor_name = defaultdict(list)
        self.token_id_len = 10
        self.senser_hash = {}
        self.senser_pointer = 0

    def _run(self, iter, by_fa=False):

        stack = deque([])

        for i in range(iter):
            time = datetime.now() + timedelta(seconds=i)
            token_id = self._unique_id(self.token_id_len)
            self._set_logs(token_id, self.start_node, time=time, by_fa=by_fa)
            stack.append((token_id, self.route[self.start_node.name], time))

        while stack:
            token_id, gate, time = stack.popleft()

            node = gate.get_next_node()

            node, time = self._set_logs(token_id, node, time, by_fa=by_fa)

            if self.route[node.name] == None:
                continue

            stack.append(
                (token_id, self.route[node.name], time + timedelta(seconds=node.time)))

    def to_dataframe(self, iter):
        self._run(iter)
        for i in self.logs:
            self._pad_list(i, 3 + self.senser_pointer)
        sensor_columns = [i[0] for i in sorted(
            self.senser_hash.items(), key=lambda x: x[1])]

        return pd.DataFrame(self.logs, columns=['token_id', 'facility', '@timestamp'] + sensor_columns)

    def _set_logs(self, token_id, node, time, by_fa=False):
        if by_fa:
            sensor_log = self._generate_sensor_log_by_facility(node.sensor)
            log_entry = [token_id, node.name, time +
                         timedelta(seconds=node.time)] + sensor_log
            if not self._fa_sensor_name[node.name]:
                self._fa_sensor_name[node.name] = [i.name for i in node.sensor]
            self._by_fa[node.name].append(log_entry)
        else:

            sensor_log = self._generate_sensor_log(node.sensor)
            log_entry = [token_id, node.name, time +
                         timedelta(seconds=node.time)] + sensor_log
            self.logs.append(log_entry)
        return node, time + timedelta(node.time)

    def _generate_sensor_log(self, sensors):
        sensor_log = [None] * self.senser_pointer
        for sensor in sensors:
            if sensor.name in self.senser_hash:
                try:
                    sensor_log[self.senser_hash[sensor.name]
                               ] = sensor._get_value()
                except IndexError:
                    diff = self.senser_hash[sensor.name] - len(sensor_log)
                    sensor_log += [None] * diff + \
                        [sensor._get_value()]
            else:
                self.senser_hash[sensor.name] = self.senser_pointer
                diff = self.senser_hash[sensor.name] - len(sensor_log)
                sensor_log += [None] * diff + \
                    [sensor._get_value()]
                self.senser_pointer += 1
        return sensor_log

    def _generate_sensor_log_by_facility(self, sensors):
        sensor_log = [None] * len(sensors)

        for index in range(len(sensors)):
            sensor_log[index] = sensors[index]._get_values()
        return sensor_log

    def _unique_id(self, size):
        chars = list(set(string.ascii_uppercase +
                     string.digits).difference('LIO01'))
        return ''.join(random.choices(chars, k=size))

    def _pad_list(self, list_to_pad, desired_length):
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

    def to_csv(self, iter, path):
        df = self.to_dataframe(iter)
        df.to_csv(path, ',')

    def by_facility(self, iter):
        self._run(iter, by_fa=True)

        for key, logs in self._by_fa.items():
            self._by_fa[key] = pd.DataFrame(
                logs, columns=['token_id', 'facility', '@timestamp'] + self._fa_sensor_name[key])

        return self._by_fa
