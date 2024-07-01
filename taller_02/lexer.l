%{
#include "grammar.tab.h"
%}

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

[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return IDENTIFIER; }
[0-9]+"."[0-9]*        { yylval.num = atof(yytext); return NUMBER; }
[0-9]*"."[0-9]+        { yylval.num = atof(yytext); return NUMBER; }
[0-9]+                 { yylval.num = atoi(yytext); return NUMBER; }

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
