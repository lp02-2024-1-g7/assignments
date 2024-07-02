## Marco Teórico

### Introducción a los Sistemas de Actores

El modelo de actores es un paradigma de programación que trata a "actores" como la unidad fundamental de computación. Un actor es una entidad que puede recibir y enviar mensajes, crear nuevos actores y decidir cómo responder a los mensajes recibidos. Este modelo es especialmente útil en sistemas distribuidos y concurrentes debido a su simplicidad y robustez en el manejo de concurrencia y comunicación.

### Modelo de Actores en Sistemas Distribuidos

En sistemas distribuidos, el modelo de actores proporciona una forma efectiva de gestionar la concurrencia y la comunicación entre diferentes nodos del sistema. Cada actor puede considerarse como un proceso independiente que se comunica con otros actores mediante el envío de mensajes. Esta comunicación es asíncrona, lo que significa que el emisor no necesita esperar una respuesta inmediata. Los actores son inherentemente seguros frente a condiciones de carrera porque no comparten estado; en lugar de ello, los actores se comunican exclusivamente mediante mensajes.

Las principales características del modelo de actores en sistemas distribuidos son:

- **Encapsulamiento de Estado**: Cada actor mantiene su propio estado privado, que no puede ser accedido directamente por otros actores. La modificación del estado se realiza en respuesta a los mensajes recibidos.
- **Comunicación Asíncrona**: Los actores se comunican enviando mensajes asíncronos. Esto permite que los actores sigan ejecutándose sin esperar a que los mensajes sean procesados.
- **Creación Dinámica de Actores**: Los actores pueden crear nuevos actores. Esto permite la construcción dinámica y flexible de sistemas complejos.
- **Tolerancia a Fallos**: Debido a su naturaleza independiente y encapsulada, los actores pueden ser reiniciados o reemplazados sin afectar al sistema en su conjunto.

### ANTLR: Una Herramienta para la Generación de Analizadores

ANTLR (Another Tool for Language Recognition) es una poderosa herramienta que se utiliza para generar analizadores léxicos y sintácticos a partir de una gramática formal. Es ampliamente utilizada para construir compiladores, intérpretes y otros procesadores de lenguaje. ANTLR permite definir la gramática de un lenguaje y genera automáticamente el código necesario para analizar y procesar programas escritos en ese lenguaje.

#### Analizador Léxico

El analizador léxico es la primera fase del análisis de un lenguaje de programación. Su tarea principal es convertir una secuencia de caracteres de entrada en una secuencia de tokens, que son unidades atómicas del lenguaje como palabras clave, identificadores, operadores y literales. En ANTLR, se define una gramática léxica utilizando un conjunto de reglas que describen los patrones de los tokens.

Ejemplo de gramática léxica en ANTLR:
```antlr
lexer grammar ActorLangLexer;

ACTOR               : 'actor' ;
SEND                : 'send' ;
RECEIVE             : 'receive' ;
START               : 'start' ;
ON                  : 'on' ;
TO                  : 'to' ;
PORT                : 'port' ;
PRINT               : 'print' ;
ARROW               : '->' ;
LBRACE              : '{' ;
RBRACE              : '}' ;
LPAREN              : '(' ;
RPAREN              : ')' ;
SEMICOLON           : ';' ;
ASSIGN              : '=' ;
COMMA               : ',' ;
IDENTIFIER          : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING_LITERAL      : '"' ~["]* '"' ;
INT_LITERAL         : [0-9]+ ;
WS                  : [ \t\r\n]+ -> skip ;
```

#### Analizador Sintáctico

El analizador sintáctico recibe la secuencia de tokens del analizador léxico y construye una estructura jerárquica llamada árbol sintáctico o árbol de análisis. Esta estructura representa la gramática del lenguaje y permite identificar la estructura lógica del programa. La gramática sintáctica en ANTLR se define utilizando reglas que describen cómo se combinan los tokens para formar construcciones del lenguaje.

Ejemplo de gramática sintáctica en ANTLR:
```antlr
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
```

### Listeners y Visitors en ANTLR

ANTLR genera dos tipos de interfaces para recorrer el árbol sintáctico: listeners y visitors. Ambos métodos permiten realizar acciones específicas mientras se recorre el árbol, pero tienen diferencias en su enfoque y uso.

#### Listeners

Los listeners en ANTLR siguen un patrón de diseño conocido como "visitor pattern". ANTLR genera automáticamente una clase base con métodos que se llaman cuando se entra y sale de cada regla de la gramática. Puedes extender esta clase base y anular los métodos para realizar acciones específicas durante el recorrido del árbol.

Ejemplo de un listener:
```python
from ActorLangParserListener import ActorLangParserListener
from actor import Actor, Message

class MyActorLangListener(ActorLangParserListener):
    def __init__(self):
        self.actors = {}  # Store created actors
        self.actions = []  # Store actions to be executed

    def enterActorDefinition(self, ctx):
        actor_id = ctx.IDENTIFIER().getText()
        port = ctx.actorBody().portDeclaration().INT_LITERAL().getText()
        self.actors[actor_id] = Actor(actor_id, port)

    def exitSendStatement(self, ctx):
        sender_name = ctx.IDENTIFIER().getText()
        recipient_name = ctx.STRING_LITERAL(1).getText().strip('"')
        message = ctx.STRING_LITERAL(0).getText().strip('"')
        recipient_address = ctx.STRING_LITERAL(1).getText().strip('"')
        port = ctx.INT_LITERAL().getText()  # Port number

        action = ("send", sender_name, recipient_name, message, recipient_address, port)
        self.actions.append(action)

    def exitPrintStatement(self, ctx):
        message = ctx.STRING_LITERAL().getText().strip('"')
        print(message)

    def execute_actions(self):
        for action in self.actions:
            if action[0] == "send":
                _, sender_name, recipient_name, message, recipient_address, port = action
                sender = self.actors[sender_name]
                sender.send(f"{recipient_address}:{port}", Message(message))
```

#### Visitors

Los visitors son otra forma de recorrer el árbol sintáctico. En lugar de seguir el patrón de entrada y salida de listeners, los visitors definen un método de visita para cada regla de la gramática. Esto permite un control más explícito sobre el recorrido y las acciones a realizar.

Ejemplo de un visitor:
```python
from ActorLangParserVisitor import ActorLangParserVisitor
from actor import Actor, Message

class MyActorLangVisitor(ActorLangParserVisitor):
    def __init__(self):
        self.actors = {}  # Store created actors
        self.actions = []  # Store actions to be executed

    def visitActorDefinition(self, ctx):
        actor_id = ctx.IDENTIFIER().getText()
        port = ctx.actorBody().portDeclaration().INT_LITERAL().getText()
        self.actors[actor_id] = Actor(actor_id, port)
        return self.visitChildren(ctx)

    def visitSendStatement(self, ctx):
        sender_name = ctx.IDENTIFIER().getText()
        recipient_name = ctx.STRING_LITERAL(1).getText().strip('"')
        message = ctx.STRING_LITERAL(0).getText().strip('"')
        recipient_address = ctx.STRING_LITERAL(1).getText().strip('"')
        port = ctx.INT_LITERAL().getText()  # Port number

        action = ("send", sender_name, recipient_name, message, recipient_address, port)
        self.actions.append(action)
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx):
        message = ctx.STRING_LITERAL().getText().strip('"')
        print(message)
        return self.visitChildren(ctx)

    def execute_actions(self):
        for action in self.actions:
            if action[0] == "send":
                _, sender_name, recipient_name, message, recipient_address, port = action
                sender = self.actors[sender_name]
                sender.send(f"{recipient_address}:{port}", Message(message))
```

### Árboles de Parseo y Walkers

El árbol de parseo (parse tree) es una representación estructurada del código fuente de acuerdo con la gramática del lenguaje. Los walkers (recorridos) permiten navegar por este árbol para realizar diversas tareas, como la interpretación o la compilación del código. ANTLR proporciona una clase `ParseTreeWalker` que facilita el recorrido del árbol utilizando listeners.

Ejemplo de uso de un walker:
```python
def main(file_path):
    input_stream = FileStream(file_path)
    lexer = ActorLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ActorLangParser(stream)
    tree = parser.program()



    listener = MyActorLangListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.execute_actions()
```
