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

        return pd.DataFrame(self.logs, columns=['token_id', 'facility', '@timestamp'] + sensor_columns)

    def to_csv(self, iter, path):
        """
        Save the DataFrame to a CSV file.

        Args:
          iter: The number of iterations.
          path: The path to the CSV file.
        """
        df = self.to_dataframe(iter)
        df.to_csv(path, ',')

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
