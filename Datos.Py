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
        Funcion.Modificar_Usuario()
        pass
    elif menu_option == 4:
        print("Saliendo del programa.")
try:
    pass
except ValueError:
    print("Opción no válida. Inténtelo de nuevo.")