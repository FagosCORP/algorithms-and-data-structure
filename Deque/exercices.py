from re import L
import numpy as np


class Deque:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.init = -1
        self.final = 0
        self.number_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __is_fulled_deque(self):
        return (self.init == 0 and self.final == self.capacity - 1) or (
            self.init == self.final + 1
        )

    def __is_empty_deque(self):
        return self.init == -1

    def add_start(self, value):
        if self.__is_fulled_deque():
            exit("Deque is fulled")

        if self.init == -1:
            self.init = 0
            self.final = 0
        elif self.init == 0:
            self.init = self.capacity - 1
        else:
            self.init -= 1
        self.values[self.init] = value
