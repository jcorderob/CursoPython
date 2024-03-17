import os

# Programa que permite  declarar 4 variables, darles un valor inicial
# (inicializarlas)  y realizar las 4 operaciones  aritmeticas basicas

val1, val2, val3, val4 = 5, 10, 15, 20
rSuma = val1 + val2
rResta = val3 - val4
rMulti = val1 * val2
rDiviEntera = val3 // val1
rDiviFlotante = val3 / val1

os.system('cls')
print("\n\n\n")
print (rSuma, rResta, rMulti, rDiviEntera ,rDiviFlotante)

print ("La suma es = ", rSuma)

# CADENAS  f
print ("Suma= {rSuma} Resta = {rResta}, Multip = {rMulti} División = {rDiviEntera}")
print (f"Suma= {rSuma} Resta = {rResta}, Multip = {rMulti} División = {rDiviFlotante}")

print (f"La suma es = {rSuma}")

print (f"\nSuma= {rSuma} \nResta = {rResta} \nMultip = {rMulti} \nDivisión = {rDiviEntera}")





