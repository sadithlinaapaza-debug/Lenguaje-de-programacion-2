import math

class Cateto_a:
    def __init__(self, cateto_a):
        self.cateto_a = float(cateto_a)

class Cateto_b:
    def __init__(self, cateto_b):
        self.cateto_b = float(cateto_b)

class Hipotenusa(Cateto_a, Cateto_b):
    def __init__(self, cateto_a, cateto_b):
        Cateto_a.__init__(self, cateto_a)
        Cateto_b.__init__(self, cateto_b)

    def calcular_hipotenusa(self):
        a = self.cateto_a
        b = self.cateto_b
        if a < 0 or b < 0:
            raise ValueError("Los catetos deben ser números no negativos.")
        return math.sqrt(a*a + b*b)

    def __str__(self):
        return f"Cateto a = {self.cateto_a}, Cateto b = {self.cateto_b}"

def main():
    try:
        ca = input("Ingrese cateto a: ")
        cb = input("Ingrese cateto b: ")
        hip = Hipotenusa(ca, cb)
        h = hip.calcular_hipotenusa()
        print(hip)
        print(f"Hipotenusa = {h:.4f}")
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
