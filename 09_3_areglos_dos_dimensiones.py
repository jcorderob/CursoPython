import os
import numpy as np

# Programa que llena una matriz LOCAL 4x4  con números aleatorios entre 0 y 100 y 
# luego imprima dicha matriz.
#

def mostrar_matriz_uno_a_uno(p_matriz):
    # Mostrar la matriz
    for fila in range(4):  # Iterar sobre filas
        print("\n")
        for columna in range(4):  # Iterar sobre columnas
            print(f"{p_matriz[fila, columna]:>5}", end=" ")  
            # '<' indica alineación a la izquierda y '10' es el ancho fijo

    input("\n\nPress any key...")

def crear_matriz():
    # Crear una matriz vacía con la biblioteca numpy
    #matriz_vacia = np.empty((4, 4), dtype=int)

    # Crear una matriz llena de "ceros" con la biblioteca numpy
    #matriz_llena_de_ceros = np.zeros((4, 4), dtype=int)

    # Llenar la matriz con números aleatorios
    matriz_llena = np.random.randint(0, 100, size=(4, 4))  # Números aleatorios entre 0 y 99

    print("\n",matriz_llena)
    print(type(matriz_llena))

    mostrar_matriz_uno_a_uno(matriz_llena)


# ----- Función principal (main) del programa ----------
def main():
    os.system("cls")
    crear_matriz()

# Cuerpo principal del programa------------------------
main()
