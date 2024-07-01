# Taller 01: Análisis Léxico LEX

## Introducción

Este proyecto es parte del Taller 01 del curso de compiladores, cuyo objetivo es construir un analizador léxico para un lenguaje de programación de propósito específico utilizando la herramienta FLEX. El analizador léxico es capaz de reconocer varios elementos del lenguaje, incluyendo palabras clave, identificadores, operadores, literales y estructuras de control, así como realizar cálculos específicos para el problema de dos vías de clasificación utilizando rachas.

## Requisitos

- FLEX
- GCC
- Un editor de texto (recomendado Visual Studio Code)

## Instalación WSL (Windows Subsystem for Linux)

En una terminal, ejecuta los siguientes comandos para instalar FLEX y GCC si aún no los tienes instalados:

```sh
sudo apt-get update
sudo apt-get install flex
sudo apt-get install gcc
```

## Compilación

1. **Generar el analizador léxico**:
   Utiliza FLEX para generar el archivo `lex.yy.c` a partir del archivo `lexer.l`.

   ```sh
   flex lexer.l
   ```

2. **Compilar el código generado**:
   Usa GCC para compilar el archivo generado `lex.yy.c` y crear un ejecutable llamado `lexer`.

   ```sh
   gcc lex.yy.c -o lexer -lfl
   ```

## Ejecución

1. **Crear el archivo de entrada**:
   Crea un archivo de entrada llamado `input.txt` con el siguiente contenido:

   ```plaintext
    begin
    // Declaraciones
    int a = 5;
    float b = 3.14;
    int i;
    int j;
    int T_mod = 0;
    int T_bi[3];
    int T_tj[3];
    int R_mod = 0;
    float P_ij[3][3];
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int R_ij[3][3] = {
        {1, 1, 1},
        {1, 1, 1},
        {1, 1, 1}
    };

    // Calcular el total de datos del modelo
    for (i = 0; i < 3; i = i + 1) {
        for (j = 0; j < 3; j = j + 1) {
            T_mod = T_mod + matrix[i][j];
        }
    }
    print(T_mod);

    // Calcular el total de datos por bloque

    for (i = 0; i < 3; i = i + 1) {
        T_bi[i] = 0;
        for (j = 0; j < 3; j = j + 1) {
            T_bi[i] = T_bi[i] + matrix[i][j];
        }
        print(T_bi[i]);
    }

    // Calcular el total de datos por tratamiento
    for (j = 0; j < 3; j = j + 1) {
        T_tj[j] = 0;
        for (i = 0; i < 3; i = i + 1) {
            T_tj[j] = T_tj[j] + matrix[i][j];
        }
        print(T_tj[j]);
    }

    // Calcular el número de rachas por celda (simplificado para el ejemplo)

    for (i = 0; i < 3; i = i + 1) {
        for (j = 0; j < 3; j = j + 1) {
            print(R_ij[i][j]);
        }
    }

    // Calcular el número total de rachas en el modelo

    for (i = 0; i < 3; i = i + 1) {
        for (j = 0; j < 3; j = j + 1) {
            R_mod = R_mod + R_ij[i][j];
        }
    }
    print(R_mod);

    // Calcular el promedio de rachas por celda (simplificado para el ejemplo)
    for (i = 0; i < 3; i = i + 1) {
        for (j = 0; j < 3; j = j + 1) {
            P_ij[i][j] = cast(float,R_ij[i][j]) / cast(float,matrix[i][j]);
            print(P_ij[i][j]);
        }
    }

    end
   ```

2. **Ejecutar el analizador léxico**:
   Ejecuta el analizador léxico con el archivo de entrada `input.txt`.

   ```sh
   ./lexer < input.txt
   ```

## Propósito del Programa

El propósito de este programa es analizar un archivo en el que se define un lenguaje de programación para resolver el problema de dos vías de clasificación utilizando conceptos de teoria de rachas.

Revisar [Marco Teórico](./marcoteorico.md) para más información.

### Operaciones Específicas

- **Calcular el total de datos del modelo (`T_mod`)**: Suma de todos los valores en la matriz `matrix`.
- **Calcular el total de datos por bloque (`T_bi`)**: Suma de los valores en cada fila de la matriz `matrix`.
- **Calcular el total de datos por tratamiento (`T_tj`)**: Suma de los valores en cada columna de la matriz `matrix`.
- **Calcular el número de rachas por celda (`R_ij`)**: En este ejemplo simplificado, se asume que cada celda tiene una racha.
- **Calcular el número total de rachas en el modelo (`R_mod`)**: Suma del número de rachas en todas las celdas.
- **Calcular el promedio de rachas por celda (`P_ij`)**: División del número de rachas en cada celda por el valor en la celda correspondiente de la matriz.

## Vocabulario del Lenguaje

El vocabulario completo que reconoce el lenguaje de programación de propósito específico incluye palabras clave, identificadores, números, operadores y símbolos. A continuación se detallan los elementos que forman parte del vocabulario del lenguaje:

- **Palabras clave:**
  - `begin`: Inicio del programa.
  - `end`: Fin del programa.
  - `int`: Tipo de dato entero.
  - `float`: Tipo de dato flotante.
  - `if`: Estructura condicional.
  - `else`: Estructura condicional.
  - `for`: Estructura de repetición.
  - `while`: Estructura de repetición.
  - `print`: Función de impresión.
  - `read`: Función de lectura.
  - `cast`: Función de conversión de tipo.

- **Operadores y símbolos:**
  - `=`
  - `;`
  - `(`
  - `)`
  - `{`
  - `}`
  - `[`
  - `]`
  - `<`
  - `>`
  - `+`
  - `-`
  - `*`
  - `/`
  - `==`
  - `!=`
  - `<=`
  - `>=`
  - `,`
  - `"`

### Categorías Léxicas

Las categorías léxicas necesarias para la construcción del lenguaje de programación de propósito específico son las siguientes:

- **Palabras clave:** Son las palabras reservadas que tienen un significado específico en el lenguaje y no pueden ser utilizadas como identificadores.
  - `BEGIN_PROGRAM`
  - `END_PROGRAM`
  - `INT`
  - `FLOAT`
  - `IF`
  - `ELSE`
  - `FOR`
  - `WHILE`
  - `PRINT`
  - `READ`
  - `CAST_FUNC`

- **Identificadores:** Son los nombres de variables definidos por el usuario.
  - `IDENTIFIER`

- **Números:**
  - `NUMBER`

- **Operadores aritméticos:** Son los operadores utilizados para realizar operaciones matemáticas.
  - `PLUS`
  - `MINUS`
  - `MULT`
  - `DIV`

- **Operadores de comparación:** Son los operadores utilizados para comparar valores.
  - `LT`
  - `GT`
  - `EQ`
  - `NEQ`
  - `LEQ`
  - `GEQ`

- **Símbolos:** Son los símbolos utilizados para delimitar bloques de código o expresiones.
  - `ASSIGN`
  - `SEMICOLON`
  - `LPAREN`
  - `RPAREN`
  - `LBRACE`
  - `RBRACE`
  - `LBRACKET`
  - `RBRACKET`
  - `COMMA`
  - `QUOTE`

### Patrones Basados en Expresiones Regulares

Los patrones basados en expresiones regulares se utilizan para identificar las diferentes categorías léxicas en el código fuente. A continuación se presentan los patrones utilizados en el analizador léxico, así como sus definiciones y extensiones regulares:

- **Definiciones:**
  - `DIGIT`: `[0-9]`
  - `LETTER`: `[a-zA-Z_]`
  - `IDENTIFIER`: `{LETTER}({LETTER}|{DIGIT})*`
  - `FLOAT_NUMBER`: `({DIGIT}+"."{DIGIT}*|{DIGIT}*"."{DIGIT}+)`
  - `INTEGER`: `{DIGIT}+`

- **Patrones Regulares:**
  - `IDENTIFIER`: `[a-zA-Z_][a-zA-Z0-9_]*`
  - `FLOAT_NUMBER`: `([0-9]+"."[0-9]*|[0-9]*"."[0-9]+)`
  - `INTEGER`: `[0-9]+`
  - `PLUS`: `\+`
  - `MINUS`: `\-`
  - `MULT`: `\*`
  - `DIV`: `\/`
  - `LT`: `<`
  - `GT`: `>`
  - `EQ`: `==`
  - `NEQ`: `!=`
  - `LEQ`: `<=`
  - `GEQ`: `>=`
  - `ASSIGN`: `=`
  - `SEMICOLON`: `;`
  - `LPAREN`: `\(`
  - `RPAREN`: `\)`
  - `LBRACE`: `\{`
  - `RBRACE`: `\}`
  - `LBRACKET`: `\[`
  - `RBRACKET`: `\]`
  - `COMMA`: `,`
  - `QUOTE`: `\"`
  - `CAST_FUNC`: `cast`
  - `BEGIN_PROGRAM`: `begin`
  - `END_PROGRAM`: `end`
  - `INT`: `int`
  - `FLOAT`: `float`
  - `IF`: `if`
  - `ELSE`: `else`
  - `FOR`: `for`
  - `WHILE`: `while`
  - `PRINT`: `print`
  - `READ`: `read`
  - `COMMENT`: `//.*`
  - `WHITESPACE`: `[ \t\r\n]+`

Estas definiciones y patrones permiten al analizador léxico identificar y clasificar correctamente cada componente del código fuente del lenguaje de programación de propósito específico, facilitando así su posterior análisis sintáctico y semántico.

## Referencias
[^1]: [GNU Flex manual](https://ftp.gnu.org/old-gnu/Manuals/flex-2.5.4/html_mono/flex.html)
[^2]: [Lexical Analysis With Flex, for Flex 2.6.2](https://westes.github.io/flex/manual/)
[^3]: [Compilers: Principles, Techniques, & Tools, 2nd ed](https://www.google.com.co/books/edition/Compilers/dIU_AQAAIAAJ?hl=en&gbpv=0&bsq=Compilers:%20Principles,%20Techniques,%20and%20Tools%202ed)


