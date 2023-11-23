import json
#Usaremos Json Para Guardar Los Datos.
json_dataDevelopers=open("DataBaseDevelopers.json","w")
# Lista para almacenar los desarrolladores en memoria "Json"
listDs=json_dataDevelopers()

#Informacion  Empleado.

class Empelado():
    def __init__(self,Nombre,Skill,añ_exp,id=None) :
        #En Caso De Que El Id No Se Encuentre Registrado Lo Creamos En Else.
        if id is not None:
            self.id=id
        else:
            self.id=len(listDs)+1 # toma longitud y crea
        self.Nombre= Nombre
        self.Skill=Skill
        self.añ_exp=añ_exp
        self.habilid=Habilidades_Programacion(Skill,añ_exp)  
    
         
#Informacion Para Clasificacion En Tipo De Experiencia
class Habilidades_Programacion():
        def __init__(self,lenguajes,Añ_Exp) :
             Lenguajes_Trainer=["CSS","HTML"]
             Lenguajes_Junior=["JavaScripa","Phyton"]+Lenguajes_Trainer
             Lenguaje_Middle=["Java","C#","PHP"]+Lenguajes_Junior
             Lenguaje_Senior=['Ruby', 'Go', 'Swift']+Lenguaje_Middle
             Lenguaje_Lead=['Kotlin', 'Rust', 'TypeScript']+Lenguaje_Senior

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
             
        
        
      
# Cargar datos de JSON
with open("DataBaseDevelopers.json", "r") as json_dataDevelopers:
    listDs = json.load(json_dataDevelopers)



#Menu

def  menu():
    print("1. Agregar Desarrollador")
    print("2. Mostrar Desarrolladores")
    print("3. Imprimir Contenido del Archivo JSON")
    print("4. Salir")