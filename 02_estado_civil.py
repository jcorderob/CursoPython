import os

# Programa que lee el nombre de una persona y su estado civil. Para indicar
# el estado civil se ingresará un caracter alfabetico (S-C-V-D-O) que es la
# letra inicial de C/U de los  estadoS  existentes. 
# El programa muestra como salida el nombre y el estado civil  completo.

os.system('cls')
print("\n\nNombre de la persona?")
nombre = input()

print("\n\nEstado civil (S-C-V-D-O)?")
edoCivil  =  input().upper()

if edoCivil == "S" : 
    estadoCivil = "Soltero(a)"
elif  edoCivil == "C" :
    estadoCivil = "Casado(a)"
elif  edoCivil == "V" :
    estadoCivil = "Viudo(a)"
elif  edoCivil == "D" :
    estadoCivil = "Divorciado(a)"
else :
    estadoCivil = "Otro"

print (f"\n\nEl estado civil de {nombre} es {estadoCivil}")

