class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo_estudiante = codigo_estudiante
        self.cursos = []
        
    def inscribirse(self, curso):
        self.cursos.append(curso)
        curso.agregar_estudiante(self)

    def mostrar_informacion(self):
        print(f"\nEstudiante: {self.nombre} | DNI: {self.dni} | Código: {self.codigo_estudiante}")
        print("Cursos inscritos:")
        for curso in self.cursos:
            print(f" {curso.nombre_curso}")


class Profesor:
    def __init__(self, nombre, dni, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad
        
    def mostrar_informacion(self):
        print(f"Profesor: {self.nombre} | DNI: {self.dni} | Especialidad: {self.especialidad}")


class Curso:
    def __init__(self, nombre_curso, profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            
    def mostrar_detalles(self):
        print(f"\nCurso: {self.nombre_curso}")
        print("Profesor:")
        self.profesor.mostrar_informacion()
        print("Estudiantes inscritos:")
        for est in self.estudiantes:
            print(f" {est.nombre} ({est.codigo_estudiante})")


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []
        
    def agregar_curso(self, curso):
        self.cursos.append(curso)
        
    def mostrar_cursos(self):
        print(f"\nUniversidad: {self.nombre}")
        for curso in self.cursos:
            curso.mostrar_detalles()

prof1 = Profesor("Ing. Juan Carlos", "01323043", "Programación")
prof2 = Profesor("Ing. Leonel Coila", "01456789", "Lenguaje de Programación")
prof3 = Profesor("Ing. José Tito", "02598741", "Base de Datos")
prof4 = Profesor("Ing. Luis Rossel", "03589642", "Análisis y Diseño de Sistemas")
prof5 = Profesor("Mg. Confesor Vargas", "04578963", "Modelos Discretos")
prof6 = Profesor("Mg. Elvis Roque", "05587621", "Inferencia Estadística")
prof7 = Profesor("Ing. Fred Torres", "06687421", "Programación Numérica")  


curso1 = Curso("Lenguajes de Programación II", prof1)
curso2 = Curso("Lenguaje de Programación I", prof2)
curso3 = Curso("Sistemas de Gestión de Base de Datos", prof3)
curso4 = Curso("Análisis y Diseño de Sistemas de Información", prof4)
curso5 = Curso("Modelos Discretos", prof5)
curso6 = Curso("Inferencia Estadística", prof6)
curso7 = Curso("Programación Numérica", prof7)  


est1 = Estudiante("Gleny Angelica Condori Mamani", "74705025", "240349")
est2 = Estudiante("Sadith Lina Apaza Huayta", "72450000", "240251")


univ = Universidad("Universidad Nacional del Altiplano")


univ.agregar_curso(curso1)
univ.agregar_curso(curso2)
univ.agregar_curso(curso3)
univ.agregar_curso(curso4)
univ.agregar_curso(curso5)
univ.agregar_curso(curso6)
univ.agregar_curso(curso7)


est1.inscribirse(curso1)
est1.inscribirse(curso3)
est1.inscribirse(curso6)
est1.inscribirse(curso7)

est2.inscribirse(curso2)
est2.inscribirse(curso4)
est2.inscribirse(curso5)
est2.inscribirse(curso7)

univ.mostrar_cursos()
est1.mostrar_informacion()
est2.mostrar_informacion()
