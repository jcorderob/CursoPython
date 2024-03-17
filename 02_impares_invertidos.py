import os

# ----------------------------------------------------------------------
# Programa que muestra los 10 primeros números enteros positivos e impares
# pero en forma invertida: 19- 17- 15- 13- 11- 9- 7- 5- 3- 1.
# ----------------------------------------------------------------------

os.system("cls") 
  
print ("\n -------------- Números Positivos invertidos -----------\n")

secuenciaImpar = 19; 
for control in range(1, 11):
    print(control, " - ", secuenciaImpar)
    secuenciaImpar = secuenciaImpar - 2
 
# ----------------------------------------------------------------------
# Programa que muestra los 0 primeros números enteros negativos e impares
# pero en forma invertida: -19 -17 -15 -13 -11 -9 -7 -5 -3 -1.
# ----------------------------------------------------------------------
    
print ("\n --------------- Números negativos invertidos-----------\n")

for control in range(-19, -1, 2):
    print(control)
    
 