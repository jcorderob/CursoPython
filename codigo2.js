estilos1 = "font-size:18px; color: yellow" 
estilos2 = "font-size:18px; color: #33cc33"

/*   estilos1 RECOMENDADOS DE CODIFICACIÓN JAVASCRIPT

 Variables  = camelCase. Empieza con una letra minúscula y cada palabra subsecuente 
                         empieza con una letra mayúscula.

 Funciones  = Igual que las variables.

 Objetos    = camelCase.  Igual que las variables y funciones.
              Uso: Propiedades y métodos de objetos.

 Clases     = PascalCase. Similar a camelCase, pero empieza con una letra mayúscula.
              Uso: Nombres de clases y constructores.

 Constantes =  MAYÚSCULAS_SNAKE_CASE

 */

var nombre = "Albani Mendoza"
var edad   = 20 
var salario= 32567.75
var estadoCivil = 's'

console.log ("%cDATOS DE LA PERSONA:\n", estilos1)
console.log ("%cNOMBRE:"+ nombre+ "\n", estilos1)
console.log ("%cEDAD  :"+ edad+ "\n", estilos1)
console.log ("%cSALARIO:"+ salario+ "\n", estilos1)

var estadoCivil  = estadoCivil.toUpperCase()

switch (estadoCivil){
    case 'S' : estado = "Soltero(a)"
               break;
    case 'C' : estado = "Casado(a)"
               break;
    case 'D' : estado = "Divorciado(a)"
               break;
    case 'V' : estado = "Viudo(a)"
               break;
    default:
               estado = "Otro..."
    } // fin del switch 

console.log ("%cESTADO CIVIL: "+ estado , estilos1)

if (edad <= 12)
    console.log("\n%c"+ nombre + " Un(a) niño(a) ", estilos1)
else if (edad <= 19)
    console.log("\n%c"+ nombre + " es adolescente ", estilos1)
else if (edad <= 65)
    console.log("\n%c"+ nombre + " es adulto ", estilos1)
else
    console.log("\n%c"+ nombre + " adulto mayor ", estilos1)


/* Salida usando plantillas de cadena */

console.log (`\n%cESTADO CIVIL : ${estado}`, estilos1)


console.log ("%cESTADO CIVIL: %c"+estado, estilos1 , estilos2)

