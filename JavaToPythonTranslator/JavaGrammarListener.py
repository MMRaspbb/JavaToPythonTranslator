# Generated from JavaGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JavaGrammarParser import JavaGrammarParser
else:
    from JavaGrammarParser import JavaGrammarParser

# This class defines a complete listener for a parse tree produced by JavaGrammarParser.
class JavaGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by JavaGrammarParser#compilationUnit.
    def enterCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#compilationUnit.
    def exitCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#statement.
    def enterStatement(self, ctx:JavaGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#statement.
    def exitStatement(self, ctx:JavaGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#expression.
    def enterExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#expression.
    def exitExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        pass



del JavaGrammarParser