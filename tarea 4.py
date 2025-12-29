class Vehiculo:
    def acelerar(self):
        print("El vehiculo acelera")

class Volador:
    def volar(self):
        print("Vuela por los aires")

class Avion(Vehiculo,Volador):
    def accion(self):
        print("Es un transporte")

avion = Avion()
avion.acelerar()
avion.volar()
avion.accion()
