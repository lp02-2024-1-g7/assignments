%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern FILE *yyin;

%}

DIGIT               [0-9]
LETTER              [a-zA-Z_]
IDENTIFIER          {LETTER}({LETTER}|{DIGIT})*
FLOAT_NUMBER        ({DIGIT}+"."{DIGIT}*|{DIGIT}*"."{DIGIT}+)
INTEGER             {DIGIT}+

%%

"//".*               {/* Ignore single-line comments */}
"begin"              { printf("BEGIN_PROGRAM\n"); }
"end"                { printf("END_PROGRAM\n"); }
"int"                { printf("INT\n"); }
"float"              { printf("FLOAT\n"); }
"if"                 { printf("IF\n"); }
"else"               { printf("ELSE\n"); }
"for"                { printf("FOR\n"); }
"while"              { printf("WHILE\n"); }
"print"              { printf("PRINT\n"); }
"read"               { printf("READ\n"); }
"cast"               { printf("CAST_FUNC\n"); }

{IDENTIFIER}         { printf("IDENTIFIER(%s)\n", yytext); }
{FLOAT_NUMBER}       { printf("NUMBER(%s)\n", yytext); }
{INTEGER}            { printf("NUMBER(%s)\n", yytext); }

"="                  { printf("ASSIGN\n"); }
";"                  { printf("SEMICOLON\n"); }
"("                  { printf("LPAREN\n"); }
")"                  { printf("RPAREN\n"); }
"{"                  { printf("LBRACE\n"); }
"}"                  { printf("RBRACE\n"); }
"["                  { printf("LBRACKET\n"); }
"]"                  { printf("RBRACKET\n"); }
"<"                  { printf("LT\n"); }
">"                  { printf("GT\n"); }
"+"                  { printf("PLUS\n"); }
"-"                  { printf("MINUS\n"); }
"*"                  { printf("MULT\n"); }
"/"                  { printf("DIV\n"); }
"=="                 { printf("EQ\n"); }
"!="                 { printf("NEQ\n"); }
"<="                 { printf("LEQ\n"); }
">="                 { printf("GEQ\n"); }
","                  { printf("COMMA\n"); }
"\""                 { printf("QUOTE\n"); }

[ \t\r\n]+           { /* skip whitespace */ }
.                    { printf("Unexpected character: %s\n", yytext); }

%%

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
