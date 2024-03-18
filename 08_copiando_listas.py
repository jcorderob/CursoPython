import os, copy

os.system("cls")

"""
# --------------  COPIAR LISTAS -------------- 

paises = ["Venezuela","Rusia","Japón", "Dinamarca","Perú","Chile","Australia"]
segundaLista = paises

print ("\n--------------- PAISES ORIGINAL ----")
print("\n",paises)

print("\n---------- LOS MISMOS PAISES EN OTRA LISTA ------------")
print("\n",segundaLista)

# Alteración del los datos en el objeto lista
paises.sort()

print ("\n\n--------------- PAISES ORIGINAL DESPUÉS DEL ORDENAMIENTO----")
print("\n",paises)

print("\n---------- LOS MISMOS PAISES EN SEGUNDA LISTA ------------")
print("\n",segundaLista)

"""

# --------------  <<REFERENCIAR>>  NO ES IGUAL  A <<COPIAR>> LISTAS -------------- 

paises = ["Venezuela","Rusia","Japón", "Dinamarca","Perú","Chile","Australia"]
segundaLista = paises.copy()

# Mostramos la primera lista
print ("\n--------------- PAISES ORIGINAL ----")
print("\n",paises)

paises.sort()

print ("\n--------------- PAISES ORDENADA ----")
print("\n",paises)

# Mostramos la segunda lista
print ("\n--------------- SEGUNDA LISTA COPIA DE LA PRIMERA ----")
print("\n",segundaLista)


