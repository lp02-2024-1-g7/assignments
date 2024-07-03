%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex(void);
extern int yylineno;
extern char *yytext;

typedef union {
    char *str;
    double num;
} YYSTYPE;

#define YYSTYPE_IS_DECLARED 1
#define YYDEBUG 1
%}

%union {
    char *str;
    double num;
}

%token <str> IDENTIFIER
%token <num> NUMBER
%token INT FLOAT IF ELSE FOR WHILE PRINT READ CAST
%token ASSIGN SEMICOLON LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET
%token LT GT PLUS MINUS MULT DIV EQ NEQ LEQ GEQ COMMA QUOTE CAST_FUNC
%token BEGIN_PROGRAM END_PROGRAM

%type <num> expression
%type <str> assignment_statement
%type <str> loop_assignment_statement
%type <str> declaration_statement
%type <str> declarations
%type <str> statements
%type <str> statement
%type <str> if_statement
%type <str> while_statement
%type <str> for_statement
%type <str> print_statement
%type <str> program
%type <str> array_initialization
%type <str> array_elements
%type <str> numbers
%type <str> type
%type <str> array_declaration

%left LT GT LEQ GEQ EQ NEQ
%left PLUS MINUS
%left MULT DIV

%%

program:
    BEGIN_PROGRAM declarations statements END_PROGRAM { printf("Program parsed successfully.\n"); }
    ;

declarations:
    declaration_statement declarations
    | /* empty */ { $$ = strdup(""); }
    ;

declaration_statement:
    type IDENTIFIER SEMICOLON { $$ = strdup("variable declaration"); }
    | type IDENTIFIER ASSIGN expression SEMICOLON { $$ = strdup("variable assignment declaration"); }
    | type IDENTIFIER array_declaration SEMICOLON { $$ = strdup("array declaration"); }
    | type IDENTIFIER array_initialization SEMICOLON { $$ = strdup("array initialization"); }
    ;

type:
    INT { $$ = strdup("int"); }
    | FLOAT { $$ = strdup("float"); }
    ;

array_declaration:
    LBRACKET NUMBER RBRACKET { $$ = strdup("array declaration"); }
    | LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET { $$ = strdup("2D array declaration"); }
    ;

array_initialization:
    LBRACKET NUMBER RBRACKET ASSIGN LBRACE numbers RBRACE { $$ = strdup("array initialization"); }
    | LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET ASSIGN LBRACE array_elements RBRACE { $$ = strdup("2D array initialization"); }
    ;

array_elements:
    LBRACE numbers RBRACE { $$ = strdup("array elements"); }
    | array_elements COMMA LBRACE numbers RBRACE { char *temp = malloc(strlen($1) + strlen(", array elements") + 1); strcpy(temp, $1); strcat(temp, ", array elements"); $$ = temp; }
    ;

numbers:
    NUMBER { $$ = strdup("number"); }
    | numbers COMMA NUMBER { char *temp = malloc(strlen($1) + strlen(", number") + 1); strcpy(temp, $1); strcat(temp, ", number"); $$ = temp; }
    ;

statements:
    statement statements { char *temp = malloc(strlen($1) + strlen($2) + 1); strcpy(temp, $1); strcat(temp, $2); $$ = temp; }        
    | /* empty */ { $$ = strdup(""); }
    ;

statement:
    assignment_statement
    | if_statement
    | while_statement
    | for_statement
    | print_statement
    ;

assignment_statement:
    IDENTIFIER ASSIGN expression SEMICOLON { $$ = strdup("assignment statement"); }
    | IDENTIFIER LBRACKET expression RBRACKET ASSIGN expression SEMICOLON { $$ = strdup("array element assignment statement"); }     
    | IDENTIFIER LBRACKET expression RBRACKET LBRACKET expression RBRACKET ASSIGN expression SEMICOLON { $$ = strdup("2D array element assignment statement"); }
    ;

loop_assignment_statement:
    type IDENTIFIER ASSIGN expression { $$ = strdup("loop assignment statement"); }
    | IDENTIFIER ASSIGN expression { $$ = strdup("loop assignment statement"); }
    ;

if_statement:
    IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE { $$ = strdup("if-else statement"); }
    | IF LPAREN expression RPAREN LBRACE statements RBRACE { $$ = strdup("if statement"); }
    ;

while_statement:
    WHILE LPAREN expression RPAREN LBRACE statements RBRACE { $$ = strdup("while statement"); }
    ;

for_statement:
    FOR LPAREN loop_assignment_statement SEMICOLON expression SEMICOLON loop_assignment_statement RPAREN LBRACE statements RBRACE { $$ = strdup("for statement"); }
    ;

print_statement:
    PRINT LPAREN expression RPAREN SEMICOLON { $$ = strdup("print statement"); }
    ;

expression:
    NUMBER { $$ = $1; }
    | IDENTIFIER { $$ = 0; /* Placeholder, you'll need to fetch the value */ }
    | expression PLUS expression { $$ = $1 + $3; }
    | expression MINUS expression { $$ = $1 - $3; }
    | expression MULT expression { $$ = $1 * $3; }
    | expression DIV expression { $$ = $1 / $3; }
    | LPAREN expression RPAREN { $$ = $2; }
    | expression LT expression { $$ = $1 < $3; }
    | expression GT expression { $$ = $1 > $3; }
    | expression EQ expression { $$ = $1 == $3; }
    | expression NEQ expression { $$ = $1 != $3; }
    | expression LEQ expression { $$ = $1 <= $3; }
    | expression GEQ expression { $$ = $1 >= $3; }
    | CAST_FUNC LPAREN type COMMA expression RPAREN { $$ = $5; }  // Type casting
    | IDENTIFIER LBRACKET expression RBRACKET { $$ = 0; }  // Array access
    | IDENTIFIER LBRACKET expression RBRACKET LBRACKET expression RBRACKET { $$ = 0; }  // 2D Array access
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error at line %d: %s (text: %s)\n", yylineno, s, yytext);
    exit(1);  // Parar la ejecución en caso de error
}

int main(void) {
    yydebug = 0;
    return yyparse();
}
