import matplotlib.pyplot as plt
import numpy as np

xpuntos = np.array([0,6])      # Los arrays son similares a listas.
ypuntos = np.array([0, 500])    # Se recomiendan en tareas numéricas intensivas.

plt.plot(xpuntos, ypuntos)      # plot() sirve para crear gráficos de líneas 
plt.show()