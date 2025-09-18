import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes.lower()

    def signo(self):
        if (self.mes == "enero" and self.dia >= 20) or (self.mes == "febrero" and self.dia <= 18):
            return "Acuario"
        elif (self.mes == "febrero" and self.dia >= 19) or (self.mes == "marzo" and self.dia <= 20):
            return "Piscis"
        elif (self.mes == "marzo" and self.dia >= 21) or (self.mes == "abril" and self.dia <= 19):
            return "Aries"
        elif (self.mes == "abril" and self.dia >= 20) or (self.mes == "mayo" and self.dia <= 20):
            return "Tauro"
        elif (self.mes == "mayo" and self.dia >= 21) or (self.mes == "junio" and self.dia <= 20):
            return "Géminis"
        elif (self.mes == "junio" and self.dia >= 21) or (self.mes == "julio" and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == "julio" and self.dia >= 23) or (self.mes == "agosto" and self.dia <= 22):
            return "Leo"
        elif (self.mes == "agosto" and self.dia >= 23) or (self.mes == "septiembre" and self.dia <= 22):
            return "Virgo"
        elif (self.mes == "septiembre" and self.dia >= 23) or (self.mes == "octubre" and self.dia <= 22):
            return "Libra"
        elif (self.mes == "octubre" and self.dia >= 23) or (self.mes == "noviembre" and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == "noviembre" and self.dia >= 22) or (self.mes == "diciembre" and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == "diciembre" and self.dia >= 22) or (self.mes == "enero" and self.dia <= 19):
            return "Capricornio"
        else:
            return "Fecha inválida"

# Función para mostrar el signo
def calcular_signo():
    try:
        nombre = entry_nombre.get()
        dia = int(entry_dia.get())
        mes = mes_var.get()

        if not nombre:
            messagebox.showwarning("Advertencia", "Ingrese su nombre")
            return

        persona = Persona(nombre, dia, mes)
        resultado = f"{persona.nombre} nació el {persona.dia} de {persona.mes.capitalize()} y su signo es {persona.signo()}"
        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Error", "Ingrese un día válido (número entero)")

# Interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Signo Zodiacal")
root.geometry("420x300")
root.resizable(False, False)
root.configure(bg="#FFA500")  # Fondo anaranjado

# Título
label_titulo = tk.Label(root, text="Signo Zodiacal", font=("Arial", 16, "bold"), bg="#FFA500", fg="white")
label_titulo.pack(pady=10)

# Nombre
frame_nombre = tk.Frame(root, bg="#FFA500")
frame_nombre.pack(pady=5)
tk.Label(frame_nombre, text="Nombre:", bg="#FFA500", fg="black").pack(side=tk.LEFT)
entry_nombre = tk.Entry(frame_nombre, width=20)
entry_nombre.pack(side=tk.LEFT)

# Día
frame_dia = tk.Frame(root, bg="#FFA500")
frame_dia.pack(pady=5)
tk.Label(frame_dia, text="Día:", bg="#FFA500", fg="black").pack(side=tk.LEFT)
entry_dia = tk.Entry(frame_dia, width=5)
entry_dia.pack(side=tk.LEFT)

# Mes con menú desplegable
frame_mes = tk.Frame(root, bg="#FFA500")
frame_mes.pack(pady=5)
tk.Label(frame_mes, text="Mes:", bg="#FFA500", fg="black").pack(side=tk.LEFT)
mes_var = tk.StringVar(root)
mes_var.set("enero")  # valor por defecto
meses = ["enero","febrero","marzo","abril","mayo","junio",
         "julio","agosto","septiembre","octubre","noviembre","diciembre"]
menu_mes = tk.OptionMenu(frame_mes, mes_var, *meses)
menu_mes.pack(side=tk.LEFT)

# Botón
btn_calcular = tk.Button(root, text="Calcular Signo", command=calcular_signo, bg="white", fg="black")
btn_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 12, "bold"), bg="#FFA500", fg="black")
label_resultado.pack(pady=20)

root.mainloop()
