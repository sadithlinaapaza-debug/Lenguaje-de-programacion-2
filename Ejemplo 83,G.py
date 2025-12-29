from typing import TypeVar, Generic
T = TypeVar('T',int,float)

class Calculadora(Generic[T]):
    def __init__(self,a:T,b:T):
        self.a = a
        self.b = b

    def sumar(self)->T:
        return self.a + self.b

    def restar(self)->T:
        return self.a - self.b

    def multiplicar(self)->T:
        return self.a * self.b

    def dividir(self)->T:
        if self.b == 0:
            raise ValueError("No se puede dividir entre cero")
        return self.a / self.b

cal_int = Calculadora[int](a,5)
print("Sumar: ",cal_int.sumar())
print("Resta: ",cal_int.restar())
print("Multiplicar: ",cal_int.multiplicar())
print("Dividir: ",cal_int.dividir())

print("**** FLOTANTE*****")
cal_float = Calculadora[float](10.5,2.5)
print("Sumar: ",cal_float.sumar())
print("Resta: ",cal_float.restar())
print("Multiplicar: ",cal_float.multiplicar())
print("Dividir: ",cal_float.dividir())
