import os

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"6 cilindros"
}

os.system("cls")
# La forma CORRECTA de generar una COPIA de un diccionario es a través del
# método '.copy()'. 
#
# La asignación tradicional ' dicc1 = dicc2 ' lo que hace es crear una nueva
# referencia al mismo conjunto de datos. Dos variables distintas apuntando al
# mismo diccionario.

# -------- CREANDO UNA NUEVA REFERENCIA AL MISMO OBJETO -----------

diccionario2 = diccionario  # Crea una referencia que apunta a 'diccionario'

diccionario["color"] = "rojo"  # Agrega un nuevo par 'clave:valor'

#print("\n Diccionario Original : ", diccionario)
#print("\n Segundo diccionario  : ", diccionario2)


# ------------------- COPIANDO DICCIONARIOS ----------------------

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"6 cilindros"
}

#diccionario2 = diccionario.copy()
diccionario2 = dict(diccionario)

diccionario["color"] = "rojo"  # Agrega un nuevo par 'clave:valor'

print("\n Diccionario Original : ", diccionario)
print("\n Segundo diccionario  : ", diccionario2)



