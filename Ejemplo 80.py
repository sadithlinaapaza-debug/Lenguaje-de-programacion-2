from typing import TypeVar
import math

T = TypeVar('T',int,float)

def calcular_hipotenusa(cateto_a:T,cateto_b:T)->T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

a = float(input("Ingrese cateto a: "))
b = float(input("Ingrese cateto b: "))

print("Hipotenusa = ",calcular_hipotenusa(a,b))
