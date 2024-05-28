import os

# Definición de clase
class MamiferoCuadrupedo:
    
    # Atributos de clase. Son idénticos para cada objeto (instancia)
    especie = "Mamífero"
    organos_respiratorios = ["Pulmones", "Fosas nasales"]
    extremidades = 4

    # Atributos de instancia. Varían entre los distintos objetos(instancias)
    
    def __init__(self, nombre, edad, peso):  # Método constructor
        self.__mi_nombre = nombre
        self.__mi_edad = edad
        self.__mi_peso = peso
    
    def get_datos_privados(self):
        cadena = "NOMBRE: " + self.__mi_nombre +"\n" + \
                 "EDAD  : " + str(self.__mi_edad) + "\n" + \
                 "PESO  : " + str(self.__mi_peso) + "\n"
        return (cadena)
    
    def set_cambiar_nombre(self,nuevo_nombre ):
        self.__mi_nombre = nuevo_nombre;


# Fin de definición de clase

# Funcion principal
def main():

    os.system("cls")

    # Instanciamientos de la clase MamiferoCuadrupedo
    perro = MamiferoCuadrupedo("Bobby", 3, 10) # Instanciado objeto perro
    
    # Acceso a atributos de instancia
    print("\n\033[32m --ATRIBUTOS DE INSTANCIA--\033[0m")
    print("-------- Perro -----------")
    print(perro.get_datos_privados())      # Getter que devuelve los datos privados de instancia

    perro.set_cambiar_nombre("Scooby Doo") # Setter que cambia el nombre

    print(perro.get_datos_privados())

# Fin de definicion de funcion main()


# Cuerpo principal del programa
if __name__ == "__main__": 
    main()   

# Fin de cuerpo principal
