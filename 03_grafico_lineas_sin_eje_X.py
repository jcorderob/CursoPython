import matplotlib.pyplot as plt
import numpy as np


# Si no damos los puntos X, python asume por defecto los valores 1, 2, 3,...

#xpuntos = np.array([2,3,4,5,6])      
ypuntos = np.array([3,500,100,300,50])    

#plt.plot(ypuntos, "o") 


#plt.plot(ypuntos, marker= "o") 
#plt.plot(ypuntos, marker= "o", ms=20) # markersize
#plt.plot(ypuntos, marker= "o", ms=20, mec= '#33ffac') # markeredgecolor
#plt.plot(ypuntos, marker= "o", ms=20, mec= 'b', mfc='r') # markerfacecolor
#plt.plot(ypuntos, marker= "o", ms=20, mec= 'b', mfc='r', ls= "dashed", lw=6)
                                              # linestyle  , linewidth      

#plt.show()

ypuntos = np.array([3,500,100,300,50]) 
ypuntos2 = np.array([10,100,450,50,500]) 
plt.plot(ypuntos)
plt.plot(ypuntos2)
plt.show()

# Trabajando con marcadores en lugar de Líneas
#plt.plot(ypuntos,marker="o") 
#plt.show()
