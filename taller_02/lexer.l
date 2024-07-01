%{
#include "grammar.tab.h"
%}

DIGIT               [0-9]
LETTER              [a-zA-Z_]
IDENTIFIER          {LETTER}({LETTER}|{DIGIT})*
FLOAT_NUMBER        ({DIGIT}+"."{DIGIT}*|{DIGIT}*"."{DIGIT}+)
INTEGER             {DIGIT}+

%%

"//".*  {/* Ignore single-line comments */}

"begin"                { return BEGIN_PROGRAM; }
"end"                  { return END_PROGRAM; }
"int"                  { return INT; }
"float"                { return FLOAT; }
"if"                   { return IF; }
"else"                 { return ELSE; }
"for"                  { return FOR; }
"while"                { return WHILE; }
"print"                { return PRINT; }
"read"                 { return READ; }
"cast"                 { return CAST_FUNC; }

{IDENTIFIER}           { yylval.str = strdup(yytext); return IDENTIFIER; }
{FLOAT_NUMBER}         { yylval.num = atof(yytext); return NUMBER; }
{INTEGER}              { yylval.num = atoi(yytext); return NUMBER; }

"="                    { return ASSIGN; }
";"                    { return SEMICOLON; }
"("                    { return LPAREN; }
")"                    { return RPAREN; }
"{"                    { return LBRACE; }
"}"                    { return RBRACE; }
"["                    { return LBRACKET; }
"]"                    { return RBRACKET; }
"<"                    { return LT; }
">"                    { return GT; }
"+"                    { return PLUS; }
"-"                    { return MINUS; }
"*"                    { return MULT; }
"/"                    { return DIV; }
"=="                   { return EQ; }
"!="                   { return NEQ; }
"<="                   { return LEQ; }
">="                   { return GEQ; }
","                    { return COMMA; }
"\""                   { return QUOTE; }

[ \t\n]+               { /* skip whitespace */ }
.                      { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
