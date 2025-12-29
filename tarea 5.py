import math
class Figura:
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura)/2

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)

figuras = [ Rectangulo(4,7),Triangulo(3,9),Circulo(5)]

for f in figuras:
    print("Área:", f.area())
