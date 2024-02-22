import numpy as np


class Pilha:
    def __init__(self, capacidade) -> None:
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.chararray(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo >= self.__capacidade - 1:
            return True
        return False

    def pilha_vazia(self):
        if self.__topo <= -1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            exit("Pilha esta cheia")
        self.__topo += 1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        desempilhado = self.__valores[self.__topo]
        if self.pilha_vazia():
            return -1
        self.__topo -= 1
        return desempilhado

    def ver_topo(self):
        if self.pilha_vazia():
            return -1
        return self.__valores[self.__topo]
