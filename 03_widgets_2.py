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
button.pack( anchor="nw", padx=50)    # Visualiza la ventana


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


labelFrame.configure(width=300, height=300)
labelFrame.pack()
labelFrame.pack_propagate(False) # Evita que el labelFrame se recoja

button3 = tk.Button(labelFrame,text="Botón 3", font=("Arial", 16))
button3.pack()


ventana.mainloop()

