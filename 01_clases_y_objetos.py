import os

# Definición de clase
class MamiferoCuadrupedo:
    
    # Atributos de clase. Son idénticos para cada objeto (instancia)
    especie = "Mamífero"
    organos_respiratorios = ["Pulmones", "Fosas nasales"]
    extremidades = 4

    # Atributos de instancia. Varían entre los distintos objetos(instancias)
    
    def __init__(self, nombre, edad, peso):  # Método constructor
        self.mi_nombre = nombre
        self.mi_edad = edad
        self.mi_peso = peso

# Fin de definición de clase


# Función que muestra los atributos de clase en diversas instancias

def mostrar_atributos_de_clase(perro, gato, vaca):

    # Acceso a atributos de clase
    print("\n\033[32m --ATRIBUTOS DE CLASE --\033[0m")
    print("-------- Perro -----------")
    print(perro.especie)                # Salida: Mamífero
    print(perro.organos_respiratorios)  # Salida: ['Pulmones', 'Fosas nasales']
    print(perro.extremidades)           # Salida: 4

    # Acceso a atributos de clase
    print("\n--------- Vaca ----------")
    print(vaca.especie)                # Salida: Mamífero
    print(vaca.organos_respiratorios)  # Salida: ['Pulmones', 'Fosas nasales']
    print(vaca.extremidades)           # Salida: 4

    # Acceso a atributos de clase
    print("\n-------- Gato -----------")
    print(gato.especie)                # Salida: Mamífero
    print(gato.organos_respiratorios)  # Salida: ['Pulmones', 'Fosas nasales']
    print(gato.extremidades)           # Salida: 4

# Fin de la función: mostrar_atributos_de_clase()


# Función que muestra los atributos de instancia en diversos objetos

def mostrar_atributos_de_instancia(perro, gato, vaca):
    # Acceso a atributos de clase
    print("\n\033[32m --ATRIBUTOS DE INSTANCIA--\033[0m")
    print("-------- Perro -----------")
    print("NOMBRE: ",perro.mi_nombre)                # Salida: Boby
    print("EDAD  : ",perro.mi_edad)                  # Salida: 3
    print("PESO  : ",perro.mi_peso)                  # Salida: 10

    # Acceso a atributos de clase
    print("\n--------- Vaca ----------")
    print("NOMBRE: ",vaca.mi_nombre)                # Salida: canela
    print("EDAD  : ",vaca.mi_edad)                  # Salida: 8
    print("PESO  : ",vaca.mi_peso)                  # Salida: 600

    # Acceso a atributos de clase
    print("\n-------- Gato -----------")
    print("NOMBRE: ",gato.mi_nombre)                # Salida: Minina
    print("EDAD  : ",gato.mi_edad)                  # Salida: 2
    print("PESO  : ",gato.mi_peso)                  # Salida: 1
    

# Fin de la función: mostrar_atributos_de_instancia()


# Funcion principal
def main():

    os.system("cls")

    # Instanciamientos de la clase MamiferoCuadrupedo
    perro = MamiferoCuadrupedo("Bobby", 3, 10) # Instanciado objeto perro
    gato = MamiferoCuadrupedo("Minina",2, 1)   # Instanciado objeto gato
    vaca = MamiferoCuadrupedo("Canela",8,600)  # Instanciado objeto vaca  

    mostrar_atributos_de_clase(perro, gato, vaca)
    print("\n\n")
    mostrar_atributos_de_instancia(perro, gato, vaca)

# Fin de definicion de funcion main()


# Cuerpo principal del programa
if __name__ == "__main__": 
    main()   

# Fin de cuerpo principal
