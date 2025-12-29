class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,monto):
        self.saldo += monto

    def retirar(self,monto):
        if monto > self.saldo:
            print("saldo insuficiente")
        else:
            self.saldo -= monto

    def mostrar_saldo(self):
        print(f"La cuenta de {self.titular} , Saldo: {self.saldo}")

c1 = CuentaBancaria("Ana", 500)
c2 = CuentaBancaria("Luis", 300)

c1.depositar(200)
c1.retirar(100)
c1.mostrar_saldo()

c2.retirar(400)
c2.mostrar_saldo()
