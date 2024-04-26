import os

# Podemos crear diccionarios dentro de un diccionario. Eso se llama 
# diccionarios anidados.

alumnosMatematica= {
    "alumno1":{
        "dni"    : "U-00231",
        "nombre" : "Luis Carvajal",
        "nota"   : 7               # escala del 1 al 10
    },
    "alumno2":{
        "dni"    : "U-00792",
        "nombre" : "María Moreno",
        "nota"   : 8              
    },
    "alumno3":{
        "dni"    : "U-00632",
        "nombre" : "Carmen Muñoz",
        "nota"   : 7               
    }
    }

os.system("cls")

# Mostrar todos los alumnos de la asignatura 'Matemática' ----------

print("\nTodos los alumnos\n")
print(alumnosMatematica)

# Mostrar los datos completos de un alumno en particular ----------
print("-" * 50)
print("\nDatos del  <alumno3>: ")
print(alumnosMatematica["alumno3"])

# Mostrar el <nombre> y la <nota> de un alumno en particular ----------
print("-" * 50)
print("\nDatos Parciales de un alumno en particular: ")
print(f"Nombre = {alumnosMatematica['alumno3']['nombre']}" 
      f" , Nota   = {alumnosMatematica['alumno3']['nota']}")

# Mostrar un listado de Nombres y Notas -----------------------
print("-" * 50)
print("\n\033[32mNOMBRES        NOTAS\033[0m")
for alumno, detalles in alumnosMatematica.items():
    print("{:<17}{:<2}".format(detalles['nombre'], detalles['nota']))