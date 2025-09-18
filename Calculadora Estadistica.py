class CalculadoraEstadistica:
    def __init__(self, lista, numero):
        self.lista = lista
        self.numero = numero

    def ingresar_datos(self):
        datos = input("Ingrese los datos: ")
        self.lista = []
        for i in datos.split():
            self.numero = float(i)
            self.lista.append(self.numero)

    def media(self):
        total = 0
        contador = 0
        for i in self.lista:
            total = total + i
            contador = contador + 1
        if contador == 0:
            return 0
        return total / contador

    def varianza(self):
        m = self.media()
        suma = 0
        contador = 0
        for i in self.lista:
            suma = suma + (i - m) ** 2
            contador = contador + 1
        if contador == 0:
            return 0
        return suma / contador

    def desviacion_estandar(self):
        return self.varianza() ** 0.5

CalculadoraDatos = CalculadoraEstadistica([], 0)

CalculadoraDatos.ingresar_datos()

print("Media:", CalculadoraDatos.media())
print("Varianza:", CalculadoraDatos.varianza())
print("Desviación estándar:", CalculadoraDatos.desviacion_estandar())
