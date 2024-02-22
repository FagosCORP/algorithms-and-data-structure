import numpy as np
from Pilha import Pilha


class Validate_Expressions:
    def __init__(self, expression) -> None:
        self.__expression = expression
        self.__valid_expression_open = set(["{", "[", "("])
        self.__valid_expression_close = set(["}", "]", ")"])
        self.pilha = Pilha(len(self.__expression))

    def acc_expression(self):
        for i in range(len(self.__expression) + 1):

            if self.__expression[i] in self.__valid_expression_open:
                self.pilha.empilhar(self.__expression[i])

            elif self.__expression in self.__valid_expression_close:

                char_open = self.pilha.desempilhar()
                char_close = self.__expression[i]
                self.isValidExpression(char_open, char_close, i)

    def isValidExpression(self, char_open, char_close, posicao):
        mapping = {"{": "}", "[": "]", "(": ")"}

        if char_open in mapping and mapping[char_open] != char_close:
            print("Erro na posição", posicao)
            return False

        return True
