class SalaJuegos(object):
    def __init__(self):
        self.edad = 0
        self.precio = 0

    def leer(self):
        self.edad = int(input("Ingrese la edad del cliente: "))

    def calcular(self):
        if self.edad < 4:
            self.precio = 0

        elif self.edad <= 18:
            self.precio = 5

        else:
            self.precio = 10

    def imprimir(self):
        print("Edad del cliente:", self.edad)

        if self.precio == 0:
            print("Entrada gratis")
        else:
            print("Precio de la entrada:", self.precio, "€")

