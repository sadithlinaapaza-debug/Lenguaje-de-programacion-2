class Nadador: #clase base 1
    def nadar(self):
        print("Nadando en el agua")

class Volador: #clase base 2
    def volar(self):
        print("volando por el aire")

class Pato(Nadador,Volador): #clase derivada
    def graznar(self):
        print("¡Cuac!")

class Cisne(Nadador,Volador): #clase derivada
    def trompetean(self):
        print("¡Whoop!")

pato = Pato()
pato.nadar()
pato.volar()
pato.graznar()

cisne = Cisne()
cisne.nadar()
cisne.volar()
cisne.trompetean()
