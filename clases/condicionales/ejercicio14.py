class NumEntero_numPrimo(object):
    def __init__(self):
        self.num=0
        self.cont=0

    def leer_datos(self):
        self.num=int(input("Ingrese un numero entero: "))

    def calcular_primo(self):
        for i in range(1,self.num+1):
            if self.num%i==0:
                self.cont+=1

    def imprimir_primo(self):
        if self.cont==2:
            print(f"El numero {self.num} es primo")
        else:
            print(f"El numero {self.num} no es primo")