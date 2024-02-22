import numpy as np

# Regrinhas de se lembrar
# A ultima_posicao sempre começa negativa para auxiliar nas comparaçoes se existem valores
# E tambem para saber em qual realmente e aultima ultima_posicao contando com os indices no vetor
# A ultima_posicao comeca sempre no menos um
# Logo a alocacao no vetor ele sempre comeca no 0 pensando isso na linha 30 ele sempre faz a inserçoes
# De maneira certa
# Pois se caso ele nem entra no while por causa do valor da ultima_posicao ser menor que o valor da posicao
# E se entrar lembre-se o valor guardado na ultima_posicao corresponde a indices existentes nao numero de itens


class VetorOrdenado:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            exit("O vetor esta vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i])

    def insere(self, valor):

        if self.capacidade - 1 == self.ultima_posicao:
            exit("O vetor esta cheio.")

        posicao = 0
        while posicao <= self.ultima_posicao:
            posicao += 1
            if self.valores[posicao] > valor:
                break

        # eu vou ter que ir jogando todos do dez ate o 5 para frente
        # pois vou ter que inserir um no lugar do 5
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # Voce sempre vai quebrar os dados nunca utilizar a base de dados originais
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)

            # Se achou de primeira
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não encontrou
            elif limite_inferior > limite_superior:
                return -1
            # Se não encontrou no limite vamos ver se e menor
            # Ou maior e definir os limites de buscas de indices
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1
