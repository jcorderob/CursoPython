import tkinter as tk  # Importar el módulo tkinter

# Crea el objeto de la clase ventana, pero no lo muestra  
ventana = tk.Tk()
   
ventana.geometry("500x400")                 # ancho x alto.
ventana.title("ProfesorenVideo")            # Pone título a la ventana.

icono = tk.PhotoImage(file="ProfesorenVideo.png") # carga la imagen.
ventana.iconphoto(True, icono)  # Establece el ícono de ventana.

#------------------- Creación de widgets tipo Botón
#
button = tk.Button(ventana,text="Botón 1")
button.pack()   # Visualiza la ventana


#------------------- Creación de Frames (Marcos)
#
# Un Frame (Marco) es un cuadro dentro del cual podemos ir poniendo objetos
# llamados widgets.

frame1 = tk.Frame(ventana)        # Hay que especificar la ventana destino 
frame1.configure(width=300, height=300,
                  highlightbackground="black",  # Color del borde del marco
                  highlightthickness=5)         # Grosor del borde.
                                      #Al no tener atributos no se ve.

frame1.pack()   #  Visualiza el frame. 

button2 = tk.Button(frame1,text="Botón 2")
button2.pack() 

frame1.pack_propagate(False) # El contenedor No se ajusta al tamaño del widget


#------------------- Creación de LabelFrames (Marcos de etiqueta)
#
labelFrame = tk.LabelFrame(ventana, 
                           text="Contenedor de Widgets",
                           bg="cyan")
                       # debo eliminar 200 y 100. cambiar a 20 y 10
                       # sino el texto del 'boton' no se verá

labelFrame.configure(width=300, height=300)
labelFrame.pack()
labelFrame.pack_propagate(False)

button3 = tk.Button(labelFrame,text="Botón 3", font=("Arial", 16))
button3.pack()



# ----------------------- Agregar Checkbuttons al frame1
check_var1 = tk.IntVar()  # variable entera o Booleana
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()

checkbutton1 = tk.Checkbutton(labelFrame, text="Opción 1", variable=check_var1, )
checkbutton1.pack()
checkbutton2 = tk.Checkbutton(labelFrame, text="Opción 2", variable=check_var2)
checkbutton2.pack()
checkbutton3 = tk.Checkbutton(labelFrame, text="Opción 3", variable=check_var3)
checkbutton3.pack()

# ----------------------Agregar Radiobuttons al frame1
radio_var = tk.IntVar()
radio_var.set(1)  # Valor inicial seleccionado

radiobutton1 = tk.Radiobutton(labelFrame, text="Opción A", variable=radio_var, value=1)
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(labelFrame, text="Opción B", variable=radio_var, value=2)
radiobutton2.pack()
radiobutton3 = tk.Radiobutton(labelFrame, text="Opción C", variable=radio_var, value=3)
radiobutton3.pack()


ventana.mainloop()

