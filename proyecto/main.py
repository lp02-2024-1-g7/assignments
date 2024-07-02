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
