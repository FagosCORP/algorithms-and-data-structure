# Operadores logicos

verdadeiro = True
falso = False

verdadeiro & falso
verdadeiro and falso

verdadeiro or falso
verdadeiro | falso

not verdadeiro

# condicionais
if verdadeiro:
    print(verdadeiro)
else:
    print(falso)
    if verdadeiro & falso:
        print(verdadeiro & falso)
    else:
        print(not falso)
        print(not verdadeiro)
