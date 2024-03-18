import os

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi"]

os.system("cls")
print(lista)

# -------------------  Indizando la lista ------------------
print(f"Primer elemento de lista -0- : {lista[0]}")
print(f"Ultimo elemento de lista -4- : {lista[4]}")
print(f"Longitud de  lista: {len(lista)}")

# ---- Indización <negativa> ( comienza de atrás hacia adelante) ------------
# <-1> es el último índice, <-2> es el penúltimo, <-3> el ante penúltimo 

print (f"\nUltimo elemento con índice negativo (-1) {lista[-1]}")
print (f"\nPenúltimo elemento con índice negativo (-2)  {lista[-2]}")
print (f"\nAnte penúltimo elemento con índice negativo (-3)  {lista[-3]}")

# ------------------- Rangos de  Índices ------------------
# No incluye el último

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi","Melón","Uvas"]
print ("\n",lista [3:5])   # No incluye al elemento '5'.

# -------------El rango [:n]  comienza desde <el inicio> ---------------

print ("\n",lista [ :4])  # Desde el inicio, excluye al último

# -------------El rango [n: ]  toma hasta  <el final> ---------------

print ("\n",lista [3: ])  # Hasta el final

# ----------- Verificar si un elemento existe en la lista  --------------

print ("\n",lista)
if "Kiwi" in lista:
    print ("\nEl 'Kiwi' si está en la lista ")
    print (f"'Kiwi' está en la posición: {lista.index('Kiwi')}")

# print (f"'Mango' está en la posición: {lista.index('Mango')}")


