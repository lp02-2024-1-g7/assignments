%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);    // Function to handle errors
int yylex(void);                // Function to get the next token  
extern FILE *yyin;              // Input file

typedef struct Var {
    char *name; // Variable name
    int type; // 0 for int, 1 for float
    union { // Union to store the value of the variable
        int ival;
        float fval;
    } value; 
} Var;

Var variables[100]; // Tenemos hasta 100 variables no mas
int var_count = 0;

// Function to get the index of a variable by its name
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
    float fval;
    char *sval;
} // Union to store the value of the token

%token <ival> NUMBER
%token <sval> IDENTIFIER
%token INT FLOAT
%token ASSIGN
%token TBEGIN TEND 
%token PRINT
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET SEMICOLON

%type <ival> expression

%%

program:
    TBEGIN LBRACE statement_list RBRACE { printf("Program executed successfully.\n"); }
    ;

statement_list:
    statement
    | statement_list statement
    ;

statement:
    // print(x)
    PRINT LPAREN expression RPAREN SEMICOLON { 
            printf("%d\n", $3); 
        }
    // int x;
    | INT IDENTIFIER SEMICOLON { 
            variables[var_count].name = $2; 
            variables[var_count].type = 0; // Inicializa la variable como tipo int en 0
            var_count++;
            printf("Variable tipo entero declarada %s\n", $2);
        }
    // float x;
    | FLOAT IDENTIFIER SEMICOLON { 
            variables[var_count].name = $2; 
            variables[var_count].type = 0; // Inicializa la variable como tipo float en 1
            var_count++;
            printf("Variable tipo flotante declarada %s\n", $2);
        }
    // x = 2;
    | IDENTIFIER ASSIGN expression SEMICOLON {
        int index = get_var_index($1);
        if (index == -1) {
            yyerror("La variable no existe");
        } else {
            if (variables[index].type == 0) {
                variables[index].value.ival = $3;
            } else {
                variables[index].value.fval = (float)$3;
            }
            printf("Valor asignado a la variable %s\n", $1);
        }
      }
    ;

expression:
    NUMBER { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "Could not open %s\n", argv[1]);
            return 1;
        }
        yyin = file;
    }
    yyparse();
    return 0;
}
