import math  
class Circulo:
    def __init__(self,radio):
        self.__radio

        def get_radio(self):
            return self.__radio

        def set_radio(self,nueva_radio):
            if nueva_radio > 0:
               self.__radio = nueva_radio
            else:
               print("Radio no valida")

        def calcular_area(self):
            return math.pi*self.__radio**2

        def calcular_perimetro(self):
            return 2*math.pi*self.__radio

circulo = Circulo(3)
print("Area del circulo",round(circulo.calcular_area(),2))
print("Area del perimetro",round(circulo.calcular_perimetro(),2))
