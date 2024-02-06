import re

frase = "Ola meu numero de telefone é (31)00000-0000"

frase1 = "A placa de carro que eu anotei foi FRT-1998"

frase2 = "Entre em contato com e-mail teste@teste.com"

# Função match
# dando escape pois eu preciso que encontre
# /( -> primeiro selecionado para escape
# /d -> quantidade de digitos dentro são dois digitos
# /) -> fechando passando um caractere de espaço
# /d{4-5} entre 4 ou 5 digitos
# - ponto para ser utilizado como separador
# /d{4} passando que apos o digito vai ser utilizado 4 digitos
#
rgTelefone = "\(\d{2}\)\d{4,5}-\d{4}"
re.search(rgTelefone, frase)

# [] buscando caracteres de a-z ou A-Z
# {3} quantidade de caracteres procuradas
# - separador pelo oque eu estou buscando
# /d buscando digitos numericos
# {4} quatro digitos buscados
#
rgPlaca = "[A-Za-z]{3}-\d{4}"
re.search(rgPlaca, frase1)

# /w+ buscando uma quantidade de caracteres alfanumericos
# @ separador para o e-mail validado
#
rgEmail = "\w+@\w+\.[a-z]{2,20}"
re.search(rgEmail, frase2)

# Match verifica se esta no inicio da frase
re.match(rgEmail, frase2)

# findAll
re.findall(rgEmail, frase2)

# /W
# ? aparece https 0 ou uma vez
# [a-zA-z0-9./] pode aparecer numero ou letras e depois o (.)
# + uma ou mais vezes
fraseUrl = "https://google.com.br"
rgUrl = "https?//[a-zA-z0-9./]+"
re.findall(rgUrl, fraseUrl)
