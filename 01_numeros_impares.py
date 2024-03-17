import os

# ----------------------------------------------------------------------
# Programa que muestra los 10 primeros números enteros positivos e impares.
# ----------------------------------------------------------------------

os.system("cls") 

print ("Los primeros 10 números enteros e impares son:")
print ("----------------------------------------------")

secuenciaImpar = 1
for contador in range(1, 11):
    print(contador, " - ", secuenciaImpar)
    secuenciaImpar = secuenciaImpar + 2

# El mismo programa anterior, pero con otra variante de la instrucción <for>
    

print ("\n ----------- Otra versión del mismo ejercicio -----------\n")

for control in range(1, 21, 2):
    print(control)



