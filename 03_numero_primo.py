import os


#Programa que lee un número desde el teclado y verifica si es primo o no.

#NOTA: Un número N es <primo> si sólamente tiene 2 divisores, que son el <1> y 
#    el mismo número N. Nos referimos a división entera exacta, con resto == 0.

# METODOLOGÍA: para un número <N> se verifican todos sus posible divisores y
#              se van contando. Si la cuenta es = 2, es primo sino No lo es.    

#    Ejemplo : Sea el número  <N>
# Posibles divisores de  <N>: (1), 2, 3, 4, 5, 6, 7, 8, 9, ..., (N)

#    Ejemplo : Sea el número  <8>
# Posibles divisores de  <N>: (1), (2), 3, (4), 5, 6, 7, (8)

#    Ejemplo : Sea el número  <7>
# Posibles divisores de  <N>: (1), 2, 3, 4, 5, 6, (7) 

os.system("cls")

print ("\n\nIngrese número entero positivo > 1"); numero = int(input())

cuentaDivisores = 2
for indice in range(2, numero):   # No contemplar a   '1'   ni a  'numero'
    if (numero % indice == 0):
        cuentaDivisores += 1

if (cuentaDivisores == 2): print(f"El número {numero} es Primo")
else:  print(f"El número {numero} No es Primo")

