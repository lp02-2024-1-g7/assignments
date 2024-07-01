# Marco Teórico Taller 01: Análisis Léxico LEX

## Analizador Léxico
El analizador léxico, también conocido como lexer o scanner, es el componente del compilador que se encarga de leer el código fuente y dividirlo en unidades léxicas llamadas tokens. Estos tokens son secuencias de caracteres que representan símbolos significativos del lenguaje, como palabras clave, identificadores, operadores y delimitadores. El analizador léxico facilita el trabajo del analizador sintáctico al simplificar la estructura del código fuente.

## Analizador Léxico LEX
LEX es una herramienta de generación de analizadores léxicos que se utiliza para construir programas que reconocen patrones en un flujo de entrada y generan tokens como salida. LEX permite definir reglas de coincidencia basadas en expresiones regulares y acciones asociadas a cada regla. Estas acciones se ejecutan cuando se encuentra un patrón coincidente, permitiendo realizar tareas como la generación de tokens, el conteo de líneas o la manipulación de variables. Contiene la siguiente estructura básica:

```lex
declaraciones
%%
reglas
%%
código
```

## Lenguaje de Programación de Propósito Específico
Un lenguaje de programación de propósito específico (DSL, por sus siglas en inglés) está diseñado para resolver problemas específicos en un dominio particular, a diferencia de los lenguajes de propósito general que se utilizan para una amplia gama de aplicaciones. Los DSLs ofrecen una sintaxis y semántica optimizadas para tareas específicas, lo que permite a los usuarios expresar soluciones de manera más eficiente y efectiva dentro de ese dominio.

## El Problema de Dos Vías de Clasificación
El problema de dos vías de clasificación es un modelo estadístico utilizado para analizar datos que pueden clasificarse en dos dimensiones, comúnmente denominadas bloques y tratamientos. Este modelo se utiliza para evaluar los efectos de diferentes tratamientos en distintos bloques, permitiendo el análisis de la variabilidad dentro y entre los bloques.

## Paradigma Imperativo
El paradigma imperativo es un estilo de programación en el que el programador especifica explícitamente los pasos que debe seguir la computadora para alcanzar un objetivo. Esto incluye la definición de secuencias de instrucciones, estructuras de control como bucles y condicionales, y la manipulación de variables y estructuras de datos.

## Estructuras de Secuencia, Selección e Iteración
- **Secuencia**: Representa la ejecución lineal de instrucciones, una tras otra.
- **Selección**: Permite la ejecución de diferentes bloques de código en función de una condición (por ejemplo, instrucciones `if-else`).
- **Iteración**: Permite la repetición de un bloque de código mientras una condición sea verdadera (por ejemplo, bucles `for` y `while`).

## Vocabulario
El vocabulario de un lenguaje de programación incluye todas las palabras clave, identificadores, literales y operadores que son reconocidos y utilizados en el lenguaje. Definir el vocabulario es crucial para el desarrollo del analizador léxico, ya que este debe ser capaz de identificar y categorizar cada elemento del código fuente.

## Categorías Léxicas
Las categorías léxicas son las clases en las que se agrupan los tokens del lenguaje, tales como palabras clave, identificadores, operadores, literales y delimitadores. Cada token se clasifica en una categoría léxica específica basada en su función y significado dentro del lenguaje.

## Patrones
En el contexto del análisis léxico, los patrones son expresiones regulares que describen la estructura de los diferentes tokens. Los patrones se utilizan para definir cómo se debe reconocer cada tipo de token en el código fuente.

## Expresiones Regulares, Definiciones y Extensiones Regulares
- **Expresiones Regulares**: Son secuencias de caracteres que definen un patrón de búsqueda. Se utilizan en los analizadores léxicos para identificar y extraer tokens del código fuente.
- **Definiciones Regulares**: Son nombres asignados a expresiones regulares, lo que permite su reutilización y simplificación en la especificación de patrones.
- **Extensiones Regulares**: Son ampliaciones de las expresiones regulares básicas que proporcionan mayor potencia y flexibilidad en la definición de patrones léxicos.

## Análisis Sintáctico
A diferencia del análisis léxico, que se centra en la estructura de los tokens individuales, el análisis sintáctico se ocupa de la estructura jerárquica y gramatical del código fuente. El analizador sintáctico verifica si las secuencias de tokens forman una estructura gramaticalmente válida según las reglas del lenguaje.

## Gramática Libre de Contexto
Una gramática libre de contexto es una descripción formal de la estructura sintáctica de un lenguaje de programación que se basa en reglas de producción. Estas reglas definen cómo se pueden combinar los símbolos no terminales y terminales del lenguaje para formar expresiones válidas.

# Notación BNF
La notación de Backus-Naur, también conocida por sus denominaciones inglesas Backus-Naur form (BNF), Backus-Naur formalism o Backus normal form, es un metalenguaje usado para expresar gramáticas libres de contexto: es decir, una manera formal de describir lenguajes formales.

# Notación E-BNF
La notación extendida de Backus-Naur (EBNF) es una extensión de la notación de Backus-Naur (BNF) que incluye algunas características adicionales para hacer las gramáticas más fáciles de leer y escribir. EBNF agrega constructores como repeticiones, opciones y agrupaciones para simplificar la especificación de gramáticas.

## Pruebas Tipo Friedman
Las "pruebas tipo Friedman" se refieren a un conjunto de pruebas estadísticas no paramétricas utilizadas para detectar diferencias en tratamientos en experimentos bloqueados. Específicamente, la prueba de Friedman se usa para comparar más de dos tratamientos en muestras relacionadas. Esta prueba es útil cuando no se cumplen los supuestos de normalidad necesarios para pruebas paramétricas como el ANOVA de medidas repetidas.

### Detalle de la Prueba de Friedman
La prueba de Friedman es una alternativa no paramétrica al ANOVA de medidas repetidas. Se utiliza para evaluar si hay diferencias estadísticamente significativas entre las medianas de tres o más grupos emparejados o dependientes. Es particularmente útil en experimentos donde el mismo conjunto de sujetos está expuesto a diferentes tratamientos.

- **Proceso**:
  1. **Clasificación de Datos**: Para cada bloque (o sujeto), se clasifica cada tratamiento.
  2. **Cálculo de Rangos**: Se asignan rangos a los tratamientos dentro de cada bloque.
  3. **Cálculo del Estadístico de Prueba**: Se utiliza la siguiente fórmula para calcular el estadístico de prueba de Friedman:
     \[
     \chi^2_F = \frac{12}{nt(k+1)} \sum_j R_j^2 - 3n(k+1)
     \]
     Donde:
     - \( n \) es el número de bloques.
     - \( k \) es el número de tratamientos.
     - \( R_j \) es el rango sumado de cada tratamiento.

- **Hipótesis**:
  - **Nula (H0)**: No hay diferencias en las medianas de los tratamientos.
  - **Alternativa (H1)**: Al menos un tratamiento difiere en su mediana.

- **Conclusión**: Si el estadístico calculado es mayor que el valor crítico de \(\chi^2\) con \(k-1\) grados de libertad, se rechaza la hipótesis nula, concluyendo que hay diferencias significativas entre los tratamientos.

## Teoría de Rachas
La teoría de rachas es un enfoque estadístico utilizado para analizar la secuencia de datos y detectar patrones o estructuras significativas en los mismos. Las rachas son secuencias de valores idénticos en una cadena de datos, y el análisis de rachas se centra en la identificación y conteo de estas secuencias para extraer información relevante.

## Problema de Dos Vías de Clasificación Utilizando Rachas
El problema de dos vías de clasificación utilizando rachas es un enfoque estadístico para analizar datos estructurados en una matriz de dos dimensiones, donde los datos se clasifican en bloques y tratamientos. El análisis implica la identificación y conteo de rachas en los datos, lo que proporciona información sobre la variabilidad y la estructura de los datos en el modelo.

## Conceptos Claves de Teoría de Rachas

### Alfabeto de Categorías
Un conjunto finito de símbolos, cada uno representando un grupo o categoría específica. Por ejemplo, en un alfabeto \(\Sigma = \{a, e, u\}\), cada símbolo pertenece a una categoría distinta.

### Racha
Una sucesión de uno o más símbolos idénticos en una cadena, seguidos o precedidos por símbolos diferentes o por ningún símbolo. Ejemplo: En la cadena "eeeeauuuuuuu", hay tres rachas: "eeee", "a" y "uuuuuuuu".

### Categorías
Particiones de un conjunto en subconjuntos mutuamente excluyentes y exhaustivos. Cada subconjunto se denomina categoría.

### Multicotomización
Proceso de clasificar un conjunto de valores en múltiples categorías. Por ejemplo, clasificando números en positivos y negativos.

### Estructura de la Cadena Multicotomizada
La cadena resultante de la multicotomización que presenta una estructura específica basada en la posición, longitud y clase de los símbolos de las rachas.

### Función Contadora y Número de Rachas
Función que cuenta el número de rachas en una cadena multicotomizada hasta un determinado símbolo.

### Modelo de Dos Vías de Clasificación
Modelo estadístico que incluye parámetros como efectos de tratamientos y bloques, y una matriz de datos que representa estos efectos.

### Operaciones Punto
Operaciones matemáticas definidas sobre el modelo de dos vías de clasificación, como el total de datos del modelo, total de datos por bloque y por tratamiento, y conjunto de datos del modelo.

### Multicotomización del Modelo de Dos Vías
Algoritmo para aplicar la multicotomización en el modelo de dos vías, clasificando los datos y calculando las rachas en cada celda de la matriz de datos.

### Operaciones Punto sobre el Modelo de Rachas
Operaciones específicas sobre las rachas en el modelo de dos vías, como el número y promedio de rachas por celda, bloque, tratamiento y el modelo completo.

### Funciones sobre la Información del Modelo
Construcción de funciones basadas en las variables y parámetros relacionados con las rachas para analizar y procesar la información del modelo.

Este marco teórico proporciona una base sólida para el desarrollo del análisis léxico y el entendimiento de los conceptos estadísticos y computacionales necesarios para el Taller 01.

## Operaciones Específicas del Problema de Dos Vías de Clasificación Utilizando Rachas

### Operaciones Punto
Las operaciones punto son aquellas que se realizan en puntos específicos de la matriz de datos del modelo de dos vías de clasificación. Estas operaciones se utilizan para calcular diversas métricas y estadísticas a partir de los datos.

1. **Total de Datos del Modelo (\(T_{mod}\))**:
   - **Descripción**: Suma de todos los datos presentes en la matriz de datos del modelo.
   - **Fórmula**: \( T_{mod} = \sum_{i=1}^{b} \sum_{j=1}^{t} x_{ij} \)
   - **Donde**:
     - \( b \): Número de bloques
     - \( t \): Número de tratamientos
     - \( x_{ij} \): Valor del dato en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

2. **Total de Datos por Bloque (\(T_{bi}\))**:
   - **Descripción**: Suma de los datos de un bloque específico \(i\).
   - **Fórmula**: \( T_{bi} = \sum_{j=1}^{t} x_{ij} \)
   - **Donde**:
     - \( t \): Número de tratamientos
     - \( x_{ij} \): Valor del dato en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

3. **Total de Datos por Tratamiento (\(T_{tj}\))**:
   - **

Descripción**: Suma de los datos de un tratamiento específico \(j\).
   - **Fórmula**: \( T_{tj} = \sum_{i=1}^{b} x_{ij} \)
   - **Donde**:
     - \( b \): Número de bloques
     - \( x_{ij} \): Valor del dato en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

4. **Conjunto de Datos del Modelo (\(S_{mod}\))**:
   - **Descripción**: Conjunto de todos los datos presentes en la matriz del modelo.
   - **Fórmula**: \( S_{mod} = \{ x_{ij} \ | \ 1 \leq i \leq b, \ 1 \leq j \leq t \} \)
   - **Donde**:
     - \( b \): Número de bloques
     - \( t \): Número de tratamientos
     - \( x_{ij} \): Valor del dato en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

### Multicotomización del Modelo de Dos Vías
La multicotomización es el proceso de clasificar los datos del modelo en múltiples categorías y analizar las rachas resultantes.

1. **Número de Rachas por Celda (\(R_{ij}\))**:
   - **Descripción**: Cuenta de las rachas en una celda específica \((i,j)\).
   - **Fórmula**: \( R_{ij} = \text{número de rachas en } x_{ij} \)

2. **Número de Rachas por Bloque (\(R_{bi}\))**:
   - **Descripción**: Suma del número de rachas en todas las celdas de un bloque específico \(i\).
   - **Fórmula**: \( R_{bi} = \sum_{j=1}^{t} R_{ij} \)
   - **Donde**:
     - \( t \): Número de tratamientos
     - \( R_{ij} \): Número de rachas en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

3. **Número de Rachas por Tratamiento (\(R_{tj}\))**:
   - **Descripción**: Suma del número de rachas en todas las celdas de un tratamiento específico \(j\).
   - **Fórmula**: \( R_{tj} = \sum_{i=1}^{b} R_{ij} \)
   - **Donde**:
     - \( b \): Número de bloques
     - \( R_{ij} \): Número de rachas en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

4. **Número Total de Rachas en el Modelo (\(R_{mod}\))**:
   - **Descripción**: Suma del número de rachas en todas las celdas del modelo.
   - **Fórmula**: \( R_{mod} = \sum_{i=1}^{b} \sum_{j=1}^{t} R_{ij} \)
   - **Donde**:
     - \( b \): Número de bloques
     - \( t \): Número de tratamientos
     - \( R_{ij} \): Número de rachas en la celda correspondiente al bloque \(i\) y tratamiento \(j\)

5. **Promedio de Rachas por Celda (\(P_{ij}\))**:
   - **Descripción**: Promedio de rachas en una celda específica \((i,j)\).
   - **Fórmula**: \( P_{ij} = \frac{R_{ij}}{N_{ij}} \)
   - **Donde**:
     - \( R_{ij} \): Número de rachas en la celda correspondiente al bloque \(i\) y tratamiento \(j\)
     - \( N_{ij} \): Número total de datos en la celda \((i,j)\)

6. **Promedio de Rachas por Bloque (\(P_{bi}\))**:
   - **Descripción**: Promedio de rachas en todas las celdas de un bloque específico \(i\).
   - **Fórmula**: \( P_{bi} = \frac{R_{bi}}{T_{bi}} \)
   - **Donde**:
     - \( R_{bi} \): Número de rachas en el bloque \(i\)
     - \( T_{bi} \): Total de datos en el bloque \(i\)

7. **Promedio de Rachas por Tratamiento (\(P_{tj}\))**:
   - **Descripción**: Promedio de rachas en todas las celdas de un tratamiento específico \(j\).
   - **Fórmula**: \( P_{tj} = \frac{R_{tj}}{T_{tj}} \)
   - **Donde**:
     - \( R_{tj} \): Número de rachas en el tratamiento \(j\)
     - \( T_{tj} \): Total de datos en el tratamiento \(j\)

8. **Promedio Total de Rachas en el Modelo (\(P_{mod}\))**:
   - **Descripción**: Promedio de rachas en todas las celdas del modelo.
   - **Fórmula**: \( P_{mod} = \frac{R_{mod}}{T_{mod}} \)
   - **Donde**:
     - \( R_{mod} \): Número total de rachas en el modelo
     - \( T_{mod} \): Total de datos en el modelo

### Funciones sobre la Información del Modelo
Estas funciones construyen y analizan la información del modelo basándose en las rachas y otros parámetros.

1. **Función de Conteo de Rachas (\(F_{cr}\))**:
   - **Descripción**: Calcula el número de rachas en una secuencia de datos.
   - **Fórmula**: \( F_{cr}(x) = \sum_{i=1}^{n-1} [x_i \neq x_{i+1}] + 1 \)
   - **Donde**:
     - \( x \): Secuencia de datos
     - \( n \): Longitud de la secuencia
     - \([x_i \neq x_{i+1}]\): Indicador de cambio entre \(x_i\) y \(x_{i+1}\)

2. **Función de Longitud de Rachas (\(F_{lr}\))**:
   - **Descripción**: Calcula la longitud promedio de las rachas en una secuencia de datos.
   - **Fórmula**: \( F_{lr}(x) = \frac{n}{F_{cr}(x)} \)
   - **Donde**:
     - \( x \): Secuencia de datos
     - \( n \): Longitud de la secuencia
     - \( F_{cr}(x) \): Número de rachas en la secuencia

3. **Función de Variabilidad de Rachas (\(F_{vr}\))**:
   - **Descripción**: Calcula la variabilidad en la longitud de las rachas en una secuencia de datos.
   - **Fórmula**: \( F_{vr}(x) = \frac{\sum_{i=1}^{F_{cr}(x)} (l_i - F_{lr}(x))^2}{F_{cr}(x) - 1} \)
   - **Donde**:
     - \( x \): Secuencia de datos
     - \( l_i \): Longitud de la \(i\)-ésima racha
     - \( F_{cr}(x) \): Número de rachas en la secuencia
     - \( F_{lr}(x) \): Longitud promedio de las rachas en la secuencia