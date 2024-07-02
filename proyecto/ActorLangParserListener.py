# Generated from ActorLangParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ActorLangParser import ActorLangParser
else:
    from ActorLangParser import ActorLangParser

# This class defines a complete listener for a parse tree produced by ActorLangParser.
class ActorLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by ActorLangParser#program.
    def enterProgram(self, ctx:ActorLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by ActorLangParser#program.
    def exitProgram(self, ctx:ActorLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by ActorLangParser#actorDefinition.
    def enterActorDefinition(self, ctx:ActorLangParser.ActorDefinitionContext):
        pass

    # Exit a parse tree produced by ActorLangParser#actorDefinition.
    def exitActorDefinition(self, ctx:ActorLangParser.ActorDefinitionContext):
        pass


    # Enter a parse tree produced by ActorLangParser#actorBody.
    def enterActorBody(self, ctx:ActorLangParser.ActorBodyContext):
        pass

    # Exit a parse tree produced by ActorLangParser#actorBody.
    def exitActorBody(self, ctx:ActorLangParser.ActorBodyContext):
        pass


    # Enter a parse tree produced by ActorLangParser#portDeclaration.
    def enterPortDeclaration(self, ctx:ActorLangParser.PortDeclarationContext):
        pass

    # Exit a parse tree produced by ActorLangParser#portDeclaration.
    def exitPortDeclaration(self, ctx:ActorLangParser.PortDeclarationContext):
        pass


    # Enter a parse tree produced by ActorLangParser#messageHandler.
    def enterMessageHandler(self, ctx:ActorLangParser.MessageHandlerContext):
        pass

    # Exit a parse tree produced by ActorLangParser#messageHandler.
    def exitMessageHandler(self, ctx:ActorLangParser.MessageHandlerContext):
        pass


    # Enter a parse tree produced by ActorLangParser#statements.
    def enterStatements(self, ctx:ActorLangParser.StatementsContext):
        pass

    # Exit a parse tree produced by ActorLangParser#statements.
    def exitStatements(self, ctx:ActorLangParser.StatementsContext):
        pass


    # Enter a parse tree produced by ActorLangParser#statement.
    def enterStatement(self, ctx:ActorLangParser.StatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#statement.
    def exitStatement(self, ctx:ActorLangParser.StatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#sendStatement.
    def enterSendStatement(self, ctx:ActorLangParser.SendStatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#sendStatement.
    def exitSendStatement(self, ctx:ActorLangParser.SendStatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#receiveStatement.
    def enterReceiveStatement(self, ctx:ActorLangParser.ReceiveStatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#receiveStatement.
    def exitReceiveStatement(self, ctx:ActorLangParser.ReceiveStatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#startStatement.
    def enterStartStatement(self, ctx:ActorLangParser.StartStatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#startStatement.
    def exitStartStatement(self, ctx:ActorLangParser.StartStatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:ActorLangParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:ActorLangParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#printStatement.
    def enterPrintStatement(self, ctx:ActorLangParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by ActorLangParser#printStatement.
    def exitPrintStatement(self, ctx:ActorLangParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by ActorLangParser#expression.
    def enterExpression(self, ctx:ActorLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ActorLangParser#expression.
    def exitExpression(self, ctx:ActorLangParser.ExpressionContext):
        pass



del ActorLangParser