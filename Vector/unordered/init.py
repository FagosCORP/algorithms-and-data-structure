# Controlar quais jogadores estão no campo
# (Estrutura de dados)
#
# Ações que podem ser executadas
#
# Inserir um jogador na estrutura quando ele estiver em campo.
# Verificar se um jogador esta presente, pesquisando o numero do jogador na estrutura.
# Remover quando um jogador for para o descanso ou casa.

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


vetor = Vetor(10)
vetor.imprime()
