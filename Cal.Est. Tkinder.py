import tkinter as tk
from tkinter import messagebox

class CalculadoraEstadistica:
    def __init__(self, lista=None, numero=0):
        self.lista = lista if lista is not None else []
        self.numero = numero

    def ingresar_datos(self, datos):
        self.lista = []
        for i in datos.split():
            try:
                self.numero = float(i)
                self.lista.append(self.numero)
            except ValueError:
                pass  

    def media(self):
        if not self.lista:
            return 0
        return sum(self.lista) / len(self.lista)

    def varianza(self):
        if not self.lista:
            return 0
        m = self.media()
        return sum((i - m) ** 2 for i in self.lista) / len(self.lista)

    def desviacion_estandar(self):
        return self.varianza() ** 0.5


# --- Interfaz con Tkinter ---
def calcular():
    datos = entrada.get()
    calculadora.ingresar_datos(datos)

    media = calculadora.media()
    varianza = calculadora.varianza()
    desviacion = calculadora.desviacion_estandar()

    messagebox.showinfo(
        "Resultados",
        f"Media: {media:.2f}\nVarianza: {varianza:.2f}\nDesviación Estándar: {desviacion:.2f}"
    )


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Estadística")
ventana.geometry("400x250")
ventana.configure(bg="pink")  # Fondo rosado

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese los datos separados por espacio:", bg="pink", font=("Arial", 12))
etiqueta.pack(pady=10)

# Entrada de datos
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botón calcular
boton = tk.Button(ventana, text="Calcular", command=calcular, bg="white", font=("Arial", 12))
boton.pack(pady=15)

# Instancia de la calculadora
calculadora = CalculadoraEstadistica()

# Iniciar loop
ventana.mainloop()
