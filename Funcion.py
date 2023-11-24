import json
#Usaremos Json Para Guardar Los Datos.
json_Developers= "DataBaseDevelopers.json"

#Abrir Archivo o Guardar Json
def JsonDesarrolladores():
    try:
        with open(json_Developers, "r") as archivo:
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
def SaveDesarrolladores(Desarrollador):
    with open(json_Developers, "w") as archivo1:
        data = [{"id": dev.id, "Nombre": dev.Nombre, "Skill": dev.Skill, "añ_exp": dev.añ_exp} for dev in Desarrollador]
        json.dump(data, archivo1)

#Informacion  Empleado.
class Empleado():
    def __init__(self,Nombre,Skill,añ_exp, id=None) :
        #En Caso De Que El Id No Se Encuentre Registrado Lo Creamos En Else.
        if id is not None:
            self.id=id
        else:
            self.id=len(json_Developers) + 1 # toma longitud y crea
        self.Nombre= Nombre
        self.Skill=Skill
        self.añ_exp=añ_exp
        
    
         
#Informacion Para Clasificacion En Tipo De Experiencia
class Habilidades_Programacion():
        
        def __init__(self,lenguajes,Añ_Exp) :
             Lenguajes_Trainer=["CSS","HTML"]
             Lenguajes_Junior=["JavaScripa","Phyton"]+Lenguajes_Trainer
             Lenguaje_Middle=["Java","C#","PHP"]+Lenguajes_Junior
             Lenguaje_Senior=['Ruby', 'Go', 'Swift']+Lenguaje_Middle
             Lenguaje_Lead=['Kotlin', 'Rust', 'TypeScript']+Lenguaje_Senior
               #self.clasificacion = self.clasificar_habilidades(lenguajes, Lenguajes_Trainer, Lenguajes_Junior, Lenguaje_Middle, Lenguaje_Senior, Lenguaje_Lead)
             if (hab in lenguajes for hab in Lenguaje_Lead):
                  return ("Trainer")
             elif (hab in lenguajes for hab in Lenguaje_Senior):
                  return ("Senior")
             elif  (hab in lenguajes for hab in Lenguaje_Middle):
                  return ("Middle")
             elif (hab in lenguajes for hab in Lenguajes_Junior):
                  return ("Junior")
             elif (hab in lenguajes for hab in Lenguajes_Trainer):
                  return("Trainer")
             else:
                  return ("No se pudo verificar Por Favor Verifique Su Empleado!")
             
        #esta seria la  clasificacion de funciones sip
        
#Lista para almacenar los desarrolladores en memoria "Json"
listDS = JsonDesarrolladores()


#Menu
def  menu():
    print("1. Agregar Desarrollador")
    print("2. Mostrar Desarrolladores")
    print("3. Imprimir Contenido del Archivo JSON")
    print("4. Salir")

#Imprimir Json
def Ver_desarrolladores():
    print("\nLista de Desarrolladores:")
    for Desarrolladores in listDS:
        print(f"ID: {Desarrolladores.id}, Nombre: {Desarrolladores.Nombre}, Habilidades: {Desarrolladores.Skill}, "
              f"Años de Experiencia: {Desarrolladores.añ_exp}")
    print()

#Agregar Desarrollador
def Nuevo_Usuario():
    Nombre = input("Ingrese Nombre Del Empleado: ")
    Skill = input("Ingrese Habilidades (Separadas En Coma): ")
    Añ_Expe = float(input("Ingrese Su Experiencia En Años: "))

    Desarrollador = Empleado(Nombre,Skill,Añ_Expe)
    listDS.append(Desarrollador)
    SaveDesarrolladores(listDS)
    print()
    print(f"El Desarrollador {Nombre} ha sido agregado exitosamente.")
    print()

# El siguiente código solo se ejecutará si este script se ejecuta directamente
if __name__ == "__main__":
    menu()
