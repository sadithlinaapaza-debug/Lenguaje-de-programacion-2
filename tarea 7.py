class Motor:
    def encender(self):
        print("el motor se enciende")

class Auto:
    def __init__(self):
        self.motor = Motor()
        
    def arrancar(self):
        print("El auto arranca")
        self.motor.encender()

a = Auto()
a.arrancar()
        
