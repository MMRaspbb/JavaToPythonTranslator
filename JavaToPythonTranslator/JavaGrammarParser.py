# Generated from JavaGrammar.g4 by ANTLR 4.13.0
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
        4,1,14,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,1,4,3,4,53,8,4,1,4,0,0,
        5,0,2,4,6,8,0,0,54,0,10,1,0,0,0,2,12,1,0,0,0,4,23,1,0,0,0,6,45,1,
        0,0,0,8,52,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,13,5,9,0,0,13,14,
        5,11,0,0,14,18,5,1,0,0,15,17,3,4,2,0,16,15,1,0,0,0,17,20,1,0,0,0,
        18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,
        2,0,0,22,3,1,0,0,0,23,24,5,10,0,0,24,25,5,11,0,0,25,26,5,3,0,0,26,
        27,5,4,0,0,27,31,5,1,0,0,28,30,3,6,3,0,29,28,1,0,0,0,30,33,1,0,0,
        0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,
        5,2,0,0,35,5,1,0,0,0,36,37,3,8,4,0,37,38,5,5,0,0,38,46,1,0,0,0,39,
        40,5,6,0,0,40,41,5,3,0,0,41,42,3,8,4,0,42,43,5,4,0,0,43,44,5,5,0,
        0,44,46,1,0,0,0,45,36,1,0,0,0,45,39,1,0,0,0,46,7,1,0,0,0,47,48,5,
        11,0,0,48,49,5,7,0,0,49,53,3,8,4,0,50,53,5,11,0,0,51,53,5,8,0,0,
        52,47,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,9,1,0,0,0,4,18,31,45,
        52
    ]

class JavaGrammarParser ( Parser ):

    grammarFileName = "JavaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "';'", "'System.out.println'", 
                     "'='", "<INVALID>", "'class'", "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Literal", "CLASS", "VOID", "Identifier", "INT", "STRING", 
                      "WS" ]

    RULE_compilationUnit = 0
    RULE_classDeclaration = 1
    RULE_methodDeclaration = 2
    RULE_statement = 3
    RULE_expression = 4

    ruleNames =  [ "compilationUnit", "classDeclaration", "methodDeclaration", 
                   "statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Literal=8
    CLASS=9
    VOID=10
    Identifier=11
    INT=12
    STRING=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(JavaGrammarParser.ClassDeclarationContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = JavaGrammarParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.classDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(JavaGrammarParser.CLASS, 0)

        def Identifier(self):
            return self.getToken(JavaGrammarParser.Identifier, 0)

        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = JavaGrammarParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(JavaGrammarParser.CLASS)
            self.state = 13
            self.match(JavaGrammarParser.Identifier)
            self.state = 14
            self.match(JavaGrammarParser.T__0)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 15
                self.methodDeclaration()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(JavaGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(JavaGrammarParser.VOID, 0)

        def Identifier(self):
            return self.getToken(JavaGrammarParser.Identifier, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = JavaGrammarParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(JavaGrammarParser.VOID)
            self.state = 24
            self.match(JavaGrammarParser.Identifier)
            self.state = 25
            self.match(JavaGrammarParser.T__2)
            self.state = 26
            self.match(JavaGrammarParser.T__3)
            self.state = 27
            self.match(JavaGrammarParser.T__0)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2368) != 0):
                self.state = 28
                self.statement()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(JavaGrammarParser.T__1)
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

        def expression(self):
            return self.getTypedRuleContext(JavaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JavaGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.expression()
                self.state = 37
                self.match(JavaGrammarParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(JavaGrammarParser.T__5)
                self.state = 40
                self.match(JavaGrammarParser.T__2)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(JavaGrammarParser.T__3)
                self.state = 43
                self.match(JavaGrammarParser.T__4)
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(JavaGrammarParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(JavaGrammarParser.ExpressionContext,0)


        def Literal(self):
            return self.getToken(JavaGrammarParser.Literal, 0)

        def getRuleIndex(self):
            return JavaGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = JavaGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(JavaGrammarParser.Identifier)
                self.state = 48
                self.match(JavaGrammarParser.T__6)
                self.state = 49
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(JavaGrammarParser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(JavaGrammarParser.Literal)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





