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
        4,1,26,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,5,0,39,8,0,10,0,
        12,0,42,9,0,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,2,1,2,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,5,5,63,8,5,10,5,12,5,66,9,5,1,5,
        1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,81,8,9,10,9,
        12,9,84,9,9,1,10,1,10,1,10,3,10,89,8,10,1,11,1,11,1,11,5,11,94,8,
        11,10,11,12,11,97,9,11,1,12,1,12,3,12,101,8,12,1,13,1,13,1,13,1,
        13,5,13,107,8,13,10,13,12,13,110,9,13,1,13,3,13,113,8,13,3,13,115,
        8,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,3,16,125,8,16,1,17,
        1,17,1,17,5,17,130,8,17,10,17,12,17,133,9,17,1,17,0,0,18,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,1,0,10,14,1,0,17,24,
        129,0,40,1,0,0,0,2,46,1,0,0,0,4,51,1,0,0,0,6,53,1,0,0,0,8,57,1,0,
        0,0,10,64,1,0,0,0,12,69,1,0,0,0,14,71,1,0,0,0,16,75,1,0,0,0,18,77,
        1,0,0,0,20,85,1,0,0,0,22,90,1,0,0,0,24,100,1,0,0,0,26,102,1,0,0,
        0,28,118,1,0,0,0,30,120,1,0,0,0,32,124,1,0,0,0,34,126,1,0,0,0,36,
        39,3,2,1,0,37,39,5,1,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,42,1,0,0,
        0,40,38,1,0,0,0,40,41,1,0,0,0,41,1,1,0,0,0,42,40,1,0,0,0,43,45,3,
        4,2,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,
        49,1,0,0,0,48,46,1,0,0,0,49,50,3,6,3,0,50,3,1,0,0,0,51,52,7,0,0,
        0,52,5,1,0,0,0,53,54,5,9,0,0,54,55,3,30,15,0,55,56,3,8,4,0,56,7,
        1,0,0,0,57,58,5,2,0,0,58,59,3,10,5,0,59,60,5,3,0,0,60,9,1,0,0,0,
        61,63,3,4,2,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,3,12,6,0,68,11,1,0,0,0,69,
        70,3,14,7,0,70,13,1,0,0,0,71,72,3,16,8,0,72,73,3,18,9,0,73,74,5,
        1,0,0,74,15,1,0,0,0,75,76,3,28,14,0,76,17,1,0,0,0,77,82,3,20,10,
        0,78,79,5,4,0,0,79,81,3,20,10,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,
        1,0,0,0,82,83,1,0,0,0,83,19,1,0,0,0,84,82,1,0,0,0,85,88,3,22,11,
        0,86,87,5,5,0,0,87,89,3,24,12,0,88,86,1,0,0,0,88,89,1,0,0,0,89,21,
        1,0,0,0,90,95,3,30,15,0,91,92,5,6,0,0,92,94,5,7,0,0,93,91,1,0,0,
        0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,23,1,0,0,0,97,95,
        1,0,0,0,98,101,3,26,13,0,99,101,3,32,16,0,100,98,1,0,0,0,100,99,
        1,0,0,0,101,25,1,0,0,0,102,114,5,2,0,0,103,108,3,24,12,0,104,105,
        5,4,0,0,105,107,3,24,12,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,113,
        5,4,0,0,112,111,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,103,
        1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,117,5,3,0,0,117,27,1,
        0,0,0,118,119,7,1,0,0,119,29,1,0,0,0,120,121,5,25,0,0,121,31,1,0,
        0,0,122,125,3,34,17,0,123,125,3,30,15,0,124,122,1,0,0,0,124,123,
        1,0,0,0,125,33,1,0,0,0,126,127,5,16,0,0,127,131,3,16,8,0,128,130,
        5,8,0,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,35,1,0,0,0,133,131,1,0,0,0,13,38,40,46,64,82,88,95,100,
        108,112,114,124,131
    ]

class JavaGrammarParser ( Parser ):

    grammarFileName = "JavaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "','", "'='", "'['", 
                     "']'", "'[]'", "'class'", "'public'", "'protected'", 
                     "'private'", "'static'", "'abstract'", "'final'", "'new'", 
                     "'boolean'", "'char'", "'byte'", "'short'", "'int'", 
                     "'long'", "'float'", "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CLASS", "PUBLIC", "PROTECTED", "PRIVATE", 
                      "STATIC", "ABSTRACT", "FINAL", "NEW", "BOOLEAN", "CHAR", 
                      "BYTE", "SHORT", "INT", "LONG", "FLOAT", "DOUBLE", 
                      "IDENTIFIER", "WS" ]

    RULE_compilationUnit = 0
    RULE_typeDeclaration = 1
    RULE_classOrInterfaceModifier = 2
    RULE_classDeclaration = 3
    RULE_classBody = 4
    RULE_classBodyDeclaration = 5
    RULE_memberDeclaration = 6
    RULE_fieldDeclaration = 7
    RULE_typeType = 8
    RULE_variableDeclarators = 9
    RULE_variableDeclarator = 10
    RULE_variableDeclaratorId = 11
    RULE_variableInitializer = 12
    RULE_arrayInitializer = 13
    RULE_primitiveType = 14
    RULE_identifier = 15
    RULE_expression = 16
    RULE_creator = 17

    ruleNames =  [ "compilationUnit", "typeDeclaration", "classOrInterfaceModifier", 
                   "classDeclaration", "classBody", "classBodyDeclaration", 
                   "memberDeclaration", "fieldDeclaration", "typeType", 
                   "variableDeclarators", "variableDeclarator", "variableDeclaratorId", 
                   "variableInitializer", "arrayInitializer", "primitiveType", 
                   "identifier", "expression", "creator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    CLASS=9
    PUBLIC=10
    PROTECTED=11
    PRIVATE=12
    STATIC=13
    ABSTRACT=14
    FINAL=15
    NEW=16
    BOOLEAN=17
    CHAR=18
    BYTE=19
    SHORT=20
    INT=21
    LONG=22
    FLOAT=23
    DOUBLE=24
    IDENTIFIER=25
    WS=26

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

        def typeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.TypeDeclarationContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.TypeDeclarationContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32258) != 0):
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [9, 10, 11, 12, 13, 14]:
                    self.state = 36
                    self.typeDeclaration()
                    pass
                elif token in [1]:
                    self.state = 37
                    self.match(JavaGrammarParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(JavaGrammarParser.ClassDeclarationContext,0)


        def classOrInterfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.ClassOrInterfaceModifierContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.ClassOrInterfaceModifierContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_typeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDeclaration" ):
                listener.enterTypeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDeclaration" ):
                listener.exitTypeDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDeclaration" ):
                return visitor.visitTypeDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typeDeclaration(self):

        localctx = JavaGrammarParser.TypeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typeDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                self.state = 43
                self.classOrInterfaceModifier()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.classDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassOrInterfaceModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(JavaGrammarParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(JavaGrammarParser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(JavaGrammarParser.PRIVATE, 0)

        def STATIC(self):
            return self.getToken(JavaGrammarParser.STATIC, 0)

        def ABSTRACT(self):
            return self.getToken(JavaGrammarParser.ABSTRACT, 0)

        def getRuleIndex(self):
            return JavaGrammarParser.RULE_classOrInterfaceModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassOrInterfaceModifier" ):
                listener.enterClassOrInterfaceModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassOrInterfaceModifier" ):
                listener.exitClassOrInterfaceModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassOrInterfaceModifier" ):
                return visitor.visitClassOrInterfaceModifier(self)
            else:
                return visitor.visitChildren(self)




    def classOrInterfaceModifier(self):

        localctx = JavaGrammarParser.ClassOrInterfaceModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classOrInterfaceModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
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


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(JavaGrammarParser.CLASS, 0)

        def identifier(self):
            return self.getTypedRuleContext(JavaGrammarParser.IdentifierContext,0)


        def classBody(self):
            return self.getTypedRuleContext(JavaGrammarParser.ClassBodyContext,0)


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
        self.enterRule(localctx, 6, self.RULE_classDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(JavaGrammarParser.CLASS)
            self.state = 54
            self.identifier()
            self.state = 55
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classBodyDeclaration(self):
            return self.getTypedRuleContext(JavaGrammarParser.ClassBodyDeclarationContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = JavaGrammarParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(JavaGrammarParser.T__1)
            self.state = 58
            self.classBodyDeclaration()
            self.state = 59
            self.match(JavaGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberDeclaration(self):
            return self.getTypedRuleContext(JavaGrammarParser.MemberDeclarationContext,0)


        def classOrInterfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.ClassOrInterfaceModifierContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.ClassOrInterfaceModifierContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_classBodyDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBodyDeclaration" ):
                listener.enterClassBodyDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBodyDeclaration" ):
                listener.exitClassBodyDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyDeclaration" ):
                return visitor.visitClassBodyDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classBodyDeclaration(self):

        localctx = JavaGrammarParser.ClassBodyDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classBodyDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                self.state = 61
                self.classOrInterfaceModifier()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.memberDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(JavaGrammarParser.FieldDeclarationContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_memberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDeclaration" ):
                listener.enterMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDeclaration" ):
                listener.exitMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberDeclaration" ):
                return visitor.visitMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def memberDeclaration(self):

        localctx = JavaGrammarParser.MemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_memberDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.fieldDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self):
            return self.getTypedRuleContext(JavaGrammarParser.TypeTypeContext,0)


        def variableDeclarators(self):
            return self.getTypedRuleContext(JavaGrammarParser.VariableDeclaratorsContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_fieldDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclaration" ):
                listener.enterFieldDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclaration" ):
                listener.exitFieldDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclaration" ):
                return visitor.visitFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclaration(self):

        localctx = JavaGrammarParser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fieldDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.typeType()
            self.state = 72
            self.variableDeclarators()
            self.state = 73
            self.match(JavaGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(JavaGrammarParser.PrimitiveTypeContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_typeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeType" ):
                listener.enterTypeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeType" ):
                listener.exitTypeType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeType" ):
                return visitor.visitTypeType(self)
            else:
                return visitor.visitChildren(self)




    def typeType(self):

        localctx = JavaGrammarParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.primitiveType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.VariableDeclaratorContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_variableDeclarators

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarators" ):
                listener.enterVariableDeclarators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarators" ):
                listener.exitVariableDeclarators(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarators" ):
                return visitor.visitVariableDeclarators(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarators(self):

        localctx = JavaGrammarParser.VariableDeclaratorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDeclarators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.variableDeclarator()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 78
                self.match(JavaGrammarParser.T__3)
                self.state = 79
                self.variableDeclarator()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaratorId(self):
            return self.getTypedRuleContext(JavaGrammarParser.VariableDeclaratorIdContext,0)


        def variableInitializer(self):
            return self.getTypedRuleContext(JavaGrammarParser.VariableInitializerContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = JavaGrammarParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.variableDeclaratorId()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 86
                self.match(JavaGrammarParser.T__4)
                self.state = 87
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(JavaGrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_variableDeclaratorId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorId" ):
                listener.enterVariableDeclaratorId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorId" ):
                listener.exitVariableDeclaratorId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaratorId" ):
                return visitor.visitVariableDeclaratorId(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaratorId(self):

        localctx = JavaGrammarParser.VariableDeclaratorIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableDeclaratorId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.identifier()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 91
                self.match(JavaGrammarParser.T__5)
                self.state = 92
                self.match(JavaGrammarParser.T__6)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayInitializer(self):
            return self.getTypedRuleContext(JavaGrammarParser.ArrayInitializerContext,0)


        def expression(self):
            return self.getTypedRuleContext(JavaGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_variableInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializer" ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializer" ):
                listener.exitVariableInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableInitializer" ):
                return visitor.visitVariableInitializer(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializer(self):

        localctx = JavaGrammarParser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variableInitializer)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.arrayInitializer()
                pass
            elif token in [16, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.expression()
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


    class ArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableInitializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaGrammarParser.VariableInitializerContext)
            else:
                return self.getTypedRuleContext(JavaGrammarParser.VariableInitializerContext,i)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_arrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInitializer" ):
                listener.enterArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInitializer" ):
                listener.exitArrayInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInitializer" ):
                return visitor.visitArrayInitializer(self)
            else:
                return visitor.visitChildren(self)




    def arrayInitializer(self):

        localctx = JavaGrammarParser.ArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(JavaGrammarParser.T__1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33619972) != 0):
                self.state = 103
                self.variableInitializer()
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 104
                        self.match(JavaGrammarParser.T__3)
                        self.state = 105
                        self.variableInitializer() 
                    self.state = 110
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 111
                    self.match(JavaGrammarParser.T__3)




            self.state = 116
            self.match(JavaGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(JavaGrammarParser.BOOLEAN, 0)

        def CHAR(self):
            return self.getToken(JavaGrammarParser.CHAR, 0)

        def BYTE(self):
            return self.getToken(JavaGrammarParser.BYTE, 0)

        def SHORT(self):
            return self.getToken(JavaGrammarParser.SHORT, 0)

        def INT(self):
            return self.getToken(JavaGrammarParser.INT, 0)

        def LONG(self):
            return self.getToken(JavaGrammarParser.LONG, 0)

        def FLOAT(self):
            return self.getToken(JavaGrammarParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(JavaGrammarParser.DOUBLE, 0)

        def getRuleIndex(self):
            return JavaGrammarParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = JavaGrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33423360) != 0)):
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JavaGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return JavaGrammarParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = JavaGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(JavaGrammarParser.IDENTIFIER)
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

        def creator(self):
            return self.getTypedRuleContext(JavaGrammarParser.CreatorContext,0)


        def identifier(self):
            return self.getTypedRuleContext(JavaGrammarParser.IdentifierContext,0)


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
        self.enterRule(localctx, 32, self.RULE_expression)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.creator()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.identifier()
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


    class CreatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(JavaGrammarParser.NEW, 0)

        def typeType(self):
            return self.getTypedRuleContext(JavaGrammarParser.TypeTypeContext,0)


        def getRuleIndex(self):
            return JavaGrammarParser.RULE_creator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreator" ):
                listener.enterCreator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreator" ):
                listener.exitCreator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreator" ):
                return visitor.visitCreator(self)
            else:
                return visitor.visitChildren(self)




    def creator(self):

        localctx = JavaGrammarParser.CreatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_creator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(JavaGrammarParser.NEW)
            self.state = 127
            self.typeType()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 128
                self.match(JavaGrammarParser.T__7)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





