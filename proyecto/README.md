# Proyecto de Lenguajes para Sistema de Actores 

## Introductión
Este proyecto implementa un sistema de actores básico en Python, donde los actores se comunican entre sí utilizando sockets TCP. Cada actor puede ser configurado a través de un archivo de entrada que describe su comportamiento. El sistema de actores se basa en un analizador léxico y sintáctico implementado con ANTLR y un runtime de Python.

Mas información en [marcoteorico.md](marcoteorico.md)

## Requisitos
- JDK 8 o superior
- JAR de ANTLR 4.11.1 (incluido en el repositorio)
- Runtime ATLR para Python

### Instalación
Java Development Kit (JDK) es necesario para compilar y ejecutar el código Java. Puedes instalarlo en Ubuntu usando el siguiente comando:
```bash
sudo apt update
sudo apt install default-jdk
java -version
```

Para verificar que ANTLR está instalado correctamente, ejecuta el siguiente comando:
```bash
java -jar antlr-4.11.1-complete.jar
```

Para crear un entorno virtual de python, ejecuta el siguiente comando:
```bash
python3 -m venv venv
```

Para activar el entorno virtual de python, ejecuta el siguiente comando:
```bash
source venv/bin/activate
```

Runtime de ANTLR versión 4.11.1 para Python se puede instalar usando pip:
```bash
python3 -v
pip install antlr4-python3-runtime==4.11.1
pip -h
```

Verificar la versión de ANTLR instalada:
```bash
pip show antlr4-python3-runtime
```

Verifica que ANTLR está instalado correctamente:
```bash
python3
>>> import antlr4
>>> exit()
```

## Analisador Léxico
Tal y como se realizpó en el taller 01, se implementó un analizador léxico con FLEX. En este caso, se implementará un analizador léxico con ANTLR.

Debe tener definido un archivo de gramática que describa el lenguaje de programación que se desea analizar. En este caso, se usará el archivo `ActorLangLexer.g4`.
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

## Analisador Sintático
Similar al analizador léxico, se implementará un analizador sintáctico tal como se hizo en el taller 02, pero esta vez también con ANTLR.

Debe tener definido un archivo de gramática que describa el lenguaje de programación que se desea analizar. En este caso, se usará el archivo `ActorLangParser.g4`.

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

## Compilación
Para compilar el analizador léxico y sintáctico, se debe ejecutar el siguiente comando:

```bash
java -jar antlr-4.11.1-complete.jar -Dlanguage=Python3  ActorLangLexer.g4 ActorLangParser.g4
```

Donde `antlr-4.11.1-complete.jar` es el archivo JAR de ANTLR, `ActorLangLexer.g4` es el archivo de la gramática del analizador léxic, `ActorLangParser.g4` es el archivo de la gramática del analizador sintáctico, `-Dlanguage=Python3` indica que se generará el código en Python, `-listener` indica que se generará un listener, y `-visitor` indica que se generará un visitor.

Esto creará los siguientes archivos:

- `ActorLangLexer.interp`: archivo de interpretación del analizador léxico.
- `ActorLangLexer.py`: archivo de implementación del analizador léxico.
- `ActorLangLexer.tokens`: archivo de tokens del analizador léxico.

- `ActorLangParser.interp`: archivo de interpretación del analizador sintáctico.
- `ActorLangParser.py`: archivo de implementación del analizador sintáctico.
- `ActorLangParser.tokens`: archivo de tokens del analizador sintáctico.

- `ActorLangParserListener.py`: sirve para escuchar eventos generados por el analizador sintáctico.
- `ActorLangVisitor.py`: sirve para visitar nodos generados por el analizador sintáctico.

## Python runtime
Las clases Actor y Message se encuentran en el archivo `actor.py`. 
```python
# proyecto\actor.py
import socket
import threading
import time

class Actor:
    def __init__(self, id, port):
        self.id = id
        self.port = port
        self.inbox = []  # Incoming messages

    def send(self, recipient, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # extract the recipient address and port
                host, port = recipient.split(':')
                s.connect((host, int(port)))
                s.sendall(message.content.encode())  # Convert the message content to bytes
        except Exception as e:
            print(f"Error sending message from Actor {self.id}: {e}")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', int(self.port)))
            s.listen()
            print(f"Actor {self.id} listening on port {self.port}")
            while True:
                conn, addr = s.accept()
                threading.Thread(target=self.handle_connection, args=(conn,)).start()

    def handle_connection(self, conn):
        with conn:
            data = conn.recv(1024)
            message = Message(data.decode('utf-8'))
            self.inbox.append(message)
            print(f"Actor {self.id} received: {message}")

class Message:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content

```

Este código define una clase `Actor` que representa un actor en el sistema. Cada actor tiene un identificador único, un puerto en el que escucha para recibir mensajes y una bandeja de entrada para almacenar los mensajes recibidos. La clase `Actor` también tiene un método `send` para enviar mensajes a otros actores y un método `start` para iniciar el actor y escuchar en su puerto.

## ANTLR Listener

```python
# proyecto\listener.py
from ActorLangParserListener import ActorLangParserListener
from actor import Actor, Message
from ActorLangParser import ActorLangParser

class MyActorLangListener(ActorLangParserListener):
    def __init__(self):
        self.actors = {}  # Store created actors
        self.actions = []  # Store actions to be executed

    def enterActorDefinition(self, ctx):
        """
        This method is called when entering an actor definition in the grammar.

        Parameters:
            ctx (antlr4.ParserRuleContext): The context object representing the actor definition.

        Returns:
            None

        Side Effects:
            - Updates the `actors` dictionary with a new Actor object.

        """
        actor_id = ctx.IDENTIFIER().getText()
        port = ctx.actorBody().portDeclaration().INT_LITERAL().getText()
        self.actors[actor_id] = Actor(actor_id, port)

    def exitSendStatement(self, ctx):
        """
        Process the exit event of the 'sendStatement' rule.

        Args:
            ctx: The context object representing the 'sendStatement' rule.

        Returns:
            None

        Raises:
            None
        """
        sender_name = ctx.IDENTIFIER().getText()
        recipient_name = ctx.STRING_LITERAL(1).getText().strip('"')
        message = ctx.STRING_LITERAL(0).getText().strip('"')
        recipient_address = ctx.STRING_LITERAL(1).getText().strip('"')
        port = ctx.INT_LITERAL().getText()  # Port number

        action = ("send", sender_name, recipient_name, message, recipient_address, port)
        self.actions.append(action)

    def exitStartStatement(self, ctx):
        """
        Starts the actor with the given identifier.

        Parameters:
        - ctx: The context object containing the actor identifier.

        Returns:
        None
        """
        actor = ctx.IDENTIFIER().getText()
        port = ctx.STRING_LITERAL().getText().strip('"')
        action = ("start", actor, port)
        self.actions.append(action)
        

    def exitPrintStatement(self, ctx):
        """
        Prints the message extracted from the given context.

        Parameters:
        - ctx: The context object containing the string literal.

        Returns:
        None
        """
        message = ctx.STRING_LITERAL().getText().strip('"')
        print(message)

    def execute_actions(self):
        for action in self.actions:
            if action[0] == "send":
                _action, sender_name, recipient_name, message, recipient_address, port = action
                sender = self.actors[sender_name]
                sender.send(f"{recipient_address}:{port}", Message(message))
            elif action[0] == "start":
                port = action[2]
                actor = self.actors[action[1]]
                actor.start()
```

Este código define una clase `MyActorLangListener` que hereda de `ActorLangParserListener` y anula algunos de los métodos generados por ANTLR. En particular, anulamos los métodos `enterActorDefinition`, `exitSendStatement` y `exitPrintStatement` para manejar la creación de actores, el envío de mensajes y la impresión de mensajes, respectivamente.

## Main Program
```python
# proyecto\main.py
from antlr4 import *
from ActorLangLexer import ActorLangLexer
from ActorLangParser import ActorLangParser
from listener import MyActorLangListener
import sys

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

if __name__ == '__main__':
    # Obtener el archivo de entrada desde la línea de comandos
    file_path = sys.argv[1] # .\proyecto\input01.txt
    main(file_path)
```

Este código define una función `main` que toma la ruta de un archivo de entrada como argumento y crea un analizador léxico y sintáctico para analizar el archivo. Luego, crea una instancia de `MyActorLangListener` y un `ParseTreeWalker` para recorrer el árbol de análisis y ejecutar el código correspondiente. 

## Ejecución
Primero definimos un archivo de entrada `input01.txt` con el siguiente contenido:
```plaintext
actor Actor1 {
    port = 9090;
    on "Hello, Actor1!" -> {
        start("9090", Actor1);
        print("Message received in Actor1.");
    }
}
```

Luego, ejecutamos el programa principal `main.py`:
```bash
python main.py input01.txt
```

Segundo definimos un archivo de entrada `input02.txt` con el siguiente contenido:
```plaintext
actor Actor2 {
    port = 9091;
    on "init" -> {
        send("Hello, Actor1!", Actor2) to "127.0.0.1" port 9090;
        print("Message sent from Actor1.");
    }
}
```

Luego, ejecutamos el programa principal `main.py`:
```bash
python main.py input02.txt
```