idade = 13

if idade >= 0 & idade <= 12:
    print("criança")
elif idade > 12 & idade <= 18:
    print("adolescente")
elif idade > 18:
    print("adulto")
else:
    print("Numero nao reconhecido.")


# Calculando a media.
valor1 = 10
valor2 = 30
valor3 = 5

media = valor1 + valor2 + valor3 / 3
if media >= 0.0 and media <= 4.0:
    print("Aluno reprovado")
elif media >= 4.1 and media <= 6.0:
    print("Precisa fazer o exame")
    exame = 6
    if exame >= 6.0:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("Aprovado!")
