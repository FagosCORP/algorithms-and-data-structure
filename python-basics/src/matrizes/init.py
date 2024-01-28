import numpy as np

# definindo linhas e colunas
# definindo uma matriz de duas linhas e tres colunas
#
####### colunas[0]    \     [1]
# ------------------------------
#
# 0 - linhas [2]    \     [4]
# 1 - linhas [3]    \     [5]
# 2 - linhas [1]    \     [7]
#
matriz = np.array([[2, 3, 1], [4, 5, 7]])

# Ver o corpo da matriz
# linhas e colunas
matriz.shape
soma = 0
for i in matriz.shape[0]:
    print(matriz[i])

    for j in range(matriz.shape[1]):
        print(matriz[i][j])


cont = 4
lista = []
soma = 0
while cont >= 0:
    print("Digite um numero")
    value = 1
    lista.append(value)
    soma += value
    cont -= 1

np.array(lista).sum()

dicionario = {"portugues": 10, "matematica": 9}
soma = 0

for nota in dicionario.values():
    soma += nota

nota = soma / len(dicionario.values())
