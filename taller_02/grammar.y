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
    int type; // 0 para int, 1 para float
    union { // Unión para almacenar el valor de la variable
        int ival;
        double fval;
    } value; 
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

%token <ival> INT_NUMBER
%token <fval> FLOAT_NUMBER
%token <sval> IDENTIFIER
%token INT FLOAT
%token ASSIGN
%token TBEGIN TEND 
%token PRINT
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET SEMICOLON

%type <fval> expression

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
    ;

expression:
    INT_NUMBER { $$ = $1; }
    | FLOAT_NUMBER { $$ = $1; }
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
    yyparse();
    return 0;
}
