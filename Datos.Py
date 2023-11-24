import Funcion 

# Lista para almacenar los desarrolladores en memoria "Json"
listDS = Funcion.JsonDesarrolladores()

menu_option = 0
while menu_option != 4:
    Funcion.menu()
    menu_option = int(input("Seleccione una opción: "))

    if menu_option == 1:
        Funcion.Nuevo_Usuario()
        
    elif menu_option == 2:
        Funcion.Ver_desarrolladores()
    elif menu_option == 3:
        # Opción para imprimir el contenido del archivo JSON
        # (puedes implementar esta función si lo deseas)
        pass
    elif menu_option == 4:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")