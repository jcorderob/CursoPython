import os

lista = ["Manzana","Limón","Cereza","Naranja","Kiwi","melón","Pera"]

os.system("cls")

print("\nLista original: ",lista)

# -----  remover según valor  -------
lista.remove("Cereza")
print("\nLista con un elemento removido: ",lista)

# --- Si el elemento a eliminar se repite, sólo se elimina el primero

lista = ["Manzana","Limón","Cereza","Naranja","Limón","melón","Pera"]
print("\nLista con elementos repetidos: ",lista)
lista.remove("Limón")
print("\nLista con un solo elemento removido: ",lista)

# -----  remover según posición  -------
lista = ["Manzana","Limón","Cereza","Naranja","Limón","melón","Pera"]
print("\nLista original: ",lista)
lista.pop(3)
print("\nLista con elemento eliminado con el método pop(): ",lista)

# -----  vaciar  la lista entera  -------
lista = ["Manzana","Limón","Cereza","Naranja","Limón","melón","Pera"]
print("\nLista original: ",lista)
lista.clear()
print("\nLista vacía: ",lista)

# -----  Eliminar la lista entera  -------
lista = ["Manzana","Limón","Cereza","Naranja","Limón","melón","Pera"]
print("\nÚltima lista original: ",lista)
del lista  # borra físicamente la lista
print(lista)

