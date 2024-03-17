import os, math


#Programa que lee un número desde el teclado y verifica si es primo o no.

#NOTA: Un número N es <primo> si sólamente tiene 2 divisores, que son el <1> y 
#    el mismo número N. Nos referimos a división entera exacta, con resto == 0.

# METODOLOGÍA: Para la versión mejorada de este algoritmo se procesan los 
#              posibles divisores  que hay entre 2 y la parte entera de la raíz
#              cuadrada del número <N>.
#              Se verifican todos sus posible divisores  que hay entre 
#               2 ...y.... parte-entera (raiz cuadrada(N))

#    Ejemplo : Sea el número  N = 17
#              parte entera de su raiz cuadrada es = 4.
#              Posibles divisores de  <N>: (1), 2, 3, 4    (17)

#    Ejemplo : Sea el número  <8>
# Posibles divisores de  <N>: (1), (2), 3, (4), 5, 6, 7, (8)

#    Ejemplo : Sea el número  <7>
# Posibles divisores de  <N>: (1), 2, 3, 4, 5, 6, (7) 

os.system("cls")

print ("\n\nIngrese número entero positivo > 1"); numero = int(input())


esPrimo = True
raizCuadrada = int(math.sqrt(numero))
for indice in range(2, raizCuadrada+1):   # No contemplar a   '1'   ni a  'numero'
    if (numero % indice == 0):
        esPrimo = False
        break

if esPrimo  : print(f"El número {numero} es Primo")
else:  print(f"El número {numero} No es Primo")

