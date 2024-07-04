%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);
extern FILE *yyin;
%}

%union {
    int ival;
}

%token <ival> NUMBER
%token TBEGIN TEND PRINT
%token LPAREN RPAREN SEMICOLON

%type <ival> expression

%%
program:
    TBEGIN statement_list TEND { printf("Program executed successfully.\n"); }
    ;

statement_list:
    statement
    | statement_list statement
    ;

statement:
    PRINT LPAREN expression RPAREN SEMICOLON { printf("%d\n", $3); }
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
