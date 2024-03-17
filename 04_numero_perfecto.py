import os


# Programa que lee un número <N> desde el teclado y verifica si es perfecto.

# NOTA: Los números perfectos son aquellos iguales a la suma de sus divisores:
# IMPORTANTE: Dentro de los posibles divisores NO debe incluirse el propio <N>.

# Ejemplo: Para N = 6.  probar con: 1, 2, 3, 4, 5, 
#         <6> se puede dividir por 1, 2 y 3. y cuando sumas esos números, 
#         el resultado es <6>. Por tanto <6> es perfecto

# METODOLOGÍA: para un número <N> se verifican todos sus posible divisores
#              (excepto N), y se van acumulando. Si el acumulado es = <N>
#              es perfecto sino No lo es.    

# Ejemplo : Sea el número  <N>
# Posibles divisores de  <N>: 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., N-1

#    Ejemplo : Sea el número  <8>
# Posibles divisores de  <8>: (1), (2), 3, (4), 5, 6, 7

#    Ejemplo1 : Sea el número  <6> es perfecto.
# Posibles divisores de  <6>: (1), (2), (3), 4, 5

#    Ejemplo2 : Sea el número  <28> es perfecto.
# Posibles divisores de  <6>: (1), (2), 3, (4), 5,6, (7), 8, 9,10,
#                             11, 12, 13, (14), 15, 16, 17, 18, 19, 20,
#                             21, 22, 23, 24, 25, 26, 27.

os.system("cls")

print ("\n\nIngrese número entero positivo > 1 "); numero = int(input())

sumaDivisores = 1
for indice in range(2, numero):
    if (numero % indice == 0):
        sumaDivisores += indice

if (sumaDivisores == numero): print(f"El número {numero} es Perfecto")
else:  print(f"El número {numero} No es Perfecto")

