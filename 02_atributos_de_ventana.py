import tkinter as tk  # Importar el módulo tkinter

ventana = tk.Tk()     # Crea el objeto de la clase ventana, pero no lo muestra.


ventana.title("ProfesorenVideo") # Pone título a la ventana.
#ventana.geometry("500x400")      # ancho x alto.

#ventana.minsize(150, 200)        # Mínimo tamaño permitido.
#ventana.maxsize(800, 700)        # Máximo tamaño permitido.

#icono = tk.PhotoImage(file="ProfesorenVideo.png") # carga la imagen.
#ventana.iconphoto(True, icono)  # Establece el ícono de ventana.
                                # 'True' para que el icono se muestre también
                                # en la barra de tareas.

ventana.iconbitmap("profesorenvideo.ico") # --> Es la forma más sencilla

ventana.configure(bg="#9bfac7")  # BackGround 

#ventana.resizable(False,True)

#ventana.geometry("500x400+500+500")  # ancho x alto + separa izq + separa arriba.


#Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

#Establecer el tamaño de la ventana al tamaño de la pantalla
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

ventana.mainloop() # "mainloop" debe ser la última instrucción que se coloca. 


