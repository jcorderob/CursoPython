import tkinter as tk
from tkinter import ttk

# Función para actualizar la Progressbar
def actualizar_progressbar():
    for i in range(101):
        progress_var.set(i)
        ventana.update_idletasks()  # Asegurar que la barra de progreso se redibuje
        ventana.after(15)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets Tkinter y ttk")

# Crear un Notebook
notebook = ttk.Notebook(ventana)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# Crear Frames para cada pestaña del Notebook
frame1 = ttk.Frame(notebook, padding="10")
frame2 = ttk.Frame(notebook, padding="10")
frame3 = ttk.Frame(notebook, padding="10")
notebook.add(frame1, text='Pestaña 1')
notebook.add(frame2, text='Pestaña 2')
notebook.add(frame3, text='Pestaña 3')

# Listbox en la primera pestaña
listbox_label = ttk.Label(frame1, text="Listbox:")
listbox_label.pack(anchor=tk.W)
listbox = tk.Listbox(frame1, height=10)
listbox.pack(padx=10, pady=10, fill='both', expand=True)
for item in ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]:
    listbox.insert(tk.END, item)

# Combobox en la primera pestaña
combobox_label = ttk.Label(frame1, text="Combobox:")
combobox_label.pack(anchor=tk.W)
combobox = ttk.Combobox(frame1, values=["Opción 1", "Opción 2", "Opción 3"])
combobox.pack(padx=10, pady=10, fill='both', expand=True)

# Textarea en la segunda pestaña
textarea_label = ttk.Label(frame2, text="Textarea:")
textarea_label.pack(anchor=tk.W)
textarea = tk.Text(frame2, height=10)
textarea.pack(padx=10, pady=10, fill='both', expand=True)

# Treeview en la tercera pestaña
treeview_label = ttk.Label(frame3, text="Treeview:")
treeview_label.pack(anchor=tk.W)
treeview = ttk.Treeview(frame3, columns=("Columna_1", "Columna_2"), show="headings")
treeview.heading("Columna_1", text="Columna 1")
treeview.heading("Columna_2", text="Columna 2")
treeview.pack(padx=10, pady=10, fill='both', expand=True)

# Le insertamos valores al Treeview
treeview.insert("", "end", values=("Item 1", "Valor 1"))
treeview.insert("", "end", values=("Item 2", "Valor 2"))

# Progressbar
progressbar_label = ttk.Label(ventana, text="Progressbar:")
progressbar_label.pack(anchor=tk.W)
progress_var = tk.IntVar()                      # variable de control
progressbar = ttk.Progressbar(ventana, orient="horizontal", length=300, 
                              mode="determinate", variable=progress_var)
progressbar.pack(padx=10, pady=10)
start_button = ttk.Button(ventana, text="Iniciar", command=actualizar_progressbar)
start_button.pack(padx=10, pady=10)

# Iniciar el loop principal
ventana.mainloop()

