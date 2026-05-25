import math

class Fx_ecuacion(object):
    def __init__(self, x=0, mu=0, sigma=0, euler=math.e, pi=math.pi):
        self.a = x
        self.b = mu
        self.c = sigma
        self.euler = euler
        self.pi = pi

    def leer_datos(self):
        self.a = float(input('x = '))
        self.b = float(input('mu = '))
        self.c = float(input('sigma = '))

    def calcular_fx(self):
        return math.sqrt(((self.a-self.b) / self.c) ** 2)

    def imprimir_fx(self):
        print(f'f({self.a}) = {self.calcular_fx()}')