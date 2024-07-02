parser grammar ActorLangParser;

options { tokenVocab=ActorLangLexer; }

program             : actorDefinition+ ;
actorDefinition     : ACTOR IDENTIFIER LBRACE actorBody RBRACE ;
actorBody           : portDeclaration messageHandler* ;
portDeclaration     : PORT ASSIGN INT_LITERAL SEMICOLON ;
messageHandler      : ON STRING_LITERAL ARROW LBRACE statements RBRACE ;
statements          : statement* ;
statement           : sendStatement | receiveStatement | startStatement | assignmentStatement | printStatement ;
sendStatement       : SEND LPAREN STRING_LITERAL COMMA IDENTIFIER RPAREN TO STRING_LITERAL PORT INT_LITERAL SEMICOLON ;
receiveStatement    : RECEIVE LPAREN RPAREN SEMICOLON ;
startStatement      : START LPAREN STRING_LITERAL COMMA IDENTIFIER RPAREN SEMICOLON ;
assignmentStatement : IDENTIFIER ASSIGN expression SEMICOLON ;
printStatement      : PRINT LPAREN STRING_LITERAL RPAREN SEMICOLON ;
expression          : STRING_LITERAL | IDENTIFIER | INT_LITERAL ;
