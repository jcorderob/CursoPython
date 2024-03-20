import os

# Realice un programa que permita mostrar  los 'N' primeros términos de la
# siguiente serie:
#  1, 3, 7, 15, 31, 63, 127, 255,...,N;  Donde N = (N-1)*2 + 1 y mayor a 1. 
#                         
# Además el programa debe mostrar la suma de los N primeros términos de la serie.

os.system("cls")
nTerminos = int(input("\n\nIngrese la cantidad de términos a conocer : "))

if ( nTerminos<= 1 ) :
    print("Debes ingresar un valor > 1 ")
else:
    termino = 1
    contaTerminos= 0
    sumaTerminos = 0
    while (contaTerminos < nTerminos):
        contaTerminos += 1
        print(termino,end='-')
        sumaTerminos += termino        
        termino = termino * 2 + 1
        
    
    print(f"\n\nLa sumatoria de los {nTerminos} primeros términos es : "
          f" {sumaTerminos}")


