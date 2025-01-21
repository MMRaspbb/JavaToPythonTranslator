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


    # Visit a parse tree produced by JavaGrammarParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:JavaGrammarParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classBody.
    def visitClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:JavaGrammarParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JavaGrammarParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeType.
    def visitTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JavaGrammarParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JavaGrammarParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JavaGrammarParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JavaGrammarParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:JavaGrammarParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#primitiveType.
    def visitPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#identifier.
    def visitIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#expression.
    def visitExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#creator.
    def visitCreator(self, ctx:JavaGrammarParser.CreatorContext):
        return self.visitChildren(ctx)



del JavaGrammarParser