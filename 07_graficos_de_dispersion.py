import matplotlib.pyplot as plt
import numpy as np
import os


os.system("cls")  

# ------------- Graficos de Dispersion -------------------
valoresX = np.array([2,9,4,11,12,9,6,5,7,8,7,2,17,])
valoresY = np.array([103,87,94,78,77,85,86, 99,86,87,88,111,86,])

valoresX2 = np.array([12,9,7,3,11,4,7,14,12,2,2,8,1,15,8])
valoresY2 = np.array([90,95,94,100,79,112,91,80,85,100,105,84,105,90,99])

plt.scatter(valoresX, valoresY, c="#fca8b1", s=120)
plt.scatter(valoresX2, valoresY2, c="#33fc72")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.show()

















