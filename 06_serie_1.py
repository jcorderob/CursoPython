import os

# realice un programa que calcule y muestre los <N> primeros términos de la
# siguiente sucesión:
#    1/1! + 2/2! + 3/3! + 4/4! + 5/5! + ... + n/n!
#  
# Ejemplos de factorial: 
#                     5! = 5 x 4 x 3 x 2 x 1 = 120
#                     7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040
#
# El programa debe mostrar también la sumatoria de los <N> términos (SERIE).

os.system("cls")
numTerminos = int(input("\n Indique el número de términos a mostrar : "))

sumaTerminos = 0
# El primer ciclo es para mostrar los <N> términos
print ("\n Los términos de la sucesión son: ")
for control1 in range (1, numTerminos+1): 
    factorial = 1
    for control2 in range (control1, 0, -1):
        factorial *= control2
    
    print (f"\033[32m{control1}/{factorial}  \033[0m", end=' + ')

    sumaTerminos += (control1/factorial)

print (f"\n\n La sumatoria total (SERIE) es :\033[32m {sumaTerminos}\033[0m")

