import matplotlib.pyplot as plt
import numpy as np
import os

x = np.array(["Producto1", "Producto2", "Producto3", "Producto4", "Producto5"])
y = np.array([3, 8, 1, 10, 4])

os.system("cls")

# ----- Dibujando gráficos de barras ----------
#plt.bar(x,y)  # Verticales


plt.barh(x,y)  # Horizontales
#plt.bar(x,y, color="green", width=0.5)  # con color y grosor
plt.show()
















