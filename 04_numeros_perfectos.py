import os, time

# Realizar un programa que permita leer una lista de números enteros positivos
# que termina al ingresar el valor <0>.
# Con cada número ingresado el programa verificará si es perfecto o no. 
#
# Recuerde que un número perfecto es aquel cuya suma de todos sus divisores 
# (excepto él) da un valor equivalente al número mismo.
#
# Ejemplo: <6> es un número perfecto, pues sus divisores sin incluirlo a él
#          son: 1, 2, 3      y la suma de ellos 1 + 2 + 3 = <6>

continuar = True

while continuar :
    os.system("cls")
    print("\n\033[43m \033[30m << ESTE PROGRAMA VERIFICA SI EL NÚMERO QUE"
          " USTED INGRESE ES PERFECTO >>\033[0m")
    
    numero = int(input("\nIngrese un número (\033[32m 0 para finalizar"
                       " \033[0m) : "))
    
    if (numero == 0): 
        continuar = False; continue 

    sumaDivisores = 0
    for control in range(1, numero): # El ciclo 'for' llegará hasta numero-1
        if (numero % control == 0):
            sumaDivisores += control
    
    if sumaDivisores == numero :
        print (f"El número {numero} es perfecto !!! ")
    else:
        print (f"El número {numero} No es perfecto !!! ")

    time.sleep(4)

# Fin del programa
    