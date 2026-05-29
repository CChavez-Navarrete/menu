class Persona(object):
    def __init__(self):
        self.nombre = ""
        self.sexo = ""
        self.grupo = ""

    def leer(self):
        self.nombre = input("Ingrese su nombre: ")
        self.sexo = input("Ingrese su sexo (M/F): ").upper()

    def calcular(self):
        match self.sexo:
            case "M":
                if self.nombre[0].upper() < "N":
                    self.grupo = "Grupo A"
                else:
                    self.grupo = "Grupo B"

            case "F":
                if self.nombre[0].upper() < "M":
                    self.grupo = "Grupo A"
                else:
                    self.grupo = "Grupo B"

            case _:
                self.grupo = "Sexo no válido"

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Sexo:", self.sexo)
        print("Resultado:", self.grupo)


