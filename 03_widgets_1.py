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
#button.pack(side='left', anchor="nw")    # Visualiza la ventana

button2 = tk.Button(ventana,text="Botón 2")
button2.pack()
#button2.pack(side='left', anchor="nw")

button3 = tk.Button(ventana,text="Botón 3", font=("Arial", 16))
button3.pack()

#------------------- Creación de Frames (Marcos)
#
# Un Frame (Marco) es un cuadro dentro del cual podemos ir poniendo objetos
# llamados widgets.

frame1 = tk.Frame(ventana)        # Hay que especificar la ventana destino 
frame1.configure(width=300, height=300,
                  highlightbackground="black",  # Color del borde del marco
                  highlightthickness=5)         # Grosor del borde.
                                      #Al no tener atributos no se ve.

#frame1.pack_propagate(False) # El contenedor No se ajusta al tamaño del widget

frame1.pack()   #  frame en la ventana. 
frame1.pack_propagate(False)


#------------------- Creación de LabelFrames (Marcos de etiqueta)
#
labelFrame = tk.LabelFrame(ventana, 
                           text="Contenedor de Widgets",
                           bg="blue")



labelFrame.configure(width=300, height=300)
labelFrame.pack()

ventana.mainloop()


