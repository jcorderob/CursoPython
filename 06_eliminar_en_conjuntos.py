import os


#-------- LOS ELEMENTOS DE CONJUNTOS NO SE PUEDEN MODIFICAR -------------
# pero si se pueden <agregar> y <eliminar>  nuevos elementos

miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}

#--------------ELIMINANDO ELEMENTOS DE UN CONJUNTO -------------
# Usar los métodos:  '.remove()'    o    '.discard()'
#
# IMPORTANTE:
#           '.remove()'  --> Generará error si su argumento no existe.
#           '.discard()' --> NO genera error si su argumento no existe.

os.system("cls")
print("\n El conjunto original es: ",miConjunto)

miConjunto.remove("TRES")
miConjunto.discard("CUATRO") 

print("\n El conjunto original es: ",miConjunto)


# miConjunto.remove("OCHO")

# miConjunto.discard("VEINTE")
# print("\n El conjunto original es: ",miConjunto)

print("\n El conjunto con la eliminación realizada es: ",miConjunto)

# ---------------  VACIAR UN CONJUNTO --------------------

miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}
# os.system("cls")
print("\n El conjunto original es: ",miConjunto)

miConjunto.clear()
print("\n El conjunto vacío es : ", miConjunto)


