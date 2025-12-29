import math
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class Figura_Generica(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

class Rectangulo(Figura_Generica[T]):
    def __init__(self, a: T, b: T):
        super().__init__(a, b)
        
    def area(self) -> T:
        return self.a * self.b
    
    def perimetro(self) -> T:
        return 2 * self.a + 2 * self.b

class Circulo(Figura_Generica[T]):
    def __init__(self, radio: T):
        super().__init__(a=0, b=radio)  
        
    def area(self) -> float:
        return math.pi * (self.b ** 2)
        
    def perimetro(self) -> float:
        return 2 * math.pi * self.b

rect = Rectangulo(4, 5)
print("Área del rectángulo:", rect.area())
print("Perímetro del rectángulo:", rect.perimetro())

cir = Circulo(3)
print("Área del círculo:", cir.area())
print("Perímetro del círculo:", cir.perimetro())
