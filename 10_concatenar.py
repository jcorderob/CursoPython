import os


# **** Existen 4 métodos para añadir elementos a listas  ****


# List Concatenacion: Podemos usar el operador '+' para concatenar (unir)
#           múltiples listas y así generar una nueva que las contiene a todas.

os.system("cls")

# -------------------- EJERCICIO 1 -----------------------
# Programa que permita   CONCATENAR (UNIR) varias listas 

listaPares    = [2, 4, 10, 20, 30]
listaImpares  = [3, 7, 9, 17, 21]
listaNegativos= [-5, -8, -11, -12, -19] 
listaPrimos   = [5, 7, 11, 17, 23]

listaUnida = listaPares + listaImpares + listaNegativos + listaPrimos

print(f"\nLista de Pares : {listaPares}")
print(f"\nLista de Impares : {listaImpares}")
print(f"\nLista de negativos : {listaNegativos}")
print(f"\nLista de Primos : {listaPrimos}")

print("\033[32m","\033[1m","\n\nVERDE")  #activar color verde

print(f"\nLista Concatenada : {listaUnida}")

print("\033[0m","\n\nTEXTO NORMAL")   #desactivar color y volver a blanco

#  https://gist.github.com/kamito/704813 - Listado de colores     




