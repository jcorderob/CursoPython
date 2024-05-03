import os
import tkinter.messagebox as messagebox 

os.system("cls")

#----------------------------------------------------------------
# Programa que realiza las 4 operaciones aritméticas básicas empleando
# funciones con pase de parámetros y un  Menú de opciones.
#----------------------------------------------------------------
def sumar(a, b):
    return  a+b

def restar(c, d):
    return  c - d

def multiplicar(operando1, operando2):
    return operando1 * operando2

def dividir(operando1, operando2):
    return operando1 / operando2

def mostrarMenu():
    continuar = True
    while continuar :
        print("\n\tSelecciona una opción:")
        print("\tSumar  -------> 1")
        print("\tRestar -------> 2")
        print("\tMultiplicar --> 3")
        print("\tDividir ------> 4")
        print("\tSalir   ------> 5")
        opcion = int(input("\n\t¿Qué opción deseas elegir? "))

        if (opcion not in [1,2,3,4,5,]):
            messagebox.showwarning("¡ERROR!","Opción no válida,  \
                                        \n Ingrese número entre 1 y 5")

        else: continuar = False  # para salir del ciclo while
        os.system("cls")

    return opcion

def main():
    os.system("cls")        
    continuar = True
    while continuar:
        print("\n\nPrograma q' realiza las <4> operaciones aritméticas básicas\n")
        operando1 = int(input("Ingrese el primer operando  : "))
        operando2 = int(input("Ingrese el segundo operando : "))

        opcion = mostrarMenu()
        if  opcion == 1:
            resultado = sumar(operando1, operando2)
        elif opcion == 2:
            resultado = restar(operando1, operando2)
        elif opcion == 3:
            resultado = multiplicar(operando1, operando2)
        elif opcion == 4:
            resultado = dividir(operando1, operando2)
        else:
            print("Salir del programa...")
            continuar = False

        if continuar :
            print(f"\n\nEl resultado de la operación es : "
                    f"\033[32m {resultado} \033[0m")
            resp = input("\nDesea efectuar otra operación (S/N) ?").upper()
            if (resp == "N"): continuar= False 

#--------------------------------------------------------------
# Cuerpo principal del programa
main()
#--------------------------------------------------------------