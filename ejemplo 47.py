class Animal: #clase base
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacerSonido(self):
        pass
    
class Perro(Animal): #herencia derivada

    def hacerSonido(self):
        return "Guau!"
class Gato(Animal): #herencia derivadda
    def hacerSonido(self):
        return "¡Miau!"
    
perro =Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")
gato =Gato("Luna")
print(f"{gato.nombre} dice {gato.hacerSonido()}")
