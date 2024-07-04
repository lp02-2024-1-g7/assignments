from ActorLangParser import ActorLangParser
from ActorLangLexer import ActorLangLexer
from antlr4 import *

class ActorLangVisitor(ParseTreeVisitor):
    def visitProgram(self, ctx):
        # Visitar cada definición de actor
        for actorDefinition in ctx.actorDefinition():
            self.visit(actorDefinition)

    def visitActorDefinition(self, ctx):
        actorId = ctx.IDENTIFIER().getText()
        # Iniciar actor aquí
        print(f"Defining actor {actorId}")

    def visitSendStatement(self, ctx):
        message = ctx.STRING_LITERAL().getText()
        recipient = ctx.IDENTIFIER().getText()
        # Lógica para enviar mensaje
        print(f"Sending message {message} to {recipient}")

    # Implementar otros métodos visitantes según sea necesario