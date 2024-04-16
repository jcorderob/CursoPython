import os


diccionario = {
  "marca": "Fiat",
  "modelo": "spacio",
  "anio": 1995,
  "motor":"4 cilindros"
}

os.system("cls")

# ------ La forma más óptima de recorrer un diccionario es con el ciclo < for >.

print("\n\033[32mDiccionario:\033[0m \n",diccionario)

# --------- Obteniendo las claves de un diccionario --------- 

print("\n \033[32m Claves del Diccionario: \033[0m \n")
for control in diccionario:
    print(control)


# CONCLUSIÓN: Al recorrer un diccionario de la forma mostrada encima, se está
#             accediendo a las claves.
    
# IMPORTANTE: Al obtener las claves por el método explicado arriba, podemos
#            usarlas como índices para acceder a los <valores> del diccionario.

print("\n\033[32mValores del diccionario: \033[0m\n")
for control in diccionario:
    print(diccionario[control])  # Equivalente a print(diccionario["marca"])


# --------- Acceso a las <claves> de un diccionario, usando el método: .keys()

print("\n\033[32mClaves con el método '.keys()' : \033[0m\n")
for control in diccionario.keys():
    print(control)  

# --------- Acceso a los <valores> de un diccionario, usando el método: .values()

print("\n\033[32mClaves con el método '.values()' : \033[0m\n")
for control in diccionario.values():
    print(control)  

# Podemos acceder en simultáneo a las <claves> y <valores> de un diccionario,
# usando el método: .items()

print("\n\033[32mClaves-valores con el método '.items()' :\033[0m \n")
for clave,valor in diccionario.items():
    print(clave,"-",valor)  
    