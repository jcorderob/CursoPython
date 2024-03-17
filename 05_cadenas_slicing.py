import os


#---------------  IMPRIMIR CADENAS CON SEPARADOR ----------------------
# Podemos utilizar un separador utilizando el parámetro 'sep'. 
# Éste caracter se mostrará entre las cadenas.


os.system("cls")
print("\n\n")
print ("Curso","de", "programación", "con", "Python",sep="-")



# --------- LAS CADENAS SE PUEDEN  indizar (ponerles un índice) ---------------
# ---------- PARA REFERENCIAR A UN ELEMENTO O A VARIOS  -----------------------
os.system("cls")
print("\n\n")

nombre = "MARIA CASANOVA"
print(nombre,"\n\n")
print (nombre[0])
print (nombre[6])
print("\n\n")




# -------------------  SLICING (rebanada, pedazo) DE CADENAS ------------------
# -----------------------  variable[inicio : final-1]        ------------------
# -----------------------    al último valor se le resta 1  ------------------- 
print("\n\n")
print("nombre  =",nombre[0:5])
print("apellido=",nombre[6:14])





