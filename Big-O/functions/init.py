# Funções Big - 0
# constant
# log (n) logarithmic
# n linear
# n^2 quadradic
# n^3 cubic
# exponential

from math import log
import numpy as np
import matplotlib.pyplot as plt

# Essa função gera numeros espaçados
# De um ate 10 gere 100 numeros espaçados
#
n = np.linspace(1, 10, 100)

labels = [
    "Constant",
    "Logarithmic",
    "Linear",
    "Log linear",
    "Quadratic",
    "Cubic",
    "Exponential",
]

# one constante tudo vira o mesmo numero
# log eles diminuem conforme o original
# linear se mantem mas coloca tudo no lugar novmente
# numero vezes a quantidade que possuem de funcoes 20 * n(items)
# numero de items quadrado
# numero de items ao cubo
# 2  ao cubo de (n)
#
big_o = [np.ones(n.shape()), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]
