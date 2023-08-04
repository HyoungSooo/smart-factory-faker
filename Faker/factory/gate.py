import random
from numpy.random import choice


class BaseGate:
    def __init__(self, node) -> None:
        self.next = node

    def get_next_node(self, get_all_node=False):
        return self.next


class SeqLoop(BaseGate):
    def __init__(self, node) -> None:
        super().__init__(node)


class Or(BaseGate):
    def __init__(self, bp: list = [], node: list = []) -> None:
        super().__init__(node)
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


class Loop(BaseGate):
    def __init__(self, node) -> None:
        super().__init__(node)
        self.__loop_is_open = True
        self.__loop_count = None
        self.__loop_counter = 0

    def set_loop_count(self, count):
        self.__loop_counter = count

    def __check_loop_is_open(self):
        if self.__loop_counter >= self.__loop_count:
            self.__loop_is_open = False
            return False

        return True

    def get_next_node(self, get_all_node=False):
        if self.__loop_is_open:
            return super().get_next_node(get_all_node)
        else:
            return None
