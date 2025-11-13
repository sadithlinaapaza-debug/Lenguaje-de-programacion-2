class Metodo_pago:
    def __init__(self, monto):
        self.monto = monto

    def pago(self):
        print("Realiza un pago genérico")
        pass


class Tarjeta(Metodo_pago):
    def pago(self):
        print(f"Pago de S/. {self.monto:.2f} con tarjeta de crédito")


class Paypal(Metodo_pago):
    def pago(self):
        print(f"Pago de S/. {self.monto:.2f} con PayPal")


class Efectivo(Metodo_pago):
    def pago(self):
        print(f"Pago de S/. {self.monto:.2f} en Efectivo")
        
class Yape(Metodo_pago):
    def pago(self):
        print(f"Pago de S/. {self.monto:.2f} en yape")


pagos = [Tarjeta(19),
    Paypal(20),
    Efectivo(100),
    Yape(50)]

for pago in pagos:
    pago.pago()
