import os

# IMPORTANTE: LAS TUPLAS TIENEN LAS SIGUIENTES CARACTERÍSTICAS:
#      ORDENADAS, NO SE PUEDEN MODIFICAR y  ACEPTAN DUPLICADOS.
#
# Las tuplas se escriben con paréntesis "()" y se indizan con "[]".
#
# El manejo de los índices en las TUPLAS es igual que en las LISTAS.
#

# ------ Programa que crea una tupla y la muestra por pantalla ------


miTupla = ("UNO","DOS","TRES","CUATRO","CINCO")

os.system("cls")

print(f"\n\nLa tupla completa es : \033[32m {miTupla} \033[0m")



# ------ Las tuplas aceptan valores duplicados --- ------

miTupla = ("UNO","DOS","TRES","UNO","CINCO","DOS")

#os.system("cls")

print(f"\n\nTupla con duplicados : \033[32m {miTupla} \033[0m")


# -----------  Acceso a elementos individuales en una tupla ------

miTupla = ("UNO","DOS","TRES","UNO","CINCO","DOS")

#os.system("cls")

print(miTupla)
print("\n\nEl tercer elemento (posic. 2) de la tupla es :" 
"\033[32m", miTupla[2], "\033[0m")



"""
# --------------  LAS TUPLAS NO PUEDEN MODIFICARSE ------------------
# Programa que intenta modificar un elemento de la tupla y genera <ERROR>

miTupla[2] = "SEIS"   # Esto no está permitido.

print(f"\n\nLa tupla completa es : \033[32m {miTupla} \033[0m")


#--------------  AÑADIR ELEMENTOS A UNA TUPLA ------------------
# Realice un programa que le añada (agregar al final) elementos a una tupla.
# NOTA 2 : Recuerde que las tuplas NO pueden modificarse

# La solución para añadir elementos al final de la tupla es 
# crear una nueva tupla con los elementos que serán añadidos y
# luego concatenar las dos tuplas para generar una TERCERA tupla.

tupla1 = ("UNO","DOS","TRES")
tupla2 = (1,2,3)

#os.system("cls")

print("\n Tupla 1 :", tupla1)
print("\n Tupla 2 :", tupla2)

tupla3 = tupla1 + tupla2
print("\n Tupla 3 :", tupla3)

"""
