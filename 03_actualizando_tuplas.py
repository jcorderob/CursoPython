import os

# Recuerde que las tuplas son <inmutables>, por tanto no se puede eliminar,
# añadir o modificar los elementos de una <tupla>.
#
# En caso de requerirlo, debemos convertirla en <lista> , hacer los cambios
# y volver a convertir la <lista> en una <tupla>.
#  en <tupla>.

os.system("cls")

tuplaAutos = ("Mustang", "Chevy", "Volkswagen","Aveo")
print ("\nTupla autos: ",tuplaAutos)

listaAutos = list(tuplaAutos)  # Convertimos la tupla a lista.

listaAutos[1] = "Onix turbo"    # actualizamos la lista

tuplaAutos = tuple(listaAutos)

print("\n",tuplaAutos)



# Cualquier otra operación de actualización de una <tupla> debe hacerse
# a través de listas. Con la EXCEPCIÓN de la CONCATENACIÓN de tuplas, la cual
# si esta permitida.

tuplaAutos = ("Mustang", "Chevy", "Volkswagen","Aveo")
autos2 = ("optra","corsa", "sail")
print ("\n\nTupla autos: ",tuplaAutos)
print ("\nTupla autos 2: ",autos2)

tuplaAutos += autos2  # tuplaAutos = TuplaAutos + autos2
print ("\n\nTupla autos concatenada: ",tuplaAutos)

