import random
from numpy.random import choice


class SeqLoop:
    def __init__(self, node) -> None:
        self.next = node

    def get_next_node(self, get_all_node=False):
        return self.next


class Or:
    def __init__(self, bp: list = [], node: list = []) -> None:
        self.next = node
        if not bp:
            raise TypeError('bp is not define Or(bp:list, node:list)')
        self.branch_probability = bp
        self.next_nodes_list = list()

        self._set_next_nodes_list()

    def _set_next_nodes_list(self):
        for node, probability in zip(self.next, self.branch_probability):
            self.next_nodes_list.extend([node]*probability)

    def get_next_node(self, get_all_node=False):
        if not get_all_node:
            node = random.choices(
                self.next_nodes_list)
            return node[0]
        return self.next
