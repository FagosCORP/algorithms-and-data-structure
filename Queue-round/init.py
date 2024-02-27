import numpy as np


class QueueRound:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.init = 0
        self.final = -1
        self.number_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __is_stack_empty(self):
        return self.number_elements == 0

    def __is_stack_fulled(self):
        return self.number_elements == self.capacity

    def add(self, value):
        if self.__is_stack_fulled():
            exit("Stack is fulled")

        if self.final == self.capacity - 1:
            self.final = -1

        self.final += 1
        self.values[self.final] = value
        self.number_elements += 1

    def remove(self):
        if self.__is_stack_empty():
            exit("Stack is empty")

        temp = self.values[self.init]
        self.init += 1

        if self.init == self.capacity - 1:
            self.init = 0
        self.number_elements -= 1

        return temp

    def init_value(self):
        if self.__is_stack_empty():
            return -1
        return self.values[self.init]
