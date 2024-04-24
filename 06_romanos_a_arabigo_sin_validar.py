import os
os.system("cls")


# En este programa <se asume> que el romano ingresado por el usuario
# está libre de errores, todo normal. Nos enfocaremos en la lógica
# de conversión, únicamente.

diccRomano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

romanoUsuario = input("Ingresa un numero en Romano menor a 4000: ").upper()
print(romanoUsuario)

# ------------------ Conversión a arábigo -------------------
# MMMCMXCIX = 3999,     máximo valor que trabajaremos en este programa.
# IXV
# IV   

longitud = len (romanoUsuario) - 1
cifraArabiga=0         

for indice, letra in enumerate(romanoUsuario):
    valorLetra = diccRomano[letra]

    if (indice < longitud):        # no se ha alcanzado el final de <romanoUsuario>
        siguiente = romanoUsuario[indice + 1] 
        valorSiguiente = diccRomano[siguiente]

        if (valorLetra >= valorSiguiente):
            cifraArabiga += valorLetra
        else:
            cifraArabiga -= valorLetra
    else:
        cifraArabiga += valorLetra

print ("Resultado = ", cifraArabiga)


