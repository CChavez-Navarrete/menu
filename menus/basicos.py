from clases.basicos.ejercicio1 import Recta
from clases.basicos.ejercicio2 import cordenadas
from clases.basicos.ejercicio3 import Fx_ecuacion
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
    def ejecutar(self):
        while self.opcion!=4:
            self.mostrar_menu_basicos()
            self.leer_ejecutar_opcion()