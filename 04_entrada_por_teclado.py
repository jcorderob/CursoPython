import os

# Programa que pide un Nombre, edad y dirección de una persona
# los lee desde el teclado y muestra la salida por pantalla
# Funcion  input()

"""
os.system("cls")

print("\n\n")
print("Cuál es tu nombre?")
nombre= input()
print("Cuál es tu edad?")
edad= input()
print("Cuál es tu dirección")
direccion= input()

print("\n\n------------------------------------------------")
print(f"Nombre = {nombre}")
print(f"Edad   = {edad}")
print(f"Dirección = {direccion}")

"""

# Programa que pide dos valores numéricos, los lee desde el teclado
# y realiza varios cálculos con ellos. 

os.system("cls")

print ("\n\n\nIngrese 2 valores numéricos para realizar algunos cálculos:")
print("\nIngrese 1er Número"); opera1 = int(input())

print("\nIngrese 2do Número"); opera2 = int(input())

potencia = opera1 ** opera2
cociEntero = opera1 // opera2
cociReal   = opera1 / opera2
resto  = opera1 % opera2
negativo = - opera1
positivo = - opera2

# Generar valores Booleanos (lógicos)
logico1 = opera1 == opera2
logico2 = negativo > 0 

os.system('cls')
print (f"\n\nOperando 1= {opera1} - Operando 2 = {opera2}")
print(f"\nPotencia = {potencia}")
print(f"\nCociente entero = {cociEntero}")
print(f"\nCociente real = {cociReal}")
print(f"\nResto = {resto}")
print(f"\nNegati del operador1 = {negativo}")
print(f"\nPositivo del operador1 = {negativo}")
print(f"\nLógico 1 = {logico1}")
print(f"\nLógico 2 = {logico2}")




