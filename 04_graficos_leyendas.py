import matplotlib.pyplot as plt
import numpy as np
import os


os.system("cls")   
ypuntos = np.array([3,500,100,300,50]) 
ypuntos2 = np.array([10,100,450,50,500]) 

# -------- Cambiando la fuente de las etiquetas  -----------
diccFuenteTitulo = {'family':'serif','color':'blue','size':20}
diccFuenteEjes   = {'family':'serif','color':'darkred','size':15}

# --------------  Dibujando las etiquetas  -----------------
plt.title("TITULO DEL GRÁFICO", fontdict= diccFuenteTitulo)
plt.xlabel("Leyenda eje X", fontdict= diccFuenteEjes)
plt.ylabel("Leyenda eje Y", fontdict= diccFuenteEjes)
plt.show()

