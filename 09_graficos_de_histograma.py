import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(40,5,250) # (La media, la desviación estándar, total)

plt.hist(x)
plt.show() 