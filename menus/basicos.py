from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import cordenadas
from clases.basicos.ejercicio3 import Fx_ecuacion
from clases.ciclos.ejercicio5 import Sumatorias
from clases.condicionales.ejercicio14 import NumEntero_numPrimo
from clases.condicionales.ejercicio17 import Dosnum_divicion
from clases.condicionales.ejercicio18 import Persona
from clases.condicionales.ejercicio20 import IMC
from clases.condicionales.ejercicio24 import SalaJuegos
from clases.condicionales.ejercicio4 import Circunferencia

class basicos(object):
    def __init__(self):
        self.opcion = 0
        
    def mostrar_menu_basicos(self):
        print("-----MENU BASICOS-----")
        print("1, pendiente de una recta")
        print("2. distancia entre dos puntos")
        print("3.fx ecuacion")
        print("4. volver al menu")
        
        
    def leer_ejecutar_opcion(self):
        self.opcion =int(input("seleccionar una opcion"))
        match self.opcion:
            case 1:
                figura = Recta(0,0,0,0)
                figura.leer_datos()
                figura.calcular_pendiente()
                figura.imprimir_pendiente()
            case 2:
                puntos = cordenadas()
                puntos.leer_datos()
                puntos.calcular_distancia()
                puntos.imprimir_distancia()
            case 3:
                ecuacion = Fx_ecuacion()
                ecuacion.leer_datos()
                ecuacion.calcular_fx()
                ecuacion.imprimir_fx() 
            case 4:
                radio= Circunferencia(0,0,0)
                radio.leer_datos()
                radio.calcular_punto(radio.x2, radio.y2)
                radio.imprimir_punto()
            case 5:
                radio= Sumatorias()
                radio.leer_datos()
                radio.calcular_sumatoria()
                radio.imprimir_sumatoria()
            case 6:
            case 14:
                numero = NumEntero_numPrimo()
                numero.leer_datos()
                numero.calcular_primo()
                numero.imprimir_primo()
            case 17:
                divicion = Dosnum_divicion()
                divicion.leer_datos()
                divicion.calcular_divicion()
                divicion.imprimir_divicion()
            case 18:
                grupo = Persona()
                grupo.leer()
                grupo.calcular()
                grupo.imprimir()
            case 20:
                persona = IMC()
                persona.leer()
                persona.calcular()
                persona.imprimir()
            case 24:
                cliente = SalaJuegos()
                cliente.leer()
                cliente.calcular()
                cliente.imprimir()

    def ejecutar(self):
        while self.opcion!=4:
            self.mostrar_menu_basicos()
            self.leer_ejecutar_opcion()