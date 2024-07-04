%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);    // Función para manejar errores
int yylex(void);                // Función para obtener el siguiente token
extern FILE *yyin;              // Archivo de entrada

// Estructura para almacenar las variables
typedef struct Var {
    char *name; // Nombre de la variable
    int type; // 0 para int, 1 para float, 2 para arreglo de int, 3 para arreglo de float, 4 para arreglo bidimensional de int, 5 para arreglo bidimensional de float
    union { // Unión para almacenar el valor de la variable
        int ival;
        double fval;
        int *iarr;    // Puntero para arreglo de int
        double *farr; // Puntero para arreglo de float
        int **iarr2d; // Puntero para arreglo bidimensional de int
        double **farr2d; // Puntero para arreglo bidimensional de float
    } value;
    int size1; // Primer tamaño del arreglo (si aplica)
    int size2; // Segundo tamaño del arreglo (si aplica)
} Var;

Var variables[100]; // Hasta 100 variables
int var_count = 0;  // Contador de variables

// Función para obtener el índice de una variable por su nombre
int get_var_index(char *name) {
    for (int i = 0; i < var_count; i++) {
        if (strcmp(variables[i].name, name) == 0) { // strcmp devuelve 0 si las cadenas son iguales
            return i;
        }
    }
    return -1;
}

%}

%union {
    int ival;
    double fval;
    char *sval;
} // Unión para almacenar el valor del token

// %token sirve para definir los tokens. %token <tipo> token1 token2 ... tokenN
%token <ival> INT_NUMBER 
%token <fval> FLOAT_NUMBER
%token <sval> IDENTIFIER
%token INT FLOAT
%token ASSIGN
%token TBEGIN TEND
%token PRINT
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET SEMICOLON COMMA
%token LT GT LE GE EQ NE
%token AND OR

// %type sirve para definir el tipo de retorno de las reglas. %type <tipo> regla1 regla2 ... reglaN
%type <fval> expression

// %left, %right, %nonassoc sirve para definir la precedencia de los operadores
%left '+' '-'
%left '*' '/'
%left LT GT LE GE EQ NE
%left AND OR

// Los operadores como '+' no son tokens, pero se pueden usar en las reglas

%%

program:
    TBEGIN LBRACE statement_list RBRACE { printf("Programa ejecutado exitosamente.\n"); }
    ;

statement_list:
    statement
    | statement_list statement
    ;

statement:
    // print(x)
    PRINT LPAREN expression RPAREN SEMICOLON {
            if ($3 == (int)$3) {
                printf("%d\n", (int)$3);
            } else {
                printf("%f\n", $3);
            }
        }
    // int x;
    | INT IDENTIFIER SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 0; // Inicializa la variable como tipo int
            variables[var_count].value.ival = 0; // Valor por defecto
            var_count++;
            printf("Variable tipo int declarada: %s\n", $2);
        }
    // float x;
    | FLOAT IDENTIFIER SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 1; // Inicializa la variable como tipo float
            variables[var_count].value.fval = 0.0; // Valor por defecto
            var_count++;
            printf("Variable tipo float declarada: %s\n", $2);
        }
    // int arr[10];
    | INT IDENTIFIER LBRACKET INT_NUMBER RBRACKET SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 2; // Inicializa la variable como arreglo de int
            variables[var_count].size1 = $4; // Tamaño del arreglo
            variables[var_count].value.iarr = (int *)malloc($4 * sizeof(int)); // Asigna memoria para el arreglo
            for (int i = 0; i < $4; i++) {
                variables[var_count].value.iarr[i] = 0; // Inicializa los elementos a 0
            }
            var_count++;
            printf("Arreglo tipo int declarado: %s[%d]\n", $2, $4);
        }
    // float arr[10];
    | FLOAT IDENTIFIER LBRACKET INT_NUMBER RBRACKET SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 3; // Inicializa la variable como arreglo de float
            variables[var_count].size1 = $4; // Tamaño del arreglo
            variables[var_count].value.farr = (double *)malloc($4 * sizeof(double)); // Asigna memoria para el arreglo
            for (int i = 0; i < $4; i++) {
                variables[var_count].value.farr[i] = 0.0; // Inicializa los elementos a 0.0
            }
            var_count++;
            printf("Arreglo tipo float declarado: %s[%d]\n", $2, $4);
        }
    // int arr[5][10];
    | INT IDENTIFIER LBRACKET INT_NUMBER RBRACKET LBRACKET INT_NUMBER RBRACKET SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 4; // Inicializa la variable como arreglo bidimensional de int
            variables[var_count].size1 = $4; // Primer tamaño del arreglo
            variables[var_count].size2 = $7; // Segundo tamaño del arreglo
            variables[var_count].value.iarr2d = (int **)malloc($4 * sizeof(int *)); // Asigna memoria para el arreglo
            for (int i = 0; i < $4; i++) {
                variables[var_count].value.iarr2d[i] = (int *)malloc($7 * sizeof(int)); // Asigna memoria para cada fila
                for (int j = 0; j < $7; j++) {
                    variables[var_count].value.iarr2d[i][j] = 0; // Inicializa los elementos a 0
                }
            }
            var_count++;
            printf("Arreglo bidimensional tipo int declarado: %s[%d][%d]\n", $2, $4, $7);
        }
    // float arr[5][10];
    | FLOAT IDENTIFIER LBRACKET INT_NUMBER RBRACKET LBRACKET INT_NUMBER RBRACKET SEMICOLON {
            variables[var_count].name = $2;
            variables[var_count].type = 5; // Inicializa la variable como arreglo bidimensional de float
            variables[var_count].size1 = $4; // Primer tamaño del arreglo
            variables[var_count].size2 = $7; // Segundo tamaño del arreglo
            variables[var_count].value.farr2d = (double **)malloc($4 * sizeof(double *)); // Asigna memoria para el arreglo
            for (int i = 0; i < $4; i++) {
                variables[var_count].value.farr2d[i] = (double *)malloc($7 * sizeof(double)); // Asigna memoria para cada fila
                for (int j = 0; j < $7; j++) {
                    variables[var_count].value.farr2d[i][j] = 0.0; // Inicializa los elementos a 0.0
                }
            }
            var_count++;
            printf("Arreglo bidimensional tipo float declarado: %s[%d][%d]\n", $2, $4, $7);
        }
    // x = 2;
    | IDENTIFIER ASSIGN expression SEMICOLON {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
        } else {
            if (variables[index].type == 0) {
                variables[index].value.ival = (int)$3;
            } else {
                variables[index].value.fval = $3;
            }
            printf("Valor asignado a la variable %s\n", $1);
        }
      }
    // arr[2] = 5;
    | IDENTIFIER LBRACKET INT_NUMBER RBRACKET ASSIGN expression SEMICOLON {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
        } else {
            if (variables[index].type == 2) { // Arreglo de int
                if ($3 < 0 || $3 >= variables[index].size1) {
                    yyerror("Índice fuera de rango");
                } else {
                    variables[index].value.iarr[$3] = (int)$6;
                    printf("Valor %d asignado a %s[%d]\n", (int)$6, $1, $3);
                }
            } else if (variables[index].type == 3) { // Arreglo de float
                if ($3 < 0 || $3 >= variables[index].size1) {
                    yyerror("Índice fuera de rango");
                } else {
                    variables[index].value.farr[$3] = $6;
                    printf("Valor %f asignado a %s[%d]\n", $6, $1, $3);
                }
            } else {
                yyerror("La variable no es un arreglo");
            }
        }
      }
    // arr[2][3] = 5;
    | IDENTIFIER LBRACKET INT_NUMBER RBRACKET LBRACKET INT_NUMBER RBRACKET ASSIGN expression SEMICOLON {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
        } else {
            if (variables[index].type == 4) { // Arreglo bidimensional de int
                if ($3 < 0 || $3 >= variables[index].size1 || $6 < 0 || $6 >= variables[index].size2) {
                    yyerror("Índice fuera de rango");
                } else {
                    variables[index].value.iarr2d[$3][$6] = (int)$9;
                    printf("Valor %d asignado a %s[%d][%d]\n", (int)$9, $1, $3, $6);
                }
            } else if (variables[index].type == 5) { // Arreglo bidimensional de float
                if ($3 < 0 || $3 >= variables[index].size1 || $6 < 0 || $6 >= variables[index].size2) {
                    yyerror("Índice fuera de rango");
                } else {
                    variables[index].value.farr2d[$3][$6] = $9;
                    printf("Valor %f asignado a %s[%d][%d]\n", $9, $1, $3, $6);
                }
            } else {
                yyerror("La variable no es un arreglo bidimensional");
            }
        }
      }
    ;

expression:
    // 666
    INT_NUMBER { $$ = $1; }
    // 3.14
    | FLOAT_NUMBER { $$ = $1; }
    // foo
    | IDENTIFIER {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
            $$ = 0; // Valor por defecto en caso de error
        } else {
            if (variables[index].type == 0) {
                $$ = variables[index].value.ival;
            } else {
                $$ = variables[index].value.fval;
            }
        }
      }
    // arr[2]
    | IDENTIFIER LBRACKET INT_NUMBER RBRACKET {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
            $$ = 0; // Valor por defecto en caso de error
        } else {
            if (variables[index].type == 2) { // Arreglo de int
                if ($3 < 0 || $3 >= variables[index].size1) {
                    yyerror("Índice fuera de rango");
                    $$ = 0;
                } else {
                    $$ = variables[index].value.iarr[$3];
                }
            } else if (variables[index].type == 3) { // Arreglo de float
                if ($3 < 0 || $3 >= variables[index].size1) {
                    yyerror("Índice fuera de rango");
                    $$ = 0.0;
                } else {
                    $$ = variables[index].value.farr[$3];
                }
            } else {
                yyerror("La variable no es un arreglo");
                $$ = 0;
            }
        }
      }
    // arr[2][3]
    | IDENTIFIER LBRACKET INT_NUMBER RBRACKET LBRACKET INT_NUMBER RBRACKET {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no está declarada");
            $$ = 0; // Valor por defecto en caso de error
        } else {
            if (variables[index].type == 4) { // Arreglo bidimensional de int
                if ($3 < 0 || $3 >= variables[index].size1 || $6 < 0 || $6 >= variables[index].size2) {
                    yyerror("Índice fuera de rango");
                    $$ = 0;
                } else {
                    $$ = variables[index].value.iarr2d[$3][$6];
                }
            } else if (variables[index].type == 5) { // Arreglo bidimensional de float
                if ($3 < 0 || $3 >= variables[index].size1 || $6 < 0 || $6 >= variables[index].size2) {
                    yyerror("Índice fuera de rango");
                    $$ = 0.0;
                } else {
                    $$ = variables[index].value.farr2d[$3][$6];
                }
            } else {
                yyerror("La variable no es un arreglo bidimensional");
                $$ = 0;
            }
        }
      }
    // 1 + 2
    | expression '+' expression {
        $$ = $1 + $3;
      }
    // 3 - 2
    | expression '-' expression {
        $$ = $1 - $3;
      }
    // 2 * 3
    | expression '*' expression {
        $$ = $1 * $3;
      }
    // 6 / 3
    | expression '/' expression {
        if ($3 == 0) { // Evita la división por cero
            yyerror("División por cero");
            $$ = 0;
        } else {
            $$ = $1 / $3;
        }
      }
    // expresiones lógicas
    // 1 < 2
    | expression LT expression {
        $$ = $1 < $3;
      }
    // 2 > 1
    | expression GT expression {
        $$ = $1 > $3;
      }
    // 1 <= 2
    | expression LE expression {
        $$ = $1 <= $3;
      }
    // 2 >= 1
    | expression GE expression {
        $$ = $1 >= $3;
      }
    // 1 == 1
    | expression EQ expression {
        $$ = $1 == $3;
      }
    // 1 != 2
    | expression NE expression {
        $$ = $1 != $3;
      }
    // 1 && 0
    | expression AND expression {
        $$ = $1 && $3;
      }
    // 1 || 0
    | expression OR expression {
        $$ = $1 || $3;
      }
    // (1 + 2)
    | '(' expression ')' {
        $$ = $2;
      }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "No se pudo abrir %s\n", argv[1]);
            return 1;
        }
        yyin = file;
    }
    yyparse(); // Llama al parser
    return 0; // Termina el programa
}
