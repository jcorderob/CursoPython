import os


#             0       1      2        3       4        5        6
# paises = ["Perú","EEUU","España","Rusia","Japón", "Perú","Australia"]

#---------------- RECORRIENDO UNA LISTA CON <for> --------------------------

# Realice un Programa que muestre una lista generada internamente.
# NO haga uso de índices.

paises = ["Perú","EEUU","España","Rusia","Japón", "Perú","Australia"]

os.system("cls")
print("\n\n Paises de la lista:\n")
                            # for cont in range(1,22,2)
for control in paises:      #     cont -> 1, 3, 5, 7, 9.....
    print (control)         #  control -> "Perú", "EEUU", "España", ...

#-------------- RECORRIENDO UNA LISTA CON UN <índice> -----------------------

# Realice un Programa que muestre una lista generada internamente.

# paises = ["Perú","EEUU","España","Rusia","Japón", "Perú","Australia"]

print("\n\n Paises de la lista mostrados con: For:\n")

for control in range(len(paises)):
    print (paises[control], end= ' - ')

#-------------- RECORRIENDO UNA LISTA CON UN <índice> -----------------------

# Realice un Programa que muestre una lista generada internamente.
# NO haga uso del ciclo <for>.

#paises = ["Perú","EEUU","España","Rusia","Japón", "Perú","Australia"]

print("\n\n Paises de la lista mostrados con: While:\n")

indice = 0         
while indice < len(paises):
    print (paises[indice], end= ' - ')
    indice += 1
