import numpy as np


class QueuePriority:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.number_elements = 0
        self.values = np.empty(capacity, dtype=int)

    def __is_queue_empty(self):
        return self.number_elements == 0

    def __is_queue_fulled(self):
        return self.number_elements == self.capacity

    def add(self, value):
        if self.__is_queue_fulled():
            exit("Queue is fulled")

        if self.__is_queue_empty():
            self.values[self.number_elements] = value
            self.number_elements += 1
        else:
            x = self.number_elements - 1
            while x >= 0:
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                else:
                    break
                x -= 1
            self.values[x + 1] = value
            self.number_elements += 1

    def remove(self):
        if self.__is_queue_empty():
            exit("Queue is empty")
        value = self.values[self.number_elements - 1]
        self.number_elements -= 1
        return value

    def initial_value(self):
        if self.__is_queue_empty():
            return -1

        return self.values[self.number_elements - 1]
