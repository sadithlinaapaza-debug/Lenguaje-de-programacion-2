import math

# Principio S 
class CalculadoraHipotenusa:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")


# Principio O y L
class HipotenusaTriangulo(CalculadoraHipotenusa):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError("Los catetos deben ser positivos")

        return math.sqrt(self.a**2 + self.b**2)


# Principio D 
class Aplicacion:
    def __init__(self, calculadora: CalculadoraHipotenusa):
        self.calculadora = calculadora
        
    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"Hipotenusa = {resultado:.2f}")


hipotenusa = HipotenusaTriangulo(3, 4)
app = Aplicacion(hipotenusa)
app.ejecutar()
