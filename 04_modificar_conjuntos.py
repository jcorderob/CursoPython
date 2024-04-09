import os

#-------- LOS ELEMENTOS DE CONJUNTOS NO SE PUEDEN MODIFICAR -------------
# pero si se pueden <eliminar> y <agregar> nuevos elementos

# Pero, y si quiero modificar un elemento ya existente dentro de un conjunto,
# cómo hago ???
# Se convierte en Lista, se modifica la lista y luego se reconvierte a Conjunto.

miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}

# miConjunto[2] = "SIETE"        # Esto generaría un error de interpretación

# os.system("cls")

print("\n El conjunto es: ",miConjunto)

# ---------------- Modificar un conjunto convirtiéndolo en lista -----------
# ----------------------- Luego se reconvierte a conjunto ------------------

# ----- se pide cambiar la cadena "TRES" por "SIETE" 

listaTemporal = list(miConjunto)
indiceTres = listaTemporal.index("TRES")

listaTemporal[indiceTres] = "SIETE"
miConjunto = set(listaTemporal)

print("\n El conjunto modificado es: ",miConjunto)
