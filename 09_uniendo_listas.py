import os

# --------------  MEZCLAR LISTAS -------------- 
os.system("cls")

paises = ["Venezuela","Rusia","Japón", "Dinamarca"]
numeros = [12, 22, 32, 42, 52]

mezclados = paises + numeros

print ("--------------- PAISES  ----")
print("\n",paises)

print ("--------------- NUMEROS  ----")
print("\n",numeros)

print ("--------------- LISTAS MEZCLADAS  ----")
print("\n",mezclados)



# --------------  EXTENDIENDO UNA LISTA CON ELEMENTOS DE OTRA --------------
# Extender la lista <paises> con la lista <numeros>
 

paises = ["Venezuela","Rusia","Chile", "Dinamarca"]
numeros = [12, 22, 32, 42, 52]

print ("--------------- PAISES  ----")
print(paises,"\n")

print ("--------------- NUMEROS  ----")
print(numeros,"\n")

paises.extend(numeros)
print ("\n--------------- PAISES UNIDA  CON NUMEROS MEDIANTE extend()  ----")
print(paises,"\n")



# --------------  AÑADIENDO UNA LISTA A OTRA -------------- 

paises = ["Venezuela","Rusia","Japón", "Dinamarca"]
numeros = [12, 22, 32, 42, 52]

print ("--------------- PAISES  ----")
print("\n",paises)

print ("--------------- NUMEROS  ----")
print("\n",numeros)

numeros.append(paises)
print ("--------------- PAISES AÑADIDOS A NUMEROS CON append()  ----")
print("\n",numeros)


