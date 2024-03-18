import os

# Realice un programa que muestre ordenados  los elementos de una lista.
# El metodo .sort() hace ordenamiento alfanumérico.

# --------------  Ordenar cadenas de caracteres -------------- 
os.system("cls")

paises = ["Venezuela","Rusia","Japón","Dinamarca","Perú","Belgica","Australia"]
numeros =[1230, 15, 8, 45, -2, 256, -45, 38]
"""
print("\nLISTADO DE PAISES ORIGINAL",paises)
paises.sort()
print("\nLISTA DE PAISES ORDENADOS ASCENDENTE:")
print("\n",paises)

# -------------- Ordenar números -------------- 
print("------------------------")
print("\n\n\nLISTADO DE NUMEROS ORIGINAL: ",numeros)
numeros.sort()
print("\nLISTA DE NÚMEROS  ORDENADOS - ASCENDENTE:")
print("\n",numeros)


# --------------  Ordenamiento DESCENDENTE -------------- 

paises = ["Belgica","Venezuela","Rusia","Chile", "Dinamarca","Perú","Australia"]
numeros =[1230, 15, 8, 45, -2, 256, -45, 38]

print("\n\n\nListado de paises Original",paises)
paises.sort(reverse= True)
print("\nLISTA DE PAISES ORDENADOS - DESCENDENTE:")
print("\n",paises)

# -- EL ORDENAMIENTO DISTINGUE MAYÚSCULAS / MINÚSCULAS<Case Sensitive> ----- 

paises = ["belgica","Venezuela","rusia","Japón", "Dinamarca","Perú","Australia"]

print("\n\n\nLISTADO DE PAISES ORIGINAL: ",paises)
print("\nLISTADO <case sensitive> :")
paises.sort()
print("\n",paises)

"""
# -- EL ORDENAMIENTO CON FUNCIONES CLAVE (key functions) ----- 

paises = ["belgica","Venezuela","rusia","Japón", "Dinamarca","Perú","Australia"]

print("\n\n\nLISTADO DE PAISES ORIGINAL:",paises)

print("\nLISTADO con <key functions - lower> :")
paises.sort(key= str.lower)       # Puede ser tambien: <str.upper>
print("\n",paises)


