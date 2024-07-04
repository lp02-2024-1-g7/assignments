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
","                     { return COMMA; }

"+"                     { return '+'; } // Operador de suma
"-"                     { return '-'; } // Operador de resta
"*"                     { return '*'; } // Operador de multiplicación
"/"                     { return '/'; } // Operador de división

"<"                     { return LT; } // Operador de comparación menor que
">"                     { return GT; } // Operador de comparación mayor que
"<="                    { return LE; } // Operador de comparación menor o igual que
">="                    { return GE; } // Operador de comparación mayor o igual que
"=="                    { return EQ; } // Operador de comparación igual que
"!="                    { return NE; } // Operador de comparación diferente que

"&&"                    { return AND; } // Operador lógico AND
"||"                    { return OR; } // Operador lógico OR

[ \t\n\r]+              ;  // Ignorar espacios en blanco y saltos de línea: LF `\n` y CRLF `\r\n`
.                       { yyerror("Unexpected character"); }
%%
