class Dosnum_divicion(object):
    def __init__(self):
        self.num1=0
        self.num2=0
        self.divicion=0

    def leer_datos(self):
        self.num1=int(input("Ingrese el primer numero: "))
        self.num2=int(input("Ingrese el segundo numero: "))

    def calcular_divicion(self):
        if self.num2!=0:
            self.divicion=self.num1/self.num2
        else:
            print("No se puede dividir por cero")

    def imprimir_divicion(self):
        if self.num2!=0:
            print(f"La divicion de {self.num1} entre {self.num2} es: {self.divicion}")  