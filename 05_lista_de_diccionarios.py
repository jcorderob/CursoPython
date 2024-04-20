import os
listaAutos = [
    {
        "marca": "Fiat",
        "modelo": "spacio",
        "anio": 1995,
        "motor": "4 cilindros"
    },
    {
        "marca": "Ford",
        "modelo": "Fiesta",
        "anio": 2010,
        "motor": "3 cilindros"
    },
    {
        "marca": "Chevrolet",
        "modelo": "Spark",
        "anio": 2015,
        "motor": "4 cilindros"
    }
]

os.system("CLS") 

print("\n\033[32m Modelos de autos: \033[0m ")

# ----------- Obteniendo el modelo de cada auto.--------------------

for indice in range(0,len(listaAutos)):       # Iteración basada en un rango
    print(listaAutos[indice]["modelo"],"\n")

# ----------- Obteniendo el modelo de cada auto. Versión mejorada--------------------

print("\n\n\033[32m Modelos de autos Versión mejorada: \033[0m ")

for autoDicc in listaAutos:                       # ciclo basado en un iterable
    print(autoDicc["modelo"])
    
    
# ----------- Obteniendo un listado de todos los autos --------------------

print("\n\033[32m Modelos de autos: \033[0m ")
print("\n\033[32mMarca        Modelo    Año   Motor \033[0m")
for autoDicc in listaAutos:                  # iteración basada en elementos de un iterable
    print(autoDicc["marca"], autoDicc["modelo"],autoDicc["anio"], autoDicc["motor"])


# ----------- Obteniendo un listado MEJORADO de todos los autos --------------------
# --------------  El formateo se hace con la función:  "str.format()"
print("\n\033[32m MODELOS DE AUTOS: \033[0m ")
print("\n\033[32mMarca        Modelo    Año   Motor \033[0m")
for autoDicc in listaAutos:                  
    print("{:<12} {:<9} {:<5} {:<10}".format(autoDicc["marca"], autoDicc["modelo"], 
                                            autoDicc["anio"], autoDicc["motor"]))

 
