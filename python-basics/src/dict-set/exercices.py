# Dicionarios

dicionario = {"key": "value", "key": "value"}

# Acessar um elemento

dicionario["key"]

dicionario["novo"] = "value"

del (dicionario)["key"]

# acessar valores e chaves:
dicionario.items()


dicionario.keys()

dicionario.values()
# Adicionar novos valores

dicionario.update(dicionario)

for key, value in dicionario.items():
    print(key, value)


# Conjuntos
# Conjuntos na matematica
# elementos unicos
conjuntos = {"proteina", "acidos", "testosterona"}
conjuntos2 = {"proteina", "acidos", "testosterona"}

set(conjuntos)
set(conjuntos2)

conjuntos2.difference(conjuntos)
conjuntos3 = conjuntos.intersection(conjuntos2)
