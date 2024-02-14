# Como comparar algoritmos?
# Comparação objetiva entre algoritmos.
# Considera as diferenças de linguagem, poder de processamento e sistema operacional.
# O quanto a complexidade do algoritmos aumenta de acordo com a entrada.


# Função 1 O(n)
# possui ao total 11 passos mas pode variar conforme o parametro
# O big O e O (n)
def soma1(n):
    soma = 0
    for numero in range(n + 1):
        soma += numero

    return soma


# Tempo de execução da função
# %timeit soma1(10)

# Função 2


# possui apenas 3 passos.
# primeiro soma o numero + 1
# logo em seguida o multiplica
# Divide o valor para se tratar de uma soma
# Numero fixo de passos
# Big O(3)
def soma2(n):
    return (n * (n + 1)) / 2


# %timeit soma2(10)
