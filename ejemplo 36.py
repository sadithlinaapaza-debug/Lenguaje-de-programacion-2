import gc
class Estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado {self.nombre} {self.edad} años {self.carrera}")

    def mostrar_informacion(self):
        print(f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años")

    def __del__(self):
        print(f"Estudiante eliminado {self.nombre}")

datos_estudiantes = [("Ana",20,"Medicina"),
                     ("Luis",22,"Ingenieria"),
                     ("Carla",19,"Arquitectura")]

grupo = []

for datos in datos_estudiantes:
    estudiante = Estudiante(*datos)
    estudiante.mostrar_informacion()
    grupo.append(estudiante) #append es añadir

grupo.clear()
del estudiante
gc.collect()
print("Fin del programa")
