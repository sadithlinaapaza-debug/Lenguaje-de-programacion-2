class Cateto_a:
    def __init__(self,cateto_a):
        self.cateto_a = cateto_a

class Cateto_b:
    def __init__(self,cateto_b):
        self.cateto_b = cateto_b

class Hipotenusa(Cateto_a,Cateto_b):
    def __init__(self,cateto_a,cateto_b):
      Cateto_a.__init__(self,cateto_a)
      Cateto_b.__init__(self,cateto_b)

def calcularHipotenusa(self):
    
