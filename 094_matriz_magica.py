import os
import numpy as np

# Programa que permite generar y mostrar una matriz mágica. 
#
# IMPORTANTE: La matriz mágica es aquella en la cual toda suma que se haga
# en una linea recta que atraviese toda la matriz, da siempre el mismo valor.
#
# Ejemplo: En la siguiente matriz, toda suma en linea recta y atravesando
#          toda la matriz nos da el valor <15>.
#
#          8  1  6
#          3  5  7
#          4  9  2


matriz_magica = np.zeros((5,5), dtype=int)


# ----------------- Función -----------------------
def generar_matriz_magica():
    dimensiones   = matriz_magica.shape   # Devuelva una tupla(fil,col) -> 5 x 5
    total_filas    = dimensiones[0] - 1 # -1 para adpatarlo a Python.
    total_columnas = dimensiones[1] - 1 # -1 para adpatarlo a Python.  
   
    fila = 0                      # primero fila
    columna = total_columnas // 2 # calcula la columna del medio.
    contador = 0

    #             (total_filas + 1) * (total_columnas + 1)    
    while contador < dimensiones[0] * dimensiones[1]:
        contador += 1
        matriz_magica[fila,columna] = contador

        fila -= 1 ; columna += 1  # Para avanzar a la posición inmediata superior derecha
                                  # de la matriz.
        
        if (fila < 0) and (columna <= total_columnas):    # CASO 1
                                # Desbordó la fila pero las columnas  NO.
            fila = total_filas   # el indice va a la última fila.

        elif  (columna > total_columnas)  and (fila >= 0):   # CASO 2
                              # Desbordó la columna pero las filas NO.  
            columna = 0       # Vuelve el indice a la primera columna.

        elif (fila < 0 ) and (columna > total_columnas):  # CASO 3
                                              # Desbordó filas y columnas.
            fila += 2 ; columna -= 1          # Debajo de donde partio.

        elif matriz_magica[fila,columna] != 0 :            # CASO 4
                                              # posición ocupada
            fila += 2 ; columna -= 1          # Debajo de donde partio.
                                              # Igual al CASO 3.


# ----------- Función  ------------------------------------
def mostrar_matriz_magica():
    print("\n------ Matriz Mágica -------")
    for fila in range(matriz_magica.shape[0]):  # Recorremos las filas
        print("\n")
        for columna in range(matriz_magica.shape[1]):  # Recorremos las columnas
            print(f"{matriz_magica[fila, columna]:>6}", end="")  

# ----------- Función  ------------------------------------
def main():
    os.system("cls")
    generar_matriz_magica()
    mostrar_matriz_magica() ; print("\n")

# ------ Cuerpo principal(main) del programa ------
main()





