lista = []

try:
    lista.append(float(input("Digite um numero:")))
    lista.append(float(input("Digite outro numero:")))
    divisao = lista[0] / lista[1]
except ValueError:
    print("Valor invalido")
except ZeroDivisionError:
    print("Valores nao podem ser dividos por zero")
except IndexError:
    print("Error indices invalidos")
except KeyboardInterrupt:
    print("Execucao interrompida")
else:
    print(f"Valor da divisao: {divisao}")
