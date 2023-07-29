import pandas as pd
from collections import defaultdict
from .base_processor import BaseProcessor


class Processor(BaseProcessor):
    def __init__(self, start_node, route) -> None:
        """Initialize the processor with the start node and the route.

          Args:
            start_node: The start node of the simulation.
            route: The route of the simulation.
        """
        self.start_node = start_node
        self.route = route
        self.logs = []
        self._by_fa = defaultdict(list)
        self._fa_sensor_name = defaultdict(list)
        self.token_id_len = 10
        self.senser_hash = {}
        self.senser_pointer = 0

    def by_facility(self, iter):
        """
        Generate a Pandas DataFrame for each facility.

        Args:
          iter: The number of iterations.

        Returns:
          A dictionary of Pandas DataFrames.
        """
        self._run(iter, by_fa=True)

        for key, logs in self._by_fa.items():
            self._by_fa[key] = pd.DataFrame(
                logs, columns=['token_id', 'facility', '@timestamp'] + self._fa_sensor_name[key])

        return self._by_fa
