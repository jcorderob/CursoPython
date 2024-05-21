import os
# Crear el diccionario para almacenar los datos del trabajador
trabajador = {
    'dni': '',
    'nombre_apellido': '',
    'año_de_ingreso': '',
    'sexo': '',
    'edad': '',
    'salario': ''
}

# Lista vacía para almacenar los datos de los trabajadores
lista_trabajadores = []


# --------------------------  Función Registrar   
def eliminar_trabajadores():
    while True: 
        os.system("cls")
        print("\n\n     \033[32m** MÓDULO ELIMINAR **\033[0m")
        dni_a_buscar = input("\nDNI de trabajador o \033[33m'000'\033[m para retornar al Menú :")
        if dni_a_buscar == '000': 
            break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar)
            if resultado_busqueda[0] == True:
                trabajador = resultado_busqueda[2]
                respuesta = input(f"Desea eliminar a {trabajador['nombre_apellido']} S/N ?")
                if respuesta.upper() == 'S':
                    indice = resultado_busqueda[1]
                    del lista_trabajadores[indice]
                    input("\nTrabajador eliminado, presione <enter>")
            else:
                input(f"\nDNI \033[32m{dni_a_buscar}\033[0m no registrado, presione <enter>")    


# --------------------------  Función Buscar dni 
def buscar_dni(dni_buscado):
    for indice, trabajador in enumerate(lista_trabajadores):
        if trabajador['dni'] == dni_buscado:
            return True, indice, trabajador # Devuelve una tupla
    return False, None


# --------------------------  Función Consultar   
def consultar_trabajadores():
    while True:
        os.system("cls")
        print("\n\n     \033[32m** MÓDULO CONSULTAR **\033[0m")
        dni_a_buscar = input("\nIngrese DNI de trabajador o \033[33m'000'\033[m " 
                             "para retornar al Menú :")
        if  dni_a_buscar == '000': break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar) # Devuelve una tupla
            if resultado_busqueda[0] == True:             # if resultado_busqueda[0] : 
                trabajador = resultado_busqueda[2]
                print("DNI        : ", trabajador['dni'])
                print("NOMBRE     : ", trabajador['nombre_apellido'])
                print("AÑO INGRESO: ", trabajador['año_de_ingreso'])
                print("SEXO       : ", trabajador['sexo']) 
                print("EDAD       : ", trabajador['edad'])
                print("SALARIO    : ", trabajador['salario'])
            else:
                print(f"\nDNI = \033[32m{dni_a_buscar}\033[0m, no está registrado!!.")

            input("\n\nPresione una tecla para continuar ...")         


# --------------------------  Función Validar año de ingreso
# --------------------------  Manejo de excepciones 
def validar_anio():
    while True:           
            entrada = input("Año de ingreso    :")  
            try:
                # Intentar convertir la entrada a un número entero
                anio = int(entrada)
                return anio
            except ValueError:
                print("\033[33mPor favor, ingrese una edad válida.\033[0m") 


# --------------------------  Función Validar entero
def validar_edad():
    while True:           
            entrada = input("Edad              :")  
            try:
                # Intentar convertir la entrada a un número entero
                edad = int(entrada)
                return edad
            except ValueError:
                print("\033[33mPor favor, ingrese una edad válida.\033[0m") 


# --------------------------- Funcion Validar sexo
def validar_sexo():
    while True:          
            entrada= input("Sexo (F/M)        : ").upper()
            if entrada in ['F','M']:
                return entrada
            else:
                print("\033[33mEl sexo debe ser F o M\033[0m")


def validar_salario():
        while True:         
            entrada= input("salario           : ")
            try:
                # intentar convertir entrada a numero flotante
                salario = float(entrada)
                return salario
            except:
                print("\033[33mPor favor, ingrese un salario válido.\033[0m")  


# --------------------------  Función Registrar   
def registrar_trabajadores():
    global trabajador
    # Ciclo para ingresar los datos de múltiples trabajadores
    while True:
        os.system("cls")
        print("\n\n\033[32m** MÓDULO REGISTRO DE TRABAJADORES **\033[0m\n")
        # Solicitar al usuario que ingrese los datos del trabajador
        dni_a_buscar = input("Ingrese el dni o '\033[33m000\033[0m' para volver al Menú: ")
        # Si el usuario ingresa "000", se rompe el ciclo
        if dni_a_buscar == '000':
            break
        else:
            resultado_busqueda = buscar_dni(dni_a_buscar) # Se recible una tupla
            if resultado_busqueda[0] == True:
                print(f"\nDNI \033[32m{dni_a_buscar}\033[0m ya registrado!!")
                trabajador = resultado_busqueda[2] 
                input(f"\nPertenece al trabajador: {trabajador['nombre_apellido']}") 
                continue    
            else:
                trabajador['dni'] = dni_a_buscar
                trabajador['nombre_apellido'] = input("Nombre y apellido : ").lower().title()    
                trabajador['año_de_ingreso'] = validar_anio()
                trabajador['sexo'] = validar_sexo()
                trabajador['edad'] = validar_edad()
                trabajador['salario'] = validar_salario()
                # Agregar una copia del diccionario <trabajador> a la lista de trabajadores
                lista_trabajadores.append(trabajador.copy())
                input("\nTrabajador Registrado, presione <enter>")

                
# --------------------------  Función Listar 
def listar_trabajadores():
    # Imprimir la lista de trabajadores
    os.system("cls")
    print("\n\033[32m            ** REPORTE DE TRABAJADORES **\n")
    print("Nro   DNI   NOMBRE           AÑO INGRESO SEXO     EDAD    salario")
    print("===   ===   ======           =========== ====     ====    ======\033[0m")
    acumula_salario = 0
    for contador, trabajador in enumerate(lista_trabajadores, 1):
        print(f"{contador:<6}{trabajador['dni']:<6}{trabajador['nombre_apellido']:<20}"  
              f"{trabajador['año_de_ingreso']:<10}{trabajador['sexo']:<9}"    
              f"{trabajador['edad']:<7}" f"{trabajador['salario']:.2f}")
        
        acumula_salario += trabajador['salario']

    salario_promedio = acumula_salario / len(lista_trabajadores)
    print("---------".rjust(66))  
    print("Salario Promedio:".rjust(41),end="")
    print(f"\033[32m{salario_promedio:>24.2f}\033[0m")
        
    input("\n\nPresione una tecla para continuar ...")


# -------------------------- Mostrar y leer opciones
def leer_opcion():
    os.system("cls")
    print("\n\n\033[32m     *MENÚ DE OPCIONES*\033[0m")
    print("                     Opción".rjust(33))
    print("                     ------".rjust(33))
    print("Registrar trabajador ....... 1")
    print("Consultar trabajador ....... 2")
    print("Eliminar trabajador  ....... 3")
    print("Listar trabajadores  ....... 4")
    print("\033[33mSalir  ....... 0 \033[0m".rjust(40))
    while True:
        opcion = input("\033[32mOpción? \033[0m ".rjust(32))
        if opcion  in ['0','1','2','3','4']:
            break
        else:
            print("Opción inválida");
    return opcion 


# --------------------------  Función main() 
def main():
    while True:
        opcion = leer_opcion()
        if   opcion == '1': registrar_trabajadores() 
        elif opcion == '2': consultar_trabajadores()
        elif opcion == '3': eliminar_trabajadores()
        elif opcion == '4': listar_trabajadores()
        elif opcion == '0': break


# Cuerpo principal del programa
if __name__ == "__main__":
    main()
