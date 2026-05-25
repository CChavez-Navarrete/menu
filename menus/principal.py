from menus.basicos import basicos

class principal(object):
    def __init__(self):
        self.opcion=0
        
    def mostrar_menu(self):
        print("-----MENU PRINCIPAL-----")
        print("1. basicos")
        print("2. condicionales")
        print("3. ciclos")
        print("4. salir")
        
    def leer_ejecutar_opcion(self):
        self.opcion = int (input("seleccione una opcion"))
        match self.opcion:
            case 1:
                Basicos = basicos()
                Basicos.ejecutar()
                
    def ejecutar(self):
        while self.opcion != 4:
            self.mostrar_menu()
            self.leer_ejecutar_opcion()
            
    
                    
                    