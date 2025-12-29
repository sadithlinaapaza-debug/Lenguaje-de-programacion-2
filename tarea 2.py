class Producto:
    def __init__(self,nombre,precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
        return self.__nombre

    def set_precio(self,nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo")

    def aplicar_descuento(self,porcentaje):
        if porcentaje < 0 or porcentaje > 100:
            print("Descuento invalido")
        else:
            nuevo_precio = self.__precio * (1 - porcentaje / 100)
            self.set_precio(nuevo_precio)

p1 = Producto("Laptop", 3000)
p1.aplicar_descuento(15)
print("Precio final:", p1.get_precio())

p2 = Producto("Mouse", -20)  
p2.aplicar_descuento(200)   
print("Precio final:", p2.get_precio())
