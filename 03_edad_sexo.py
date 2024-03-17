import os

"""
-------------------------------------------------------------------
Programa que pide el nombre de una persona, su edad, sexo y 
posteriormente el programa debe mostrar una salida similar a las siguientes:

* Pedro Pérez es un hombre adulto . 
* Carmen Uzcategui es una niña . 
* David López es un hombre adulto mayor .
-------------------------------------------------------------------
"""
os.system("cls")
print ("\n\n\n")

#----------------------  ENTRADA DE DATOS ------------------------
print ("Ingrese los datos personales ")
print ("---------------------------- ")
print ("Nombre:");  nombre =input()
print ("Edad:  ");  edad = int(input())
print ("Sexo (M-F):"); sexo =input()


sexo = sexo.upper()
#----------------------  PROCESAMIENTO DE DATOS ------------------------

cadenaDeSalida = nombre + " "  # Variable que contendrá  mensaje de salida

if (edad <= 12) :  # if (edad <= 12) and (sexo == 'F')  -> niña  :: No usar
                   # if (edad <= 12) and (sexo == 'M')  -> niño  :: No usar   
    if ( sexo == "F"):
        cadenaDeSalida += "es una niña "
    else: cadenaDeSalida += "es un niño "

elif (edad <= 19):

    if ( sexo == "F"):
        cadenaDeSalida += "es una adolescente "
    else: cadenaDeSalida += "es un adolescente "

elif (edad < 65):

    if ( sexo.upper() == "F"):
        cadenaDeSalida += "es una mujer adulta "
    else: cadenaDeSalida += "es un hombre adulto "

else:

    if ( sexo.upper() == "F"):
        cadenaDeSalida += "es una mujer adulta mayor "
    else: cadenaDeSalida += "es un hombre adulto mayor "       


#----------------------  SALIDA DE DATOS ------------------------

print ("***  -------------------- SALIDA DE DATOS -----------------\n")
print (cadenaDeSalida)
