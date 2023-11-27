import Funcion 

# Lista para almacenar los desarrolladores en memoria "Json"
listDS = Funcion.JsonDesarrolladores()

while True:
    try: 
        Funcion.menu()
        menu_option = int(input("Seleccione una opción: "))
        if menu_option == 1:
            Funcion.Nuevo_Usuario()
        
        elif menu_option == 2:
            Funcion.Ver_desarrolladores()
        elif menu_option == 3:
            Funcion.Modificar_Usuario()
        elif menu_option == 4:
            Funcion.Dev_Eliminar()
        elif menu_option == 5:
            print("Saliendo del programa.")
            break
        else:
            print()
            print("Opcion Invalida, Por Favor Ingrese La Opcion, De Acuerdo Al Menu Brindado: ")
          
    except ValueError:
        print()
        print("Valor no válida. Inténtelo de nuevo.")
    break