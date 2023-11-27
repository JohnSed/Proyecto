import json
#Usaremos Json Para Guardar Los Datos.
json_Developers= "DataBaseDevelopers.json"

#Abrir Archivo Json
def JsonDesarrolladores():
    try:
        with open(json_Developers, "r",encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                Empleado_Desarrollador = json.loads(contenido)
                return [Empleado(**Dev) for Dev in Empleado_Desarrollador]
            else:
                return []#Devuleve Lista Vacia
    except FileNotFoundError:#Excepcion Para que informe si el archivo Json No existe 
        return []#Devuleve Lista Vacia
    except json.decoder.JSONDecodeError:# Excepcion Si EL Json esta mal definido o sus cmapos esta vacio
        return []#Devuleve Lista Vacia
    
#Guardar Informacion En Json
def SaveDesarrolladores( Desarrollador):
    with open(json_Developers, "w",encoding="utf-8") as archivo1:
        data = [{"id": dev.id, "Nombre": dev.Nombre, "Skill": dev.Skill, "añ_exp": dev.añ_exp} for dev in Desarrollador]
        json.dump(data, archivo1,ensure_ascii=False)

#Informacion  Empleado.
class Empleado():
    def __init__(self,Nombre,Skill,añ_exp, id=None) :
        #En Caso De Que El Id No Se Encuentre Registrado Lo Creamos En Else.
        if id is not None:
            self.id=id
        else:
            self.id=id
        self.Nombre= Nombre
        self.Skill=self.Skill = [] if Skill is None else Skill if isinstance(Skill, list) else [Skill] # Verificar si la variable Skill es una instancia de la clase list.
        self.añ_exp=añ_exp

#Lista para almacenar los desarrolladores en memoria "Json"
listDS = JsonDesarrolladores()


#Menu
def  menu():
    print("1. Agregar Desarrollador")
    print("2. Mostrar Desarrolladores")
    print("3. Modificar Desarrollador")
    print("4. Eliminar Desarrrolador: ")
    print("5. Salir")
    
    
#Imprimir Json
def Ver_desarrolladores():
    print("\nLista de Desarrolladores:")
    for Desarrolladores in listDS:
        print(f"ID: {Desarrolladores.id}, Nombre: {Desarrolladores.Nombre}, Habilidades: {Desarrolladores.Skill}, "
              f"Años de Experiencia: {Desarrolladores.añ_exp}")
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
        Añ_Expe = float(input("Ingrese Su Experiencia En Años: "))

        # Crear la instancia de Empleado después de ingresar la información
        Desarrollador = Empleado(Nombre, Skill, Añ_Expe, id)

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
        if nuevo_skill:
            desarrollador_a_modificar.Skill.extend(nuevo_skill.split(','))  # Extender la lista de habilidades
        # Años Experiencia
        print(f"Años de experiencia actuales: {desarrollador_a_modificar.añ_exp}")
        nuevo_añ_exp = input("Ingrese los nuevos años de experiencia (o presione Enter para dejarlos sin cambios): ")
        desarrollador_a_modificar.añ_exp = float(nuevo_añ_exp) if nuevo_añ_exp else desarrollador_a_modificar.añ_exp

        SaveDesarrolladores(listDS)
        print(f"Desarrollador con ID {desarrollador_a_modificar.id} modificado exitosamente.")
    else:
        print(f"No se encontró ningún desarrollador con ID {id_modificar}")

# El siguiente código solo se ejecutará si este script se ejecuta directamente
if __name__ == "__main__":
        menu()

#Informacion Para Clasificacion En Tipo De Experiencia
class Habilidades_Programacion():
        
        def __init__(self,lenguajes,Añ_Exp,Level) :
             self.Levele= Level
             Lenguajes_Trainer=["CSS","HTML"]
             Lenguajes_Junior=["JavaScripa","Phyton"]+Lenguajes_Trainer
             Lenguaje_Middle=["Java","C#","PHP"]+Lenguajes_Junior
             Lenguaje_Senior=['Ruby', 'Go', 'Swift']+Lenguaje_Middle
             Lenguaje_Lead=['Kotlin', 'Rust', 'TypeScript']+Lenguaje_Senior
               #self.clasificacion = self.clasificar_habilidades(lenguajes, Lenguajes_Trainer, Lenguajes_Junior, Lenguaje_Middle, Lenguaje_Senior, Lenguaje_Lead)
             if (hab in lenguajes for hab in Lenguaje_Lead) and Añ_Exp < 3:
                  Level= ("Lead")
             elif (hab in lenguajes for hab in Lenguaje_Senior) and Añ_Exp < 3:
                  Level = ("Senior")
             elif  (hab in lenguajes for hab in Lenguaje_Middle) and Añ_Exp < 2:
                  Level ="Middle"
             elif (hab in lenguajes for hab in Lenguajes_Junior) and Añ_Exp < 1:
                  Level ="Junior"
             elif (hab in lenguajes for hab in Lenguajes_Trainer) and Añ_Exp < 1:
                  Level ="Trainer"
                  
             else:
                  return ("No se pudo verificar Por Favor Verifique Su Empleado!")
             
        #esta seria la  clasificacion de funciones sip
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
        
