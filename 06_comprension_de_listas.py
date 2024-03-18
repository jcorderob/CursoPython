import os

#------- RECORRIENDO UNA LISTA USANDO <COMPRENSIÓN DE LISTAS>---------------
# La comprensión de listas es un método abreviado para el tratamiento de listas.

# Realice un programa que muestre los elementos de una lista.

os.system("cls")
paises = ["Perú","Venezuela","Dinamarca","Rusia","Japón", "Belgica","Australia"]
print("\nLISTA DE PAISES:\n")
[print(x) for x in paises]

# -------------------------------------------------------------------------
# Realice un programa que recorra todos los elementos de una lista y verifique
# cuáles tienen la letra 'e' en su nombre. Con ellos genera otra lista.

paises = ["Perú","Venezuela","Dinamarca","Rusia","Japón", "Belgica","Australia"]
print("\nLISTA DE PAISES:\n")
listaNueva = [control for control in paises if "e" in control]

print("\nLISTA DE PAISES con letra 'e' :\n")
print (listaNueva)


