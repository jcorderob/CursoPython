import os

diccionario = {
  "marca": "Fiat",
  "modelo": "Spacio",
  "anio": 1995
}


os.system("cls")
print("\nDiccionario original: ",diccionario)

# -------------------- MODIFICANDO VALORES DE UN DICCIONARIO ---------------

diccionario["anio"] = 2024
print("\nDiccionario con cambios: ",diccionario)

# ---------- MODIFICANDO VALORES CON EL MÉTODO:  '.update()' ---------------

diccionario.update({"modelo": "Fiorino"})
print("\nDiccionario con cambios: ",diccionario)

# ------------- AÑADIENDO ITEMS A UN DICCIONARIO ------------------------

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995
}

diccionario["motor"] = "4 cilindros"
print("\nDiccionario con nuevo item: ",diccionario)

# -------- AÑADIENDO ITEMS CON EL MÉTODO:  '.update()' -------------------

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995
}

diccionario.update({"motor":"6 cilindros"})
print("\nDiccionario con nuevo item: ",diccionario)

# -------- ELIMINANDO ITEMS CON EL MÉTODO:  '.pop()' -------------------

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"8 cilindros"
}

diccionario.pop("modelo")
print("\nDiccionario con un item menos: ",diccionario)

# -------- ELIMINANDO ITEMS CON LA PALABRA CLAVE: 'del' -------------------

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"6 cilindros"
}

del diccionario["marca"]
print("\nDiccionario con un item menos: ",diccionario)

# IMPORTANTE: Se puede borrar TODO el diccionario con la palabra clave: 'del'

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"6 cilindros"
}

del diccionario
# print("\nDiccionario vacío: ",diccionario)  # --> Provoca error

# IMPORTANTE: Un diccionario se <VACÍA> con el método: '.clear()'

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"6 cilindros"
}

diccionario.clear()
print("\nDiccionario vacío: ",diccionario)
