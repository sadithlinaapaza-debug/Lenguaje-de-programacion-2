class FiguraGeometrica:
    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Subclases deben implementar este metodo")

    def perimetro(self):
        raise NotImplementedError("Subclases deben implementar este metodo")

class Circulo(FiguraGeometrica):
    def __init__(self,radio):
        super().__init__("Circulo")
        self.radio = radio

    def area(self):
        return 3.141592*(self.radio**2)

    def perimetro(self):
        return 2*3.141592*self.radio

circulo = Circulo(5)
print(f"Nombre: {circulo.nombre}")
print(f"Area: {circulo.area()}")
print(f"Perimetro: {circulo.perimetro()}")
