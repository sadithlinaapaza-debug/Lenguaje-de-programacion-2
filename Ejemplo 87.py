# Clase base 
class CalculadoraFibonacci:
    def calcular(self):
        raise NotImplementedError("Debe implementar el metodo calcular")


# Principio O y L
class FibonacciNumero(CalculadoraFibonacci):
    def __init__(self, n):
        self.n = n

    def calcular(self):
        serie = []
        a, b = 0, 1
        for _ in range(self.n):
            serie.append(a)
            a, b = b, a + b
        return serie


# Principio D
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora
        
    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"La serie de Fibonacci es: {resultado}")


fibonacci = FibonacciNumero(7)
app = Aplicacion(fibonacci)
app.ejecutar()
