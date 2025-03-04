## ejerciocio 1.
la difernetes formas en la que se pueden representar datos con N bits esta dad por la ecuacion 2^N

## consulta 1

1.En una computadora, todos los datos se representan utilizando el sistema binario, que está compuesto por bits (0 y 1). Estos bits son la unidad básica de información y se combinan para representar números, letras, imágenes, sonidos y cualquier otro tipo de información. Por ejemplo, los números se convierten a su equivalente binario mediante sistemas como el binario puro (para enteros) o el estándar IEEE 754 (para números decimales). Las letras y caracteres se representan mediante códigos como ASCII o Unicode, donde cada carácter tiene un valor numérico único que se traduce a binario. Las imágenes se descomponen en píxeles, y cada píxel se codifica en binario según su color, utilizando sistemas como RGB. En resumen, cualquier dato que ingresamos a una computadora se convierte en una secuencia de bits que el hardware y el software pueden procesar, almacenar y manipular.

2.nuestro sistema operativo más usado, windows, es uno basado en 64 bits, lo cual son unas 1.846674407x10^19 formas de guardar informacion, y no ha surguido un sistema difeente pq no se han gastado esas posibilidades de guardar información, si en el futuro el sisitema evolucionara, las posibilidades serian, de hecho, estas mismas al cuadrado.

3.

| Unidad       | Símbolo | Equivalencia               |
|--------------|---------|----------------------------|
| Byte         | B       | 1 Byte                     |
| Kilobyte     | KB      | 1,024 Bytes                |
| Megabyte     | MB      | 1,024 Kilobytes (KB)       |
| Gigabyte     | GB      | 1,024 Megabytes (MB)       |
| Terabyte     | TB      | 1,024 Gigabytes (GB)       |
| Petabyte     | PB      | 1,024 Terabytes (TB)       |
| Exabyte      | EB      | 1,024 Petabytes (PB)       |
| Zettabyte    | ZB      | 1,024 Exabytes (EB)        |
| Yottabyte    | YB      | 1,024 Zettabytes (ZB)      |

4.La creacion de un sistema más simple para representar datos garndes es la base de la evolucion de la tecnologia, sin esa, es muy dificil imaginar otra que tenga la misma eficiencia.

## ejercicio 2

1.

-10101010102 = 682_10

-111112 =31_10

-100000002 = 128_10

-1001001002 = 292_10

-1110002 = 56_10

2.usando divisiones sucesivas

-127_10=1111111_2
-246_10=11110110_2
-1025_10=10000000001_2
-354_10=101100010_2
-187_10=10111011_2

## ejercicio 3

1. 
Números enteros

C:

-int: Entero con signo (generalmente 4 bytes).

-short: Entero corto con signo (generalmente 2 bytes).

-long: Entero largo con signo (generalmente 4 o 8 bytes).

-unsigned int, unsigned short, unsigned long: Enteros sin signo.

Java:

-int: Entero con signo (4 bytes).

-short: Entero corto con signo (2 bytes).

-long: Entero largo con signo (8 bytes).

-byte: Entero muy corto con signo (1 byte).

-No tiene tipos sin signo.
Python:
int: Entero de precisión arbitraria (no tiene límite de tamaño).

2. 
Números decimales (flotantes)

C:

-float: Número de punto flotante de precisión simple (4 bytes).

-double: Número de punto flotante de precisión doble (8 bytes).

-long double: Precisión extendida (depende de la implementación).
Java:

-float: Precisión simple (4 bytes).

-double: Precisión doble (8 bytes).
Python:

-float: Número de punto flotante de doble precisión (equivalente a double en C/Java).

3. 
Letras del alfabeto (caracteres)

C:

-char: Un solo carácter (1 byte).
Java:

-char: Un solo carácter (2 bytes, soporta Unicode).
Python:

-No tiene un tipo específico para caracteres individuales. Usa cadenas de 
longitud 1 (str).

4.
 Cadenas de texto

C:

-No tiene un tipo de dato nativo para cadenas. Se usan arreglos de caracteres (char[]) terminados en \0.

Java:

-String: Cadena de caracteres (inmutable y soporta Unicode).
Python:

-str: Cadena de caracteres (inmutable y soporta Unicode).

5. 
Valores booleanos
C:
 
 -No tiene un tipo booleano nativo. Se usa int (0 para false, 1 para true).
 
 -En C99, se introdujo _Bool y la macro bool (definida en <stdbool.h>).

Java:

 -boolean: Puede ser true o false.

Python:

 -bool: Puede ser True o False (es una subclase de int, donde True es 1 y False es 0).

6. 
Otros tipos de datosC:

-void: Representa la ausencia de tipo (usado en funciones que no retornan valor).

-Punteros: int*, char*, etc.
Java:

-void: Representa la ausencia de tipo (usado en métodos que no retornan valor).

-Tipos de referencia: Clases, interfaces, arreglos.
Python:

-None: Representa la ausencia de valor.

-Tipos dinámicos: No se declara el tipo de una variable explícitamente.

## ejercicio 4
| Tipo de dato       | C                  | Java               | Python       |
|--------------------|--------------------|--------------------|--------------|
| Entero             | `int`, `short`, `long` | `int`, `short`, `long` | `int`        |
| Decimal            | `float`, `double`  | `float`, `double`  | `float`      |
| Carácter           | `char`             | `char`             | `str` (longitud 1) |
| Cadena de texto    | `char[]`           | `String`           | `str`        |
| Booleano           | `_Bool` (C99)      | `boolean`          | `bool`       |
| Sin valor          | `void`             | `void`             | `None`       |

## ejercicio 5

hay datos int, float, bool, char. Que dan como resultado:
4(entero)+4(flotante)+1(booleano)+10(texto)=19bytes

en tiempo serian 360resgistros/hora
por 24 hrs darian 8640 registros
en espacio serian 8640*19bytes que dan:
164160bytes
en KB es 164160bytes/1024 ≈ 160.31KB
en MB es 160.31KB/1024 ≈ 0.1565MB
que es el resultado final

## ejercicio 6
que tal vez a la hora de evaluar por encima se ve muchos, pero despues de convertirlos me doy cuenta que son muy pocos, y la gran informacion de datos que se trasfieren frecuentemente en el mundo que son unos 5 trillones de bytes de datos al día.