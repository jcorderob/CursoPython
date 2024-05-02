import os

# Programa que crea una lista con valores enteros ingresados por teclado y
# posteriormente la muestrE.

# IMPORTANTE: Recuerde que hay 3 formas de ingresar elementos a una lista:
#             lista.append(), lista.insert(), lista.extend()

lista = []    # Crea una lista vacía. >> Lista es una variable <Global> <<
os.system("cls")

# ---- Función------
def llenar_lista():
    os.system("cls")
    cantidad = int(input("\n\nCuántos elementos desea que contenga la lista?: "))
    
    for contador in range(cantidad):
        os.system("cls")
        lista.append( int( input(f"\n\nIngrese el  valor  {contador+1} : ") ) ) 

# ---- Fin de Función------
        
# ---- Función------      
def mostrar_lista():
    os.system("cls")
    print (f"\nLa lista es :  ")
    for valorLista in lista:
        print (valorLista, end=" - ")

    print("\n\n")

# ---- Fin de Función------
    
# ------------  Cuerpo principal (main) - Llamado de las funciones -------------

llenar_lista()
mostrar_lista()




