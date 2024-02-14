# Constant O (1)
# ou 0 (quantas vezes e chamada dentro da função)
lista = [1, 2, 3, 4, 5, 6]


def constant_func(n):
    print(n[0])


constant_func(lista)


# Linear - O (n)
# Esta se executando conforme o tamanho do que foi enviado ao parametro
# Depende do Valor de N
# Ai ele vai aumentar conforme o numero de N definido
#
def linear_func(n):
    for value in n:
        print(value)


linear_func(lista)
