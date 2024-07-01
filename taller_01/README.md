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
    int a = 5;
    float b = 3.14;

    // Definición de una matriz 3x3
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Variables auxiliares
    int i, j;

    // Calcular el total de datos del modelo
    int T_mod = 0;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            T_mod += matrix[i][j];
        }
    }
    print(T_mod);

    // Calcular el total de datos por bloque
    int T_bi[3];
    for (i = 0; i < 3; i++) {
        T_bi[i] = 0;
        for (j = 0; j < 3; j++) {
            T_bi[i] += matrix[i][j];
        }
        print(T_bi[i]);
    }

    // Calcular el total de datos por tratamiento
    int T_tj[3];
    for (j = 0; j < 3; j++) {
        T_tj[j] = 0;
        for (i = 0; i < 3; i++) {
            T_tj[j] += matrix[i][j];
        }
        print(T_tj[j]);
    }

    // Calcular el número de rachas por celda (simplificado para el ejemplo)
    int R_ij[3][3] = {
        {1, 1, 1},
        {1, 1, 1},
        {1, 1, 1}
    };
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            print(R_ij[i][j]);
        }
    }

    // Calcular el número total de rachas en el modelo
    int R_mod = 0;
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            R_mod += R_ij[i][j];
        }
    }
    print(R_mod);

    // Calcular el promedio de rachas por celda (simplificado para el ejemplo)
    float P_ij[3][3];
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            P_ij[i][j] = (float)R_ij[i][j] / (float)matrix[i][j];
            print(P_ij[i][j]);
        }
    }
   ```

2. **Ejecutar el analizador léxico**:
   Ejecuta el analizador léxico con el archivo de entrada `input.txt`.

   ```sh
   ./lexer < input.txt
   ```

## Explicación del Propósito del Programa y su Funcionamiento

El propósito de este programa es analizar un archivo de entrada en el que se define un lenguaje de programación de propósito específico diseñado para resolver el problema de dos vías de clasificación utilizando conceptos de rachas. El analizador léxico se encarga de dividir el código fuente en tokens que representan las diferentes partes del lenguaje, facilitando su posterior análisis y procesamiento.

### Operaciones Específicas

- **Calcular el total de datos del modelo (`T_mod`)**: Suma de todos los valores en la matriz `matrix`.
- **Calcular el total de datos por bloque (`T_bi`)**: Suma de los valores en cada fila de la matriz `matrix`.
- **Calcular el total de datos por tratamiento (`T_tj`)**: Suma de los valores en cada columna de la matriz `matrix`.
- **Calcular el número de rachas por celda (`R_ij`)**: En este ejemplo simplificado, se asume que cada celda tiene una racha.
- **Calcular el número total de rachas en el modelo (`R_mod`)**: Suma del número de rachas en todas las celdas.
- **Calcular el promedio de rachas por celda (`P_ij`)**: División del número de rachas en cada celda por el valor en la celda correspondiente de la matriz.

Estos cálculos ilustran cómo se pueden aplicar los conceptos de rachas al análisis de datos estructurados en matrices, permitiendo extraer métricas y estadísticas útiles para el problema de dos vías de clasificación.

## Referencias
[^1]: [GNU Flex manual](https://ftp.gnu.org/old-gnu/Manuals/flex-2.5.4/html_mono/flex.html)
[^2]: [Lexical Analysis With Flex, for Flex 2.6.2](https://westes.github.io/flex/manual/)
[^3]: [Compilers: Principles, Techniques, & Tools, 2nd ed](https://www.google.com.co/books/edition/Compilers/dIU_AQAAIAAJ?hl=en&gbpv=0&bsq=Compilers:%20Principles,%20Techniques,%20and%20Tools%202ed)


