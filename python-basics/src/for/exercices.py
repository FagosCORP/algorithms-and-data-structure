for numero in range(3, 10):
    print(numero)

for numero in range(10, 3):
    print(numero)

# While repetição
numero = 1

while numero < 1:
    print("verdadeiro")
    numero -= 1

soma = 0
while numero < 6:
    soma += numero
    numero += 1

numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Digite um numero:"))


notas = [10, 20, 30, 40, 50]
tamanhoArray = len(notas)
percorrer = 1
while tamanhoArray <= percorrer:
    soma += notas[percorrer]
    if tamanhoArray == percorrer:
        media = soma / tamanhoArray


for numero in range(0, 11):
    for vezes in range(0, 11):
        print(numero, vezes, numero * vezes)
