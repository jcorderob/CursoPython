import os
import numpy as np

# función -------------------------------
# Mostrar el vector individualmente y en lineas separadas ------
def imprimir_vector(p_vector):
    print ("\n\nElementos del vector:\n")
    for elemento in p_vector:
        print(elemento, end=" - ")
    print("\n")

# función -------------------------------
def crear_vector():
    vector= np.array([3, 5, 7, 9, 11, 13, 15, 17, 19]) # Variable Local
    print(vector)
    print(type(vector))

    imprimir_vector(vector)

# función principal (main)---------------
def main():
    os.system("cls")
    crear_vector()

# Cuerpo principal del programa----------
main()






