import os

# ---------------------------   MANEJO DE CONJUNTOS ------------------------
# IMPORTANTE: Tenga en cuenta que los CONJUNTOS son: NO-ORDENADOS,  
#             NO-MODIFICABLES (pero sí aceptan Eliminar y Añadir elementos),
#             NO ACEPTAN DUPLICADOS, son NO-INDIZABLES, son MULTI-DATA-TYPE.

# Programa que genera de manera automática un conjunto y lo muestra por pantalla


miConjunto = {"UNO","DOS","TRES","CUATRO","CINCO"}

#----------------------------------------------------------
os.system("cls")

print(f"\n\nEl conjunto completo es : \033[32m {miConjunto} \033[0m")
print(f"\n\nEl conjunto completo es : \033[32m {miConjunto} \033[0m")
print(f"\n\nEl conjunto completo es : \033[32m {miConjunto} \033[0m")


# ------------------------------------------------------------- 

# Programa para  crear conjuntos con diferentes datos

# IMPORTANTE: Si usted coloca el valor entero <1> y el True, se rechaza uno
#             de los dos. Igual pasa al colocar <0> y False. En ambos casos
#             acepta el PRIMERO, los demás se rechazan.


#os.system("cls")
miConjunto1 = {"UNO","DOS","TRES",1,2,3}
miConjunto2 = {"DOS","TRES","CUATRO",2,3,4,True}
miConjunto3 = {"UNO","DOS","TRES",True,2,3, 1, 0, False}

print(f"\n\nEl conjunto 1 completo es :  \033[32m {miConjunto1} \033[0m")
print(f"\n\nEl conjunto 2 completo es :  \033[32m {miConjunto2} \033[0m")
print(f"\n\nEl conjunto 3 completo es :  \033[32m {miConjunto3} \033[0m")






# --------------- TOMAR LA LONGITUD DE UN CONJUNTO --------------


os.system("cls")
miConjunto1 = {"UNO","DOS","TRES",1,2,3}
miConjunto2 = {"DOS","TRES","CUATRO",2,3,4,True}
miConjunto3 = {"UNO","DOS","TRES",True,2,3, 1,0, False}

print(f"\n\nEl conjunto1 completo es :  \033[32m {miConjunto1} \033[0m")
print ("\nLongitud : ", len(miConjunto1))
print(f"\n\nEl conjunto2 completo es :  \033[32m {miConjunto2} \033[0m")
print ("\nLongitud : ", len(miConjunto2))
print(f"\n\nEl conjunto3 completo es :  \033[32m {miConjunto3} \033[0m")
print ("\nLongitud : ", len(miConjunto3))


#--------------- El constructor < set() >  -----------------------
# ----------------- Permite crear <conjuntos> --------------------
#os.system("cls")
tupla = ("hola", "nunca", "versatil", "mañana")
print ("\n\n",tupla)
print(type(tupla))
print("-----------------")
conjunto = set(tupla)  # convierte la tupla en un conjunto
print (conjunto)
print(type(conjunto))

#-------------------------------------------------------------



