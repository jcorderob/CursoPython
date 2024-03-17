import os

"""
-------------------------------------------------------------------
Programa que pide el nombre de una persona, su edad, sexo y el estado civil,
posteriormente el programa debe mostrar una salida similar a las siguientes:

* Pedro Pérez es un hombre adulto y casado 
* Carmen Uzcategui es una niña soltera 
* David López es un hombre adulto mayor viudo.
-------------------------------------------------------------------
"""
os.system("cls")
print("\n\n\n")

#----------------------  ENTRADA DE DATOS ------------------------
print ("Ingrese los datos personales ")
print ("---------------------------- ")
nombre = input("Nombre:") 
edad   = int(input("Edad:  "))
sexo =input("Sexo (M-F):").upper() 
print ("Estado Civil (S-C-V-D)");  edoCivil=input().upper()

#----------------------  PROCESAMIENTO DE DATOS ------------------------

cadenaDeSalida = nombre + " "  # Variable que contendrá  mensaje de salida

# Trabajando sólo con edad y sexo. El estado civil se hace aparte.
if (edad <= 12) :

    if ( sexo == "F"):
        cadenaDeSalida += "es una niña "
    else: cadenaDeSalida += "es un niño "

elif (edad <= 19):

    if ( sexo == "F"):
        cadenaDeSalida += "es una adolescente "
    else: cadenaDeSalida += "es un adolescente "

elif (edad <= 65):

    if ( sexo == "F"):
        cadenaDeSalida += "es una mujer adulta "
    else: cadenaDeSalida += "es un hombre adulto "

else:
    if ( sexo == "F"):
        cadenaDeSalida += "es una mujer adulta mayor "
    else: cadenaDeSalida += "es un hombre adulto mayor "       

# Evaluación del estado civil junto al sexo

if (edoCivil =='S') :

    if ( sexo == "F"):
        cadenaDeSalida += "Soltera "    
    else: cadenaDeSalida += "soltero " 

elif (edoCivil =='C'):

    if ( sexo == "F"):
        cadenaDeSalida += "casada "    
    else: cadenaDeSalida += "Casado "

elif (edoCivil =='V'):

    if ( sexo == "F"):
        cadenaDeSalida += "Viuda "    
    else: cadenaDeSalida += "Viudo "

else:

    if ( sexo == "F"):
        cadenaDeSalida += "Divorciada "    
    else: cadenaDeSalida += "Divorciado "
#----------------------  SALIDA DE DATOS ------------------------

print ("***  -------------------- SALIDA DE DATOS -----------------\n")
print (cadenaDeSalida)

