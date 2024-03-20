import os

# Realice un programa que haga uso de dos ciclos anidados y envíe mensajes
# de salida que permitan entender cómo funciona el anidamiento de ciclos.

# --------------- Ejemplo con ciclos <for> -----------------------
"""
for cont1 in range(1,6):                    # Este ciclo se ejecuta 5 veces.
    print (f"\n------- Ciclo externo - Iteración Nº {cont1} --------")
    for cont2 in range(1,4):                # Este ciclo se ejecuta 3 veces.
        print (f"\t\t Ciclo interno - {cont2} ")  # \t avanza 8 espacios
"""

# ------- Mismo ejercicio con un ciclo <for> y un <while> ---------

for cont1 in range(1,6):      # Este ciclo se ejecuta 5 veces.
    print (f"\n------- Ciclo externo - Iteración Nº {cont1} --------")
    cont2 = 1
    while cont2 <= 3 :         # Este ciclo se ejecuta 3 veces.                   
        print (f"\t\t Ciclo interno - {cont2} ")  # \t avanza 8 espacios
        cont2 +=  1
    print ("salí del ciclo interno")
