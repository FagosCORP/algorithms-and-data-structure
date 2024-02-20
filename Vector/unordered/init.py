# Controlar quais jogadores estão no campo
# (Estrutura de dados)
#
# Ações que podem ser executadas
#
# Inserir um jogador na estrutura quando ele estiver em campo.
# Verificar se um jogador esta presente, pesquisando o numero do jogador na estrutura.
# Remover quando um jogador for para o descanso ou casa.
# So vai remover o valor duplicado da ultima_posicao quando ocorrer uma inserção
# pois a ultima_posicao foi decrementada
#

import numpy as np


class Vetor:

    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("capacidade maxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        # busca linear posição por posição
        for index in range(self.valores + 1):
            if self.valores[index] == valor:
                return index
        return -1

    def excluir(self, valor):
        index = self.pesquisar(valor)
        if index == -1:
            return -1
        for i in range(index, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1


vetor = Vetor(10)
vetor.imprime()

# imprimir as posicões:
# E saber o numero de posições que estão cheias
#
