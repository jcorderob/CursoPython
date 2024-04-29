import matplotlib.pyplot as plt
import numpy as np

valores = np.array([35, 25, 25, 15])
etiquetas = ["Atletismo", "Trekking", "Natación", "Tenis"]
explote = [0.15,0,0,0]
misColores = ["#ab12ba","#123cfa","#87ca54","#c8a9f0"]
#plt.pie(valores, labels = etiquetas)


#plt.pie(valores, labels = etiquetas, startangle = 90)
#plt.pie(valores, labels = etiquetas, explode = explote)

plt.pie(valores, labels = etiquetas,colors= misColores, explode = explote, shadow = True)
#plt.pie(valores, labels = etiquetas)
# misColores = ["#ab12ba","#123cfa","#87ca54","#c8a9f0"]
plt.legend(title="Deportes")
plt.show() 