import os

# Programa que lee un número entero y verifica si es par o impar
# NOTA: Un número es par si el resto de su división entre 2 es cero.

os.system('cls')
print("\n\nIngrese un número entero > 0")
numero = int(input())  # El 'input()' SIEMPRE devuelve una cadena

if numero % 2 == 0 :
    print (f"\nEl número  {numero} es < par >")
else:
    print (f"\nEl número {numero} es < impar >")