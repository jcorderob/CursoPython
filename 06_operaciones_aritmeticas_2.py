import os

# Programa que resuelve una expresione aritmética
# ------------------- EJEMPLO 1-------------------

val1, val2, val3, val = 3, -3 , 4, 5

exp1 = 4 + 5 * 4 / 2 * 3
#       4 + 20   / 2 * 3
#       4 +     10   * 3  
#       4 +         30
#                


os.system("cls")
print("\n\n\n")
print (exp1)     



# Programa que resuelve una expresiones aritmética
# ------------------- EJEMPLO 2-------------------


exp2 = 3 * 2 ** 3 * 2 // (2 * 3)

# exp2 = 3 * 2 ** 3 * 2 // (6) 
# exp2 = 3 *   8    * 2 // (6)
# exp2 =   24       * 2 // (6)
# exp2 =        48      // (6)
# exp2 =              8

os.system("cls")
print("\n\n\n")
print (exp2) 





# Importancia de dar un valor inicial a las variables
# ------------------- EJEMPLO 3-------------------


val1, val2, val3, val4 = 5, 10, 15, 20

result = 0
result += val4  # result = result + val4

os.system("cls")
print("\n\n\n")
print (result) 

result = -result
print("\n\n")
print (result) 


