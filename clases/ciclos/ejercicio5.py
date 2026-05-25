import math
class sumatorias(object):
  def __init__(self):
    self.n = 0
    self.serie = 0

def leer_datos(self):
      self.n = int(input("Ingrese el valor de n: "))

def calcularSerie(self):
      self.serie = 0
      for i in range(1, self.n + 1):
        self.serie += 1/math.sqrt((2*i+1)**2)

def imprimirSerie(self):
      print(f"El valor de la serie es: {self.serie}")