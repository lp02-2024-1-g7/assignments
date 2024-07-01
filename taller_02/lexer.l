%{
#include "parser.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

digit      [0-9]
letter     [a-zA-Z_]
identifier {letter}({letter}|{digit})*
number     {digit}+(\.{digit}+)?
whitespace [ \t\n\r]+

%%
"int"       { return INT; }
"float"     { return FLOAT; }
"if"        { return IF; }
"else"      { return ELSE; }
"for"       { return FOR; }
"while"     { return WHILE; }
"print"     { return PRINT; }
"read"      { return READ; }

"="         { return ASSIGN; }
";"         { return SEMICOLON; }
"("         { return LPAREN; }
")"         { return RPAREN; }
"{"         { return LBRACE; }
"}"         { return RBRACE; }
"<"         { return LT; }
">"         { return GT; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"*"         { return MULT; }
"/"         { return DIV; }
"=="        { return EQ; }
"!="        { return NEQ; }
"<="        { return LEQ; }
">="        { return GEQ; }
"\""        { return QUOTE; }
"["         { return LBRACKET; }
"]"         { return RBRACKET; }
","         { return COMMA; }

{identifier}   { yylval.str = strdup(yytext); return IDENTIFIER; }
{number}       { yylval.num = atof(yytext); return NUMBER; }
{whitespace}   { /* Ignorar espacios en blanco */ }
"//".*         { /* Ignorar comentarios de una línea */ }
.              { printf("Unexpected character: %c\n", *yytext); exit(1); }

%%

int yywrap(void) {
    return 1;
}
