# funcoes
#
# Sem parametros, sem retorno mas com parametros e função que possui parametros e retorno.
#
def funcoes():
    print("escrevendo funcoes aninonimas")


funcoes()


def funcParam(nome: str):
    print(nome)


funcParam("ryan")


def funcReturn(nome: str):
    return nome


returnVar = funcReturn("ryan")


def calcula_energia_gravitaciona(e, g, h, m):
    return g * m * h * e


calcula_energia_gravitaciona(90, 30, 12, 12)

help(calcula_energia_gravitaciona)
