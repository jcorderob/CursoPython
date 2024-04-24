import tkinter.messagebox as messagebox
import os, sys
os.system("cls")


diccRomano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

romanoUsuario = input("Ingresa un numero en Romano menor a 4000: ").upper()
print(romanoUsuario)

# -------- Validar que la cadena  ingresada sea un Romano válido ------------

simbolosNoValidos = [letra for letra in romanoUsuario  if letra not in diccRomano]

if ( len(simbolosNoValidos) >0 ):
    messagebox.showwarning("¡ERROR!","Entrada inválida, no está escrita en romano!!")
    sys.exit()  # Detenemos el programa de manera abrupta, no tiene caso seguir.
    
# ----------- validar que 'V','L','D' no se repitan más de 1 vez ---------------
#  -------------  se hará uso de una comprensión de listas -------------------- 

# variable = [nueva_expresion for elemento in iterable] condición # Condic Opcional

ini5Repetidos = [letra for letra in ['V','L','D']
                                                if romanoUsuario.count(letra)>1]

if (len(ini5Repetidos)>0):
    messagebox.showwarning("¡ERROR!", "Número inválido,  <ini5> repetidos")
    sys.exit()  # Detenemos el programa de manera abrupta, no tiene caso seguir.

# # --------- validar que 'I','X','C','M' no se repitan más de 3 veces ----------
 
ini1Repetidos = [letra for letra in ['I','X','C','M']
                                                if romanoUsuario.count(letra)>3]
if (len(ini1Repetidos)>0):
    messagebox.showwarning("¡ERROR!", 
                    "Cifra romana inválida, hay <ini1> repetidos más de 3 veces")
    sys.exit()  # Detenemos el programa de manera abrupta, no tiene caso seguir.

# ------------------ Conversión a arábigo -------------------

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


