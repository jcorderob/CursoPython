import tkinter as tk
from tkinter import ttk

# Función para realizar la operación seleccionada
def calcular():
    try:
        val1 = float(resultado1.get())
        val2 = float(resultado2.get())
        operacion = operacion_seleccionada.get()
        
        if operacion == "Sumar":
            resultado = val1 + val2
        elif operacion == "Restar":
            resultado = val1 - val2
        elif operacion == "Multiplicar":
            resultado = val1 * val2
        elif operacion == "Dividir":
            if val2 == 0:
                resultado = "Error: División por 0"
            else:
                resultado = val1 / val2
        elif operacion == "Potencia":
            resultado = val1 ** val2
        else:
            resultado = "Seleccione una operación"
        
        resultado_salida.delete(0, tk.END)
        resultado_salida.insert(0, str(resultado))
    except ValueError:
        resultado_salida.delete(0, tk.END)
        resultado_salida.insert(0, "Entrada inválida")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")

# Etiquetas y cajas de texto para los valores
ttk.Label(ventana, text="Valor 1:").grid(column=0, row=0, padx=10, pady=10)
resultado1 = ttk.Entry(ventana)
resultado1.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(ventana, text="Valor 2:").grid(column=0, row=1, padx=10, pady=10)
resultado2 = ttk.Entry(ventana)
resultado2.grid(column=1, row=1, padx=10, pady=10)

# Variable para guardar la operación seleccionada
operacion_seleccionada = tk.StringVar()

# Botones de radio para seleccionar la operación
operaciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Potencia"]
row = 2
for operacion in operaciones:
    ttk.Radiobutton(ventana, text=operacion, variable=operacion_seleccionada, value=operacion).grid(column=0, row=row, padx=10, pady=5, sticky=tk.W)
    row += 1

# Botón para calcular el resultado
boton_resultado = ttk.Button(ventana, text="Resultado", command=calcular)
boton_resultado.grid(column=0, row=row, padx=10, pady=10)

# Caja de texto para mostrar el resultado
resultado_salida = ttk.Entry(ventana)
resultado_salida.grid(column=1, row=row, padx=10, pady=10)

# Iniciar el loop principal
ventana.mainloop()
