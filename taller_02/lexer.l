%{
#include "grammar.tab.h"
#include <stdio.h>

void yyerror(const char *s);
%}

%%
"begin"         { return TBEGIN; }
"end"           { return TEND; }
"print"         { return PRINT; }
[0-9]+          { yylval.ival = atoi(yytext); return NUMBER; }
"("             { return LPAREN; }
")"             { return RPAREN; }
";"             { return SEMICOLON; }
[ \t\n\r]+      ;  // Ignorar espacios en blanco y saltos de línea: LF `\n` y CRLF `\r\n`
.               { yyerror("Unexpected character"); }
%%
