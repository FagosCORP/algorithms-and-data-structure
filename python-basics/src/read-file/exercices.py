with open("file.txt") as text:
    for linha in text:
        print(linha)

with open("file.txt") as text:
    r = text.readlines()
    text.readline(1)
