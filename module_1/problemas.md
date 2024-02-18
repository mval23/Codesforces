1. Encuentra el cuadrado
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Siendo el primer ejercicio del curso y como para ir calentando motores, empecemos con algo bastante simple: dado un número entero N en el rango [ - 1000, 1000], mostrar su cuadrado.

**Input**  
La entrada contiene una única línea con el valor de N.

**Output**  
El cuadrado de N.

**Example**  
inputCopy  
7  
outputCopy  
49  

2. Hola mundo bilingüe  
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Ya todos conocemos el ultra famoso "Hola mundo", o su versión en inglés "Hello world". ¿Qué tal si hacemos una pequeña variación y complicados el asunto? La idea es que dado un entero positivo N en el rango no mayor a 10000, se alternen esos mensajes: una vez en español, la siguiente en inglés, la siguiente en español, y así sucesivamente hasta mostrar N mensajes.

**Input**  
La entrada contiene una única línea con el valor de N.

**Output**  
N líneas cada una con el mensaje (sin las comillas) "Hola mundo" y "Hello world" apareciendo de manera alternada.

**Example**  
inputCopy  
5  
outputCopy  
Hola mundo  
Hello world  
Hola mundo  
Hello world  
Hola mundo  

3. Positivos y negativos  
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Dada una secuencia de números enteros, ¿cuál será la sumatoria de los positivos, y cuál la de los negativos?

**Input**  
La entrada comienza con una línea que contiene un valor entero positivo N no mayor a mil. Posteriormente siguen N líneas, cada una con un entero dentro del rango [ - 9999, 9999]

**Output**  
Una única línea con el siguiente mensaje: "positivos Q, negativos R" (sin las comillas) y siendo Q y R la sumatoria de números positivos y negativos respectivamente.

**Example**  
inputCopy  
10  
45  
32  
-78  
16  
-32  
0  
-98  
-3  
40  
61  
outputCopy  
positivos 194, negativos -211  

4. Los 4 fantásticos  
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Los 4 fantásticos hicieron su debut en el mundo de los cómics en noviembre de 1961 bajo la editorial de Marvel, creados por Stan Lee y Jack Kirby. Su historia comienza cuando cuatro individuos (Reed Reichards, Susan Storm, Johnny Storm, y Ben Grimm) obtuvieron superpoderes tras la exposición a rayos cósmicos durante una misión científica al espacio exterior.

Hablando de cuartetos famosos, ¿Sabes que los cuatro primeros números primos son 2, 3, 5, y 7 verdad? Bueno, pues la idea es que dado un número entero positivo se debe decir si es múltiplo de alguno de esos cuatro o si no es múltiplo de ninguno. En caso que sea múltiplo de más de uno de ellos solo se debe mencionar al menor (por ejemplo el 210 es múltiplo de todos, entonces se debería mostrar "es múltiplo de 2").

En síntesis, dado un número entero positivo N mayor a 7 pero menor a un millón se debe mostrar uno, y solo uno, de estos cinco mensajes (sin tildes):

- es multiplo de 2
- es multiplo de 3
- es multiplo de 5
- es multiplo de 7
- no es multiplo de ninguno de los primeros cuatro primos

**Input**  
La entrada contiene una única línea con el valor de N.

**Output**  
Una única línea con el mensaje a mostrar.

**Example**  
inputCopy  
21  
outputCopy  
es multiplo de 3  

5. Potencias menores  
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Supongamos que queremos conocer todas las potencias enteras positivas del número 2 que sean menores o iguales a 50. Estas serían: 21 = 2, 22 = 4, 23 = 8, 24 = 16, y 25 = 32. O si quisiéramos conocer las del número 3 menores o iguales a 100 serían: 31 = 3, 32 = 9, 33 = 27, y 34 = 81.

Si generalizamos, el problema sería entonces encontrar las potencias enteras positivas del número A que sean menores o iguales a B.

**Input**  
La entrada comienza con una línea que contiene un valor entero positivo A (2≤A≤20). La siguiente línea contiene un valor entero positivo B (A≤B≤9 × 1016).

**Output**  
La salida debe tener, de a una por línea, las potencias correspondientes.

**Example**  
inputCopy  
5  
1000  
outputCopy  
5  
25  
125  

6. Conjetura de Collatz  
**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes  
**input:** standard input  
**output:** standard output  

Fuente: [Wikipedia](https://commons.wikimedia.org/wiki/File:Lothar_Collatz.jpg)  
La conjetura de Collatz, conocida también como conjetura 3N+1, fue enunciada por el matemático Lothar Collatz en 1937, y a la fecha no se ha resuelto.

Partiendo de la siguiente operación, aplicable a cualquier número entero positivo:  
- Si el número es par, se divide entre 2  
- Si el número es impar, se multiplica por 3 y se suma 1  

Que formalmente, equivale a tener una función:

f(N)=[ si N es par ; 3N+1 si N es impar]

La conjetura indica que para cualquier N, si se repite indefinidamente dicha operación, eventualmente se llegará a un valor de 1.

Por ejemplo, si N = 6, se obtendría la siguiente sucesión: 6, 3, 10, 5, 16, 8, 4, 2, 1

Si N = 13, se obtendría 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

**Input**  
La entrada contiene una línea con un valor entero positivo N no mayor a 1000.

**Output**  
La salida debe tener, de a una por línea, y comenzando por el valor de N los elementos de la sucesión hasta llegar a 1 (creeremos en Collatz y supondremos que siempre será una sucesión finita).

**Example**  
inputCopy  
11  
outputCopy  
11  
34  
17  
52  
26  
13  
40  
20  
10  
5  
16  
8  
4  
2  
1  
