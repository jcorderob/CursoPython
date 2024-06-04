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
    
    @property
    def obtener_datos(self):
        cadena = "NOMBRE: " + self.__mi_nombre +"\n" + \
                 "EDAD  : " + str(self.__mi_edad) + "\n" + \
                 "PESO  : " + str(self.__mi_peso) + "\n"
        return (cadena)
    
    @property   # Todos estos métodos (getter, setter, y deleter) con igual nombre
    def mi_nombre(self):
        return "El nuevo nombre es: "+ self.__mi_nombre
    
    @mi_nombre.setter
    def mi_nombre(self,nuevo_nombre ):
        self.__mi_nombre = nuevo_nombre


# Fin de definición de clase

# Funcion principal
def main():

    os.system("cls")

    # Instanciamientos de la clase MamiferoCuadrupedo
    perro = MamiferoCuadrupedo("Bobby", 3, 10) # Instanciado objeto perro
    
    # Acceso a atributos de instancia
    print("\n\033[32m --ATRIBUTOS DE INSTANCIA--\033[0m")
    print("-------- Perro -----------")
    print(perro.obtener_datos)      # Getter que devuelve los datos privados de instancia

    perro.mi_nombre = "Scooby Doo" # Setter se comporta como un atributo ,
                                   # no deben usarse los peréntesis "()".

    print(perro.mi_nombre)

# Fin de definicion de funcion main()


# Cuerpo principal del programa
if __name__ == "__main__": 
    main()   

# Fin de cuerpo principal
