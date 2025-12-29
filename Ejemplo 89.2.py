import math

# Principio S
class FiguraGeometrica:
    def area(self):
        raise NotImplementedError("Debe implementar el método area")

    def perimetro(self):
        raise NotImplementedError("Debe implementar el método perimetro")


# Principio O y L
class Circulo(FiguraGeometrica):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("El radio debe ser positivo")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimetro(self):
        return 2 * math.pi * self.r


# Principio O y L
class Rectangulo(FiguraGeometrica):
    def __init__(self, b, a):
        if b <= 0 or a <= 0:
            raise ValueError("Los lados deben ser positivos")
        self.b = b
        self.a = a

    def area(self):
        return self.b * self.a

    def perimetro(self):
        return 2 * (self.b + self.a)


# Principio D
class Aplicacion:
    def __init__(self, figura: FiguraGeometrica):
        self.figura = figura

    def ejecutar(self):
        print(f"Área: {self.figura.area():.2f}")
        print(f"Perímetro: {self.figura.perimetro():.2f}")

print("Circulo:")
circulo = Circulo(3)
app_circulo = Aplicacion(circulo)
app_circulo.ejecutar()

print("Rectangulo:")
rectangulo = Rectangulo(3, 4)
app_rectangulo = Aplicacion(rectangulo)
app_rectangulo.ejecutar()
