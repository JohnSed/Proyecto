# script_agregar_desarrollador.py
from Funciones import create_developer, get_developers

# Crear un desarrollador
developer_data = {
    'name': 'Nombre del Desarrollador',
    'skills': 'Habilidades del Desarrollador',
    'years_of_experience': 3,
    'level': 'Intermedio'
}
nuevo_desarrollador = create_developer(developer_data)

# Obtener la lista de desarrolladores
lista_desarrolladores = get_developers()
print(lista_desarrolladores)