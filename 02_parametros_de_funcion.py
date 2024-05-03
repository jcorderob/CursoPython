import os

os.system("cls")

# Programa que realiza las 4 operaciones aritméticas básicas empleando
# funciones con pase de parámetros.

def sumar(a, b):
    resultado = a + b
    return  resultado

def restar(c, d):
    return  c - d

def multiplicar(operando1, operando2):
    resultado = operando1 * operando2
    return resultado

def dividir(dividendo, divisor):
    return dividendo / divisor

# ----------Diversas maneras de llamar a una función------------

resultadoSuma = sumar(15,17)
print(f"\nLa suma es : \033[32m {resultadoSuma} \033[0m")

print(f"\nLa resta es : {restar(17,15)}")

resultadoMultipli = multiplicar (7,8)
print(f"\nLa multiplicación es : {resultadoMultipli}")

print(f"\nLa división es : {dividir(13,3):.2f}")

