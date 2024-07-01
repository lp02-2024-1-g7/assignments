#include <stdio.h>

int main() {
    extern int yylex();
    yylex();
    return 0;
}
