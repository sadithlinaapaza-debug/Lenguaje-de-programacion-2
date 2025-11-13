class VehiculoTerrestre:
    def conducir(self):
        print("Conducir por la carretera")
    def frenar(self):
        print("El vehiculo terrestre se ha detenido")

class VehiculoAcuario:
    def navegar(self):
        print("Navegar por el agua")
    def fondear(self):
        print("El vehiculo acuatico ha fondeado")

class VehiculoAnfibio(VehiculoTerrestre,VehiculoAcuario):
    def transformar(self,modo):
        if modo == "tierra":
            print("Cambiando al modo terrestre." )
        elif modo == "agua":
            print("Cambiando al modo acuatico.")
        else:
            print("Modo no reconocido")

def main():
    anfibio = VehiculoAnfibio()
    anfibio.transformar("tierra")
    anfibio.conducir()
    anfibio.frenar()

    print("\n")

    anfibio.transformar("agua")
    anfibio.navegar()
    anfibio.fondear()
if __name__=="__main__":
    main()
