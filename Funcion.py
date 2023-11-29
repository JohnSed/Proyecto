import json
#Usaremos Json Para Guardar Los Datos.
json_Developers= "DataBaseDevelopers.json"

#Abrir Archivo Json
def JsonDesarrolladores():
    try:
        with open(json_Developers, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                Empleado_Desarrollador = json.loads(contenido)
                return [Empleado(Nombre=dev['Nombre'], Skill=dev['Skill'], añ_exp=dev['añ_exp'], id=dev['id'], Level=dev.get('Level', None)) for dev in Empleado_Desarrollador]
            else:
                return []  # Devuelve Lista Vacia
    except FileNotFoundError:
        return []  # Devuelve Lista Vacia
    except json.decoder.JSONDecodeError:
        return []  # Devuelve Lista Vacia

#Guardar Informacion En Json
def SaveDesarrolladores( Desarrollador):
    with open(json_Developers, "w",encoding="utf-8") as archivo1:
        data = [{"id": dev.id, "Nombre": dev.Nombre, "Skill": dev.Skill, "añ_exp": dev.añ_exp,"Level":dev.Level} for dev in Desarrollador]
        json.dump(data, archivo1,ensure_ascii=False)

#Informacion  Empleado.
class Empleado():
    def __init__(self,Nombre,Skill,añ_exp,Level, id=None) :
        #En Caso De Que El Id No Se Encuentre Registrado Lo Creamos En Else.
        if id is not None:
            self.id=id
        else:
            self.id=id
        self.Nombre= Nombre
        self.Skill= [] if Skill is None else Skill if isinstance(Skill, list) else [Skill] # Verificar si la variable Skill es una instancia de la clase list.
        self.añ_exp=añ_exp
        self.Level=Level

# clasificar a los desarrolladores

        
class Habilidades_Programacion:
    def __init__(self, lenguajes, Añ_Exp, Level):
        self.Level = Level
        self.lenguajes = lenguajes
        self.Añ_Exp = Añ_Exp
        self.Lenguajes_Trainer = ["CSS","HTML"]
        self.Lenguajes_Junior = ["JAVASCRIPT","PYTHON"] 
        self.Lenguaje_Middle = ["JAVA","C#","PHP"] 
        self.Lenguaje_Senior = ['RUBY','GO','SWIFT'] 
        self.Lenguaje_Lead = ['KOTLIN','RUST','TYPESCRIPT'] 


        self.Añ_Junior = 1
        self.Añ_Middel = 2
        self.Añ_Senior = 3
        self.Añ_Lead = 4

    def Level_Dep(self, Empleado):

        if any(hab in Empleado.Skill for hab in self.Lenguaje_Lead) and Empleado.añ_exp >= self.Añ_Lead and Empleado.añ_exp <= self.Añ_Lead+Empleado.añ_exp:
            return "Lead"
        elif any(hab in Empleado.Skill for hab in self.Lenguaje_Senior) and Empleado.añ_exp  >= self.Añ_Senior and Empleado.añ_exp <= self.Añ_Senior+Empleado.añ_exp:
            return "Senior"
        elif any(hab in Empleado.Skill for hab in self.Lenguaje_Middle) and Empleado.añ_exp >=  self.Añ_Middel and Empleado.añ_exp <= self.Añ_Middel+Empleado.añ_exp:
            return "Middle"
        elif any(hab in Empleado.Skill for hab in self.Lenguajes_Junior) and Empleado.añ_exp >=  self.Añ_Junior and Empleado.añ_exp <= self.Añ_Junior+Empleado.añ_exp:
            return "Junior"
        elif all(hab in Empleado.Skill for hab in self.Lenguajes_Trainer) :
            return "Trainer"
            
        else:
            print("No se pudo Identificar Lenguaje De Acuerdo A La Base De Datos. Por favor, Verificar o Actualizar La Lista De Habilidades Predeterminadas.")
            return None
        
#Lista para almacenar los desarrolladores en memoria "Json"
listDS = JsonDesarrolladores()

#Menu
def  menu():
    print("1. Agregar Desarrollador")
    print("2. Mostrar Desarrolladores")
    print("3. Modificar Desarrollador")
    print("4. Eliminar Desarrrolador: ")
    print("5. Busqueda Desarrollador Por Documento.")
    print("6. Salir")
    
    
#Imprimir Json
def Ver_desarrolladores():
    print("\nLista de Desarrolladores:")
    for Desarrolladores in listDS:
        print(f"ID: {Desarrolladores.id}, Nombre: {Desarrolladores.Nombre}, Habilidades: {Desarrolladores.Skill}, "
              f"Años de Experiencia: {Desarrolladores.añ_exp}",f"Nivel:{Desarrolladores.Level}")
    print()

#Agregar Desarrollador
def Nuevo_Usuario():
    id = int(input("Ingrese Numero De Cedula Del Empleado: "))
    # Verificar si el ID ya existe
    id_existente = any(dev.id == id for dev in listDS)

    if id_existente:
        print(f"El ID: {id}, Ingresado Ya Existe, Por Favor Verifique Documento")
    else:
        # Si el ID no existe, continuar con la entrada de otros datos
        Nombre = input("Ingrese Nombre Del Empleado: ")
        Skill = input("Ingrese Habilidades (Separadas En Coma): ")
        Skill=Skill.upper()
        Skill = Skill.split(',')
        Añ_Expe = float(input("Ingrese Su Experiencia En Años: "))

        # Crear la instancia de Empleado después de ingresar la información
        
        Desarrollador = Empleado(Nombre, Skill, Añ_Expe, None, id)  # Asegúrate de pasar el id correctamente
        Desarrollador.Level = Habilidades_Programacion(Desarrollador.Skill, Desarrollador.añ_exp, None).Level_Dep(Desarrollador)


        listDS.append(Desarrollador)
        SaveDesarrolladores(listDS)
        print(f"El Desarrollador {Nombre} ha sido agregado exitosamente.")

#Modificar Desarrollador

def Modificar_Usuario():
    Ver_desarrolladores()  # Mostrar La Lista De Desarrolladores

    id_modificar = int(input("Ingrese Id Del Desarrollador a Modificar: "))
    # Buscar el desarrollador por su ID
    desarrollador_a_modificar = next((dev for dev in listDS if dev.id == id_modificar), None)
    
    if desarrollador_a_modificar:
        # Nombre
        print(f"Modificacion El Desarrollador Con Id {desarrollador_a_modificar.id}:")
        print(f"Nombre actual: {desarrollador_a_modificar.Nombre}")
        nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para dejarlo sin cambios): ")
        desarrollador_a_modificar.Nombre = nuevo_nombre if nuevo_nombre else desarrollador_a_modificar.Nombre

        # Habilidades
        print(f"Habilidades actuales: {desarrollador_a_modificar.Skill}")
        nuevo_skill = input("Ingrese las nuevas habilidades (o presione Enter para dejarlas sin cambios): ")
        nuevo_skill=nuevo_skill.upper()
        if nuevo_skill:
            desarrollador_a_modificar.Skill.extend(nuevo_skill.split(','))  # Extender la lista de habilidades

        # Años Experiencia
        print(f"Años de experiencia actuales: {desarrollador_a_modificar.añ_exp}")
        nuevo_añ_exp = input("Ingrese los nuevos años de experiencia (o presione Enter para dejarlos sin cambios): ")
        desarrollador_a_modificar.añ_exp += float(nuevo_añ_exp) if nuevo_añ_exp else 0.0

        # Lógica de reclasificación
        desarrollador_a_modificar.Level = Habilidades_Programacion(desarrollador_a_modificar.Skill, desarrollador_a_modificar.añ_exp, None).Level_Dep(desarrollador_a_modificar)
        SaveDesarrolladores(listDS)

        print(f"Desarrollador con ID {desarrollador_a_modificar.id} modificado exitosamente.")
    else:
        print(f"No se encontró ningún desarrollador con ID {id_modificar}")
def Dev_Eliminar():
    global listDS
    Ver_desarrolladores()
    Id_Dev_str = input("Ingrese el número de cédula del desarrollador a eliminar: ")

    try:
        Id_Dev = int(Id_Dev_str)
    except ValueError:
        print("Por favor, ingrese el número de documento sin espacios ni puntos.")
        return  # Salir de la función si la entrada no es un entero válido

    # Verificar si hay algún desarrollador cuyo ID coincida con el ID de entrada
    desarrollador_a_eliminar = next((dev for dev in listDS if dev.id == Id_Dev), None)

    if desarrollador_a_eliminar:
        listDS.remove(desarrollador_a_eliminar)
        print(f"Desarrollador con ID {Id_Dev} eliminado exitosamente.")
    else:
        print(f"No se encontró un desarrollador con el ID {Id_Dev}.")

    SaveDesarrolladores(listDS)

def Busqueda_Por_Desarrallador():
    id_buscar = int(input("Ingrese Id Del Desarrollador a Verificar: "))
    # Buscar el desarrollador por su ID
    desarrollador_buscado = next((dev for dev in listDS if dev.id == id_buscar), None)

    if desarrollador_buscado is not None:
        print(f"Cedula: {desarrollador_buscado.id} - Nombre: {desarrollador_buscado.Nombre} - Habilidades: {desarrollador_buscado.Skill} - Años Experiencia: {desarrollador_buscado.añ_exp} - Nivel: {desarrollador_buscado.Level}")
        
 
    else:
        print("Desarrollador No Encontrado.")

       # Crear una instancia de Habilidades_Programacion dentro de la función
    
    habilidades_programacion = Habilidades_Programacion(None, None, None)  # Ajusta los parámetros según sea necesario  
    # Acceder a la lista Lenguajes_Junior de la instancia
    if desarrollador_buscado.Level =="Trainer":

        habilidades_faltantes = list(set(habilidades_programacion.Lenguajes_Junior) - set(desarrollador_buscado.Skill))
        Años_Exper=habilidades_programacion.Añ_Junior
        print(f"Habilidades Faltantes Para Ascender A Junior: {habilidades_faltantes} y {Años_Exper} Años De Experiencia ")

    if desarrollador_buscado.Level =="Junior":
        habilidades_faltantes = list(set(habilidades_programacion.Lenguaje_Middle) - set(desarrollador_buscado.Skill))
        Años_Exper=habilidades_programacion.Añ_Middel
        print(f"Habilidades Faltantes Para Ascender A Middle: {habilidades_faltantes} y {Años_Exper} Años De Experiencia ")

    if desarrollador_buscado.Level =="Middle":
        habilidades_faltantes = list(set(habilidades_programacion.Lenguaje_Senior) - set(desarrollador_buscado.Skill))
        Años_Exper=habilidades_programacion.Añ_Senior
        print(f"Habilidades Faltantes Para Ascender A Senior: {habilidades_faltantes} y {Años_Exper} Años De Experiencia ")

    if desarrollador_buscado.Level =="Senior":
        habilidades_faltantes = list(set(habilidades_programacion.Lenguaje_Lead) - set(desarrollador_buscado.Skill))
        Años_Exper=habilidades_programacion.Añ_Senior
        print(f"Habilidades Faltantes Para Ascender A Lead: {habilidades_faltantes} y {Años_Exper} Años De Experiencia ")



# El siguiente código solo se ejecutará si este script se ejecuta directamente
if __name__ == "__main__":
        menu()
