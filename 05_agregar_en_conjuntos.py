import os

#-------- LOS ELEMENTOS DE CONJUNTOS NO SE PUEDEN MODIFICAR -------------
# pero si se pueden <eliminar> y <agregar> nuevos elementos

miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}

os.system("cls")

print("\n El conjunto es: ",miConjunto)

#------------------- AGREGAR ELEMENTOS A CONJUNTOS -------------------------

miConjunto.add("VEINTE") # Método , lo que se coloca dentro se llama argumento
print("\n Conjunto con un elemento añadido: ",miConjunto)


#-------------------- AÑADIENDO UN CONJUNTO A OTRO -------------

segundoConjunto = {False,25}

miConjunto.update(segundoConjunto)

print("\n miConjunto con el segundo conjunto añadido: ")
print(miConjunto)

# IMPORTANTE : El método 'update()' permite que  su argumento sea cualquier
#              elemento iterable (lista, tupla, diccionario o conjunto).
# 

tupla = (True,False,25,"UNA CADENA")
miConjunto.update(tupla)

print("\n miConjunto con una tupla añadida: ")
print(miConjunto)


