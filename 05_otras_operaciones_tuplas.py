import os

# Otras operaciones sobre una tupla: UNIÓN de Tuplas.
"""
letras = ("UNO","DOS","TRES","CUATRO","CINCO")
numeros   = (1, 2, 3, 4, 5)

os.system("cls")

print("\n Tupla letras :")
print(letras)
print("\n Tupla numeros :")
print(numeros)

# ------------- Unión de tuplas

numerosLetras = letras + numeros
print("\n Tupla unión :")
print(numerosLetras)



# ----------------  Multiplicando los valores de una tupla ---------

numLetras = ("UNO","DOS","TRES","CUATRO","CINCO")
numeros   = (1, 2, 3, 4, 5)

letrasDuplicada   = numLetras * 2
numerosTriplicada = numeros * 3

print("\n Letras duplicada :")
print(letrasDuplicada)
print("\n Numeros triplicada :")
print(numerosTriplicada)

"""

# ---------------------- EMPACANDO / DESEMPACANDO TUPLAS ---------------------

autos = ("Malibú", "Aveo", "Volkswagen")      # Empacando

print("\n\n Tupla Autos:",end=" "); print (autos)

(grande, mediano, chico) = autos              # Desempacando

print("\n")
print(grande)
print(mediano)
print(chico)


