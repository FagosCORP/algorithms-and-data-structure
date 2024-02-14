# Primeiramente você cria a função logo em seguida
# Se for possivel fazer o calculo do  Big - O
# O (n)


# Estamos criando uma lista com 1001 elementos
# %timeit lista1001()
# rodando temos um tmepo de microsegundos
# O (n)
#
def lista1001():
    lista = []
    for valor in range(1000):
        lista.append(valor)
    return lista


lista1001()


# fica de forma mais entendivel não roda muitas logo o log(n)
#
# rodando temos um tmepo de nanosegundos
# O (1)
def listaUpdated1001():
    return range(1001)
