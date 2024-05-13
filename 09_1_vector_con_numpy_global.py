import os
import numpy as np

# Realizar un programa que llene un vector con números enteros y lo muestre.

vector= np.array([3, 5, 7, 9, 11, 13, 15, 17, 19]) # Variable Global

# Mostrar el vector en elementos individuales y separados por un guión ------
# función -------------------------------------------------
def imprimir_vector_uno_a_uno():
    print ("\n\nElementos del vector:\n")
    for elemento in vector:
        print(elemento, end=" - ")
    print("\n")

# Mostrar el vector como un único bloque---------------------
def imprimir_vector_general():
    print(vector)
    print(type(vector))

# función principal (main)-----------------------------------
def main():
    os.system("cls")
    imprimir_vector_general()
    imprimir_vector_uno_a_uno()

# Cuerpo principal del programa----------
main()






