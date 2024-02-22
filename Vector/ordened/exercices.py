import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade: int) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor esta vazio")
            exit()
        for i in range(self.ultima_posicao + 1):
            print(self.valores[i])

    def inserir(self, valor):
        # verifico se ja esta lotado
        if self.ultima_posicao == self.capacidade - 1:
            print("O vetor ja esta cheio")
            exit()

        # aqui eu to pegando a posicao que vai ser inserido o novo elemento
        # verifico se esta antes ou depois
        # aqui e para ordenar
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            # caso ele nao achar maior vai inserir na ultima posicao
            # por que aconteceu dele inserir na nova ultima mais um
            if i == self.ultima_posicao:
                posicao = i + 1

        ### Acabamos de achar logo em seguida
        # logo em seguida preciso realizar o seguinte agora eu vou ir da ultima_posicao ate a posicao que eu vou inserir para remanejar
        # eu aumentei o tamanho do array e passei o ultimo valor para ele na primeira interação
        # todos ficaram um para frente ate chegar naquele  valor
        #
        # logo em seguida ate chegar na posicao que eu tenho que inserir que agora ficou duplicada tanto na posicao dela quanto na posicao a frente
        # por fim eu preciso agora somente inserir na posicao onde o valor vai ficar para remover a duplicidade e ajustar
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao != -1:
            x = self.ultima_posicao
            while x >= posicao:
                self.valores[x + 1] = self.valores[x]
                x -= 1

            self.ultima_posicao -= 1
        return -1


vetor = VetorOrdenado(10)
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.excluir(3)
vetor.imprime()
