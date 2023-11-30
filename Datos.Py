import Funcion 
import os # libreria de sistema imperativo que uso para el metodo de cls = clear en consola
limpiar_pantalla = lambda: os.system('cls') # asigna el metodo de clear de system a una funcion llamada limpiar pantalla

# Lista para almacenar los desarrolladores en memoria "Json"
listDS = Funcion.JsonDesarrolladores()

while True:
    try:
        limpiar_pantalla() 
        Funcion.menu()
        menu_option = int(input("Seleccione una opción: "))
        match menu_option:
            case 1:
                Funcion.Nuevo_Usuario()
        
            case  2:
                Funcion.Ver_desarrolladores()
            case  3:
                Funcion.Modificar_Usuario()
            case  4:
                Funcion.Dev_Eliminar()
            case  5:
                Funcion.Busqueda_Por_Desarrallador()
            case  6:
                print("Saliendo del programa.")
                break
            case _ :
                print("\nOpcion Invalida, Por Favor Ingrese La Opcion, De Acuerdo Al Menu Brindado: ")
        print("\n\nPresione cualquier tecla para continuar")
        input()
          
    except ValueError:
        print("\nValor no válida. Inténtelo de nuevo.")
    