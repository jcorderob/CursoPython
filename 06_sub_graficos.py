import matplotlib.pyplot as plt
import numpy as np
import os


os.system("cls")   
ypuntos = np.array([3,500,100,300,50]) 
ypuntos2 = np.array([10,100,450,50,500]) 

# -------- Cambiando la fuente de las etiquetas  -----------
diccFuenteTitulo = {'family':'serif','color':'blue','size':20}
diccFuenteEjes   = {'family':'serif','color':'darkred','size':15}


# -------- Dibujando el gráfico 1 --------------------
plt.subplot(2, 1, 1) # subplot (num filas, num columnas, orden-> 1, primero)
plt.plot(ypuntos)

# -------- Dibujando el gráfico 2 --------------------
plt.subplot(2, 1, 2)
plt.plot(ypuntos2)   # subplot (num filas, num columnas, orden-> 2, segundo)


# ------------  Dibujando la rejilla o cuadrícula  -----------------
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.show()

