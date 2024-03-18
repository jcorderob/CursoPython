import os

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi","melón","Pera"]

os.system("cls")

print("\n",lista)

# -----  Modificando el item de la posición 2 -----
lista[2] = "Mango"
print("\nLista modificada en posición 2 : ",lista)

# -----  Modificando rangos de valores ---------
lista[3:5] = ["Banana","Sandía"]  # No incluye al último del rango
print("\nLista modificada: ",lista)

# --  Si el número de items es menor al especificado, la lista se reduce -----

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi","melón","Pera"]
print("\n Lista original: ",lista)

lista[3:6] = ["Banana"]
print("\nLista reducida: ",lista)

# -----------  Insertar elementos en una lista ----------------
# --- Al insertar elementos los demás no se pierden ----------

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi","melón","Pera"]
print("\n",lista)
lista.insert(2,"Papaya")
print("\nLista con una inserción: ",lista)

# --- Unir dos listas (extendiendo la primera)  ----------

frutas = ["Manzana","Limón","Cereza"]
vegetales = ["Coliflor","Apio","Espinaca"]

frutas.extend(vegetales)   # Método 'extend()
print("\nLista extendida: ",frutas)

# El método <extend()> también funciona con  tuplas, conjuntos y diccionarios
