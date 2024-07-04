# Generated from ActorLangParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,108,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        5,5,5,58,8,5,10,5,12,5,61,9,5,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,1,1,0,17,19,101,0,27,1,0,0,0,2,31,1,0,0,0,4,37,
        1,0,0,0,6,44,1,0,0,0,8,49,1,0,0,0,10,59,1,0,0,0,12,67,1,0,0,0,14,
        69,1,0,0,0,16,81,1,0,0,0,18,86,1,0,0,0,20,94,1,0,0,0,22,99,1,0,0,
        0,24,105,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,
        1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,32,5,1,0,0,32,33,5,17,0,0,
        33,34,5,10,0,0,34,35,3,4,2,0,35,36,5,11,0,0,36,3,1,0,0,0,37,41,3,
        6,3,0,38,40,3,8,4,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,
        42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,45,5,7,0,0,45,46,5,15,0,
        0,46,47,5,19,0,0,47,48,5,14,0,0,48,7,1,0,0,0,49,50,5,5,0,0,50,51,
        5,18,0,0,51,52,5,9,0,0,52,53,5,10,0,0,53,54,3,10,5,0,54,55,5,11,
        0,0,55,9,1,0,0,0,56,58,3,12,6,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,
        1,0,0,0,59,60,1,0,0,0,60,11,1,0,0,0,61,59,1,0,0,0,62,68,3,14,7,0,
        63,68,3,16,8,0,64,68,3,18,9,0,65,68,3,20,10,0,66,68,3,22,11,0,67,
        62,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,
        0,68,13,1,0,0,0,69,70,5,2,0,0,70,71,5,12,0,0,71,72,5,18,0,0,72,73,
        5,16,0,0,73,74,5,17,0,0,74,75,5,13,0,0,75,76,5,6,0,0,76,77,5,18,
        0,0,77,78,5,7,0,0,78,79,5,19,0,0,79,80,5,14,0,0,80,15,1,0,0,0,81,
        82,5,3,0,0,82,83,5,12,0,0,83,84,5,13,0,0,84,85,5,14,0,0,85,17,1,
        0,0,0,86,87,5,4,0,0,87,88,5,12,0,0,88,89,5,18,0,0,89,90,5,16,0,0,
        90,91,5,17,0,0,91,92,5,13,0,0,92,93,5,14,0,0,93,19,1,0,0,0,94,95,
        5,17,0,0,95,96,5,15,0,0,96,97,3,24,12,0,97,98,5,14,0,0,98,21,1,0,
        0,0,99,100,5,8,0,0,100,101,5,12,0,0,101,102,5,18,0,0,102,103,5,13,
        0,0,103,104,5,14,0,0,104,23,1,0,0,0,105,106,7,0,0,0,106,25,1,0,0,
        0,4,29,41,59,67
    ]

class ActorLangParser ( Parser ):

    grammarFileName = "ActorLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'actor'", "'send'", "'receive'", "'start'", 
                     "'on'", "'to'", "'port'", "'print'", "'->'", "'{'", 
                     "'}'", "'('", "')'", "';'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "ACTOR", "SEND", "RECEIVE", "START", 
                      "ON", "TO", "PORT", "PRINT", "ARROW", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "SEMICOLON", "ASSIGN", "COMMA", 
                      "IDENTIFIER", "STRING_LITERAL", "INT_LITERAL", "WS" ]

    RULE_program = 0
    RULE_actorDefinition = 1
    RULE_actorBody = 2
    RULE_portDeclaration = 3
    RULE_messageHandler = 4
    RULE_statements = 5
    RULE_statement = 6
    RULE_sendStatement = 7
    RULE_receiveStatement = 8
    RULE_startStatement = 9
    RULE_assignmentStatement = 10
    RULE_printStatement = 11
    RULE_expression = 12

    ruleNames =  [ "program", "actorDefinition", "actorBody", "portDeclaration", 
                   "messageHandler", "statements", "statement", "sendStatement", 
                   "receiveStatement", "startStatement", "assignmentStatement", 
                   "printStatement", "expression" ]

    EOF = Token.EOF
    ACTOR=1
    SEND=2
    RECEIVE=3
    START=4
    ON=5
    TO=6
    PORT=7
    PRINT=8
    ARROW=9
    LBRACE=10
    RBRACE=11
    LPAREN=12
    RPAREN=13
    SEMICOLON=14
    ASSIGN=15
    COMMA=16
    IDENTIFIER=17
    STRING_LITERAL=18
    INT_LITERAL=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actorDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ActorLangParser.ActorDefinitionContext)
            else:
                return self.getTypedRuleContext(ActorLangParser.ActorDefinitionContext,i)


        def getRuleIndex(self):
            return ActorLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ActorLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.actorDefinition()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActorDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTOR(self):
            return self.getToken(ActorLangParser.ACTOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ActorLangParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(ActorLangParser.LBRACE, 0)

        def actorBody(self):
            return self.getTypedRuleContext(ActorLangParser.ActorBodyContext,0)


        def RBRACE(self):
            return self.getToken(ActorLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_actorDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActorDefinition" ):
                listener.enterActorDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActorDefinition" ):
                listener.exitActorDefinition(self)




    def actorDefinition(self):

        localctx = ActorLangParser.ActorDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_actorDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ActorLangParser.ACTOR)
            self.state = 32
            self.match(ActorLangParser.IDENTIFIER)
            self.state = 33
            self.match(ActorLangParser.LBRACE)
            self.state = 34
            self.actorBody()
            self.state = 35
            self.match(ActorLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActorBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def portDeclaration(self):
            return self.getTypedRuleContext(ActorLangParser.PortDeclarationContext,0)


        def messageHandler(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ActorLangParser.MessageHandlerContext)
            else:
                return self.getTypedRuleContext(ActorLangParser.MessageHandlerContext,i)


        def getRuleIndex(self):
            return ActorLangParser.RULE_actorBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActorBody" ):
                listener.enterActorBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActorBody" ):
                listener.exitActorBody(self)




    def actorBody(self):

        localctx = ActorLangParser.ActorBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_actorBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.portDeclaration()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 38
                self.messageHandler()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PortDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PORT(self):
            return self.getToken(ActorLangParser.PORT, 0)

        def ASSIGN(self):
            return self.getToken(ActorLangParser.ASSIGN, 0)

        def INT_LITERAL(self):
            return self.getToken(ActorLangParser.INT_LITERAL, 0)

        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_portDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPortDeclaration" ):
                listener.enterPortDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPortDeclaration" ):
                listener.exitPortDeclaration(self)




    def portDeclaration(self):

        localctx = ActorLangParser.PortDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_portDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ActorLangParser.PORT)
            self.state = 45
            self.match(ActorLangParser.ASSIGN)
            self.state = 46
            self.match(ActorLangParser.INT_LITERAL)
            self.state = 47
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessageHandlerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(ActorLangParser.ON, 0)

        def STRING_LITERAL(self):
            return self.getToken(ActorLangParser.STRING_LITERAL, 0)

        def ARROW(self):
            return self.getToken(ActorLangParser.ARROW, 0)

        def LBRACE(self):
            return self.getToken(ActorLangParser.LBRACE, 0)

        def statements(self):
            return self.getTypedRuleContext(ActorLangParser.StatementsContext,0)


        def RBRACE(self):
            return self.getToken(ActorLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_messageHandler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessageHandler" ):
                listener.enterMessageHandler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessageHandler" ):
                listener.exitMessageHandler(self)




    def messageHandler(self):

        localctx = ActorLangParser.MessageHandlerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_messageHandler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ActorLangParser.ON)
            self.state = 50
            self.match(ActorLangParser.STRING_LITERAL)
            self.state = 51
            self.match(ActorLangParser.ARROW)
            self.state = 52
            self.match(ActorLangParser.LBRACE)
            self.state = 53
            self.statements()
            self.state = 54
            self.match(ActorLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ActorLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(ActorLangParser.StatementContext,i)


        def getRuleIndex(self):
            return ActorLangParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = ActorLangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 131356) != 0:
                self.state = 56
                self.statement()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendStatement(self):
            return self.getTypedRuleContext(ActorLangParser.SendStatementContext,0)


        def receiveStatement(self):
            return self.getTypedRuleContext(ActorLangParser.ReceiveStatementContext,0)


        def startStatement(self):
            return self.getTypedRuleContext(ActorLangParser.StartStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(ActorLangParser.AssignmentStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(ActorLangParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return ActorLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ActorLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.sendStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.receiveStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.startStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.assignmentStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.printStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SendStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEND(self):
            return self.getToken(ActorLangParser.SEND, 0)

        def LPAREN(self):
            return self.getToken(ActorLangParser.LPAREN, 0)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ActorLangParser.STRING_LITERAL)
            else:
                return self.getToken(ActorLangParser.STRING_LITERAL, i)

        def COMMA(self):
            return self.getToken(ActorLangParser.COMMA, 0)

        def IDENTIFIER(self):
            return self.getToken(ActorLangParser.IDENTIFIER, 0)

        def RPAREN(self):
            return self.getToken(ActorLangParser.RPAREN, 0)

        def TO(self):
            return self.getToken(ActorLangParser.TO, 0)

        def PORT(self):
            return self.getToken(ActorLangParser.PORT, 0)

        def INT_LITERAL(self):
            return self.getToken(ActorLangParser.INT_LITERAL, 0)

        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_sendStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendStatement" ):
                listener.enterSendStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendStatement" ):
                listener.exitSendStatement(self)




    def sendStatement(self):

        localctx = ActorLangParser.SendStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sendStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ActorLangParser.SEND)
            self.state = 70
            self.match(ActorLangParser.LPAREN)
            self.state = 71
            self.match(ActorLangParser.STRING_LITERAL)
            self.state = 72
            self.match(ActorLangParser.COMMA)
            self.state = 73
            self.match(ActorLangParser.IDENTIFIER)
            self.state = 74
            self.match(ActorLangParser.RPAREN)
            self.state = 75
            self.match(ActorLangParser.TO)
            self.state = 76
            self.match(ActorLangParser.STRING_LITERAL)
            self.state = 77
            self.match(ActorLangParser.PORT)
            self.state = 78
            self.match(ActorLangParser.INT_LITERAL)
            self.state = 79
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECEIVE(self):
            return self.getToken(ActorLangParser.RECEIVE, 0)

        def LPAREN(self):
            return self.getToken(ActorLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ActorLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_receiveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiveStatement" ):
                listener.enterReceiveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiveStatement" ):
                listener.exitReceiveStatement(self)




    def receiveStatement(self):

        localctx = ActorLangParser.ReceiveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_receiveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ActorLangParser.RECEIVE)
            self.state = 82
            self.match(ActorLangParser.LPAREN)
            self.state = 83
            self.match(ActorLangParser.RPAREN)
            self.state = 84
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(ActorLangParser.START, 0)

        def LPAREN(self):
            return self.getToken(ActorLangParser.LPAREN, 0)

        def STRING_LITERAL(self):
            return self.getToken(ActorLangParser.STRING_LITERAL, 0)

        def COMMA(self):
            return self.getToken(ActorLangParser.COMMA, 0)

        def IDENTIFIER(self):
            return self.getToken(ActorLangParser.IDENTIFIER, 0)

        def RPAREN(self):
            return self.getToken(ActorLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_startStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartStatement" ):
                listener.enterStartStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartStatement" ):
                listener.exitStartStatement(self)




    def startStatement(self):

        localctx = ActorLangParser.StartStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_startStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ActorLangParser.START)
            self.state = 87
            self.match(ActorLangParser.LPAREN)
            self.state = 88
            self.match(ActorLangParser.STRING_LITERAL)
            self.state = 89
            self.match(ActorLangParser.COMMA)
            self.state = 90
            self.match(ActorLangParser.IDENTIFIER)
            self.state = 91
            self.match(ActorLangParser.RPAREN)
            self.state = 92
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ActorLangParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ActorLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ActorLangParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = ActorLangParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ActorLangParser.IDENTIFIER)
            self.state = 95
            self.match(ActorLangParser.ASSIGN)
            self.state = 96
            self.expression()
            self.state = 97
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ActorLangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(ActorLangParser.LPAREN, 0)

        def STRING_LITERAL(self):
            return self.getToken(ActorLangParser.STRING_LITERAL, 0)

        def RPAREN(self):
            return self.getToken(ActorLangParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ActorLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = ActorLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ActorLangParser.PRINT)
            self.state = 100
            self.match(ActorLangParser.LPAREN)
            self.state = 101
            self.match(ActorLangParser.STRING_LITERAL)
            self.state = 102
            self.match(ActorLangParser.RPAREN)
            self.state = 103
            self.match(ActorLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ActorLangParser.STRING_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(ActorLangParser.IDENTIFIER, 0)

        def INT_LITERAL(self):
            return self.getToken(ActorLangParser.INT_LITERAL, 0)

        def getRuleIndex(self):
            return ActorLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ActorLangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





