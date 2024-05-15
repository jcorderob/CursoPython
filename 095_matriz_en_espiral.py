import os
import numpy as np

# Programa que permite generar y mostrar una matriz en forma de Espiral. 
#
#          1  2  3
#          8  9  4
#          7  6  5

# ----------- Función  ------------------------------------
def mostrar_matriz_espiral(p_matriz_espiral):
    print("\n------ Matriz Mágica -------")
    for fila in range(p_matriz_espiral.shape[0]):  # Recorremos las filas
        print("\n")
        for columna in range(p_matriz_espiral.shape[1]):  # Recorremos las columnas
            print(f"{p_matriz_espiral[fila, columna]:>6}", end="")  

# ----------------- Función -----------------------
def generar_matriz_espiral():
    matriz_espiral = np.empty((5,5), dtype=int)
    dimensiones   = matriz_espiral.shape   # Devuelva una tupla(fil,col) -> 5 x 5
    total_filas    = dimensiones[0] - 1 # -1 para adpatarlo a Python.
    total_columnas = dimensiones[1] - 1 # -1 para adpatarlo a Python.  
   
    fila= columna= contador = 0 
    sentido = 'dere'
    lim_superior = 0;   lim_derecha = total_columnas 
    lim_izquierda = 0 ; lim_abajo = total_filas

    #             (total_filas + 1) * (total_columnas + 1)    
    while contador < dimensiones[0] * dimensiones[1]:
        contador += 1; 
        matriz_espiral[fila,columna] = contador
        #print(fila,",",columna,"->",contador)
        if ( sentido == 'dere' )  : columna += 1             # avanza columna.
        elif  (sentido == 'sube') : fila += 1                # sube fila.
        elif (sentido == 'izqi')  : columna -= 1             # disminuye columna.
        else                      : fila -= 1                # baja fila.

        if (columna > lim_derecha)      : sentido = 'sube' ; fila += 1 ; columna -= 1
        elif (fila  > lim_abajo)        : sentido = 'izqi' ; columna -= 1 ; fila -= 1
        elif (columna <  lim_izquierda) : sentido = 'baja' ; fila -= 1 ; columna += 1
        elif (fila  == lim_superior) and (sentido == 'baja') : 
            sentido = 'dere' ; columna += 1 ; fila += 1
            # cerrar el cajón de los límites
            lim_derecha -= 1 ; lim_abajo -=1; lim_izquierda += 1 ;  lim_superior += 1
    
    mostrar_matriz_espiral(matriz_espiral) ; print("\n")                                 

# ----------- Función  ------------------------------------
def main():
    os.system("cls")
    generar_matriz_espiral()

# ------ Cuerpo principal(main) del programa ------
main()





