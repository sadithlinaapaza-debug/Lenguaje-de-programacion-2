class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return self.salario
        
class EmpleadoPorHoras(Empleado):
    def __init__(self,nombre,salario,horas):
        super().__init__(nombre,salario)
        self.horas = horas
        
    def calcular_pago(self):
        return self.salario * self.horas

empleados = [
    EmpleadoTiempoCompleto("Ana", 2000),
    EmpleadoPorHoras("Luis", 20, 8)
]

for e in empleados:
    print(f"{e.nombre} cobra: {e.calcular_pago()}")
