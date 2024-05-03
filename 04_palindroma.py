import os

def palindromo (frase):
    longitud = len(frase)
    if ( longitud > 1):
        indiInferior = 0
        indiSuperior = longitud - 1

        while ( frase[indiInferior] == frase[indiSuperior]) and  \
              ( indiInferior <= indiSuperior) :
              indiInferior += 1
              indiSuperior -= 1
        
        if ( indiInferior > indiSuperior ):
             return "La frase ingresada es palíndroma"
        else:
             return "La frase ingresada No es palíndroma"
    else:
         return "La frase debe tener al menos dos letras o caracteres"
 
def main():
     continuar = True
     while continuar :
          os.system("cls") 
          print("\n"*2)
          cadena = input("Ingrese una frase con al menos 2 letras o caracteres: ")
          print("\n", palindromo(cadena))

          respuesta = input("\n\n Desea probar con otra cadena (S/N) ? : ").upper()
          if respuesta == "N" : continuar = False

# -------------- Cuerpo principal del programa --------------------
main()





             
