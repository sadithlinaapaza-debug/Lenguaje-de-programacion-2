from typing import TypeVar, Generic
import tkinter as tk

T = TypeVar('T', int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self): return self.a + self.b
    def restar(self): return self.a - self.b
    def multiplicar(self): return self.a * self.b

    def dividir(self):
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.a / self.b


# ---------------------------------------------------
# ANIMACIÓN Y CAMBIO DE CARITA
# ---------------------------------------------------

def dibujar_carita_normal():
    canvas.delete("all")
    cara = canvas.create_oval(10, 10, 80, 80, fill="#FFD166", outline="#FFA500", width=3)
    eye1 = canvas.create_oval(30, 35, 38, 43, fill="black")
    eye2 = canvas.create_oval(52, 35, 60, 43, fill="black")
    smile = canvas.create_arc(30, 40, 60, 70, start=200, extent=140, style="arc", width=3)
    return [cara, eye1, eye2, smile]

def dibujar_carita_error():
    canvas.delete("all")
    cara = canvas.create_oval(10, 10, 80, 80, fill="#FFB5A7", outline="#FF6B6B", width=3)
    eye1 = canvas.create_oval(30, 35, 38, 43, fill="black")
    eye2 = canvas.create_oval(52, 35, 60, 43, fill="black")
    triste = canvas.create_arc(30, 55, 60, 75, start=20, extent=140, style="arc", width=3)
    return [cara, eye1, eye2, triste]


# ---------------------------------------------------
#   OPERACIONES
# ---------------------------------------------------

def ejecutar_operacion(op):
    try:
        label_mensaje.config(text="")
        dibujar_carita_normal()  # volver a carita feliz

        a = float(entry_a.get())
        b = float(entry_b.get())

        calc = Calculadora(a, b)

        if op == "sumar": r = calc.sumar()
        elif op == "restar": r = calc.restar()
        elif op == "multiplicar": r = calc.multiplicar()
        elif op == "dividir": r = calc.dividir()

        if isinstance(r, float) and r.is_integer():
            r = int(r)

        label_resultado.config(text=f"= {r}")
        label_mensaje.config(text="¡Muy bien! 😊", fg="green")

    except ValueError:
        label_mensaje.config(text="Error: ingresa solo números.", fg="red")
        dibujar_carita_error()
    except Exception as e:
        label_mensaje.config(text=f"{e}", fg="red")
        dibujar_carita_error()


def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_resultado.config(text="")
    label_mensaje.config(text="")
    dibujar_carita_normal()


# ---------------------------------------------------
#   VENTANA
# ---------------------------------------------------

ventana = tk.Tk()
ventana.title("CalcDivertida para Niños 🎈")
ventana.geometry("650x450")   # ventana más grande
ventana.config(bg="#FFF7E6")
ventana.resizable(False, False)

header = tk.Label(
    ventana, text="¡Calculadora Divertida!",
    font=("Comic Sans MS", 26, "bold"),
    bg="#FFE082", fg="#5A3E1B", pady=10
)
header.pack(fill="x", pady=10)

# ------------------------------
# ENTRADAS
# ------------------------------
frame_inputs = tk.Frame(ventana, bg="#FFF7E6")
frame_inputs.pack()

tk.Label(frame_inputs, text="Valor A:", bg="#FFF7E6",
         font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(frame_inputs, font=("Arial", 16), width=10, justify="center")
entry_a.grid(row=0, column=1, padx=10)

tk.Label(frame_inputs, text="Valor B:", bg="#FFF7E6",
         font=("Arial", 14, "bold")).grid(row=0, column=2, padx=10, pady=10)
entry_b = tk.Entry(frame_inputs, font=("Arial", 16), width=10, justify="center")
entry_b.grid(row=0, column=3, padx=10)

# ------------------------------
# BOTONES EN FILA
# ------------------------------

frame_botones = tk.Frame(ventana, bg="#FFF7E6")
frame_botones.pack(pady=15)

btn_cfg = {
    "font": ("Arial", 14, "bold"),
    "width": 12,
    "height": 2,
    "bd": 0
}

tk.Button(frame_botones, text="➕ Sumar", bg="#6FCF97", fg="white",
          command=lambda: ejecutar_operacion("sumar"), **btn_cfg).pack(side="left", padx=10)

tk.Button(frame_botones, text="➖ Restar", bg="#F2994A", fg="white",
          command=lambda: ejecutar_operacion("restar"), **btn_cfg).pack(side="left", padx=10)

tk.Button(frame_botones, text="✖️ Multiplicar", bg="#56CCF2", fg="white",
          command=lambda: ejecutar_operacion("multiplicar"), **btn_cfg).pack(side="left", padx=10)

tk.Button(frame_botones, text="➗ Dividir", bg="#F5668A", fg="white",
          command=lambda: ejecutar_operacion("dividir"), **btn_cfg).pack(side="left", padx=10)

# BOTÓN BORRAR (ahora grande y visible)
tk.Button(frame_botones, text="🧽 Borrar", bg="#B39DDB", fg="black",
          width=10, height=2, font=("Arial", 14, "bold"),
          command=limpiar).pack(side="left", padx=10)

# ------------------------------
# RESULTADO
# ------------------------------
label_resultado = tk.Label(
    ventana, text="", font=("Arial", 32, "bold"),
    fg="#0f4c81", bg="#FFF7E6"
)
label_resultado.pack(pady=10)

label_mensaje = tk.Label(ventana, text="", bg="#FFF7E6", font=("Arial", 14))
label_mensaje.pack(pady=5)

# ------------------------------
# CARITA (normal por defecto)
# ------------------------------
canvas = tk.Canvas(ventana, width=120, height=100, bg="#FFF7E6", highlightthickness=0)
canvas.pack()

dibujar_carita_normal()

entry_a.focus()

ventana.mainloop()
