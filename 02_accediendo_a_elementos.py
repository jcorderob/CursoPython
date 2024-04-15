import os

diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995
}

# ------------  ACCEDIENDO A LOS ELEMENTOS DE UN DICCIONARIO --------
#
# La referencia a cada elemento se hace con corchetes y la clave:  ["clave"] .

os.system("CLS") 
print ("\n  \033[32m Diccionario: \033[0m ",diccionario,)

print("\n \033[32m Items:  Marca y Modelo: \033[0m  ",diccionario['marca'], 
                                                      diccionario['modelo'])

# ------------  TAMBIÉN SE PUEDE ACCEDER CON EL MÉTODO '.get()'  --------
#

print("\n \033[32m Items: Marca y Modelo con el método <get>: \033[0m  ",
                            diccionario.get('marca'), diccionario.get('modelo'))

# ------------  MOSTRAR TODOS LOS ITEMS DE UN DICCIONARIO  --------
#
print("\n \033[32m Items: \033[0m  ", diccionario.items())

# ------------  MOSTRAR TODAS LAS CLAVES DE UN DICCIONARIO  --------
#
print("\n \033[32m Items: Claves: \033[0m  ", diccionario.keys())

# ------------  MOSTRAR TODAS LOS VALORES DE UN DICCIONARIO  --------
#
print("\n \033[32m Items: Values: \033[0m ", diccionario.values())

# -------  VERIFICANDO SI UNA CLAVE ESTÁ PRESENTE EN EL DICCIONARIO  --------
#

if "anio" in diccionario:
    print("\n \033[32m 'anio'\033[0m es una clave : ")

