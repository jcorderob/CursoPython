import tkinter as tk

def main():
    ventana = tk.Tk()
    ventana.title("Ejemplo de Grid en Tkinter")

    # Crear los widgets
    label1 = tk.Label(ventana, text="Etiqueta 1", bg="lightblue")
    label2 = tk.Label(ventana, text="Etiqueta 2", bg="lightgreen")
    label3 = tk.Label(ventana, text="Etiqueta 3", bg="lightyellow")
    label4 = tk.Label(ventana, text="Etiqueta 4", bg="lightpink")


    # Usar el grid para colocar los widgets
    label1.grid(row=0, column=0)
    label2.grid(row=1,  column=1)
    label3.grid(row=2, column=2)
    label4.grid(row=3, column=0, columnspan=3, sticky="WESN")


    # Expansión del grid para que  se expanda verticalmente
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_rowconfigure(2, weight=1)
    ventana.grid_rowconfigure(3, weight=1)

    
    # Expansión del grid para que  se expanda horizontalmente
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)   
    

    ventana.mainloop()

if __name__ == "__main__":
    main()
