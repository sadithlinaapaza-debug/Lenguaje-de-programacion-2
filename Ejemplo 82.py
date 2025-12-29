from typing import TypeVar, Generic
import math

T = TypeVar('T', int, float)

class TrianguloRectangulo(Generic[T]):
    def __init__(self,a:T,b:T):
        self.a = a
        self.b = b

    def calcular_hipotenusa(self)-> int:
        return math.sqrt(self.a**2 + self.b**2)

    def calcular_area(self)-> int:
        return (self.a*self.b)/2

    def calcular_perimetro(self)-> float:
        return self.a + self.b + TrianguloRectangulo.calcular_hipotenusa(self)

def main():
    try:
        a = float(input("Ingrese el valor de A: "))
        b = float(input("Ingrese el valor de B: "))
        if a<=0 or b<=0:
            raise ValueError("Los valores deben ser numeros positivos")
        
        cal = TrianguloRectangulo(a,b) 
    
        print(f"La hipotenusa del triangulo es: {cal.calcular_hipotenusa():2f}")
        print(f"El area del triangulo es: {cal.calcular_area():2f}")
        print(f"El perimetro del triangulo es: {cal.calcular_perimetro():2f}")
        
    except ValueError as ve:
        print("Error",ve)
if __name__=="__main__":
    main()
