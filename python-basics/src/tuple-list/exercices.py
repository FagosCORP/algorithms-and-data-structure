tupla = (
    "Homo sapiens",
    "familiares",
)

tupla[0]
tupla[1]

# Posição do index

tupla.index("Homo sapiens")

for element in tupla:
    print(element)


# Listas

lista1 = ["Homo sapiens", "familiares"]

lista2 = ["Homo sapiens", "familiares"]

lista3 = lista1 + lista2

# Posição
lista1[3]

lista3[0:2]

lista3.append("gorila")
lista3.remove("gorila")

del lista1

for item in lista3:
    print(item)
