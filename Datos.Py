import Funcion 

# Lista para almacenar los desarrolladores en memoria "Json"
listDS = Funcion.JsonDesarrolladores()

while True:
    try: 
        Funcion.menu()
        menu_option = int(input("Seleccione una opción: "))
        print()

        if menu_option == 1:
            Funcion.Nuevo_Usuario()
        
        elif menu_option == 2:
            Funcion.Ver_desarrolladores()
        elif menu_option == 3:
            Funcion.Modificar_Usuario()
            
        elif menu_option == 4:
            print("Saliendo del programa.")
            break
        elif menu_option == 5:
            Funcion.eliminar_usuario()
        else:
            print()
            print("Opcion Invalida, Por Favor Ingrese La Opcion, De Acuerdo Al Menu Brindado: ")
            print()
    except ValueError:
        print()
        print("Opción no válida. Inténtelo de nuevo.")
        continue