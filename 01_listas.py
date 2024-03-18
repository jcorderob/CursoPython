import os

# En Python existen 4 tipos de colecciones de datos:
#     Lista(list), Tupla(tuple), Conjunto(set), Diccionario(dictionary)
#
# Es lo que en otros lenguajes se conoce como Arreglos(arrays) de datos.

# LISTAS - CARACTERÍSTICAS : 
#                    <Ordenadas>, <Modificables> y <Aceptan Duplicados>

os.system("cls")


# -------------- Formas de crear una lista -------------------

listaNombres = ["Pedro","María","Orlando","Carmen"]
print (listaNombres)


# ---------------- Las listas son ordenadas -----------------
print (listaNombres); print (listaNombres); print (listaNombres)


# ---------------- Las listas aceptan duplicados -----------------
listaNombres = ["Pedro","María","Orlando","Orlando","Carmen", "María"]
print (listaNombres)


# -------------------------- Crear una lista vacía --------------
lista2 = [] ;                   
print("\nLista2 : ",lista2)


# ---------------- Longitud de una lista -----------------
print ("\nLongitud de lista : ", len(listaNombres))


# ------ Las listas soportan elementos de distinto tipo (multi type) --------
listaValores = ["Pedro",True,"Orlando",25,"Carmen", False]
print (listaValores)


# -------- El constructor de listas  --------------
listaVacia = list()
print ("\n Lista vacía:", listaVacia)

listaConDatos = list(("hola", "que tal", "bien", False))
print("\n Última lista:", listaConDatos)


