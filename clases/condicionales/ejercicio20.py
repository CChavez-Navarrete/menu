class IMC(object):
    def __init__(self):
        self.peso = 0
        self.estatura = 0
        self.imc = 0
        self.resultado = ""

    def leer(self):
        self.peso = float(input("¿Cuál es tu peso en kg? "))
        self.estatura = float(input("¿Cuál es tu estatura en metros? "))

    def calcular(self):
        self.imc = round(self.peso / (self.estatura ** 2), 2)

        if self.imc < 18.5:
            self.resultado = "PESO BAJO"

        elif self.imc < 24.9:
            self.resultado = "NORMAL"

        elif self.imc < 29.9:
            self.resultado = "SOBREPESO"

        else:
            self.resultado = "OBESIDAD"

    def imprimir(self):
        print("Tu IMC es:", self.imc)
        print("Clasificación:", self.resultado)


