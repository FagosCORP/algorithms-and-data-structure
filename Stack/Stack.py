import numpy as np


class Stack:
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__final_stack = -1
        self.__values = np.chararray(self.__capacity, dtype=int)

    def __stack_is_fulled(self):
        if self.__final_stack >= self.__capacity - 1:
            return True
        return False

    def stack_is_empty(self):
        if self.__final_stack <= -1:
            return True
        return False

    def push(self, value):
        if self.__stack_is_fulled():
            exit("Stack is fulled")
        self.__final_stack += 1
        self.__values[self.__final_stack] = value

    def remove(self):
        removed = self.__values[self.__final_stack]
        if self.stack_is_empty():
            return -1
        self.__final_stack -= 1
        return removed

    def show_final_stack(self):
        if self.stack_is_empty():
            return -1
        return self.__values[self.__final_stack]
