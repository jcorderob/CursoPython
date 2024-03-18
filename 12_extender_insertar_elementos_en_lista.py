import os

# **** Existen 4 métodos para añadir elementos a listas  ****

# append(): Añade elementos al final de la lista.
# insert(): Inserta el elemento en el índice dado y desplaza todo lo demás.
# extend(): Extiende la lista mediante el añadido de elementos iterables.
#           Elementos iterables son: Listas, Tuplas y Cadenas (strings).
# List Concatenacion: Podemos usar el operador '+' para concatenar (unir)
#           múltiples listas y así generar una nueva que las contiene a todas.

os.system("cls")

# -------------------- EJERCICIO 1 -----------------------
# Programa que permita insertar  elementos en cualquier posición de una lista. 


listaHeterogenea = [1, 2, 3, 4, 5]

"""
print(f'\nLista Actual: {listaHeterogenea}')

print("\n\nVamos a añadir elementos a la lista: \n")
num = int(input("\nIngrese un número para añadir a la Lista:\n"))

index = int(input(f'Ingrese una posición entre 0 y {len(listaHeterogenea) - 1} \
    donde desee insertar el nuevo número:\n'))

listaHeterogenea.insert(index, num)

print(f'Lista de números actualizada {listaHeterogenea}')

"""





# -------------------- EJERCICIO 2 -----------------------
# Programa que permita extender añadir elementos iterables a una lista.
# Elementos iterables pueden ser: Listas, Tuplas, Strings.

# IMPORTANTE: Los elementos nuevos pueden ser de distintos tipos. 

listaHeterogenea = [1, 2, 3, 4, 5]
print(f'\nLista Actual: {listaHeterogenea}\n')

listaHeterogenea.extend([-1, -2,"CASA", True, False])  # Añadiendo una Lista

print("\n",listaHeterogenea)

listaHeterogenea.extend((3, 4))  # Añadiendo una tupla

print("\n",listaHeterogenea)

listaHeterogenea.extend("ABC")  # Añadiendo elementos de cadena (string)

print("\n",listaHeterogenea)

listaHeterogenea.extend(["ABC","HOLA", "ProfesorenVideo"]) # Añade lista

print("\n",listaHeterogenea)

