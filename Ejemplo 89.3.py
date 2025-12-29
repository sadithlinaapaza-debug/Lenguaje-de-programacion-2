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

print("CÍRCULO:")
radio = float(input("Ingresa el radio: "))
circulo = Circulo(radio)
app_circulo = Aplicacion(circulo)
app_circulo.ejecutar()

print("\nRECTÁNGULO:")
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
rectangulo = Rectangulo(base, altura)
app_rectangulo = Aplicacion(rectangulo)
app_rectangulo.ejecutar()
