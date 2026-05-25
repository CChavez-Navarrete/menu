import math

class cordenadas(object):
    def _init_(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def leer_datos(self):
        self.x1 = float(input('X1 = '))
        self.y1 = float(input('Y1 = '))
        self.x2 = float(input('X2 = '))
        self.y2 = float(input('Y2 = '))

    def calcular_distancia(self):
        return math.sqrt((self.x2 - self.x1)*2 + (self.y2 - self.y1)*2)

    def imprimir_distancia(self):
        print(f'd = {self.calcular_distancia()}')