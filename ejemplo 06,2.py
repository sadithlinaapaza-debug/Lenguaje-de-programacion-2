class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False 

personan = float("ingrese nombre")
persona = float("ingrese edad")

if personan.es_mayor_de_edad():
    print(f"La persona {personan} es mayor de edad")

else:
    print(f"La persona {personan} es menor de edad")
