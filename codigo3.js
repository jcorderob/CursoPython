/* Programa que calcula el factorial de un número 
   7! = 7 * 6 * 5 * 4 * 3 * 2 * 1  
   1! = 1
   0! = 1 
   */


var estilos1 = "font-size: 24px; color : yellow";
    estilos2 = "font-size: 24px; color : lightgreen";
    valor = 7.5;

    if (Number.isInteger(valor)){
    
        var factorial = 1;

        for (let i=valor; i>=1; i--){
            factorial = factorial * i;
        }

        console.log(`%cEl Factorial de ${valor} es %c ${factorial}`, estilos1, estilos2);
    }
    else console.log("%c El número debe ser entero", estilos1);



