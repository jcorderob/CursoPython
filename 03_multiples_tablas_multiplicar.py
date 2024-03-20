import os

# Realice un programa que muestre las tablas de multiplicar que se encuentren
# en un rango sugerido por el ususario.

"""
   TABLA DEL 7     TABLA DEL 8
   -----------     ------------
    7 x 1 = 7       8 X 1  = 8
    7 x 2 = 14      8 X 2  = 16
    7 x 3 = 21      8 X 3  = 24
    .....         
    7 x 9  = 63     8 X 9  = 72
    7 x 10 = 70     8 X 10 = 80  
"""

os.system("cls")
print("\n \033[42m [Ingrese el rango de las tablas a mostrar.\033[0m")
inferior = int(input("\n valor inferior ? "))
superior = int(input("\n valor superior ? "))

for conta1 in range(inferior, superior+1):
    print (F"\n\t\t \033[42m TABLA DEL {conta1}\033[0m") # Muestra encabezado
    for conta2 in range (1,11):
        print(f"\t\t{conta1} x {conta2} = {conta1 * conta2}") # Genera tabla

