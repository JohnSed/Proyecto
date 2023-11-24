import json

# Archivo JSON para almacenar los desarrolladores
json_filename = 'developers_data.json'

def load_developers_from_file():
    try:
        with open(json_filename, 'r') as file:
            developers = json.load(file)
        return [Developer(**dev) for dev in developers]
    except FileNotFoundError:
        return []

def save_developers_to_file(developers):
    with open(json_filename, 'w') as file:
        json.dump([dev.__dict__ for dev in developers], file)

class Developer:
    def __init__(self, name, skills, years_of_experience, level, id=None):
        self.id = id if id is not None else len(developers_list) + 1
        self.name = name
        self.skills = skills
        self.years_of_experience = years_of_experience
        self.level = level

# Lista para almacenar los desarrolladores en memoria
developers_list = load_developers_from_file()

def display_menu():
    print("1. Agregar Desarrollador")
    print("2. Mostrar Desarrolladores")
    print("3. Clasificar Desarrolladores por Habilidades y Niveles")
    print("4. Imprimir Contenido del Archivo JSON")
    print("5. Salir")

def add_developer():
    name = input("Ingrese el nombre del desarrollador: ")
    skills = input("Ingrese las habilidades del desarrollador (separadas por coma): ")
    years_of_experience = int(input("Ingrese los años de experiencia del desarrollador: "))
    level = input("Ingrese el nivel del desarrollador: ")

    developer = Developer(name, skills, years_of_experience, level)
    developers_list.append(developer)
    save_developers_to_file(developers_list)
    print(f"Desarrollador {name} agregado exitosamente.")

def show_developers():
    print("\nLista de Desarrolladores:")
    for developer in developers_list:
        print(f"ID: {developer.id}, Nombre: {developer.name}, Habilidades: {developer.skills}, "
              f"Años de Experiencia: {developer.years_of_experience}, Nivel: {developer.level}")
    print()

def classify_developers():
    skills_to_level = {}

    for developer in developers_list:
        skills = developer.skills.split(', ')
        for skill in skills:
            if skill not in skills_to_level:
                skills_to_level[skill] = {'Principiante': 0, 'Intermedio': 0, 'Avanzado': 0}
            skills_to_level[skill][developer.level] += 1

    print("\nClasificación de Desarrolladores por Habilidades y Niveles:")
    for skill, levels in skills_to_level.items():
        print(f"\nHabilidad: {skill}")
        for level, count in levels.items():
            print(f"Nivel {level}: {count} desarrollador(es)")

def print_json_content():
    try:
        with open(json_filename, 'r') as file:
            content = json.load(file)
        print("\nContenido del Archivo JSON:")
        print(json.dumps(content, indent=2))
        print()
    except FileNotFoundError:
        print("El archivo JSON no existe.")

if __name__ == '__main__':
    while True:
        display_menu()
        option = input("Seleccione una opción: ")

        if option == '1':
            add_developer()
        elif option == '2':
            show_developers()
        elif option == '3':
            classify_developers()
        elif option == '4':
            print_json_content()
        elif option == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

