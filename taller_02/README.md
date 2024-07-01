# Taller 02: Análisis Sintáctico

## Introducción
El problema de dos vías de clasificación utilizando la teoría de rachas es un método estadístico empleado para analizar datos categóricos y observar patrones. La teoría de rachas se utiliza en pruebas estadísticas, como las pruebas de Friedman, para evaluar la consistencia de un conjunto de observaciones.

Para ayudar al estadístico a trabajar con estas pruebas, el lenguaje de programación debe permitir:

1. **Definir y manejar variables y arreglos/matrices:** Esto es crucial para almacenar datos y resultados intermedios.
2. **Realizar operaciones matemáticas y lógicas:** Necesario para llevar a cabo cálculos y comparaciones.
3. **Estructuras de control de flujo:** Permiten ejecutar algoritmos que involucran ciclos y decisiones condicionales.
4. **Funciones de entrada/salida:** Para mostrar resultados y posiblemente leer datos.


## Requisitos
- FLEX
- GCC
- Bison
- Un editor de texto (recomendado Visual Studio Code)

## Instalación WSL (Windows Subsystem for Linux)

En una terminal, ejecuta los siguientes comandos para instalar FLEX y GCC si aún no los tienes instalados:

```sh
sudo apt-get update
sudo apt-get install flex
sudo apt-get install gcc
sudo apt-get install bison
```

## Compilación

1. **Generar el analizador léxico**:
    Utiliza FLEX para generar el archivo `lex.yy.c` a partir del archivo `lexer.l`.
    
    ```sh
    flex -o lex.yy.c lexer.l
    ```

    donde `-o lex.yy.c` indica que el archivo de salida se llamará `lex.yy.c`.

2. **Compilar la gramática**:
    Usa Bison para generar el archivo `gramamr.tab.c` y `gramamr.tab.h` a partir del archivo `gramamr.y`.

    ```sh
    bison -d grammar.y
    ```

    donde `-d` indica que se debe generar el archivo de cabecera `gramamr.tab.h`.

3. **Compilar el código generado**:
    Usa GCC para compilar los archivos generados `lex.yy.c` y `gramamr.tab.c` y crear un ejecutable llamado `parser`.

    ```sh
    gcc lex.yy.c grammar.tab.c -o parser -lfl
    ```

## Ejecución
1. **Crear el archivo de entrada**:
   Crea un archivo de entrada llamado `input01.txt` con el siguiente contenido:

   ```plaintext
    int a = 5;
    float b = 3.14;

    // Definición de una matriz 3x3
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Variables auxiliares
    int i; 
    int j;
   ```

2. **Ejecutar el analizador léxico**:
    ```sh
    ./parser < input01.txt
    ```

    donde `< input01.txt` indica que la entrada del programa se leerá desde el archivo `input.txt`.


## Salida de la ejecución

Para la entrada
```plaintext
int a = 5;
float b = 3.14;

// Definición de una matriz 3x3
int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Variables auxiliares
int i; 
int j;
```

Tenemos una ejecución exitosa del analizador léxico, y la salida será similar a la siguiente, la cual vamos a desglosar a continuación:

Ejecución del analizador léxico

```shell
$ ./parser < input01.txt
```

Salida del analizador léxico

```plaintext
Starting parse
Entering state 0
```

Arriba notamos que el analizador léxico ha comenzado a analizar el archivo de entrada. La salida indica que el analizador ha entrado en el estado 0, el cual es el estado inicial del autómata.

```plaintext
Stack now 0
Reading a token
Next token is token INT ()
Shifting token INT ()
Entering state 1
```

La parte `Stack now 0` indica que la pila está vacía. El analizador léxico ha leído el token `INT` y ha entrado en el estado 1, el cual es el estado que indica que se ha encontrado un token `INT`. `Shifting token INT ()` indica que el token `INT` se ha movido a la pila.

```plaintext
Stack now 0 1
Reducing stack by rule 7 (line 71):
   $1 = token INT ()
-> $$ = nterm type ()
Entering state 6
```

La parte `Stack now 0 1` indica que la pila contiene los estados 0 y 1. El analizador léxico ha reducido la pila utilizando la regla 7, la cual indica que el token `INT` se ha reducido a un `nterm type`. `Entering state 6` indica que el analizador ha entrado en el estado 6, el cual es el estado que indica que se ha encontrado un tipo.

```plaintext
Stack now 0 6
Reading a token
Next token is token IDENTIFIER ()
Shifting token IDENTIFIER ()
Entering state 21
```

La parte `Stack now 0 6` indica que la pila contiene los estados 0 y 6. El analizador léxico ha leído el token `IDENTIFIER` y ha entrado en el estado 21, el cual es el estado que indica que se ha encontrado un token `IDENTIFIER`. `Shifting token IDENTIFIER ()` indica que el token `IDENTIFIER` se ha movido a la pila.

```plaintext
Stack now 0 6 21
Reading a token
Next token is token ASSIGN ()
Shifting token ASSIGN ()
Entering state 28
```

El analizador léxico ha leído el token `ASSIGN` y ha entrado en el estado 28, el cual es el estado que indica que se ha encontrado un token `ASSIGN`. `Shifting token ASSIGN ()` indica que el token `ASSIGN` se ha movido a la pila.

```plaintext
Stack now 0 6 21 28
Reading a token
Next token is token NUMBER ()
Shifting token NUMBER ()
Entering state 33
```

El analizador léxico ha leído el token `NUMBER` y ha entrado en el estado 33, el cual es el estado que indica que se ha encontrado un token `NUMBER`. `Shifting token NUMBER ()` indica que el token `NUMBER` se ha movido a la pila.

```plaintext
Stack now 0 6 21 28 33
Reducing stack by rule 27 (line 124):
   $1 = token NUMBER ()
-> $$ = nterm expression ()
Entering state 40
```

El analizador léxico ha reducido la pila utilizando la regla 27, la cual indica que el token `NUMBER` se ha reducido a un `nterm expression`. `Entering state 40` indica que el analizador ha entrado en el estado 40, el cual es el estado que indica que se ha encontrado una expresión.

```plaintext
Stack now 0 6 21 28 40
Reading a token
Next token is token SEMICOLON ()
Shifting token SEMICOLON ()
Entering state 59
```

El analizador léxico ha leído el token `SEMICOLON` y ha entrado en el estado 59, el cual es el estado que indica que se ha encontrado un token `SEMICOLON`. `Shifting token SEMICOLON ()` indica que el token `SEMICOLON` se ha movido a la pila.

```plaintext
Stack now 0 6 21 28 40 59
Reducing stack by rule 5 (line 66):
   $1 = nterm type ()
   $2 = token IDENTIFIER ()
   $3 = token ASSIGN ()
   $4 = nterm expression ()
   $5 = token SEMICOLON ()
-> $$ = nterm declaration_statement ()
Entering state 5
```

El analizador léxico ha reducido la pila utilizando la regla 5, la cual indica que los tokens `type`, `IDENTIFIER`, `ASSIGN`, `expression` y `SEMICOLON` se han reducido a un `nterm declaration_statement`. `Entering state 5` indica que el analizador ha entrado en el estado 5, el cual es el estado que indica que se ha encontrado una declaración.

A este punto se procesado la primera línea del archivo de entrada `int a = 5;`. El analizador léxico continuará procesando el resto del archivo de entrada de manera similar.

```plaintext
...(continuación de la salida)...
Stack now 0 4
Now at end of input.
Reducing stack by rule 15 (line 91):
-> $$ = nterm statements ()
Entering state 13
```

Finalmente, la salida indica que el analizador léxico ha llegado al final de la entrada y ha reducido la pila utilizando la regla 15, la cual indica que se ha encontrado un `nterm statements`. `Entering state 13` indica que el analizador ha entrado en el estado 13, el cual es el estado final del autómata.

```plaintext
Stack now 0 4 13
Reducing stack by rule 1 (line 56):
   $1 = nterm declarations ()
   $2 = nterm statements ()
Program parsed successfully.
-> $$ = nterm program ()
Entering state 3
```

La salida final indica que el programa se ha analizado correctamente y que se ha encontrado un `nterm program`. `Entering state 3` indica que el analizador ha entrado en el estado 3, el cual es el estado final del autómata.

```plaintext
Stack now 0 3
Now at end of input.
Shifting token "end of file" ()
Entering state 7
```

Finalmente, el analizador léxico ha llegado al final de la entrada y ha entrado en el estado 7, el cual es el estado final del autómata.

```plaintext
Stack now 0 3 7
Stack now 0 3 7
Cleanup: popping token "end of file" ()
Cleanup: popping nterm program ()
```

La salida final indica que el analizador léxico ha terminado de analizar el archivo de entrada y ha limpiado la pila.

## Especificación de patrónes léxicos
Para el análisis léxico de nuestro lenguaje de programación, se han definido los siguientes patrones léxicos en el archivo `lexer.l`:

```lex
%{
#include "grammar.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

/*** Definición de patrones utilizando expresiones regulares ***/
digit      [0-9]
letter     [a-zA-Z_]
identifier {letter}({letter}|{digit})*
number     {digit}+(\.{digit}+)?
whitespace [ \t\n\r]+

/*** Reglas de sustitución ***/
%%
"int"       { return INT; }         /* Tipo de dato entero */
"float"     { return FLOAT; }       /* Tipo de dato flotante */
"if"        { return IF; }          /* Estructura de selección */
"else"      { return ELSE; }        /* Parte de la estructura de selección */
"for"       { return FOR; }         /* Estructura de iteración */
"while"     { return WHILE; }       /* Estructura de iteración */
"print"     { return PRINT; }       /* Función de impresión */
"read"      { return READ; }        /* Función de lectura */

"="         { return ASSIGN; }      /* Operador de asignación */
";"         { return SEMICOLON; }   /* Punto y coma */
"("         { return LPAREN; }      /* Paréntesis izquierdo */
")"         { return RPAREN; }      /* Paréntesis derecho */
"{"         { return LBRACE; }      /* Llave izquierda */
"}"         { return RBRACE; }      /* Llave derecha */
"<"         { return LT; }          /* Operador menor que */
">"         { return GT; }          /* Operador mayor que */
"+"         { return PLUS; }        /* Operador de suma */
"-"         { return MINUS; }       /* Operador de resta */
"*"         { return MULT; }        /* Operador de multiplicación */
"/"         { return DIV; }         /* Operador de división */
"=="        { return EQ; }          /* Operador igual a */
"!="        { return NEQ; }         /* Operador diferente a */
"<="        { return LEQ; }         /* Operador menor o igual que */
">="        { return GEQ; }         /* Operador mayor o igual que */
"\""        { return QUOTE; }       /* Comillas dobles */
"["         { return LBRACKET; }    /* Corchete izquierdo */
"]"         { return RBRACKET; }    /* Corchete derecho */
","         { return COMMA; }       /* Coma */

{identifier}   { yylval.str = strdup(yytext); return IDENTIFIER; }          /* Identificador */
{number}       { yylval.num = atof(yytext); return NUMBER; }                /* Número */
{whitespace}   { /* Ignorar espacios en blanco */ }                         /* Espacios en blanco */
"//".*         { /* Ignorar comentarios de una línea */ }                   /* Comentarios de una línea */
.              { printf("Unexpected character: %c\n", *yytext); exit(1); }  /* Caracter inesperado */

%%
/*** Función de cierre ***/
int yywrap(void) {
    return 1;
}
```

¡Felicidades por haber logrado el análisis correcto del archivo de entrada! A continuación, se actualiza la sección de la especificación de BNF de la gramática en tu documento para que use EBNF:

## Especificación EBNF de la gramática

La especificación de la gramática de nuestro lenguaje se encuentra en el archivo `grammar.bnf`. La gramática se encuentra en formato EBNF y se ha dividido en varias reglas para facilitar su lectura. La gramática se ha definido de acuerdo a los requerimientos del enunciado del taller 02, orientado al problema de dos vías de clasificación utilizando conceptos de teoría de rachas.

### Programa `program`

Un programa comienza con la declaración de variables y arreglos que se utilizarán a lo largo del análisis, seguido de las instrucciones que definen el flujo del programa y realizan cálculos estadísticos.

```ebnf
program = declarations, statements ;
```

**Ejemplo:**
```plaintext
int n;
float mean;
n = 10;
mean = 0.0;
for (int i = 0; i < n; i = i + 1) {
    mean = mean + data[i];
}
mean = mean / n;
print(mean);
```

### Declaraciones `declarations`

En las declaraciones la recursión permite una cantidad arbitraria de declaraciones. Las declaraciones son necesarias para definir las variables y arreglos que se utilizarán en el programa.

```ebnf
declarations = { declaration_statement } ;
```

**Ejemplo:**
```plaintext
int n;
float mean;
```

### Declaración `declaration_statement`

Existen tres tipos de declaraciones: variables simples, variables inicializadas, y arreglos. Las declaraciones permiten definir las variables y arreglos necesarios para almacenar datos y resultados de las pruebas estadísticas.

```ebnf
declaration_statement = type, IDENTIFIER, ";"
                      | type, IDENTIFIER, "=", expression, ";"
                      | type, IDENTIFIER, array_initialization, ";" ;
```

**Ejemplo:**
```plaintext
int n;
float mean = 0.0;
int data[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

### Tipo `type`

Se soportan tipos `int` y `float` porque las pruebas estadísticas pueden involucrar datos enteros y de punto flotante.

```ebnf
type = "int" | "float" ;
```

### Inicialización de Arreglos `array_initialization`

Permite la inicialización de matrices, las cuales son esenciales para almacenar tablas de datos en un análisis de clasificación de dos vías.

```ebnf
array_initialization = "[", NUMBER, "]", "=", "{", numbers, "}"
                     | "[", NUMBER, "]", "[", NUMBER, "]", "=", "{", array_elements, "}" ;
```

**Ejemplo:**
```plaintext
int data[2][3] = {{1, 2, 3}, {4, 5, 6}};
```

### Elementos de Arreglos `array_elements`

Soporta la inicialización de elementos de matrices, permitiendo una estructura clara y flexible para definir los datos. La **recursión** permite una cantidad arbitraria de elementos de matriz.

```ebnf
array_elements = "{", numbers, "}"
               | array_elements, ",", "{", numbers, "}" ;
```

**Ejemplo:**
```plaintext
{1, 2, 3}
{{1, 2, 3}, {4, 5, 6}}
```

### Lista de números `numbers`

Permite la especificación de listas de números, necesarios para llenar las matrices con datos de observación.

```ebnf
numbers = NUMBER
        | numbers, ",", NUMBER ;
```

**Ejemplo:**
```plaintext
1
1, 2, 3
```

### Expresiones `expression`

Permite la realización de cálculos matemáticos y lógicos, necesarios para llevar a cabo pruebas estadísticas y comparaciones de datos. Las expresiones soportadas son:
- Números
- Identificadores
- Operador aritmético de suma
- Operador aritmético de resta
- Operador aritmético de multiplicación
- Operador aritmético de división
- Paréntesis
- Operador de comparación menor que
- Operador de comparación mayor que
- Operador de comparación igual a
- Operador de comparación diferente de
- Operador de comparación menor o igual que
- Operador de comparación mayor o igual que

```ebnf
expression = NUMBER
           | IDENTIFIER
           | expression, "+", expression
           | expression, "-", expression
           | expression, "*", expression
           | expression, "/", expression
           | "(", expression, ")"
           | expression, "<", expression
           | expression, ">", expression
           | expression, "==", expression
           | expression, "!=", expression
           | expression, "<=", expression
           | expression, ">=", expression
           | IDENTIFIER, "[", expression, "]" ;  // Acceso a elementos de arreglos
```

**Ejemplo:**
```plaintext
x + y
(x - y) / z
total >= 0
data[i]
```

### Sentencias `statements`

Permite una secuencia de sentencias que define el flujo del programa, incluyendo cálculos, condicionales y bucles. La **recursión** permite una cantidad arbitraria de sentencias.

```ebnf
statements = { statement } ;
```

**Ejemplo:**
```plaintext
n = 10;
mean = 0.0;
for (int i = 0; i < n; i = i + 1) {
    mean = mean + data[i];
}
mean = mean / n;
print(mean);
```

### Tipos de Sentencias

Proporciona las estructuras de control de flujo necesarias para implementar algoritmos de análisis estadístico.

```ebnf
statement = assignment_statement
          | if_statement
          | while_statement
          | for_statement
          | print_statement ;
```

### Asignación `assignment_statement`

Permite asignar valores a variables y arreglos, necesarios para almacenar resultados intermedios y finales de las pruebas estadísticas.

```ebnf
assignment_statement = IDENTIFIER, "=", expression, ";" ;
```

**Ejemplo:**
```plaintext
n = 10;
mean = 0.0;
```

### Asignación en Bucle `loop_assignment_statement`

Permite la asignación de valores en bucles, esencial para realizar cálculos iterativos en pruebas estadísticas.

```ebnf
loop_assignment_statement = type, IDENTIFIER, "=", expression
                          | IDENTIFIER, "=", expression ;
```

**Ejemplo:**
```plaintext
j = 0
i = i + 1
k = k * 2
```

### Condicional If-Else `if_statement`

Permite la ejecución condicional de bloques de código, esencial para implementar algoritmos que requieren decisiones basadas en condiciones.

```ebnf
if_statement = "if", "(", expression, ")", "{", statements, "}", "else", "{", statements, "}"
             | "if", "(", expression, ")", "{", statements, "}" ;
```

**Ejemplo:**
```plaintext
if (n > 0) {
    mean = total / n;
} else {
    mean = 0;
}
```

### Bucle While `while_statement`

Permite la ejecución repetida de un bloque de código mientras se cumpla una condición, necesario para implementar algoritmos iterativos.

```ebnf
while_statement = "while", "(", expression, ")", "{", statements, "}" ;
```

**Ejemplo:**
```plaintext
while (i < n) {
    total += data[i];
    i = i + 1;
}
```

### Bucle For `for_statement`

Permite la ejecución repetida de un bloque de código con una inicialización, condición y actualización, esencial para implementar algoritmos iterativos.

```ebnf
for_statement = "for", "(", loop_assignment_statement, ";", expression, ";", loop_assignment_statement, ")", "{", statements, "}" ;
```

**Ejemplo:**
```plaintext
for (i = 0; i < n; i = i + 1) {
    total += data[i];
}
```

### Impresión `print_statement`

Permite la impresión de valores en la consola, necesaria para mostrar resultados intermedios y finales de las pruebas estadísticas.

```ebnf
print_statement = "print", "(", expression, ")", ";" ;
```

**Ejemplo:**
```plaintext
print(mean);
```

### Números `NUMBER`

Permite la especificación de números enteros y de punto flotante, necesarios para realizar cálculos estadísticos y comparaciones.

```ebnf
NUMBER = /* expresión regular para número */
```

### Identificadores `IDENTIFIER`

Permite la especificación de identificadores, necesarios para nombrar variables y arreglos en el programa.

```ebnf
IDENTIFIER = /* expresión regular para identificador */
```

### Gramática Completa
La especificación completa se vería así:
```bnf
<program> ::= <declarations> <statements>

<declarations> ::= <declaration> <declarations>
                 | /* empty */

<declaration> ::= <type> <IDENTIFIER> ";"
                | <type> <IDENTIFIER> "=" <expression> ";"
                | <type> <IDENTIFIER> <array_initialization> ";"

<type> ::= "int"
         | "float"

<array_initialization> ::= "[" <NUMBER> "]" "[" <NUMBER> "]" "=" "{" <array_elements> "}"

<array_elements> ::= "{" <numbers> "}"
                   | <array_elements> "," "{" <numbers> "}"

<numbers> ::= <NUMBER>
            | <numbers> "," <NUMBER>

<expression> ::= <NUMBER>
               | <IDENTIFIER>
               | <expression> "+" <expression>
               | <expression> "-" <expression>
               | <expression> "*" <expression>
               | <expression> "/" <expression>
               | "(" <expression> ")"
               | <expression> "<" <expression>
               | <expression> ">" <expression>
               | <expression> "==" <expression>
               | <expression> "!=" <expression>
               | <expression> "<=" <expression>
               | <expression> ">=" <expression>

<statements> ::= <statement> <statements>
               | /* empty */

<statement> ::= <assignment_statement>
              | <if_statement>
              | <while_statement>
              | <for_statement>
              | <print_statement>

<assignment_statement> ::= <IDENTIFIER> "=" <expression> ";"

<loop_assignment_statement> ::= <IDENTIFIER> "=" <expression>

<if_statement> ::= "if" "(" <expression> ")" "{" <statements> "}" "else" "{" <statements> "}"
                 | "if" "(" <expression> ")" "{" <statements> "}"

<while_statement> ::= "while" "(" <expression> ")" "{" <statements> "}"

<for_statement> ::= "for" "(" <loop_assignment_statement> ";" <expression> ";" <loop_assignment_statement> ")" "{" <statements> "}"

<print_statement> ::= "print" "(" <expression> ")" ";"

<NUMBER> ::= /* expresión regular para número */

<IDENTIFIER> ::= /* expresión regular para identificador */
```

## Referencias
[^1]: [GNU Flex manual](https://ftp.gnu.org/old-gnu/Manuals/flex-2.5.4/html_mono/flex.html)
[^2]: [Lexical Analysis With Flex, for Flex 2.6.2](https://westes.github.io/flex/manual/)
[^3]: [Compilers: Principles, Techniques, & Tools, 2nd ed](https://www.google.com.co/books/edition/Compilers/dIU_AQAAIAAJ?hl=en&gbpv=0&bsq=Compilers:%20Principles,%20Techniques,%20and%20Tools%202ed)
[^4]: [Bison 3.8.1](https://www.gnu.org/software/bison/manual/bison.html)