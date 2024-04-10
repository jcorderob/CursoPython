import os

# ---------------------- MÉTODO: .union() ---------------------------
# El método ".union()", al igual que el método ".update()", permite unir 2 o más
# conjuntos. También permiten unir conjuntos  con otras colecciones de datos 
# como listas y tuplas. 
conjuntoColores = {"Amarillo", "Violeta", "Verde"}
listaVariada = ["Aguila", "Violeta", "Gato", False, 25]
tupla = ("Perro", 76)

conjuntoResultante = conjuntoColores.union(listaVariada, tupla)

os.system("cls")
print("\n\n Conjunto colores: "); print(conjuntoColores)
print("\n\n Lista variada: "); print(listaVariada)
print("\n\n Tupla: "); print(tupla)
print("\n\n Conjunto unión: ")
print(conjuntoResultante)






# ---------------------- MÉTODO: .intersection() ------------------
# El método ".intersection()" devolverá un nuevo conjunto, que  contiene 
# solamente los elementos que están presentes en ambos conjuntos. 
# Este método también permite trabajar con listas y tuplas.

conjuntoColores = {"Amarillo", "Violeta", "Verde"}
conjuntoVariado = {"Aguila", "Violeta", "Gato", False, 25}

conjuntoResultante = conjuntoColores.intersection(conjuntoVariado)

os.system("cls")
print("\n\n Conjunto colores: "); print(conjuntoColores)
print("\n\n Conjunto variado: "); print(conjuntoVariado)
print("\n\n Conjunto intersección: ")
print(conjuntoResultante)








# ----------------------- MÉTODO: .difference() -------------------
# El método ".difference()" devolverá un nuevo conjunto que contendrá sólo 
# los elementos del primer conjunto que no están presentes en el otro conjunto.
# Este método también permite trabajar con listas y tuplas.

conjuntoColores = {"Amarillo", "Violeta", "Verde"}
tuplaVariada = ("Aguila", "Violeta", "Gato", False, 25)

conjuntoResultante = conjuntoColores.difference(tuplaVariada)

os.system("cls")
print("\n\n Conjunto colores: "); print(conjuntoColores)
print("\n\n Tupla variada: "); print(tuplaVariada)
print("\n\n Conjunto diferencia: ")
print(conjuntoResultante)




# ----------------------- MÉTODO: .symmetric_difference() -------------------
# El método ".symmetric_difference()" mantiene sólo los elementos que NO están 
# presentes en ambos  conjuntos.
# Este método también permite trabajar con listas y tuplas.

conjuntoColores = {"Amarillo", "Violeta", "Verde"}
conjuntoVariado = {"Aguila", "Violeta", "Gato", False, 25}

conjuntoResultante = conjuntoColores.symmetric_difference(conjuntoVariado)

# conjuntoResultante = conjuntoColores ^ conjuntoVariado

os.system("cls")
print("\n\n Conjunto colores: "); print(conjuntoColores)
print("\n\n Conjunto variado: "); print(conjuntoVariado)
print("\n\n Conjunto Diferencia simétrica: ")
print(conjuntoResultante)

