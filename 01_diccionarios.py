import os

# ------------------------ LOS DICCIONARIOS < dict() >  ---------------------
#
# Son un conjunto de elementos caracterizados por contener cada uno
# un par denominado: clave : valor 
#
# Los diccionarios son:  ORDENADOS,  MODIFICABLES, NO ACEPTAN DUPLICADOS


diccionario = {
  "marca": "Fiat",
  "modelo": "spazio",
  "anio": 1995
}

# ------------  MOSTRAR LOS ELEMENTOS DE UN DICCIONARIO --------

os.system("CLS") 
print ("\nDiccionario:\n",diccionario)

# --- UN DICCIONARIO PUEDE CONTENER A CUALQUIER OTRO CONJUNTO DE DATOS ------

diccionario2 = {
  "marca": "Fiat",
  "modelo": "spazio",
  "anio": 1995,
  "color" : ["Blanco","Azul","Rojo", "Amarillo"]
}

print ("\nDiccionario 2: \n",diccionario2)

