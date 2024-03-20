import os

# Este programa NO hace uso de ciclos anidados. Se creó con fines didácticos
# como punto de aprtida para explicar ciclos anidados.

# Realice un programa que muestre la tabla de multiplicar de un número <N>
# requerido por el usuario.
"""
    Ejemplo, salida de la tabla del 7:
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    .....
    7 x 9  = 63
    7 x 10 = 70   
"""

os.system("cls")
tabla = int(input("\n\n Cuál tabla de multiplicar desea ? "))

print (F"\n\t\t \033[42m TABLA DEL {tabla}\033[0m")
for conta in range (1,11):
    print(f"\t\t{tabla} x {conta} = {tabla * conta}")

