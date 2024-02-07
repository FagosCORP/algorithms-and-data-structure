# Agrupamento de objeto similares que possuem o mesmo atributos e metodos
# Molde de bonecos de gesso
# Define o formato e tamanho
# O molde e sempre o mesmo mas pode possuir caracteristicas diferentes (cor, tamanho e etc)
# Respeitando a estrutura base do molde
# Molde =>  classe
# Objeto => variaveis que voce pode gerar com a classe
# caracteristicas do objetos => (atributos)
#  Açoes são => (metodos do objeto)


class Aluno:
    def __init__(self, nome, nota1, nota2) -> None:
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self) -> int:
        return self.nota1 + self.nota2 / 2
