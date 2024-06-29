/* Programa que alcula si un número es <Capicúa>. 
   Los números capicúas son aquellos que se leen igual de izquierda a derecha
   y vicerversa.
   Ejms: 67576 , 77577, 223322 
   
   Procedimiento: Descomponer la cifra en sus respectivos dígitos de atrás hacia adelante,
                  y en la medida en que tenemos los dígitos, vamos armando una segunda cifra
                  pero 'al revés'. Finalmente se comparan las dos cifras y si son iguales
                  entonces la cifra original es <capicúa>.
   */


var estilos1 = "font-size: 24px; color : yellow";
    estilos2 = "font-size: 24px; color : lightgreen";
    cifraOriginal = 77587;
    cifraTemporal = cifraOriginal;  // Es la cifra que se va a ir descomponiendo (achicando).
    cifraInvertida = 0;   // para formar la cifra a la inversa

    do{
        
        let digito = cifraTemporal % 10; // Obtenemos el resto de la división, 
                                     //que será el último dígito.

        cifraInvertida = cifraInvertida * 10 + digito;

        cifraTemporal = Math.floor(cifraTemporal / 10);  // aquí se va descomponiendo la copia de 
                                                         // la cifraOriginal. Se busca pafrte entera. 

    } while (cifraTemporal != 0) ;    // Este es el unico ciclo que lleva " ; ". 

    if (cifraOriginal == cifraInvertida){

        console.log(`%cLa cifra ${cifraOriginal} es Capicúa `, estilos1);
    }
    else console.log(`%cLa cifra ${cifraOriginal} No es Capicúa `, estilos1);



