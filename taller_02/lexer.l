%{
#include "grammar.tab.h"
#include <stdio.h>

void yyerror(const char *s);
%}

DIGIT               [0-9]
LETTER              [a-zA-Z_]
IDENTIFIER          {LETTER}({LETTER}|{DIGIT})*
FLOAT               ({DIGIT}+"."{DIGIT}*|{DIGIT}*"."{DIGIT}+)
INTEGER             {DIGIT}+

%%
"begin"                 { return TBEGIN; }
"end"                   { return TEND; }
"int"                   { return INT; }
"float"                 { return FLOAT; }
"print"                 { return PRINT; }
"log"                   { return LOG; }

{IDENTIFIER}            { yylval.sval = strdup(yytext); return IDENTIFIER; }
{FLOAT}                 { yylval.fval = atof(yytext); return FLOAT_NUMBER; }
{INTEGER}               { yylval.ival = atoi(yytext); return INT_NUMBER; }

"("                     { return LPAREN; }
")"                     { return RPAREN; }
"{"                     { return LBRACE; }
"}"                     { return RBRACE; }
"["                     { return LBRACKET; }
"]"                     { return RBRACKET; }
"="                     { return ASSIGN; }
";"                     { return SEMICOLON; }
[ \t\n\r]+              ;  // Ignorar espacios en blanco y saltos de línea: LF `\n` y CRLF `\r\n`
.                       { yyerror("Unexpected character"); }
%%
