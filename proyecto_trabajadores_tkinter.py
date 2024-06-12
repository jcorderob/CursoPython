import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Trabajador:
    def __init__(self, nombre, dni, fecha_ingreso, edad, sexo, sueldo):
        self.nombre = nombre
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.edad = edad
        self.sexo = sexo
        self.sueldo = sueldo

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Trabajadores")
        
        self.trabajadores = []
        
        # Crear formulario
        self.form_frame = tk.Frame(ventana)
        self.form_frame.pack(padx=10, pady=10)
        self.form_frame.configure(
                  highlightbackground="black",  # Color del borde del marco
                  highlightthickness=1) 
        
        tk.Label(self.form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.form_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.form_frame, text="DNI").grid(row=1, column=0, padx=5, pady=5)
        self.dni_entry = tk.Entry(self.form_frame)
        self.dni_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.form_frame, text="Fecha Ingreso (dd-mm-yyyy)").grid(row=2, column=0, padx=5, pady=5)
        self.fecha_ingreso_entry = tk.Entry(self.form_frame)
        self.fecha_ingreso_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.form_frame, text="Edad").grid(row=3, column=0, padx=5, pady=5)
        self.edad_entry = tk.Entry(self.form_frame)
        self.edad_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.form_frame, text="Sexo").grid(row=4, column=0, padx=5, pady=5)
        self.sexo_entry = tk.Entry(self.form_frame)
        self.sexo_entry.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(self.form_frame, text="Sueldo").grid(row=5, column=0, padx=5, pady=5)
        self.sueldo_entry = tk.Entry(self.form_frame)
        self.sueldo_entry.grid(row=5, column=1, padx=5, pady=5)
        
        tk.Button(self.form_frame, text="Registrar", 
                  command=self.registrar_trabajador).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Crear Treeview
        self.tree = ttk.Treeview(ventana, columns=("DNI", "Nombre", "Fecha Ingreso", "Edad", 
                                                   "Sexo", "Sueldo"), show='headings')
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha Ingreso", text="Fecha Ingreso")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("Sueldo", text="Sueldo")
        
        self.tree.pack(padx=10, pady=10)
    
    def registrar_trabajador(self):
        nombre = self.nombre_entry.get()
        dni = self.dni_entry.get()
        fecha_ingreso = self.fecha_ingreso_entry.get()
        edad = self.edad_entry.get()
        sexo = self.sexo_entry.get()
        sueldo = self.sueldo_entry.get()
        
        # Validación básica de los campos
        if not (nombre and dni and fecha_ingreso and edad and sexo and sueldo):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Validar fecha
        try:
            datetime.strptime(fecha_ingreso, "%d-%m-%Y") # Convierte la cadena en objeto fecha
        except ValueError:
            messagebox.showerror("Error", "La fecha de ingreso debe tener el formato dd-mm-yyyy")
            return
        
        # Crear y guardar trabajador
        trabajador = Trabajador(nombre, dni, fecha_ingreso, edad, sexo, sueldo)
        self.trabajadores.append(trabajador)
        
        # Añadir trabajador al Treeview
        self.tree.insert("", "end", values=(dni, fecha_ingreso, edad, sexo, sueldo))
        
        # Limpiar formulario
        self.nombre_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.fecha_ingreso_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.sexo_entry.delete(0, tk.END)
        self.sueldo_entry.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", "Trabajador registrado con éxito")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = App(ventana)
    ventana.mainloop()
