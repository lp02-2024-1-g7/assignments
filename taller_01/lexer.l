%{
#include <stdio.h>
%}

/*** Definición de patrones utilizando expresiones regulares ***/
digit      [0-9]
letter     [a-zA-Z_]
identifier {letter}({letter}|{digit})*
number     {digit}+(\.{digit}+)?
whitespace [ \t\n\r]

/*** Reglas de sustitución ***/
%%
"int"       { printf("INT\n"); }          /* Tipo de dato entero */
"float"     { printf("FLOAT\n"); }        /* Tipo de dato flotante */
"if"        { printf("IF\n"); }           /* Estructura de selección */
"else"      { printf("ELSE\n"); }         /* Parte de la estructura de selección */
"for"       { printf("FOR\n"); }          /* Estructura de iteración */
"while"     { printf("WHILE\n"); }        /* Estructura de iteración */
"print"     { printf("PRINT\n"); }        /* Función de impresión */
"read"      { printf("READ\n"); }         /* Función de lectura */

"="         { printf("ASSIGN\n"); }       /* Operador de asignación */
";"         { printf("SEMICOLON\n"); }    /* Punto y coma */
"("         { printf("LPAREN\n"); }       /* Paréntesis izquierdo */
")"         { printf("RPAREN\n"); }       /* Paréntesis derecho */
"{"         { printf("LBRACE\n"); }       /* Llave izquierda */
"}"         { printf("RBRACE\n"); }       /* Llave derecha */
"<"         { printf("LT\n"); }           /* Operador menor que */
">"         { printf("GT\n"); }           /* Operador mayor que */
"+"         { printf("PLUS\n"); }         /* Operador de suma */
"-"         { printf("MINUS\n"); }        /* Operador de resta */
"*"         { printf("MULT\n"); }         /* Operador de multiplicación */
"/"         { printf("DIV\n"); }          /* Operador de división */
"=="        { printf("EQ\n"); }           /* Operador igual a */
"!="        { printf("NEQ\n"); }          /* Operador diferente a */
"<="        { printf("LEQ\n"); }          /* Operador menor o igual que */
">="        { printf("GEQ\n"); }          /* Operador mayor o igual que */
"\""        { printf("QUOTE\n"); }        /* Comillas dobles */
"["         { printf("LBRACKET\n"); }     /* Corchete izquierdo */
"]"         { printf("RBRACKET\n"); }     /* Corchete derecho */
","         { printf("COMMA\n"); }        /* Coma */

{identifier}   { printf("IDENTIFIER(%s)\n", yytext); }
{number}       { printf("NUMBER(%s)\n", yytext); }
{whitespace}   { /* Ignorar espacios en blanco */ }
"//".*         { /* Ignorar comentarios de una línea */ }
.              { printf("Unexpected character: %c\n", *yytext); }

%%
/*** Función de cierre ***/
int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("fopen");
            return 1;
        }
        yyin = file;
    }
    yylex();
    return 0;
}
