import os

# **** Existen 4 Métodos para añadir elementos a listas  ****

# append(): Añade elementos al final de la lista.
# insert(): Inserta el elemento en el índice dado y desplaza todo lo demás.
# extend(): Extiende la lista mediante el añadido de elementos iterables.
#           Elementos iterables son: Listas, Tuplas y Cadenas (strings).
# Concatenacion de Lista: Podemos usar el operador '+' para concatenar (unir)
#           múltiples listas y así generar una nueva que las contiene a todas.

os.system("cls")

# -------------------- EJERCICIO 1 -----------------------

# Se dese un programa que permita crear una lista de elementos 
# y luego genere una salida en pantalla de los elementos almacenados.

print("\n\nLista Original de frutas:")
frutas = ["Manzana", "Banana", "Mora", "Naranja"]

print(frutas)


# -------------------- EJERCICIO 2 -----------------------


# Programa que añade un elemento nuevo a la Lista. El nuevo elemento se genera
# internamente desde el programa.

print("\n\nLe vamos a agregar una fruta nueva generada internamente:")
frutas.append("Sandía")
print("\n\nLista Modificada con la adición de una nueva fruta:")
print(frutas)

"""
# -------------------- EJERCICIO 3 -----------------------

# Programa que añade un elemento nuevo a la Lista. El nuevo elemento debe
# ingresar por teclado.


nuevaFruta = input("\nIngrese nueva fruta: ")

# Mostrar la lista Modificada de las frutas - Parte 2.
frutas.append(nuevaFruta)
print("\n\nLista Modificada de frutas:")
print(frutas)

"""

# -------------------- EJERCICIO 4 -----------------------

# Programa que añade Múltiples  elementos a la Lista. Los nuevos elementos
# deben ingresar por teclado.



cantidad = int(input("\n\nCuántos elementos nuevos dese ingresar?"))

for control in range(cantidad):   # El ciclo va desde cero(0) hasta uno(1)
    nuevaFruta = input("\nIngrese nueva fruta: ")
    frutas.append(nuevaFruta)

# Mostrar la lista Modificada de las frutas - Parte 2.

print("\n\nLista Modificada de frutas:\n")
print(frutas)


