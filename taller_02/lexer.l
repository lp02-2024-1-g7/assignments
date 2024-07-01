%{
#include "grammar.tab.h"
%}

%%
"//".*  {/* Ignore single-line comments */}

"int"                   { return INT; }
"float"                 { return FLOAT; }
"if"                    { return IF; }
"else"                  { return ELSE; }
"for"                   { return FOR; }
"while"                 { return WHILE; }
"print"                 { return PRINT; }
"read"                  { return READ; }
"cast"                  { return CAST_FUNC; }  // Token para la función de casteo

[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return IDENTIFIER; }
[0-9]+"."[0-9]*         { yylval.num = atof(yytext); return NUMBER; } // Manejo de números en punto flotante
[0-9]*"."[0-9]+         { yylval.num = atof(yytext); return NUMBER; } // Manejo de números en punto flotante
[0-9]+                  { yylval.num = atoi(yytext); return NUMBER; } // Manejo de números enteros

"="                     { return ASSIGN; }
";"                     { return SEMICOLON; }
"("                     { return LPAREN; }
")"                     { return RPAREN; }
"{"                     { return LBRACE; }
"}"                     { return RBRACE; }
"["                     { return LBRACKET; }
"]"                     { return RBRACKET; }
"<"                     { return LT; }
">"                     { return GT; }
"+"                     { return PLUS; }
"-"                     { return MINUS; }
"*"                     { return MULT; }
"/"                     { return DIV; }
"=="                    { return EQ; }
"!="                    { return NEQ; }
"<="                    { return LEQ; }
">="                    { return GEQ; }
","                     { return COMMA; }
"\""                    { return QUOTE; }

[ \t\n]+                { /* skip whitespace */ }
.                       { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
