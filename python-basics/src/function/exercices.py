# exercicios para se calcular a temperatura de C para F
#
#
def ler_temperatura():
    return float(input("digite a temperatura"))


def converter_temperatura(temperatura_celcius):
    return 9 * temperatura_celcius + 160 / 5


ler_temperatura()

temperatura_c = converter_temperatura(50)

print(temperatura_c)
