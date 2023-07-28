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

            node, time = self._set_logs(
                token_id, node, time, by_fa=False)

            if self.route[node.name] == None:
                continue

            heapq.heappush(
                token_stack, [time, token_id,  self.route[node.name]])

    def _set_start_token(self, iter):
        stack = []
        time = 0
        for i in range(iter):
            token_id = self._unique_id(self.token_id_len)
            node, time = self._set_logs(token_id, self.start_node,
                                        time=time, by_fa=False)
            stack.append(
                [time, token_id, self.route[self.start_node.name]])

        return stack

    def _set_logs(self, token_id, node, time, by_fa=False):
        if by_fa:
            sensor_log = self._generate_sensor_log_by_facility(node.sensor)
            log_entry = [token_id, node.name, self.now + timedelta(seconds=time) +
                         timedelta(seconds=node.time)] + sensor_log
            if not self._fa_sensor_name[node.name]:
                self._fa_sensor_name[node.name] = [i.name for i in node.sensor]
            self._by_fa[node.name].append(log_entry)
        else:

            sensor_log = self._generate_sensor_log(node.sensor)
            log_entry = [token_id, node.name, datetime.strftime(self.now + timedelta(seconds=time) +
                         timedelta(seconds=node.time), '%Y-%m-%d %H:%M:%S')] + sensor_log
            self.logs.append(log_entry)
        return node, time + node.time
