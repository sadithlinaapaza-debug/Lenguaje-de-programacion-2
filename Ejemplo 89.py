import math

# Principio S 
class FigurasGeometricas:
    def area(self):
        raise NotImplementedError("Debe implementar el método calcular")

    def perimetro(self):
        raise NotImplementedError("Debe implementar el método calcular")
    
# Principio O y L
class Circulo(FigurasGeometricas):
    def __init__(self,a):
        self.a = a

    def area(self):
        if self.a <= 0:
            raise ValueError("El radio debe ser positivos")

        return math.pi * self.a**2

    def perimetro(self):
        if self.a <= 0:
            raise ValueError("El radio debe ser positivos")

        return 2 * math.pi * self.a

# Principio O y L
class Rectangulo(FigurasGeometricas):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError("Los lados deben ser positivos")

        return self.a * self.b

    def perimetro(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError("Los lados deben ser positivos")

        return (self.a * 2)+(self.b * 2)


# Principio D 
class Aplicacion:
    def __init__(self, calculadora: FigurasGeometricas):
        self.calculadora = calculadora
        
    def ejecutar(self):
        resultado = self.calculadora.area()
        print(f"El area del Circulo es = {Circulo.area:.2f}")
        print(f"El area del Rectangulo es = {Rectangulo.area:.2f}")

        resultado = self.calculadora.perimetro()
        print(f"El perimetro del Circulo es = {Circulo.perimetro:.2f}")
        print(f"El perimetro del Rectangulo es = {Rectangulo.perimetro:.2f}")

circulo = Circulo(3)
rectangulo = Rectangulo(3,4)
app = Aplicacion(circulo)
app = Aplicacion(rectangulo)
app.ejecutar()
