from collections import deque
from datetime import datetime, timedelta
import string
import random
import pandas as pd
from collections import defaultdict
from Faker.miner.analyzer import Analyzer
from Faker.miner.visualize import ProcessVisualize, PlotData


class BaseProcessor:
    def __init__(self):
        self.senser_hash = {}
        self.senser_pointer = 0
        self._fa_sensor_name = defaultdict(list)
        self.token_id_len = 10
        self.df = None

        self.analyzer = Analyzer()
        self.visualizer = ProcessVisualize(
            './', 'ProcessMap', 'ProcessMap', 'Process')

    def _run(self, iter, by_fa=False):
        '''The `_run()` function runs the simulation for the given number of iterations.
        It first generates a unique ID for each token.
        Then, it sets the logs for the start node.
        Then, it pushes the start node and the time to the stack.
        While the stack is not empty, it pops the top element from the stack.
        It then gets the next node from the gate.
        It sets the logs for the next node.
        If the next node is the end node, it does nothing.
        Otherwise, it pushes the next node and the time to the stack.'''

        stack = self._set_start_token(iter, by_fa=by_fa)

        while stack:
            token_id, gate, time = stack.popleft()

            node = gate.get_next_node()

            node, time = self._set_logs(token_id, node, time, by_fa=by_fa)

            if self.route[node.name] == None:
                continue

            stack.append(
                (token_id, self.route[node.name], time + timedelta(seconds=node.time)))

    def _set_start_token(self, iter, by_fa):
        stack = deque([])
        for i in range(iter):
            time = datetime.now() + timedelta(seconds=i)
            token_id = self._unique_id(self.token_id_len)
            self._set_logs(token_id, self.start_node, time=time, by_fa=by_fa)
            stack.append((token_id, self.route[self.start_node.name], time))

        return stack

    def _set_logs(self, token_id, node, time, by_fa=False):
        '''The `_set_logs()` function sets the logs for the given node.
        If the `by_fa` flag is True, it generates the sensor log for the facility.
        Otherwise, it generates the sensor log for the node.
        It then appends the log entry to the logs or the `_by_fa` dictionary.'''
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
        base_sensor_log = [None] * self.senser_pointer
        for sensor in sensors:
            flag, data = sensor._get_values()
            if flag:
                if sensor.name in self.senser_hash:
                    try:
                        base_sensor_log[self.senser_hash[sensor.name]
                                        ] = data
                    except IndexError:
                        diff = self.senser_hash[sensor.name] - \
                            len(base_sensor_log)
                        base_sensor_log += [None] * diff + \
                            [data]
                else:
                    self.senser_hash[sensor.name] = self.senser_pointer
                    diff = self.senser_hash[sensor.name] - len(base_sensor_log)
                    base_sensor_log += [None] * diff + \
                        [data]
                    self.senser_pointer += 1
            else:
                break
        else:
            return flag, base_sensor_log

        return flag, data

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

    def to_dataframe(self, iter):
        """
          Generate a Pandas DataFrame from the logs.

          Args:
            iter: The number of iterations.

          Returns:
            A Pandas DataFrame.
        """
        self._run(iter)
        for i in self.logs:
            self._pad_list(i, 3 + self.senser_pointer)
        sensor_columns = [i[0] for i in sorted(
            self.senser_hash.items(), key=lambda x: x[1])]

        self.df = pd.DataFrame(self.logs, columns=[
                               'token_id', 'facility', '@timestamp'] + sensor_columns).sort_values(by='@timestamp')

        return self.df

    def to_csv(self, iter, path):
        """
        Save the DataFrame to a CSV file.

        Args:
          iter: The number of iterations.
          path: The path to the CSV file.
        """
        df = self.to_dataframe(iter)
        df = df.sort_values(by='@timestamp')
        df.to_csv(path, ',')
