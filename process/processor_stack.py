from .base_processor import BaseProcessor
from datetime import datetime, timedelta
from collections import defaultdict
import heapq
import pandas as pd


class CallStackProcessor(BaseProcessor):
    def __init__(self, start_node, route):
        self.start_node = start_node
        self.route = route
        self.logs = []
        self._by_fa = defaultdict(list)
        self._fa_sensor_name = defaultdict(list)
        self.token_id_len = 10
        self.senser_hash = {}
        self.senser_pointer = 0
        self.now = datetime.now()

    def _run(self, iter):
        token_stack = self._set_start_token(iter)
        heapq.heapify(token_stack)

        while token_stack:
            time, token_id, gate = heapq.heappop(token_stack)

            node = gate.get_next_node()

            if node._check_is_running(time):
                node, time = self._set_logs(
                    token_id, node, time)

                if self.route[node.name] == None:
                    continue

                heapq.heappush(
                    token_stack, [time, token_id,  self.route[node.name]])
            else:
                heapq.heappush(
                    token_stack, [time + 1, token_id, gate])
        print(node.sensor[0]._get_data_generator())

    def _set_start_token(self, iter):
        stack = []
        time = 0
        for i in range(iter):
            token_id = self._unique_id(self.token_id_len)
            node, time = self._set_logs(token_id, self.start_node,
                                        time=time)
            stack.append(
                [time, token_id, self.route[self.start_node.name]])

        return stack

    def _set_logs(self, token_id, node, time):
        sensor_log = self._generate_sensor_log(node.sensor)
        log_entry = [token_id, node.name, datetime.strftime(self.now + timedelta(seconds=time) +
                                                            timedelta(seconds=node.time), '%Y-%m-%d %H:%M:%S')] + sensor_log
        self.logs.append(log_entry)
        return node, time + node.time
