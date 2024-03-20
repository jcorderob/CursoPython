import os

os.system("cls")

# Programa que lee un número entero positivo por teclado y determina
# si es capicúa. Un número capicúa es aquel que se lee igual hacia
#  adelante que hacia atrás. Ejms:   1331,   4224,  765567 .

"""------------------------------------------------------------------
SOLUCIÓN: Este ejercicio se resuelve trabajando con los cocientes (//)
          y los restos (%) del número ingresado.
          Dentro de un ciclo se hace divisiones por <10>. La división
          con <//> para obtener el cociente. La división con <%> para
          obtener el resto o resíduo. Con este residuo se forma un
          segundo número. 
          Al terminar el ciclo se compara el núero original con el 
          segundo número que se formó con los resíduos. Si son iguales
          entonces el número original es CAPICÚA.
------------------------------------------------------------------"""


# """------------------------------------------------------------------
numero = int(input("\n\n Ingrese un número entero positivo: "))

auxiliar = numero

numeroInvertido = 0

while auxiliar != 0 :
    cociente = auxiliar // 10
    resto    = auxiliar %  10
    numeroInvertido = numeroInvertido * 10 + resto
    auxiliar = cociente
else:
    if numero == numeroInvertido :
        print (f"\n\n El número {numero} es Capicúa")
    else:
        print (f"\n\n El número {numero} No es Capicúa")
# ------------------------------------------------------------------"""


