import random


class SeqLoop:
    def __init__(self, node) -> None:
        self.next = node

    def get_next_node(self):
        return self.next


class Or:
    def __init__(self, bp: list = [], node: list = []) -> None:
        self.next = node
        if not bp:
            raise TypeError('bp is not define Or(bp:list, node:list)')
        self.branch_probability = bp

    def get_next_node(self):
        node = random.choices(self.next, weights=self.branch_probability, k=1)
        return node[0]
