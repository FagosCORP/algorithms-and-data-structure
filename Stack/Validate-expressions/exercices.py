from Stack.Stack import Stack
import numpy as np


class Validate_Expressions:
    def __init__(self, expression) -> None:
        self.__expression = expression
        self.__valid_expression_open = set(["{", "[", "("])
        self.__valid_expression_close = set(["}", "]", ")"])
        self.stack = Stack(len(self.__expression))

    def acc_expression(self) -> None:
        for i in range(len(self.__expression) + 1):

            if self.__expression[i] in self.__valid_expression_open:
                self.stack.push(self.__expression[i])

            elif self.__expression in self.__valid_expression_close:

                char_open = self.stack.remove()
                char_close = self.__expression[i]
                self.is_valid_expression(char_open, char_close, i)

    def is_valid_expression(self, char_open, char_close, index) -> bool:
        mapping = {"{": "}", "[": "]", "(": ")"}

        if char_open in mapping and mapping[char_open] != char_close:
            print("Error in line", index)
            return False

        return True
