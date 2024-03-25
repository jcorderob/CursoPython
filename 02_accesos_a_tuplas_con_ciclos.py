import os

miTupla = ("UNO","DOS","TRES","UNO","CINCO","DOS")

os.system("cls")

"""
# -----------  Acceso a elementos individuales en una tupla ------



print(miTupla)
print("\n\nEl tercer elemento (posic. 2) de la tupla es :" 
"\033[32m", miTupla[2], "\033[0m")

# -----------  Acceso con el ciclo <for>-- ------
print("\n\n Acceso con ciclo <for>")
for control in miTupla:
    print(control)

# -----------  Acceso con el ciclo <while>-- ------
print("\n Tupla mostrada con ciclo <while> ")
control = 0
while control < len(miTupla):
    print(miTupla[control])
    control += 1

"""

# -----------  Acceso a rangos de valores -- ------
    
miTupla = ("UNO","DOS","TRES","UNO","CINCO","DOS")

print("\n Tupla completa: ", miTupla)
print("\n rango de valores de tupla [2:5] ")

print(miTupla[2:5])  # Observe que < miTupla[2:5] > devuelve una tupla.
                     # OJO: No incluye el último.

# ---------  Verificar si un item (valor) existe dentro de la tupla --------
    

if "TRES" in miTupla:
    print ("\n\nEfectivamente el valor 'TRES' existe dentro de la tupla")
else: print("\n\nEl valor no existe")



