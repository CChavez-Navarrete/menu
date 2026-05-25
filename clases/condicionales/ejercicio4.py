class Circunferencia(object):
    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio
        
    def leer_datos(self):
        self.x = int(input("x centro: "))
        self.y = int(input("y centro: "))
        self.radio = int(input("radio: "))
        self.x2 = int(input("x punto: "))
        self.y2 = int(input("y punto: "))

    def calcular_punto(self, x2, y2):

        d = ((x2 - self.x) ** 2 + (y2 - self.y) ** 2) ** 0.5

        if d < self.radio:
            print("El punto está dentro de la circunferencia")
        elif d > self.radio:
            print("El punto está fuera de la circunferencia")
        else:
            print("El punto está sobre la circunferencia")

        print(f"d = {d}")
        
    def imprimir_punto(self):
        print(f"Centro: ({self.x}, {self.y}), Radio: {self.radio}")
