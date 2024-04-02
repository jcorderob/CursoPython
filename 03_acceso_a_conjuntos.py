import os

# ------------------  ACCESO A CONJUNTOS ------------------------
#
# IMPORTANTE: los conjuntos No permiten el acceso a sus elementos individuales
#           a través de un índice. En su lugar debe hacerse con el ciclo <for>.

# Programa que crea un conjunto y lo muestra por pantalla

miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}

os.system("cls")
print("-----", miConjunto, "------")

#----------------------------------------------------------

print("Acceso a elementos de un conjunto con el ciclo <for> : ")
for control in miConjunto:
    print (control)

#-------- VERIFICANDO  SI UN ELEMENTO PERTENECE A UN CONJUNTO -------------
#os.system("cls")
print("-----", miConjunto, "------")
if "TRES" in miConjunto:
    print("\n 'TRES' pertenece al conjunto \n")

# ------ Un condicional dentro de un < print() > --------------------
print('OCHO' in miConjunto)   # devuelve verdadero

