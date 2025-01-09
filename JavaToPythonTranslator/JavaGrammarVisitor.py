# Generated from JavaGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JavaGrammarParser import JavaGrammarParser
else:
    from JavaGrammarParser import JavaGrammarParser

# This class defines a complete generic visitor for a parse tree produced by JavaGrammarParser.

class JavaGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaGrammarParser#compilationUnit.
    def visitCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#statement.
    def visitStatement(self, ctx:JavaGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#expression.
    def visitExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)



del JavaGrammarParser