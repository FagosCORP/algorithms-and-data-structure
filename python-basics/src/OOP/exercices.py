class Triangulo:
    # definindo o construtor para classe criada.
    # particularidade do python que precisa ser passado
    def __init__(self, lado1, lado2, lado3, base, altura) -> None:
        # estou definindo as propiedades
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            print("Certamente não e um triangulo.")
        elif (
            self.lado3
            == self.lado2 | self.lado1
            == self.lado2 | self.lado1
            == self.lado3
        ):
            print("Triangulo isósceles")
        else:
            print("Outro tipo de triangulo")


triangulo = Triangulo(1, 2, 3, 10, 20)
triangulo.lado1
triangulo.lado2
triangulo.lado3
triangulo.tipo()

triangulo1 = Triangulo(31, 2, 10, 10, 20)
triangulo1.lado1
triangulo1.lado2
triangulo1.lado3
triangulo1.tipo()
