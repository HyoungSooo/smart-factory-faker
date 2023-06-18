import random


class SeqLoop:
    def __init__(self, node) -> None:
        self.next = node

    def get_next_node(self):
        return self.next


class Or:
    def __init__(self, *node) -> None:
        self.next = node

    def get_next_node(self):
        return random.choice(self.next)
