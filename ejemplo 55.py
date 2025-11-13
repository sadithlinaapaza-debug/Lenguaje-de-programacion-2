class Vehiculo:
    def iniciar(self):
        print("Sonido generico")

class Coche(Vehiculo):
    def iniciar(self):
        print("El coche arranca y acelera")

class Bicicleta(Vehiculo):
    def iniciar(self):
        print("La bicicleta empieza a pedalear")

class Barco(Vehiculo):
    def iniciar(self):
        print("El barco enciende el motor y zarpa")

vehiculo = [Coche(), Bicicleta(), Barco()]
for v in vehiculo:
    v.iniciar()
