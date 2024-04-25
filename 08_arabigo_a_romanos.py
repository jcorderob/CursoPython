import os, sys
import tkinter.messagebox as messagebox

os.system("cls")

# Definir los símbolos Romanos y sus valores Decimales correspondientes
simbolosRoma = ['M','CM', 'D','CD', 'C', 'XC', 'L','XL', 'X','IX', 'V', 'IV', 'I']
valoresDeci  = [1000, 900, 500, 400, 100, 90,   50, 40,   10,  9,   5,    4,   1]

# --- Combinar las dos listas en un <objetozip> y luego en <diccionario> ----

diccionario = dict(zip(valoresDeci, simbolosRoma))
decimalUsuario = int(input("Ingrese un número decimal (arábigo) : "))

if ( decimalUsuario <= 0 or decimalUsuario >= 4000 ):
    messagebox.showwarning("¡ERROR!","Entrada inválida, número fuera de rango!! \
                                        \n Ingrese número entre 1 y 3999")
    sys.exit()  # Detenemos el programa de manera abrupta, no tiene caso seguir.

salidaEnRomano = ''  # cadena o string
# Iterar sobre los valoresDeci del diccionario
for decimalDic, simboloRom in diccionario.items():  # cada 'item' es un par clave:valor
    while decimalUsuario >= decimalDic:
        decimalUsuario -= decimalDic
        salidaEnRomano += simboloRom

print("Romano : ", salidaEnRomano)
